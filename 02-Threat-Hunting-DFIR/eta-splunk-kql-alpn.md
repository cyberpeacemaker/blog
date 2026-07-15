---
title: "ETA Splunk KQL ALPN"
description: "Collects Splunk, KQL, and ALPN query ideas for encrypted traffic analysis."
created: 2026-07-15 21:07
updated: 2026-07-15
type: reference
lang: zh
status: draft
tags: [threat-hunting, eta, c2]
---

> Related: [[MOC - Threat Hunting]] · [[eta-threat-hunting-overview]] · [[beacon]]

# ETA Splunk KQL ALPN
既然你胃口大開，那我們今天就把威脅獵人的「終極武器庫」全部搬出來！

當傳統的特徵碼（Signatures）失效時，ETA（加密流量分析）就是獵人手中的顯微鏡。接下來，我們將從**實戰偵測語法（Splunk/KQL）**、**攻擊者的規避策略與反制**，以及 **TLS 握手中的隱藏細節**三個維度，帶你進入更深層的狩獵世界。

### 實戰演練：寫出你的第一個 ETA 獵捕語法

在實際企業環境中，你不可能手動去點看每個封包。我們必須利用 SIEM（如 Splunk 或 Microsoft Sentinel）來自動篩選出「長得不正常的加密連線」。

#### 1. Splunk 語法：尋找偽裝成合法服務的 JA3 指紋異常

這個語法專門用來抓出「連線去往 Telegram / Discord 等合法 SaaS，但發起客戶端根本不是瀏覽器或官方 App」的異常行為。

Splunk SPL

```
index=network sourcetype=zeek_ssl
| fields src_ip, dest_ip, server_name, ja3
| lookup ja3_legitimate_browser_list.csv ja3 OUTPUT browser_name
| lookup suspected_c2_ja3.csv ja3 OUTPUT is_malicious, malware_family
| eval is_anomaly = if(isnull(browser_name) AND (server_name="api.telegram.org" OR server_name="discord.com" OR server_name="slack.com"), "Yes", "No")
| stats count, values(browser_name) as client_identity by src_ip, dest_ip, server_name, ja3, is_anomaly, is_malicious, malware_family
| search is_anomaly="Yes" OR is_malicious="true"
| table src_ip, dest_ip, server_name, ja3, client_identity, malware_family, count
```

> **獵人筆記：** 此語法比對了「合法瀏覽器 JA3 白名單」。如果連線目的地是 Telegram，但其 JA3 指紋卻不在白名單內（表示不是 Chrome/Firefox/Safari 等），就會被判定為 `is_anomaly="Yes"` 並立案調查。

#### 2. KQL (Microsoft Sentinel) 語法：利用封包長度標準差尋找 C2 心跳 (Beaconing)

當惡意程式與 C2 進行心跳連線時，因為是自動化腳本，每次傳輸的封包大小都非常固定（標準差極小）。

Code snippet

```
let TimeWindow = 2h;
let MinConnections = 30;
let MaxStdDev = 10; // 封包大小的標準差小於 10 字节，代表極度均勻，非常人工
CommonSecurityLog
| where TimeGenerated > ago(TimeWindow)
| where DestinationPort == 443
| summarize
    ConnectionCount = count(),
    AvgPayload = avg(SentBytes),
    StdDevPayload = stdev(SentBytes),
    MinPayload = min(SentBytes),
    MaxPayload = max(SentBytes)
    by SourceIP, DestinationIP
| where ConnectionCount > MinConnections and StdDevPayload < MaxStdDev
| project SourceIP, DestinationIP, ConnectionCount, AvgPayload, StdDevPayload
| order by StdDevPayload asc
```

> **獵人筆記：** 正常的網頁瀏覽，封包大小標準差動輒數千。如果一個連線在 2 小時內連了 30 次以上，且 `StdDevPayload`（傳送位元組標準差）小於 10，代表這是一台極度規律的機器人在跟外網通訊。

### 貓鼠遊戲：攻擊者的 ETA 規避手法 vs 獵人的反制策略

威脅狩獵是一場持續的智力對決。當攻擊者知道我們在使用 ETA 時，他們會用更狡猾的招式，而我們也有對應的破解之道：

#### 攻擊者招式 A：JA3 指紋隨機化與偽裝 (Fingerprint Spoofing)

- **攻擊手法：** 攻擊者使用如 `uTLS` 等開源函式庫，動態模擬 Chrome 的 TLS Client Hello 特徵，甚至在每次連線時，隨機排列密碼套件（Cipher Suites）與擴充套件，讓獵人的 JA3 靜態特徵碼完全失效。

- **獵人反制：JA3S + JARM 聯防**

    - 雖然 Client 端的指紋一直在變，但 **C2 伺服器的反應（JA3S）** 往往因為後端作業系統或 C2 框架的限制而難以隨機化。

    - **JARM（主動 TLS 側寫）：** 獵人可以主動向可疑目標發送 10 個精心設計的 TLS 探針。不論客戶端怎麼變，C2 伺服器對這 10 個探針的回應組合（JARM 雜湊值）是唯一的。如果發現一台主機的 TLS 客戶端特徵天天在變，但它連過去的伺服器 JARM 指紋卻恆等於 Cobalt Strike，警報器就該響了。


#### 攻擊者招式 B：流量填充與整形 (Traffic Padding)

- **攻擊手法：** 為了混淆 SPLT（封包長度與時間序列），惡意程式在發送的每個加密封包尾端，塞入隨機長度的垃圾資料（Padding），讓封包大小看起來毫無規律，偽裝成人類在瀏覽網頁。

- **獵人反制：TCP 連線首包分析（First-Packet Size）與 TCP 視窗大小**

    - 雖然攻擊者可以填充後續的資料封包，但他們很難對 **TLS 握手階段（Handshake）** 的封包進行任意填充，因為握手協議有嚴格的格式規定。

    - 此外，觀察 `TCP Window Size` 的變化，通常自動化程式的視窗控制機制與現代瀏覽器的複雜擁塞控制（Congestion Control）有著顯著的統計學差異。


### 隱藏在 TLS 握手中的無聲告密者：ALPN

在 TLS 握手過程中，有一個常被忽略但極具價值的欄位：**ALPN（應用層協定協商，Application-Layer Protocol Negotiation）**。

ALPN 是客戶端用來告訴伺服器「我們在加密通道建立後，底層要用什麼協定溝通」的明文欄位（例如 `h2` 代表 HTTP/2，`http/1.1` 代表舊版網頁）。

```
Client Hello (明文) ──>  [ 我支援的 ALPN: h2, http/1.1 ]
Server Hello (明文) <──  [ 決定使用: h2 ]
```

#### 獵人的 ALPN 異常清單：

1. **ALPN 缺失（No ALPN）：** 現代瀏覽器為了優化效能，100% 會帶上 ALPN 欄位。如果你在 Port 443 看到一個**完全沒有 ALPN** 的 TLS 握手連線，這通常是舊型的自建 C2、未經優化的自動化惡意腳本（如某些 Python 舊庫）或某些粗糙的 VPN 隧道。

2. **ALPN 錯配：** 例如協商了 `h2` (HTTP/2)，但在加密建立後，獵人觀察到該連線完全沒有 HTTP/2 的「多路復用」特徵（一個 TCP 連線內同時跑多個 Request），反而呈現單一線性的、慢速的資料傳輸。這代表攻擊者只是「掛羊頭賣狗肉」，用 HTTP/2 的名義來包裹自定義的 C2 協議。


### 威脅獵人的進階思維

ETA 的本質，其實是「尋找不協調感（Incongruity）」。

- 一個合法的瀏覽器，為什麼會向一個沒有網域名稱、只有臨時 IP 的伺服器發起連線？

- 一個合法的 HTTPS 加密通道，為什麼在 24 小時內，封包大小的變化量趨近於零？

- 一台財務部的電腦，為什麼會突然使用一個只有開源駭客工具才會使用的 SSH 指紋（HASSH）向外連線？


當我們不再執著於「看見內容」，而是學會「觀察行為與特徵」，加密流量在獵人眼裡，就跟明文一樣無所遁形。

看完這些更進階的攻防與語法，**你覺得哪一個部分最讓你感到驚奇？** 是利用「標準差」來盲測 C2 心跳，還是「ALPN」這種握手階段的無聲告密者？

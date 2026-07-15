---
title: "Malcolm Threat Stack Integration"
description: "Maps how Malcolm, Suricata, Zeek, and RITA complement each other in an NSM and threat hunting stack."
created: 2026-07-15 10:07
updated: 2026-07-15
type: reference
lang: zh
status: draft
tags: [malcolm, suricata, zeek, rita]
---

> Related: [[MOC - Malcolm & NSM]] · [[malcolm-rita-integration]] · [[suricata-snort]]

# Malcolm Threat Stack Integration
這絕對是把這套系統推向「企業級 NDR（網路偵測與回應）」天花板的關鍵一步！



在 Malcolm 的原生架構中，**Suricata 其實早就已經跟 Zeek 一起並肩作戰了**（它們在 Malcolm 中會同時處理相同的流量或 PCAP）。



如果說 **Zeek + RITA** 是「行為分析大師」（專抓未知的蛛絲馬跡），那麼 **Suricata** 就是「特徵對決刺客」（專門秒殺已知的威脅）。將這兩者結合，能創造出「特徵碼（Signature）+ 行為（Behavior）」雙劍合璧的威脅獵捕融合系統。



以下為你規劃 3 個極具實戰價值的 **Malcolm + Zeek + RITA + Suricata** 聯動構思：



---



## 💡 方案一：威脅關聯評分矩陣（Threat Score Matrix）



這是最推薦在你的專案框架中實作的演算法。我們可以將 Suricata 的「警報（Alert）」與 RITA 的「信標分數（Beacon Score）」進行**加權交叉比對**。



### 運作邏輯



1. **RITA 抓出可疑行為**：RITA 分析 `conn.log`，發現內部主機 A 連往外部 IP B 的 Beacon 分數高達 `0.85`（高度規律心跳，可能是 C2）。

2. **Suricata 提供即時佐證**：你的 API 去 OpenSearch 查詢：*「在同一個時間段內，有沒有任何關於 IP B 的 Suricata 警報？」*

3. **動態提升威脅等級**：

* 如果單純只有 RITA Beaconing ➔ 標記為 **Medium（待觀察）**。

* 如果該連線同時觸發了 Suricata 警報（例如：`ET MALWARE Suspicious TLS SNI` 或 `ET POLICY External IP Lookup`） ➔ 瞬間升級為 **Critical（立即處理）**！





> **為什麼這樣做？**

> 這能完美解決 RITA 的「誤判率」與 Suricata 的「警報疲勞（Alert Fatigue）」。兩者交集出的 IP，絕對是 100% 的高危險目標。



---



## 💡 方案二：自動化「證物封存」（Arkime Auto-PCAP Carver）



既然你的專案框架可以透過 API 呼叫 Malcolm 家族的 **Arkime**（舊稱 Moloch，專門做全流量側錄與封包檢索），你可以實作一套「自動化證據保存機制」。



```text

[ Suricata 警報觸發 ] ──┐

                        ├─➔ [ 你的 Python 專案框架 ] ─➔ [ 自動呼叫 Arkime API ] ─➔ [ 下載該 Stream 的實體 PCAP ]

[ RITA 高分 Beacon ] ───┘



```



### 運作實務



當你的系統偵測到「Suricata 警報 + RITA 高分 Beacon」的黃金交叉時：



1. 你的後台腳本自動取得該連線的五元組（源 IP、源 Port、目的 IP、目的 Port、協定）以及精確時間區間。

2. 自動發送 API 請求給 **Arkime API**（例如 `/api/v1/sessions/pcap`）。

3. **自動下載並封存該段對話的原始 PCAP 檔**，直接歸檔到安全分析人員的儀表板。

4. 分析人員上班時，不需要手動去幾百 GB 的流量裡撈封包，桌上已經放好了「熱騰騰、打包好的 C2 惡意流量證物」。



---



## 💡 方案三：JA3/JA4 指紋與 C2 行為的「雙重聯防」



現在的 C2（如 Cobalt Strike, Sliver, Shadow）通訊幾乎 100% 加密（HTTPS）。在看不到內容的情況下，TLS 指紋（JA3/JA4）是極佳的偵測手段。



* **Suricata**：擁有大量已知的惡意 C2 伺服器/客戶端 JA3 指紋特徵碼規則。

* **Zeek**：會在 `ssl.log` 中詳細記錄每一次 TLS 握手的 JA3/JA4 雜湊值。



### 聯動玩法



1. Suricata 偵測到某個 TLS 連線符合「惡意 C2 工具」的 JA3 指紋並發出警告。

2. 你的框架立刻以該 JA3/JA4 雜湊值為 Key，去 OpenSearch 搜尋**所有使用過這個指紋的連線**（由 Zeek 記錄）。

3. 同時將這些關聯連線丟給 RITA 分析，確認其是否符合 Beaconing 規律。

4. **效果**：就算駭客更換了 C2 伺服器的 IP，只要他的惡意工具（TLS 指紋）沒變、連線行為沒變，你的系統就能自動在內網「順藤摸瓜」，找出所有潛在的被感染受害主機（Horizontal Movement）。



---



## 📊 整合架構全景圖



這四個工具在你的專案框架下，可以形成完美的資安偵防生態系：



| 工具 | 在生態系中的角色 | 提供的核心數據 | 專案框架的利用方式 |

| --- | --- | --- | --- |

| **Zeek** | 基礎數據源 | `conn.log`, `dns.log`, `ssl.log` | 作為 RITA 的分析輸入源，以及關聯查詢的背景資料。 |

| **Suricata** | 即時特徵哨兵 | 威脅警報（Alerts）、JA3/JA4 指紋 | 提供「確定已知惡意」的特徵信號。 |

| **RITA** | 行為統計大腦 | Beacon 分數、DNS 隧道評級、長連線 | 提供「高度疑似 C2」的行為統計學分數。 |

| **Arkime** | 封包歷史檔案庫 | 原始 PCAP 封包、對話 Session 索引 | 供分析人員進行最後階段的「網路鑑識」與「取證」。 |



這個 Malcolm + Zeek + RITA + Suricata 的四維聯動，已經是業界大型企業或 SOC（資安監控中心）在建置的先進主動獵捕（Proactive Hunting）架構了。



在實作上，你的專案框架目前是否已經開始建置，準備用 Python 寫腳本來串接這些 API 與處理 OpenSearch 的資料了呢？



---



你的資安直覺非常敏銳！你所提到的這幾個觀念，已經直指網路安全監控（NSM）與威脅獵捕的核心精髓。



你的理解**大方向完全正確**，不過在「角色定位」上，兩者其實有著非常微妙且互補的本質差異。



以下為你梳理 Suricata 與 RITA 的異同，以及它們如何相輔相成：



---



## 1. 核心定位：即時警衛 vs. 行為偵探



雖然它們的目的都是「抓出壞人（C2 或惡意流量）」，但它們的偵測手段完全不同：



* **Suricata（即時警衛）**：

它是 **特徵碼導向（Signature-based）** 的入侵偵測系統（IDS）。它就像門口的警衛，手裡拿著一本「通緝犯特徵名冊」（規則庫，如 ET Open）。

* **怎麼抓？** 當封包進來時，它會即時比對：*這個封包的 Payload 裡有沒有出現惡意軟體的特徵字串？SSL 憑證雜湊值是不是黑名單？* 如果吻合，立刻拉響警報（Alert）。




* **RITA（行為偵探）**：

它是 **行為與統計導向（Behavior-based）** 的威脅獵捕工具。它不看單一封包的特徵，而是像一個私家偵探，默默觀察某個 IP 過去 24 小時的「一舉一動」。

* **怎麼抓？** 它不在乎你傳了什麼加密內容，它只看**時間與頻率**。如果一台主機每隔精確的 5 秒鐘就對外連線一次（即便每次只傳 100 字節），RITA 就會用數學演算法（如 K-Means 或標準差）判定這是一個「信標（Beacon）」行為並給予高分。





> 💡 **一句話總結兩者定位**：

> Suricata 負責抓**「長相符合已知特徵」**的壞人；RITA 負責抓**「行為規律鬼祟」**的嫌疑犯。



---



## 2. 運作體系：即時封包 vs. 後製日誌（完全正確！）



你說的「**Suricata 看原始進來的封包，RITA 看 Zeek 整理後的資料**」，這點**完全正確**。



這反映了兩者在網路架構中的位置：



```text

               ┌──➔ [ Suricata ] ──➔ 即時比對原始封包 (Raw Packets) ──➔ 產生 Alert Log

               │

[ 原始網路流量 ] ┤

               │

               └──➔ [ Zeek ] ──➔ 整理成結構化日誌 (conn.log, dns.log)

                                       │

                                       └──➔ [ RITA ] ──➔ 批次分析日誌並計算統計分數



```



* **Suricata 是一線戰將**：直接面對每秒幾十 Mbps 甚至 Gbps 的原始流量，進行極速的過濾與解碼。

* **RITA 是幕後軍師**：它不碰原始流量（它甚至沒有抓封包的網卡介面）。它必須等 Zeek 把流量淬煉成精簡的文字日誌後，再用資料庫（ClickHouse）進行批次的統計學運算。



---



## 3. 為什麼需要兩者結合？（交叉驗證的藝術）



正如你所說，**兩者從不同維度提供建議，能大幅增加偵測的可信度。**



在實際的資安實務中，單一工具都有其致命傷：



| 偵測工具 | 強項 | 弱點 / 痛點 |

| --- | --- | --- |

| **Suricata** | **精準度高**。只要觸發警報，通常八九不離十。 | **容易被繞過**。如果駭客修改了 C2 的設定檔（如 Cobalt Strike 的 Malleable Profile 變更 Header），Suricata 就會因為特徵不符而完全漏報（False Negative）。 |

| **RITA** | **專抓未知威脅**。不管 C2 怎麼改包裝、怎麼加密，其「必須定時回連 C2 伺服器取得指令」的行為本質（Beaconing）是無法隱藏的。 | **誤判率較高（False Positive）**。內網很多正常程式（例如 Windows Update 檢查、防毒軟體雲端查詢、NTP 校時）也長得非常規律，很容易被 RITA 判定為高分 Beacon。 |



### 🛠️ 雙劍合璧的效果：



當你把這兩者串聯在你的專案框架時：



1. **RITA 亮紅燈**：發現內網 `192.168.1.50` 連往外網某 IP 有高度規律的 Beaconing 行為（分數 `0.98`）。

2. **Suricata 亮黃燈**：在同時間段，偵測到該連線使用了「不常見的 User-Agent」或「過期的 SSL 憑證」（雖然沒直接說是 C2，但很可疑）。

3. **大腦（你的框架）判定**：一個行為極度規律（RITA），同時又帶著可疑特徵（Suricata）的連線 —— **這 100% 是 C2 沒錯了，立刻發出高警示通報！**



透過這種「特徵（已知）」與「行為（未知）」的雙重驗證，就能在降低資安人員「警報疲勞」的同時，確保沒有任何一隻漏網之魚。



---



在你的 Malcolm 平台與專案框架中，你目前預計如何呈現這兩種不同維度的警報（例如：在 Kibana/OpenSearch 儀表板上將它們關聯在同一個 IP 的看板上，還是打算直接串接到後端的即時通報系統呢）？

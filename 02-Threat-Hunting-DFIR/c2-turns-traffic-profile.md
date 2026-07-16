---
title: "C2 Turns Traffic Profile"
description: "Connects Wireshark packet and stream turns to C2 traffic profiling for threat hunting."
created: 2026-07-15
updated: 2026-07-15
type: reference
lang: zh
status: draft
tags: [threat-hunting, dfir]
---

> Related: [[MOC - Threat Hunting]] · [[beacon]] · [[threat-hunting-c2-volume-beacon]]

# C2 Turns Traffic Profile
## Source: `Inbox/wireshark-stream-pkts-index-turn.md`

這是一個非常經典且重要的 Wireshark 觀念問題！這涉及到「底層網路傳輸」**與**「上層應用程式解讀」之間的差別。

以下為你詳細解析這兩個疑問：

## 1. `pkts` 與 `packets` 的關係是什麼？

- **它們是同一個詞！**

    `pkts` 單純只是 `packets`（封包）的**英文簡寫**（Abbreviation）。

    因此，`17 client pkts` 與 `17 client packets` 代表的是完全一樣的意思。


## 2. 為什麼主介面有 172 個封包，但追蹤視窗裡只有 33 個（17 + 16）？

你開啟的視窗標題是 **「Follow HTTP Stream」**（追蹤 HTTP 資料流）。Wireshark 在這個模式下，看的是「重組後的應用層（HTTP）資料」，而不是「網路上跑的所有原始 TCP 封包」。

導致數量對不上的主要原因有以下三個：

### ① 過濾掉了「不含資料」的 TCP 控制封包

在 TCP 連線中，有大量的封包**不攜帶任何實際的 HTTP 資料**，它們只負責維持連線的狀態。在「Follow Stream」視窗中，這些沒有 Payload（承載資料）的封包會被直接過濾掉、不計入統計。

- **連線建立**：三次握手（Three-way Handshake）的 `SYN`、`SYN-ACK`、`ACK`。

- **純確認封包（Pure ACKs）**：當 A 端傳資料給 B 端後，B 端回傳一個沒有資料的 `ACK` 封包來報平安。

- **連線中斷**：結束連線時的 `FIN`、`RST` 封包。


> 在你主畫面的 172 個封包中，很大一部分只是這類「不帶資料的工具包」。

### ② TCP 的重組（Reassembly）機制

- 網路傳輸有最大傳輸單元（MTU，通常為 1500 位元組）的限制。

- 如果伺服器要回傳一個 16 KB 的 HTTP 網頁資料（如你選單顯示的 Entire conversation 16 kB），它**無法**塞進單一個 TCP 封包裡，而是會被拆成大約 11~12 個獨立的 TCP 封包傳送。

- Wireshark 在呈現 「Follow HTTP Stream」時，會貼心地把這 12 個分段封包**重組（Reassemble）還原成 1 個完整的 HTTP 回應**。在 Follow 統計中，這 12 個原始封包就會被合併計算為 **1 個 server pkt**。


## 3. 從你的 YAML 截圖中尋找鐵證 🔍

如果你仔細觀察截圖中 YAML 格式的 `packet` 序號，就會發現它們是**跳號**的：

YAML

```
- packet: 1   # 用戶端傳送的第一個「有資料」的封包 (peer: 0)
- packet: 4   # 中間的 packet 2、3 沒出現（因為它們是沒有資料的純 ACK 或控制封包）
- packet: 9   # 伺服器端回傳的第一個「有資料」的封包 (peer: 1)
- packet: 15  # 下一個... 中間的 10~14 被重組或過濾掉了
```

這非常清楚地說明了兩者的差別：

> - **主視窗顯示的 172 packets**：是網路上跑的**所有原始 TCP 封包**（包含握手、純 ACK、被拆散的分段封包）。
>
> - **底部的 33 pkts（17 client + 16 server）**：是 Wireshark 幫你過濾與重組後，**真正含有 HTTP 應用層資料的「對話次數」**。
>

## Source: `Inbox/turns-threat-hunting.md`

這是一個**非常高階且敏銳的資安威脅獵捕（Threat Hunting）思維**！

答案是：**完全可以！**

在網路鑑識中，`turns`（輪轉次數）是一個用來評估連線是「機器自動化行為」還是「人類即時操作」的黃金指標。透過分析 `turns` 的數量、Payload 大小以及連線頻率，我們可以直接推論出以下幾種經典的 **C2（命令與控制）通訊模式**。

## 透過 `turns` 推論三種經典的 C2 模式

### 模式一：即時互動式命令（Interactive Shell / Hands-on-Keyboard）

- **數據特徵**：**極高的 `turns`**、中低密度的 Payload（通常每次只有幾十到幾百位元組）。

- **就像你的案例**：33 個封包，產生了 31 次 `turns`。這代表雙方幾乎是「我講一句、你回一句」，沒有任何一方連續發送多個資料包。

- **C2 行為推論**：這高度疑似**攻擊者正在進行即時的 Reverse Shell（反向 Shell）操作**。

    - 攻擊者（Server）輸入：`whoami`（1 轉）

    - 受害主機（Client）回傳：`NT AUTHORITY\SYSTEM`（2 轉）

    - 攻擊者輸入：`ipconfig`（3 轉）...

    - 這種「即時敲擊鍵盤並等待回應」的行為，會在單一連線中製造出極高比例的 `turns`。


### 模式二：定期心跳與信標（Beaconing / Heartbeat）

- **數據特徵**：**極低的 `turns`（通常只有 1 ~ 2 次）**、Payload 極小、且連線規律。

- **連線特徵**：每隔固定時間（例如 5 秒、60 秒，或帶有輕微隨機抖動 Jitter），客戶端就會發起一次新的 Stream。

- **C2 行為推論**：這是最經典的 **C2 Beacon（信標）** 運作方式（如 Cobalt Strike、Sliver 的預設 HTTP 模式）。

    - 受害主機每分鐘開啟一個 Stream 問：「有指令要執行嗎？」（Client 1 pkt）

    - C2 伺服器回覆：「沒事，繼續睡。」（Server 1 pkt）

    - 雙方講完，立刻斷開連線。整個連線可能只有 2 個封包、**1 次 turn**。


### 模式三：檔案下載與資料外洩（Staging / Exfiltration）

- **數據特徵**：**極低的 `turns`**、但其中一方的 **Payload 異常巨大**。

- **連線特徵**：

    - **工具下載（Staging）**：Client 發送一個小請求（1 turn），Server 瘋狂灌入好幾 MB 的惡意程式檔案（如 Mimikatz），在經過 TCP 重組後，Server 只有 1 個巨大的 PDU（1 turn）。

    - **資料外洩（Exfiltration）**：Client 開啟連線後，連續上傳好幾 MB 的壓縮檔，Server 只回傳一個 `HTTP 200 OK`。

- **C2 行為推論**：這屬於 C2 的階段性任務——**載入第二階段惡意程式（Stage 2 Payload）**，或是**敏感資料竊取外傳**。


## C2 行為特徵對照表 📊

為了方便你快速判斷，可以參考這張特徵對照表：

|**C2 通訊模式**|**Turns 數量**|**Payload 大小**|**連線持續時間 / 頻率**|**懷疑的駭客行為**|
|---|---|---|---|---|
|**互動式 Shell**|🔴 **極高** (接近封包數)|🟡 中~低 (每次僅數百 Bytes)|長連線 (Persistent)|駭客正在**現場下指令**、偵察內網。|
|**定期信標 (Beacon)**|🟢 **極低** (1~2 次)|🟢 極小|週期性發起 (如每 30 秒一次)|木馬程式在**定期確認**有無新任務。|
|**第二階段下載**|🟢 **極低** (1~2 次)|🔴 **極大** (數 MB，Server 端)|單次、快速結束|正在下載其他的惡意工具。|
|**資料外洩**|🟢 **極低** (1~2 次)|🔴 **極大** (數 MB，Client 端)|單次或分批大量傳輸|企業內部的機密檔案正在被偷走。|

## ⚠️ 威脅獵捕時的注意事項（避免誤判）

雖然 `turns` 很好用，但別忘了在真實世界中，也有**合法的流量**會長得很像 C2：

1. **即時通訊軟體 / 網頁**（如 LINE、Websocket 聊天室）：這類軟體因為需要即時傳輸文字，也會產生極高的 `turns`。

2. **API 輪詢（Polling）**：許多系統背景程式會一直向伺服器查詢有沒有新資料，行為與 Beaconing 極為相似。


> **資安專家的下一步**：
>
> 當你看到 31 次 turns 懷疑是互動式 C2 時，請記得看一下你的 **YAML data 內容**：
>
> - 內容是人類讀得懂的 `cmd.exe` 指令與主機回應嗎？
>
> - 還是雖然看不懂（二進制），但這些資料正持續往一個奇怪的外網 IP 傳送？
>
>     結合 `turns` 數據與實際內容，就能讓你的資安鑑識精準度大幅提升！
>

---
title: "Malcolm IT and OT Subnet Filters"
description: "Shows OpenSearch and Arkime filters for observing IT-to-OT and OT-to-IT subnet traffic in Malcolm."
created: 2026-07-16
updated: 2026-07-16
type: howto
lang: zh
status: draft
tags: [malcolm, nsm, opensearch, threat-hunting]
---

> Related: [[MOC - Malcolm & NSM]] · [[MOC - OpenSearch Querying]] · [[malcolm-opensearch-json-dsl]]

這一步非常關鍵！在 OT 安全（如 Purdue Model 普渡模型）的防禦架構中，IT 與 OT 之間的跨網段邊界（Boundary）通常是最需要嚴格審查的防線。

在 Malcolm 中，你可以透過多種方式下 Filter 來精準觀測這兩個網段之間的雙向或單向連線。以下為你整理在 **OpenSearch Dashboards（Kibana）** 語法，以及如果你切換到 **Arkime** 查看 PCAP 時對應的語法。

## 一、 OpenSearch / Kibana 篩選語法 (KQL)

在 Malcolm 頂部的搜尋欄（也就是你截圖中寫著 `DQL` 或 `KQL` 的輸入框）直接輸入以下語法：

### 1. 雙向觀測（IT $\leftrightarrow$ OT）

> 只要這兩個網段有任何一方在跟彼此講話，全部撈出來。

Code snippet

```
(source.ip: "192.168.65.0/24" AND destination.ip: "192.168.60.0/24") OR (source.ip: "192.168.60.0/24" AND destination.ip: "192.168.65.0/24")
```

### 2. 單向觀測：IT 往 OT（IT $\rightarrow$ OT）

> 觀測是否有 IT 網段的主機主動對 OT 網段發起連線（例如：工程師從辦公區遠端連線、漏洞掃描、甚至是潛在的橫向移動）。

Code snippet

```
source.ip: "192.168.65.0/24" AND destination.ip: "192.168.60.0/24"
```

### 3. 單向觀測：OT 往 IT（OT $\rightarrow$ IT）

> 觀測是否有 OT 設備主動連向 IT 網段（例如：PLC 拋資料給 Historian 資料庫。**警告**：如果是 OT 主機主動對 IT 建立不尋常的連線，需防範反向 Shell、C2 或者是資料外洩）。

Code snippet

```
source.ip: "192.168.60.0/24" AND destination.ip: "192.168.65.0/24"
```

## 二、 Arkime (Moloch) 篩選語法

如果你在 Malcolm 中切換到 **Arkime 介面**（通常用來看詳細的 Session 和下載 PCAP），欄位名稱會有些許不同，請在搜尋列輸入：

- **雙向觀測 (IT $\leftrightarrow$ OT)**：
    
    Plaintext
    
    ```
    (ip.src == 192.168.65.0/24 && ip.dst == 192.168.60.0/24) || (ip.src == 192.168.60.0/24 && ip.dst == 192.168.65.0/24)
    ```
    
- **IT 往 OT (IT $\rightarrow$ OT)**：
    
    Plaintext
    
    ```
    ip.src == 192.168.65.0/24 && ip.dst == 192.168.60.0/24
    ```
    

## 三、 套用 Filter 後的威脅獵捕思維（觀察重點）

當你套用了上述 Filter 後，建議切換到 Malcolm 的 **Connections 儀表板**，並把注意力放在以下幾點：

1. **通訊協定（Protocols / Ports）**：
    
    - **正常情況**：通常只會有特定的歷史資料庫同步（如 SQL, OPC UA）或特定網管協定。
        
    - **異常警訊**：如果看到 **RDP (3389)**、**SSH (22)**、**Telnet (23)**、**VNC (5900)** 或 **SMB (445)** 跨越了 IT/OT 邊界，必須查明這是否為未授權的遠端維護通道。
        
2. **一對多（One-to-Many）行為**：
    
    - 有沒有單一的 IT 主機（`192.168.65.x`），同時對多個 OT 主機（`192.168.60.x`）發送連線？這很可能是內網掃描（Reconnaissance）。
        
3. **流量與時間（Bytes & Duration）**：
    
    - 有沒有連線時間極長，且傳輸了大量資料（High Bytes Out）的情況？需要確認是不是大宗資料外洩（Exfiltration）。
        

當你套用了這個雙向 Filter 之後，有沒有看到什麼不應該出現在 OT 邊界上的通訊協定（例如遠端桌面、未加密的網頁或未知的 Port）？

---
title: "Malcolm Threat Hunting Points of Interest"
description: "Uses Suricata alerts, Zeek notices, Zeek weird logs, and LongConnection pivots to prioritize Malcolm threat hunting."
created: 2026-07-16
updated: 2026-07-16
type: howto
lang: zh
status: draft
tags: [malcolm, nsm, threat-hunting]
---

> Related: [[MOC - Threat Hunting]] · [[MOC - Malcolm & NSM]] · [[zeek-seen-bytes]]

你的 Threat Hunting 起手式非常標準且專業！

在 Malcolm 這樣的網路流量分析（NTA）平台中，從 **Suricata Alert**、**Zeek Notice** 和 **Zeek Weird** 開始，通常是最能快速抓到「蛛絲馬跡」的鐵三角。

以下為你評估目前的起手式思路，並針對你提供的 `LongConnection`（長連線）截圖進行深度解讀，提供具體的下一步調查建議。

## 一、 對你目前威脅獵捕起手式的評估與建議

這個思路非常好，因為這三個維度剛好互補：

- **Suricata Alert（特徵導向）**：幫你抓出「已知惡意」的行為（例如特定的 CVE 漏洞利用、已知惡意軟體的 C2 軌跡）。
    
- **Zeek Notice（行為與原則導向）**：幫你抓出「不一定惡意但很可疑」的行為（例如這張截圖中的長連線、密碼暴力破解、憑證過期等）。
    
- **Zeek Weird（協定異常）**：幫你抓出不符合 RFC 規範的封包（這在 OT 網段很常見，有時是設備老舊，有時是攻擊者在進行掃描或嘗試規避檢測）。
    

> 💡 **進階獵捕建議**：
> 
> **不要孤立看待它們**。試著尋找**交集**。例如：如果某個 IP 同時觸發了 Suricata Alert（顯示有潛在攻擊嘗試）**且**在 Zeek Weird 中有大量的 TCP 重置（Reset）或異常行為，這台主機的調查優先級（Triage Priority）就應該被拉到最高。

## 二、 截圖解讀：Zeek Notice `LongConnection` 數據分析

這張 `LongConnection` 儀表板透露了非常多關於你 OT 環境的實用資訊：

### 1. 正常的 OT 營運基準（Baseline）

在 OT 網段中，長連線往往是**常態**而非異常。因為工業協定（如 Modbus、S7comm）需要持續進行資料輪詢（Polling）。

- **Modbus 輪詢活動**：目的地 `192.168.60.4`（OT 網段）是整個網路的 Hub，有高達 698 次長連線。細看「Message Details」，多個 OT 主機（`.10` 到 `.15`）正持續對 `.4` 的 `502/tcp`（Modbus）進行超過 10 分鐘甚至 60 分鐘的連線。這極可能是 PLC 與 SCADA 之間的正常通訊。
    
- **S7comm 活動**：`192.168.0.3 -> 192.168.0.2:102/tcp` 也是典型的西門子 PLC 通訊（Port 102）。
    

### 2. 潛在的異常與關注點（調查重點）

- **跨網段與邊界安全（最關鍵！）**：
    
    - 在「Notice - Destination IP Address」中，我們看到了 **`192.168.65.67`**（IT 網段主機）出現在目的地列表中，且有 43 次記錄。
        
    - **核心問題**：是誰在跟這台 IT 主機建立「長連線」？如果是 OT 網段（`192.168.60.0/24`）的主機直接與這台 IT 主機建立長連線，這可能違反了普渡模型（Purdue Model）的網路隔離原則。這可能是維護通道、雙網卡主機的橋接，甚至是潛在的橫向移動或資料外洩通道。
        
- **廣播型長連線**：
    
    - 日誌最後幾行顯示 `192.168.60.12/15` 朝 `192.168.60.255:1347/udp`（OT 廣播地址）發送持續的 UDP 流量。需要確認 Port 1347 是否為你們廠區內特定工業設備（如設備發現、心跳包）的正常協定。
        

## 三、 接下來的 Step-by-Step 獵捕行動

為了從這 1,408 筆資料中撈出真正的威脅，建議你在 Malcolm 中執行以下步驟：

### Step 1：過濾已知噪聲，讓異常浮現

因為大量的 Modbus（Port 502）和 S7comm（Port 102）長連線塞滿了你的視線，你必須先把這些「已知營運流量」濾掉。

- **在 Malcolm 頂部新增 Filter**：
    
    `NOT (destination_port: 502) AND NOT (destination_port: 102)`
    
- _目的_：排除這些常態連線後，看看還剩下哪些 `LongConnection`。是否有 RDP（3389）、SSH（22）、HTTP（80/8080）或不明 Port 的長連線？
    

### Step 2：深挖 IT 與 OT 的交會點（聚焦 `192.168.65.67`）

這台 IT 主機是目前最值得懷疑的 Pivot Point。

1. 在 Malcolm 中過濾：`destination_ip: "192.168.65.67"`。
    
2. 觀察其 **Source IP**：是誰連過來的？如果是 OT 網段的設備，記錄下該 OT 設備的 IP。
    
3. **進行軸轉（Pivot）分析**：
    
    - 切換到 **Connections 儀表板**（`conn.log`），查看這兩個 IP 之間的歷史對話。
        
    - 檢查連線的**傳輸進出流量（Bytes）**：是單向傳輸大量數據（可能在竊取資料/Historian 同步），還是雙向均等？
        
    - 查看 **History 欄位**：有沒有異常的 TCP 連線建立與中斷行為？
        

### Step 3：檢查 Web 管理介面的長連線

在 Message Details 中，我們有看到 `192.168.60.153 -> 192.168.60.19:80/tcp`（HTTP）長連線超過 10 分鐘。

- 調查 `.153` 是否為工程師工作站？連線到 `.19` 的網頁管理介面是否為正常維護？有沒有可能是未授權的連線或 Session 殘留？
    

當你過濾掉 Modbus（502）和 S7comm（102）等常態工業流量後，剩餘的長連線中，是否出現了不尋常的通訊協定（例如 HTTP, SSH, RDP），或者發現其他跨 IT/OT 網段的 IP 連線？

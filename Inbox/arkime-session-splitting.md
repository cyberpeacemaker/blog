---
created: 2026-07-14 20:07
updated: 2026-07-14 20:07
tags: []
type: reference
lang: en
status: draft
---
這是一段在網路鑑識（Network Forensics）或 CTF（奪旗賽）中常見的任務指引。

簡而言之，這句話是要求你：**「透過下載並分析原始封包（PCAP），完整拼湊出攻擊者在 `192.168.65.69` 與 `10.99.40.20:80` 之間傳輸的完整明文攻擊劇本（Playbook），不要偷懶使用 Arkime 自動解析產生的 HTTP MD5 檔案導出功能，因為那個功能會漏掉後半段的資料。」**

下面為您詳細拆解這兩個關鍵問題：

## 1. 什麼是 `http.md5`？

在網路流量分析工具 **Arkime**（前身為 Moloch）中，**`http.md5`** 是一個元數據（Metadata）欄位：

- **功能**：當 Arkime 在監控/解析 HTTP 流量時，會自動幫傳輸中的 HTTP 回應主體（Response Body，例如網頁內容、下載的檔案、腳本等）計算出 MD5 雜湊值（Hash），並記錄在這個欄位中。
    
- **http.md5 path（HTTP MD5 路徑）**：指的是利用這個雜湊值，透過 Arkime 內建的檔案自動還原/導出機制（Carving）來提取檔案。
    

## 2. 為什麼會 Drop（遺漏）「late keep-alive tasks」？

這涉及了 **HTTP Keep-Alive 協議的特性** 與 **Arkime 解析器的系統限制與 Bug**：

### 核心原因 A：HTTP Keep-Alive 與會話限制

- **Keep-Alive 機制**：允許瀏覽器/客戶端與伺服器之間「共用同一個 TCP 連線」來發送多個 HTTP 請求與回應（Tasks），而不需要每次都重新建立連線。
    
- **會話切片（Session Splitting）**：為了效能，Arkime 對於「單一 TCP 會話」有封包數量限制（預設為 10,000 個封包）或時間超時限制（Timeout）。如果這個 Keep-Alive 連線持續太久，或者後半段的任務（late tasks）間隔時間過長，Arkime 會判定該 Session 已結束或進行切片，進而**停止為後續的 HTTP 內容計算 MD5**。
    

### 核心原因 B：Arkime 內建解析器的 Bug

- 在某些 Arkime 版本的 HTTP 解析器中存在已知缺陷：當多個請求共用同一個 Keep-Alive 連線時，解析器在計算完前幾個 `http.md5` / `sha256` 後，**無法正確重置或釋放 HTTP 解析器的狀態**。
    
- 這導致後半段（late）在這個連線上傳輸的 HTTP 內容，其雜湊值**不會被計算**。如果你只依賴 `http.md5` 相關的自動導出路徑，那些後半段傳輸的攻擊劇本（Tasks）就會被**無聲無息地遺漏（Silently dropped）**。
    

## 💡 您應該如何正確操作？

既然自動化的 `http.md5` 還原路徑會漏掉關鍵的攻擊步驟，你必須回歸最穩健的**手動還原（Carving raw packets）**：

1. 在 Arkime 界面中搜尋 `192.168.65.69 ↔ 10.99.40.20:80` 的會話。
    
2. 點擊 **Export PCAP** 將該會話的原始封包下載下來。
    
3. 將 PCAP 檔案放入 **Wireshark** 打開。
    
4. 找到該 TCP 連線，右鍵選擇 **Follow -> TCP Stream**（跟隨 TCP 串流）。
    
5. 這樣你就能看到完整、不中斷的明文 HTTP 請求與回應流，進而順利找出完整的攻擊劇本。
    

你需要我進一步提供如何使用 Python (Scapy) 或是 Wireshark 來手動還原這段 Keep-Alive 封包內容的具體指令嗎？


---
title: "Zeek FUID and CUID"
description: "Explains Zeek connection UIDs and file FUIDs for pivoting across logs."
created: 2026-07-14 20:07
updated: 2026-07-14 20:07
tags: [malcolm, nsm, zeek]
type: reference
lang: zh
status: draft
---

> Related: [[MOC - Malcolm & NSM]] · [[zeek-file-reassembler]] · [[cross-id-analysis]]

在網路安全監控工具 **Zeek**（舊稱 Bro）中，`cuid`（或在日誌中常簡稱為 `uid`）與 `fuid` 是其日誌系統中非常核心的兩個**唯一識別碼（Unique Identifiers）**。

這兩個識別碼的設計，主要是為了解決網路流量分析中的**關聯追蹤、日誌交叉檢索與「一對多」的傳輸關係**。

## 什麼是 cuid 與 fuid？

- **`cuid` (Connection Unique ID / 連線唯一識別碼)：**
    
    - 在日常的 Zeek 日誌中（如 `conn.log`、`http.log`、`dns.log`），這個欄位通常直接顯示為 **`uid`**。但在 Zeek 的特定腳本結構（如 `Notice::FileInfo` 紀錄）中，為了與檔案 ID 區分，會被明確命名為 **`cuid`**。
        
    - 它用來唯一標記一個**網路連線（由來源 IP、來源 Port、目的 IP、目的 Port 與傳輸協定組成的 5-Tuple）**。
        
    - 在 Zeek 中，連線 ID 的字串開頭固定為字母 **`C`**（例如：`CzoFRWTQ6YIzfFXHk`）。
        
- **`fuid` (File Unique ID / 檔案唯一識別碼)：**
    
    - 由 Zeek 的 **檔案分析框架 (File Analysis Framework)** 產生，用來唯一標記在網路傳輸中被偵測或提取出來的**單一檔案**（例如：透過 HTTP、FTP 或 SMTP 傳輸的 exe、pdf、jpg 等）。
        
    - 在 Zeek 中，檔案 ID 的字串開頭固定為字母 **`F`**（例如：`FBbQxG1GXLXgmWhbk9`）。
        

## 為什麼要同時存在這兩種 ID？

Zeek 同時設計這兩種識別碼，主要有以下三個關鍵原因：

### 1. 處理網路傳輸中「一對多」的關係

在真實的網路行為中，連線與檔案並非一對一的關係，如果只有一種 ID 會造成混亂：

- **單一連線傳輸多個檔案：** 在一個 HTTP 持續連線（Keep-Alive）中，瀏覽器可能會在**同一個連線 (`cuid`)** 下連續下載多個圖片或網頁元件。有了 `fuid`，我們就能在同一個 `cuid` 下，精確區分並追蹤多個不同的檔案實體。
    
- **單一檔案跨多個連線（如分段下載）：** 某些分段下載或 P2P 傳輸中，一個大檔案可能會拆分並透過多個不同的 TCP 連線傳輸。
    

### 2. 跨日誌的關聯追蹤與 Pivoting（樞紐分析）

Zeek 的設計哲學是將不同層級與協定的資訊拆分到不同的專屬日誌中（例如：`conn.log`、`http.log`、`files.log`）。

- 當你在 `files.log` 發現一個惡意檔案（透過 `fuid` 標記，並伴隨 MD5/SHA256 哈希值），你可以直接複製該日誌欄位中的 `uid`（即 `cuid`），直接去 `conn.log` 或 `http.log` 進行**反向追蹤**，查出是哪一個 IP 在什麼時間、透過什麼 URL 下載了這個檔案。
    

> **關聯範例：**
> 
> - `conn.log` 記錄連線：`uid` = **`C123`** (記錄了 IP、流量大小)
>     
> - `http.log` 記錄請求：`uid` = **`C123`** (記錄了 GET 請求、Host 主機)
>     
> - `files.log` 記錄檔案：`uid` = **`C123`** 且 `fuid` = **`F456`** (記錄了檔案哈希、大小，並指出它屬於 `C123` 這條通道)
>     

### 3. 解耦分析架構 (Decoupled Analysis)

Zeek 採用模組化設計。**協定分析器**（如 HTTP 解析器）只專注於解析網路協定的標頭與狀態；而**檔案分析器**則專注於檔案本身的操作（如計算雜湊值、辨識 MIME 類型、甚至將檔案還原寫入硬碟）。

透過將連線識別碼（`cuid`）與檔案識別碼（`fuid`）分離，檔案分析框架就能在不干擾底層網路連線狀態的情況下，獨立進行深度的檔案安全分析。

## 快速對比表

|**特性**|**cuid (通常在日誌中顯示為 uid)**|**fuid**|
|---|---|---|
|**全稱**|Connection Unique ID|File Unique ID|
|**主要功能**|識別唯一的**網路連線 (Session)**|識別唯一的**傳輸檔案 (File)**|
|**開頭字母**|**`C`** (例如：`CzoFRWTQ6...`)|**`F`** (例如：`FBbQxG1G...`)|
|**產生來源**|連線狀態與協定分析器 (Conn Analyzer)|檔案分析框架 (File Analysis Framework)|
|**常見日誌**|`conn.log`, `http.log`, `dns.log` 等|`files.log` (但內含對應的 `uid` 欄位以供關聯)|

這套雙 ID 機制讓 Zeek 在面對龐大且複雜的網路流量時，依然能保持極高的高效性、結構性與無縫的威脅追蹤能力。


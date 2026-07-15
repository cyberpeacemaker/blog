---
title: "Arkime http.md5 vs Zeek MIME Type"
description: "Compares Arkime http.md5 with Zeek mime_type for file triage and evasion resistance."
created: 2026-07-14 20:07
updated: 2026-07-14 20:07
tags: [malcolm, nsm, arkime, zeek]
type: reference
lang: zh
status: draft
---

> Related: [[MOC - Malcolm & NSM]] · [[arkime-http-md5]] · [[zeek-files-mime-type-mz]]

問得太好了！你立刻聯想到另一個在網路安全界地位極高的工具 —— **Zeek**（舊稱 Bro）。

如果說 Arkime 的 `http.md5` 像是一個「比對黑名單的通緝令資料庫」**，那麼 Zeek 的 `mime_type` 就像是一個**「擁有 X 光火眼金睛的海關檢查員」。

Zeek 的 `mime_type`（記錄在 `files.log` 中）在設計上**比單純的 MD5 聰明得多**，防守方非常依賴它。但同樣地，它也有其極限與被繞過的可能。

以下為您詳解 Zeek 的 `mime_type` 運作原理、為什麼它很強，以及黑客會怎麼繞過它。

## 一、 Zeek 是如何判定 `mime_type` 的？（為什麼它很聰明）

在網路傳輸中，伺服器通常會在 HTTP Header 宣告這個檔案是什麼類型（例如 `Content-Type: image/jpeg`）。

如果是笨一點的系統，就會直接相信這個宣告，並把檔案當作圖片。但 **Zeek 完全不信任 HTTP Header，也不信任副檔名（`.jpg`）**。

### 1. 魔術數字（Magic Numbers / File Signatures）

Zeek 採用的是 **「內容檢測（Content Inspection）」**。當一個檔案流經網路時，Zeek 會默默抓取檔案的前幾個 Byte（通常是前 1024 內容），去比對內部的「文件特徵碼資料庫」：

- 如果前兩個字元是 `MZ`（十六進位 `4D 5A`），Zeek 就會判定它是 Windows 執行檔，標記為 `application/x-dosexec`。
    
- 如果開頭是 `PK`（十六進位 `50 4B`），Zeek 就會判定它是 ZIP 壓縮檔，標記為 `application/zip`。
    

## 二、 Zeek `mime_type` 在資安上的三大神級用途

正因為 Zeek 是看「內容本質」而不是看「外在包裝」，這賦予了防守方極強的偵測能力：

### 1. 揪出「掛羊頭賣狗肉」的偽裝（Mismatches）

黑客最喜歡把惡意程式（`.exe`）改名成圖片（`cat.jpg`）來誘騙使用者下載，或者繞過防火牆。

- **黑客的包裝**：副檔名是 `.jpg`，HTTP Header 寫著 `image/jpeg`。
    
- **Zeek 的 X 光**：掃描檔案開頭發現 `MZ`，強行將 `mime_type` 標記為 `application/x-dosexec`。
    
- **安全警報**：資安人員只要下一行簡單的指令：_「找出所有副檔名是 .jpg，但 Zeek mime_type 卻是 application/x-dosexec 的連線」_。這種偽裝就會立刻見光死。
    

### 2. 精準觸發後續動作（如檔案還原、沙箱分析）

你不需要把所有的網路流量都存下來（這樣硬碟會爆）。你可以告訴 Zeek：

> 「只要看到 `mime_type` 是 `application/x-dosexec`（執行檔）或 `application/pdf`（容易藏漏洞的PDF），就把檔案自動提取（Extract）出來，送去火眼沙箱（Sandbox）跑跑看有沒有毒。」

### 3. 無視副檔名模糊化

有些網址下載時長這樣：`[http://malicious.com/download?id=992837](http://malicious.com/download?id=992837)`。這個 URL 完全沒有副檔名。但 Zeek 依然能透過 `mime_type` 精確辨識出它其實下載了一個腳本、一個 Office 文件還是一個壓縮檔。

## 三、 那麼，黑客要怎麼繞過 Zeek 的 `mime_type`？

雖然 Zeek 很有智慧，但道高一尺、魔高一丈。攻擊者依然有辦法讓 Zeek 無法正確識別：

### 1. 加密或混淆（Encryption / Obfuscation）

這是最致命的繞過方式。

- 如果攻擊者在傳輸前，先用一個簡單的密鑰（例如 XOR 運算）把惡意程式加密，或者使用 HTTPS（加密傳輸）。
    
- 此時，檔案開頭的 `MZ` 變成了隨機的亂碼（例如 `0x3F 0xA2`）。
    
- Zeek 看不透加密後的內容，只能無奈地將其標記為 `application/octet-stream`（意思是：我只知道這是二進位資料，但看不出是什麼）。這就成功實現了隱蔽傳輸。
    

### 2. 雙重特徵檔（Polyglot Files）

這是一種非常高級的黑客技術。攻擊者刻意設計一個檔案，它的結構同時滿足兩種檔案格式的特徵。

- 例如：一個檔案的前面看起來是個合法的 `GIF` 圖片（Zeek 判定為 `image/gif`），但後面其實藏了執行檔的程式碼。當它在受害者電腦運行時，特定的解譯器會去執行後半段。
    
- 這會導致 Zeek 的特徵檢測出現混淆或誤判。
    

### 3. 加密壓縮檔（Password-Protected Zip）

如果攻擊者把惡意程式放進 ZIP，並加上密碼。

- Zeek 只能識別出 `mime_type` 是 `application/zip`，這是完全合法的格式。
    
- Zeek 無法解開密碼，因此無法得知裡面藏了什麼。
    

## 💡 總結

|**偵測維度**|**Arkime 的 http.md5**|**Zeek 的 mime_type**|
|---|---|---|
|**本質**|檔案的「身份證號碼」（唯一值）|檔案的「DNA / 種類」（類別）|
|**防偽能力**|極低（改 1 個 Byte 就失效）|中高（改檔名、改網頁標頭都沒用）|
|**主要用途**|快速比對已知威脅、去重|發現偽裝行為、分類過濾、觸發自動化分析|
|**繞過難度**|輕而易舉（加垃圾資料、分段）|中等（需透過加密、混淆或特製檔案）|

所以，現代資安防護都是**兩者結合**：先用 Zeek 的 `mime_type` 篩選出「所有的執行檔」，再用這些執行檔去比對有沒有符合惡意 `http.md5` 的通緝犯。如果兩者都漏過了，最後就得靠你手動去撈 Raw PCAP 封包來做終極大還原了！

你有在 Zeek 的日誌（例如 `files.log`）中看過這些欄位嗎？還是你正準備要把 Zeek 融入你的分析工作流中呢？


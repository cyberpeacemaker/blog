---
title: "Zeek MIME Type and MZ Magic Bytes"
description: "Explains how Zeek identifies Windows executables via MZ magic bytes and MIME labeling."
created: 2026-07-14 16:07
updated: 2026-07-14 16:07
tags: [malcolm, nsm, zeek]
type: reference
lang: zh
status: draft
---

> Related: [[MOC - Malcolm & NSM]] · [[mime-http]] · [[http-md5-zeek-mime-type]]

要深入理解為什麼 `application/x-dosexec` 被稱為檔案的「數位 DNA」，我們需要把視角從高階的日誌檔案，切換到計算機底層的**二進位數據（Binary Data）**。

這是一場攻擊者與防守者在網路邊界上的「偽裝與拆穿」賽博攻防戰。以下為你深度拆解這個技術核心：

## 1. 什麼是魔術數位（Magic Bytes）？

在電腦世界裡，作業系統或網路設備要辨識一個檔案是什麼類型，最快的方法不是看副檔名，而是看檔案開頭的前幾個位元組（Bytes）。這幾個固定的特徵碼就被稱為 **Magic Bytes（魔術數位）**。

對於所有 Windows 的可執行檔（包括 `.exe`、`.dll`、`.sys` 等，統稱為 **PE 檔案**，即 Portable Executable），它們的設計者微軟在幾十年前就定下了死規矩：**檔案的第一個和第二個位元組，必須是 `M` 和 `Z` 這兩個字母。**

> 💡 **冷知識：** `MZ` 這兩個字母，是當年 MS-DOS 執行檔格式的設計者 Mark Zbikowski 的名字縮寫。這個古老的印記一直留到了今天的 Windows 11。

如果我們用十六進位編輯器（Hex Editor）打開任何一個 Windows 程式，你絕對會看到以下景象：

- **十六進位內容：** `4D 5A ...`（`4D` 是 M 的 ASCII 碼，`5A` 是 Z 的 ASCII 碼）
    
- **文字表現：** `MZ` 開頭，後面通常會跟著一句 `This program cannot be run in DOS mode.`
    

## 2. Zeek 這類的資安系統是怎麼抓到它的？

當攻擊者透過 HTTP 流量下載惡意程式時，網路流量在傳輸層會被拆成無數個 TCP 封包。

像 Zeek (舊稱 Bro) 這樣的網路安全監控系統（NSM），它的工作原理是**網路流量還原**。它會在記憶體中把這些破碎的封包重新拼湊回原本的檔案檔案流（File Stream）。

1. **檔案框架啟動：** 當 Zeek 偵測到有 HTTP 檔案傳輸，它的「檔案分析框架（File Analysis Framework）」就會介入。
    
2. **只看開頭：** Zeek 不需要等整個 6MB 的檔案全部下載完。它只要看到檔案流的前幾個位元組是 `4D 5A`（`MZ`），它的大腦（特徵庫）就會立刻彈出對應標籤。
    
3. **打上 MIME 標籤：** 接著，它就會在日誌（`files.log`）中的 `mime_type` 欄位填入 `application/x-dosexec`。這代表：**「別管網址寫什麼，這玩意兒本質上就是個 Windows 執行檔！」**
    

## 3. 攻擊者的偽裝術 vs. 分析師的火眼金睛

為什麼說「分析師沒有被看似合法的檔名欺騙」是數據素養的體現？我們來看看實戰中經典的「欄位衝突」奇觀。

在惡意流量中，日誌常常會呈現出極具衝突的矛盾：

|**日誌欄位 (Log Field)**|**攻擊者的偽裝 (看似正常)**|**流量的真實本質 (現出原形)**|
|---|---|---|
|**`url.path`**|`/images/logo.png` (偽裝成圖片)|`/file/download` (刻意模糊)|
|**`http.response.header.content_type`**|`image/png` (伺服器說我是圖片)|`application/octet-stream` (未知流)|
|**`file.mime_type` (Zeek 鑑識)**|**`image/png`** ❌|**`application/x-dosexec`** ⭕|

### 為什麼這是一個巨大的告警（Red Flag）？

一個正常的網站，當使用者存取一個 `.png` 圖片網址時，網路線路上流過去的檔案 DNA 應該是 `image/png`（Magic Bytes 為 `89 50 4E 47`）。

但如果今天 `url.path` 寫著 `logo.png`，或是像你提供的情境中，雖然是一個抽象的下載接口 `/mapi/document`，但 Zeek 抓到的數位 DNA 卻是 `application/x-dosexec`。

這就觸發了資安鐵律：**「名實不符，必有妖孽。」** 這是攻擊者最常用的「障眼法（Masquerading）」，用來躲避那些只檢查副檔名或 URL 關鍵字的老舊防火牆。

## 4. 攻擊者為什麼不把 `MZ` 擦掉？

你可能會問：「既然資安系統會盯著 `MZ` 看，那駭客把檔案開頭的 `MZ` 刪掉或改掉，不就能躲過檢查了嗎？」

答案是：**不行。因為魔術數位是給 Windows 作業系統的「開機解碼密碼」。**

如果攻擊者把惡意程式開頭的 `MZ` 改成了 `AB`，當這個檔案落地到受害者的電腦上時，Windows 的雙擊執行或進程加載器（PE Loader）讀到開頭不是 `MZ`，就會直接彈出錯誤：`此應用程式無法在您的電腦上執行`。

**唯一的例外：** 攻擊者使用加密（Encryption）或編碼（如 Base64、XOR）。如果檔案在網路上傳輸時全身打馬賽克，Zeek 就確實看不出 `MZ`。但正如你的第二份報告（POI-02-3）所述，一旦它是 cleartext（明文）直接在網路線上裸奔下載，它的 `MZ` 數位 DNA 就注定暴露在分析師的監控之下了。


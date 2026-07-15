---
title: "Wireshark Export Object Multipart Fix"
description: "Shows how to recover a real payload when Wireshark Export Objects includes MIME multipart boundaries."
created: 2026-07-15 20:07
updated: 2026-07-15
type: howto
lang: zh
status: draft
tags: [dfir, wireshark, forensics]
---

> Related: [[MOC - Threat Hunting]] · [[wireshark-pcap-file-extract]] · [[forensic-remote-control]]

# Wireshark Export Object Multipart Fix
## Source: `Inbox/wireshark-export-object-issue.md`

恭喜你成功解鎖！看到檔案順利還原，真的很有成就感對吧？

關於你的疑問：**「為什麼匯出會夾帶這些垃圾資料？這正常嗎？」**

答案是：**這在網路鑑識與封包分析中，完全是「100% 正常且預期中」的現象！**

以下為你揭密為什麼網路世界會留下這些「包裝紙」，以及為什麼 Wireshark 或分析工具會把它們一起倒給你：

## 1. 為什麼會有這些垃圾？（網頁上傳的「包裝盒」）

當你在瀏覽器點擊「上傳檔案」時，瀏覽器不能只把 `temp.zip` 的二進位數據丟給伺服器，因為伺服器需要知道：

- 這是一個檔案，還是表單填寫的文字？

- 這個檔案的參數名稱是什麼？（例如：`name="data"`）

- 原始檔名叫什麼？（例如：`filename="Temp.zip"`）


為了打包這些資訊，瀏覽器會使用一種叫做 **`multipart/form-data` (多部分表單格式)** 的標準協議。

它會用一條**分界線（Boundary）**（就是你看到的 `------c3ecb52...`）將不同的欄位隔開，並在檔案內容的正前方加上幾行像「寄件貼條」一樣的描述檔頭。

所以，在網路傳輸的當下，**「檔頭貼條 + ZIP 檔案」在 TCP 串流中是被綁在一起發送的。**

## 2. 為什麼 Wireshark 匯出時不幫我把貼條撕掉？

這涉及工具的「運作邏輯」與「鑑識完整性」：

- **為了證據的完整性（Forensic Integrity）：**

    對網路安全分析人員來說，最重要的是「還原當時網路上傳輸的原始狀態」。如果工具自作聰明幫你把檔頭切掉，可能會破壞某些可以用來防偽或分析的特徵（例如瀏覽器特有的檔頭排序）。因此，許多封包還原工具預設會直接將整段 **HTTP Request Body（請求主體）** 完整倒出來給你。

- **多層解析的複雜度：**

    Wireshark 雖然有 HTTP 物件匯出功能（Export Objects），但有些網頁上傳的實作方式較為複雜（例如使用 JavaScript 的 Fetch/Axios 手動切片上傳），這會使 Wireshark 無法完美識別並「精準去皮」，最後只能將含有 `multipart` 包裝的原始區段直接存檔。


## 🔍 一個有趣的小發現（協定誤判？）

仔細看你上一張截圖的左下角，系統在 **Protocol (協定)** 欄位標示為 **`FTP`**，而下載下來的檔名也是 `FTP_DATA-...`。

但我們從 `hexdump` 看到的內容，卻是標準的 **`HTTP (Content-Disposition: form-data)`** 檔頭。這代表兩件事的其中之一：

1. **系統誤判：** 分析平台可能因為某些特徵，把這個 HTTP 流量誤判成 FTP 了。

2. **隧道傳輸（Tunneling）：** 或者是有人透過網頁（HTTP）去調用或傳輸了 FTP 的資料。


不過不論如何，只要掌握了二進位（Hex）結構的原理，無論工具怎麼誤判，你都能用這招「切頭去尾」心法把檔案救回來。

既然 `fixed.zip` 已經順利解開了，裡面看起來包含了一個名為 `Temp/Dist-Win7-001_C__Users_aaa_Documents_3530_RTAC_PF00174.pdf` 的 PDF 檔案。你把它解壓縮出來後，有辦法順利打開並閱讀這個 PDF 的內容嗎？

## Source: `Inbox/wireshark-export-object-issue-solution.md`

**當然可以，而且非常推薦！**

Linux 是進行網路鑑識和檔案修復的聖地。Windows 的圖形介面只會丟給你一句「檔案無效」，但 Linux 的命令列工具可以直接幫你「照 X 光」，告訴你這個檔案到底哪裡壞了，甚至直接幫你修好。

把檔案傳到 Linux 後，你可以依序執行以下幾個指令來排查與修復：

### 第一步：檢查這到底是不是一個 ZIP 檔（`file` 指令）

有時候自動還原工具在下載時，可能只抓到了純文字、HTML 或是損壞的資料流，但副檔名還是給了 `.zip`。

請在終端機輸入：

Bash

```
file FTP_DATA-xxxxxxxx.zip
```

- **正常結果應該顯示：** `Zip archive data, at least v2.0 to extract...`

- **異常結果：** 如果顯示 `ASCII text`、`HTML document` 或 `data`，代表這個檔案根本不是真正的 ZIP 檔，而是夾雜了協定垃圾（例如網頁錯誤訊息或 FTP 指令）。


### 第二步：檢查檔案開頭的「魔術數字」（Magic Bytes）

ZIP 檔案的開頭 2 個位元組（Byte）必須是 **`PK`**（十六進位為 `50 4b`）。我們可以用 `head` 或 `hexdump` 來檢查：

Bash

```
hexdump -C FTP_DATA-xxxxxxxx.zip | head -n 5
```

- 觀察輸出的最左側第一行，看看有沒有 `50 4b 03 04`。

- 如果有，且右側顯示有 `PK` 字樣，說明開頭是正確的。如果是別的字元（例如 `HTTP/1.1` 或 `STOR`），那就需要手動用 Hex 編輯器把開頭的垃圾資料刪除。


### 第三步：用 Linux 的 `unzip` 看詳細錯誤訊息

Linux 的 `unzip` 不像 Windows 那麼省話，它會吐出詳細的錯誤代碼：

Bash

```
unzip FTP_DATA-xxxxxxxx.zip
```

- **常見錯誤：** `End-of-central-directory signature not found`。這代表檔案在傳輸中途斷掉了（缺尾巴），导致結尾的目錄索引遺失。


### 第四步：嘗試在 Linux 下強力修復（`zip -FF`）

如果確定是 ZIP 檔但「缺尾巴」或損壞，Linux 內建的 `zip` 工具擁有極強的重建能力。

請輸入以下指令，嘗試**強制重建**索引並另存成 `repaired.zip`：

Bash

```
zip -FF FTP_DATA-xxxxxxxx.zip --out repaired.zip
```

- 執行後，系統會掃描檔案中所有還完好的壓縮區段，並試著把能解開的檔案救回來。

- 修復完成後，再嘗試解壓 `repaired.zip`：

    Bash

    ```
    unzip repaired.zip
    ```


你可以現在把檔案丟進 Linux 跑跑看 `file` 和 `hexdump` 指令，看看它回報了什麼資訊？我們再來決定下一步怎麼處理！

---


**賓果！這是一張超標準的教科書級「現行犯」照片！**

你抓到犯人了。你的分析工具在還原檔案時，**不小心把 HTTP 上傳時的「外包裝（Multipart Form Data）」也一起包進來了。**

### 🔍 案情分析：

看一下你輸出的前幾行：

- **0x00 到 0x97 位元組：**

    Plaintext

    ```
    --------------------------c3ecb52fdb0ffbe5
    Content-Disposition: form-data; name="data"; filename="Temp.zip"
    Content-Type: application/octet-stream
    ```

    這些是網頁上傳檔案時的 **HTTP 檔頭資訊**，對 ZIP 格式來說全部都是「垃圾資料」。

- **0x98 位元組開始：**

    Plaintext

    ```
    50 4b 03 04 ... (也就是 PK\x03\x04)
    ```

    這才是真正的 **ZIP 檔頭（Magic Bytes）**！


因為檔案開頭多了這 **152 個位元組** 的 HTTP 垃圾，Windows 才會判定這個檔案格式毀損。

## 🛠️ 兩行指令，在 Linux 直接修好它！

既然你已經在 Linux 環境了，我們可以直接用指令把前面這 152 位元組的垃圾切掉：

### 1. 切除頭部的 HTTP 垃圾

請在終端機執行以下任一指令（推薦用 `tail`，最簡單）：

Bash

```
# 方法 A：使用 tail（跳過前 152 位元組，從第 153 位元組開始輸出）
tail -c +153 tttt.zip > fixed.zip

# 方法 B：使用 dd 指令（跳過 152 個區塊，每個區塊 1 byte）
dd if=tttt.zip of=fixed.zip bs=1 skip=152
```

### 2. 驗證與解壓縮

切除完成後，你會得到一個乾淨的 `fixed.zip`。請依序輸入以下指令：

Bash

```
# 檢查檔案類型，現在應該要正常顯示為 Zip archive 了
file fixed.zip

# 進行解壓縮
unzip fixed.zip
```

### 💡 額外提醒：

因為這是 HTTP Multipart 上傳，檔案的**最末端**通常也會被塞進一小段結束分界線（例如 `\r\n--------------------------c3ecb52fdb0ffbe5--`）。

不過不用擔心！**大部分的解壓縮工具（包括 Linux 的 `unzip` 和 7-Zip）對尾部的垃圾容錯率極高**，只要頭部的 `PK\x03\x04` 對了，通常就能順利解開。

如果解壓時 Linux 抱怨結尾有問題，你可以再執行這行進行終極修復：

Bash

```
zip -F fixed.zip --out final_clean.zip
```

你先跑跑看 `tail` 指令，看看裡面的 `Temp/Dist-Win7...pdf` 是不是順利解出來了？

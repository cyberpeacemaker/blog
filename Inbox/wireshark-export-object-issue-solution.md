---
created: 2026-07-15 20:07
updated: 2026-07-15 20:07
tags: []
type: reference
lang: en
status: draft
---
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
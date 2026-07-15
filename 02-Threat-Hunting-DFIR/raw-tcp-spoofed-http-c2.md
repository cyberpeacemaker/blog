---
title: "Raw TCP Spoofed HTTP C2"
description: "Analyzes high-entropy raw TCP traffic on port 80 that masquerades as HTTP during C2 investigation."
created: 2026-07-15 21:07
updated: 2026-07-15
type: reference
lang: zh
status: draft
tags: [threat-hunting, dfir, c2, wireshark]
---

> Related: [[MOC - Threat Hunting]] · [[threat-hunting-c2-volume-beacon]] · [[beacon]]

# Raw TCP Spoofed HTTP C2
這張 Wireshark 截圖中藏著非常多**關鍵且高度可疑**的資安線索！你打開的確實就是報告中提到的那台主機與 `JAS5fnkTcEVHjZ...` 相關的封包。

從這張圖裡，我們可以解讀出以下幾個極具價值的資訊：

## 1. 異常特徵：偽裝成 HTTP 的 Raw TCP 流量

在截圖中間的 `Export HTTP object list`（匯出 HTTP 物件清單）視窗中，你可以看到：

- **Hostname（主機名稱）、Content Type（內容類型）、Filename（檔案名稱）全部都是空白的。**

- **每個物件的大小全都剛好是 `1460 bytes`。**


> 💡 **這代表什麼？**
>
> `1460 bytes` 是乙太網路（Ethernet）中單個 TCP 封包能承載的最大資料量（MSS, Maximum Segment Size）。
>
> 如果是正常的 HTTP 傳輸（例如下載圖片或網頁），Wireshark 會重組封包並秀出 Hostname（如 `google.com`）和 Content Type（如 `image/png`）。
>
> 這裡每個封包都被獨立切碎、完全沒有 HTTP 標頭（Header），卻因為使用 **Port 80** 而被 Wireshark 誤判為 HTTP。這極有可能是**惡意程式為了規避防火牆檢測，故意假借 Port 80 管道，在傳送自定義的 Raw TCP 加密流量**。

## 2. 內容分析：高熵（Encrypted）加密特徵

看左下角選取的 **Frame 749**：

- 展開的內容只有 `Data (1460 bytes)`，沒有任何 HTTP 協議的結構（如 GET, POST 或 Response 代碼）。

- 右下角 Hex dump（十六進位值）顯示：`48 e8 93 cb 4d bf f7 c0...`，右側的 ASCII 欄位完全沒有任何可讀的英文字母或字串。

- 這證實了前文所說的 **"high-entropy binary"（高熵二進位）**。這些資料經過了高度加密或混淆，無法直接透過肉眼或簡單的解碼器還原。


## 3. 來源與目的：高度疑似「橫向移動」或「內部 staging」

看一下封包的 IP：

- **Source IP（來源）**：`192.168.65.69`

- **Destination IP（目的）**：`10.99.40.20`


> ⚠️ **這兩個 IP 都是私有 IP（Private IP）！**
>
> 這意味著這個傳輸**完全發生在你們的企業內網（LAN）之中**。這不是往外網連線，而是內網兩台設備在頻繁地傳送加密資料。
>
> 在駭客攻擊鏈中，這非常符合**「橫向移動（Lateral Movement）」**或**「內部資料暫存（Staging）」**的特徵。攻擊者可能已經控制了 `192.168.65.69`，正在將資料打包傳送到內網的另一台跳板機 `10.99.40.20`。

## 🛠️ 建議你下一步這樣做：

既然 `Export HTTP object` 沒用，請改用以下方式觀察這個連線：

1. **跟隨 TCP 串流（Follow TCP Stream）**：

    - 在封包列表中（例如 Frame 749）點右鍵。

    - 選擇 **Follow** -> **TCP Stream**。

    - 這會把整段對話（來與回）拼湊在一起。請滑到最頂端，看看連線剛建立時（前幾個封包），雙方有沒有進行任何明文的握手（Handshake）或提示字元（例如 `SSH-` 或特定的暗號）。

2. **調查這兩台設備的身份**：

    - 查一下 `192.168.65.69` 是誰的電腦或哪台伺服器？

    - 查一下 `10.99.40.20` 是什麼設備？（是網域控制站 Domain Controller？資料庫？還是另一台不該有密切往來的員工電腦？）

---

Python

```
# Let's inspect the environment and write a script to download/load the image, OCR it, and analyze the base64 payload.
# Since we have the image in our context, wait, we don't have direct access to image file path unless we can find it.
# Let's check what files are in the current workspace or if we can extract text using an OCR library like pytesseract (if installed) or if we should just do manual OCR on the first few characters to check the magic bytes.

# Let's try to find the image file in the directory first.
import os
print(os.listdir('.'))

```

Code output

```
['input_file_1.png', 'input_file_0.png']

```

Python

```
from PIL import Image
for f in sorted(os.listdir('.')):
    if f.endswith('.png') or f.endswith('.jpg'):
        img = Image.open(f)
        print(f, img.size)

```

Code output

```
input_file_0.png (1024, 602)
input_file_1.png (1070, 934)

```

Python

```
try:
    import pytesseract
    print("pytesseract available")
except ImportError:
    print("pytesseract NOT available")

```

Code output

```
pytesseract NOT available

```

Python

```
import base64

# Let's decode the transcribed lines
b64_str = (
    "bXphjCwTHTL8WhsQ4GOMidZra5tx/P7Jjvh7dCppshOEpKND1hUvXGjC5XzvcTfb1tHNoqlM0LrC"
    "RYTl4elLLeo4025t8ehc07g3NY+y+0z9jHaA4JzMgy50hS1FaTYudTesSB52g3tn9zd3QaPvNO"
    "Vfod7s71zmL3KrEYX2mj7aged6SXYSSnbtA5bOuib6De0e2odxt7wYsw7HyhKwoG76RljoY2Sx3w"
    "zNOGZMQXJNARW7i0S9l/WvXcOP/GKNkpF5Xv8gR1BdqO/MT/VRNqELs6OUHLuhxWvbKLN7Vt43L"
)

try:
    decoded = base64.b64decode(b64_str)
    print("Decoded length:", len(decoded))
    print("Decoded hex (first 64 bytes):", decoded[:64].hex())
    print("Decoded text (ASCII representation, ignoring non-ascii):")
    # print only printable ascii characters
    print("".join([chr(b) if 32 <= b < 127 else '.' for b in decoded]))
except Exception as e:
    print("Error:", e)

```

Code output

```
Error: Invalid base64-encoded string: number of data characters (301) cannot be 1 more than a multiple of 4

```

Python

```
lines = [
    "bXphjCwTHTL8WhsQ4GOMidZra5tx/P7Jjvh7dCppshOEpKND1hUvXGjC5XzvcTfb1tHNoqlM0LrC",
    "RYTl4elLLeo4025t8ehc07g3NY+y+0z9jHaA4JzMgy50hS1FaTYudTesSB52g3tn9zd3QaPvNO",
    "Vfod7s71zmL3KrEYX2mj7aged6SXYSSnbtA5bOuib6De0e2odxt7wYsw7HyhKwoG76RljoY2Sx3w",
    "zNOGZMQXJNARW7i0S9l/WvXcOP/GKNkpF5Xv8gR1BdqO/MT/VRNqELs6OUHLuhxWvbKLN7Vt43L"
]
for i, l in enumerate(lines):
    print(f"Line {i+1} length: {len(l)}")

```

Code output

```
Line 1 length: 76
Line 2 length: 74
Line 3 length: 76
Line 4 length: 75

```

Python

```
import base64

# Let's try decoding line 1 alone
try:
    print("Line 1 decoded:", base64.b64decode(lines[0])[:16].hex())
    print("Line 1 text:", "".join([chr(b) if 32 <= b < 127 else '.' for b in base64.b64decode(lines[0])]))
except Exception as e:
    print(e)

```

Code output

```
Line 1 decoded: 6d7a618c2c131d32fc5a1b10e0638c89
Line 1 text: mza.,..2.Z...c...kk.q.....{t*i.....C../\h..|.q7......L...

```

Python

```
import base64
print(base64.b64decode("bXph"))

```

Code output

```
b'mza'

```

Python

```
try:
    import easyocr
    print("easyocr available")
except ImportError:
    print("easyocr NOT available")

```

Code output

```
easyocr NOT available

```

Python

```
import base64
line = "bXphjCwTHTL8WhsQ4GOMidZra5tx/P7Jjvh7dCppshOEpKND1hUvXGjC5XzvcTfb1tHNoqlM0LrC"
# bXph -> b'mza'
# jCwT -> b'\x8c,\x13'
# HTL8 -> b'\x1d2\xfc'
# WhsQ -> b'Wh\x11' wait, let's verify WhsQ
# Let's decode piece by piece
print("bXph ->", base64.b64decode("bXph"))
print("jCwT ->", base64.b64decode("jCwT"))
print("HTL8 ->", base64.b64decode("HTL8"))
print("WhsQ ->", base64.b64decode("WhsQ"))
print("4GOM ->", base64.b64decode("4GOM"))
print("idZr ->", base64.b64decode("idZr"))
print("a5tx ->", base64.b64decode("a5tx"))
print("/P7J ->", base64.b64decode("/P7J"))
print("jvh7 ->", base64.b64decode("jvh7"))
print("dCpp ->", base64.b64decode("dCpp"))
print("shOE ->", base64.b64decode("shOE"))
print("pKND ->", base64.b64decode("pKND"))
print("1HUv ->", base64.b64decode("1HUv"))
print("XGjC ->", base64.b64decode("XGjC"))
print("5Xzv ->", base64.b64decode("5Xzv"))
print("cTfb ->", base64.b64decode("cTfb"))
print("1tHN ->", base64.b64decode("1tHN"))
print("oqlM ->", base64.b64decode("oqlM"))
print("0LrC ->", base64.b64decode("0LrC"))

```

Code output

```
bXph -> b'mza'
jCwT -> b'\x8c,\x13'
HTL8 -> b'\x1d2\xfc'
WhsQ -> b'Z\x1b\x10'
4GOM -> b'\xe0c\x8c'
idZr -> b'\x89\xd6k'
a5tx -> b'k\x9bq'
/P7J -> b'\xfc\xfe\xc9'
jvh7 -> b'\x8e\xf8{'
dCpp -> b't*i'
shOE -> b'\xb2\x13\x84'
pKND -> b'\xa4\xa3C'
1HUv -> b'\xd4u/'
XGjC -> b'\\h\xc2'
5Xzv -> b'\xe5|\xef'
cTfb -> b'q7\xdb'
1tHN -> b'\xd6\xd1\xcd'
oqlM -> b'\xa2\xa9L'
0LrC -> b'\xd0\xba\xc2'

```

你切換到 **Follow TCP Stream**，並且以 **YAML 格式**呈現，這招非常好！這讓我們看到了這起傳輸的**關鍵致命證據**。

從這張圖中，我們可以拼湊出極其重要的「案情真相」：

## 🔍 三大關鍵線索解析

### 1. 確鑿的「工具下載」行為：1 擊換 7.7 MB

請注意視窗最下方的狀態列：

> **`1 client pkt, 5,321 server pkts`**
>
> **`Entire conversation (7767 kB)`**（整段對話高達 **7.7 MB**）

- **解讀**：客戶端（`192.168.65.69`）只發送了 **1 個封包**（Packet 3），伺服器（`10.99.40.20`）就瘋狂回傳了 **5,321 個封包**，塞給它 7.7 MB 的資料，然後連線就結束了（1 turn）。

- **結論**：這百分之百是「下載大檔案」的行為。客戶端丟出一個「請求（Request）」，隨後下載了一個約 7.7 MB 的二進位檔案。這完美呼應了上一篇報告說的 _"likely large tool-download"_。


### 2. 偽裝成 Port 80 的「非 HTTP 協定」

看封包結構中的 `data: !!binary |`：

- YAML 格式中的 `!!binary` 代表 Wireshark 把原始封包的 Hex 轉成了 Base64 編碼（也就是圖中那一大串 `bXphj...`）。

- **致命線索**：這裡**完全沒有任何 HTTP 標頭**（沒有 `GET /... HTTP/1.1`、沒有 `User-Agent`、沒有 `Host`）。

- **結論**：這是一個**假借 Port 80 管道，實則運行私有/加密協定**的連線。攻擊者知道企業防火牆通常會放行 Port 80（HTTP），所以故意用這個通訊埠來避開偵測。


### 3. 攻擊手法推測：載入第二階段惡意程式（Payload Stage 2）

結合以上兩點，這極度符合以下黑客攻擊情境：

- 內網的 `192.168.65.69` 已經被植入了初期的輕量「下載器（Loader）」。

- Loader 啟動後，往內網的 `10.99.40.20` 發送了一個極短的加密「敲門暗號」（即 Packet 3 的內容）。

- 伺服器確認暗號無誤，立刻把高達 7.7 MB 的主功能惡意軟體（例如：Cobalt Strike Beacon、側載工具、或橫向移動工具）加密後傳送下去，準備在記憶體中解密執行。


## 🛠️ 分析官的下一步：我們該怎麼追？

因為這 7.7 MB 的資料在傳輸時可能經過加密（High-entropy），直接從封包還原成檔案並不容易，但你可以透過以下方向進行「實體追查」：

1. **鎖定時間點與主機**：

    - 封包的時間戳記為 `1714059542`（轉換為台灣時間為 **2024年4月25日 23:39:02**）。

    - 請去撈 `192.168.65.69` 這台主機在**該時間點**的 EDR（如 CrowdStrike、Defender for Endpoint）或 Windows Event Log / Sysmon 日誌。

2. **尋找「誰開了這個 Port」**：

    - 尋找在該時間點，是哪一個 **Process（處理程序）** 建立了往 `10.99.40.20:80` 的連線？（通常會是一個異常的臨時目錄程式，或是被注入的合法程序如 `powershell.exe`, `rundll32.exe`, `svchost.exe`）。


這兩台設備（`192.168.65.69` 和 `10.99.40.20`）在你們內網中，目前已知分別是什麼樣的角色（例如：誰的個人電腦、或是哪台伺服器）嗎？

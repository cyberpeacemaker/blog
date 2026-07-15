---
title: "PowerShell EncodedCommand"
description: "Explains PowerShell EncodedCommand behavior, UTF-16LE Base64 decoding, and detection relevance."
created: 2026-07-15
updated: 2026-07-15
type: howto
lang: zh
status: draft
tags: [threat-hunting, dfir]
---

> Related: [[MOC - Threat Hunting]] · [[beacon]] · [[powershell-execution-policy]]

# PowerShell EncodedCommand
## Source: `Inbox/powershell-base64-encoded-command.md`

沒錯！你的直覺超級準，完全就是這個意思！

在 PowerShell 的世界裡，這個參數的完整名稱是 **`-EncodedCommand`**（因為 PowerShell 支援縮寫，所以寫成 `-Encoded`、`-encoded` 甚至 `-enc` 系統都看得懂）。

它的用意就是大聲告訴作業系統：

> **「報告！我後面要帶入的指令不是普通的英文，而是一串用 Base64 編碼過的 Unicode 字串。請你先幫我『解碼』還原，然後直接執行它！」**

## 為什麼駭客（和網管人員）這麼愛用這個參數？

既然都要執行，為什麼不直接輸入正常的英文指令（明文），非要脫褲子屁股先編碼一次呢？這背後有兩個非常實際的原因：

### 1. 解決「特殊符號」的大災難（相容性）

在寫複雜的指令時，裡面通常會有一堆單引號 `'`、雙引號 `"`、括號 `()`、斜線 `\` 或是管線符號 `|`。

- **直接執行的慘劇**：如果你要把這串指令當作參數傳給別的程式執行，這些特殊符號很容易被系統誤判，導致程式斷在奇怪的地方，直接報錯。

- **編碼後的神奇效果**：經過 Base64 編碼後，不管你的指令原本多複雜，**通通都會變成只由「大小寫英文字母、數字、加號 `+`、斜線 `/` 和等號 `=`」組成的純文字**。這樣傳遞指令絕對不會出錯，堪稱「防呆神器」。


### 2. 躲避防毒軟體的「關鍵字偵測」（混淆/隱蔽）

這是駭客最看重的一點。

- **明文執行**：如果防毒軟體或主機監控（如 EDR）看到指令裡出現 `DownloadData`、`[http://10.99.40.20](http://10.99.40.20)`、`stop-process` 等敏感字眼，警報器立刻就會逼逼作響，並直接攔截。

- **編碼執行**：變成 `JABzAGUAcgB...` 這種鬼畫符後，一些比較陽春的偵測系統（只認關鍵字的那種）就會直接瞎掉，覺得這只是一串普通的資料而放行。


## 它是怎麼運作的？（技術小流程）

如果我們想把一句指令「我是一隻貓」丟給 PowerShell 執行，流程是這樣的：

1. **原始指令**：`Write-Host "我是一隻貓"`

2. **轉換成二進位（UTF-16LE 格式）**：這是 Windows 預設的文字格式。

3. **Base64 編碼**：轉換成 `VwByAGkAdABlAC0ASABvAHMAdAAgACgAIgDmiJHmmK/kuIDpoLrogr9bIik=`。

4. **執行**：

    Bash

    ```
    powershell.exe -EncodedCommand VwByAGkAdABlAC0ASABvAHMAdAAgACgAIgDmiJHmmK/kuIDpoLrogr9bIik=
    ```


PowerShell 看到 `-EncodedCommand`，就會在背景把這串亂碼吐回 `Write-Host "我是一隻貓"`，然後神不知鬼不覺地在螢幕上印出這行字。

這就是為什麼在你的演練日誌裡，會看到那段長達好幾百個字元的「黑魔法」字串了！

---

Python

```
b = b"hello world"
# Let's decode it as UTF-16LE (with ignoring or replacing errors for odd byte length)
try:
    print(b.decode('utf-16le'))
except Exception as e:
    print(e)
    # 11 bytes, so odd number of bytes.
    print(b[:-1].decode('utf-16le'))

```

Code output

```
'utf-16-le' codec can't decode byte 0x64 in position 10: truncated data
敨汬⁯潷汲

```

Python

```
import base64
text = "hello world"
encoded = base64.b64encode(text.encode('utf-16le')).decode('utf-8')
print(encoded)

```

Code output

```
aABlAGwAbABvACAAdwBvAHIAbABkAA==

```

You have run into one of the most classic and amusing "gotchas" in PowerShell!

What you are seeing is a text decoding error called **mojibake** (where characters are garbled because of a mismatch in encoding formats).

Here is exactly what is happening under the hood and how to fix it.

## The Core Problem: UTF-8 vs. UTF-16LE

When you use the `-EncodedCommand` parameter, PowerShell expects the Base64 string to represent a **UTF-16LE (Unicode)** encoded string, where every character is represented by 2 bytes.

However, your Base64 string (`aGVsbG8gd29ybGQ=`) is encoded in **UTF-8 (ASCII)**, where every character is represented by 1 byte.

Because of this, PowerShell tried to decode your 1-byte characters by smashing them together in pairs of 2 to read them as UTF-16LE:

- It took the byte for **`h`** (`0x68`) and **`e`** (`0x65`), combined them into the 2-byte character `0x6568`, which translates to the Chinese character **`敨`**.

- It took **`l`** (`0x6C`) and **`l`** (`0x6C`), combined them, and got **`汬`**.

- It paired **`o`** and (space) to get **`⁯`**.

- It paired **`w`** and **`o`** to get **`潷`**.

- It paired **`r`** and **`l`** to get **`汲`**.

- The leftover **`d`** was orphaned, resulting in the error character ``.


Essentially, PowerShell successfully decoded your Base64 string, got "hello world", but then read it in the wrong language, resulting in **`敨汬⁯潷汲`**, which it then tried (and failed) to run as a command.

## How to Fix It

To make PowerShell understand your command, you must encode it as **UTF-16LE** before turning it into Base64.

### 1. The Quick Fix

The correct UTF-16LE Base64 string for `hello world` is `aABlAGwAbABvACAAdwBvAHIAbABkAA==`. Run this instead:

PowerShell

```
powershell.exe -EncodedCommand aABlAGwAbABvACAAdwBvAHIAbABkAA==
```

_(Note: "hello world" isn't a valid PowerShell cmdlet, so it will still return an error saying 'hello world' is not recognized—but at least it will be in English!)_

### 2. How to Encode Commands Correctly in PowerShell

If you want to generate properly encoded commands in the future, you can use this quick PowerShell snippet to do the heavy lifting for you:

PowerShell

```
# 1. Define your command
$command = "Write-Host 'Hello, World!'"

# 2. Convert it to UTF-16LE bytes
$bytes = [System.Text.Encoding]::Unicode.GetBytes($command)

# 3. Encode those bytes to Base64
$encoded = [Convert]::ToBase64String($bytes)

# 4. Output the result
$encoded
```

## Source: `Inbox/powershell-encodedcommand.md`

沒錯！你的直覺超級準，完全就是這個意思！

在 PowerShell 的世界裡，這個參數的完整名稱是 **`-EncodedCommand`**（因為 PowerShell 支援縮寫，所以寫成 `-Encoded`、`-encoded` 甚至 `-enc` 系統都看得懂）。

它的用意就是大聲告訴作業系統：

> **「報告！我後面要帶入的指令不是普通的英文，而是一串用 Base64 編碼過的 Unicode 字串。請你先幫我『解碼』還原，然後直接執行它！」**

## 為什麼駭客（和網管人員）這麼愛用這個參數？

既然都要執行，為什麼不直接輸入正常的英文指令（明文），非要脫褲子屁股先編碼一次呢？這背後有兩個非常實際的原因：

### 1. 解決「特殊符號」的大災難（相容性）

在寫複雜的指令時，裡面通常會有一堆單引號 `'`、雙引號 `"`、括號 `()`、斜線 `\` 或是管線符號 `|`。

- **直接執行的慘劇**：如果你要把這串指令當作參數傳給別的程式執行，這些特殊符號很容易被系統誤判，導致程式斷在奇怪的地方，直接報錯。

- **編碼後的神奇效果**：經過 Base64 編碼後，不管你的指令原本多複雜，**通通都會變成只由「大小寫英文字母、數字、加號 `+`、斜線 `/` 和等號 `=`」組成的純文字**。這樣傳遞指令絕對不會出錯，堪稱「防呆神器」。


### 2. 躲避防毒軟體的「關鍵字偵測」（混淆/隱蔽）

這是駭客最看重的一點。

- **明文執行**：如果防毒軟體或主機監控（如 EDR）看到指令裡出現 `DownloadData`、`[http://10.99.40.20](http://10.99.40.20)`、`stop-process` 等敏感字眼，警報器立刻就會逼逼作響，並直接攔截。

- **編碼執行**：變成 `JABzAGUAcgB...` 這種鬼畫符後，一些比較陽春的偵測系統（只認關鍵字的那種）就會直接瞎掉，覺得這只是一串普通的資料而放行。


## 它是怎麼運作的？（技術小流程）

如果我們想把一句指令「我是一隻貓」丟給 PowerShell 執行，流程是這樣的：

1. **原始指令**：`Write-Host "我是一隻貓"`

2. **轉換成二進位（UTF-16LE 格式）**：這是 Windows 預設的文字格式。

3. **Base64 編碼**：轉換成 `VwByAGkAdABlAC0ASABvAHMAdAAgACgAIgDmiJHmmK/kuIDpoLrogr9bIik=`。

4. **執行**：

    Bash

    ```
    powershell.exe -EncodedCommand VwByAGkAdABlAC0ASABvAHMAdAAgACgAIgDmiJHmmK/kuIDpoLrogr9bIik=
    ```


PowerShell 看到 `-EncodedCommand`，就會在背景把這串亂碼吐回 `Write-Host "我是一隻貓"`，然後神不知鬼不覺地在螢幕上印出這行字。

這就是為什麼在你的演練日誌裡，會看到那段長達好幾百個字元的「黑魔法」字串了！

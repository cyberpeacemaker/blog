---
title: "Binary vs Text Files"
description: "Explains the practical distinction between human-readable text files and application-specific binary files even though all data is stored as bits."
created: 2026-07-20
updated: 2026-07-20
tags: [dev]
type: reference
lang: zh
status: draft
---

> Related: [[05-Software-Engineering]] · [[text-protocol-base64]] · [[image-binary-to-text-representation]]

You just hit the nail on the head. Technically speaking, **yes, every single file on your computer is a binary file.**

At the lowest level, your hard drive or SSD doesn't care if it's saving a Shakespearean sonnet or a 4K video game—it’s all just billions of 1s and 0s (bits) grouped into 8-bit chunks (bytes).

However, in the world of computing, we draw a line between **"Text" (Non-Binary)** and **"Binary"** files based on **how those bytes are meant to be interpreted**.

Here is how the distinction works in practice:

## 1. Non-Binary Files (Plain Text Files)

When programmers call a file "text" or "non-binary," they mean the data inside is strictly meant to represent human-readable characters.

Every byte in a text file maps directly to a character using a standardized encoding system (like **ASCII** or **UTF-8**). For example, the byte `01000001` always translates directly to the capital letter "A".

- **The Notepad Test:** If you open a text file in a basic text editor like Notepad or TextEdit, it will look perfectly readable.
    
- **Common Extensions:** `.txt`, `.csv`, `.html`, `.json`, `.css`, and source code files like `.py` (Python), `.js` (JavaScript), or `.cpp` (C++).
    

## 2. Binary Files (In the Common Sense)

When we call a file "binary," we mean it contains custom data structures that _cannot_ be interpreted as plain text. The bytes don't represent letters; instead, they represent pixel colors, audio frequencies, compiled machine code, or compressed data.

- **The Notepad Test:** If you try to open a binary file in Notepad, you will get a chaotic wall of unreadable gibberish, weird symbols, and random emoji. The text editor is trying to force those bytes into characters, but the math doesn't line up.
    
- **Common Extensions:**
    
    - **Executables:** `.exe`, `.app`, `.dmg`
        
    - **Media:** `.jpg`, `.png`, `.mp3`, `.mp4`
        
    - **Compressed:** `.zip`, `.rar`, `.tar`
        
    - **Formatted Docs:** `.pdf`, `.docx`, `.xlsx` _(Fun fact: Modern Word documents are actually hidden ZIP files filled with XML code and media, which is why they are binary!)_
        

### Quick Comparison At a Glance

|**Feature**|**Text (Non-Binary) Files**|**Binary Files**|
|---|---|---|
|**What the data represents**|Plain characters and text formatting (like tabs and newlines).|Custom data structures (images, audio, compiled code).|
|**Human Readability**|High (Read it instantly in any basic editor).|Low (Looks like alien gibberish in a text editor).|
|**Software Needed**|Any basic text viewer.|Specific software designed to decode that exact format (e.g., Photoshop for `.psd`).|
|**Corruption Risk**|Low. If a few bytes break, you just lose a couple of letters.|High. If a few bytes break, the whole file might become unopenable.|

Think of it like language: All books are made of ink and paper (binary storage), but "text files" are written in a universal alphabet everyone can read, while "binary files" are written in a highly specialized, encrypted shorthand that only specific programs have the key to translate.

---

雖然在電腦的底層世界裡，所有檔案本質上都是由 0 和 1 組成的，但在日常應用中，我們通常會把檔案區分為**文字檔案（Non-binary / Text file）**與**二進位檔案（Binary file）**。

分辨它們最簡單、最直覺的「暴力測試法」就是：**直接用「記事本」打開它。** 如果看得到看得懂的字，它就是 Non-binary；如果畫面直接口吐白沫、滿滿的亂碼與怪怪的符號，它就是 Binary。

以下為你詳細拆解這兩者的差別：

## 📄 Non-binary 檔案（純文字檔案）

這類檔案完全由**人類可讀的字元**組成。它們使用特定的編碼系統（如 ASCII、UTF-8）將數字轉換成英文字母、漢字或標點符號。檔案中除了文字本身，頂多只有換行符號（LF/CRLF）或空格。

- **特點：**
    
    - 可以用任何簡單的文字編輯器（如 Notepad、VS Code、Vim）直接打開並閱讀、修改。
        
    - 結構通常是「一行一行」的。
        
- **常見副檔名：**
    
    - 純文字：`.txt`、`.csv`（表格數據）、`.log`（日誌）
        
    - 程式原始碼：`.py`、`.js`、`.cpp`、`.html`、`.css`
        
    - 設定檔：`.json`、`.xml`、`.yaml`、`.ini`
        

## 💾 Binary 檔案（二進位檔案）

這類檔案不是為了讓人直接閱讀而設計的，而是為了讓**特定的應用程式或電腦硬體**高效讀取。它們包含任意的二進位位元組（0x00 到 0xFF），這些數據可能代表顏色、音頻頻率、微處理器指令等。

- **特點：**
    
    - 用文字編輯器打開會是一堆無法顯示的亂碼（俗稱「豆腐塊」或奇怪符號）。
        
    - 必須用專用的軟體才能解碼。例如：`.png` 要用圖片檢視器打開，`.mp3` 要用播放器打開。
        
    - 只要改錯其中一個位元組（Byte），整個檔案就可能直接損毀打不开。
        
- **常見副檔名：**
    
    - 執行檔／程式：`.exe`、`.app`、`.dmg`
        
    - 圖片：`.jpg`、`.png`、`.gif`
        
    - 影音：`.mp3`、`.mp4`、`.wav`
        
    - 壓縮檔：`.zip`、`.rar`、`.7z`
        
    - 複雜文件：`.pdf`、`.docx`、`.xlsx`（_註：現代的 Office 檔案本質上是打包了 XML 的壓縮檔，所以歸類在 Binary_）
        

## 📊 快速對比表

| **特性**     | **Non-binary (文字檔案)** | **Binary (二進位檔案)**            |
| ---------- | --------------------- | ----------------------------- |
| **可讀性**    | 人類直接可讀                | 僅限特定軟體／機器可讀                   |
| **用記事本打開** | 顯示正常的文字與程式碼           | 滿螢幕的亂碼與問號                     |
| **資料結構**   | 以「行」為單位，編碼統一          | 連續的位元組流，結構複雜且緊湊               |
| **檔案大小**   | 相對較大（因為文字編碼佔空間）       | 相對較小（資料經過壓縮或特殊編碼）             |
| **修改方式**   | 隨便找個編輯器就能改            | 必須使用對應軟體或十六進位編輯器 (Hex Editor) |

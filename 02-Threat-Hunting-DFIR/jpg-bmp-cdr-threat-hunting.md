---
title: "JPG to BMP CDR and Threat Hunting"
description: "Explains why image conversion can work as CDR for defense but can destroy forensic evidence during threat hunting."
created: 2026-07-22
updated: 2026-07-22
tags: [threat-hunting, dfir]
type: reference
lang: zh
status: draft
---

> Related: [[MOC - Threat Hunting]] · [[YARA]] · [[writeup-guideline]]

你的直覺非常敏銳！你一眼就抓到了關鍵：**因為 JPG 是有損壓縮，丟失的資料永遠回不來了。**

不過，這裡有一個關於 **CDR（Content Disarmament and Reconstruction，內容消毒與重構）** 最常見的觀念誤區：

> **CDR 的「重構 (Reconstruction)」，指的是重構一個「安全的檔案結構」，而不是還原「100% 原始的資料/畫質」。**

事實上，**「資料被破壞/重繪」非但不是 CDR 的缺點，反而是它能成功防禦的核心機制！**

## 為什麼轉檔算是一種 CDR？

惡意份子常利用 JPG 藏匿攻擊程式碼，常見手法包括：

1. **EXIF 標籤藏 Payload：** 把惡意 Shellcode 藏在圖片的拍攝時間、相機型號等欄位。
    
2. **檔案尾端附加（Append Payload）：** 在 JPG 的標準結束標記（`FF D9`）後面，硬串接一個 `.exe` 或 `.ps1` 腳本。
    
3. **利用 Parser 漏洞：** 製作畸形的 JPG 標頭（Header），專門誘發特定的圖片檢視器產生記憶體溢位（Buffer Overflow）。
    

當你把 JPG 解碼並轉存為 BMP 時，程式**只會抓取「螢幕上看得見的像素」**，將其重新填入全新的 BMP 結構中。這意味著：

- EXIF 裡的惡意代碼 ➔ **被丟棄**
    
- 尾端附加的惡意檔案 ➔ **被剝離**
    
- 畸形的標頭漏洞 ➔ **被壓平重構**
    

從防禦（Mitigation）的角度來看，這確實達到了 CDR 的目的：**徹底消滅潛在武器，只留下安全的視覺內容。**

## 從 Threat Hunting（威脅獵捕）的角度來看呢？

如果你站在 **Threat Hunting** 的角度，把 JPG 轉成 BMP 這件事，評價就完全相反了：

### ❌ 缺點：這等於在「破壞犯罪現場」

Threat Hunter 的任務是**找出威脅、了解攻擊者手法（TTPs）**。如果你在分析之前就把 JPG 轉成了 BMP：

- **破壞證據：** 隱藏在 EXIF 或尾端的 Payload 會直接蒸發，你將無法提取攻擊者留下的 C2 伺服器 IP、加密腳本或特徵碼（YARA Rules 丟失）。
    
- **Hash 改變：** 轉檔後檔案的 MD5/SHA256 會完全不同，無法在威脅情報（Threat Intel）庫中匹配已知威脅。
    

### ⭕ 唯一的特例：圖像隱寫術（Steganography）分析

在威脅獵捕中，有一種情境會主動將影像展開：**當你懷疑圖片使用了「隱寫術」時**。

- 攻擊者有時會把機密資料隱藏在像素的最低有效位元（LSB）。
    
- 獵捕者需要將 JPG 解碼為最原始的像素陣列（如 BMP 或 RAW 記憶體資料），才能進行直方圖分析、像素差值比對，把藏在視覺雜訊裡的秘密抓出來。
    

## 總結

- **對「網路安全防禦 (Defensive / Gateway)」而言：** JPG 轉 BMP/PNG 是一種非常粗暴但有效且成本極低的 CDR 手段。
    
- **對「威脅獵捕 (Threat Hunting / Forensics)」而言：** **絕對不能先轉檔！** 你必須保留原始 JPG 的每一個 Byte，才能鑑識檔案結構中的惡意痕跡。
    

你是正在規劃企業內部的 CDR 圖片過濾機制，還是在建立用於分析疑似惡意圖片的威脅分析管道（Pipeline）呢？


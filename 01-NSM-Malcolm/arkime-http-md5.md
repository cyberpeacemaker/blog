---
title: "Arkime HTTP MD5"
description: "Explains Arkime http.md5 as a fast file triage, deduplication, and threat intel pivot."
created: 2026-07-14 20:07
updated: 2026-07-14 20:07
tags: [malcolm, nsm, arkime]
type: reference
lang: zh
status: draft
---

> Related: [[MOC - Malcolm & NSM]] · [[arkime]] · [[arkime-http-md5-bypass]]

既然提到了這個限制，你可能會覺得：「既然這功能在某些情況下會漏，那當初設計它到底有什麼用？」

其實在日常的藍隊（防守方）運維、資安事件調查（Incident Response）與威脅獵捕（Threat Hunting）中，`http.md5` 是一個**極度實用且能幫分析師省下大量時間的「神級功能」**。

它的核心價值可以歸納為以下四個維度：

## 1. 威脅情報（IOC）秒速比對

當攻擊者透過 HTTP 下載惡意程式（例如木馬、後門、Webshell）時，Arkime 會在流量經過的瞬間算出該檔案的 MD5 雜湊值。

- **省去下載還原的時間**：你不需要手動把 PCAP 下載下來、用 Wireshark 還原成 `.exe` 或 `.elf`，再上傳到外部網站。
    
- **一鍵查詢 VirusTotal**：在 Arkime 介面上，你點擊這個 `http.md5` 的值，就能直接連結到 **VirusTotal** 或 **AlienVault OTX**。一秒鐘就能知道這個剛被下載的檔案是不是已知惡意軟體。
    

## 2. 檔案去重與排查（Deduplication & Triage）

在大型企業網路中，每天有成千上萬次檔案傳輸。如果遇到了資安事件：

- **去重分析**：假設你看到有 1,000 個使用者都下載了某個更新檔，如果他們的 `http.md5` 全都一模一樣，你只需要分析其中一個，就可以確保其他 999 次下載也是安全的。
    
- **異常點擊**：如果大家都下載同檔名的檔案，但只有某一個使用者的 `http.md5` 與眾不同，那很可能就是針對性的釣魚攻擊或惡意程式替換。
    

## 3. 歷史威脅獵捕（Threat Hunting）

當資安組織（如 CISA、MND）發布了最新的威脅情資，裡面包含了一串黑客組織愛用的工具 MD5 雜湊值（Hash List）：

- 你可以直接在 Arkime 搜尋列輸入：`http.md5 == [惡意MD5值]`。
    
- 幾秒鐘內，Arkime 就能幫你搜遍過去幾個月的所有流量，確認有沒有員工不小心下載過這個檔案。如果沒有這個欄位，你得把幾 TB 的原始 PCAP 全部解開來比對，那將會是場災難。
    

## 4. 便捷的檔案自動還原 (Carving)

Arkime 內部有儲存機制。當它辨識出 `http.md5` 時，通常代表它已經把這個 HTTP 傳輸的檔案本體暫存起來了。

- 在 Arkime 介面的 "Files" 標籤頁中，你可以直接看到這些被提取出來的檔案列表，並提供「一鍵下載」功能。
    
- 這對 **90% 以上的常規檔案（如 PDF、EXE、ZIP 壓縮檔）** 來說非常完美，只有在遇到極端、漫長的 Keep-Alive 多任務傳輸時才會發生我們前面提到的遺漏問題。
    

> 📌 **一句話總結：**
> 
> `http.md5` 是為了**「大規模快速篩選、比對與威脅情報檢索」**而生的利器；而手動 Carving 原始封包，則是為了**「100% 精準的鑑識與細節重構」**。兩者相輔相成。

你目前是在練習 CTF 藍隊鑑識題目，還是在幫公司建立/運維 Arkime 這套流量監控系統呢？


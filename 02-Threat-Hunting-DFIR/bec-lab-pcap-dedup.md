---
title: "BEC Lab PCAP Dedup"
description: "Explains duplicate BEC lab PCAP ingestion and how to reason about repeated sessions during analysis."
created: 2026-07-15
updated: 2026-07-15
type: reference
lang: zh
status: draft
tags: [threat-hunting, dfir]
---

> Related: [[MOC - Threat Hunting]] · [[bec-pcap-analysis-summary]] · [[cross-id-analysis]]

# BEC Lab PCAP Dedup
這段話是在分析**網路流量分析與實驗室環境建置中「資料重複（Duplication）」的根本原因，並解釋為什麼可以用「雜湊值（Hash）」來安全地進行去重（Deduplication）**。

簡單來說：**這是一起因為實驗室建置腳本寫壞，導致資料被重複匯入了 8 次的烏龍事件，而不是真實的網路異常。**

以下為您逐句拆解與詳細翻譯：

## 核心概念拆解

### 1. 自然原因 vs. 人為複製（為什麼會有 8 倍的資料？）

> **原文：** "Natural causes (SPAN mirroring, TCP retransmit, Arkime session-splitting) would produce varying copy counts and differing framing/timestamps, hence different hashes. A uniform ×8 with identical bytes and identical timestamps means the same capture was ingested/replicated 8 times during the lab build."

- **自然原因（Natural causes）：**

    在真實或正常的網路環境中，如果出現重複封包，通常是因為：

    - **SPAN mirroring（監聽埠鏡像）：** 網路設備設定鏡像時，重複抓到了同個封包。

    - **TCP retransmit（TCP 重傳）：** 封包遺失導致客戶端重新發送。

    - **Arkime session-splitting（Arkime 會話拆分）：** 流量側錄工具 Arkime 因為逾時或連線太長，把同一個連線切成好幾段。

    - _特徵：_ 這些情況產生的重複資料，**數量會是隨機的**，而且封包的標頭（Framing）或時間戳記（Timestamps）會有些微落差，因此**雜湊值（Hash）會不一樣**。

- **人為複製（Lab build 異常）：**

    - 但在這裡，資料呈現**極度規律的「剛好 8 倍（×8）」**，而且每個重複封包的位元組（Bytes）與時間戳記**完全一模一樣**。

    - _結論：_ 這不可能是網路自然產生的。唯一的解釋是：**在建置實驗室環境時，同一個 PCAP（封包擷取檔）被系統重複匯入（Ingest）或複製了 8 次。**


### 2. 去重的安全性

> **原文：** "So: safe and correct to dedup by content hash."

- **解釋：**

    既然確認這 8 倍的資料完全是「人為複製的雜音」，而非真實的網路行為（如 TCP 重傳），我們就可以**非常放心地直接使用內容的雜湊值（Content Hash，如 SHA256）來進行去重（Dedup）**。這樣做完全不會誤刪任何有價值的網路行為數據。


### 3. 現狀分析：為什麼有的地方對、有的地方錯？

> **原文：** "The v1 playbook.json already dedups at the body level via `caldera.dedup_bodies` (sha256), which is why its task/result counts were right — but the per-session transcripts and INDEX.md are 1:1 with sessions, so the ×8 noise shows there."

這解釋了為什麼系統裡的部分資料看起來是正常的，部分卻塞滿了垃圾資料：

- **`playbook.json` 表現正常：**

    因為在第 1 版的 Playbook 中，程式碼已經在「內容主體層級（Body level）」使用了 `caldera.dedup_bodies`（利用 SHA256 雜湊）來進行去重。所以這裡的任務（Task）和結果（Result）數量是正確的，沒有膨脹 8 倍。

- **會話記錄（Transcripts）和 `INDEX.md` 塞滿雜音：**

    但是，每個連線會話（Session）對應的文字紀錄（Transcripts）以及索引檔（`INDEX.md`）是與會話呈 **1:1 關係** 產生的。由於最前端匯入的 Session 本身就被複製了 8 次，而這些檔案生成時**沒有經過去重機制**，所以這 8 倍的垃圾數據（×8 noise）就毫無保留地呈現在這裡了。


## 💡 總結

1. **問題點：** 實驗室環境在建置時，把同一份流量檔案重複匯入了 8 次。

2. **解法：** 直接用 Hash 值把重複的 7 份刪掉（去重）是安全且正確的。

3. **待辦事項：** 雖然 `playbook.json` 已經有去重機制所以沒事，但必須針對會話記錄（Transcripts）和 **`INDEX.md`** 補上相同的去重邏輯，才能把那 8 倍的雜音徹底清除。

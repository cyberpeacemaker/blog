---
title: "Malcolm RITA Integration"
description: "Explains Malcolm, Zeek, OpenSearch, and RITA integration paths for beacon analysis."
created: 2026-07-15 10:07
updated: 2026-07-15
type: reference
lang: zh
status: draft
tags: [malcolm, zeek, rita, opensearch]
---

> Related: [[MOC - Malcolm & NSM]] · [[malcolm-orchestration]] · [[zeek-rita]]

# Malcolm RITA Integration
這是一個非常棒的架構設想！使用 Malcolm 來做網路威脅獵捕是非常專業且主流的選擇。

不過，關於「透過 API 呼叫 OpenSearch/Arkime 的數據並自動串流到 RITA 分析」這個想法，**在實際運作上會遇到硬傷**。

以下為你說明為什麼「直接 API 串流」不可行，以及**業界實際上是如何完美結合 Malcolm 與 RITA 的黃金工作流**。

## ❌ 為什麼「API 查詢 ➔ RITA」這條路走不通？

主要原因在於 **RITA 要求的資料輸入格式非常傲嬌**。

- **RITA 只吃「原始 Zeek 日誌檔」**：RITA 的分析引擎（不論是舊版 MongoDB 還是新版 ClickHouse 核心）在匯入資料時，必須讀取磁碟上的 **標準 Zeek 原始文字日誌**（例如 `conn.log`、`dns.log`、`ssl.log`，格式為 TSV 或 JSON）。

- **OpenSearch/Arkime 的資料已經被「拆解與重構」**：當 Malcolm 把 Zeek 日誌透過 Logstash 送進 OpenSearch 時，資料已經被轉換成了資料庫的索引文件（Document）。

- **格式不相容**：如果你用 API 去 OpenSearch 撈資料，你拿到的是 OpenSearch 的 Query JSON。RITA 並沒有內建「去 OpenSearch/Arkime API 拉取資料並在記憶體中重構回 Zeek 格式」的功能。


如果堅持走 API 這條路，你必須自己寫一個複雜的 Middleware，把 OpenSearch 的資料撈出來、重新拼裝成標準的 `conn.log` 格式、寫入磁碟，再叫 RITA 去讀。這無異於繞了一大圈遠路。

## ✅ 業界正解：直接攔截 Malcolm 的本地 Zeek 日誌

其實，**你根本不需要去動 OpenSearch API！** 因為 Malcolm 在運作時，本來就會在本地主機上產生 RITA 最想要的原始 Zeek 日誌。

### 🛠️ 推薦的資料流架構（雙軌並行）

當你在 Malcolm 上傳 PCAP 或即時側錄流量時，資料流應該長這樣：

Plaintext

```
                       ┌───➔ [Logstash] ───➔ [OpenSearch] ───➔ [你的 API / 儀表板]
[PCAP 檔 / 流量] ➔ [Zeek]
                       └───➔ [本地 Zeek 日誌目錄] ───➔ [RITA 分析] (最順暢！)
```

### 1. 尋找 Malcolm 的日誌源頭

在 Malcolm 的 Docker 部署中，Zeek 容器產生的原始日誌會透過 Docker Volume 對應（Mount）到主機的實體目錄（通常在 Malcolm 安裝目錄下的 `./zeek-logs/`）。

### 2. 讓 RITA 直接讀取該目錄

你只需要寫一個排程腳本（Cron Job 或透過你的專案框架），定期去 Malcolm 的 `./zeek-logs/` 目錄下抓取日誌，並直接餵給 RITA：

Bash

```
# 讓 RITA 匯入 Malcolm 生成的 Zeek 原始日誌
rita import /path/to/malcolm/zeek-logs/ dataset_name
rita analyze dataset_name
```

## 🚀 終極進階玩法：把 RITA 數據「倒灌」回 OpenSearch！

既然你已經有能力透過 API 來 query Malcolm 的 OpenSearch 了，你可以實現一個資安藍隊夢寐以求的 **「自動分析閉環（Closed-loop）」**：

1. **自動分析**：Malcolm 生成 Zeek 日誌，你的腳本自動觸發 RITA 進行 C2 統計分析。

2. **結果匯出**：利用 RITA 的 API 或 CLI（例如 `rita show-beacons`）將分析結果（如 IP、Beacon 分數）匯出為 JSON。

3. **倒灌（Ingest）**：用你的 API 框架**把 RITA 的 Beacon 分析結果送回 Malcolm 的 OpenSearch 裡建立新索引**（例如 `rita-analysis-*`）。

4. **完美呈現**：你就可以在 Malcolm 的 OpenSearch Dashboards 上，直接拉出圖表看「哪些 IP 正在進行 C2 心跳連線」，並點擊直接關聯到 Arkime 看原始封包！


這個閉環工作流不僅完全避開了手動轉換日誌的痛苦，還能讓你的專案框架發揮最大價值。

你目前規劃的這個專案框架，是用什麼程式語言（例如 Python）來撰寫的呢？

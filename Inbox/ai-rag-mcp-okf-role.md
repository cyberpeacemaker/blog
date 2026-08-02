---
created: 2026-08-02 21:08
updated: 2026-08-02 21:08
tags: []
type: reference
lang: en
status: draft
---
在現代的多代理人（Multi-Agent）與 LLM 生態中，**MCP** 與 **OKF** 扮演著「**管道協定**」與「**知識封裝**」這兩個互補的核心角色。

如果把上一題的 RAG 比喻為「圖書館檢索系統」，那麼 **MCP** 就是連接 Agent 與工具的 **「通用傳輸管道（USB-C 接頭）」**，而 **OKF** 則是知識資料的 **「標準書籍排版格式」**。

## 1. MCP (Model Context Protocol) ——「通用連線管道」

- **核心定義：** 由 Anthropic 主導並推動的開放標準，旨在解決 AI Agent 與外部工具/資料庫溝通時「介面不統一」的問題。
    
- **在此資安架構中的角色：**
    
    - **統一工具呼叫介面：** 系統中的 `Extractor`、`Generator` 或 `Verifier` 需要與不同的外部系統互動（如查詢 RAG 資料庫、呼叫 SIEM API、觸發 GATE A 的 `pySigma` 或 `Zeek PCAP replay`）。**透過 MCP，Agent 不需要為每一套工具寫死客製化的 API 程式碼**，而是用統一的標準 Protocol 進行工具發現（Tool Discovery）與呼叫。
        
    - **動態上下文傳遞：** MCP 允許 Agent 在跨代理人協同作業時，以標準格式共享與維護執行狀態，避免上下文（Context）在傳遞過程中流失。
        

## 2. OKF (Open Knowledge Format) ——「領域知識的標準封裝」

- **核心定義：** 由 Google Cloud 推出的開放標準規範，主張使用簡單且人類與 AI 均可閱讀的 Markdown（結合 YAML 結構化 Header）來統一封裝企業內部的領域知識與規格。
    
- **在此資安架構中的角色：**
    
    - **知識規格統一化：** 圖中的 RAG tool 存放著 `ATT&CK`、`STIX`、`protocol specs` 等龐大資料。若資料格式千奇百怪（有的 PDF、有的 JSON、有的內部 Wiki），Extractor 很難精準讀取。OKF 將這些規範統一用 **「Markdown + YAML」** 封裝成概念檔案（Concepts），讓 Agent 一眼就能辨識 `type: stix_schema` 或 `type: protocol_spec`。
        
    - **資安專家與 AI 知識同步（Git-friendly）：** 資安專家可以在 Git 儲存庫中像寫程式碼一樣維護 OKF Markdown 文件；當威脅情報或通訊協定更新時，資安專家更新文件，Agent 就能無縫讀取到最新知識，實現「雙向可讀、無需轉換層」。
        

## 三者如何協同運作？（RAG + OKF + MCP）

三者在架構中的合作關係如下：

|**組件**|**角色與職責**|**在架構中的比喻**|
|---|---|---|
|**OKF (格式)**|將資安規格（ATT&CK, STIX, RFC）以 Markdown/YAML 統一標準進行封裝。|**標準化的書籍格式**|
|**RAG (檢索)**|當 Extractor 遇到特定威脅時，根據需求精準搜尋出相關的 OKF 知識片段。|**智慧圖書館檢索系統**|
|**MCP (管道)**|讓 Sub-Agents (Extractor, Generator, GATE A) 能以標準協定呼叫 RAG 或硬體檢測工具。|**連接 Agent 與工具的 USB-C 線**|

### 💡 完整工作流程情境

1. **Extractor** 收到一封全新的威脅情報，需要查詢 STIX 2.1 的欄位定義與相關協定。
    
2. **Extractor** 透過 **MCP 通訊協定** 傳送查詢請求給 **RAG 檢索器**。
    
3. **RAG** 從內部資料庫中，抓出以 **OKF 格式** 撰寫的 `stix_spec.md` 與 `rfc_spec.md`。
    
4. **Extractor** 讀取結構化的 OKF 內容後，精準轉化出 IOCs 與 TTPs，並將資料傳給 **Generator**。
    
5. **Generator** 產出 Sigma 規則後，再透過 **MCP** 傳送給 **GATE A** 自動執行 `pySigma` 檢驗。


---
created: 2026-08-02 21:08
updated: 2026-08-02 21:08
tags: []
type: reference
lang: en
status: draft
---
在這張系統架構圖中，RAG（檢索增強生成，標示為 **RAG tool**）的角色可以定位為 **「領域知識與標準規範的錨定器（Domain Knowledge & Spec Grounder）」**，也就是整個系統的「精準參考書與規範手冊」。

如果說：

- **多代理人 (Sub-agents)** 是「具備不同專業的協作團隊」；
    
- **Verifier** 是「嚴格審查語意邏輯、尋找邊界案例（Edge cases）的反例質疑者」；
    
- **GATE A** 是「執行層面的硬核定性編譯/測試關卡」；
    

那麼 **RAG 的角色就是確保最前端的情報處理「不幻覺、不脫靶、嚴格遵循資安業界標準」**。

## RAG 在此架構中的 4 大核心角色

### 1. 規格與標準 Mapping（Schema-bound Alignment）

- **圖中標示：** `ATT&CK · STIX · protocol specs` $\rightarrow$ 送入 `EXTRACTOR (schema-bound)`。
    
- **作用：** 從 OSINT（公開來源情報）擷取到的原始文章通常是雜亂無章的自然語言。RAG 會即時檢索最新的 **MITRE ATT&CK 框架編號**（如 `T1059.001`）與 **STIX 2.1 格式規範**，確保 Extractor 輸出 `IOCs + TTPs` 時，不是憑空想像技術名稱，而是嚴格符合資安通用的資料結構（Schema）。
    

### 2. 技術細節與協定補全（Protocol Context Injection）

- **圖中標示：** `protocol specs`（通訊協定規格）。
    
- **作用：** 在研析威脅情報時，情報可能會提到特定的網路封包欄位或異常行為。RAG 為 Extractor 提供權威的 RFC 網路協定規範與技術文件，讓 LLM 能精準理解情報所指的欄位特徵，避免對底層網路行為做出錯誤的判斷。
    

### 3. 下遊生成的「品質提昇器」（降低 Verifier 與 GATE A 的重試成本）

- **作用：** 後續的 `GENERATOR` 需要產出高精準度的 `Sigma`、`YARA` 或 `SIEM query`。
    
- 如果 Extractor 提取出的 TTP 或 IOC 格式混亂，Generator 就極易生成語法錯誤的規則，導致在 `GATE A`（`pySigma` / `yarac compile`）被退件重來（觸發圖中的 auto-correction loop）。RAG 在最前端「把關輸入品質」，能大幅減少後續 Agent 之間的對抗與重試次數。
    

### 4. 動態知識更新（消除 LLM 知識時效性限制）

- **作用：** LLM 模型本身的知識有訓練截止點（Cutoff），且難以記憶龐大且經常更新的攻擊特徵庫。RAG 作為外掛資料庫，無需重新微調（Fine-tune）模型，即可動態導入最新的公開語法規格或威脅情資語料（Public Corpora）。
    

> **總結：**
> 
> RAG 在這個架構中是 **「事實與標準的基石（Grounding Layer）」**。它確保 Extractor 提取出的情報具備「嚴格的標準格式與正確的領域知識」，讓後續的 Generator、Verifier 與 GATE A 都能在正確的基底上進行生成與驗證。


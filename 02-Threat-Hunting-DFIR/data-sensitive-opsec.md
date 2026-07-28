---
title: "Data-Sensitive OPSEC"
description: "Summarizes OPSEC guidance for sanitizing sensitive OT/CI threat-hunting data before sharing or AI-assisted analysis."
created: 2026-07-27
updated: 2026-07-27
tags: [threat-hunting, dfir, nsm, ai]
type: reference
lang: zh
status: draft
---

> Related: [[MOC - Threat Hunting]] · [[opsec]] · [[ai-threat-hunting-capabilities]] · [[MOC - AI Agents]]

這個規則的方向非常正確且必要。關鍵基礎設施（OT/CI）的威脅獵捕最忌諱「獵捕過程本身成為洩密管道（OPSEC Failure）」。你列出的規則已經涵蓋了最核心的實體標識（IP、主機名、廠區名），但實務上還需要進一步補齊「隱性特徵」與「自動化脫敏」的機制。

## 針對現有規則的補充與強化建議

你們目前的規則偏向「明文實體標識」的管控，建議從以下三個維度進行擴充：

### 1. 擴充「隱性敏感資料」清單

除了 IP 和主機名，以下資料在獵捕過程中極易被忽略卻同樣敏感：

- **封包與記憶體檔案：** PCAP 檔、Memory Dumps（裡面常包含記憶體中的明文憑證、Session Token 或內部網路拓撲）。
    
- **系統日誌內隱特徵：** Syslog 中的 MAC 位址、內部使用者帳號（SAM Account Name）、內部 SID、Active Directory 網域 SID。
    
- **路徑與配置文件：** 程式碼或 YARA/Sigma 規則中硬編碼的特定路徑（例如 `C:\Siemens\WinCC\Projects\Facility_A\...`），這會直接暴露廠區使用的 OT 軟體與架構。
    
- **API Key / SSH Key / 憑證檔：** 包含內部簽發的私有 CA 憑證。
    

### 2. 防止「側洩漏與拓撲三角定位（Fingerprinting）」

即使隱藏了 IP 和主機名稱，**特徵組合**依然可能曝露身份：

- **設備特徵檔：** 上傳了包含特定 PLC 型號 + 特定韌體版本 + 罕見 OT 協定（如 S7Comm、GOOSE、DNP3）的完整 Log，攻擊者或 Cloud LLM 能輕易推算出這是哪一家關鍵基礎設施。
    
- **脫敏規則：** 應採用「一致性代換（Deterministic Masking）」，將 `192.168.1.10` 統一轉化為 `IP_SRV_01`，而不是直接刪除，否則會破壞 Log 之間的關聯分析（Correlation）。
    

### 3. 落地執行機制（不能只靠工程師自律）

- **在地端自建工具鏈：** 程式碼管理應使用地端自建的 GitLab / Gitea；若需要 LLM 協助分析 Log 或寫規則，應採用地端推論方案（如 Ollama / vLLM 搭配開源模型），確保數據完全不出 Perimeter。
    
- **自動化脫敏腳本（Sanitization Pipeline）：** 工程師在將任何資料發送給外部夥伴或進行輔助分析前，必須先過一次在地端的 Anonymization 腳本，自動偵測並遮蔽敏感 Pattern。
    

## 國際標準與實務作法

國際上針對關鍵基礎設施與安全威脅情報（CTI）處理，主要參考以下標準規範：

### 1. ISA/IEC 62443（工業自動化與控制系統資安標準）

- **Zone & Conduit（區域與管道）概念：** 獵捕過程中產生的原始 Telemetry（遙測資料）屬於 Control Zone 或 Operational Zone 的資產。未經脫敏與邊界安全設備（Data Diode 或嚴格審查的 Jump Host）過濾，資料**嚴禁跨越 Conduit 傳輸至 Enterprise 網段或 Public Cloud**。
    

### 2. FIRST TLP 2.0（Traffic Light Protocol 交通號誌協定）

這是國際資安社群（如 FIRST、MISP）分享情報的標準：

- **TLP:RED（嚴格限制）：** 獵捕現場獲取的原始 Log、含有真實 IP/主機名/架構的報告。僅限內部 Hunting Team 核心成員知悉，**不得傳播，嚴禁上雲**。
    
- **TLP:AMBER / AMBER+STRICT：** 經過脫敏後的內部 TTPs 分析結果，可限制性地分享給主管機關或同集團廠區。
    
- **TLP:GREEN / CLEAR：** 抽離所有廠區特徵後產生的通用 IOC（如惡意程式 Hash、公開的 C2 IP），可分享給國家級 CERT/ISAC 或資安社群。
    

### 3. NIST SP 800-82 Rev. 3 & SP 800-150

- **NIST SP 800-82 Rev. 3（OT 系統安全指南）：** 明確指出 OT 環境的資料應實施「預設拒絕上雲（Default Cloud Denial）」原則。雲端輔助分析必須建立在 Data Masking 與單向傳輸的前提下。
    
- **NIST SP 800-150（資安威脅情報分享指南）：** 要求組織在分享或外送威脅情報前，必須建立 Standard De-identification Process（標準去識別化流程），明確定義「個人可識別資訊（PII）」與「組織敏感特徵（ASI）」的移除步驟。
    

### 4. CISA（美國資安暨基礎設施安全局）實務做法

CISA 在執行 CI 威脅獵捕時，採用 **Clean Room（乾淨隔離實體環境）** 模式：

1. 現場採集的資料只能匯入 **Air-Gapped（實體隔離）** 的分析工作站。
    
2. 獵捕報告產出後，必須對照 **Sanitization Checklist（脫敏檢核表）** 逐項核對，確定不含敏感拓撲後才進行加密歸檔或上報。
    

目前你們在獵捕過程中，使用的分析工具（如 ELK、Splunk 或分析腳本）是已經完全部署在地端隔離區，還是工程師仍習慣透過個人筆電連網並遠端存取地端環境呢？


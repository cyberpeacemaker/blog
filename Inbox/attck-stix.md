---
created: 2026-08-02 21:08
updated: 2026-08-02 21:08
tags: []
type: reference
lang: en
status: draft
---

在資安威脅情報（Cyber Threat Intelligence, CTI）領域中，**ATT&CK** 和 **STIX** 是兩個最核心的國際通用標準。

簡單來說：

- **ATT&CK** 是 **「駭客攻擊手法的百科全書（字典）」**。
    
- **STIX** 是 **「資安情資交換的通用語言（格式）」**。
    

## 1. MITRE ATT&CK —— 駭客戰術與技術百科全書

- **全稱：** Adversarial Tactics, Techniques, and Common Knowledge
    
- **維護單位：** 美國非營利組織 MITRE
    
- **它是在做什麼的？**
    
    MITRE 收集了現實世界中所有已知駭客組織的真實攻擊行為，將它們歸納成一套矩陣（Matrix）。它將攻擊過程拆解為兩個核心層級：
    
    - **Tactics（戰術 / 駭客的目的）：** 駭客現在想幹嘛？（例如：`Initial Access` 初期存取、`Execution` 執行程式碼、`Exfiltration` 資料外洩）。
        
    - **Techniques（技術 / 駭客的方法）：** 駭客具體怎麼做到？每個技術都有獨一無二的編號（T-Code）。
        
        - _範例：_ `T1059.001` 代表「利用 PowerShell 執行惡意指令」。
            

> **比喻：** ATT&CK 就像是「資安界的病理診斷手冊」，看到某種症狀（攻擊特徵），就能精準查出這是哪種病毒/駭客手法（T-Code）。

## 2. STIX —— 資安情資的通用資料格式

- **全稱：** Structured Threat Information eXpression
    
- **維護單位：** OASIS 國際標準組織
    
- **它是在做什麼的？**
    
    不同的資安工具（如防火牆、SIEM、EDR、威脅情報平台）如果各自用自己的格式記錄情資，系統之間就無法溝通。STIX 定義了一套標準的 JSON 結構（Schema），用來描述「誰（SDA/攻擊者）、在什麼時間、用了什麼工具、攻擊了哪個資產、產生了哪些 IOC（如惡意 IP 或 Hash）」。
    

> **比喻：** STIX 就像是「資安情資的快遞標準箱/通用 JSON 格式」。不論是哪家廠商的設備，只要把情資裝進 STIX 這個標準箱裡，其他設備就能直接讀懂。

## 兩者如何協同運作？

在資安維運與威脅狩獵中，這兩者通常是搭配使用的：

|**項目**|**MITRE ATT&CK**|**STIX**|
|---|---|---|
|**扮演角色**|**內容知識庫**（行為與知識）|**資料載體**（格式與語法）|
|**解決的問題**|「駭客這次攻擊用了什麼手段？」|「我要如何把這個攻擊情資打包發給其他人/系統？」|
|**資料型態**|戰術矩陣、技術編號（如 T1059）|JSON 結構化檔案|

## 回到您最初的資安 Agent 架構圖

在上圖的架構中，RAG 放了 `ATT&CK` 與 `STIX`，運作邏輯如下：

1. **OSINT 抓到原始文章：** 例如網路新聞寫著 _「駭客透過 PowerShell 釣魚郵件下載了惡意程式」_。
    
2. **Extractor 對照 ATT&CK（RAG 檢索）：** 模型檢索 ATT&CK 知識庫，得知這段描寫對應到 `T1566`（Phishing）與 `T1059.001`（PowerShell）。
    
3. **Extractor 輸出成 STIX 格式：** 根據 STIX 規範，將這些 TTPs 與 IOCs 打包成結構化的 JSON 物件，精準交給後續的 `Generator` 去撰寫對應的 Sigma / YARA 聯防規則。

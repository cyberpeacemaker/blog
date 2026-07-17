---
created: 2026-07-17 16:07
updated: 2026-07-17 16:07
tags: []
type: reference
lang: en
status: draft
---
在威脅獵捕（Threat Hunting）的世界裡，從單純「憑直覺看有趣的警報（Alert-driven）」走向「系統化、框架化（Framework-driven）」是提升獵捕效率與成熟度的必經之路。

目前業界有幾個非常成熟、被主流 SOC/MDR 團隊廣泛採用的框架、工作流（Workflow）與成熟度評估模型。

## 1. 經典工作流：The Threat Hunting Loop (SANS / Sqrrl)

這是威脅獵捕最經典、最直覺的 **4 步循環 SOP**。不論你用什麼工具，這幾乎是所有獵捕團隊的日常運作邏輯：

```
   ┌───────────────────────────────────┐
   │                                   │
   ▼                                   │
【 1. 建立假設 】 ──► 【 2. 調查與 Pivot 】
(Hypothesis)         (Investigate)
                         │
                         ▼
【 4. 偵測自動化 】 ◄── 【 3. 發現新 TTP/模式 】
(Enrich & Automate)  (Uncover Patterns)
```

- **Step 1. 建立假設 (Hypothesis)：**
    
    - 例如：「攻擊者可能正在利用最近的 CVE 漏洞，並在網絡內透過特定的 WMI 進行橫向移動。」
        
- **Step 2. 調查與 Pivot (Investigate)：**
    
    - 利用你提到的 **Suricata** 或 **Zeek** 作為 Pivot point，關聯端點日誌（如 Sysmon）、活動目錄日誌（Active Directory logs）等，驗證你的假設。
        
- **Step 3. 發現新 TTP/攻擊模式 (Uncover Patterns)：**
    
    - 在調查過程中，你可能會發現新型態的惡意行為、未曾見過的文件路徑或未知的 C2 IP。
        
- **Step 4. 偵測自動化與回饋 (Enrich & Automate)：**
    
    - **最重要的一步！** 獵捕結束後，將成果轉化為「長期監控的警報規則」（例如：寫一條新的 Suricata 規則或 Yara rule），讓獵捕成果變成常駐防禦，釋放獵捕人員的時間。
        

## 2. 現代企業最實用的框架：PEAK Framework

由知名資安研究團隊 Splunk SURGe 提出的 **PEAK 框架**（Prepare, Execute, Act with Knowledge），是近年非常受到推崇且極具操作性的現代威脅獵捕架構。它將獵捕流程分為三大階段，並定義了**三種獵捕類型**：

### PEAK 的三大階段：

1. **Prepare（準備）：** 定義獵捕目標、研究數據源、撰寫假設（Hypothesis）、規劃分析工具與範圍。
    
2. **Execute（執行）：** 收集並清理數據，透過統計分析、關聯性查詢進行調查，驗證假設。
    
3. **Act with Knowledge（知識化行動）：** 記錄發現、通報事件、**將獵捕邏輯轉化為自動化偵測規則**，並撰寫獵捕報告。
    

### PEAK 定義的三種獵捕類型：

|**獵捕類型**|**核心邏輯**|**適用場景**|
|---|---|---|
|**假設驅動型 (Hypothesis-Driven)**|基於威脅情資、最新漏洞（TTPs）來建立假設並進行驗證。|追查特定 APT 組織或新興漏洞利用。|
|**基線型 (Baseline Hunts)**|針對特定數據源進行基線（Baseline）分析，找出偏離常態的異常。|釐清環境中「正常」的網路流量與系統行為（例如：Zeek weird 統計）。|
|**模型輔助型 (Model-Assisted / M-ATH)**|利用機器學習、統計模型或 AI (LLM) 篩選海量數據，協助獵捕人員。|在極其龐大的日誌海中快速聚焦高風險異常。|

## 3. 情資驅動型標竿：TaHiTI 框架 (Threat Hunting Methodology)

**TaHiTI** 是由荷蘭金融機構與資安社群共同開發的威脅獵捕框架。它的核心理念是 **「威脅情資（CTI）驅動」**：

- 它強調每一場獵捕的起點，都必須源自於**高質量的威脅情資**（例如敵手 TTPs、威脅報告、ISAC 分享的情資）。
    
- TaHiTI 的優勢在於它提供了一套非常精確的 **SOP 指引**，包括如何將情資提煉成「獵捕觸發點（Hunting Trigger）」，以及如何量化評估每一場獵捕的「覆蓋率（Coverage）」與「有效性（Efficacy）」。
    
- 這套框架非常適合已經擁有專職 CTI（威脅情資）團隊，且希望與 Threat Hunter 深度協同的成熟 SOC 團隊。
    

## 4. 如何衡量自己團隊的成熟度？ SANS HMM (Hunting Maturity Model)

當你開始建立 SOP 後，你一定會被問到：「我們的威脅獵捕做得有多好？」這時就可以拿出 David Bianco 提出的 **HMM 評估模型**：

- **HM0 - Initial (初始級)：** 主要依賴自動化警報（Alert-driven）。幾乎沒有主動獵捕。
    
- **HM1 - Minimal (極簡級)：** 開始收集關鍵日誌，偶爾會根據威脅情資指標（如 IP/Hash）去搜尋歷史日誌（IOC-driven）。
    
- **HM2 - Procedural (程序級)：** 能夠導入他人寫好的獵捕程序（SOP/Playbooks），並定期執行（TTP-driven）。
    
- **HM3 - Innovative (創新級)：** 團隊能夠自己分析數據、建立全新的假設，並撰寫出新的獵捕方法。
    
- **HM4 - Leading (領先級)：** 幾乎將所有成功的獵捕流程自動化，並轉化為常態性的偵測機制。
    

### 🚀 給你的落地實踐建議

如果你想在目前的團隊中落實，最快、最不痛苦的 SOP 導入路徑是：

1. 以 **The Threat Hunting Loop** 作為團隊溝通的基礎心態。
    
2. 採用 **PEAK 框架** 的流程來寫你的第一份 **Hunting Playbook**。
    
3. 每次獵捕完，強迫團隊必須有 **"Act"（轉化為自動化偵測）** 的產出，如此一來，你們的獵捕成熟度就會在 short order 內直接從 HM1 躍升到 HM3！
    

你目前所處的組織，是否有專門負責威脅情資（CTI）的團隊可以提供輸入，還是主要由你們這些 Hunter 兼任情資收集與分析呢？


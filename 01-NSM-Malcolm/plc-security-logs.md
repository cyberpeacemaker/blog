---
title: "PLC Security Logs and OT Cost Tradeoffs"
description: "Explains why small PLCs often expose telemetry instead of security logs and why OT security requirements push controls to network layers."
created: 2026-07-20
updated: 2026-07-20
tags: [nsm, threat-hunting]
type: reference
lang: zh
status: draft
---

> Related: [[MOC - Malcolm & NSM]] · [[ot-hmi-ews-plc-rtu]] · [[critial-infrastructure]]

你的這個比喻非常精準，完全點出了**IT（資訊技術）思維**與**OT（營運技術）現實**之間最大的鴻溝！

「電腦 100 $\rightarrow$ 110」大家覺得理所當然，因為電腦本來就是通用運算設備，多花 10% 買安全合情合理。但「PLC 10 $\rightarrow$ 20」是**成本直接翻倍**，在講求毛利與量產的工業自動化領域，這對廠商和採用者來說都是巨大的衝擊。

對於你提到的現象，我有幾個深層的看法：

## 1. 廠方的反應是正常的：Telemetry $\neq$ Security Log

當被問到資安紀錄時，廠方回「蝦？」並拿出開關紀錄，這反映了目前的現狀。

- **Telemetry（遙測資料）**：關注的是「功能與狀態」（燈有沒有亮？PLC有沒有在跑？）。
    
- **Cybersecurity Log（資安日誌）**：關注的是「誰在什麼時間、用什麼權限、執行了什麼安全敏感的操作」（例如：誰嘗試了錯誤的密碼？誰在刷寫新的韌體？）。
    

對小PLC來說，光是記錄遙測資料就已經快把那點可憐的記憶體（Memory）和運算資源榨乾了，根本沒有餘力去跑加密演算法或儲存詳細的稽核日誌。

## 2. 為什麼國際趨勢（如 IEC 62443、歐盟 CRA）硬要推？

既然成本影響巨大，為什麼國際法規（例如歐盟即將實施的《網路韌性法案》Cyber Resilience Act）還是強推「Security by Design」，連簡單的連網設備都不放過？

> **核心原因在於：駭客要的不是你的「電燈」，而是你的「跳板」。**

在現代工廠中，一個控制電燈或排風扇的微型 PLC，如果跟核心的生產線 SCADA 系統連在同一個網路內，駭客就能把這個「最弱的節點」當成突破口（Lateral Movement）。歷史上著名的 Target 百貨資安事件，駭客就是透過空調系統（HVAC）的憑據一路摸進核心刷卡系統的。

## 3. 現實的骨感：小PLC可能永遠無法「10 $\rightarrow$ 20」

如同你所說，要小PLC直接在硬體上提升資安等級，成本太高。因此，業界未來的發展大概不會是讓 PLC 本身變得像電腦一樣強大，而是走以下兩條路：

- **輕量化資安標準**：不要求小 PLC 做複雜的行為分析，只要求最基本的「韌體簽章（Firmware Signing）」和「關閉預設密碼」，把成本壓在 10 $\rightarrow$ 11 以內。
    
- **網路層代打（MDR/邊緣網關）**：PLC 繼續保持愚蠢和便宜（10元），但在它前面放一個便宜的工業防火牆或通訊閘道器（Gateway），由這個網關來負責加密和阻擋攻擊。
    

你這個「10 $\rightarrow$ 20」的成本比例論述非常中肯。在你的實務經驗或觀察中，你覺得台灣的製造業客戶，會願意為了符合這種國際資安法規而多掏錢，還是會傾向用「網路實體隔離（Air-gapped）」這種傳統速成法來規避？


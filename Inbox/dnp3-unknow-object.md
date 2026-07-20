---
created: 2026-07-20 15:07
updated: 2026-07-20 15:07
tags: []
type: reference
lang: en
status: draft
---
這個資安警報（Rule ID: 2270004）屬於工控系統（ICS/SCADA）網路安全領域。簡單來說，**Suricata 在監聽網路流量時，發現了 DNP3 協定中「查不到字典」的神秘代碼。**

為了讓你完全理解，我們把這個警報拆解成「通訊機制」、「觸發原因」與「排查步驟」來細說：

## 1. 核心背景：什麼是 DNP3 的 Object 與 Variation？

DNP3（Distributed Network Protocol 3）是電力、水力等基礎設施常用的通訊協定（例如控制中心與變電所的設備對話）。為了讓溝通更有效率，DNP3 把所有的數據都**標準化與物件化**：

- **Object Group（物件群組）：** 定義資料的「大分類」。例如：
    
    - Group 1：數位輸入（Binary Input，如開關狀態）
        
    - Group 30：類比輸入（Analog Input，如電壓、溫度）
        
- **Variation（變體）：** 定義資料的「細部格式」。例如在 Group 30（類比輸入）之下：
    
    - Variation 1：32 位元有正負號的整數
        
    - Variation 2：16 位元有正負號的整數
        

當主控端（Master）向設備（Outstation）要資料，或者設備主動回報時，封包裡一定會包含特定的 Group 和 Variation 數字（例如：`Group 30, Variation 2`）。

## 2. 為什麼會觸發這個警報？

Suricata 的內建解碼器（Parser）存有一份標準的 DNP3 官方字典（依據 IEEE 1815 標準）。當解碼器解析封包時，**看到了不合常理、不存在於標準定義中的 Group 或 Variation 數字**，就會觸發 `DNP3 Unknown object`。

這通常由以下四種情況引起：

### A. 廠商自訂的私有擴充（最常見的誤報原因）

許多工控設備廠商（如 ABB、Siemens、Schweitzer Engineering Laboratories）為了實現特殊功能，會在官方標準之外，自行定義私有的 Object Group（例如官方沒定義的 Group 110）。

- **結果：** 設備運作完全正常，但標準的 Suricata 認不出它，進而誤報（False Positive）。
    

### B. 網路雜訊與封包損毀

工控環境可能存在電磁干擾，或者網路線路不穩定，導致資料在傳輸過程中位元翻轉（Bit Flip）。

- **結果：** 原本合法的 `Group 1` 意外變成了 `Group 99`，Suricata 解析失敗而告警。這種情況通常是偶發性的。
    

### C. 惡意攻擊與模糊測試（Fuzzing）

攻擊者可能正在對工控設備進行**漏洞探測**或 **Fuzzing 測試**（故意發送亂碼封包，看設備會不會當機）。

- **結果：** 如果伴隨大量的類似告警，且來自非預期的 IP，極可能是攻擊者試圖利用未知的協定漏洞來癱瘓 PLC 或 RTU。
    

### D. Suricata 版本過舊

DNP3 標準（IEEE 1815）隨時間有進行修訂與更新。如果 Suricata 規則或解碼器版本太老舊，可能就無法識別新標準中加入的合法物件。

## 3. 資安分析師（SOC）該如何處置？

收到這個警報時，建議啟動以下排查流程：

1. **抓取 PCAP 封包：** 這是最重要的步驟。撈取該警報觸發時的原始網路流量。
    
2. **比對設備手冊：** 查看來源與目的 IP 是什麼設備（哪家廠商的 PLC/RTU？）。翻閱該設備的 **DNP3 Device Profile**（每台工控設備都會附帶這份文件），檢查廠商是否真的有使用自訂（Proprietary）的 Object Group。
    
3. **評估流量行為：**
    
    - 如果這是**長期、定期**出現的流量，且設備運行正常 $\rightarrow$ 通常是**廠商私有擴充**，建議針對該 IP 區段將此 Rule 進行優化或加白（Suppress/Disable）。
        
    - 如果這是**突發性、大量**出現，且來自外部或非管理網段 $\rightarrow$ 必須懷疑是**惡意掃描或攻擊**，應立即隔離相關 IP。
        

這個警報目前是在你的實際生產環境中大增，還是你在進行資安設備的建置與測試呢？


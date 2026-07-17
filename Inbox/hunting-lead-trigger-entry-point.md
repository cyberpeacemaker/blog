---
created: 2026-07-17 16:07
updated: 2026-07-17 16:07
tags: []
type: reference
lang: en
status: draft
---

在 Cyber Threat Hunting（威脅獵捕）的領域中，你直覺想到的 **Pivot** 和 **POI** 都非常貼近，但在英文的專業資安術語中，它們的用法與情境有些微的差異。

以下為你整理最道地、最常在威脅獵捕報告或日常工作（Standup, Handover）中使用的英文說法：

## 1. 最推薦、最標準的說法：Pivot (動詞/名詞)

在資安調查中，**Pivot**（樞紐/關聯分析）是最核心的動詞。當你以 Suricata alert 或 Zeek notice 為起點，去追查其他關聯資料（例如：端點日誌、PCAP、處理程行為）時，這個動作就叫做 **Pivoting**。

如果你想表達「以這些警報為切入點/支點」，你可以這樣說：

- **Pivot off of / Pivot from [Alerts]** (動詞用法，極常用)
    
    > _"We will **pivot off of** the Suricata alerts to search for suspicious endpoint activities."_
    > 
    > （我們將以 Suricata 警報為切入點，去搜尋可疑的端點活動。）
    > 
    > _"Let's **pivot from** this Zeek notice to see if there are any related DNS queries."_
    > 
    > （讓我們從這個 Zeek notice 切入，看看有沒有相關的 DNS 查詢。）
    
- **Pivot Point** (名詞用法)
    
    > _"Suricata alerts, Zeek notices, and Zeek weird logs are great **pivot points** for our hunt."_
    > 
    > （Suricata 警報、Zeek notice 和 Zeek weird 日誌是我們獵捕非常好的切入點/關聯點。）
    

## 2. 獵捕理論中最正式的詞：Hunting Lead (獵捕線索)

在威脅獵捕的框架中（例如 Mitre ATT&CK 或各種 Hunting Methodology），獵捕的「起點」或「觸發點」通常不叫 POI，而是稱為 **Lead**（線索）。

Suricata alert 或 Zeek weird 就是標準的 **Hunting Leads**（或 Trigger）：

- **Hunting Lead / Threat Lead**
    
    > _"We are using Zeek weird logs as a **hunting lead** to look for potential data exfiltration."_
    > 
    > （我們正將 Zeek weird 日誌作為獵捕線索，來尋找潛在的資料外洩。）
    > 
    > _"These alerts serve as our initial **hunting leads**."_
    > 
    > （這些警報是我們最初的獵捕線索。）
    

## 3. 其他常見的「切入點」說法

除了 Pivot 和 Lead 之外，以下幾個字在英文討論中也非常自然：

- **Entry Point (入口點 / 切入點)**
    
    > _"The Zeek notice is our **entry point** into this investigation."_
    > 
    > （這個 Zeek notice 是我們進入這次調查的切入點。）
    
- **Starting Point (起點)**
    
    > _"Using Zeek weird as a **starting point**, we can map out the attacker's lateral movement."_
    > 
    > （以 Zeek weird 作為起點，我們可以描繪出攻擊者的橫向移動。）
    

## 4. 關於 "POI" 的補充說明

在威脅獵捕中，**POI**（Point of Interest）雖然能被聽懂，但它在資安界有以下微調：

- **通常指實體（Entities），而非事件：**
    
    在數位鑑識（DFIR）或威脅情資（CTI）中，大家比較常把特定的 IP、Domain、Hash 或帳號稱為 **POI (Point of Interest)** 或 **IOI (Indicator of Interest)**。
    
- **警報本身：**
    
    對於 Suricata alert 或 Zeek weird 這種「日誌/警報事件」，用 **Lead**、**Trigger** 或 **Pivot point** 會比說 POI 來得更加道地。
    

### 💡 總結速查表

| **中文想表達的意思**    | **推薦英文術語**                    | **實戰造句範例**                                              |
| --------------- | ----------------------------- | ------------------------------------------------------- |
| **從...切入/關聯分析** | **Pivot off of...**           | _"We can **pivot off of** these Zeek weird logs."_      |
| **...是很好的切入點**  | **...is a great pivot point** | _"Suricata alerts are great **pivot points**."_         |
| **作為獵捕起點/線索**   | **...as a hunting lead**      | _"Let's use this Zeek notice as our **hunting lead**."_ |
| **調查的入口**       | **Entry point**               | _"This alert is our **entry point** for today's hunt."_ |

---
created: 2026-07-17 21:07
updated: 2026-07-17 21:07
tags: []
type: reference
lang: en
status: draft
---
你完全抓到這些框架的精髓了！

  

沒錯，不論是 SANS、PEAK 還是 TaHiTI，剝開華麗的學術外衣，它們的核心骨架就是這三個骨幹：**「產出假設 ──► 驗證假設 ──► 轉化自動化偵測」**。只要這三點動起來，你的威脅獵捕引擎就已經在運轉了。

  

至於你提出的想法：**「先不考慮即時 CTI，直接用 MITRE ATT&CK 框架來產生 Hunting Ticket」**——這在業界其實是一個**非常經典、而且極度推薦的「神級起手式」**！

  

在資安領域，這被稱為 **Framework-Driven Hunting（框架驅動型獵捕）** 或 **ATT&CK-Driven Hunting**。以下為你分析為什麼這個做法非常棒，以及你該如何漂亮地落地。

  

---

  

## 為什麼「MITRE 產生 Ticket」是非常棒的策略？

  

### 1. 解決「不知道要獵捕什麼」的痛點

  

很多團隊剛開始獵捕時，最常遇到的瓶頸是：「今天坐在電腦前，到底要找什麼？」

直接看 MITRE ATT&CK 矩陣，等於把駭客所有的「考題」都列出來了。你只需要一題一題去解，完全不用憑空想像。

  

### 2. 與你現有的 Zeek / Suricata 完美契合

  

MITRE ATT&CK 的每個技術（Technique）都會列出 **Data Sources（數據源）**。

例如：

  

* **T1071 (Application Layer Protocol)** ── 數據源直接指向 Web Traffic、DNS Queries，這正是 **Zeek** 的強項！

* **T1043 (Commonly Used Port)** ── 這可以直接對應到 **Suricata** 的特定 Alert 與流量特徵。

  

### 3. 進度可視化（Metrics & Board）

  

用 Ticket（如 Jira, GitLab Issues）來管理獵捕，能讓你的工作從「虛無飄渺的通靈」變成「看板上的工程指標」。你可以清楚地向主管展示：「我們本季針對 MITRE 框架中的 15 個技術進行了主動獵捕，其中 3 個轉化成了自動化警報。」

  

---

  

## 實務 SOP：如何把 MITRE 變成一張張 Hunting Ticket？

  

你可以設計一個標準的 **Ticket 範本**，每當你要發起一次獵捕，就開一張 Ticket。範本結構可以長這樣：

  

> ### 🎫 Hunting Ticket Template

>

>

> * **Ticket 主旨：** `[Hunt] T1071.001 - Web Protocols (Zeek DNS/HTTP Focus)`

> * **MITRE 技術：** [T1071.001](https://attack.mitre.org/techniques/T1071/001/) (Application Layer Protocol: Web Protocols)

> * **獵捕假設 (Hypothesis)：**

> * *「我們假設組織內有受駭主機正在透過不尋常的 HTTP/HTTPS 流量（例如：異常的 User-Agent、固定頻率的 Beaconing）向外部 C2 進行通訊。」*

>

>

> * **所需數據源 (Required Data Sources)：**

> * `zeek_http` (尋找異常 User-Agent、非瀏覽器產生的 HTTP 請求)

> * `zeek_conn` (分析連線頻率、連線持續時間)

> * `suricata_alerts` (交叉比對是否有相關特徵警報)

>

>

> * **獵捕步驟 (Playbook/Queries)：**

> * *(在此處貼上特定的 Splunk/KQL/ELK 查詢語法，方便之後重複執行)*

>

>

> * **獵捕結果 (Outcome)：**

> * [ ] 未發現異常 (Negative Hunt)

> * [ ] 發現異常活動，已轉交 IR 處理 (True Positive)

> * [ ] 發現防禦盲點，已新增/優化 [X] 條偵測規則 (Detection Engineered)

>

>

>

>

  

---

  

## 給你的 2 個關鍵避坑指南 (Pro-Tips)

  

雖然這個做法很棒，但 MITRE ATT&CK 矩陣非常龐大（有幾百個子技術），如果盲目亂開 Ticket，團隊很快就會崩潰。建議你採取以下兩個過濾機制：

  

### 1. 數據源可行性過濾（Data Feasibility）

  

在開 Ticket 之前，先問自己：**「我們有這個日誌嗎？」**

  

* 如果想獵捕 **T1059 (PowerShell 惡意執行)**，但你們目前端點沒有收 Sysmon 或 Windows Event Log 4688，那這張 Ticket 就先不要開。

* 既然你手上有 **Suricata** 和 **Zeek**，首波 Ticket 應該**全數聚焦在「網路層（Network-based）」的技術**（例如：Exfiltration Over Alternative Protocol, Domain Generation Algorithms (DGA), Command and Control）。

  

### 2. 優先級篩選（Prioritization）

  

不要從 T1001 一路排到 T1600。你可以參考紅隊報告（如 Red Canary Threat Detection Report）或是 CISA 每年公布的「最常被利用的漏洞/技術」Top 10。

  

* **優先挑選「最常見」且「你們能看得到」的技術來做。**

  

---

  

### 💡 總結

  

你提出的「MITRE 產生 Ticket」是非常務實且具有高度產業水準（Enterprise-ready）的作法。它避開了即時情資的雜亂干擾，讓你們能專注在「打底（Posture Hardening）」——把環境中常見的攻擊路徑，用 Zeek 和 Suricata 掃描、清理過一遍。

  

你目前打算先從 MITRE 矩陣中的哪一個戰術（Tactics，例如：Initial Access, Command and Control, Exfiltration）開始著手挑選技術呢？

---

  

網路上每天都有最新一手的威脅情報與分析報告（威脅情報，CTI）。這些報告裡通常塞滿了各種 **IOC（藍色/惡意 IP、惡意網域、檔案 Hash 等）**。

  

答案是：**非常有用，但「用法」決定了你是高階的獵人，還是疲於奔命的打地鼠工人。**

  

如果只是拿到 IP 就去搜尋，這在資安界被稱為「**Whack-a-Mole（打地鼠）**」——因為攻擊者每秒都能更換 IP 和 Hash。在著名的 **Pyramid of Pain（痛苦之金字塔）** 理論中，Hash 和 IP 處於最底層，對攻擊者來說換掉它們「毫無痛覺」。

  

---

  

## 如何正確使用最新報告中的 IOC？

  

為了不讓日常獵捕被淹沒在瑣碎的 IOC 中，建議你將這些報告轉化為以下三種實戰用法：

  

### 1. 進行「回溯獵捕」(Retro-Hunting) —— 檢查過去是否中招

  

當新報告出爐時，裡面的惡意 IP 或網域往往是「最近幾天/幾週」才活躍的。這時你要做的是：**拿著這些 IOC，往回搜歷史日誌。**

  

* **怎麼做：** 寫一個簡單的 Query，在你的 **Zeek (conn, dns, http)** 歷史日誌（例如過去 30 天或 90 天）中，搜尋是否有主機與報告中的惡意 IP 或 DGA（網域產生演算法）網域進行過連線。

* **價值：** 這能幫你確認「在防禦規則更新之前，我們是否已經被滲透了？」

  

### 2. 行為特徵提煉 (TTP Extraction) —— 轉化為你的 MITRE Ticket

  

這是在威脅獵捕中**最高價值**的用法。讀報告時，不要只看附錄的 IP 清單，要看**內文描述的攻擊手法（TTPs）**。

  

> **舉個例子：**

> 報告寫道：「攻擊者入侵後，利用 PowerShell 下載了工具，並產生了大量異常的 `User-Agent: Mozila/5.0`（注意：拼錯了，少了一個 `l`）。」

> * **轉化為 Ticket 的思維：**

> * IP 可能會變，但攻擊者粗心寫錯的 User-Agent 或工具特徵不容易變。

> * 這時你就可以開一張 Hunting Ticket：`[Hunt] T1071.001 - Detect Typos in Web User-Agents`。

> * 利用你的 **Zeek HTTP logs** 寫一條查詢語法，撈出所有含有拼寫錯誤或不尋常的 User-Agent。

>

>

>

>

  

### 3. 自動化防禦阻斷 (Automated Ingestion) —— 讓機器做苦工

  

手動去搜幾百個 IP 是在浪費獵人的生命。重複性高、技術含量低的 Static IOC，應該直接交給自動化。

  

* **怎麼做：**

1. 將報告中的 IP/Domain 匯入到你的 **TIP（威脅情資平台，如 MISP）** 或 SIEM 中。

2. 利用這些 Feed 自動產生 **Suricata 規則** 進行阻斷，或是自動觸發防火牆（Firewall）阻擋。

3. 獵人只要負責看自動化比對成功後彈出的 Alert 即可。

  
  
  

---

  

## 實戰工作流：當你看到一份新報告時

  

你可以把新報告的處理流程併入你現有的 **Jira / Ticket 工作流**中：

  

```

收到最新威脅報告

  │

  ├──► [ 動作 A ] 靜態 IOC ──► 丟給 SIEM / MISP 自動比對歷史紀錄 (Retro-hunt 30天)

  │

  └──► [ 動作 B ] 提取 TTP ──► 評估：「我們看得見這行為嗎？」(Zeek/Suricata 有收這日誌嗎？)

                                 │

                                 └──► 是 ──► 新增一張 MITRE Hunting Ticket，排入下週獵捕時程！

  

```

  

這樣一來，你的威脅獵捕既有「架構驅動（MITRE 矩陣打底）」的穩健，又保有「情資驅動（最新報告）」的靈活性。

  

你目前所使用的日誌保存機制（Retention Policy），通常能夠支持你往回追溯（Retro-hunt）多久以前的 Zeek 或網路流量紀錄呢？


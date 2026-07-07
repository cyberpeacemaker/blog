---
created: 2026-06-11
tags: [software]
type: reference
lang: zh
status: draft
---

## 1. 關於 SoC 與你的直覺

### SoC 是什麼的縮寫？

> **SoC** 代表 **Separation of Concerns（關注點分離）**。

你腦中浮現的 **Separation of Duty (SoD，職責分離)** 其實也沒錯，但它更多時候是用在資訊安全（Information Security）或組織管理領域（例如：開發人員跟部署人員要分開、記帳跟出納要分開，以防弊端）。

而在**軟體架構**中，我們講 **Separation of Concerns (SoC)**。它的核心想法是：**「程式碼中的每一個模組、類別（Class）或函數（Function），都應該只專注做好一件事情（一個 Concern）。」**

* **壞例子（攪和在一起）：** 一個畫面的按鈕點擊事件裡，同時寫了「UI 動畫」、「檢查欄位格式」、「打 API 傳資料」、「處理資料庫寫入」。這樣只要資料庫一換，你連 UI 都要跟著改。
* **好例子（SoC）：** 畫面只管顯示（UI Concern），API 模組只管連線（Network Concern），資料庫模組只管存取（Storage Concern）。

掌握了 SoC 的心法後，我們才能看懂 **Design Pattern** 與 **Clean Architecture**。

---

## 2. Design Pattern（設計模式）

設計模式是**微觀（Micro）**的解決方案。它是過去幾十年來，無數頂尖工程師在物件導向程式設計（OOP）中遇到常見問題時，總結出來的**「最佳實踐模板」**。

它不是現成的代碼，而是一種**概念框架**。經典的 GoF（Gang of Four）將其分為三大類：

* **創建型（Creational）：** 解決「如何優雅地建立物件」的問題。
* *例如 Singleton（單例模式）：* 確保整個專案中某個類別（如資料庫連線、Log 紀錄器）永遠只有一個實例。


* **結構型（Structural）：** 解決「如何將類別或物件組裝成更大的結構」的問題。
* *例如 Adapter（轉接器模式）：* 把原本介面不相容的兩個東西串起來，就像出國用的插頭轉接頭。


* **行為型（Behavioral）：** 解決「物件之間如何溝通、分配職責」的問題。
* *例如 Strategy（策略模式）：* 根據不同的狀況切換不同的演算法。在你的 `BEC_2` 中，如果針對不同的漏洞（Exploit）有不同的攻擊手法，就可以用策略模式動態切換。



---

## 3. Clean Architecture（乾淨架構）

如果說 Design Pattern 是房間裡的「家具擺設技巧」，那麼 Clean Architecture 就是整棟房子的「結構藍圖」。它是宏觀（Macro）的架構設計，由 Robert C. Martin (Uncle Bob) 提出。

Clean Architecture 的核心是一圈一圈的同心圓，其最神聖的鐵律是「依賴規則（Dependency Rule）」：程式碼的依賴方向只能由外向內，內圈絕對不能知道外圈的任何事情。

### 核心分層（由內到外）：

1. **Entities（企業業務邏輯 / 核心本體）：** 最內圈。保護最核心的業務邏輯或資料模型，這部分程式碼最穩定，不論外部工具怎麼換，這裡都不應該變。
2. **Use Cases（應用程式業務邏輯）：** 實現系統的各種功能流程（例如：執行一次漏洞掃描流程）。它會去操作 Entities。
3. **Interface Adapters（介面轉接層）：** 負責轉換資料。把外圈（如資料庫、網頁框架）的資料轉換成內圈 Use Cases 看得懂的格式。常見的 MVC 中的 Controller、Presenter 就在這一層。
4. **Frameworks & Drivers（框架與驅動）：** 最外圈。諸如資料庫（MySQL/MongoDB）、Web 框架（Flask/Express）、UI 介面、或是你用的第三方工具。這一層是最容易變動的。

### 為什麼要這麼麻煩？

因為它帶來了極高的**解耦（Decoupling）**：

* **獨立於框架：** 你的核心邏輯不會被特定框架綁死。哪天想把 Web 框架換掉，內圈的 Use Cases 紋絲不動。
* **可測試性（Testability）：** 內圈業務邏輯可以在沒有資料庫、沒有 UI 的情況下，單獨進行單元測試（Unit Test）。

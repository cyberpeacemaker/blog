---
created: 2026-06-11
tags: [threat-hunting, dfir]
type: reference
lang: zh
status: draft
---

## 1. Project Building Methodology（專案建構論）

你提到對「初始結構」與「專案成長中的維護」有了通用認知，這非常棒。專案最怕一開始疊床架屋，或是後期膨脹時失控。

* **過度設計（Over-engineering）的拉鋸：** 剛從其他專案吸收經驗回來時，很容易想把所有厲害的 Design Pattern 或 Clean Architecture 全套進去。建議在 `BEC_2` 採取 **"Pay as you go"（漸進式擴充）** 的策略，初始結構保持輕量、職責分離（SOC），但留好擴充介面。
* **Survey 的威力：** 盲目寫 code 往往會流於土法煉鋼。在動手前先針對相似開源專案進行 Survey，定義出 **Blueprint（藍圖）**，可以幫你省下後期 80% 的重構時間。

## 2. AI Utilizing Methodology（AI 應用論）

看來你已經摸索出 AI 的「進階正確打開方式」，不再只是把 Claude 當成進階版 Google，而是當成一個**協作夥伴**。

* **你目前掌握的（Rule, Skills, Dynamic Workflow）：** 這代表你已經在實作「脈絡控制（Context Engineering）」。給予 AI 明確的角色、可用的 Tools/Skills，並根據當前狀態動態調整工作流，這正是目前業界最推崇的 Prompt Engineering 核心。
* **你列出的那些「厲害名詞」：** 不用被這些名詞嚇到，它們其實可以串成一條線。為了讓你之後探索心裡有個底，我幫你做個簡單的分類藍圖：

```
                    ┌─────── AI 驅動核心 (LLM) ───────┐
                    │  雲端/商用: Claude, GPT-4       │
                    │  本地/開源: Llama-3             │
                    │  本地執行引擎: vLLM / Ollama    │
                    └───────────────┬─────────────────┘
                                    │
       ┌────────────────────────────┼────────────────────────────┐
       ▼                            ▼                            ▼
【知識增強 (RAG)】           【Agent 框架 / 工作流】       【工具與協議 (MCP)】
擴充 AI 的大腦記憶，          LangGraph: 複雜圖形狀態機     Model Context Protocol:
讓它能讀取你的私有文件        Langflow: 可視化拖拉工作流     統一 AI 讀取本地檔案或
或專案代碼。                 (適合把你的 Dynamic Workflow  外部 API 的標準介面。
                             具現化)

```

> 💡 **強烈建議：** 在翻修 `BEC_2` 時，可以優先了解 **MCP (Model Context Protocol)**。因為你手上有公司提供的 Claude，MCP 可以讓 Claude 直接與你本地的開發環境、檔案系統或資料庫互動，對重構專案會是超級神兵。

## 3. CTF Playbook Create Methodology（CTF 劇本論）

CTF（奪旗賽）是一個時間壓力極大、且極度依賴「知識重用」的場景。將其自動化、劇本化是非常有遠見的做法。

* **Playbook 範本設計：** 建議採取「模組化」與「參數化」。例如把 Scan、Exploit、Post-Exploitation 分開，並將 Target IP, Ports 等變數抽離。
* **AI 與 Playbook 的結合點：** 你可以把你的 Playbook 範本當成 `Skills` 餵給 Claude，結合你前面提到的 Dynamic Workflow。讓 AI 根據當前 CTF 題目回傳的 Banner 或漏洞特徵，**自動選擇並生成對應的 Playbook 腳本**，這會直接變成一個自動化 Cyber Attack/Defense Agent 的雛形。


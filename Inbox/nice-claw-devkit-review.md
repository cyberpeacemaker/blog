---
created: 2026-07-14 17:07
updated: 2026-07-14 17:07
tags: []
type: reference
lang: en
status: draft
---
你的直覺非常敏銳，一眼就抓到了這份 Devkit 最核心的設計亮點。

這份文件展示了一個非常前沿且成熟的 **「AI 原生開發流程（AI-Native Development Flow）」**。它並不是讓人類失業，而是把重複性的 Git 操作、格式化、甚至開 PR 的瑣事，全權委託給 Claude Code，讓人能專注在更高層次的架構與邏輯上。

針對你的心得，我有以下幾個深度的看法與呼應：

## 1. 關於專案管理框架（Issue > Draft PR > Kanban）

你提到的「Issue -> Draft PR -> 看板管理」在這種 AI 協同開發的專案中**至關重要**，原因有兩個：

- **為 AI 劃定邊界：** 當我們讓 Claude Code 接管開發（例如「跟 Claude 說要做什麼，它會自動開分支、改 code」），人類就必須在更高維度進行控制。**Issue 就是人類對 AI 下達的「最高指導原則」**，而 Kanban 則是團隊確保 AI 沒有失控亂跑的儀表板。
    
- **Draft PR 是最佳的緩衝區：** 既然程式碼很大程度是由 AI 生成、並透過 `/ship` 自動推上去的，直接開常規 PR 壓力太大。先進入 Draft PR 狀態，可以讓人類維護者（Owner）有充分的時間，搭配專案裡的 `code-reviewer.md` 與 `python-reviewer.md` 進行雙重把關。
    

## 2. 關於「Claude 接管一切」與 CI/CD 的新定義

你敏銳地察覺到 CI/CD 的概念在這裡轉變了。傳統的 CI 是「人寫完 code 丟上去，機器檢查」；而在這裡，變成了「AI 在本機驅動，CI 在雲端做硬性防禦」。

我們可以把這個架構拆解為「雙層防線」：

- **本機端（Claude 負責進攻與輔助）：** Claude 透過 `.claude/rules` 在你寫 code 時事前提醒，存檔時觸發 `hooks` 自動修正，最後用 `/ship` 一鍵打包。這極大地降低了人類「忘記跑 format」或「操作 Git 發生失誤」的機率。
    
- **雲端 CI（GitHub Actions 負責絕對防守）：** 雖然 Claude 很聰明，但它依然有幻覺或出錯的可能。因此，GitHub Actions 在這裡扮演了**不妥協的閘門（Gatekeeper）**。特別是 `sensitive-patterns`（敏感資料掃描）在 CI 的 required check 裡絕對卡死，就是為了防止 AI 或人類不小心把真實場域的 IP 或 Token 推上 main。
    

## 3. 這份設計最漂亮的地方：機密與規範的解耦

除了你提到的協同架構，這份 Devkit 還有一個非常值得學習的工程實踐：

它把 **「開發規範（Payload）」** 和 **「敏感資料（Sensitive Patterns / .env）」** 徹底分離。Devkit 只管分發規則（Skills, Rules, Hooks），而真正的機密走安全管道繞過 Git。這樣既能享受 AI 對全局專案知識的理解（那 16 個知識包非常驚人），又完全杜絕了供應鏈洩漏的風險。

總結來說，這個 Repo 代表了目前最理想的 AI 共生開發型態：**人類定策略（Issue/Kanban）、AI 做苦工（Coding/Hooks/Ship）、CI 做終極防禦（Gatekeeper）。** 照著這套框架走，開發效率和代碼質量都會非常高。

既然你正準備深入審閱或參與這個專案，你想先從調整他們本機的 Hooks 腳本（例如格式化工具的行為）開始看起，還是先研究那 16 個專案知識包（Skills）是如何引導 AI 的？


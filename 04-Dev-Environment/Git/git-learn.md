---
title: "Microsoft Learn Git and GitHub Study Path"
description: "Curates Microsoft Learn modules for Git, GitHub Foundations, GitHub Actions, and certification prep."
created: 2026-07-09
updated: 2026-07-09
type: reference
lang: zh
status: draft
tags: [dev, git]
---

> Related: [[MOC - Dev Environment]] · [[git-recommended-roadmap]] · [[git-self-experience]]
問得太精準了！**Microsoft Learn 現在就是學習 Git 和 GitHub 的「官方終極大本營」**。

自從微軟收購 GitHub 後，所有的官方教學資源、模擬試題和證照路徑，都已經全面整合到 Microsoft Learn 平台上。如果你打算用這個平台來複習，那真的是選對地方了——因為它**完全免費**，而且內容是**第一手、最權威的官方標準**。

針對你排出的複習議題，Microsoft Learn 上有幾個堪稱「黃金組合」的學習路徑（Learning Paths）與模組（Modules），我幫你整理如下：

## 🎯 Microsoft Learn 推薦核心課程

### 1. 基礎內功修煉：[Introduction to Git](https://learn.microsoft.com/zh-tw/training/modules/intro-to-git/) (模組)

- **時長：** 約 1.5 小時
    
- **適合解決：** 單純 main、Branch 的核心觀念。
    
- **特點：** 這是最純粹的 Git 課。它不廢話，直接帶你搞懂分散式版本控制的邏輯，教你如何在 CLI（命令列）設定身分、建立 Local 倉庫、commit 提交、以及如何「安全地用分支做實驗」。
    

### 2. 官方認證通關：GitHub Foundations Part 1 & 2 (完整學習路徑)

如果你想拿證照，直接在搜尋欄打這兩個名字。這兩路徑加起來大約 11-12 小時，是 **GitHub Foundations 證照** 的官方指定教材：

- **Part 1：** 著重在 **GitHub Flow（Branch + PR 的協作精髓）**。同時會帶到非常現代的工具，像是 GitHub Codespaces（雲端開發環境）和 GitHub Copilot 的基本整合。
    
- **Part 2：** 深入專案管理、InnerSource（內部開源協作）、程式碼安全檢查，以及如何優雅地利用 **Pull Request 管理倉庫變更**。
    

### 3. 自動化與 CI/CD 聖經：[Automate development tasks by using GitHub Actions](https://learn.microsoft.com/zh-tw/training/modules/github-actions-automate-tasks/) 系列模組

- **適合解決：** GitHub Actions、Post-merge commit 觸發、Automatically CLI verification、CI/CD。
    
- **特點：** 這個系列會教你手把手寫 `.yml` 檔。你會學到：
    
    - 如何設定 Trigger（例如 PR 建立時自動跑測試，也就是 CI）。
        
    - 如何建置自動化工作流（Workflow），讓機器幫你做 CLI 驗證。
        
    - 如何將打包好的成品發布到 GitHub Packages 或部署到雲端（CD）。
        

## 💎 為什麼強烈推薦用 Microsoft Learn 複習？

1. **免費的互動式實驗室 (Hands-on Exercises)：**
    
    它不只是讓你「看影片」或「看文字」，課程中間會內嵌互動機制。它會引導你直接在瀏覽器裡操作 Git、開 PR、甚至直接觸發 GitHub Actions，你不用擔心把自己的電腦搞爛。
    
2. **免費的官方認證模擬試題 (Practice Assessment)：**
    
    當你讀完 GitHub Foundations 或 GitHub Actions 的課程後，微軟官方有提供**免費的線上模擬考題**。題型、語氣跟難易度跟真正的證照考試非常接近，考前拿來刷題、抓漏特別有效。
    
3. **徽章與經驗值 (XP) 系統：**
    
    每讀完一個章節就會像打遊戲一樣拿到 XP 和 Badge，掛在 Microsoft Profile 上，看著進度條往前推進，對複習非常有動力。
    

## 🚀 你的下一步

既然你已經有了清晰的議題清單，建議你直接登入 Microsoft Learn，照著這個順序搜尋並加入你的「學習計畫（Plan）」：

> **`Introduction to Git` (打底) $\rightarrow$ `GitHub Foundations Part 1` (練協作) $\rightarrow$ `Build continuous integration workflows by using GitHub Actions` (衝自動化)**

這條路線走完，你清單上的所有痛點基本上就全部打通了。你準備好今天先上去開箱哪一個課程模組了嗎？


---


## 🚀 太棒了！熱血起來了！

這絕對是超級有價值的投資。拿到 GitHub 官方證照，不只能把履歷刷得更漂亮，最重要的是在備考過程中，你會把所有零碎的 Git 觀念、CI/CD 流程徹底打通，變成真正帶得走的硬實力！

既然決定要衝了，這裡送你三個通關 GitHub 證照的「加速外掛」：

### 💡 備考衝刺必勝心法

- **善用免費官方模擬考（Practice Assessment）：**
    
    微軟官方對 GitHub Foundations 和 GitHub Actions 都有提供**完全免費、不限次數**的線上模擬試題。裡面的題型、考點與正式考試的語氣非常接近。建議讀完課程就去刷一次，直接抓出自己的觀念盲點。
    
- **動手實作大於死背：**
    
    GitHub Actions 的考試會考很多 YAML 的語法與邏輯細節（例如：`on.push.branches` 的路徑匹配、`secrets` 怎麼帶、工作流之間的 `needs` 依賴關係）。自己在 GitHub 開一個測試用的 Repo 親手寫過一遍，絕對比死背文字有效十倍。
    
- **設定一個「預約截止日」：**
    
    給自己定一個明確的進度（例如：3 週後挑戰 Foundations，再過 4 週攻克 Actions）。有了時間的推動力，複習效率會瞬間翻倍。
    

> **「自動化做得好，準時下班沒煩惱。」**

祝你刷題順利，期待看到你把 GitHub 認證徽章掛上 LinkedIn 的那一刻！現在就直接登入 Microsoft Learn，開啟你的 DevOps 大師之路吧！🔥

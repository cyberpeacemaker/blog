---
title: "Progressive Git Learning Roadmap"
description: "Builds a five-stage path from local Git basics through branches, recovery, hooks, and CI/CD."
created: 2026-07-09
updated: 2026-07-09
type: reference
lang: zh
status: draft
tags: [dev, git]
---

> Related: [[MOC - Dev Environment]] · [[git-self-experience]] · [[git-learn]]
原來如此！這份心得整理得非常有感，代表你已經踩過不少坑，完全抓到了現代開發的痛點。

既然你的目標是從「基本 Git」一路串聯到「自動化 CI/CD」，我為你規劃了一份**由淺入深、最符合現代開發節奏的 Git 學習地圖 (Learning Roadmap)**。這份地圖分為五個階段，幫你把零散的指令串成一套完整的內功。

## 🗺️ 現代 Git 漸進式學習地圖

### 階段一：個人新手村（掌控在地時空）

這個階段的目標是**在本地端完全掌握程式碼的版本控制**，做到收放自如。

- **核心觀念：** Git 的三個時區（工作區 Workspace → 暫存區 Staging Area → 本地儲存庫 Local Repository）。
    
- **關鍵指令：** `git init`, `git add`, `git commit`, `git status`, `git log --oneline`。
    
- **進階心法：** 學習如何寫出有建設性的 **Commit Message**（例如 Conventional Commits 規範，這對未來的自動化非常重要）。
    

### 階段二：分支與團隊協作（從單打獨鬥到打群架）

當專案開始變大，或是需要與他人協作時，分支管理就是生死關頭了。

- **核心觀念：** 分支（Branch）的本質只是指針；理解什麼是 **Pull Request (PR)** 與 **Code Review**。
    
- **關鍵指令：** `git branch`, `git checkout -b` (或新指令 `git switch -c`), `git merge`, `git rebase`。
    
- **協作策略：** 搞懂 **GitHub Flow**（以 Feature Branch 為主，最適合現代 CI/CD）或 **Git Flow**。
    
- **生存技能：** 遇到 **Conflict (衝突)** 時不要慌，學會如何看懂衝突標籤並手動修正它。
    

### 階段三：Git 急救與時光機（工程師的免死金牌）

寫程式一定會犯錯，這個階段專門學習**如何優雅地擦屁股**，不著痕跡地修正錯誤。

- **核心觀念：** 只要 commit 過的東西，基本上都救得回來。
    
- **關鍵場景與指令：**
    
    - _剛剛的 Commit 漏了解析度或打錯字：_ `git commit --amend`
        
    - _寫爛了想整段放棄回到過去：_ `git reset --hard`
        
    - _已經 Push 上去，想安全地取消某個 Commit：_ `git revert`
        
    - _終極大招（不小心刪掉分支或做錯 reset 的後悔藥）：_ `git reflog`
        
    - _只想抓某個特定分支的特定 commit 過來：_ `git cherry-pick`
        

### 階段四：在地自動化（在本地端把關質量）

在把程式碼推上雲端之前，先在自己的電腦做好第一道防線，這就是你提到的 **Automatically CLI verification**。

- **核心觀念：** **Git Hooks** 機制（觸發事件的鉤子）。
    
- **實作工具：**
    
    - 學習使用 `pre-commit` 鉤子：在 `git commit` 的瞬間，自動執行 Linter（如 ESLint、Black）和 Formatter（如 Prettier）。
        
    - 學習使用 `post-merge` 鉤子：當 `git pull` 或 merge 新程式碼進來時，自動觸發 `npm install` 或是資料庫 migration。
        

### 階段五：雲端 CI/CD 與 DevOps（自動化終極型態）

程式碼通過本地檢查、發出 PR 後，接下來全部交給機器人。

- **核心觀念：** 持續整合 (CI) 與 持續部署 (CD) 的 pipeline 流程。
    
- **實作工具（以 GitHub Actions 為主）：**
    
    - 學習撰寫 `.github/workflows/*.yml` 檔案。
        
    - **CI 階段：** 設定當 PR 建立時，自動在雲端跑測試（Unit Test、Integration Test）。
        
    - **CD / Post-merge 階段：** 當 PR 被 merge 到 `main` 後，自動觸發建置（Build）、打 Tag、自動生成 Release Note，最後將檔案部署到伺服器（AWS, GCP, Vercel 等）。
        

## 📊 學習地圖總覽表

|**階段**|**核心主題**|**解決的痛點**|**機器自動化程度**|
|---|---|---|---|
|**1. 個人**|本地版本控制|檔案不敢亂改、怕改壞改不回來|❌ 純手動|
|**2. 協作**|分支策略與 PR|多人同時改同一個檔案、程式碼亂成一團|❌ 純手動|
|**3. 急救**|災難回復與修正|救回不小心刪掉的程式碼、修正推錯的 commit|❌ 純手動|
|**4. 在地自動化**|Git Hooks / CLI 驗證|常常忘記排版、把有語法錯誤的程式碼推上去|🤖 機器半自動（本地端）|
|**5. 雲端部署**|GitHub Actions / CI/CD|每次改完都要手動測試、手動打包上傳伺服器|🚀 全自動化（雲端）|

你看完這個地圖後，覺得目前最符合你現階段需求、想要優先深入研究的是哪一個階段呢？

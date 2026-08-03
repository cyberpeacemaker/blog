---
created: 2026-08-03 16:08
updated: 2026-08-03 16:08
tags: []
type: reference
lang: en
status: draft
---


完全正確！你的概念非常到位！

在自己的分支（Branch）開發時，**「少次大修改不如多次小 Commit」**。每一次完成一個微小的進度（例如：刻好 UI、寫好 API 串接、修掉一個小 Bug），commit 一次是最好的習慣。這樣萬一寫爛了，隨時可以退回上一個完美的狀態。

以下為你整理從「寫程式」到「開 PR（Pull Request）」的完整流程與指令：

## 🔄 開發到開 PR 的標準 4 步驟

```
修改程式碼 ➔ git add ➔ git commit (重複多次) ➔ git push ➔ 上平台開 PR
```

### 1. 寫程式與多次 Commit (在本地端)

寫完一部分程式碼後，可以先看改了什麼，然後存檔提交：

Bash

```
# 查看有哪些檔案被修改了（新手必備好習慣！）
git status

# 把修改過的檔案加入暫存區
git add .

# 提交一次 Commit，並寫下清晰的說明紀錄
git commit -m "feat: 完成登入頁面基本 UI 佈局"
```

> 💡 **進度推進**：接著你可能又寫了驗證邏輯，就可以再 repeat 一次：
> 
> `git add .` $\rightarrow$ `git commit -m "fix: 修復信箱格式驗證的 Bug"`。

### 2. 把程式碼推送到遠端 (Git Push)

當這項功能寫得差不多，準備要給同事審核時，就把你本地的所有 Commit 一起推上去：

如果是這個分支**第一次**推上去：

Bash

```
git push -u origin feature/add-login-page
```

> 💡 `-u` (或 `--set-upstream`) 會讓本地分支與遠端建立連結。之後在這個分支只要直接打 `git push` 就可以推上去了！

### 3. 上 GitHub / GitLab 建立 PR (Pull Request)

推送成功後，終端機通常會貼心附上一串網址，或者你直接打開 GitHub/GitLab 專案頁面：

1. 頁面上方會出現一個醒目的按鈕：**「Compare & pull request」**，直接點下去。
    
2. **填寫 PR 標題與內文**：簡單說明這次改了什麼、怎麼測試。
    
3. **指定 Reviewer**：標註你的主管或同事來幫你審核程式碼（Code Review）。
    
4. 點擊 **「Create pull request」**！
    

### 4. (補充) 如果推上去後，發現還要修東西怎麼辦？

**別緊張！不需要重新開 PR。**

你只需要在本地繼續修改程式碼、`git add .` $\rightarrow$ `git commit`，然後再次 `git push`。GitHub / GitLab 會**自動**把你最新的 Commit 補充進剛才開好的那個 PR 裡面。

## 💡 最佳實踐懶人包

- **Commit 顆粒度**：盡量「單一職責」，一個 Commit 只做一件事，訊息（Commit Message）要清楚描述做了什麼。
    
- **Push 時間點**：下班前、或準備開 PR 前 push 就好；但如果怕電腦壞掉，隨時 push 上去當備份也是沒問題的！
    

你們團隊在 Code Review 時有特別要求的 Commit 訊息格式（例如 Conventional Commits），或者你想了解被同事要求修改（Requested Changes）時該怎麼處理嗎？
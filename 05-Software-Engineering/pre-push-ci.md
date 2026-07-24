---
title: "Pre-push vs CI Checks"
description: "Explains how local pre-push checks and server-side CI checks should split scope and terminology."
created: 2026-07-23
updated: 2026-07-23
tags: [dev, git, workflow]
type: concept
lang: zh
status: draft
---

> Related: [[05-Software-Engineering]] · [[cicd-get-started]] · [[github-action-workflows]]

這句話常見於工程團隊的任務清單（JIRA / Issue）、開發規範文件或 PR 討論中。

一句話總結它的意思就是：**「明確劃分『程式碼上傳前（本地端）』與『自動測試（伺服器端）』分別要檢查哪些項目，並統一這兩者的溝通名詞與規範。」**

## 核心概念拆解

### 1. 什麼是 Pre-push 與 CI？

- **Pre-push（推送前檢查）**：在你的電腦（本地端）執行 `git push` 的那一刻，自動觸發的腳本檢查（例如利用 Git Hooks 或 Husky）。
    
- **CI（Continuous Integration，持續整合）**：程式碼成功推送到 GitHub / GitLab 後，由遠端伺服器（如 GitHub Actions、Jenkins）自動執行的流水線測試與建置。
    

### 2. 為什麼要釐清「檢查範圍」？

如果檢查分配不當，會嚴重影響開發體驗：

- **Pre-push 太重**：如果在本地 push 前就要執行全部的單元測試與 E2E 測試，每次 push 都要等 10 分鐘，工程師會想直接跳過（`--no-verify`）。
    
- **CI 太雜**：如果連基本的程式碼格式化（Prettier/Lint）都留給 CI 做，不僅浪費遠端伺服器資源，還要等 CI 跑完報錯才發現漏了分號，效率極低。
    

> **典型的範圍分工：**
> 
> - **Pre-push 負責**：輕量、快速的事（如：Lint 語法檢查、Format 格式化、簡單的型別檢查）。
>     
> - **CI 負責**：重量、耗時的事（如：完整 Unit Test、整合測試、Docker Image 建置、資安掃描）。
>     

### 3. 為什麼要釐清「用語」？

團隊內部常常名詞混用（例如有人把 Lint 叫 Code Review，把 Type-check 叫 Build）。釐清用語是為了**讓大家講同某種語言**，例如統一把管道節點命名為 `lint`、`test`、`build`，或是統一 Commit Message 與 PR 狀態的描述方式。


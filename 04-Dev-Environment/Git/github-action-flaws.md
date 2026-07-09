---
title: "Git Hooks and GitHub Actions Guardrail Tradeoffs"
description: "Explains why local hooks catch issues before push while GitHub Actions remain the authoritative CI backstop."
created: 2026-07-09
updated: 2026-07-09
type: reference
lang: zh
status: draft
tags: [dev, git, workflow]
---

> Related: [[MOC - Dev Environment]] · [[github-hook-action]] · [[automation-pr-merge-policy]]
這份設定檔寫得非常漂亮，具備高水準的工程紀律！它不只是一個簡單的開發指南，而是一套完整的「防呆與資安防禦機制」。

針對你的問題，我們來逐一拆解這個設定的精妙之處、Git Hook 的致命缺點，以及它跟 GitHub Actions 的微妙關係。

## 🧐 我怎麼看？推薦嗎？

**非常推薦，這是一套成熟團隊才會有的「防彈級」設定。**

它有幾個極具價值的亮點：

1. **環境鐵則（Conda Isolation）**：強制不用 system Python，能徹底避免團隊成員因為 Python 版本或套件衝突而發生的「在我的電腦上可以跑，在你的不行」的慘劇。
    
2. **極致的資安意識**：把敏感特徵檔（`sensitive-patterns`）放在權限為 `600`（只有當前使用者可讀寫）的家目錄下，不進專案版控。
    
3. **強制的防呆驗證**：它在步驟 2 寫了一段「故意踩紅線」的驗證指令。這太棒了！很多團隊裝了 Hook 從不測試，直到出事才發現 Hook 根本沒生效。
    
4. **Devkit 抽離設計**：把 AI 助理（Claude Code）的規範和工具獨立成另一個 repo（`otex-claw-devkit`），既能統一管理團隊的 AI 提示詞（Prompts）與規則，又不會讓核心專案的 Git 紀錄變得混亂。
    

## 🔓 Git Hook 可以被繞過嗎？

**可以，而且非常容易。**

Git Hook 是一個「君子協定」，它完全運行在開發者的本機電腦上。只要開發者想繞過，有以下幾種常見方法：

- **指令加上參數**：在 `git push` 後面加上 `--no-verify`（或 `-n`），Git 就會直接無視所有 Hook，強行把程式碼推上去。
    
- **直接刪除腳本**：去 `.git/hooks/` 資料夾下把 `pre-push` 檔案砍掉或改名。
    
- **根本不執行安裝**：如果新進隊友漏看了文件，沒有執行 `bash scripts/install-git-hooks.sh`，那這道閘門對他來說根本不存在。
    

> ⚠️ **結論**：Git Hook 只能用來**「防呆」**（防止自己或隊友不小心犯錯），絕對不能用來**「防壞人」**。

## 🎯 是不是因為「不能推上去」所以不用 GitHub Actions？

**你說對了一半！這確實是其中一個核心原因，但更精準的說法是：「因為一旦推上去，就已經太遲了。」**

你直覺聯想到敏感資料不能推上雲端，這完全正確。如果我們**只**用 GitHub Actions 來檢查敏感資料，會遇到兩個致命問題：

### 1. 凡推過必留下痕跡（Git 歷史紀錄污染）

假設小明不小心把 AWS 的金鑰（Secret Key）寫在程式碼裡，然後 `git push` 上去。此時 GitHub Actions 啟動，抓到了這個錯誤並阻擋了 PR 合併。

- **結果**：雖然程式碼沒進 `main` 分支，但這個含金鑰的 Commit **已經存在於 GitHub 的伺服器上了**！
    
- **代價**：任何人只要去挖小明的那個分支歷史，就能看到金鑰。團隊必須立刻啟動資安通報、作廢並更換該金鑰，還要用極其麻煩的指令（如 `git-filter-repo`）去刪除遠端的歷史紀錄。
    

> 💡 **這就是 `pre-push` Hook 的價值**：在資料連小明的電腦都還沒離開之前，就直接一巴掌拍掉。沒出門，就不算洩漏。

### 2. 敏感特徵（Sensitive Patterns）的保密性

如果把用來檢查敏感資料的規則（`sensitive-patterns`）直接放進 GitHub 專案或 GitHub Actions 裡，等於是把「我們公司怎麼檢查資安、我們有哪些敏感欄位格式」的底牌暴露出來。放在本機的 `~/.config/` 則是更安全的做法。

## 🛠️ 完美的終極架構應該是？

既然 Git Hook 會被繞過，而 GitHub Actions 又有「推上去就遲了」的風險，最安全的公司通常會採取「雙重防線」：

1. **第一道防線（本機 Git Hook）**：就像這份文件寫的，用 `pre-push` 幫開發者做第一線防呆，省去金鑰外洩和等待雲端跑測試的時間。
    
2. **第二道防線（GitHub Actions）**：在雲端依然要跑一次一模一樣的檢查（例如使用託管型的秘密掃描工具如 Trufflehog，或是跑自動化測試）。因為即使有人用了 `--no-verify` 繞過本機檢查，也會在 GitHub Actions 這關被徹底封殺，確保主分支（`main`）絕對乾淨。
    

這份設定檔負責了非常完美的「第一道防線」，是一個非常有水準的架構設計。

你在看這份設定時，有沒有哪一個檢查項目（例如前端型別、ruff 錯誤）是你在過去的開發中也常常不小心踩到的雷呢？

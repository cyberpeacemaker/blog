---
title: "Git SSH Permission Denied"
description: "Troubleshoots GitHub SSH publickey failures and HTTPS fallback options on Windows."
created: 2026-07-15
updated: 2026-07-15
type: howto
lang: zh
status: draft
tags: [dev, git]
---

> Related: [[MOC - Dev Environment]] · [[github-permission-ssh]] · [[github-ssh]]

# Git SSH Permission Denied
啊，遇到了每個開發者都一定會經歷過的魔王關卡：**SSH 權限被拒絕 (`Permission denied (publickey)`)**。

這代表你的 Git 目前是用 **SSH 模式**去跟 GitHub 連線，但 GitHub 認不出你這台電腦的身份（或者是你還沒把這台電腦的 SSH 金鑰放到 GitHub 帳號裡）。

別慌，我們有兩個解決辦法。**推薦直接用「方法一」**，最快也最不容易出錯！

## 方法一：切換成 HTTPS 模式（最快、最推薦）

既然你在 Windows (PowerShell) 環境下，切換成 HTTPS 模式後，Git 會自動跳出瀏覽器視窗讓你「點擊登入」GitHub，通常 10 秒鐘就能解決。

請在終端機依序輸入以下指令：

PowerShell

```
# 1. 把連線網址從原本的 SSH (git@...) 改成 HTTPS (https://...)
git remote set-url origin https://github.com/nagameTW/otex-claw-devkit.git

# 2. 再次嘗試同步
git pull origin main
```

> 💡 **這時會發生什麼事？**
>
> 畫面通常會彈出一個微軟的登入小視窗（Git Credential Manager），問你是否要透過瀏覽器驗證 GitHub。直接點選 **「Sign in with your browser」**，在網頁點擊同意，完成後回來看終端機，它就已經默默下載完成了！

## 方法二：把這台電腦的 SSH 金鑰綁定到 GitHub

如果你之後就是想堅持用 SSH 連線，那你必須讓 GitHub 認識你這台電腦。請按照以下步驟操作：

### 1. 檢查你有沒有現成的 SSH 金鑰

在終端機輸入：

PowerShell

```
cat ~/.ssh/id_ed25519.pub
```

- **如果畫面噴出一長串以 `ssh-ed25519 AAAAC3...` 開頭的文字**：代表你有金鑰，請把那一整串文字**全部複製**起來，跳到下面的第 3 步。

- **如果顯示找不到檔案 (No such file or directory)**：代表你從來沒建立過，請看第 2 步。


### 2. 產生一組新的 SSH 金鑰（如果上一步找不到檔案）

在終端機輸入（記得把 Email 換成你的）：

PowerShell

```
ssh-keygen -t ed25519 -C "你的GitHub電子郵件@example.com"
```

隨後它會問你問題，**不用輸入任何東西，瘋狂按 Enter 鍵（大約 3 次）**直到它結束。 結束後，再次輸入 `cat ~/.ssh/id_ed25519.pub`，並把那一長串文字**全部複製**。

### 3. 把金鑰貼到 GitHub 網站上

1. 打開瀏覽器，進入你的 [GitHub 設定頁面 (SSH and GPG keys)](https://github.com/settings/keys)。

2. 點擊右上角的綠色按鈕 **「New SSH key」**。

3. **Title**：隨便填，例如 `My Windows Laptop`。

4. **Key**：把你剛剛複製的那一長串文字整條貼進去。

5. 點擊 **「Add SSH key」**。


綁定完成後，回到 VSCode 的終端機，重新輸入 `git pull origin main` 就能順利通過了！

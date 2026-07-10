---
title: "Conda in PowerShell on Windows"
description: "Shows how to initialize Conda for PowerShell, adjust execution policy, and verify Node.js and Conda commands."
created: 2026-07-09
updated: 2026-07-09
type: howto
lang: zh
status: draft
tags: [dev, python]
---

> Related: [[MOC - Dev Environment]] · [[conda-miniconda]] · [[powershell-execution-policy]]
可以，而且用 PowerShell（或 Windows Terminal）絕對比舊版的 Command Prompt 舒服多了！

不過，因為我們在安裝 Miniconda 時沒有勾選「加入環境變數 (PATH)」，所以如果你直接打開一般的 PowerShell 輸入 `conda`，系統會跟你裝傻說找不到這個指令。

要讓一般的 PowerShell 完美支援 Conda 和 Node.js，請按照以下步驟設定：

## Step 1. 先確認 Node.js

Node.js 很乖，安裝時就已經自動寫入系統路徑了。你現在打開一般的 PowerShell，輸入：

PowerShell

```
node -v
```

應該就能直接看到版本號，這部分不用另外設定。

## Step 2. 讓 PowerShell 認得 Conda

我們需要透過 Miniconda 內建的機制，把 Conda 的啟動腳本寫進 PowerShell 的設定檔中。

1. 打開 Windows 開始功能表，搜尋並開啟 **Miniconda Prompt**（沒錯，先用它一下）。
    
2. 在裡面輸入以下指令並按 Enter：
    
    Bash
    
    ```
    conda init powershell
    ```
    
3. 畫面上會顯示一堆 `modified` 的路徑，這代表它已經把設定寫入你的 PowerShell 設定檔了。
    
4. **關閉**這個 Miniconda Prompt。
    

## Step 3. 解除 Windows 11 的指令碼限制（重要！）

Windows 11 預設基於安全性，會阻擋 PowerShell 執行外部腳本（包括 Conda 的啟動腳本）。如果現在直接打開 PowerShell，你可能會看到一串紅字寫著「_因為在此系統上禁止執行指令碼..._」。

為了解決這個問題：

1. 右鍵點擊 Windows 開始圖示，選擇 **「終端機 (系統管理員)」** 或 **「Windows PowerShell (系統管理員)」**。
    
2. 輸入以下指令並按 Enter（這會允許執行你電腦本機的腳本）：
    
    PowerShell
    
    ```
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    ```
    
3. 系統詢問是否變更時，輸入 `Y` 然後按 Enter。
    
4. 關閉這個系統管理員視窗。
    

## Step 4. 大功告成！驗證成果

現在，你可以隨意打開你平常愛用的 **PowerShell** 或 **Windows Terminal** 了。

你會發現指令列的最前面多了一個 `(base)` 的字樣，這代表 Conda 的基礎環境已經成功在 PowerShell 中啟動！

接著你可以同時測試兩個指令：

PowerShell

```
conda --version
node -v
```

只要都有出來，以後你就可以完全拋棄 Miniconda Prompt，直接在 PowerShell 裡通吃 Python 和 Node.js 了！

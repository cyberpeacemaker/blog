---
created: 2026-07-16 09:07
updated: 2026-07-16 09:07
tags: []
type: reference
lang: en
status: draft
---
切換到 WSL（Windows Subsystem for Linux）是一個非常明智的決定！從你原本使用的 PowerShell 快捷徑可以看出來，你之前是在 Windows 原生環境下透過 PowerShell 去強行執行 Linux 的 Bash 腳本（`bash scripts/install-git-hooks.sh`），這通常就是跨平台災情的開端（路徑斜線、權限、換行符號全都會打架）。

既然決定改用 WSL 重跑測試，為了確保測試精準，你的**環境調整與操作流程**建議按照以下步驟進行：

## 🛠 WSL 環境調整三部曲

### 第一步：絕對不要在 `/mnt/c/`（Windows 路徑）下操作

這是最多人踩的坑！如果你直接在 WSL 裡 `cd /mnt/c/Users/ydnaa/Documents/Github/otex-claw`，你本質上還是在存取 Windows 的檔案系統。這會導致：

1. `chmod 600` 依然可能失效（因為底層是 Windows NTFS）。
    
2. 檔案讀寫效能變得很差。
    

> 💡 **正確做法：**
> 
> 請直接在 WSL 的 Linux 原生家目錄（例如 `~`）下重新 `git clone` 專案。

Bash

```
cd ~
mkdir -p projects && cd projects
git clone https://github.com/nagameTW/otex-claw.git
```

_註：如果你需要在 Windows 編輯檔案，可以在 WSL 中輸入 `code .`，用 VS Code 的 WSL 延伸模組直接連進去開發，體驗最完美。_

### 第二步：在 WSL 內安裝 Linux 版的 Conda

你在 Windows 安裝的 Miniconda 無法（也不應該）直接給 WSL 使用。你需要給 WSL 獨立安裝一份 Linux 版本的 Miniconda：

Bash

```
# 1. 下載 Linux 版 Miniconda 安裝包
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

# 2. 執行安裝
bash Miniconda3-latest-Linux-x86_64.sh

# 3. 安裝完成後重開終端機，或執行以下指令讓 conda 生效
source ~/.bashrc
```

安裝完成後，再依照 README 的指引去建立 `otex-claw` 的虛擬環境。

### 第三步：重新驗證那些「卡點」

當你在 WSL 原生環境（Linux）下，再去跑原本出錯的步驟，預期會順利很多：

- `chmod 600 ~/.config/otex-claw/sensitive-patterns` 應該能正常工作。
    
- `bash scripts/install-git-hooks.sh` 應該不會再噴 Conda 環境找不到的錯誤（前提是你已經 `conda activate otex-claw`）。
    
- 原本在 Windows 噴出的 `NotADirectoryError: [WinError 267]` 應該會直接消失。
    

## 📝 你的 Review 筆記該如何調整？

當你用 WSL 順利跑完後，你的 Review 筆記就有了最核心的論點。你可以把結論修正為：

> ### 📌 最終 Review 結論建議
> 
> **「本專案的自動化腳本與權限設定（如 chmod、bash script）高度依賴 Linux 環境。強烈建議在 README 的『前置作業』或最開頭，加上環境限制說明：**
> 
> - _限制：本專案目前僅支援 Linux / macOS 環境。_
>     
> - _Windows 用戶提示：請務必使用 WSL2，並將專案 clone 於 Linux 原生路徑（如 `~/`）下操作，切勿在 `/mnt/c/` 盤符下執行，否則權限與 Git Hooks 腳本會失效。」_
>     

這樣一來，既不用逼同事去修痛苦的 Windows 跨平台 Bug，又能保證下一個 Onboard 的新人（如果是 Windows 用戶）不會再重蹈覆轍踩程式碼的坑。

你目前 WSL 已經裝好 Linux 版的 Conda 了嗎？還是需要我提供更詳細的環境初始化指令？


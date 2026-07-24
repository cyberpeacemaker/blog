---
title: "WSL Node.js Setup with NVM"
description: "Shows how to install Node.js in WSL with NVM and avoid Conda path conflicts during project testing."
created: 2026-07-24
updated: 2026-07-24
tags: [dev]
type: howto
lang: zh
status: draft
---

> Related: [[MOC - Dev Environment]] · [[wsl-distro]] · [[conda-uv-pixi]]

  
在 WSL (Linux) 環境下，安裝 Node.js 的**大忌**是直接使用 `sudo apt install nodejs`（這會裝到舊版，而且往後常遇到權限錯誤）。

  

最完美的標準做法是使用 **NVM (Node Version Manager)**。它能讓你自由切換 Node.js 版本，且所有套件都裝在使用者家目錄下，完全不會有權限問題。

  

以下是在 WSL 中安裝與測試 Node.js 的完整步驟：

  

---

  

## 🚀 WSL 環境 Node.js 安裝四部曲

  

### 1. 安裝 NVM

  

直接在 WSL 終端機輸入以下指令下載並執行 NVM 安裝腳本：

  

```bash

curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.5/install.sh | bash

  

```

  

安裝完成後，讓設定檔立即生效（或是關掉 WSL 視窗重新打開）：

  

```bash

source ~/.bashrc

  

```

  

驗證 NVM 是否安裝成功：

  

```bash

nvm --version

  

```

  

---

  

### 2. 安裝 Node.js

  

透過 NVM 安裝你需要的 Node.js 版本。

  

* **如果專案沒有指定版本：** 建議安裝最新的長期支援穩定版 (LTS)

```bash

nvm install --lts

  

```

  
  

* **如果專案有指定版本（例如 v20）：**

```bash

nvm install 20

  

```

  
  
  

---

  

### 3. 驗證與測試環境

  

安裝完成後，進行基本版本檢查：

  

```bash

node -v  # 應該會顯示 v24.x 或 v20.x 等版本號

npm -v   # 應該會顯示對應的 npm 版本

  

```

  

#### 🛠 進入專案實測

  

`cd` 到你克隆（clone）在 WSL 原生路徑下的專案資料夾，執行：

  

```bash

# 1. 安裝專案依賴套件

npm install

  

# 2. 執行專案測試（通常 README 或 package.json 會寫，常見如下）

npm test

# 或啟動開發伺服器

npm run dev

  

```

  

---

  

## ⚠️ 額外注意：Conda 與 NVM 的「搶路徑」衝突

  

因為你同時使用了 Conda 和 NVM，這裡有一個隱藏的「坑」需要注意：

有些 Python 專案會在 Conda 環境裡塞入一個 `nodejs` 包。請在 **`conda activate otex-claw` 之後**，輸入以下指令確認：

  

```bash

which node

  

```

  

* **正常情況：** 應該指向 `~/.nvm/versions/node/.../bin/node`

* **衝突情況：** 如果指向 `~/miniconda3/envs/otex-claw/bin/node`，代表 Conda 環境裡的 Node.js 把 NVM 的蓋掉了。

  

> 💡 **解決辦法：**

> 如果發現版本被 Conda 綁架，且版本不對，可以在專案測試時，手動下一行 `nvm use --lts`（或指定版本），強行把主導權搶回給 NVM。

  

---

  

## 📝 順手加入 README 的 Review 筆記

  

既然你在幫同事 review，測試成功後，可以建議同事在 README 的 Node.js 區塊加上這段：

  

> * "Node.js 環境建議使用 NVM 進行版本管理（避免使用 apt 原生安裝以防 `EACCES` 權限錯誤）。"

> * "若同時使用 Conda，請確保 `which node` 指向 NVM 路徑，或在 activate env 後執行 `nvm use <version>` 以免版本衝突。"

>

>

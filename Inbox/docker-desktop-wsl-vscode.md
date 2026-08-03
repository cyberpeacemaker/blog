---
created: 2026-08-03 16:08
updated: 2026-08-03 16:08
tags: []
type: reference
lang: en
status: draft
---

**不一致！這份文件點出了一個非常關鍵的差異。**

我先前是以一般最常見的「Docker Desktop + WSL」架構為你解說，但**你們團隊的文件有非常明確的特殊規範：完全不使用 Docker Desktop，而是把 Docker Engine 直接原生裝在 WSL (Ubuntu) 裡面！**

### 1. 核心差異比較

|**項目**|**我先前說的（一般常見做法）**|**你團隊文件（0x01 & 0x0A）的規範**|
|---|---|---|
|**Docker Engine 位置**|運行在 Windows 的 **Docker Desktop** 上|**原生運行在 WSL Ubuntu 24.04 內部**|
|**Windows Docker Desktop**|必須開啟並運作|**不需要！甚至「嚴禁啟用」對 Ubuntu 的 WSL Integration**|
|**服務管理**|由 Docker Desktop 應用程式管理|由 WSL 內部的 **`systemd`** 服務管理|

### 2. 為什麼剛才你會看到 Docker Desktop 的報錯？

文件中的 **`0x0A 常見問題排解`** 完美解答了這個現象：

> _「Dev Containers 在 WSL 裡找不到 `docker` 時，會回頭去啟動 `Docker Desktop.exe`...」_

因為你剛才在 WSL 裡的 Docker 沒發揮作用，VS Code 找不到 WSL 內部的 Docker，就「退而求其次」嘗試去呼叫 Windows 上的 Docker Desktop（但你又沒開 Desktop），所以才會出現我們剛才看到的 `dockerDesktopLinuxEngine` 錯誤訊號！

### 3. 依據文件，你現在應該採取的正確步驟

請完全按照這份 Onboarding 文件的指示進行（**不用管 Docker Desktop 了**）：

#### Step 1: 確認預設 WSL 發行版為 Ubuntu-24.04 (參照 §0x02)

在 Windows PowerShell 執行：

PowerShell

```
wsl --set-default Ubuntu-24.04
wsl -l -v
```

確認 `(Default)` 標記在 `Ubuntu-24.04` 上。

#### Step 2: 檢查與啟動 WSL 內部的 Docker (參照 §0x01)

開啟 **WSL2 Ubuntu 終端機**，測試 Docker 是否正常運行：

Bash

```
docker ps
```

- 如果顯示 `permission denied` ➡️ 執行 `newgrp docker`。
    
- 如果顯示 Docker 沒啟動 ➡️ 執行 `sudo systemctl start docker`，或依文件 §0x01 重新執行 `bootstrap-wsl.sh` 並重啟 WSL (`wsl --shutdown`)。
    

#### Step 3: 設定 VS Code (參照 §0x02)

1. 在 VS Code 設定 (`Ctrl + ,`) 搜尋 `executeInWSL` 並**勾選**。
    
2. 開啟命令面板 (`F1`) 選擇：**Dev Containers: Clone Repository in Container Volume**。
    

如果在 WSL Ubuntu 終端機裡輸入 `docker ps`，現在能正常顯示表格欄位嗎？


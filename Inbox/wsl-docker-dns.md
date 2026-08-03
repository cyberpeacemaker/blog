---
created: 2026-08-03 16:08
updated: 2026-08-03 16:08
tags: []
type: reference
lang: en
status: draft
---
太棒了！`docker ps` 能正常輸出，代表你已經成功把 **WSL 內部的 Docker Engine** 運作起來了，先前 Docker Desktop 的問題已經完全排除！

至於這次出現的新錯誤，從截圖最後幾行可以看出問題原因：

> `lookup mcr.microsoft.com on 10.255.255.254:53: i/o timeout`

這是 **WSL / Docker 的網路 DNS 解析逾時**。Docker 想要下載建置 Dev Container 所需的基底映像檔，但 WSL 內部的 DNS (`10.255.255.254`) 沒有回應，導致連不上外網。

### 修復步驟

請在 **WSL Ubuntu 終端機** 依序執行以下操作：

#### 1. 設定 Docker 的固定 DNS（最有效的方法）

讓 Docker 直接使用 Google/Cloudflare 的公共 DNS 伺服器，避開 WSL 自動生成的虛擬 DNS 逾時問題：

Bash

```
#[ubuntu]
# 1. 將 DNS 設定寫入 Docker 設定檔
sudo mkdir -p /etc/docker
echo '{"dns": ["8.8.8.8", "1.1.1.1"]}' | sudo tee /etc/docker/daemon.json

# 2. 重啟 WSL 內的 Docker 服務
sudo systemctl restart docker
```

#### 2. 手動測試拉取映像檔

在 WSL 終端機中手動執行 pull，確認網路連線是否恢復：

Bash

```
#[ubuntu]
docker pull mcr.microsoft.com/devcontainers/base:0-alpine-3.20
```

- **若成功下載**：代表網路問題已修復！
    
- **若依然顯示 timeout**：請檢查你的 Windows 是否開著 **VPN 或公司防火牆 / Zscaler**，嘗試先關閉 VPN 再試一次。
    

#### 3. 重新建立 Dev Container

當手動 pull 成功後，回到 VS Code 點擊彈出視窗上的 **Retry**（或按 `F1` 選擇 `Dev Containers: Rebuild Container`）即可！

在 WSL 裡幫 Docker 設定完 DNS 並重啟服務後，手動 `docker pull` 有順利開始下載了嗎？

---

你的觀察非常精準！

在 Docker 中，`daemon.json` 裡的 `"dns"` 設定其實是**給「Docker 容器內部」使用的**；但當你執行 `docker pull` 下載映像檔時，是由 **Docker Daemon 服務本身**在進行網路連線，因此它吃的是 **WSL 系統本機的 DNS**（也就是畫面上的 `10.255.255.254`）。

因為 WSL 自動生成的 DNS 指向了 Windows 主機但回應逾時，所以我們需要直接修改 **WSL 系統本身的 DNS 設定**。

### 修復步驟：直接修改 WSL 的系統 DNS

請在 **WSL Ubuntu 終端機** 依序執行以下指令：

#### Step 1: 關閉 WSL 自動覆蓋 DNS 的功能

預設情況下 WSL 每次重啟都會把 `/etc/resolv.conf` 改回 `10.255.255.254`，我們需要先停用這個行為：

Bash

```
#[ubuntu]
sudo bash -c 'cat <<EOF >> /etc/wsl.conf
[network]
generateResolvConf = false
EOF'
```

#### Step 2: 刪除舊設定並指定公共 DNS

刪除預設的連結檔，並寫入 Google/Cloudflare 的 DNS：

Bash

```
#[ubuntu]
# 刪除舊的 resolv.conf
sudo rm -f /etc/resolv.conf

# 寫入正確的 DNS
echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf
echo "nameserver 1.1.1.1" | sudo tee -a /etc/resolv.conf
```

#### Step 3: 重啟 WSL

回到 **Windows PowerShell** 關閉 WSL 讓設定徹底生效：

PowerShell

```
#[powershell]
wsl --shutdown
```

### Step 4: 測試下載

重新打開 **WSL Ubuntu 終端機**，直接測試 pull：

Bash

```
#[ubuntu]
docker pull mcr.microsoft.com/devcontainers/base:0-alpine-3.20
```

如果成功開始下載，就可以回到 VS Code 點擊 **Retry**， Dev Container 就能順利啟動了！

修改 WSL 的 `/etc/resolv.conf` 並重啟後，這次 `docker pull` 有成功開始下載映像檔嗎？
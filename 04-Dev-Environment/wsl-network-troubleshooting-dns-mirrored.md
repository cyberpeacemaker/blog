---
title: "WSL Network DNS and Mirrored Mode Troubleshooting"
description: "Troubleshoots WSL2 DNS, mirrored networking, firewall, proxy, and GitHub timeout failures on lab or corporate laptops."
created: 2026-07-16
updated: 2026-07-16
type: howto
lang: zh
status: draft
tags: [dev]
---

> Related: [[MOC - Dev Environment]] · [[wsl-network-troubleshooting]] · [[wsl-mtu]]

這個錯誤是 WSL2 惡名昭彰的網路斷聯（Timeout）傳統老症頭。因為 WSL2 本質上是個獨立的虛擬機器，它的網路是透過 Windows 的虛擬網卡橋接出去的。

從你的終端機提示字元 `LABNB01` 看起來，這台可能是公司或實驗室的筆電？如果是的話，**通常是因為公司網路、防毒軟體、VPN，或是 WSL 自行產生的 DNS 解析失敗**導致它連不上外網的 GitHub。

別慌，我們用以下三個由淺入深的排查方案來見招拆招：

### 方案一：最現代且最推薦的解法（開啟 WSL 鏡像網路模式）

如果你使用的是較新版本的 WSL（通常 Windows 11 更新後都有），微軟推出了一個叫 **Mirrored（鏡像）** 的網路模式。它能讓 WSL 直接共享 Windows 的網路狀態，**能完美解決 90% 因為公司 VPN、防毒軟體或特定網域導致的連線問題**。

1. 在 Windows 中打開檔案總管，去你的使用者家目錄（也就是你之前的路徑 `C:\Users\ydnaa\`）。
    
2. 在該目錄下新增一個文字檔，命名為 `.wslconfig`（注意前面有個點，如果本來就有這檔案就直接打開修改）。
    
3. 把以下內容貼進去並存檔：
    
    Ini, TOML
    
    ```
    [wsl2]
    networkingMode=mirrored
    dnsTunneling=true
    firewall=true
    ```
    
4. 打開 Windows 的 **PowerShell**（不是 WSL 喔），執行以下指令徹底重啟 WSL：
    
    PowerShell
    
    ```
    wsl --shutdown
    ```
    
5. 重新打開你的 WSL 終端機，再次嘗試 `git clone`。
    

### 方案二：傳統 DNS 撞牆解法（最常見原因）

如果方案一無效，很可能是 WSL 自動產生的 DNS 設定（`/etc/resolv.conf`）壞了，導致它找不到 `github.com` 的 IP。我們來手動把它改成 Google 的 DNS。

1. 在 WSL 內，先檢查能不能連到外網的 IP（測試是不是純粹 DNS 解析壞掉）：
    
    Bash
    
    ```
    ping 8.8.8.8
    ```
    
    _如果 ping 得通，代表網路是通的，純粹是找不到網址！請繼續往下走。_
    
2. 刪除舊的自動連結，並手動寫入常用的 DNS（例如 Google 或 Cloudflare）：
    
    Bash
    
    ```
    sudo rm /etc/resolv.conf
    sudo sh -c 'echo "nameserver 8.8.8.8" > /etc/resolv.conf'
    sudo sh -c 'echo "nameserver 1.1.1.1" >> /etc/resolv.conf'
    ```
    
3. 測試看看能不能 clone 了。
    
    _(注意：這個解法在 WSL 重啟後可能會被系統還原，如果有效，之後需要修改 `/etc/wsl.conf` 來禁止系統自動覆寫 DNS。)_
    

### 方案三：如果你正在使用公司 Proxy / VPN

如果你的 Windows 電腦必須掛著公司的 Proxy 或 VPN 才能上網，那麼 WSL 也必須掛上相同的 Proxy 設定。

1. 在 Windows PowerShell 中查詢你目前的 IP 位址（通常是 WSL 網卡的 Gateway）。
    
2. 或者在 WSL 中直接借用 Windows 的 Proxy。你可以嘗試把 Windows 的 Proxy 網址導給 WSL 的環境變數：
    
    Bash
    
    ```
    export http_proxy="http://你的代理伺服器IP:連接埠"
    export https_proxy="http://你的代理伺服器IP:連接埠"
    ```
    

建議你先從 **方案一（Mirrored 模式）** 開始嘗試，因為這通常是一勞永逸的作法，連後續在 WSL 裡裝 Conda 套件、跑 pip 都會順暢很多。

你可以先幫我試試看方案一，執行 `wsl --shutdown` 重啟後，`git clone` 有順利跑出進度條嗎？

---

沒問題，連不上網路時最怕「瞎子摸象」，我們直接用指令來**抽絲剝繭**，確認方法一和方法二到底有沒有生效。這也能幫我們看清到底是「設定沒吃進去」還是「被防火牆/公司網路攔截」了。

請在 WSL 視窗中依序執行以下步驟來驗證：

## 🔍 驗證方法二：DNS 是否成功改為 `8.8.8.8`？

這個最容易驗證，我們直接看設定檔內容以及能不能解析網址。

### 步驟 1：檢查設定檔內容

在 WSL 中輸入：

Bash

```
cat /etc/resolv.conf
```

- **成功設定的長相：** 畫面上應該只會出現你手動寫入的 `nameserver 8.8.8.8` 和 `nameserver 1.1.1.1`。
    
- **失敗的長相：** 如果出現很多英文字（說這是自動產生的），代表系統在重啟時又把你的設定覆蓋掉了。
    

### 步驟 2：測試網址解析

在 WSL 中輸入：

Bash

```
nslookup github.com
```

- **成功：** 會噴出 `github.com` 的好幾組 IP 位址（例如 `20.205.243.166`）。這代表 **DNS 沒問題，WSL 認得 github 是誰**。
    
- **失敗：** 出現 `connection timed out` 或 `can't find github.com`。代表 DNS 依然是死的。
    

## 🔍 驗證方法一：Mirrored（鏡像）模式有沒有啟動？

鏡像模式成功啟動的話，WSL 內部的網卡會直接複製 Windows 的網卡設定。

在 WSL 中輸入：

Bash

```
ip route
```

- **成功啟動（Mirrored）：** 你會看到預設路由（default）指向的 IP，通常會跟你 Windows 實體網路（如 Wi-Fi 或公司區網）的 Gateway 一模一樣。
    
- **未啟動（傳統 NAT）：** 預設路由會指向一個 `172.x.x.x` 開頭的虛擬 IP。
    

> ⚠️ **Windows 的隱藏陷阱：**
> 
> 你在 Windows 建立 `.wslconfig` 時，**微軟可能會偷偷幫你加上 `.txt` 副檔名**（變成 `.wslconfig.txt`），這樣 WSL 是完全讀不到的！
> 
> - **檢查方式：** 請在 Windows PowerShell 裡輸入 `ls C:\Users\ydnaa\.wslconfig*`，確認它的名字真的只有 `.wslconfig`，沒有任何尾巴。
>     

## 🚨 如果驗證都過了，卻還是 Timeout？（終極排查）

如果你發現 `nslookup github.com` 能成功查到 IP，但 `git clone` 依然卡死，這代表 **DNS 對了，但網路流量（443 Port）在出門時被攔截了**。

既然你的電腦名稱叫 `LABNB01`，強烈懷疑是以下兩個原因之一：

### 1. 公司/實驗室防火牆或防毒軟體（如 Kaspersky、Trend Micro）

Windows 的防毒軟體或防火牆常常把 WSL 視為「外部不明程式」，直接把它的外流燈號（Outbound traffic）剪掉。

- **測試指令：** 在 WSL 裡改用 `curl` 戳戳看 Google：
    
    Bash
    
    ```
    curl -I https://www.google.com
    ```
    
    如果連 Google 也是 Timeout，那確定是 WSL 的網路全部被 Windows 防火牆或防毒鎖死了。
    

### 2. GitHub 阻擋了 HTTPS

有時候網路環境對 Git 的 HTTPS 協定（443 埠）不友善，但對 SSH（22 埠）是通的。

- **測試指令：** 測試看看能不能用 SSH 敲 GitHub 的門：
    
    Bash
    
    ```
    ssh -T git@github.com
    ```
    
    _（如果回應 `Hi! You've successfully authenticated...` 雖然拒絕連線但認得你，代表 SSH 是通的！那我們之後可以改用 SSH 機制來 clone。）_
    

你先幫我跑跑看 `nslookup github.com` 和 `cat /etc/resolv.conf`，看看回傳了什麼？我們一項一項把兇手抓出來！

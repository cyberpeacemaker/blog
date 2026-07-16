---
created: 2026-07-16 20:07
updated: 2026-07-16 20:07
tags: []
type: reference
lang: en
status: draft
---
這個測試結果是個**非常經典的「WSL2 網路靈異現象」**。

它給出了兩個非常明確的關鍵訊號：

1. **`ping` 成功（且域名有成功解析）：** 代表你的 WSL 內部的 **DNS 解析正常**，而且 **ICMP 協定（小封包）是通的**。
    
2. **`curl` 卻全部掛掉（Hang 住）：** 代表只要走 **TCP 協定（HTTP/HTTPS 的 Port 80/443 大封包）** 就會被中途丟棄或攔截。
    

因為你的設備名稱帶著 `LABNB01`，這高機率是**公司/實驗室的網路環境、企業防毒防火牆，或是開啟了 VPN** 所導致的。底層原因通常有兩個：

- **MTU（最大傳輸單元）不一致：** 企業網路或 VPN 的封包上限較小（例如 1350），但 WSL2 預設用 1500。`ping` 的封包很小所以過得去，`curl` 發起 HTTP 握手時封包太大，結果在虛擬網卡被直接丟棄。
    
- **防火牆/防毒軟體攔截：** 公司的安全軟體（例如 Symantec, Windows Defender 的 Hyper-V 防火牆）只放行了主機的 TCP，卻把 WSL2 虛擬網卡送出的 TCP 流量給擋了。
    

## 🛠️ 終極解決方案：開啟 Windows 11 鏡像網路模式（Mirrored Mode）

既然你是 **Win11**，微軟在後期版本提供了一個專門解決這個痛點的特效藥 —— **鏡像網路模式**。它會讓 WSL2 直接共享 Windows 主機的網路卡與所有權限，直接繞過虛擬交換器、MTU 限制與企業防火牆。

請在 Windows 端依照以下步驟設定：

### 1. 在 Windows 建立設定檔

在 Windows 中打開 **記事本**，並將檔案另存新檔為：

- 路徑：`C:\Users\ydnaa\.wslconfig` （請注意前面有一個點 `.`，這是在你的 Windows 使用者家目錄下）
    
- 檔案內容貼上以下這幾行：
    

Ini, TOML

```
[wsl2]
networkingMode=mirrored
dnsTunneling=true
firewall=false
```

### 2. 重啟 WSL

回到 Windows 的 PowerShell（或是任何 Windows 終端機），強制關閉 WSL 讓設定生效：

PowerShell

```
wsl --shutdown
```

### 3. 重新進入 WSL 測試

重新打開你的 WSL 終端機，再次挑戰剛剛卡住的指令：

Bash

```
curl -I https://www.google.com
```

如果設定成功，這次應該一秒內就會刷出 HTTP 200 或 301 的回應了！

## 💡 備用測試（如果是純粹的 MTU 問題）

如果你暫時不想動 `.wslconfig`，可以在 WSL 內部先用這行指令，把網卡的封包大小（MTU）強行調小，測試看看是不是純 MTU 的鍋：

Bash

```
sudo ip link set dev eth0 mtu 1350
curl -I https://www.google.com
```

_（如果調完 1350 就能動，那就百分之百是 MTU 的問題。不過長遠來看，改用上面的 `mirrored` 鏡像模式是最一勞永逸的作法。）_

試試看這個 Win11 的鏡像模式，通常有 90% 的企業網路卡死問題都能靠這招原地復活！


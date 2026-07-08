---
created: 2026-07-07
tags: [uncategorized, forensic, windows]
type: howto
lang: zh
status: draft
---

> Related: [[Inbox]]

```powershell
# 1. 請在下方引號內替換成你的真實資料夾路徑
$FolderPath = "C:\Users\ydnaa\Documents\Github\2025-06-02-萬大班設備"

Write-Host "=============================================" -ForegroundColor Cyan
Write-Host "   🕵️‍♂️ Windows 資料夾權限與來源數位鑑識" -ForegroundColor Cyan
Write-Host "=============================================" -ForegroundColor Cyan

# 2. 取得目前登入使用者的真實 SID
$CurrentUser = [System.Security.Principal.WindowsIdentity]::GetCurrent()
Write-Host "[+] 你目前登入的帳號 : $($CurrentUser.Name)"
Write-Host "[+] 你目前帳號的 SID : $($CurrentUser.User.Value)"
Write-Host "---------------------------------------------"

# 3. 讀取資料夾的擁有者與權限
try {
    $Acl = Get-Acl -Path $FolderPath
    $Owner = $Acl.Owner
    Write-Host "[+] 資料夾掛名的擁有者: $Owner" -ForegroundColor Yellow
    
    # 嘗試解析擁有者的 SID
    try {
        $OwnerSID = (New-Object System.Security.Principal.NTAccount($Owner)).Translate([System.Security.Principal.SecurityIdentifier]).Value
        Write-Host "[+] 該擁有者的真實 SID: $OwnerSID"
    } catch {
        Write-Host "[!] 警告：無法解析擁有者的名稱！這代表該帳號在目前系統中並不存在。" -ForegroundColor Red
        $OwnerSID = "UNKNOWN"
    }
    
    # 診斷一：擁有者比對
    if ($OwnerSID -eq $CurrentUser.User.Value) {
        Write-Host "[v] 判定：擁有者與你目前的帳號相同。刪不掉可能是因為 UAC 或細部 Deny 規則卡死。" -ForegroundColor Green
    } else {
        Write-Host "[X] 判定：擁有者 SID 與你目前的帳號【不符】！" -ForegroundColor Red
        Write-Host "    -> 這 100% 證實了它是從其他系統搬移過來（殘留舊 SID），或是由某個以獨立權限執行的 Agent 產生的！" -ForegroundColor DarkYellow
    }
    
    Write-Host "---------------------------------------------"
    Write-Host "[+] 正在掃描細部存取控制清單 (ACE)..."
    
    $HasDeny = $false
    $HasOrphan = $false

    foreach ($Access in $Acl.Access) {
        $Identity = $Access.IdentityReference.Value
        $AccessType = $Access.AccessControlType
        $Rights = $Access.FileSystemRights
        
        # 診斷二：檢查有沒有「孤兒 SID」 (名稱顯示為 S-1-5-... 的亂碼)
        if ($Identity -match "^S-1-5-") {
            Write-Host "  ⚠️ 發現孤兒 SID: $Identity (權限: $Rights)" -ForegroundColor DarkYellow
            $HasOrphan = $true
        }
        
        # 診斷三：檢查有沒有隱藏的 Deny (拒絕) 規則
        if ($AccessType -eq "Deny") {
            Write-Host "  🛑 發現【拒絕 (Deny)】規則! 帳號: $Identity 限制了: $Rights" -ForegroundColor Red
            $HasDeny = $true
        }
    }

    Write-Host "---------------------------------------------"
    Write-Host "====== 最終診斷報告 ======" -ForegroundColor Cyan
    if ($HasOrphan) { Write-Host "👉 結論 A：畫面上出現 S-1-5 開頭的亂碼，代表這資料夾是從舊電腦/舊系統直接複製過來的，現在的系統根本不認識當初的創作者。" -ForegroundColor Yellow }
    if ($HasDeny) { Write-Host "👉 結論 B：發現 Deny 規則！在 Windows 中，Deny 的優先級高於 Allow，就算你是 Admin，只要被 Deny 咬到就絕對刪不掉。" -ForegroundColor Red }
    if (-not $HasOrphan -and -not $HasDeny -and ($OwnerSID -ne $CurrentUser.User.Value)) { Write-Host "👉 結論 C：單純是擁有者（Owner）被鎖死在當初建立的自動化工具（或特定本機帳號）身上，現有帳號沒有被賦予繼承權限。" -ForegroundColor Yellow }

} catch {
    Write-Host "[!] 錯誤：連資料夾的權限結構都讀取失敗，可能被更高階的系統權限鎖死。$($_.Exception.Message)" -ForegroundColor Red
}
Write-Host "=============================================" -ForegroundColor Cyan
```
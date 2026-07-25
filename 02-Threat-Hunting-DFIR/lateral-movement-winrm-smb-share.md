---
title: "WinRM and SMB Admin Share Lateral Movement"
description: "Explains why WinRM remote execution and SMB admin-share drops require valid credentials or equivalent hashes/tickets."
created: 2026-07-23
updated: 2026-07-24
tags: [threat-hunting, dfir, mitre]
type: reference
lang: zh
status: draft
---

> Related: [[MOC - Threat Hunting]] · [[bec-encrypted-traffic-analysis]] · [[windows-user-determine]]

**是的，這種攻擊路徑基本上需要預先取得有效的帳號密碼（或等效的認證憑證）。**

在這段描述中，攻擊者使用了 **WinRM 遠端執行** 與 **SMB 管理員共享（Admin Shares）** 來進行橫向移動（Lateral Movement），這兩個服務在 Windows 預設定位中都有嚴格的身份驗證機制。

## 關鍵技術解析：為什麼需要憑證？

### 1. SMB 管理員共享（SMB Admin Share）

- **機制**：描述中提到的「SMB admin-share drop」，通常是指存取目標主機的預設隱藏共享目錄（例如 `\\IP\ADMIN$` 或 `\\IP\C$`）並寫入檔案。
    
- **權限要求**：Windows 預設僅限本地管理員（Local Administrators）或網域管理員（Domain Admins）具備存取權限。未通過身份驗證的匿名使用者無法上傳檔案。
    

### 2. WinRM 遠端執行（WinRM Remote-Exec）

- **機制**：WinRM（Windows Remote Management）是 Windows 用於遠端管理的協定（預設埠 5985/5986）。
    
- **權限要求**：必須提供有效的使用者名稱與密碼（或 Kerberos / NTLM 認證資訊），且該帳號必須屬於目標主機的 `Remote Management Users` 或 `Administrators` 群組。
    

## 攻擊者實際上是如何做到的？

攻擊者不一定需要知道「明文密碼」，只要具備以下其中一種條件，即可達成描述中的操作：

- **哈希傳遞攻擊（Pass-the-Hash, PtH）**：
    
    若攻擊者先前已從跳板機（Pivot）傾印出管理員的 **NTLM Hash**（例如使用 Mimikatz 擷取到的 Hash），即可直接利用該 Hash 對 WinRM 或 SMB 進行認證，完全不需要將其破解為明文密碼。
    
- **密碼重用（Credential Reuse） / 權限繼承**：
    
    如果跳板機與目標主機（`Dist-EWS`）使用了相同的本地管理員密碼（Local Admin），或者攻擊者使用的是網域管理員（Domain Admin）權限，就能直接連線並控管。
    
- **票據傳遞攻擊（Pass-the-Ticket, PtT）**：
    
    利用記憶體中已有的 Kerberos 票據（TGT/TGS）進行連線。
    

## 總結

這段描述展示的是典型的**取得憑證後的橫向移動（Post-Exploitation Lateral Movement）**，而不是利用無須認證的遠端程式碼執行漏洞（Unauthenticated RCE）。攻擊者必然已經在先前的步驟中，取得了能代表 `Dist-EWS` 管理員權限的憑證或 Hash。

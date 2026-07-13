---
created: 2026-07-13 15:07
updated: 2026-07-13 15:07
tags: []
type: reference
lang: en
status: draft
---
It is completely valid to be confused here, and you probably _did_ install it! This is one of the most frustrating quirks of modern Windows: installing PowerShell 7+ doesn't automatically replace or upgrade the built-in Windows PowerShell (v5.1). Instead, they live side-by-side as two completely different programs.

Windows PowerShell is `powershell.exe`, and PowerShell 7+ is `pwsh.exe`. Right now, your terminal profile (likely inside VS Code) is still opening the old version by default.

Here is how to check what version you are currently looking at and how to swap it over.

### 1. Double-Check Your Current Version

Run this exact command in your current terminal window:

PowerShell

```
$PSVersionTable.PSVersion
```

If the `Major` version says **5**, you are running the legacy Windows PowerShell, which explains why `&&` threw that error.

### 2. How to Switch to PowerShell 7 in VS Code

Since you are working in a GitHub repository with a virtual environment (`otex-claw`), you are likely using VS Code's built-in terminal. To make it use PowerShell 7 permanently:

1. Look at the top-right corner of your terminal panel in VS Code.
    
2. Click the **dropdown arrow** right next to the `+` icon (or next to the trash can icon depending on your layout).
    
3. Click **Select Default Profile**.
    
4. A menu will drop down from the top command palette. Select **PowerShell** (it usually has a stylized dark blue/grey icon and points to `pwsh.exe`), rather than "Windows PowerShell".
    
5. Kill your current terminal instance (click the trash can icon) and open a new one (`Ctrl + ``).
    

> 💡 **Bonus Check:** If you don't see PowerShell 7 in that dropdown list, it might just need a quick system reboot, or you can launch it directly from your Windows Start Menu by searching for **PowerShell 7** or **Pwsh**.

Once you are officially running under `pwsh.exe`, your original `&&` command will work perfectly!


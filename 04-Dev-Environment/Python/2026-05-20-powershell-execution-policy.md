---
created: 2026-05-20
tags: [dev]
type: reference
lang: en
status: draft
---

Haha, I'm glad the explanation helped!

PowerShell is acting like a strict security guard right now. By default, Windows blocks scripts from running in PowerShell to protect your system from malware. Because Python's virtual environment activation tool relies on a script (`Activate.ps1`), PowerShell is refusing to load it.

Here are the easiest ways to bypass the guard and get your environment activated:

### Method 1: Bypass it for just this terminal session (Recommended & Safest)

You can tell PowerShell to lower its guard *only* for the specific terminal window you have open right now. Once you close the terminal, the restriction goes back to normal.

1. Copy and paste this command into your terminal and press **Enter**:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

```


2. Now, run your activation command again:
```powershell
.\venv\Scripts\activate

```



---

### Method 2: Fix it permanently for your user account

If you don't want to keep typing that bypass command every time you open VS Code, you can permanently allow scripts that you create on your own computer.

1. Run this command:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

```


2. It might ask you to confirm. Type **Y** and press **Enter**.
3. Now run your activation command:
```powershell
.\venv\Scripts\activate

```



---

### Method 3: The Command Prompt workaround

If PowerShell continues to give you a hard time, you can temporarily drop into the old-school Windows Command Prompt inside that exact same window, which doesn't have these script restrictions.

1. Type `cmd` and press **Enter** (your prompt will change slightly).
2. Run the Command Prompt version of the script:
```cmd
.\venv\Scripts\activate.bat

```



Once activated, your terminal prompt will show `(venv)` at the beginning of the line, meaning you are good to go!

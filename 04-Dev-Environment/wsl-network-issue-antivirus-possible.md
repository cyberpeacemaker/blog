---
title: "WSL Network Blocks from Antivirus"
description: "Explains how Symantec Endpoint Protection SONAR can quarantine dev tools and interfere with WSL networking."
created: 2026-07-13
updated: 2026-07-13
type: reference
lang: en
status: draft
tags: [dev, windows, wsl, security]
---

> Related: [[MOC - Dev Environment]] · [[wsl-network-troubleshooting]] · [[conda-install-option]]

**Yes, this is absolutely a problem**, and it is the smoking gun that explains why your setup is breaking.

Your Symantec Endpoint Protection (SEP) **SONAR** system is actively flagging and likely blocking or quarantining your project executable: `c:\users\ydnaa\miniconda3\envs\otex-claw\scripts\otex-claw.exe`.

Here is a breakdown of what is happening and how to fix it:

### 1. What is "SONAR" doing?

SONAR is Symantec’s real-time behavioral heuristic engine. It doesn't look for known viruses; instead, it looks for "suspicious behavior."

Because `otex-claw.exe` was newly created by your Python/Conda environment, it has zero global reputation. To an enterprise antivirus, a brand-new, unrecognized `.exe` trying to run or access the network looks exactly like a zero-day malware attack.

### 2. The Connection to Your Network Issue

Look closely at the other logs: SONAR is also tracking or blocking `com.docker.backend.exe` and `icacls.exe` (a Windows tool used to change file permissions).

If Symantec is being this aggressive with your development tools, **it is almost certainly the reason your WSL network connection was blocked** in your previous step. Enterprise antiviruses frequently block WSL's virtual network adapter from communicating with the outside world.

### How to Fix This

Since you are on a lab laptop (`-LABNB01`), your security policies might be strict, but try these steps:

#### Step 1: Check if the file was deleted (Quarantine)

On the left-hand menu of your Symantec window, click **檢視隔離區 (View Quarantine)**.

- If you see `otex-claw.exe` in there, Symantec deleted it.
    
- If you have administrative rights, you can right-click it and select **還原 (Restore)** and choose to exclude it from future scans.
    

#### Step 2: Add a Folder Exception (Exclusion)

To stop Symantec from bullying your development environment, you need to tell it to ignore your Conda directory.

1. In the Symantec main window, look for **變更設定 (Change Settings)** or **例外清單 (Exceptions)**.
    
2. Add an exception for the entire folder path:
    
    `C:\Users\ydnaa\miniconda3\`
    
3. If you are using WSL, you may also need to add an exception for your WSL network or project folders.
    

> 💡 **Note on the `????` text:** Don't worry about the question marks in the log. That is just a common text-encoding bug (usually a mismatch between a Chinese Windows locale and Symantec's English log formatting). The text layout is fine; it's just the language displaying incorrectly.

If you don't have local admin rights to add these exceptions, you will need to ask your lab's IT administrator to whitelist your `miniconda3` directory so you can get your work done!


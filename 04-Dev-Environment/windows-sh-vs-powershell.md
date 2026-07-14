---
title: "Windows Shell Scripts vs PowerShell"
description: "Explains why Linux .sh and systemd scripts do not run natively in Windows PowerShell."
created: 2026-07-13
updated: 2026-07-13
type: reference
lang: en
status: draft
tags: [dev, windows, powershell]
---

> Related: [[MOC - Dev Environment]] · [[powershell-v5-v7]] · [[env-setup]]

### The Short Answer: No, you cannot run this natively in Windows 11 PowerShell.

If you try to run it, PowerShell will either throw an error saying it doesn't recognize the command, or it will just open the file in a text editor.

### Why won't it work?

There are two major reasons this script won't work on your current setup:

1. **`.sh` files are Bash scripts:** These are written for Unix-like operating systems (Linux and macOS). PowerShell uses `.ps1` scripts and doesn't understand Bash syntax by default.
    
2. **`systemd` is Linux-only:** `systemd` is a system and service manager exclusive to Linux. It handles background processes (daemons) on servers. Windows 11 doesn't have `systemd`; it uses **Windows Services** instead.
    

### Do you actually need to run this?

**Probably not!**

Since you are inside a `web/frontend` directory, this script was likely included by the project developers for **deploying the app to a production Linux server** so it runs continuously in the background.

For local development on your Windows machine, you can completely ignore this script. You just need to run your standard npm development command.

### What should you do instead?

If you just want to run the project and see it in your browser:

1. Make sure you are in your frontend folder.
    
2. Run:
    
    Bash
    
    ```
    npm run dev
    ```
    
    _(Or `npm start` / `npm run start`, depending on what is defined in your `package.json`)._
    

If the project **absolutely requires** a Linux environment to function (for example, if the backend relies heavily on Linux-specific tools), you will need to install and use **WSL2 (Windows Subsystem for Linux)** on your Windows 11 machine.

Are you trying to just test and edit the frontend locally, or are you trying to host this project as a permanent server on your machine?


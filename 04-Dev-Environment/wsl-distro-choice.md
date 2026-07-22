---
title: "Choose and Launch WSL Distros"
description: "PowerShell commands for listing WSL distributions, launching a specific distro, and changing the default distro."
created: 2026-07-21
updated: 2026-07-21
tags: [dev]
type: howto
lang: en
status: draft
---

> Related: [[MOC - Dev Environment]] · [[wsl-distro]] · [[wsl-distro-switch]]

Now that you have both Ubuntu and Kali installed, typing just `wsl` will launch whichever one is set as your **default**.

Here are the easiest ways to check your installed distros, launch specific ones, or change your default.

## 1. Check Your Distro Names First

Before running commands, check the exact name WSL assigned to each distro and see which one is currently your default (marked with an asterisk `*`).

Open PowerShell or Command Prompt and run:

DOS

```
wsl -l -v
```

## 2. Launch a Specific Distro Directly

You can launch any distro on demand using the `-d` (distribution) flag followed by its name:

- **Launch Kali:**
    
    DOS
    
    ```
    wsl -d kali-linux
    ```
    
- **Launch Ubuntu:**
    
    DOS
    
    ```
    wsl -d Ubuntu
    ```
    

_(Note: Replace `kali-linux` or `Ubuntu` with the exact names shown in your `wsl -l -v` list)._

## 3. Change Your Default Distro

If you want typing `wsl` to launch a specific distro every time, you can change the default using the `--set-default` (or `-s`) flag:

- **Set Kali as default:**
    
    DOS
    
    ```
    wsl --set-default kali-linux
    ```
    
- **Set Ubuntu as default:**
    
    DOS
    
    ```
    wsl --set-default Ubuntu
    ```
    

Now, whenever you just type `wsl`, it will open your newly selected default distro.

## Alternative (Easier) GUI Methods

- **Windows Terminal:** If you use Windows Terminal, click the **dropdown arrow `v`** next to the new tab button at the top. You'll see direct profiles for both Ubuntu and Kali Linux, allowing you to run both side-by-side in separate tabs.
    
- **Start Menu:** You can simply open the Windows Start Menu and search for **"Ubuntu"** or **"Kali"** to launch them as standalone windows.


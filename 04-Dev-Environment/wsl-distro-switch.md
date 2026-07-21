---
title: "Switch Between WSL Distros"
description: "PowerShell commands for stopping Kali, launching Ubuntu, and setting Ubuntu as the default WSL distribution."
created: 2026-07-21
updated: 2026-07-21
tags: [dev]
type: howto
lang: en
status: draft
---

> Related: [[MOC - Dev Environment]] · [[wsl-distro-choice]] · [[default-wsl-distro-dev-containers]]

Here are the commands to run in your PowerShell terminal:

## 1. Stop Kali Linux

To terminate only the running Kali Linux instance:

PowerShell

```
wsl --terminate kali-linux
```

_(Or the shorthand version: `wsl -t kali-linux`)_

## 2. Enter Ubuntu 24.04

To launch and open the Ubuntu terminal:

PowerShell

```
wsl -d Ubuntu-24.04
```

_(Or using the full flag: `wsl --distribution Ubuntu-24.04`)_

### 💡 Useful Tips

- **Stop all running WSL distributions at once:**
    
    PowerShell
    
    ```
    wsl --shutdown
    ```
    
- **Set Ubuntu as your default distribution** (so typing just `wsl` will always launch Ubuntu instead of Kali):
    
    PowerShell
    
    ```
    wsl --set-default Ubuntu-24.04
    ```


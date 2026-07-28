---
title: "Ollama Get Started"
description: "Shows how to stop, start, and verify the Ollama service on Windows for local LLM workflows."
created: 2026-07-27
updated: 2026-07-27
tags: [ai, agents, dev]
type: howto
lang: en
status: draft
---

> Related: [[MOC - AI Agents]] · [[local-ai]] · [[claude-to-local-migration]] · [[My Stack]]

Here's the quick breakdown for controlling Ollama on Windows 11.

### How to Turn OFF Ollama

Since Ollama runs as a background service on Windows, closing the terminal doesn't actually stop it. Use either of these methods to turn it off completely:

#### **Method 1: System Tray (Easiest)**

1. Look at the **bottom-right corner** of your screen (near the clock).
    
2. Click the small **up arrow `^`** to open the hidden system tray icons.
    
3. Right-click the **Ollama icon** (a llama outline).
    
4. Click **Quit Ollama**.
    

#### **Method 2: PowerShell / Command Prompt**

Run this command to force-stop all Ollama background processes immediately:

PowerShell

```
Stop-Process -Name "ollama*" -Force
```

### How to Turn ON Ollama

#### **Method 1: Start Menu (UI)**

- Press the **Windows Key**, type **Ollama**, and press **Enter**.
    
- The Ollama icon will reappear in your System Tray, and `http://localhost:11434` will start responding again.
    

#### **Method 2: Command Line (Automatic)**

- Whenever you run an `ollama` command in PowerShell (like `ollama run qwen2.5-coder:7b` or `ollama serve`), Windows will **automatically boot the Ollama background engine** if it isn't already running.
    

> **Good to know (Automatic Memory Cleanup):**
> 
> You don't necessarily have to turn Ollama off every time. When you finish using Continue in VS Code, Ollama will automatically unload the model from your system RAM after **5 minutes of inactivity**, reducing its baseline RAM usage to under 50 MB.


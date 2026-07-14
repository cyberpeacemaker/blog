---
title: "Windows File Permissions with icacls"
description: "Provides a documentation template for Linux chmod and Windows icacls equivalents for sensitive files."
created: 2026-07-13
updated: 2026-07-13
type: howto
lang: en
status: draft
tags: [dev, windows, security]
---

> Related: [[MOC - Dev Environment]] · [[win-linux-crlf]] · [[env-setup]]

## How to Write the Instruction (Documentation Template)

  

When writing drafting instructions, you want them to be highly scannable so users don't accidentally copy-paste a Linux command into a Windows terminal.

  

Here is a clean, markdown-ready format you can drop right into your documentation:

  

```markdown

## Step X: Secure the Sensitive Patterns File

  

To protect your configuration, you must restrict the file permissions so that only your user account can read or write to it. Choose the command appropriate for your Operating System:

  

### Linux / macOS

Open your terminal and run:

```bash

chmod 600 ~/.config/otex-claw/sensitive-patterns

  

```

  

### Windows (Command Prompt)

  

Open CMD and run:

  

```cmd

icacls "%USERPROFILE%\.config\otex-claw\sensitive-patterns" /inheritance:r /grant:r "%USERNAME%":F

  

```

  

### Windows (PowerShell)

  

Open PowerShell and run:

  

```powershell

icacls "$HOME\.config\otex-claw\sensitive-patterns" /inheritance:r /grant:r "$($env:USERNAME):F"

  

```

  

```

  

### 💡 Pro-Tip for Writing Technical Layouts:

Keep the OS blocks visually distinct using headings or tabs if your documentation platform supports them. Notice that the paths for Windows use backslashes (`\`) instead of forward slashes (`/`), which ensures native compatibility across all Windows setups.

  

```


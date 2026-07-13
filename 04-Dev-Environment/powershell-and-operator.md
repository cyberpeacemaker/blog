---
title: "PowerShell && Operator Compatibility"
description: "Shows alternatives to the Bash-style && operator in Windows PowerShell 5 and when PowerShell 7 supports it."
created: 2026-07-13
updated: 2026-07-13
type: howto
lang: en
status: draft
tags: [dev, windows, powershell]
---

> Related: [[MOC - Dev Environment]] · [[powershell-v5-v7]] · [[powershell-execution-policy]]

Ah, the classic Windows PowerShell trap!

You are seeing this error because you are likely running the default **Windows PowerShell (version 5.1 or lower)**. The `&&` operator (which runs the second command _only_ if the first one succeeds) wasn't introduced to PowerShell until version 7.0.

Here is how you can fix it depending on what you want to achieve:

### Option 1: The True `&&` Equivalent (Recommended)

If you want `ruff format` to run **only if** `ruff check` passes without errors, use the automatic variable `$?` (which checks if the last command was successful):

PowerShell

```
ruff check otex_claw/ ; if ($?) { ruff format otex_claw/ }
```

### Option 2: Run Both Regardless of Success

If you don't care whether the check passes or fails and just want to run both commands back-to-back, use a semicolon (`;`):

PowerShell

```
ruff check otex_claw/ ; ruff format otex_claw/
```

### Option 3: Upgrade PowerShell

If you want to use `&&` natively like you would in Bash, Zsh, or Command Prompt, you can install the modern **PowerShell 7+**.

> 💡 **Quick tip on your comment:** If you actually wanted to pass those comment values (`line-length=100`, `py311`) as configuration flags directly to Ruff rather than just keeping them as notes, you can append them like this:
> 
> PowerShell
> 
> ```
> ruff check otex_claw/ --line-length 100 --target-version py311 ; if ($?) { ruff format otex_claw/ --line-length 100 --target-version py311 }
> ```
> 
> _(Though putting these in a `pyproject.toml` or `ruff.toml` file is usually much cleaner!)_


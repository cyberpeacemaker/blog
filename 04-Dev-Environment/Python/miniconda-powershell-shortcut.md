---
title: "Dedicated Miniconda PowerShell Shortcut"
description: "Shows how to undo global conda init and launch Conda only through a dedicated PowerShell shortcut."
created: 2026-07-09
updated: 2026-07-09
type: howto
lang: en
status: draft
tags: [dev, python]
---

> Related: [[MOC - Dev Environment]] · [[conda-miniconda]] · [[conda-powershell]]
Sharp eye! Yes, that is exactly what `conda init` did. It appended a block of startup code to your personal PowerShell profile script (`$PROFILE`). If you like keeping your global PowerShell clean and fast without Conda loading every single time you open a terminal, your instinct is 100% correct.

You can completely undo that profile modification and launch a standalone "Miniconda Prompt" manually instead.

### Step 1: Clean Up Your PowerShell Profile (Undo)

Before doing anything else, run this command in your current PowerShell window to cleanly strip the Conda code out of your profile:

PowerShell

```
conda init powershell --reverse
```

_Note: Once you close this PowerShell window, the `conda` command will stop working globally, just like you wanted._

### Step 2: Find Your Exact Miniconda Path

Because we need the exact file path to build your custom shortcut, run this quick snippet to see exactly where `winget` installed it on your drive:

PowerShell

```
["$HOME\miniconda3", "C:\ProgramData\miniconda3", "$env:LOCALAPPDATA\miniconda3"] | Where-Object { Test-Path "$_\Scripts\conda.exe" }
```

Keep note of the path it prints out (it will likely be something like `C:\Users\YourName\miniconda3` or `C:\ProgramData\miniconda3`).

### Step 3: Create a Dedicated "Conda Prompt" Shortcut

Instead of messing with your profile, you can create a classic desktop shortcut that triggers a temporary, self-contained Conda session only when clicked.

1. Right-click on an empty space on your **Desktop** and select **New > Shortcut**.
    
2. In the location box, paste the following single line (make sure to replace `C:\YOUR\PATH\TO` with the exact path you found in Step 2):
    

Plaintext

```
powershell.exe -ExecutionPolicy ByPass -NoExit -Command "& 'C:\YOUR\PATH\TO\miniconda3\shell\condabin\conda-hook.ps1' ; conda activate"
```

3. Click **Next**, name the shortcut **Miniconda PowerShell**, and click **Finish**.
    

### How it works now:

- Your normal PowerShell stays perfectly vanilla and untouched.
    
- Whenever you want to use Conda or manage your environments, just double-click your new **Miniconda PowerShell** desktop shortcut. It will open a dedicated terminal window with the `(base)` environment active and ready to go!

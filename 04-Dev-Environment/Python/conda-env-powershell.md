---
title: "Conda Env Creation in PowerShell"
description: "Shows how to initialize Conda for PowerShell before creating an environment from environment.yml."
created: 2026-07-14 17:07
updated: 2026-07-14 17:07
tags: [dev, python]
type: reference
lang: en
status: draft
---

> Related: [[MOC - Dev Environment]] · [[conda-powershell]] · [[powershell-execution-policy]]

This error happens because Windows PowerShell doesn't know where `conda` is located yet. Even though you installed it, the command hasn't been registered with your standard PowerShell environment.

Here is the quickest and most reliable way to fix it.

## Method 1: The Recommended Fix (Via Anaconda Prompt)

Instead of manually messing with system paths, you can let Conda register itself to your PowerShell.

1. Open your Windows **Start Menu**.
    
2. Search for **Anaconda Prompt** (or **Miniconda Prompt**, depending on what you installed) and open it.
    
3. In that black terminal window, type the following command and press **Enter**:
    
    PowerShell
    
    ```
    conda init powershell
    ```
    
4. Close your current PowerShell window in your project (`otex-claw`), open a fresh one, and try your command again:
    
    PowerShell
    
    ```
    conda env create -f environment.yml
    ```
    

## Troubleshooting: "Script Execution" Error?

After doing the steps above, when you open PowerShell, you _might_ see a red error saying scripts are disabled on this system. If that happens, run this command in PowerShell to give it permission to load Conda:

PowerShell

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

_(Type `Y` and press Enter if prompted. Then restart PowerShell again)._

## Method 2: The Manual Fix (If Method 1 didn't work)

If you can't find the Anaconda Prompt in your Start menu, you will need to add Conda to your Windows Environment Variables manually.

1. Press the **Windows Key**, type **"env"**, and select **Edit the system environment variables**.
    
2. Click the **Environment Variables...** button at the bottom right.
    
3. Under _User variables for ydnaa_, click on **Path** and click **Edit...**.
    
4. Click **New** and add these three paths (replace `anaconda3` with `miniconda3` if you installed Miniconda):
    
    - `C:\Users\ydnaa\anaconda3`
        
    - `C:\Users\ydnaa\anaconda3\Scripts`
        
    - `C:\Users\ydnaa\anaconda3\Library\bin`
        
5. Click **OK** on all windows to save.
    
6. **Restart your PowerShell** or VS Code so it detects the new paths.


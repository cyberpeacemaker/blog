---
created: 2026-07-13 15:07
updated: 2026-07-13 15:07
tags: []
type: reference
lang: en
status: draft
---
Yes, absolutely! Deleting the `.wslconfig` file entirely will instantly revert WSL back to its default settings (which is standard NAT mode).

However, just remember the golden rule of WSL configuration: **it won't take effect until you completely restart the WSL subsystem.**

Here is the cleanest way to do it based on your setup:

### Option 1: Delete the whole file

If you created the file just for this networking test and it doesn't contain any other configurations, you can safely delete it.

1. Delete `.wslconfig` from your `%USERPROFILE%` folder.
    
2. Open Windows PowerShell or Command Prompt and run:
    
    DOS
    
    ```
    wsl --shutdown
    ```
    

### Option 2: Just comment it out (Recommended)

If you think you might want to toggle it back on later, or if you have other settings in that file you want to keep, don't delete the file. Just open it and add a `#` to comment it out:

Ini, TOML

```
[wsl2]
# networkingMode=mirrored
```

Save the file, and then run `wsl --shutdown` in PowerShell.

The next time you open your Kali terminal, it will be right back to using the default NAT networking.


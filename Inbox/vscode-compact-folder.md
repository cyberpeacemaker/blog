---
created: 2026-07-17 15:07
updated: 2026-07-17 15:07
tags: []
type: reference
lang: en
status: draft
---
Yes, you absolutely can! That feature is called **Compact Folders**, and VS Code enables it by default to save vertical space.

If you prefer to see your folders in a traditional, nested tree structure instead of `assets\reference`, you can disable this setting in one of two ways:

### Method 1: Using the Settings UI (Easiest)

1. Open the Settings menu:
    
    - **Windows/Linux:** Press `Ctrl` + `,`
        
    - **macOS:** Press `Cmd` + `,`
        
2. In the search bar at the top, type: **`compact folders`**
    
3. Look for the setting labeled **Explorer: Compact Folders**.
    
4. **Uncheck** the box to disable it.
    

_The explorer will update instantly, separating your folders into a normal tree structure._

### Method 2: Editing your `settings.json` file

If you prefer configuring VS Code via code:

1. Open the Command Palette:
    
    - **Windows/Linux:** Press `Ctrl` + `Shift` + `P`
        
    - **macOS:** Press `Cmd` + `Shift` + `P`
        
2. Search for and select: **`Preferences: Open User Settings (JSON)`**
    
3. Add the following line to your settings object:
    

JSON

```
"explorer.compactFolders": false
```

4. Save the file (`Ctrl + S` or `Cmd + S`).


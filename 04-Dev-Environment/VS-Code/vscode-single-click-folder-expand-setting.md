---
title: "VS Code Double-Click Folder Expansion"
description: "Shows how to make VS Code Explorer folders expand only on double-click so single-click can select paste targets."
created: 2026-07-25
updated: 2026-07-25
tags: [dev]
type: howto
lang: en
status: draft
---

> Related: [[MOC - Dev Environment]] · [[vscode-drag-and-drop]] · [[vscode-compact-folder]]

**Yes, you can!** You can change VS Code's behavior so folders only expand when double-clicked, allowing you to single-click a folder to select it (for pasting, renaming, or copying) without expanding its contents.

## Method 1: Using the Settings UI

1. Open **Settings**:
    
    - **Windows/Linux:** `Ctrl + ,`
        
    - **macOS:** `Cmd + ,`
        
2. Search for: **`workbench.tree.expandMode`** (or **Workbench > Tree: Expand Mode**).
    
3. Change the setting from `singleClick` to **`doubleClick`**.
    

## Method 2: Editing `settings.json`

If you prefer editing your configuration directly:

1. Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`).
    
2. Type **Preferences: Open User Settings (JSON)** and press `Enter`.
    
3. Add the following line:
    

JSON

```
"workbench.tree.expandMode": "doubleClick"
```

### How it works now

- **Single-Click on folder name:** Selects/highlights the folder without opening or expanding it. Perfect for selecting a target folder and pressing `Ctrl+V` / `Cmd+V` to paste.
    
- **Double-Click on folder name:** Expands or collapses the folder.
    
- **Clicking the Arrow Icon ($\boldsymbol{>}$):** Still immediately expands or collapses the folder with a single click.


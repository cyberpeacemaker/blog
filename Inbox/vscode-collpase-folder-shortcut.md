---
created: 2026-07-25 09:07
updated: 2026-07-25 09:07
tags: []
type: reference
lang: en
status: draft
---
Unfortunately, **there is currently no setting in VS Code to disable folder expansion when pasting a file.**

When you paste a file into a folder, VS Code automatically selects and focuses the newly pasted item in the Explorer tree view. To highlight the new file inside the directory, VS Code is hardcoded to expand the target folder.

While there isn't a toggle to disable this behavior yet, here are the two fastest workarounds to clean up your Explorer tree immediately:

## 1. The Instant Keyboard Trick (`←` `←`)

Right after pasting, your selection automatically sits on the newly created file inside the expanded folder. You can collapse it in a fraction of a second using your keyboard:

1. Press **`Ctrl + V`** (or **`Cmd + V`**) to paste.
    
2. Press **`←` (Left Arrow)** once to shift focus up to the parent folder.
    
3. Press **`←` (Left Arrow)** a second time to collapse the folder.
    

## 2. Collapse Folders with a Shortcut or Click

If multiple expanded folders start cluttering your Explorer view, you can collapse everything instantly:

- **Click the Collapse Icon:** Click the **Collapse Folders in Explorer** button (the icon with stacked layers and a minus sign) at the top-right toolbar of the **EXPLORER** panel.
    
- **Bind a Keyboard Shortcut:**
    
    1. Open Keyboard Shortcuts using **`Ctrl + K, Ctrl + S`** (or **`Cmd + K, Cmd + S`** on macOS).
        
    2. Search for **`Explorer: Collapse Folders in Explorer`** (Command ID: `workbench.files.action.collapse`).
        
    3. Assign a custom hotkey (such as **`Alt + C`**) to instantly close all open folders in the file tree with one keypress.


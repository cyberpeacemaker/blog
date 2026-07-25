---
title: "VS Code Drag and Drop Explorer Settings"
description: "Explains VS Code Explorer drag-and-drop auto-expansion behavior and safer file-moving alternatives."
created: 2026-07-25
updated: 2026-07-25
tags: [dev]
type: howto
lang: en
status: draft
---

> Related: [[MOC - Dev Environment]] · [[vscode-tips]] · [[vscode-single-click-folder-expand-setting]]

Currently, Visual Studio Code **does not have a setting** to disable or adjust the hover delay for auto-expanding folders while dragging and dropping files. This behavior is built directly into VS Code’s tree widget component.

However, you can use several settings and alternative methods to manage this behavior and prevent accidental moves.

## 1. Safety & Control Settings

While you cannot turn off hover expansion individually, you can adjust related settings in **Settings** (`Ctrl+,` or `Cmd+,` on macOS):

- **Ask for Confirmation Before Moving:**
    
    - **Setting:** `explorer.confirmDragAndDrop`
        
    - **Behavior:** Set this to `true` (enabled by default). If a folder expands unexpectedly while you drag, VS Code will prompt you to confirm before completing the move, preventing accidental drops into the wrong directory.
        
- **Disable Drag and Drop Completely:**
    
    - **Setting:** `explorer.enableDragAndDrop`
        
    - **Behavior:** Set this to `false` if you want to completely disable moving files via drag and drop in the Explorer panel.
        

## 2. Better Alternatives to Drag-and-Drop

If auto-expanding folders are making file organization frustrating, these built-in alternatives offer more control:

- **Cut and Paste (`Ctrl+X` / `Cmd+X`):**
    
    1. Select the file in the Explorer view.
        
    2. Press **`Ctrl+X`** (or **`Cmd+X`** on macOS).
        
    3. Click the target folder.
        
    4. Press **`Ctrl+V`** (or **`Cmd+V`** on macOS).
        
- **Drag via Breadcrumbs or Editor Tabs:**
    
    If the target folder is already open in the editor, you can drag the file straight into its editor tab or into the **Breadcrumb path** at the top of the editor window instead of navigating the Explorer tree.


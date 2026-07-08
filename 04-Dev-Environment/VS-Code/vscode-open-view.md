---
created: 2026-07-07
tags: [dev, vscode]
type: howto
lang: en
status: draft
---

> Related: [[MOC - Dev Environment]] · [[vscode-pretty]]

Yes, you can configure VS Code so that clicking a Markdown file opens the rendered preview immediately rather than the raw text source.

Here are the easiest ways to change this behavior:

## Method 1: The Right-Click Shortcut (Easiest)

1. **Right-click** any `.md` file in your VS Code File Explorer sidebar.
    
2. Select **Open With...** from the context menu.
    
3. Click **Configure default editor for '*.md'...** at the bottom of the popup list.
    
4. Select **Markdown Preview**.
    

## Method 2: Through the Command Palette

1. Open any `.md` file.
    
2. Open the Command Palette using `Ctrl + Shift + P` (or `Cmd + Shift + P` on Mac).
    
3. Type and select **View: Reopen Editor With...**
    
4. Click **Configure default editor for '*.md'...**
    
5. Select **Markdown Preview**.
    

## Method 3: Editting `settings.json` Directly

If you prefer adding it to your global configuration manually, open your `settings.json` file and append this object:

JSON

```
"workbench.editorAssociations": {
    "*.md": "vscode.markdown.preview.editor"
}
```

> 💡 **Pro-Tip: How to edit the file later**
> 
> Once this is enabled, single-clicking any `.md` file will show the finished preview document. When you actually want to make edits to the code:
> 
> - **Double-click** anywhere inside the preview window to quickly pop back into text-editing mode.
>     
> - Alternatively, click the **"Show Source"** bracket icon `{ }` in the top-right tool menu of the open file tab.
>
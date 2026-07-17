---
title: "VS Code Folding in Markdown vs Code Files"
description: "Explains why Markdown folding follows headings or fenced blocks and how details tags or indentation folding can make sections collapsible."
created: 2026-07-16
updated: 2026-07-16
type: howto
lang: en
status: draft
tags: [dev]
---

> Related: [[MOC - Dev Environment]] · [[vscode-tips]] · [[vscode-toggle-view]]

The reason you can't collapse (fold) that section is because you are editing a **Markdown file** (`TODO.md`), which handles folding differently than programming languages like JavaScript, JSON, or Python.

In Markdown files, VS Code's default behavior only allows folding for:

1. **Headers** (like the `#` on line 1).
    
2. **Fenced code blocks** (text wrapped in triple backticks ` ``` `).
    

Because that curly brace `{` on line 5 is just written as plain text in your Markdown document, the editor doesn't recognize it as the start of a foldable block.

### How to make this section collapsible

Depending on what you are trying to achieve, here are the best ways to fix this:

#### Method 1: Use HTML `<details>` tags (Recommended)

If you want a section that is collapsible **both** in the editor and when the Markdown is rendered (like on GitHub or in a preview window), use the HTML `<details>` and `<summary>` tags:

HTML

```
<details>
<summary>Click to expand/collapse</summary>

在 WSL (Linux) 環境下，安裝 Node.js 的**大忌**是...
最完美的標準做法是使用 **NVM**...

</details>
```

#### Method 2: Use Markdown Headers

If you just want to organize your notes, you can use markdown subheadings. VS Code will automatically let you fold everything under a header until it hits another header of the same or higher level:

Markdown

```
# 執行環境 額外注意：Conda 與 NVM 的「搶路徑」衝突

## 在 WSL 下安裝 Node.js
在 WSL (Linux) 環境下，安裝 Node.js 的**大忌**是...
最完美的標準做法是使用 **NVM**...
```

#### Method 3: Force VS Code to fold by indentation (Settings Change)

If you want VS Code to ignore language-specific rules and _always_ let you fold text based on brackets and indentation level, you can change your global settings:

1. Open your VS Code Settings (`Ctrl + ,` or `Cmd + ,`).
    
2. Search for **Folding Strategy**.
    
3. Change it from `auto` to **`indentation`**.
    

_(Note: This will apply to all files, which might change how folding behaves in your other code files as well)._

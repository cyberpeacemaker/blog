---
created: 2026-07-22 11:07
updated: 2026-07-22 11:07
tags: []
type: reference
lang: en
status: draft
---
**No**, the VS Code Command Palette does not have traditional "inline text autocomplete" (like pressing `Tab` to fill in the rest of a word like in a terminal shell or code editor).

Instead, it relies on **Fuzzy Search Filtering**.

## How It Works Instead

Rather than completing your typed text, the Command Palette actively filters a dropdown list in real-time based on what you type:

- **Fuzzy Matching:** As shown in your screenshot, typing `>dev` highlights matching letters across all available commands (the bold blue letters).
    
- **Non-contiguous Search:** You don't need to type words in full or even in exact order. For example, typing `dev clone` or even `dc vol` will instantly jump to **`Dev Containers: Clone Repository in Container Volume`**.
    
- **Navigation:** You use the **`Up` / `Down` arrow keys** (or `Ctrl + N` / `Ctrl + P`) to highlight the command you want, then press **`Enter`** to run it.
    

## Quick Shortcuts for Speed

|**Action**|**Shortcut**|
|---|---|
|**Open Command Palette**|`Ctrl + Shift + P` (Win/Linux) / `Cmd + Shift + P` (Mac)|
|**Move down the list**|`Down Arrow` or `Ctrl + N`|
|**Move up the list**|`Up Arrow` or `Ctrl + P`|
|**Execute highlighted command**|`Enter`|

> **Pro-tip:** You rarely need to type full category names like `Dev Containers:`. Just type a few letters of each word you want—like `dev repo`—and press `Enter` as soon as it jumps to the top of the list!


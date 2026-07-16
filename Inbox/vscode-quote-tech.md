---
created: 2026-07-16 20:07
updated: 2026-07-16 20:07
tags: []
type: reference
lang: en
status: draft
---
Heck no! Please do not do that manually—100 lines would drive anyone crazy.

VS Code has some incredible built-in features that can do this for you in about three seconds. Here are the three best ways to do it, ranging from a clever search trick to keyboard shortcuts.

## Method 1: The Regex Find & Replace Trick 🪄 (The Safest & Easiest)

This is the absolute best way because it handles empty lines within your 100-line block perfectly.

1. **Highlight/Select** the 100+ lines you want to quote.
    
2. Press **`Ctrl + H`** (Windows) or **`Cmd + Option + F`** (Mac) to open the Find and Replace panel.
    
3. Make sure **two specific buttons** are toggled **ON** in the search box (they will light up blue):
    
    - **Use Regular Expression** (looks like `.*` — shortcut: `Alt + R` / `Cmd + Option + R`)
        
    - **Find in Selection** (looks like a highlighted square of text — shortcut: `Alt + L` / `Cmd + Option + L`)
        
4. In the **Find** field, type: `^` _(This is a regex symbol that means "the beginning of the line")_
    
5. In the **Replace** field, type: `>` _(Make sure to put a space after the `>`!)_
    
6. Click the **Replace All** button on the right (or press `Ctrl + Alt + Enter` / `Cmd + Option + Enter`).
    

Boom! Instantly, every line in that highlighted block has a `>` at the beginning.

## Method 2: The Multi-Cursor Power Move ⚡ (The Fastest)

If you prefer keyboard shortcuts over clicking search boxes, you can use VS Code's multi-cursor feature.

1. **Highlight/Select** your 100+ lines.
    
2. Press **`Shift + Alt + I`** (Windows) or **`Option + Shift + I`** (Mac).
    
    - _This places an active typing cursor at the end of every single line you highlighted._
        
3. Press the **`Home`** key (Windows) or **`Cmd + Left Arrow`** (Mac).
    
    - _This instantly teleports all 100+ cursors to the very start of their lines._
        
4. Type **`>`** (greater-than and a space).
    
5. Press **`Esc`** to exit multi-cursor mode.
    

> ⚠️ **Note:** If your text block has completely blank lines with zero characters on them, this method might skip those empty lines. If you want those empty lines to have a `>` too, stick to **Method 1**.

## Method 3: Use an Extension 🔌 (For Frequent Quoting)

If you have to do this daily and want a dedicated keyboard shortcut, you can install a helper:

1. Open the Extensions tab (`Ctrl + Shift + X` / `Cmd + Shift + X`).
    
2. Search for and install **`vscode-markdown-quote`**.
    
3. Highlight your text block and run the toggle quote command (which you can bind to a custom shortcut like `Alt + .`) to wrap and unwrap blockquotes instantly.


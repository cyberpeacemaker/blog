---
created: 2026-07-13 15:07
updated: 2026-07-13 15:07
tags: []
type: reference
lang: en
status: draft
---
Ah, the classic Vim permission wall.

The error `E45: 'readonly' option is set` means you're trying to modify a system file (looks like `/etc/gai.conf` for prioritizing IPv4/IPv6) without root (`sudo`) privileges.

Here are the three easiest ways to fix this, depending on what you want to do:

### Fix 1: The Vim "Magic" Trick (Save without exiting)

If you already made a bunch of changes and don't want to lose them by quitting, you can force Vim to save using `sudo` right now.

1. Press `Esc` to make sure you're in normal mode.
    
2. Type the following command exactly and press `Enter`:
    
    Vim Script
    
    ```
    :w !sudo tee %
    ```
    
3. Type your WSL user password if prompted.
    
4. Press `L` (or Enter) when Vim asks you to load/refresh the changes.
    
5. You can now quit safely by typing `:q!`.
    

### Fix 2: The VS Code UI Way (Highly Recommended)

Since you're already in VS Code, you don't actually have to use Vim in the terminal! You can open the file directly in the VS Code editor window, which handles permission prompts beautifully.

1. Exit your current Vim session by typing `Esc` then `:q!`.
    
2. Open the file in VS Code by typing:
    
    Bash
    
    ```
    code /etc/gai.conf
    ```
    
3. Make your edits in the nice VS Code editor text window.
    
4. Hit `Ctrl + S` to save. VS Code will pop up a notification saying you don't have permission and will offer a **"Retry as Sudo..."** button. Click it, type your password, and you're done!
    

### Fix 3: The Standard Terminal Way

If you prefer staying inside the terminal Vim interface, just quit and reopen it with root permissions:

1. Exit Vim: `Esc` then `:q!`.
    
2. Reopen the file with `sudo`:
    
    Bash
    
    ```
    sudo vim /etc/gai.conf
    ```
    
3. Make your changes and save normally with `:wq`.


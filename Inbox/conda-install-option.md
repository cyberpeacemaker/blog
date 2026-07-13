---
created: 2026-07-13 15:07
updated: 2026-07-13 15:07
tags: []
type: reference
lang: en
status: draft
---
For most users, typing **`yes`** is the best and easiest choice. Here is a quick breakdown to help you decide what to do next:

### Option 1: Type `yes` (Recommended)

This will automatically configure your shell profile (like `.bashrc` or `.zshrc`) so your computer knows where Conda lives.

- **The Good:** You can immediately start using `conda` commands whenever you open a new terminal window.
    
- **The Catch:** Every time you open a terminal, it will automatically activate the default `base` environment, adding `(base)` to your command prompt.
    

> 💡 **Pro-Tip:** If you choose `yes` but hate seeing `(base)` on your terminal startup, you can easily turn that part off while keeping Conda accessible. Once the installer finishes, open a new terminal and run:
> 
> `conda config --set auto_activate_base false`

### Option 2: Type `no` (or just press Enter)

This leaves your terminal configuration completely untouched.

- **The Good:** Your terminal startup remains clean, fast, and unaffected.
    
- **The Catch:** The `conda` command won't work out of the box when you open a new terminal. You will have to manually navigate to or source the installation path every time you want to use it, or manually run `conda init` later down the road.
    

### Recommendation

If you just want things to "just work" without dealing with manual path configurations later, type **`yes`** and hit **Enter**.

Are you setting this up for a specific development workflow, or just getting started with Python data science?


---
created: 2026-05-21
tags: [dev]
type: reference
lang: en
status: draft
---

## 1. The `[200~` and `~` Mystery: Bracketed Paste Mode

Those strange characters are part of a terminal feature called **Bracketed Paste Mode**.

When you paste text into a modern terminal, the terminal wraps your text in hidden "brackets" (ANSI escape codes) so the shell knows the text is a single pasted block, rather than you typing at light speed.

* **`\e[200~`** tells the terminal: *"A paste is starting!"*
* **`\e[201~`** tells the terminal: *"The paste is finished!"*

### Why it failed:

Sometimes, when pasting complex multi-line blocks or interacting with specific setups (like throwing a Python Heredoc into Git Bash), the shell gets confused. It fails to strip away those hidden brackets, leaving behind the literal text **`[200~`** at the front and a truncated **`~`** (from the `201~`) at the end. Because those characters became part of your code, Python threw a fit.

---

## 2. The Slash (`/`) Drama: Windows vs. Bash

In your original screenshot, the path looked like this: `c:\Users\ydnaa\Documents...`

Git Bash is a Unix-based environment running on Windows. It treats characters differently than a standard Windows command prompt:

* **The Escape Character:** In Bash, the backslash (`\`) is an "escape character" used to give special meaning to the next character (like `\n` for a new line).
* **The Glitch:** When Bash read `\y`, `\D`, and `\G` from your Windows path, it didn't see them as folder dividers. It thought you were trying to escape those letters, which completely broke the directory path.

### Why your fix worked:

By switching to forward slashes (`/`) or doubling up the backslashes (`\\`), you told Git Bash: *"Hey, ignore the escape rule, this is an actual file path."*

---

### Pro-Tip for next time

If you ever want to completely disable Bracketed Paste Mode in Git Bash to prevent those `~` characters from appearing again, you can run this command in your terminal:

```bash
echo "set enable-bracketed-paste off" >> ~/.inputrc

```

*(You will just need to restart Git Bash for it to take effect!)*
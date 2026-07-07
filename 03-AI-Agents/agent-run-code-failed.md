---
created: 2026-05-21
tags: [ai, agents]
type: reference
lang: en
status: draft
---

### 1. The Backslash Escaping Glitch (Most Likely)

When you paste a path like `C:\Users\ydnaa\.copilot\session-state\2adbc...` directly into your terminal, Windows knows exactly what to do with those backslashes (`\`).

However, VS Code agents don't type directly into the terminal like a human. They pass commands as text strings through JSON payloads and API wrappers. In almost all programming environments (like the JavaScript/TypeScript running VS Code extensions), a single backslash is an **escape character**.

* The agent tried to pass `\2adbc...`
* The underlying code likely interpreted `\2` as an octal escape sequence or a broken character code, completely mangling the file path before it ever reached the shell.

### 2. `pwsh` vs. `powershell` Environments

If you look closely at the screenshot:

* The agent's prompt button says: **`Run pwsh command?`** (PowerShell Core 7+)
* Your manual terminal at the bottom says: **`powershell`** (Windows PowerShell 5.1)

When extensions spawn a background `pwsh` instance, it often runs in a non-interactive, isolated environment. This background session sometimes lacks the specific user permissions required to access hidden configuration folders like `AppData` or `.copilot`, resulting in a silent access denial.

### 3. File Locking by the Copilot Extension

The source file was located inside `\.copilot\session-state\`. This is a temporary directory managed actively by the extension. It is highly possible that while the agent was processing your prompt, the Copilot extension still had an exclusive "file lock" on that markdown file, preventing the agent's background shell tool from reading or copying it.

---

### Why the Pivot to Python Saved the Day

This is exactly why the agent pivoted to Python (`import shutil, os`).

Python handles file system paths using raw string literals or built-in path utilities that abstract away all the messy shell-escaping and platform-specific quirks. By switching to Python, the agent bypassed the broken terminal bridge entirely and talked directly to your operating system's file manager.
---
title: "Close a VS Code Python HTTP Server"
description: "Explains why VS Code usually terminates integrated-terminal servers and why Ctrl+C is the cleaner shutdown path."
created: 2026-07-16
updated: 2026-07-16
type: howto
lang: en
status: draft
tags: [dev, python]
---

> Related: [[MOC - Dev Environment]] · [[vscode-tips]] · [[python-venv]]

The short answer is: **Closing VS Code will automatically close the Python HTTP server.**

Because the server is running inside VS Code’s integrated terminal, it operates as a child process of the editor. When you exit VS Code, it terminates the terminal shell, which automatically kills any running processes inside it (like your Python server).

### The "But..." (Why you should still close it manually)

While VS Code does a great job of cleaning up after itself, **it is still best practice to stop the server manually** before closing the editor.

Occasionally, if you abruptly close VS Code, the operating system might not release the network port (port `8000`) immediately. When you reopen VS Code and try to run the server again, you might run into a frustrating error:

> `OSError: [Errno 98] Address already in use` (or `An attempt was made to access a socket in a way forbidden by its access permissions`)

### How to shut it down cleanly in 2 seconds

You have two incredibly easy ways to close it properly before exiting:

1. **The Keyboard Shortcut (Recommended):**
    
    Click anywhere inside the terminal window to focus it, and press **`Ctrl + C`**. This gracefully stops the Python server and returns you to the normal command prompt.
    
2. **The Trash Can Icon:**
    
    Click the **Trash Can icon (`🗑️`)** in the top-right corner of the terminal panel (right next to the split terminal icons in your screenshot). This instantly kills the active terminal instance and the server with it.

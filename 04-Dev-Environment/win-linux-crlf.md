---
title: "Windows vs Linux CRLF Line Endings"
description: "Shows why CRLF line endings break Bash scripts on Linux and how to convert shell files to LF."
created: 2026-07-13
updated: 2026-07-13
type: howto
lang: en
status: draft
tags: [dev, windows, bash]
---

> Related: [[MOC - Dev Environment]] · [[git-bash]] · [[vscode-open-view]]

Ah, the classic Windows vs. Linux line-endings trap! That scrambled error message (`: invalid option nameooks.sh...`) is the ultimate smoking gun here.

  

### What is happening?

  

Windows saves text files with **CRLF** line endings (Carriage Return `\r` + Line Feed `\n`), while Linux/Bash expects just **LF** (`\n`).

  

On line 12 of your script, Bash is reading `set -o pipefail\r`. It thinks the option name is literally `pipefail\r`. Because `\r` means "move the cursor back to the start of the line," the error message prints over itself, turning `scripts/install-git-hooks.sh` into `ooks.sh`.

  

Here is how to fix it right now, and how to stop it from happening again.

  

---

  

## How to Fix It Right Now

  

### Option 1: The VS Code / IDE Quick Fix (Easiest)

  

1. Open `scripts/install-git-hooks.sh` in **VS Code**.

2. Look at the very bottom-right corner of the window status bar. You will see **CRLF**.

3. Click **CRLF** and change it to **LF**.

4. Save the file and run your command again.

  

### Option 2: Fix it from your Terminal

  

Since you have `bash` available, you can use `sed` to strip out the hidden Windows carriage returns. Run this command in your PowerShell terminal:

  

```powershell

bash -c "sed -i 's/\r$//' scripts/install-git-hooks.sh"

  

```

  

---

  

## How to Prevent This permanently (For Your Repository)

  

Since you are developing a project (`otex-claw`) that other people might use on Windows, you should force Git to always handle `.sh` files with Linux line endings.

  

Create a file named `.gitattributes` in the root of your repository (if you don't already have one) and add this line:

  

```text

*.sh text eol=lf

  

```

  

### Why do this?

  

This tells Git: *"No matter if someone clones or edits this project on Windows, Mac, or Linux, always force shell scripts to use LF line endings."* Once you commit this file, nobody on your team will ever hit this weird error again.


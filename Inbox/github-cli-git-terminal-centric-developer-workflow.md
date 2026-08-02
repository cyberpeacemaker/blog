---
created: 2026-08-02 15:08
updated: 2026-08-02 15:08
tags: []
type: reference
lang: en
status: draft
---
If you prefer a terminal-centric, developer workflow, you can bypass interactive browser flows entirely.

Here are the **three most efficient ways** to set up GitHub CLI and Git authentication on headless or SSH-connected Linux machines, ranked from best to fastest.

### 1. The Gold Standard: SSH Keys (Zero-Friction Git Ops)

Once configured, SSH keys let you `git push`, `git pull`, and `gh repo clone` seamlessly forever without ever typing a password, token, or code.

1. **Generate an SSH key** in your terminal:
    
    Bash
    
    ```
    ssh-keygen -t ed25519 -C "your_email@example.com" -N "" -f ~/.ssh/id_ed25519
    ```
    
2. **Tell `gh` CLI to use SSH as your default protocol:**
    
    Bash
    
    ```
    gh config set git_protocol ssh
    ```
    
3. **Upload the key to GitHub** (if logged in with a token) or add it manually via GitHub Settings:
    
    Bash
    
    ```
    gh ssh-key add ~/.ssh/id_ed25519.pub --title "Lab-Laptop"
    ```
    

Now you can clone directly via SSH with zero prompts:

Bash

```
gh repo clone nagameTW/otex-claw ~/deploy/otex-claw
```

### 2. The Automation Way: `GH_TOKEN` Environment Variable

If you don't want to run `gh auth login` at all, GitHub CLI automatically checks for a `GH_TOKEN` variable in your environment.

1. Generate a **Personal Access Token (classic)** with `repo` scope on GitHub.
    
2. Add it to your shell configuration (`~/.bashrc` or `~/.zshrc`):
    
    Bash
    
    ```
    echo 'export GH_TOKEN="ghp_your_actual_token_here"' >> ~/.bashrc
    source ~/.bashrc
    ```
    
3. Test it: `gh auth status` will immediately show you as logged in across all future terminal sessions.
    

### 3. Fix Browser Auto-Opening on WSL (If using Windows Subsystem for Linux)

If your terminal (`26036-LABNB01`) is a WSL environment and you _do_ want `gh` to automatically open your Windows browser when needed:

1. Install `wslu` (WSL Utilities):
    
    Bash
    
    ```
    sudo apt update && sudo apt install -y wslu
    ```
    
2. Set `wslview` as your default browser provider:
    
    Bash
    
    ```
    sudo update-alternatives --config xdg-open
    ```
    

_(Select `wslview` from the list. Next time `gh` wants to open a browser, it will launch Chrome/Edge seamlessly in Windows)._

### Summary Comparison

|**Method**|**Setup Effort**|**Daily Friction**|**Best Used For**|
|---|---|---|---|
|**SSH Keys**|2 minutes|**Zero**|Primary development machine|
|**`GH_TOKEN`**|1 minute|**Zero**|Remote servers, Docker containers, CI/CD|
|**WSL Browser Fix**|1 minute|Low (1-click)|Standard interactive usage in WSL|

Are you working inside WSL (Windows Subsystem for Linux) or a remote SSH server so I can help you dial in the exact setup for your environment?


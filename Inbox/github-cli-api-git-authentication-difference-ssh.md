---
created: 2026-08-02 15:08
updated: 2026-08-02 15:08
tags: []
type: reference
lang: en
status: draft
---
This is a very common point of confusion!

The reason `gh auth` doesn't show you as logged in is because **Git** and the **`gh` CLI** use two completely different authentication channels:

- **SSH Key = Git Authentication:** Authenticates raw Git operations (code transfer via `git@github.com`) to push and pull code.
    
- **`gh auth` = GitHub API Authentication:** Authenticates the command-line tool (talking to `api.github.com`) to manage repos, pull requests, issues, and CLI features.
    

Adding an SSH key to GitHub gives **Git** access, but it doesn't grant the **`gh` CLI** permission to talk to the API.

### How to Fix It & Connect Both

#### Step 1: Verify your SSH key works for Git

Run this test in your WSL Ubuntu terminal:

Bash

```
ssh -T git@github.com
```

> **Expected Output:** `Hi <username>! You've successfully authenticated, but GitHub does not provide shell access.`

If you see that, your SSH key is working perfectly for standard Git commands (like `git clone git@github.com:nagameTW/otex-claw.git`).

#### Step 2: Log into `gh` CLI using your SSH preference

To get `gh` logged in while telling it to use your SSH key for repo cloning:

1. Create a **Personal Access Token (classic)** on GitHub (_Settings $\rightarrow$ Developer Settings $\rightarrow$ Personal Access Tokens_) with the `repo` scope.
    
2. In WSL, run:
    
    Bash
    
    ```
    gh auth login
    ```
    
3. Answer the prompts like this:
    
    - **What account do you want to log into?** `GitHub.com`
        
    - **What is your preferred protocol for Git operations?** `SSH`
        
    - **Select an SSH key to upload...** Choose **`Skip`** (since you already added it to GitHub manually).
        
    - **How would you like to authenticate GitHub CLI?** `Paste an authentication token`
        
4. Paste your token and press Enter.
    

#### Step 3: Test cloning with `gh`

Now `gh` will use your API token for commands and your SSH key for all git operations:

Bash

```
gh repo clone nagameTW/otex-claw ~/deploy/otex-claw
```

When you run `ssh -T git@github.com` in your WSL terminal, does it greet you with your GitHub username?


---
created: 2026-07-22 10:07
updated: 2026-07-22 10:07
tags: []
type: reference
lang: en
status: draft
---
Yes, you can absolutely wire WSL Ubuntu to use the **Windows Git Credential Manager (GCM)**!

When `git ls-remote` hangs, it’s usually because Git is silently waiting for user input or authentication that it can't prompt for in a non-interactive shell. Wiring WSL to Windows GCM allows WSL (and Dev Containers) to leverage Windows' GUI popups for authentication and share saved credentials seamlessly.

Here is how to fix it step-by-step:

## Step 1: Wire WSL Ubuntu to Windows GCM

Open your **WSL Ubuntu terminal** and run the following command to set your global Git credential helper to the Windows GCM executable:

Bash

```
git config --global credential.helper "/mnt/c/Program\ Files/Git/mingw64/bin/git-credential-manager.exe"
```

> **Note:** If you are using a newer version of Git for Windows where that path doesn't exist, try this alternative path:
> 
> Bash
> 
> ```
> git config --global credential.helper "/mnt/c/Program\ Files/Git/mingw64/libexec/git-core/git-credential-manager.exe"
> ```

## Step 2: Verify the Connection in WSL

Test that the connection works by running `git ls-remote` directly in your WSL terminal against your target repository:

Bash

```
git ls-remote https://github.com/your-org/your-repo.git
```

- **What should happen:** A Windows GUI dialog or browser window will pop up asking you to sign in.
    
- Once you log in, Git will store the token securely in **Windows Credential Manager**. Future runs won't prompt you or hang.
    

## Step 3: Ensure VS Code Passes Credentials to Dev Containers

VS Code automatically copies your host’s `~/.gitconfig` and forwards credentials into Dev Containers when launching them.

1. Open **VS Code Settings** (`Ctrl + ,`).
    
2. Search for `dev.containers.copyGitConfig`.
    
3. Make sure **Dev > Containers: Copy Git Config** is **checked** (`true`).
    
4. Rebuild or reopen your workspace in the container (**F1** $\rightarrow$ **Dev Containers: Rebuild Container**).
    

## Alternative: If using SSH instead of HTTPS

If your remote URL uses SSH (e.g., `git@github.com:user/repo.git`), GCM won't be triggered. SSH hangs when no SSH agent is active to supply your key passphrase.

To fix SSH hanging:

1. Start the SSH agent in WSL Ubuntu and add your key:
    
    Bash
    
    ```
    eval "$(ssh-agent -s)"
    ssh-add ~/.ssh/id_ed25519   # replace with your SSH key filename
    ```
    
2. VS Code will automatically forward this running SSH agent into your Dev Container.


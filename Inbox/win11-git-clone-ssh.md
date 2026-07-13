---
created: 2026-07-13 16:07
updated: 2026-07-13 16:07
tags: []
type: reference
lang: en
status: draft
---
Ah, the classic SSH handshake denial. This error means GitHub is looking for an SSH key to verify who you are, but your computer either hasn't generated one, or GitHub doesn't know about it yet.

You have two ways to fix this: **Option A** (Fixing the SSH setup) or **Option B** (The quick workaround using HTTPS).

## Option A: Set Up Your SSH Key (Recommended)

If you plan to push and pull code frequently from this computer, taking a couple of minutes to set up your SSH key is worth it.

### 1. Check for existing keys

Run this command in PowerShell to see if you already have an SSH key:

PowerShell

```
ls ~/.ssh
```

- If you see files like `id_ed25519` and `id_ed25519.pub`, skip to **Step 3**.
    
- If it says the path doesn't exist, move to **Step 2**.
    

### 2. Generate a new SSH key

Run the following command (replace the email with your GitHub email):

PowerShell

```
ssh-keygen -t ed25519 -C "your_email@example.com"
```

Press **Enter** to accept the default file location, and press **Enter** twice more to skip setting a passphrase (unless you want one).

### 3. Add your key to GitHub

First, copy your public key to your clipboard:

PowerShell

```
cat ~/.ssh/id_ed25519.pub | clip
```

_(If you used an older RSA key in step 1, change `id_ed25519.pub` to `id_rsa.pub`)_

Next, add it to your profile:

1. Go to **GitHub** and log in.
    
2. Click your profile picture in the top-right corner $\rightarrow$ **Settings**.
    
3. In the left sidebar, click **SSH and GPG keys**.
    
4. Click the green **New SSH key** button.
    
5. Give it a title (like "My Windows Laptop") and **paste** your key into the "Key" field.
    
6. Click **Add SSH key**.
    

### 4. Test it and Clone again

Verify everything works by running:

PowerShell

```
ssh -T git@github.com
```

If it asks if you want to continue connecting, type `yes`. You should see a message like: _"Hi username! You've successfully authenticated..."_

Now you can run your original clone command:

PowerShell

```
git clone git@github.com:nagameTW/otex-claw.git
```

## Option B: Use HTTPS instead (The Quick Fix)

If you are in a rush and just want to download the repository without dealing with SSH keys, you can clone using the HTTPS URL instead.

Run this command in PowerShell:

PowerShell

```
git clone https://github.com/nagameTW/otex-claw.git
```

_(Note: If the repository is private, Windows will prompt you to log in via a browser window to authenticate)._

---

Windows 11 is perfect for this! You're already using PowerShell (indicated by that `PS` at the start of your path), which means those commands will work right out of the box.

Windows 11 actually has the OpenSSH client built-in by default, so you don't need to install anything extra.

The only small tweak for Windows 11 to make your life easier is using the native PowerShell command to copy your key. When you get to **Step 3**, use this command instead:

PowerShell

```
Get-Content ~/.ssh/id_ed25519.pub | Set-Clipboard
```

This ensures Windows 11 copies the text perfectly to your clipboard without adding any weird hidden formatting characters.

Other than that, the steps are exactly the same. Are you stuck on a specific step of the generation process, or did you want to try the HTTPS workaround?
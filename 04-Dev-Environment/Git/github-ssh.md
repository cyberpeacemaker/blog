---
title: "GitHub SSH Setup on Windows PowerShell"
description: "Walks through generating an SSH key, enabling ssh-agent, adding the key to GitHub, and testing authentication."
created: 2026-07-09
updated: 2026-07-09
type: howto
lang: en
status: draft
tags: [dev, git]
---

> Related: [[MOC - Dev Environment]] · [[github-authentication]] · [[github-private-clone]]
Windows 11 makes this pretty easy since it has OpenSSH built right in, but there is one classic Windows quirk we need to handle: the **SSH Agent service** is usually turned off by default.

Since it's a private repository, once you finish these steps, GitHub will know exactly who you are and let you right in (provided your GitHub account has been granted collaborator access to that repo!).

Here is the exact step-by-step for Windows 11 PowerShell:

### Step 1: Generate the SSH Key

Open your PowerShell and run the following command. Just press **Enter** through all the prompts to keep it simple (no need to type a passphrase unless you want to):

PowerShell

```
ssh-keygen -t ed25519 -C "your_github_email@example.com"
```

_(Replace with the email you actually use for GitHub)._

### Step 2: Enable the Windows SSH Service

Windows 11 tends to keep the SSH helper service disabled. Let's turn it on so your system remembers your key:

PowerShell

```
# 1. Set the service to start automatically
Set-Service -Name ssh-agent -StartupType Automatic

# 2. Start the service
Start-Service ssh-agent

# 3. Feed your new key to the service
ssh-add ~/.ssh/id_ed25519
```

### Step 3: Copy the Key to GitHub

Run this command to copy your new public key straight to your Windows clipboard:

PowerShell

```
Get-Content ~/.ssh/id_ed25519.pub | clip
```

Now, head over to GitHub in your browser:

1. Click your profile picture (top right) -> **Settings**.
    
2. Click **SSH and GPG keys** in the left menu.
    
3. Click **New SSH key**.
    
4. Give it a title (like "Win11 Desktop") and **paste** the key into the big box.
    
5. Click **Add SSH key**.
    

### Step 4: Test and Clone!

Before cloning, let's make sure GitHub recognizes you. Run this in PowerShell:

PowerShell

```
ssh -T git@github.com
```

> **Note:** It will say something like `"The authenticity of host... can't be established."` Type **`yes`** and hit Enter.

If it replies with _"Hi [YourUsername]! You've successfully authenticated..."_, you are golden. Go ahead and run your clone command again:

PowerShell

```
git clone git@github.com:nagameTW/otex-claw.git
```

Did you get the success message from the test command, or did Windows throw an error on one of the service steps?

---

Perfect! You are right on track. Looking at `image_906647.png`, the system is just asking where you want to save this new key file.

Here is exactly what you need to do right now on your keyboard:

1. **Press Enter** to accept the default location shown in the parentheses.
    
2. The terminal will then say: `Enter passphrase (empty for no passphrase):`. **Press Enter again** to leave it blank.
    
3. It will then say: `Enter same passphrase again:`. **Press Enter one last time**.
    

Once you've hit Enter those three times, you'll see a little square box made of random text characters (called a randomart image). That means your key is officially created!

### What to do right after that:

Once the key is created, run these three commands in that same PowerShell window to turn on the Windows SSH helper and load your new key:

PowerShell

```
Set-Service -Name ssh-agent -StartupType Automatic
Start-Service ssh-agent
ssh-add ~/.ssh/id_ed25519
```

Let me know once you've done that, and we'll copy it over to GitHub!

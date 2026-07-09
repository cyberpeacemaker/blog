---
created: 2026-07-09 19:07
updated: 2026-07-09 19:07
tags: []
type: reference
lang: en
status: draft
---
Ah, the classic SSH handshake fail. It's super common to run into this!

Here is what’s going on: seeing the repository in your browser just means the repository is either public or you're logged into your GitHub account on Chrome/Edge. However, your **PowerShell terminal** doesn't use your browser's login session. Because you used the SSH URL (`git@github.com:...`), GitHub is looking for a digital security badge (an SSH key) from your computer, and it isn't finding one it recognizes.

You have two ways to fix this.

### Method 1: The Quick Fix (Switch to HTTPS)

If the repository is public, you don't need to mess with SSH keys at all. You can clone it right now using the HTTPS URL instead.

Run this command in PowerShell:

PowerShell

```
git clone https://github.com/nagameTW/otex-claw.git
```

_Note: If the repo is private, Windows will likely pop up a quick window asking you to sign into your GitHub account via Git Credential Manager, and then it will clone perfectly._

### Method 2: The Permanent Fix (Set up your SSH Key)

If you specifically _want_ to use SSH so you don't have to deal with login prompts in the future, you need to give GitHub your computer's public key.

Here is how to do it in PowerShell:

**1. Check if you already have a key**

PowerShell

```
ls ~/.ssh
```

If you see files like `id_ed25519` and `id_ed25519.pub`, you have one! Skip to step 3. If it says the path doesn't exist, move to step 2.

**2. Generate a new SSH key**

Press Enter to accept all the default prompts (you don't need to type a passphrase unless you want extra security):

PowerShell

```
ssh-keygen -t ed25519 -C "your_email@example.com"
```

**3. Copy the key to your clipboard**

Run this to copy your public key:

PowerShell

```
Get-Content ~/.ssh/id_ed25519.pub | clip
```

**4. Add it to GitHub**

1. Go to GitHub.com and click your profile picture in the top right -> **Settings**.
    
2. On the left sidebar, click **SSH and GPG keys**.
    
3. Click the green **New SSH key** button.
    
4. Give it a title (like "My Windows Laptop") and **paste** your key into the big "Key" box.
    
5. Click **Add SSH key**.
    

Once that's done, go back to your PowerShell window and try your original command again:

PowerShell

```
git clone git@github.com:nagameTW/otex-claw.git
```

_(It might ask you if you trust github.com; just type `yes` and hit Enter)._

---

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
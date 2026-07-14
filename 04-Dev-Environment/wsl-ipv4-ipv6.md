---
title: "WSL IPv4 Preference and IPv6 Troubleshooting"
description: "Shows how to prefer IPv4 in WSL when IPv6 routing causes curl and package-manager timeouts."
created: 2026-07-13
updated: 2026-07-13
type: howto
lang: en
status: draft
tags: [dev, windows, wsl, networking]
---

> Related: [[MOC - Dev Environment]] · [[wsl-network-troubleshooting]] · [[vim-permission]]

Since `curl -4` resolved the issue instantly, your WSL environment is running into a common snag: it resolves internet addresses to IPv6, but your host network or ISP isn't routing IPv6 traffic out properly, causing the connection to time out.

Here are the two best ways to fix this permanently.

### Method 1: The "Prefer IPv4" Fix (Highly Recommended)

Instead of ripping out IPv6 entirely—which can sometimes upset internal WSL tools or Docker containers—you can simply tell Linux, _"Hey, look up IPv4 first, and only use IPv6 as a backup."_

This requires editing a single configuration file inside your WSL terminal:

1. Open the system's address configuration file using `nano`:
    
    Bash
    
    ```
    sudo nano /etc/gai.conf
    ```
    
2. Scroll down until you find the following line (it's usually around line 54):
    
    Plaintext
    
    ```
    #precedence ::ffff:0:0/96  100
    ```
    
3. **Uncomment it** by deleting the `#` symbol at the very beginning so it looks like this:
    
    Plaintext
    
    ```
    precedence ::ffff:0:0/96  100
    ```
    
4. Save and exit (`Ctrl + O`, then `Enter` to save, and `Ctrl + X` to exit).
    

**Why this rules:** The change is instant. You don't even need to restart WSL. Try running your normal `curl [www.google.com](https://www.google.com)` right now, and it should connect immediately.

### Method 2: The "Turn off IPv6" Fix (The Nuclear Option)

If Method 1 doesn't work for some reason, or you just want IPv6 completely disabled at the kernel level for all your WSL distros, you can do it from the Windows side.

1. Open Windows File Explorer and navigate to your user folder: `C:\Users\<YourWindowsUsername>\`
    
2. Look for a file named `.wslconfig`. If it doesn't exist, create a new text file and name it exactly `.wslconfig` (make sure it doesn't end in `.txt`).
    
3. Open it in Notepad and add these lines:
    
    Ini, TOML
    
    ```
    [wsl2]
    kernelCommandLine=ipv6.disable=1
    ```
    
4. Save the file.
    
5. To apply the change, you must completely restart the WSL sub-system. Open a standard **Windows PowerShell** window and run:
    
    PowerShell
    
    ```
    wsl --shutdown
    ```
    
6. Re-open your WSL terminal. If you run `ip -6 addr show`, it should return absolutely nothing, meaning IPv6 is dead and gone, forcing everything onto IPv4.
    

Give Method 1 a shot first—it's usually the cleanest fix for Conda/WSL environments. Did `gai.conf` get your standard `curl` working without needing the `-4` flag?

---

Here is the one-liner command to automate the change, along with a quick verification check.

Copy and paste this block into your WSL terminal:

Bash

```
# 1. Automatically uncomment the IPv4 preference line
sudo sed -i 's/#precedence ::ffff:0:0\/96  100/precedence ::ffff:0:0\/96  100/' /etc/gai.conf

# 2. Verify the change (should print the line WITHOUT a '#' symbol)
grep "precedence ::ffff:0:0/96" /etc/gai.conf

# 3. Test your connection
curl www.google.com
```


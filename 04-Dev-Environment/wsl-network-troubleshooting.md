---
title: "WSL Network Troubleshooting"
description: "Collects WSL2 network fixes for DNS, IPv6, mirrored networking, MTU, firewall, and proxy failures."
created: 2026-07-13
updated: 2026-07-13
type: howto
lang: en
status: draft
tags: [dev, windows, wsl, networking]
---

> Related: [[MOC - Dev Environment]] · [[wsl-ipv4-ipv6]] · [[wsl-network-issue-antivirus-possible]]

Ah, the classic WSL2 networking black hole.

Looking at your terminal output, your **DNS is working perfectly**—it successfully resolved `[www.google.com](https://www.google.com)` to its IPv4 addresses. However, the actual TCP handshake (`Trying 142.251...`) is hanging until you're forced to Ctrl+C out of it.

This usually happens because WSL2 runs inside a lightweight utility VM with its own virtual network adapter (NAT mode), which frequently runs into issues with **Windows Firewall, corporate VPNs, or MTU size mismatches**.

Here are the most effective ways to fix this, ranked from the easiest modern solution to standard workarounds.

### Fix 1: Switch to "Mirrored" Networking (Highly Recommended)

If you are on a modern version of Windows 11, Microsoft introduced a feature that allows WSL to mirror your Windows host's network architecture exactly. This bypasses the virtual NAT entirely and fixes almost all VPN/firewall issues.

1. In Windows, open your user profile folder (Press `Win + R`, type `%USERPROFILE%`, and hit Enter).
    
2. Create a file named `.wslconfig` (if it doesn't already exist).
    
3. Open it in a text editor and add the following lines:
    
    Ini, TOML
    
    ```
    [wsl2]
    networkingMode=mirrored
    ```
    
4. Save the file.
    
5. Open a Windows PowerShell or Command Prompt window and restart WSL to apply changes:
    
    DOS
    
    ```
    wsl --shutdown
    ```
    
6. Fire up your Kali WSL instance and try the `curl` command again.
    

### Fix 2: Lower the MTU (Maximum Transmission Unit) Size

If you are using a VPN (the `LABNB01` in your hostname suggests a lab or corporate notebook), the VPN might be dropping packets because WSL's default packet size (MTU 1500) is too large.

Inside your WSL terminal, temporarily lower the MTU to see if it fixes the issue:

Bash

```
sudo ip link set dev eth0 mtu 1350
```

_(Note: If your interface isn't named `eth0`, run `ip address` to find the correct name)._

If this fixes the `curl` command, you can make it permanent by adding `sudo ip link set dev eth0 mtu 1350` to your `~/.bashrc` or `~/.zshrc` file.

### Fix 3: The Windows Firewall Bypass

Sometimes Windows Defender Firewall decides WSL traffic is suspicious. You can quickly test if this is the culprit by running this command in **Windows PowerShell as Administrator**:

PowerShell

```
New-NetFirewallRule -DisplayName "WSL" -Direction Inbound -InterfaceAlias "vEthernet (WSL)*" -Action Allow
```

Are you currently connected to a corporate VPN or proxy on this laptop?


---

Ah, the classic WSL2 paradox: **DNS resolves perfectly, Ping responds instantly, but TCP/HTTP traffic completely ghosts you.**

Because `ping` uses tiny packets (ICMP) and `nslookup` uses UDP, they often sneak through network glitches that cause standard web traffic (`curl` over TCP) to stall. Also, since you are running in a Conda environment (indicated by that `(base)` prompt), there's an extra variable in play.

The three most likely reasons your `curl` is hanging, ordered from the easiest to test to the most common WSL quirk, include:

### 1. The IPv6 Trap

Your `nslookup` output successfully retrieved both IPv4 and IPv6 addresses. Notice that your `ping` automatically chose the IPv4 address (`142.251.152.119`). However, `curl` will often try to connect via IPv6 first if it sees it. If WSL2's IPv6 routing is misconfigured (which is incredibly common), `curl` will just sit there waiting forever.

- **The Test:** Force `curl` to use IPv4 and turn on verbose mode to see exactly what it's doing:
    
    Bash
    
    ```
    curl -4 -v www.google.com
    ```
    
- _Result:_ If this connects instantly, your WSL network configuration is choking on IPv6.
    

### 2. The Conda / Environment Proxy Ghost

Because you are active in your Conda `(base)` environment, it's highly possible that an environment variable is telling `curl` to route traffic through a proxy server that is either misconfigured or dead.

- **The Test:** Check if there are any active proxy variables blocking your path:
    
    Bash
    
    ```
    env | grep -i proxy
    ```
    
- _Result:_ If you see lines like `http_proxy` or `https_proxy` pointing to an old address, you can temporarily clear them by running `unset http_proxy https_proxy` and trying your `curl` command again.
    

### 3. The MTU (Maximum Transmission Unit) Bottleneck

This is the most notorious WSL2 networking issue. Because `ping` packets are small, they pass through without a hitch. But `curl` establishes a TCP handshake and attempts to download data, which uses much larger packets. If the MTU size inside your WSL Linux kernel is larger than what your Windows host network adapter (or VPN) allows, the packets get dropped silently at the virtual bridge.

- **The Test & Fix:** Check your current WSL MTU size (it defaults to `1500`):
    
    Bash
    
    ```
    ip link show eth0
    ```
    
- Try temporarily dropping the MTU to `1400` to see if the traffic can suddenly squeeze through:
    
    Bash
    
    ```
    sudo ip link set dev eth0 mtu 1400
    ```
    
- _Result:_ If `curl [www.google.com](https://www.google.com)` suddenly works after running this, the MTU mismatch was your culprit. You can make this fix permanent by adding that `ip link` line to the bottom of your `~/.bashrc` file.
    

What happens when you run `curl -4 -v [www.google.com](https://www.google.com)`—does it still hang, or does the verbose output show it getting stuck at a specific step like "Connecting to..."?

---

Ah, the classic WSL networking black hole. `[Errno 101] Network is unreachable` means your WSL distribution has lost its bridge to the Windows internet connection, or it's choking on DNS/proxy settings.

Given your hostname ends in **`-LABNB01`**, there is a high chance you are on a school/corporate lab network or using a VPN, which WSL notoriously struggles with out of the box.

Here is how to troubleshoot and fix this, ranked from the most likely solutions to the quickest workarounds.

### Step 0: The Quick Diagnostic

Before changing settings, let's see if WSL can talk to the outside world at all. Run this inside your WSL terminal:

Bash

```
curl -I https://www.google.com
```

- **If it times out or says "Could not resolve host":** It's a DNS or general network issue (Proceed to Fix 1 & 2).
    
- **If it connects but Conda still fails:** It's likely a proxy issue (Proceed to Fix 3).
    

### Fix 1: Enable "Mirrored" Networking (Windows 11 Best Practice)

Windows 11 introduced a networking mode that forces WSL to mirror your Windows network exactly. This fixes almost all VPN, proxy, and lab network drops.

1. Open **Windows Notepad** (or any Windows text editor).
    
2. Open (or create) the file at `C:\Users\<Your_Windows_Username>\.wslconfig`
    
3. Paste the following configuration:
    
    Ini, TOML
    
    ```
    [wsl2]
    networkingMode=mirrored
    ```
    
4. Save the file.
    
5. Open **Windows PowerShell** (not WSL) and shut down WSL to apply changes:
    
    PowerShell
    
    ```
    wsl --shutdown
    ```
    
6. Re-open your WSL terminal and try your `conda` command again.
    

### Fix 2: The DNS Breakdown (Most Common WSL Bug)

WSL frequently generates a broken `/etc/resolv.conf` file. Let's force it to use a stable public DNS (like Google or Cloudflare).

1. In WSL, open the WSL configuration file:
    
    Bash
    
    ```
    sudo nano /etc/wsl.conf
    ```
    
2. Add these lines to stop WSL from overwriting your network settings:
    
    Ini, TOML
    
    ```
    [network]
    generateResolvConf = false
    ```
    
    _(Press `Ctrl+O`, `Enter` to save, then `Ctrl+X` to exit)_.
    
3. Delete the bugged auto-generated file and create a fresh one pointing to Google's DNS:
    
    Bash
    
    ```
    sudo rm /etc/resolv.conf
    sudo bash -c 'echo "nameserver 8.8.8.8" > /etc/resolv.conf'
    ```
    
4. **Crucial:** Go to Windows PowerShell and restart WSL:
    
    PowerShell
    
    ```
    wsl --shutdown
    ```
    

### Fix 3: Are you behind a Corporate/Lab Proxy?

If your lab laptop requires a proxy to access the web, Windows might know about it, but WSL doesn't. You need to pass those environment variables to WSL.

Run this in WSL (replace with your actual lab proxy address and port):

Bash

```
export http_proxy="http://your-proxy-server:port"
export https_proxy="http://your-proxy-server:port"
```

If this works, you can make it permanent by adding those two lines to the bottom of your `~/.bashrc` file.

Did turning on the `mirrored` networking mode clear up the pipeline, or are you currently running a VPN/corporate proxy on that lab laptop?
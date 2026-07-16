---
title: "WSL MTU Troubleshooting"
description: "Explains how to test, calculate, and persist WSL MTU values when VPN or corporate networks break downloads and Git traffic."
created: 2026-07-16
updated: 2026-07-16
type: howto
lang: en
status: draft
tags: [dev]
---

> Related: [[MOC - Dev Environment]] · [[wsl-network-troubleshooting]] · [[wsl-conf-systemd-mtu]]

If your WSL connection is mysteriously freezing, dropping file downloads, or hanging on `git` or `curl` commands, you are likely dealing with the classic WSL MTU (Maximum Transmission Unit) mismatch. This is an incredibly common headache—especially when working over corporate VPNs.

Here is how to test, calculate, and persistently set your WSL MTU to get your internet running smoothly again.

## 1. How to Test Your Current WSL MTU

First, see what your Linux environment is currently using. Inside your WSL terminal, run:

Bash

```
ip link show eth0
```

Look for `mtu 1500` (or similar) in the output. This is the maximum packet size (in bytes) your WSL interface is currently allowed to send.

## 2. How to Find the Optimal MTU Value

If WSL is trying to send 1500-byte packets, but your physical network or VPN only accepts smaller packets, those packets will get silently dropped. You need to find the largest packet size your host network can handle without fragmentation.

### Method A: Check Your Host (Windows) MTU

The easiest starting point is matching your Windows host. In Windows PowerShell (opened as Administrator), run:

PowerShell

```
netsh interface ipv4 show interfaces
```

Look at your active connection (Wi-Fi, Ethernet, or your VPN adapter like GlobalProtect or AnyConnect) and check its **MTU** column. **Your WSL MTU must be equal to or lower than this host value.**

### Method B: Perform a Ping Sweep Test (Inside WSL)

To find the absolute ceiling for your current network, run this ping test inside WSL:

Bash

```
ping -M do -s 1472 -c 3 1.1.1.1
```

- `-M do`: Forces the "Do Not Fragment" flag.
    
- `-s 1472`: The packet payload size. _(1472 bytes payload + 28 bytes for IP/ICMP headers = 1500 MTU)._
    

If you get a `local error: message too long` or 100% packet loss, your MTU is too high. Keep lowering the `-s` value (e.g., `1372`, `1322`) until the ping succeeds.

> **The Golden Formula:**
> 
> `Optimal MTU = (Max working packet payload) + 28`
> 
> _Example:_ If `-s 1322` was the highest size that successfully pinged, your optimal MTU is **1350**.

## 3. What Value Should You Set?

- **Standard Home Network (No VPN):** **1500** (This is the default and requires no changes).
    
- **VPN / Corporate Network:** **1350 to 1400** is the sweet spot. Setting your MTU to **1350** is a highly recommended "universal fallback" that successfully bypasses almost all corporate VPN fragmentation issues.
    

## 4. How to Set Your WSL MTU

### Temporary Fix (Resets on reboot)

If you want to immediately test if a lower MTU fixes your connection issues, run this in WSL:

Bash

```
sudo ip link set dev eth0 mtu 1350
```

_(Replace `1350` with your calculated value)._

### Permanent Fix (Recommended)

WSL rebuilds its virtual network adapter on every reboot, so manual interface changes don't normally persist. Fortunately, you can tell WSL to set this command automatically every time it boots up.

1. Open (or create) the WSL configuration file:
    
    Bash
    
    ```
    sudo nano /etc/wsl.conf
    ```
    
2. Add the following lines:
    
    Ini, TOML
    
    ```
    [boot]
    command = "ip link set dev eth0 mtu 1350"
    ```
    
    _(Be sure to replace `1350` with your optimal MTU)._
    
3. Save and close the file (`Ctrl+O`, `Enter`, then `Ctrl+X` in nano).
    
4. **Restart WSL** to apply the changes. Open Windows PowerShell and run:
    
    PowerShell
    
    ```
    wsl --shutdown
    ```
    
    Now, reopen your WSL terminal, run `ip link show eth0`, and your MTU will be permanently set!
    

### The Modern Alternative: Mirrored Mode (Windows 11 Only)

If you are on Windows 11, you can bypass manual MTU configuration entirely. WSL has a modern network setting called **Mirrored Mode** which automatically mirrors your host's network interfaces, IP addresses, and MTUs directly into the Linux VM.

To enable it:

1. Open Windows File Explorer and go to `%USERPROFILE%` (your main user folder, e.g., `C:\Users\YourName`).
    
2. Create or edit a file named `.wslconfig`.
    
3. Paste the following configuration:
    
    Ini, TOML
    
    ```
    [wsl2]
    networkingMode=mirrored
    dnsTunneling=true
    ```
    
4. Run `wsl --shutdown` in PowerShell, then open WSL again.
    

Are you trying to resolve connection drops on a corporate VPN, or is this for a specific home network setup?

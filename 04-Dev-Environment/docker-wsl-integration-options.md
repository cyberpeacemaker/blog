---
title: "Docker Desktop WSL Integration Options"
description: "Compares default-distro and per-distro Docker Desktop WSL integration switches."
created: 2026-07-21
updated: 2026-07-21
tags: [dev]
type: reference
lang: en
status: draft
---

> Related: [[MOC - Dev Environment]] · [[docker-desktop-wsl-integration]] · [[wsl-distro-choice]]

Here is the breakdown of what each setting actually does under the hood and what happens when you turn them on or off individually.

## The Core Difference

- **"Enable integration with my default WSL distro" (Checkbox):** This is a **dynamic setting**. It automatically connects Docker to whichever Linux distribution is currently set as your system-wide default in Windows (which you can check or change in PowerShell using `wsl --list --verbose`).
    
- **Distro-Specific Switches (e.g., `Ubuntu-24.04`):** These are **static settings**. They explicitly force Docker access to be **ON** or **OFF** for that specific Linux distro, regardless of whether it's set as the default in Windows.
    

## What Happens in Each Scenario?

### 1. Checkbox ON + Ubuntu Switch OFF

- **If Ubuntu _is_ your default WSL distro:** Docker **will work** in Ubuntu because the checkbox covers whatever distro is set as default.
    
- **If Ubuntu is _not_ your default WSL distro** (e.g., if Kali is set as default): Docker **will NOT work** in Ubuntu, but it _will_ work in Kali.
    
- **If you change your default distro later:** Docker access will automatically jump to your new default distro.
    

### 2. Checkbox OFF + Ubuntu Switch ON

- **Docker WILL work in Ubuntu** no matter what.
    
- **Docker will NOT work in any other distro** (even if that other distro is marked as your Windows default).
    

### 3. BOTH are Turned ON

- **Docker WILL work in Ubuntu.**
    
- If you happen to set Kali (or another distro) as your default later, **both** Ubuntu _and_ Kali will have Docker access simultaneously (Kali via the default checkbox, Ubuntu via its explicit switch).
    

### 4. BOTH are Turned OFF

- Docker will not be accessible from any WSL distribution.
    

## Best Practice Recommendation

> **TL;DR:** To avoid confusion if you ever switch default distros in Windows, simply **toggle the switch next to `Ubuntu-24.04` ON directly**. That guarantees Ubuntu will always have Docker access no matter what your Windows default settings are.


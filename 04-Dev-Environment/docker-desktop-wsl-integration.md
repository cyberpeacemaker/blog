---
title: "Enable Docker Desktop WSL Integration"
description: "Steps to expose the Docker command inside a selected WSL2 distribution through Docker Desktop integration."
created: 2026-07-21
updated: 2026-07-21
tags: [dev]
type: howto
lang: en
status: draft
---

> Related: [[MOC - Dev Environment]] · [[docker-wsl-integration-options]] · [[default-wsl-distro-dev-containers]]

This error occurs because the WSL 2 distribution you are using does not have Docker Desktop integration enabled, meaning the `docker` command cannot be found inside that specific Linux environment.

To fix this, follow these steps:

1. **Open Docker Desktop** on your Windows host machine.
    
2. Click on the **Settings** (gear icon) in the top-right corner of the Docker Dashboard.
    
3. In the left-hand menu, go to **Resources** > **WSL Integration**.
    
4. Ensure that **Enable integration with my default WSL distro** is turned **ON**. Alternatively, find your specific Linux distribution (e.g., `Ubuntu`, `Debian`) in the list and toggle the switch next to it to **ON**.
    
5. Click **Apply & restart**.
    
6. **Restart your WSL terminal** or reload your VS Code window (if you are using Dev Containers) so the changes take effect.
    

Once applied, the `docker` command will be correctly exposed inside your WSL 2 distribution.


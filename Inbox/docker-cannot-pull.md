---
created: 2026-08-03 10:08
updated: 2026-08-03 10:08
tags: []
type: reference
lang: en
status: draft
---
### The Cause

Your VS Code Dev Container is failing to start because **Docker cannot pull the required base image** (`[mcr.microsoft.com/devcontainers/base:0-alpine-3.20](https://mcr.microsoft.com/devcontainers/base:0-alpine-3.20)`) from Microsoft's Container Registry.

Even though it worked before, VS Code needs to download the image again if:

- Your local Docker image cache was recently cleared or pruned (e.g., `docker system prune`).
    
- VS Code is trying to check for and pull updated base image layers automatically.
    

### How to Fix It

#### 1. Test the Pull Manually

Open a standard terminal (outside of VS Code) and run:

Bash

```
docker pull mcr.microsoft.com/devcontainers/base:0-alpine-3.20
```

If this fails, Docker is having network connectivity issues reaching Microsoft's servers.

#### 2. Check Connection & VPNs

- **VPN / Corporate Network:** Firewalls, Zscaler, or corporate VPNs often intercept or block traffic to `mcr.microsoft.com`. Try disconnecting from your VPN or proxy to test.
    
- **Docker Desktop Network:** Restart Docker Desktop (or run `sudo systemctl restart docker` on Linux) to reset Docker's network bridge.
    

#### 3. Disable Automatic Image Pulling in VS Code

To stop VS Code from forcing a redownload every time you open the container:

1. Open VS Code Settings (`Ctrl + ,` or `Cmd + ,`).
    
2. Search for `dev.containers.autoPull`.
    
3. Set **Dev > Containers: Auto Pull Image** to **`never`**.
    

Are you currently connected to a VPN/proxy, or did you recently run a Docker cleanup command on your system?


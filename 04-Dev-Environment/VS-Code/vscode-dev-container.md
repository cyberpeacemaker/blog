---
title: "VS Code Dev Container"
description: "Introduces VS Code Dev Containers and how they isolate project tools, extensions, and runtimes inside Docker."
created: 2026-07-23
updated: 2026-07-23
tags: [dev]
type: concept
lang: en
status: draft
---

> Related: [[MOC - Dev Environment]] · [[dev-container-volume-workflow]] · [[default-wsl-distro-dev-containers]]

A **VS Code Dev Container** (Development Container) lets you use a Docker container as a fully featured development environment.

Instead of installing programming languages, runtime environments, databases, and CLI tools directly onto your personal machine, everything runs inside an isolated container. You still get the full, snappy VS Code editor experience on your desktop, but your code, terminal, extensions, and tools live inside the container.

## How It Works

VS Code uses a split client-server architecture to make this seamless:

- **Local UI:** The VS Code interface runs on your host machine (Windows, macOS, or Linux).
    
- **Remote Workspace:** VS Code runs a small server inside the Docker container that hosts extensions, language servers, debuggers, and terminal commands.
    

```
+------------------------+          +----------------------------------+
|      Host Machine      |          |         Docker Container         |
|                        |          |                                  |
|   VS Code (UI Only)    | <======> |   VS Code Server                 |
|   (Source Code Editor) |   IPC    |   (Language Tools, Terminal,     |
|                        |          |    Extensions, Runtime/DBs)       |
+------------------------+          +----------------------------------+
```

## What’s Inside a Dev Container?

Dev containers are defined using a `.devcontainer` folder at the root of your project repository. It usually contains:

1. **`devcontainer.json`**: The primary configuration file that defines:
    
    - The base Docker image or Dockerfile to use.
        
    - VS Code extensions that should automatically install inside the container.
        
    - Port forwarding configurations (e.g., exposing port `3000` for a web app).
        
    - Environment variables and settings.
        
    - Commands to run after creation (e.g., `npm install` or `pip install`).
        
2. **`Dockerfile` or `docker-compose.yml`** _(optional)_: Used if you need custom image builds or multi-container setups (like running your app alongside a PostgreSQL database).
    

## Why Use Dev Containers?

- **Eliminates "Works on My Machine":** Every team member develops inside an identical environment, running the exact same OS, tool versions, and system packages.
    
- **Instant Developer Onboarding:** A new team member can clone the repository, click **"Reopen in Container"**, and be ready to code in minutes without reading a 20-step setup guide.
    
- **Keeps Your Host OS Clean:** No need to clutter your machine with multiple incompatible versions of Python, Node, Java, or system libraries.
    
- **Isolated Tooling:** VS Code extensions installed inside the container don't pollute your global VS Code setup.


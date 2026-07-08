---
created: 2026-07-08 19:07
tags: []
type: reference
lang:
status: draft
---
## What is GitHub Actions?

**GitHub Actions** is an automated CI/CD (Continuous Integration and Continuous Deployment) platform built directly into GitHub. It allows you to automate, customize, and execute your software development lifecycles right inside your repository.

Think of GitHub Actions as an automation engine: when a specific event happens in your repository (like pushing code or opening a pull request), GitHub spins up a temporary virtual machine, runs whatever terminal commands you want, and then tears the machine down.

## What is a Workflow?

A **Workflow** is the actual automated process you set up. It is a configurable, automated procedure defined by a **YAML file** that lives inside your repository under the specific directory path: `.github/workflows/`.

If your automation file isn't in that exact folder, GitHub will ignore it. You can have multiple workflow files in a single repository (e.g., one for testing code, one for deploying to production, and one for cleanup).

## The Core Components of a Workflow

To understand how a workflow operates, visualize it as a chain reaction broken down into 5 key building blocks:

### 1. Events (`on:`)

The **Event** is the trigger that wakes up the workflow.

- _Examples:_ A code push (`push`), a pull request being opened (`pull_request`), a cron-job schedule (`schedule`), or a button click in the GitHub UI (`workflow_dispatch`).
    

### 2. Jobs (`jobs:`)

A workflow is composed of one or more **Jobs**. By default, if you have multiple jobs, they run in **parallel** (simultaneously) to save time, though you can configure them to depend on one another sequentially.

- _Crucial Rule:_ Every job runs on its own completely isolated machine. They do not share a file system unless you explicitly upload and download pipeline artifacts.
    

### 3. Runners (`runs-on:`)

A **Runner** is the server/virtual machine executing the job.

- **GitHub-hosted runners:** GitHub rents out clean, fresh environments (`ubuntu-latest`, `windows-latest`, `macos-latest`) that disappear the moment your job finishes.
    
- **Self-hosted runners:** You can link your own servers (or cloud VMs) to GitHub if you need custom hardware, heavy GPU power, or a highly specific local network setup.
    

### 4. Steps (`steps:`)

A job is broken down into a linear sequence of **Steps** executed in order. A step can either execute a raw terminal shell command or trigger a reusable "Action." If a single step fails, the remaining steps in that job are skipped by default.

### 5. Actions (`uses:`)

An **Action** is a reusable, standalone block of code designed to handle a complex task. Instead of writing 30 lines of shell commands to log into AWS, configure Docker, or set up Java, you "use" an action built by the community or GitHub via the **GitHub Marketplace**.

## Anatomy of a Real Workflow File

Here is what a standard, production-ready CI workflow looks like (`.github/workflows/ci.yml`):

YAML

```
name: Node.js CI Pipeline

# 1. The Trigger (Event)
on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

# 2. The Heavy Lifting (Jobs)
jobs:
  build-and-test:
    # 3. The Environment (Runner)
    runs-on: ubuntu-latest

    # 4. The Sequence (Steps)
    steps:
      # Step A: Download the code from the repo onto the runner machine
      - name: Checkout repository code
        uses: actions/checkout@v4

      # Step B: Set up the programming environment using a pre-made Action
      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm' # Built-in caching to speed up subsequent runs

      # Step C: Run raw terminal commands
      - name: Install dependencies
        run: npm ci

      - name: Run automated tests
        run: npm test
```

## Advanced & Modern Best Practices

As production pipelines grow, basic workflows can become slow or vulnerable to security exploits. Keep these modern paradigms in mind:

- **Concurrency Control:** Prevent wasted billing minutes by automatically canceling older, redundant pipeline runs when a developer pushes multiple commits back-to-back.
    
    YAML
    
    ```
    concurrency:
      group: ${{ github.workflow }}-${{ github.ref }}
      cancel-in-progress: true
    ```
    
- **Security Hardening (SHA Pinning):** Supply-chain attacks targeting public GitHub repositories are highly prevalent. Security baselines heavily recommend pinning third-party actions to an immutable **commit SHA** rather than a mutable version tag (e.g., using `uses: actions/checkout@a5ac7e51b41...` instead of `@v4`) so malicious actors cannot silently modify code upstream.
    
- **Matrix Strategies:** If you need to test your application across multiple operating systems or runtime versions, use a `matrix` block to spawn multiple variations of the same job dynamically without copy-pasting YAML blocks.
    
- **Secrets Management:** Never hardcode credentials, passwords, or API tokens directly into your workflow files. Store them securely in your GitHub repository's **Settings > Secrets and Variables** configuration and reference them dynamically using `${{ secrets.YOUR_SECRET_NAME }}`.


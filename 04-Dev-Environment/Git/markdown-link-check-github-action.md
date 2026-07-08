---
created: 2026-07-08
tags: [github-actions, markdown, documentation]
type: howto
lang: en
status: draft
---

> Related: [[MOC - Dev Environment]] · [[automatically-update-internal-link]] · [[github-action-workflows]]

The GitHub Action that brings the `tcort/markdown-link-check` tool into your repository is highly popular. It acts like an automated guard dog for your documentation: every time you push code or open a Pull Request, it spins up a tiny virtual machine, scans all your `.md` files, tests every link, and throws a red flag if any of them are broken.

## How It Works Under the Hood

The link checker doesn’t just guess; it aggressively tests two types of links:

1. **Internal Links:** It verifies that local relative paths (like `../images/screenshot.png` or `./setup-guide.md`) actually point to an existing file in your repository.
    
2. **External Links:** It sends a real internet request (HTTP request) to external URLs (like `[https://github.com](https://github.com)`) to make sure the website doesn't return a `404 Not Found` or server error.
    

If it finds even one broken link, the GitHub build **fails**, preventing you from accidentally merging broken documentation.

## Quick Setup (Step-by-Step)

To add this to your GitHub repository, you don't need to install anything locally. You just need to create a workflow file.

### Step 1: Create the file

In your repository, create a nested folder structure and a file named exactly like this:

`.github/workflows/markdown-link-check.yml`

### Step 2: Paste the configuration

Copy and paste the following configuration into that file:

YAML

```
name: Check Markdown Links

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  link-check:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Run Markdown Link Check
        uses: gaurav-nelson/github-action-markdown-link-check@v1
```

Once you commit and push this file, go to the **Actions** tab on your GitHub repository web page. You will see it running in real time.

## 3 Pro-Tips for Real-World Repos

Running a raw link checker on a large repository can sometimes be annoying due to false positives or long wait times. Here is how to optimize it like a pro:

### 1. Only Check _Changed_ Files in Pull Requests

If your repository grows to hundreds of files, checking every single link on every typo-fix PR is a waste of time. You can tell the action to only scan files that were modified in that specific PR:

YAML

```
      - name: Run Markdown Link Check
        uses: gaurav-nelson/github-action-markdown-link-check@v1
        with:
          check-modified-files-only: 'yes'
          base-branch: 'main'
```

### 2. Handle the Annoying "429 Too Many Requests" Error

If you link to external sites like GitHub or Reddit multiple times, those websites might temporarily block the GitHub Action runner for spamming requests, throwing a `429` error and failing your build.

To fix this, create a configuration file named `mlc_config.json` in the root of your project:

JSON

```
{
  "aliveStatusCodes": [200, 429]
}
```

Then tell your workflow to use it:

YAML

```
        with:
          config-file: 'mlc_config.json'
```

_(This tells the system: "If a website tells me I'm requesting too fast, treat it as a valid link anyway.")_

### 3. Ignore Specific Links Inline

Sometimes you have dummy links (like `http://localhost:3000` or `http://your-internal-ip`) that will obviously fail on GitHub's servers. You can bypass the checker by wrapping the link with an inline comment directly inside your markdown file:

Markdown

```
<!-- markdown-link-check-disable-next-line -->
Check out my app at [Localhost](http://localhost:3000)
```

Are you setting this up for a personal wiki/knowledge base, or is this a team project where multiple people are editing files at the same time?


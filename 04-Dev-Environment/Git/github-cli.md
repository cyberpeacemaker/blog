---
title: "GitHub CLI"
description: "Explains what the GitHub CLI is and how it differs from Git for repository hosting workflows."
created: 2026-07-22
updated: 2026-07-22
tags: [dev, git]
type: reference
lang: en
status: draft
---

> Related: [[MOC - Dev Environment]] · [[github-authentication]] · [[git-config]]

**`gh`** stands for the **GitHub CLI** (Command Line Interface).

It is the official command-line tool built by GitHub that lets you manage your GitHub workflow—like pull requests, issues, and releases—directly inside your terminal.

## What can you do with `gh`?

Instead of switching back and forth between your terminal and the browser on `github.com`, `gh` lets you handle GitHub features directly:

- **Pull Requests:** Create, review, checkout, and merge PRs (`gh pr create`, `gh pr checkout 42`).
    
- **Issues:** Create, list, close, or assign issues (`gh issue list`).
    
- **Repositories:** Create, fork, clone, or view repositories (`gh repo create`).
    
- **GitHub Actions:** Monitor workflow runs, view logs, or trigger actions (`gh run list`).
    
- **Gists:** Create and share code snippets (`gh gist create`).
    

## `git` vs. `gh`: What's the difference?

While they sound similar, they perform completely different jobs:

|**Tool**|**Focus**|**What it handles**|**Example Commands**|
|---|---|---|---|
|**`git`**|**Source Code Versioning**|Tracks changes, branches, commits, and diffs locally.|`git commit`, `git push`, `git checkout`|
|**`gh`**|**GitHub Platform Features**|Interacts with GitHub's web tools and social workflow.|`gh pr create`, `gh issue list`, `gh repo fork`|

## Getting Started

Once installed, you link it to your GitHub account by running:

Bash

```
gh auth login
```

This opens a quick interactive prompt to log you in via your browser or a personal access token.


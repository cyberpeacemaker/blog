---
title: "Git Hooks"
description: "Explains client-side and server-side Git hooks, common quality-control uses, and a pre-commit conflict-marker example."
created: 2026-07-17
updated: 2026-07-17
type: howto
lang: en
status: draft
tags: [dev, git]
---

> Related: [[MOC - Dev Environment]] · [[git-hook-serverside-github-action]] · [[github-hook-action]]
Think of Git hooks as your personal, automated quality-control guards. They are custom scripts that Git fires off automatically whenever a major action happens—like committing, pushing, or merging.

If your code doesn't meet the standards you've set, these guards will politely (or not-so-politely) stop you in your tracks before you push mistakes to production.

## What is a Git Hook?

At their core, Git hooks are just executable scripts residing in a special directory within your repository.

They are split into two main types:

- **Client-side hooks:** Triggered by operations on your local machine (e.g., committing, merging).
    
- **Server-side hooks:** Triggered on the remote repository (e.g., receiving pushed commits). These are great for enforcing project-wide policies on platforms like GitHub, GitLab, or a self-hosted Git server.
    

## When to Use Git Hooks

You don't need hooks for everything, but they are incredibly useful for automating repetitive checkups.

- **Code Linting & Formatting:** Automatically run tools like Prettier, ESLint, or Black before a commit is finalized to keep the codebase clean.
    
- **Preventing Broken Commits:** Run unit tests before allowing a `git push` so you don't break the main build.
    
- **Enforcing Commit Message Style:** Ensure commit messages follow a specific format (like Conventional Commits) so your automated changelogs don't break.
    
- **Secrets Detection:** Scan files for accidentally exposed API keys or passwords before they leave your machine.
    

## How to Use Git Hooks

Setting up a basic Git hook is surprisingly simple because Git sets up templates for you in every repository you initialize.

### 1. Locate the Hook Directory

Go to your project's root directory. The hooks live inside the hidden `.git` folder:

Bash

```
cd .git/hooks
```

If you list the files in this directory, you will see a bunch of `.sample` files (e.g., `pre-commit.sample`, `commit-msg.sample`).

### 2. Activate a Hook

To activate a hook, you simply need to **rename the file to remove the `.sample` extension**:

Bash

```
mv pre-commit.sample pre-commit
```

### 3. Write Your Script

Open that file in your favorite text editor. You can write your hook in almost any scripting language (Bash, Python, Node.js, Ruby, etc.) as long as your machine can run it. Just make sure the first line (the shebang) points to the correct interpreter:

Bash

```
#!/bin/sh
# Your script goes here
```

### 4. Make It Executable

On Unix-like systems (macOS/Linux), Git won't run the script unless it has execution permissions. Run this command in your terminal:

Bash

```
chmod +x .git/hooks/pre-commit
```

> ⚠️ **The "Gotcha" with Sharing Hooks:**
> 
> Because the `.git` directory is never pushed to your remote repository, Git hooks aren't version-controlled by default. If you want to share hooks with your team, you'll want to use tools like **Husky** (for JavaScript/Node ecosystems), **pre-commit** (a multi-language framework), or configure a shared hooks directory using:
> 
> `git config core.hooksPath .githooks`

## A Practical Example: The "No Leftover Merge Conflicts" Hook

Have you ever accidentally committed code that still had raw git merge conflict markers (`<<<<<<<` or `>>>>>>>`) in it? It’s embarrassing and breaks builds.

Let's write a **`pre-commit`** hook to block this.

### The Script

Create or edit `.git/hooks/pre-commit` and paste the following Bash script:

Bash

```
#!/bin/sh

# Search staged files for unresolved merge conflict markers
if git diff --cached | grep -E "^\+(<<<<<<<|=======|>>>>>>>)" >/dev/null 2>&1; then
    echo "❌ ERROR: You are trying to commit unresolved merge conflicts!"
    echo "Please resolve them before committing."
    exit 1 # Returning a non-zero status aborts the commit
fi

# If we get here, everything is clean!
exit 0
```

### How it Works:

1. When you type `git commit`, Git pauses and executes this script first.
    
2. `git diff --cached` looks at all the changes you are about to commit.
    
3. `grep` searches those changes for conflict markers.
    
4. If it finds any, it prints an error message and exits with status **`1`**. Any exit code other than `0` tells Git to **abort the commit immediately**.
    
5. If clean, it exits with **`0`**, and your commit goes through smoothly.


---
title: "Automation Prompt Suggestion"
description: "Draft prompt pattern for unattended Cursor inbox triage using an audit log, atomic commits, and final push discipline."
created: 2026-07-09
updated: 2026-07-09
tags: [ai, agents, cursor, workflow]
type: reference
lang: en
status: draft
---

> Related: [[MOC - Claude & Cursor]] · [[cursor-cloud-sandbox-trap]] · [[inbox-triage-rules]]

### 1. How Direct-to-Main Pushes Work

You hit the nail on the head. Because you selected the `main` branch as the target in your automation settings (visible at the top of `image_582399.png`), the process looks like this:

```
[Cloud VM spins up] ──> [Clones your remote 'main' branch]
                             │
                             ▼
                    [Executes your instructions]
                             │
                             ▼
                    [Commits changes locally in VM]
                             │
                             ▼
[Pushes directly back to remote 'main' on GitHub] ──> [Cloud VM shuts down]
```

There are no Pull Requests or manual branches involved. The next time you open Cursor on your local machine, you will simply see that you are a few commits behind `main`. You run a quick `git pull`, and the newly organized files instantly appear on your computer.

### 2. Upgrading Your Prompt: Plan Mode + Atomic Commits

Since this automation runs completely unattended at 7:00 AM while you might be asleep, "Plan Mode" looks a little different. Instead of waiting for you to say "Yes," the AI will **write a visible audit log inside your vault** before doing anything. Combined with **atomic commits**, this ensures you can see exactly what it did, and easily undo a single mistake without rolling back the whole run.

Here is a production-grade prompt you can copy and paste directly into your **Agent Instructions**:

Plaintext

```
# Context & Goal
You are an automated vault organization agent. Read 'inbox-triage-rules.md' and 'Daily Workflow.md' to understand the structural logic for organizing markdown notes located in the 'Inbox/' directory.

# Phase 1: Plan Mode (Audit Trail)
1. Scan the 'Inbox/' directory and formulate a reorganization plan.
2. Create or append to a file named 'Inbox/Triage-Log.md'. Write out a bulleted list explaining exactly what files you intend to move, merge, or update, and why. 
3. Commit this log first: `git commit -am "chore(triage): generate daily triage plan"`

# Phase 2: Atomic Execution & Git Discipline
Execute your plan by manipulating the files. To ensure easy rollbacks, do not group all changes into one giant commit. Make separate, atomic commits for each logical action using these exact naming conventions:
- Moving a file: `git commit -am "chore(triage): move [filename] to [destination]"`
- Updating a Map of Content: `git commit -am "docs(moc): update [MOC filename]"`

# Phase 3: Final Push
Once all actions are complete and committed locally, push all individual commits directly to the remote 'main' branch. If the Inbox is already empty, log "Inbox clean" in 'Triage-Log.md', commit it, push, and exit.
```

### Why this setup is incredibly powerful:

- **The Triage Log:** When you open your Obsidian vault or notebook in the morning, you just look at `Triage-Log.md`. It acts like a morning report from your AI assistant.
    
- **Micro-Rollbacks:** If the AI accidentally misclassifies a file named `yaml-okf.md`, you don't have to sort through a massive 50-file diff. You can open your terminal and type `git log`, find the exact commit for that single file, and revert just that specific mistake.
    

Do you want the `Triage-Log.md` file to overwrite itself every morning so it stays clean, or would you prefer it to keep a running history of past days?
---
title: "Cursor Cloud Sandbox Trap"
description: "Explains why scheduled Cursor automations need committed branch or PR output instead of leaving changes inside ephemeral cloud runs."
created: 2026-07-09
updated: 2026-07-09
tags: [ai, agents, cursor, workflow]
type: reference
lang: en
status: draft
---

> Related: [[MOC - Claude & Cursor]] · [[automation-prompt-suggestion]] · [[Daily Workflow]]

Your scheduled setup in `image_582399.png` looks great, but we run into a bit of a logical paradox because of how scheduled (cron) automations work.

Here is the candid truth about your current instruction: **It is currently running in a "Groundhog Day" loop.**

### The Problem: The Cloud Sandbox Trap

Because this automation is triggered automatically **every day at 07:00** (as seen in `image_582399.png`), it spins up a fresh cloud container, pulls your `main` branch, reads your rules, and organizes the inbox perfectly inside its own little world.

But because you told it **"no commit/push"**, it drops the tools and shuts down. Those changes stay stuck in that specific run's cloud branch. The next morning at 7:00 AM, it pulls your _still-unorganized_ `main` branch and does the exact same thing again. Your actual local repo or remote GitHub `main` branch will never actually change.

## The Fix: Choose Your Automation Style

To make this automation actually useful while keeping your data safe, you should change the instruction based on one of two workflows:

### Option A: The "Safe Review" Workflow (Highly Recommended)

Instead of doing nothing, tell the agent to push its changes to a **dedicated triage branch** or **create a Pull Request**. That way, when you wake up, you just pull that branch locally or hit "Merge" on GitHub.

Plaintext

```
1. Read rules from 'inbox-triage-rules.md' and 'Daily Workflow.md'.
2. Organize the files in the 'Inbox/' directory accordingly.
3. When finished, commit the changes and push them to a new branch named 'automation/daily-inbox-triage'. Do not merge directly to main.
```

### Option B: The "Fully Autonomous" Workflow

Since this is a personal blog/Obsidian vault (`blog` repository) and not mission-critical production code, you might just want it to do the chores for you while you sleep. If you trust your rules, let it write directly to `main`.

Plaintext

```
1. Read rules from 'inbox-triage-rules.md' and 'Daily Workflow.md'.
2. Organize the files in the 'Inbox/' directory accordingly.
3. Commit the changes with the message "chore: automated daily inbox triage" and push directly to the main branch.
```

## 3 Quick Tips to Improve Your Prompt

1. **Add Explicit Paths:** Instead of just saying "Inbox", use the exact folder path (e.g., `Inbox/` or `vault/Inbox/`) so the GPT-5.5 model doesn't have to wander around your directory tree looking for it.
    
2. **Define the Commit Message:** If you choose to let it commit, enforce a clean commit message style (like `chore: daily triage`) so your Git history stays clean.
    
3. **Handle Edge Cases:** Tell it what to do if the Inbox is already empty so it doesn't waste time trying to find things to move.
    

Which of those two workflows sounds better for your daily routine—would you rather review a daily triage branch, or do you want the AI to cleanly sort your markdown files directly into `main` before you wake up? 



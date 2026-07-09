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

> Related: [[MOC - Claude & Cursor]] · [[automation-prompt-suggestion]] · [[Daily Workflow]] · [[automation-pr-merge-policy]]

Your scheduled setup in `image_582399.png` looks great, but we run into a bit of a logical paradox because of how scheduled (cron) automations work.

Here is the candid truth about your current instruction: **It is currently running in a "Groundhog Day" loop.**

### The Problem: The Cloud Sandbox Trap

Because this automation is triggered automatically **every day at 07:00** (as seen in `image_582399.png`), it spins up a fresh cloud container, pulls your `main` branch, reads your rules, and organizes the inbox perfectly inside its own little world.

But because you told it **"no commit/push"**, it drops the tools and shuts down. Those changes stay stuck in that specific run's cloud branch. The next morning at 7:00 AM, it pulls your _still-unorganized_ `main` branch and does the exact same thing again. Your actual local repo or remote GitHub `main` branch will never actually change.

## The Fix: PR + Auto-Merge (Recommended for Cursor Automation)

Cursor Cloud scheduled automations always work on an ephemeral cloud branch — they cannot reliably push directly to `main`. The correct unattended pattern is:

1. Agent commits by phase on the cloud branch
2. `bash scripts/finish-ai-task.sh` pushes the branch, opens a PR, and enables auto-merge
3. GitHub Actions CI validates the changes
4. GitHub auto-merges to `main` after checks pass

See [[automation-prompt-suggestion]] for the full prompt and [[automation-pr-merge-policy]] for repo settings.

Plaintext

```
1. Read rules from 'inbox-triage-rules.md' and 'Daily Workflow.md'.
2. Organize the files in the 'Inbox/' directory accordingly.
3. Commit by phase on the current cloud branch (do NOT checkout main).
4. Run: bash scripts/finish-ai-task.sh
   (pushes branch, opens PR, enables auto-merge after CI passes)
```

### Alternative: Direct Push to Main (Non-Cursor Contexts Only)

Direct push to `main` is workable for local scripts or automation environments that actually run on `main`. It is **not** compatible with Cursor Cloud scheduled automations, which always create a cloud branch.

## 3 Quick Tips to Improve Your Prompt

1. **Add Explicit Paths:** Instead of just saying "Inbox", use the exact folder path (e.g., `Inbox/`) so the model doesn't have to wander around your directory tree looking for it.
    
2. **Define the Commit Message:** Enforce a clean commit message style (like `chore(triage): daily inbox triage`) so your Git history stays clean.
    
3. **Handle Edge Cases:** Tell it what to do if the Inbox is already empty so it doesn't waste time trying to find things to move.

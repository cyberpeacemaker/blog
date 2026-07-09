---
title: "Direct Push Daily Triage Script"
description: "Shell workflow for trusted daily inbox triage that validates local phase commits and pushes directly to main."
created: 2026-07-09
updated: 2026-07-09
tags: [dev, git, ai, workflow]
type: howto
lang: en
status: draft
---

> Related: [[MOC - Dev Environment]] · [[automation-pr-merge-policy]] · [[git-squash-and-merge]] · [[automation-prompt-suggestion]]

You are completely right. Committing every single file move is overkill and creates unnecessary noise. Grouping by **logical sub-tasks or phases** is a much smarter, more mature way to handle git history.

Instead of thinking in _files_, we want the AI to think in _milestones_ (e.g., Phase 1: Moving/Sorting, Phase 2: Content polishing, Phase 3: Index/MOC updates).

For trusted daily inbox triage in this personal vault, use direct-to-main automation. The Cursor Automation should target `main`, commit local phase changes, validate them, then run a hardened finish script that pushes directly to `origin main`.

## 1. The Direct-to-Main "Finish Task" Script

Save this script as something generic, like `scripts/finish-ai-task.sh`.

Instead of creating or merging a PR, it detects the current branch and refuses to push unless the automation is running on `main`.

Current implementation: [`scripts/finish-ai-task.sh`](../../scripts/finish-ai-task.sh).

Key safeguards:

- fail fast on command errors
- require `main`
- require a clean working tree
- fetch `origin/main`
- refuse to push if local `main` is behind or diverged
- allow only trusted vault-triage paths in `origin/main..HEAD`
- push committed phase changes directly to `origin main`
- avoid PR creation, PR merge, and `--admin`

## 2. The Daily Triage Prompt Blueprint

Now, your prompt structure becomes modular for trusted daily triage. For larger coding, security, dependency, or ambiguous content work, use [[automation-pr-merge-policy]] and keep the workflow review-first.

> **Context:** Read 'inbox-triage-rules.md' and 'Daily Workflow.md' to organize files in 'Inbox/'.
> 
> 1. **Target:** Run this automation on `main`. Do **not** create a feature branch or pull request for daily inbox triage.
>     
> 2. **Execute & Commit by Phase:** Divide your work into logical sub-tasks. Make a clean commit after completing each major phase.
>     
>     - _Example: One commit for polishing content or updating MOCs, and a separate commit for moving/sorting files._
>         
> 3. **Verify:** Confirm the working tree is clean, only trusted vault-triage paths changed, and validation commands pass.
>
> 4. **Wrap Up:** When all phases are fully completed and committed, run the automation script to push directly to `main`: `bash scripts/finish-ai-task.sh`
>     

## Why this hits the sweet spot

- **Perfect Traceability:** When you look at your Git history on `main`, you will see the phase commits for the day. The history can look like:

    - `polish: updated formatting and tags inside project files`

    - `triage: moved 14 files to respective folders`
                
    - `mocs: appended new links to Index MOC`
        
- **Low Friction:** The AI handles the logical grouping based on its workflow phases, and the script handles the final guarded direct push.
    

Use branch PR workflows only when the task is no longer a trusted daily vault chore.
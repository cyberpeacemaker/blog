---
title: "Agent PR Squash and Merge Script"
description: "Shell sketch for pushing an automation branch, creating a PR, and squash-merging agent triage commits."
created: 2026-07-09
updated: 2026-07-09
tags: [dev, git, ai, workflow]
type: howto
lang: en
status: draft
---

> Related: [[MOC - Dev Environment]] · [[automation-pr-merge-policy]] · [[git-squash-and-merge]] · [[git-pr-example]]

You are completely right. Committing every single file move is overkill and creates unnecessary noise. Grouping by **logical sub-tasks or phases** is a much smarter, more mature way to handle git history.

Instead of thinking in _files_, we want the AI to think in _milestones_ (e.g., Phase 1: Moving/Sorting, Phase 2: Content polishing, Phase 3: Index/MOC updates).

For trusted daily inbox triage, use a hardened finish script that is dynamic but still restricted to known triage branch patterns.

## 1. The Generalized "Finish Task" Script

Save this script as something generic, like `scripts/finish-ai-task.sh`.

Instead of hardcoding one exact branch name, it detects the current branch and refuses to auto-merge anything outside daily-triage branches.

Current implementation: [`scripts/finish-ai-task.sh`](../../scripts/finish-ai-task.sh).

Key safeguards:

- fail fast on command errors
- refuse to run on `main`
- refuse unexpected branch names
- require a clean working tree
- push the current branch with upstream tracking
- reuse an existing PR when present
- create a daily-triage PR when needed
- squash-merge that specific PR
- fetch and sync `main` after merge

## 2. The Daily Triage Prompt Blueprint

Now, your prompt structure becomes modular for trusted daily triage. For larger coding, security, dependency, or ambiguous content work, use [[automation-pr-merge-policy]] and keep the workflow review-first.

> **Context:** Read 'inbox-triage-rules.md' and 'Daily Workflow.md' to organize files in 'Inbox/'.
> 
> 1. **Branch:** Checkout a new branch specific to this task (e.g., `automation/daily-inbox-triage`).
>     
> 2. **Execute & Commit by Phase:** Divide your work into logical sub-tasks. Make a clean commit after completing each major phase.
>     
>     - _Example: One commit for polishing content or updating MOCs, and a separate commit for moving/sorting files._
>         
> 3. **Wrap Up:** When all phases are fully completed, run the automation script to clean up: `bash scripts/finish-ai-task.sh`
>     

## Why this hits the sweet spot

- **Perfect Traceability:** When you look at your Git history on `main`, you will see exactly one commit for the day. If you click on it, you'll see a clean list like:

    - `polish: updated formatting and tags inside project files`

    - `triage: moved 14 files to respective folders`
                
    - `mocs: appended new links to Index MOC`
        
- **Zero Brainpower Required:** The AI handles the logical grouping based on its workflow phases, and the script handles the entire GitHub loop natively.
    

Does this phase-based approach feel closer to how you naturally organize your own manual work?
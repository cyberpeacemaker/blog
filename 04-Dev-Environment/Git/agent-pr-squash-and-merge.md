---
title: "PR Auto-Merge Daily Triage Script"
description: "Shell workflow for trusted daily inbox triage that validates phase commits, opens a PR, and enables auto-merge after CI."
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

For trusted daily inbox triage in this personal vault, use the Cursor Cloud branch + PR auto-merge pattern. The Cursor Automation should target `main` (base branch), commit local phase changes on the cloud branch, validate them, then run the finish script.

## 1. The PR Auto-Merge "Finish Task" Script

Save this script as something generic, like `scripts/finish-ai-task.sh`.

It pushes the cloud branch, opens a PR if one does not exist, and enables auto-merge so GitHub merges after CI passes.

Current implementation: [`scripts/finish-ai-task.sh`](../../scripts/finish-ai-task.sh).

Key safeguards:

- fail fast on command errors
- refuse `main` (require `cursor/daily-inbox-triage*` or `automation/daily-inbox-triage*`)
- require a clean working tree
- fetch `origin/main` and fail if the branch is behind
- validate trusted vault-triage paths via [`validate-triage-paths.sh`](../../scripts/validate-triage-paths.sh)
- push branch, open PR, enable auto-merge (`gh pr merge --auto --squash --delete-branch`)
- avoid immediate merge and `--admin`
- do not `git checkout main` at the end

## 2. The Daily Triage Prompt Blueprint

Now, your prompt structure becomes modular for trusted daily triage. For larger coding, security, dependency, or ambiguous content work, use [[automation-pr-merge-policy]] Mode 3 and keep the workflow review-first.

> **Context:** Read 'inbox-triage-rules.md' and 'Daily Workflow.md' to organize files in 'Inbox/'.
> 
> 1. **Target:** Work on the current cloud branch. Do **not** checkout `main`.
>     
> 2. **Execute & Commit by Phase:** Divide your work into logical sub-tasks. Make a clean commit after completing each major phase.
>     
>     - _Example: One commit for polishing content or updating MOCs, and a separate commit for moving/sorting files._
>         
> 3. **Verify:** Confirm the working tree is clean, only trusted vault-triage paths changed, and validation commands pass.
>
> 4. **Wrap Up:** When all phases are fully completed and committed, run: `bash scripts/finish-ai-task.sh`
>     

## Why this hits the sweet spot

- **Perfect Traceability:** Phase commits appear in the PR. After squash merge, `main` gets one clean commit per day. The PR history preserves:

    - `polish: updated formatting and tags inside project files`

    - `triage: moved 14 files to respective folders`
                
    - `mocs: appended new links to Index MOC`
        
- **Low Friction:** The AI handles the logical grouping based on its workflow phases, and the script handles push + PR + auto-merge.
- **CI gate:** [`.github/workflows/triage-validation.yml`](../../.github/workflows/triage-validation.yml) validates paths and rebuilds the vault map before merge.

Use manual-review PR workflows (Mode 3) when the task is no longer a trusted daily vault chore.

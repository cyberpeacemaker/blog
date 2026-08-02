---
title: "Manual-Review Daily Triage PR Script"
description: "Shell workflow for daily inbox triage that validates phase commits, opens a PR, and stops for human review."
created: 2026-07-09
updated: 2026-08-02
tags: [dev, git, ai, workflow]
type: howto
lang: en
status: draft
---

> Related: [[MOC - Dev Environment]] · [[automation-pr-merge-policy]] · [[git-squash-and-merge]] · [[automation-prompt-suggestion]]

You are completely right. Committing every single file move is overkill and creates unnecessary noise. Grouping by **logical sub-tasks or phases** is a much smarter, more mature way to handle git history.

Instead of thinking in _files_, we want the AI to think in _milestones_ (e.g., Phase 1: Moving/Sorting, Phase 2: Content polishing, Phase 3: Index/MOC updates).

For daily inbox triage in this personal vault, use the Cursor Cloud branch + manual-review PR pattern. The Cursor Automation should target `main` (base branch), commit local phase changes on the cloud branch, validate them, then push the branch and open a PR.

## 1. The Manual-Review "Finish Task" Script

Save this script as something generic, like `scripts/finish-ai-task.sh`.

It pushes the cloud branch and opens a PR if one does not exist. It intentionally does **not** enable auto-merge.

Current implementation: [`scripts/finish-ai-task.sh`](../../scripts/finish-ai-task.sh).

Key safeguards:

- fail fast on command errors
- refuse `main` (require `cursor/daily-inbox-triage*` or `automation/daily-inbox-triage*`)
- require a clean working tree
- fetch `origin/main` and fail if the branch is behind
- validate trusted vault-triage paths via [`validate-triage-paths.sh`](../../scripts/validate-triage-paths.sh)
- push branch and open PR
- avoid auto-merge, immediate merge, and `--admin`
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
> 4. **Wrap Up:** When all phases are fully completed and committed, push the current branch and open or update a PR to `main`. Do **not** enable auto-merge.
>     

## Why this hits the sweet spot

- **Perfect Traceability:** Phase commits appear in the PR. After squash merge, `main` gets one clean commit per day. The PR history preserves:

    - `polish: updated formatting and tags inside project files`

    - `triage: moved 14 files to respective folders`
                
    - `mocs: appended new links to Index MOC`
        
- **Review-first:** The AI handles the logical grouping based on its workflow phases, and the PR shows the exact diff for human review.
- **CI gate:** [`.github/workflows/triage-validation.yml`](../../.github/workflows/triage-validation.yml) validates paths and rebuilds the vault map before merge.

Use this manual-review PR workflow for daily triage and any task where the diff should be checked before merge.

---
title: "Automation Prompt Suggestion"
description: "Draft prompt pattern for unattended Cursor inbox triage using direct-to-main commits, validation, and final push discipline."
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

### 2. Direct-to-main prompt: phase commits + final guarded push

Since this automation runs completely unattended, do not make it wait for a manual PR review. Configure the Cursor Automation target branch as `main`, let the agent commit by phase locally, validate, then run the guarded finish script that pushes directly to `origin main`.

Here is a production-grade prompt you can copy and paste directly into your **Agent Instructions**:

```
> **Context:** Read `inbox-triage-rules.md` and `Daily Workflow.md` to organize files in `Inbox/`.
>
> 1. **Target:** Run this automation on `main`. Do **not** create a feature branch or pull request for daily inbox triage.
>
> 2. **Execute & Commit by Phase:** Divide your work into logical sub-tasks. Make a clean local commit after completing each major phase.
>
>    - Example: one commit for polishing content/updating MOCs, and a separate commit for moving/sorting files.
>    - If 3 or more files are moved, regenerate the vault map before the index/artifact commit.
>
> 3. **Verify:** Confirm the working tree is clean, only trusted vault-triage paths changed, and validation commands pass.
>
> 4. **Wrap Up:** When all phases are fully completed and committed, run:
>
>    ```bash
>    bash scripts/finish-ai-task.sh
>    ```
>
>    The finish script should push the committed phase changes directly to `origin main`. It should not create a PR, merge a PR, or use `--admin`.
```

### Why this setup works

- **No PR fatigue:** Successful daily triage appears in `main`; you just pull the latest vault changes.
    
- **Phase rollback:** If the AI misclassifies a file, use `git log` and revert the specific phase commit instead of untangling one giant diff.
    
- **Guarded final push:** `scripts/finish-ai-task.sh` refuses to push from the wrong branch, with a dirty tree, with a stale local `main`, or with changes outside trusted triage paths.
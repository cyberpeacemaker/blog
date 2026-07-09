---
title: "Automation Prompt Suggestion"
description: "Draft prompt pattern for unattended Cursor inbox triage using cloud-branch commits, PR auto-merge, and CI validation."
created: 2026-07-09
updated: 2026-07-09
tags: [ai, agents, cursor, workflow]
type: reference
lang: en
status: draft
---

> Related: [[MOC - Claude & Cursor]] · [[cursor-cloud-sandbox-trap]] · [[inbox-triage-rules]] · [[automation-pr-merge-policy]]

### 1. How Cursor Cloud Branch + PR Auto-Merge Works

Because you selected `main` as the target branch in your automation settings, Cursor clones `main` but the agent works on an ephemeral cloud branch (e.g. `cursor/daily-inbox-triage-9370`). The process looks like this:

```
[Cloud VM spins up] ──> [Clones remote 'main']
                             │
                             ▼
                    [Works on cloud branch]
                             │
                             ▼
                    [Commits changes by phase]
                             │
                             ▼
                    [finish-ai-task.sh]
                             │
              ┌──────────────┴──────────────┐
              ▼                             ▼
    [Push branch + open PR]      [Enable auto-merge]
              │                             │
              └──────────────┬──────────────┘
                             ▼
              [CI triage-validation passes]
                             │
                             ▼
              [GitHub auto-merges squash to main]
```

You wake up to organized files on `main` without manually clicking Merge. If CI fails, the PR stays open for review.

### 2. Cloud-branch prompt: phase commits + PR auto-merge

Since this automation runs completely unattended, do not make it wait for manual PR review. Configure the Cursor Automation target branch as `main` (base to clone), let the agent commit by phase on the cloud branch, validate, then run the finish script.

Here is a production-grade prompt you can copy and paste directly into your **Agent Instructions**:

```
> **Context:** Read `inbox-triage-rules.md` and `Daily Workflow.md` to organize files in `Inbox/`.
>
> 1. **Target:** Work on the current cloud branch. Do **not** checkout `main`.
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
>    The finish script pushes the branch, opens a PR, and enables auto-merge after CI checks pass. It does not merge immediately or use `--admin`.
```

### Why this setup works

- **Cursor-compatible:** Works with Cursor Cloud's ephemeral branch model; no direct push to `main` required.
- **No PR fatigue:** Auto-merge completes the PR after CI passes; you just pull the latest vault changes.
- **Phase rollback:** If the AI misclassifies a file, revert the squash commit on `main` or inspect phase commits in the PR.
- **Guarded finish:** `scripts/finish-ai-task.sh` refuses to run on `main`, with a dirty tree, with a stale branch, or with changes outside trusted triage paths.

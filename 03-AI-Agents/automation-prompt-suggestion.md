---
title: "Automation Prompt Suggestion"
description: "Draft prompt pattern for Cursor inbox triage using cloud-branch commits, PR creation, manual review, and CI validation."
created: 2026-07-09
updated: 2026-08-02
tags: [ai, agents, cursor, workflow]
type: reference
lang: en
status: draft
---

> Related: [[MOC - Claude & Cursor]] · [[cursor-cloud-sandbox-trap]] · [[inbox-triage-rules]] · [[automation-pr-merge-policy]]

### 1. How Cursor Cloud Branch + Manual-Review PR Works

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
               [Push branch + open PR]
                             │
              [CI triage-validation passes]
                             │
                             ▼
                 [Human reviews and merges]
```

You wake up to a PR that shows exactly what changed. If CI fails, the PR stays open for correction; if CI passes, you still review and merge manually.

### 2. Cloud-branch prompt: phase commits + manual-review PR

Configure the Cursor Automation target branch as `main` (base to clone), let the agent commit by phase on the cloud branch, validate, push the branch, and open a PR. The agent should stop there so a human can review and merge manually.

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
> 4. **Wrap Up:** When all phases are fully completed and committed:
>
>    ```bash
>    git push -u origin <current-branch>
>    ```
>
>    Open or update a pull request from the current cloud branch to `main` using the configured PR automation tool. Do **not** enable auto-merge and do **not** run `scripts/finish-ai-task.sh`; a human will review and merge manually.
```

### Why this setup works

- **Cursor-compatible:** Works with Cursor Cloud's ephemeral branch model; no direct push to `main` required.
- **Manual review:** GitHub shows the exact diff before anything lands on `main`.
- **Phase rollback:** If the AI misclassifies a file, inspect phase commits in the PR and ask for a correction before merging.
- **CI gate:** `triage-validation` still checks trusted paths and vault map generation before review.

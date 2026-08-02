---
title: "Daily Inbox Triage PR Workflow Tradeoff"
description: "Compares direct pushes with branch-and-PR automation for daily Obsidian inbox triage."
created: 2026-07-09
updated: 2026-08-02
tags: [dev, git, workflow, obsidian]
type: reference
lang: en
status: draft
---

> Related: [[MOC - Dev Environment]] · [[automation-pr-merge-policy]] · [[agent-pr-squash-and-merge]] · [[automation-prompt-suggestion]]

# Daily Inbox Triage PR Workflow Tradeoff

You've hit on the classic tension in DevOps and automation: **Safety vs. Friction**.

## The Verdict for Cursor Automation

**Use PR + manual review after checks.** Cursor Cloud scheduled automations always work on an ephemeral branch — direct push to `main` is not compatible with that model.

The daily triage workflow:

1. Agent works on cloud branch (`cursor/daily-inbox-triage-*`)
2. Commits by phase locally
3. Agent pushes branch and opens PR
4. CI (`triage-validation`) validates paths and rebuilds vault map
5. Human reviews the PR and merges manually

This gives you safety (CI gate, revert point) and keeps the final decision with the human reviewer.

### Why PR + Manual Review Wins for Cursor

- **Cursor-compatible:** Works with ephemeral cloud branches; direct push does not.
- **Ultimate Safety:** If the AI hallucinates, `main` stays untouched until CI passes.
- **Human checkpoint:** The PR waits for your review before anything reaches `main`.
- **Visual Diff:** GitHub shows exactly what changed before merge.

### When Direct Push Might Apply

Direct push to `main` is workable only when the automation environment can actually run on and push to `main` — local scripts, not Cursor Cloud scheduled automations. For this vault's daily triage, use Mode 3 from [[automation-pr-merge-policy]].

### The Production Prompt

See [[automation-prompt-suggestion]] for the full copy-paste prompt. Summary:

```
Read inbox-triage-rules.md and Daily Workflow.md. Organize Inbox/ per rules.

1. Work on the current cloud branch (do NOT checkout main).
2. Commit by phase after each major milestone.
3. Verify: clean tree, trusted paths only, validation passes.
4. Push the current branch and open a PR to main.
   Do not enable auto-merge; wait for manual review.
```

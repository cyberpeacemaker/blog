---
title: "Automation PR Merge Policy"
description: "Decision guide for when simple automation tasks may auto-merge and when agent work should stay review-first with phase commits."
created: 2026-07-09
updated: 2026-07-09
tags: [dev, git, ai, workflow]
type: reference
lang: en
status: draft
---

> Related: [[MOC - Dev Environment]] · [[agent-pr-squash-and-merge]] · [[git-squash-and-merge]]

# Automation PR Merge Policy

Use two automation modes:

1. **Simple trusted automation:** create a PR, squash-merge automatically, delete the branch, and sync `main`.
2. **Review-first automation:** create or update a PR, but leave merge approval to a human.

## Mode 1: trusted simple automation with automatic PR merge

Use this only for narrow, repeatable, low-risk chores where the rules are stable and the blast radius is small.

Good fit:

- Daily inbox triage
- Formatting-only maintenance
- Regenerating derived vault artifacts after deterministic note moves
- Other tasks where bad output is easy to revert and unlikely to damage production code

For daily inbox triage, the automation can run:

```bash
bash scripts/finish-ai-task.sh
```

The script should:

- fail fast with `set -euo pipefail`
- refuse to run on `main`
- allow only known triage branch patterns, such as `automation/daily-inbox-triage*` or `cursor/daily-inbox-triage*`
- require a clean working tree before pushing
- push the current branch
- reuse an existing PR when one exists
- create a PR when one does not exist
- squash-merge the specific PR URL
- delete the remote branch
- fetch and sync local `main`

## Mode 2: review-first automation

Use review-first for everything outside the trusted-simple category.

Good fit:

- Code changes
- Security-sensitive changes
- Dependency updates
- Large refactors
- Content changes with ambiguous intent
- Any task that touches multiple ownership boundaries
- Any task where the agent found complicated merge conflicts

In this mode, the agent should still commit and push its work, but should stop after opening or updating a PR. A human reviews the diff, checks assumptions, and merges manually.

## Why auto-merge is risky

The minimal auto-merge script is convenient, but it has sharp edges:

- `gh pr merge --squash --delete-branch --admin` can bypass review and branch protections.
- `gh pr create` and `gh pr merge` are GitHub write operations. Some environments, including Cursor Cloud automation contexts, may restrict direct `gh` writes.
- Without `set -e`, later commands can run after `git push` or `gh pr create` fails.
- Plain `gh pr create` fails when a PR already exists for the branch.
- `git checkout main` changes the local branch after completion, which is risky in interactive agent workflows.

The hardened daily-triage script accepts those risks only for trusted repeatable chores, then adds guardrails so it fails closed instead of continuing through partial failure.

## Phase-based commits for larger work

For non-trivial automation, split the work into logical phases and commit after each phase.

Example phases for inbox triage:

1. **Normalize content:** frontmatter, titles, descriptions, tags, and Related links.
2. **Move files:** route notes from `Inbox/` into topic folders with `git mv`.
3. **Update indexes:** MOCs, hub pages, and generated vault maps.
4. **Verify:** syntax checks, graph rebuilds, tests, or link scans.

Why this works:

- Each commit is a rollback point.
- Reviewers can see the agent's reasoning path.
- A failed verification step does not obscure which phase caused the problem.
- Squash merge can still keep `main` history clean with one final commit.

Rule of thumb: commit by **milestone**, not by individual file and not as one giant final commit.

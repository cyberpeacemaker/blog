---
title: "Automation Delivery Patterns"
description: "Decision guide for direct-to-main automation, PR auto-merge, and review-first automation patterns."
created: 2026-07-09
updated: 2026-07-09
tags: [dev, git, ai, workflow]
type: reference
lang: en
status: draft
---

> Related: [[MOC - Dev Environment]] · [[agent-pr-squash-and-merge]] · [[git-squash-and-merge]]

# Automation Delivery Patterns

Use three automation delivery modes. For this personal Obsidian vault, **daily inbox triage uses Mode 1: direct push to `main`**.

## Mode 1: direct push to main

Use this only for narrow, repeatable, low-risk chores where the rules are stable, the changed paths are predictable, and the result is easy to revert.

Good fit:

- Daily inbox triage for this personal vault
- Formatting-only maintenance in documentation
- Regenerating derived vault artifacts after deterministic note moves
- Other non-production tasks where a bad output is visible in Git history and easy to revert

How daily inbox triage should finish:

```bash
bash scripts/finish-ai-task.sh
```

The direct-push finish script should:

- fail fast with `set -euo pipefail`
- require the automation to be running on `main`
- require a clean working tree before pushing
- fetch `origin/main` and fail if local `main` is behind or diverged
- inspect `origin/main..HEAD` and allow only trusted vault-triage paths
- push committed phase changes directly to `origin main`
- avoid PR creation, PR merge, and `--admin` bypasses

Operational expectation:

1. Configure the Cursor Automation target branch as `main`.
2. Let the agent commit locally by phase.
3. Run validation before the final push.
4. Push all phase commits to `main` only after the working tree is clean.
5. Review the commit history afterward if something looks wrong; use `git revert` for rollback.

## Mode 2: branch PR with auto-merge after checks

Use this when you want unattended completion but still want GitHub branch protection or CI checks to gate the merge.

Good fit:

- Bot dependency updates
- Generated documentation in shared repositories
- Repeatable tasks with reliable CI checks
- Maintenance where reviewers do not need to inspect every run

Guardrails:

- open a PR from a bot branch
- require passing checks
- use auto-merge or a merge queue
- avoid `--admin` unless there is a documented emergency reason
- delete the branch after merge

## Mode 3: branch PR with manual review

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

## Why unattended merging is risky

Unattended automation is convenient, but it has sharp edges:

- Direct push to `main` skips the PR review surface entirely.
- `gh pr merge --squash --delete-branch --admin` can bypass review and branch protections.
- `gh pr create` and `gh pr merge` are GitHub write operations. Some environments, including Cursor Cloud automation contexts, may restrict direct `gh` writes.
- Without `set -e`, later commands can run after `git push` or `gh pr create` fails.
- Plain `gh pr create` fails when a PR already exists for the branch.
- `git checkout main` changes the local branch after completion, which is risky in interactive agent workflows.

The hardened daily-triage script accepts direct-to-main risk only for trusted repeatable chores, then adds guardrails so it fails closed instead of continuing through partial failure.

## Phase-based commits for larger work

For non-trivial automation, split the work into logical phases and commit after each phase.

Example phases for inbox triage:

1. **Normalize content:** frontmatter, titles, descriptions, tags, and Related links.
2. **Move files:** route notes from `Inbox/` into topic folders with `git mv`.
3. **Update indexes:** MOCs, hub pages, and generated vault maps.
4. **Verify:** syntax checks, graph rebuilds, tests, or link scans.

Why this works:

- Each commit is a rollback point.
- Git history shows the agent's reasoning path.
- A failed verification step does not obscure which phase caused the problem.
- Individual commits make direct-to-main rollback straightforward.

Rule of thumb: commit by **milestone**, not by individual file and not as one giant final commit.

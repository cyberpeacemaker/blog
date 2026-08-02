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

Use three automation delivery modes. For this personal Obsidian vault, **daily inbox triage uses Mode 2: branch PR with auto-merge after checks**.

## Mode 1: direct push to main

Use this only for narrow, repeatable, low-risk chores where the rules are stable, the changed paths are predictable, and the result is easy to revert — and where the automation environment can actually push to `main` (not Cursor Cloud scheduled automations).

Good fit:

- Formatting-only maintenance in documentation (local scripts)
- Regenerating derived vault artifacts after deterministic note moves
- Other non-production tasks where a bad output is visible in Git history and easy to revert

Not a fit for Cursor Cloud scheduled automations, which always work on an ephemeral cloud branch.

## Mode 2: branch PR with auto-merge after checks

Use this when you want unattended completion but still want GitHub branch protection or CI checks to gate the merge.

Good fit:

- **Daily inbox triage for this personal vault** (Cursor Automation)
- Bot dependency updates
- Generated documentation in shared repositories
- Repeatable tasks with reliable CI checks
- Maintenance where reviewers do not need to inspect every run

How daily inbox triage should finish:

```bash
bash scripts/finish-ai-task.sh
```

The finish script:

- fail fast with `set -euo pipefail`
- refuse to run on `main` (Cursor Cloud creates a branch like `cursor/daily-inbox-triage-*`)
- require a clean working tree before pushing
- fetch `origin/main` and fail if the branch is behind
- validate changed paths via [`scripts/validate-triage-paths.sh`](../../scripts/validate-triage-paths.sh)
- push the cloud branch, open a PR, and enable auto-merge (`gh pr merge --auto --squash --delete-branch`)
- avoid immediate merge and `--admin` bypasses

Operational expectation:

1. Configure the Cursor Automation target branch as `main` (base branch to clone).
2. Let the agent commit locally by phase on the cloud branch Cursor creates.
3. Run validation before calling the finish script.
4. Finish script opens a PR and enables auto-merge; GitHub merges after CI passes.
5. Review the squash commit on `main` afterward if something looks wrong; use `git revert` for rollback.

### GitHub repo settings

Required for unattended daily triage:

1. **Enable auto-merge:** Settings → General → Allow auto-merge (or `gh repo edit --enable-auto-merge`)
2. **Branch protection on `main`:**
   - Require status check: `triage-validation`
   - Allow auto-merge to satisfy required checks
   - No required human reviewers (keeps it unattended)

CI workflow: [`.github/workflows/triage-validation.yml`](../../.github/workflows/triage-validation.yml) runs on PRs from `cursor/daily-inbox-triage*` or `automation/daily-inbox-triage*` branches.

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

- Direct push to `main` skips the PR review surface entirely and is incompatible with Cursor Cloud branch workflow.
- `gh pr merge --squash --delete-branch --admin` can bypass review and branch protections.
- `gh pr create` and `gh pr merge` are GitHub write operations. Some environments, including Cursor Cloud automation contexts, may restrict direct `gh` writes.
- Without `set -e`, later commands can run after `git push` or `gh pr create` fails.
- Plain `gh pr create` fails when a PR already exists for the branch.
- `git checkout main` changes the local branch after completion, which is risky in interactive agent workflows.

The hardened daily-triage script uses auto-merge (not immediate merge) so CI gates the merge, and fails closed instead of continuing through partial failure.

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
- Phase commits appear in the PR; squash merge keeps `main` history clean.

Rule of thumb: commit by **milestone**, not by individual file and not as one giant final commit.

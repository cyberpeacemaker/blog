#!/bin/bash
set -euo pipefail

# Intended for trusted daily inbox triage on Cursor cloud branches.
# Pushes the branch, opens a PR, and enables auto-merge after CI passes.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BRANCH_NAME="$(git branch --show-current)"

if [[ "$BRANCH_NAME" == "main" ]]; then
  echo "Error: Triage finish must run on a cloud/feature branch, not main."
  exit 1
fi

if [[ "$BRANCH_NAME" != automation/daily-inbox-triage* &&
      "$BRANCH_NAME" != cursor/daily-inbox-triage* &&
      "$BRANCH_NAME" != automation/inbox-rule-application* &&
      "$BRANCH_NAME" != cursor/inbox-rule-application* ]]; then
  echo "Error: Refusing to finish unexpected branch: $BRANCH_NAME"
  exit 1
fi

if [[ -n "$(git status --porcelain)" ]]; then
  echo "Error: Working tree is dirty. Commit all changes before finishing."
  git status --short
  exit 1
fi

git fetch origin main

REMOTE_HEAD="$(git rev-parse origin/main)"
MERGE_BASE="$(git merge-base HEAD origin/main)"

if [[ "$MERGE_BASE" != "$REMOTE_HEAD" ]]; then
  echo "Error: origin/main has commits not in this branch. Rebase onto origin/main before finishing."
  exit 1
fi

CHANGED_FILES="$(git diff --name-only origin/main..HEAD)"

if [[ -z "$CHANGED_FILES" ]]; then
  echo "No local commits to push; branch is already in sync with origin/main."
  exit 0
fi

bash "$SCRIPT_DIR/validate-triage-paths.sh" origin/main

git push -u origin "$BRANCH_NAME"

PR_URL="$(gh pr view "$BRANCH_NAME" --json url --jq .url 2>/dev/null || true)"

if [[ -z "$PR_URL" ]]; then
  PR_URL="$(gh pr create \
    --title "chore(triage): daily inbox triage" \
    --body "Automated daily inbox triage. Squash commit preserves phase-by-phase history in PR commits.")"
fi

gh pr merge "$PR_URL" --auto --squash --delete-branch

echo "PR opened and auto-merge enabled: $PR_URL"
echo "Merge completes after triage-validation CI checks pass."

#!/bin/bash
set -euo pipefail

# Intended for trusted daily inbox triage runs only.
BRANCH_NAME="$(git branch --show-current)"

if [[ "$BRANCH_NAME" == "main" ]]; then
  echo "Error: You are on main. Switch to a feature branch first."
  exit 1
fi

if [[ "$BRANCH_NAME" != automation/daily-inbox-triage* && "$BRANCH_NAME" != cursor/daily-inbox-triage* ]]; then
  echo "Error: Refusing to auto-merge unexpected branch: $BRANCH_NAME"
  exit 1
fi

if [[ -n "$(git status --porcelain)" ]]; then
  echo "Error: Working tree is dirty. Commit all changes before finishing."
  git status --short
  exit 1
fi

git push -u origin "$BRANCH_NAME"

PR_URL="$(gh pr view "$BRANCH_NAME" --json url --jq .url 2>/dev/null || true)"

if [[ -z "$PR_URL" ]]; then
  PR_URL="$(gh pr create \
    --title "chore(triage): daily inbox triage" \
    --body "Automated daily inbox triage. Review squash commit description for phase-by-phase history.")"
fi

gh pr merge "$PR_URL" --squash --delete-branch --admin

git fetch origin main
git checkout main
git pull origin main
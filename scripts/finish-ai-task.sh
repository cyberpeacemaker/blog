#!/bin/bash

# 1. Dynamically get the current branch name
BRANCH_NAME=$(git branch --show-current)

# Safety check: Don't accidentally run this on main
if [ "$BRANCH_NAME" == "main" ]; then
    echo "Error: You are on the main branch. Switch to a feature branch first."
    exit 1
fi

# 2. Push the current branch
git push origin "$BRANCH_NAME"

# 3. Create the PR with a generic title (GitHub will pull in the commit history anyway)
gh pr create --title "ai($BRANCH_NAME): automated task completion" --body "Review the squash commit description for step-by-step trace."

# 4. Squash, merge, delete remote branch, and sync local main
gh pr merge --squash --delete-branch --admin
git checkout main
git pull
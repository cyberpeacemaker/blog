---
created: 2026-07-09 10:07
updated: 2026-07-09 10:07
tags: []
type: reference
lang: en
status: draft
---


```bash
#!/bin/bash
BRANCH_NAME="automation/daily-inbox-triage"

# Push the iterative commits the AI made
git push origin $BRANCH_NAME

# Create the PR
gh pr create --title "chore(triage): daily inbox triage" --body "Automated daily cleanup."

# Squash, merge, delete the remote branch, and update local main
gh pr merge --squash --delete-branch --admin
git checkout main
git pull
```
---
title: "Agent PR Squash and Merge Script"
description: "Shell sketch for pushing an automation branch, creating a PR, and squash-merging agent triage commits."
created: 2026-07-09
updated: 2026-07-09
tags: [dev, git, ai, workflow]
type: howto
lang: en
status: draft
---

> Related: [[MOC - Dev Environment]] · [[git-squash-and-merge]] · [[git-pr-example]]


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
---
title: "Git Post-Merge Commit Recovery"
description: "Explains why commits pushed after a PR merge are stranded and how to recover them with a new PR, cherry-pick, or fresh branch."
created: 2026-07-09
updated: 2026-07-09
tags: [dev, git, workflow]
type: howto
lang: en
status: draft
---

> Related: [[MOC - Dev Environment]] · [[git-pr-example]] · [[git-best-practice]]

# Git Post-Merge Commit Recovery

## What is Happening Here?

You’ve run into a classic Git timing quirk!

When PR #3 was merged, GitHub took the feature branch exactly as it looked at that exact millisecond—which capped off at commit `35d94d3`—and integrated it into your target branch (like `main` or `develop`).

Once a Pull Request is merged, it becomes an immutable historical record. When you pushed the later commit (`795917a`) to the feature branch _after_ the merge happened, the PR was already closed. GitHub will never retroactively add new commits to an already-closed or merged PR.

## Is This Normal?

**Yes, 100% normal.** It happens all the time, usually due to one of two scenarios:

1. **The Race Condition:** A developer made a final commit (`795917a`) locally but forgot to push it before someone else (or they themselves) clicked "Merge" on GitHub.
    
2. **Post-Merge Work:** A developer kept working on the same local branch, made a new commit, and pushed it without realizing the PR had already been accepted and closed.
    

## Solutions

Depending on what you want to do with that "stranded" commit (`795917a`), here is how you can fix it:

### Solution 1: Open a New Pull Request (Easiest & Cleanest)

Since GitHub already knows the previous commits are merged, you can actually open a **brand-new PR** using the exact same feature branch.

- GitHub is smart enough to realize that the old commits are already in `main`.
    
- This new PR will _only_ contain your documentation/script commit (`795917a`). Just open PR #4, get it approved, and merge it.
    

### Solution 2: Cherry-Pick the Commit Directly to Main

If your team allows direct pushes to the target branch (or if you just want to move that single commit over without another PR cycle), you can cherry-pick it:

Bash

```
# Switch to your main branch and get the latest updates
git checkout main
git pull origin main

# Grab just that specific documentation commit and apply it to main
git cherry-pick 795917a

# Push it up
git push origin main
```

### Solution 3: Move it to a Fresh Branch

If you want to keep things organized and avoid reusing a branch that was already "spent" on PR #3, you can spin the new commit off into its own branch:

Bash

```
# Create a new branch starting exactly at your documentation commit
git checkout -b fix-documentation-script 795917a

# Push the new branch to GitHub
git push origin fix-documentation-script
```

From there, you can open a fresh, clean PR for `fix-documentation-script`.

> 💡 **Pro-Tip for the Future:** To prevent this from happening again, go to your GitHub Repository **Settings**, scroll down to the "Pull Requests" section, and check the box for **"Automatically delete head branches"**. This deletes the feature branch on GitHub the moment a PR is merged, which instantly alerts developers that they need to pull from `main` and branch out afresh for their next commits!


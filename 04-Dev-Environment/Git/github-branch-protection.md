---
title: "GitHub Branch Protection"
description: "Explains branch protection rules, required pull requests, status checks, force-push blocking, and repository rulesets."
created: 2026-07-17
updated: 2026-07-17
type: reference
lang: en
status: draft
tags: [dev, git]
---

> Related: [[MOC - Dev Environment]] · [[github-collaboration-pr-loop]] · [[fix-broken-cicd]]
# Secure Your Code: A Guide to GitHub Branch Protection

Think of **GitHub Branch Protection** as the digital bouncer for your codebase. Without it, anyone with write access could accidentally (or intentionally) delete your `main` branch, force-push broken code over production, or merge untested features without a single peer review.

By setting up branch protection, you establish a set of rules that code must follow before it can touch your most important branches (typically `main`, `master`, or `production`).

## What is Branch Protection?

At its core, branch protection prevents direct commits to critical branches and forces developers to use **Pull Requests (PRs)**.

> **The Golden Rule of Team Development:** No one—not even the tech lead on a caffeine rush—should be able to push code directly to production without another set of eyes and automated tests giving it the green light.

## The Key Rules You Should Be Using

When configuring your protection rules, there are a few standard settings that form the backbone of a healthy workflow:

- **Require a Pull Request Before Merging:** This disables direct pushes. To get code in, you _must_ open a PR.
    
    - **Require Approvals:** You can set a minimum number of approvals (usually 1 or 2) from peers before a PR can merge.
        
    - **Dismiss Stale Approvals:** If someone approves your PR, but then you push _more_ changes, the previous approval is wiped, and they have to review it again.
        
- **Require Status Checks to Pass:** This connects to your CI/CD pipeline (like GitHub Actions). Your code won't merge unless your tests, linters, and security scanners pass.
    
- **Block Force Pushes & Deletions:** By default, protecting a branch blocks `git push --force` and branch deletion. This keeps your Git history safe from being rewritten or wiped out.
    
- **Require Conversation Resolution:** Ensure that all review comments and discussions are marked as "resolved" before the merge button turns green. No ignoring feedback allowed!
    

## Common Rules & Their Practical Value

Here is a quick breakdown of how these rules protect your team:

|**Rule Setting**|**Why You Want It**|**Risk of Ignoring It**|
|---|---|---|
|**Require Approvals**|Ensures code quality and knowledge sharing.|Buggy or unauthorized code slips straight to production.|
|**Require Status Checks**|Guarantees that automated tests actually pass.|Merging code that breaks the build or fails basic unit tests.|
|**Require Linear History**|Keeps your git history clean by avoiding messy merge commits.|A tangled web of merge commits that is impossible to debug later.|
|**Do not allow bypass**|Enforces rules even for repository Admins.|"Admin privilege" mistakes where a senior dev accidentally breaks production.|

## Branch Protection Rules vs. Repository Rulesets

If you've spent any time in GitHub's settings, you've probably noticed two options: **Branch Protection Rules** and **Repository Rulesets**.

- **Branch Protection Rules (Classic):** These are applied to individual branches in a specific repository. They are great for small, simple setups, but can be tedious to manage if you have dozens of repos.
    
- **Repository Rulesets (Modern):** This is the modern, more powerful way to manage branch security. Rulesets let you apply rules across multiple branches (using wildcards like `release/*`) or even across your _entire organization_. They also introduce smoother bypass rules—like allowing automated deploy bots to skip rules without giving them full admin powers.
    

> **Note on Pricing:** If you are on a free GitHub plan, branch protection is fully available for **public** repositories, but is restricted for **private** repositories unless you upgrade to Pro, Team, or Enterprise plans.

Are you setting this up for a personal project to practice good habits, or are you trying to establish a robust workflow for a collaborative team?


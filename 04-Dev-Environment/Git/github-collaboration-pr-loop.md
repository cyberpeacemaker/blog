---
title: "GitHub PR Collaboration Loop"
description: "Outlines a lightweight issue, PR review, kanban, and CI workflow for a two-person GitHub team."
created: 2026-07-14 17:07
updated: 2026-07-14 17:07
tags: [dev, git, workflow]
type: reference
lang: en
status: draft
---

> Related: [[MOC - Dev Environment]] · [[github-collaboration]] · [[github-action-workflows]]

You are already off to a fantastic start! Using the **Issue $\rightarrow$ Pull Request (PR)** workflow is standard practice for a reason: it keeps your code clean and your history traceable.

Since there are only two of you, you have a massive advantage: **maximum agility and zero corporate bureaucracy.** However, the biggest trap for a two-person team is accidentally stepping on each other's toes or letting communication slide because "there are only two of us."

Here is a practical, lightweight framework to supercharge your GitHub collaboration without slowing you down.

## 1. Optimize Your PR & Review Loop

Since both of you have push access, it’s tempting to just merge your own stuff. Don't. Use each other as a safety net.

- **The "One-Approval" Rule:** Protect your `main` branch in GitHub settings. Require at least **1 approved review** before a PR can be merged. This means you _must_ look at each other's code.
    
- **Draft PRs are Your Friend:** The moment you start writing code, open a **Draft PR**. This signals to your partner, _"Hey, I'm working on this, it's not ready yet, but you can see what I'm doing."_ It prevents you both from building the same thing differently.
    
- **Link Issues to PRs:** Use keywords in your PR description (e.g., `Closes #12` or `Fixes #45`). When the PR is merged, GitHub will automatically close the issue for you. Magic.
    

## 2. Visualize the Work (GitHub Projects)

Creating issues is great, but a flat list of issues can get messy fast.

- **Set up a Basic Kanban Board:** Go to the **Projects** tab in your repo and create a simple board with three columns: **Todo**, **In Progress**, and **Done**.
    
- **Assign Everything:** Never leave an issue unassigned. If you take it, assign it to yourself. If it’s in "In Progress" and assigned to you, your partner knows to stay away from those files to avoid merge conflicts.
    

## 3. Automate the "Boring" Stuff

Don't waste time arguing over code formatting or tabs vs. spaces in your PR comments. Let robots do that.

- **Add a Linter/Formatter:** Use tools like Prettier, ESLint, or Black (depending on your language) and enforce them.
    
- **GitHub Actions:** Set up a simple automated workflow that runs your tests and linters every time a PR is opened. If the "red X" shows up, the author knows they have to fix it before asking for a review.
    

> ### 💡 The 2-Member Golden Rule
> 
> **Code synchronously, review asynchronously.**
> 
> Talk out the big architecture design together over a quick call _before_ writing code. Once the plan is set, split up, write the code, and use GitHub PRs to review the implementation in your own time.

What is the biggest friction point you two have run into so far—is it dealing with merge conflicts, waiting too long for code reviews, or just figuring out who should work on what next?


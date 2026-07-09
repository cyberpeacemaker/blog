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

You are completely right. Committing every single file move is overkill and creates unnecessary noise. Grouping by **logical sub-tasks or phases** is a much smarter, more mature way to handle git history.

Instead of thinking in _files_, we want the AI to think in _milestones_ (e.g., Phase 1: Moving/Sorting, Phase 2: Content polishing, Phase 3: Index/MOC updates).

To make this completely general-purpose so you can use it for _any_ automation workflow, we can make two quick adjustments: make the bash script dynamic (so it works on any branch) and generalize the prompt instruction.

## 1. The Generalized "Finish Task" Script

Save this script as something generic, like `scripts/finish-ai-task.sh`.

Instead of hardcoding a specific branch name, it dynamically detects whatever branch the AI is currently working on.

Bash

```
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
```

## 2. The New Generalized Prompt Blueprint

Now, your prompt structure becomes modular. You can copy and paste this structure for file triage, coding, content generation, or any other agent workflow.

> **Context:** Read 'inbox-triage-rules.md' and 'Daily Workflow.md' to organize files in 'Inbox/'.
> 
> 1. **Branch:** Checkout a new branch specific to this task (e.g., `automation/daily-inbox-triage`).
>     
> 2. **Execute & Commit by Phase:** Divide your work into logical sub-tasks. Make a clean commit after completing each major phase.
>     
>     - _Example: One commit for polishing content or updating MOCs, and a separate commit for moving/sorting files._
>         
> 3. **Wrap Up:** When all phases are fully completed, run the automation script to clean up: `bash scripts/finish-ai-task.sh`
>     

## Why this hits the sweet spot

- **Perfect Traceability:** When you look at your Git history on `main`, you will see exactly one commit for the day. If you click on it, you'll see a clean list like:

    - `polish: updated formatting and tags inside project files`

    - `triage: moved 14 files to respective folders`
                
    - `mocs: appended new links to Index MOC`
        
- **Zero Brainpower Required:** The AI handles the logical grouping based on its workflow phases, and the script handles the entire GitHub loop natively.
    

Does this phase-based approach feel closer to how you naturally organize your own manual work?
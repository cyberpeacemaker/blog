---
title: "Draft Pull Request"
description: "Explains when draft pull requests help share work-in-progress code, run CI, and prevent accidental merges."
created: 2026-07-17
updated: 2026-07-17
type: reference
lang: en
status: draft
tags: [dev, git]
---

> Related: [[MOC - Dev Environment]] · [[github-collaboration-pr-loop]] · [[git-pr-example]]
# Draft Pull Request (Software Development)

In software development, a **Draft Pull Request** is a feature (on GitHub, GitLab, etc.) that allows you to open a PR to show your progress without triggering formal reviews or allowing it to be accidentally merged.

### When to Use

- **For Early Feedback:** You want to ask a teammate about your code structure _before_ writing the entire feature.
    
- **To Run CI/CD:** You want to see if your code passes automated testing pipelines while it is still a work-in-progress (WIP).
    
- **To Prevent Duplication:** You want to signal to the team, _"Hey, I am actively working on this task."_
    

### How to Use

1. **Push your branch** to your remote repository.
    
2. Go to the "Create Pull Request" page.
    
3. Click the dropdown arrow next to the green "Create pull request" button.
    
4. Select **Create draft pull request**.
    
5. Once your code is complete and tested, open the PR and click **Ready for review** to change it to a standard PR.
    

### Example (Draft PR Template)

> **Title:** `Draft: Implement Stripe Payment Gateway (#402)`
> 
> **What’s done so far:**
> 
> - Created the DB schema for transactions.
>     
> - Added the Stripe API wrapper.
>     
> 
> **To-Do:**
> 
> - [ ] Write unit tests.
>     
> - [ ] Handle webhook errors.
>     
> 
> **Questions for the team:**
> 
> - @LeadDev, should we store the full Stripe response in our logs, or is that a security risk?
>     

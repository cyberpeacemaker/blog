---
created: 2026-07-17 08:07
updated: 2026-07-17 08:07
tags: []
type: reference
lang: en
status: draft
---
We’ve all been there: you open a pull request (PR) to review a colleague's code, and the description is either completely blank or says something incredibly descriptive like _"fixed some stuff."_

Enter the **Pull Request Template**. It is a developer's best friend for keeping sanity intact during code reviews. Let’s dive into what they are, why they exist, and how you can start using them.

## What is a Pull Request Template?

A **Pull Request Template** is a standardized, pre-formatted Markdown file that automatically populates the description field when a developer creates a new PR.

Think of it as a digital form or checklist. Instead of staring at a blank text box, developers are greeted with guided prompts (e.g., _"What does this PR do?", "How can I test this?", "Does this close any issues?"_).

## Background: Why Do We Need Them?

In the early days of collaborative coding, PRs were often chaotic. As engineering teams grew and open-source software exploded, maintainers faced a massive bottleneck: reviewing code without context.

Without a template, reviewers have to play detective. They have to dig through commits, guess the intent of the changes, and manually check if the author wrote tests or updated the documentation.

PR templates were introduced by platforms like GitHub, GitLab, and Bitbucket to solve this. They act as a **lightweight quality gate** that shifts the responsibility of context-sharing back to the author _before_ the review process even begins.

## When to Use a PR Template

You should absolutely implement a PR template if:

- **Your team is growing:** When you scale past 2–3 developers, verbal communication isn't enough to keep track of every code change.
    
- **You run an open-source project:** Outside contributors need clear guardrails on what information you require to accept their code.
    
- **Reviews are taking too long:** If reviewers are constantly asking _"How do I run this?"_ or _"Did you test this on mobile?"_, a template will eliminate that back-and-forth.
    
- **Compliance/QA is strict:** If you need to guarantee that every change has been QA'd, peer-reviewed, and linked to a Jira/Linear ticket.
    

## How to Use It (GitHub Example)

Setting one up is incredibly easy. For GitHub, all you need to do is add a Markdown file to your repository.

1. Create a file named `pull_request_template.md`.
    
2. Place it in one of these locations in your project's root directory:
    
    - The root directory: `pull_request_template.md`
        
    - The `.github` folder (recommended to keep things clean): `.github/pull_request_template.md`
        
    - A `docs` folder: `docs/pull_request_template.md`
        
3. Commit and push this file to your default branch (usually `main` or `master`).
    

From that moment on, whenever anyone clicks "New Pull Request," the template will automatically load in the description box.

> **Pro Tip:** If you want different templates for different tasks (e.g., one for bug fixes and one for major features), GitHub allows you to create a `.github/PULL_REQUEST_TEMPLATE/` folder and store multiple template files there.

## Example: A Standard PR Template

Here is a highly effective, battle-tested template that you can copy, paste, and customize for your project:

Markdown

```
## Describe your changes
<!-- Provide a clear, concise summary of the changes you've made and why. -->


## Related Issue / Ticket
<!-- Link the Jira ticket, Linear issue, or GitHub issue here. E.g., Fixes #123 -->


## Type of change
<!-- Please delete options that are not relevant. -->
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update


## How Has This Been Tested?
<!-- Describe the tests you ran to verify your changes. Provide instructions so we can reproduce. -->
- [ ] **Local Manual Testing:** (e.g., Tested on Chrome/Safari, verified the login flow works)
- [ ] **Unit Tests:** (e.g., Added coverage for the new utility function)


## Checklist:
- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] My changes generate no new warnings
```

Are you looking to set this up for a specific platform (like GitHub, GitLab, or Bitbucket), or is there a particular bottleneck in your team's current review process you are hoping this will solve?


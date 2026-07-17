---
created: 2026-07-17 11:07
updated: 2026-07-17 11:07
tags: []
type: reference
lang: en
status: draft
---
If Pull Request templates save the _reviewers'_ sanity, **Issue Templates** save the _maintainers'_ sanity.

If you've ever received a ticket from a user or stakeholder that just says, _"The login button is broken,"_ with absolutely no context, screenshots, or error logs, then you already know exactly why Issue Templates are a lifesaver.

Here is the breakdown of how they work, why they are essential, and how to set them up.

## What is an Issue Template?

An **Issue Template** is a predefined form or Markdown structure that appears when someone goes to open a new ticket (an "Issue") in a repository.

Instead of a blank canvas, the user is prompted to fill out specific fields depending on what they are trying to do—such as reporting a bug, suggesting a new feature, or asking a question.

## Background: The Dreaded "It's Broken" Ticket

In any software project, getting feedback is great, but bad feedback is exhausting. Before issue templates, users would submit vague, one-sentence bug reports. Maintainers would then have to spend days playing "tech support ping-pong," asking:

- _What browser are you using?_
    
- _What version of the app are you running?_
    
- _Can you show me a screenshot of the error?_
    

GitHub introduced Issue Templates to intercept this frustration at the source. It forces the person reporting the issue to give you the exact diagnostic data you need to fix the problem on day one.

## When to Use Issue Templates

You should set up issue templates immediately if:

- **You run an open-source project:** Non-developers or external users will constantly submit issues, and they need strict guidelines on how to do it properly.
    
- **Your QA team or Beta testers are submitting bugs:** A template ensures every bug report looks identical, making them vastly easier to triage.
    
- **You want to separate bugs from feature requests:** Templates let you steer users down different paths from the very beginning.
    

## How to Use It (GitHub Example)

Unlike PR templates (where you usually just have one main file), GitHub allows you to create **multiple** issue templates for different scenarios.

1. In your project, create a folder named `.github/ISSUE_TEMPLATE/`.
    
2. Inside that folder, create separate Markdown files for your needs. For example:
    
    - `.github/ISSUE_TEMPLATE/bug_report.md`
        
    - `.github/ISSUE_TEMPLATE/feature_request.md`
        
3. Commit and push these to your main branch.
    

When a user clicks "New Issue" on GitHub, they will be presented with a menu asking them to choose between your templates before they can start typing.

> **Modern Upgrade Note:** GitHub also supports **Issue Forms** using YAML (`.yml` files). Instead of a text document, Issue Forms turn your templates into actual UI forms with dropdowns, required checkboxes, and text fields!

## Example: A Standard Bug Report Template

Here is a standard Markdown template you can drop into `.github/ISSUE_TEMPLATE/bug_report.md`:

Markdown

```
---
name: 🐛 Bug Report
about: Report a reproducible bug to help us improve.
title: '[BUG] - Short description of the issue'
labels: bug, triage
assignees: ''
---

## 🐛 Describe the Bug
A clear and concise description of what the bug is.

## 🔄 Steps to Reproduce
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

## 🔮 Expected Behavior
A clear and concise description of what you expected to happen.

## 📸 Screenshots / Videos
If applicable, add screenshots or screen recordings to help explain your problem.

## 💻 Environment Context
Please complete the following information:
- **OS:** [e.g. iOS 17, Windows 11]
- **Browser / App Version:** [e.g. Chrome 122, v2.4.1]
- **Device:** [e.g. iPhone 15, Macbook Pro]

## 📝 Additional Context
Add any other context or logs about the problem here.
```

Are you looking to set up simple Markdown templates for your team, or would you like to explore GitHub's advanced YAML "Issue Forms" to create structured checkboxes and dropdowns for your users?


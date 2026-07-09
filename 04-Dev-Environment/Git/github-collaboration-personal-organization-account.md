---
title: "GitHub Collaboration from Personal Accounts"
description: "Explains how direct collaborators work on personal-account repos and why organizations are safer for teams."
created: 2026-07-09
updated: 2026-07-09
type: reference
lang: en
status: draft
tags: [dev, git]
---

> Related: [[MOC - Dev Environment]] · [[github-share-repo]] · [[github-organization]]
Yes, **it absolutely still works!**

Even if the repository is owned by a personal account (like `nagameTW`) instead of a company organization, you can still use Scenario A. You just have to explicitly give your coworker permission to access it.

Here is how you set it up and how it works:

### 1. The Setup (Granting Access)

Because it's a personal account, the person who owns the account (`nagameTW`) needs to invite the coworker as a direct collaborator.

1. The owner goes to the repository on GitHub.
    
2. Clicks **Settings** (the gear icon at the top).
    
3. On the left sidebar, clicks **Collaborators**.
    
4. Clicks the green **Add people** button.
    
5. Types in the coworker's GitHub username or email and sends the invite.
    

> ⚠️ **Important:** Your coworker will receive an email and a notification on GitHub. They **must accept the invitation** before they can push any code!

### 2. The Workflow

Once they accept the invite, they treat it exactly like Scenario A. They don't need to fork it.

Bash

```
# 1. Clone the original repo directly
git clone git@github.com:nagameTW/otex-claw.git

# 2. Create a feature branch
cd otex-claw
git checkout -b feature/onboarding-setup

# 3. (Make changes, git add, git commit...)

# 4. Push the branch directly back to the original repo
git push origin feature/onboarding-setup
```

After pushing, they go to `[github.com/nagameTW/otex-claw](https://github.com/nagameTW/otex-claw)` and they will see a button to open a Pull Request.

### 💡 An "Industry Standard" Reality Check

While using a personal account works perfectly fine for small teams, side projects, or early-stage startups, the **industry standard** for a business is to use a **GitHub Organization**.

If this repo is critical for your company's daily operations, keeping it under a personal account introduces a few risks:

- **The "Bus Factor":** If the account owner leaves the company or loses access to their account, the company loses control of the repository.
    
- **Permission Chaos:** Managing access person-by-person gets messy quickly as the team grows.
    

Moving a repository to a free GitHub Organization takes about two minutes and allows you to manage permissions as a team, rather than relying on one person's account.

Is this repo just a temporary tool you guys are using for onboarding, or is it a core project that your team will be building on long-term?

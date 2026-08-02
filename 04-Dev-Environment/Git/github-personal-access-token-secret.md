---
title: "GitHub Personal Access Token Secret for PR Automation"
description: "Shows when a GitHub PAT or App token can bypass GITHUB_TOKEN limits for pull request automation."
created: 2026-08-02
updated: 2026-08-02
tags: [dev, git]
type: howto
lang: en
status: draft
---

> Related: [[MOC - Dev Environment]] · [[github-mark-pull-request-ready-for-review]] · [[github-actions-sensitive-patterns]]

# GitHub Personal Access Token Secret for PR Automation

That AI suggestion is **spot on**.

While granting permissions in YAML usually works, `GITHUB_TOKEN` frequently hits a wall on `markPullRequestReadyForReview` under three common scenarios:

1. **The PR is from a fork:** GitHub automatically strips write permissions from `GITHUB_TOKEN` on fork-created PRs for security.
    
2. **Organization-level policies:** Your GitHub Org settings might explicitly block `GITHUB_TOKEN` from performing GraphQL mutations or modifying PR states.
    
3. **Branch protection rules:** The target branch might restrict PR modifications to specific users or apps.
    

Using a custom **Personal Access Token (PAT)** or a **GitHub App token** can bypass these `GITHUB_TOKEN` limitations.

## How to Verify It (Quick PAT Test)

The fastest way to test if `GITHUB_TOKEN` restrictions are the culprit is to temporarily swap in a Personal Access Token (PAT).

### Step 1: Create a Personal Access Token

1. Go to your GitHub profile **Settings** -> **Developer settings** -> **Personal access tokens** -> **Fine-grained tokens** (or Tokens Classic).
    
2. Click **Generate new token**.
    
3. Select your repository under **Repository access**.
    
4. Set the following permissions:
    
    - **Pull requests:** Read and write
        
    - **Contents:** Read-only
        
5. Generate and copy the token.
    

### Step 2: Add the Token to Repository Secrets

1. Go to your repository's **Settings** -> **Secrets and variables** -> **Actions**.
    
2. Click **New repository secret**.
    
3. Name it `PAT_TOKEN` and paste your generated token.
    

### Step 3: Update Your Workflow File

Update the step in your `.github/workflows/` file to use a repository secret instead of the default `GITHUB_TOKEN`:

```yaml
- name: Mark PR ready for review
  env:
    GH_TOKEN: ${{ secrets.PAT_TOKEN }}  # Swapped from GITHUB_TOKEN
    PR_NUMBER: ${{ github.event.pull_request.number }}
    GH_REPO: ${{ github.repository }}
  run: |
    gh pr ready "$PR_NUMBER" --repo "$GH_REPO"
```

### Step 4: Re-run the Workflow

Trigger or rerun the failed GitHub Action:

- **If it succeeds:** You have confirmed that `GITHUB_TOKEN` permission restrictions were the issue.
    
- **If it fails with a new error:** Look at the exact output. It will tell you if the PAT is missing a specific scope or if a branch rule is blocking it.
    

## Next Steps: Production Best Practice

If the PAT test works:

- **For personal/solo repos:** Keeping the PAT in Repository Secrets is fine.
    
- **For team/organization repos:** Switch from a PAT to a **GitHub App Token** (using actions like `actions/create-github-app-token`). PATs are tied to individual user accounts (and break if that person leaves the team), whereas a GitHub App belongs to the org itself.


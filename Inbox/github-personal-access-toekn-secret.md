---
created: 2026-08-02 12:08
updated: 2026-08-02 12:08
tags: []
type: reference
lang: en
status: draft
---
That AI suggestion is **spot on**.

While granting permissions in YAML usually works, `GITHUB_TOKEN` frequently hits a wall on `markPullRequestReadyForReview` under three common scenarios:

1. **The PR is from a fork:** GitHub automatically strips write permissions from `GITHUB_TOKEN` on fork-created PRs for security.
    
2. **Organization-level policies:** Your GitHub Org settings might explicitly block `GITHUB_TOKEN` from performing GraphQL mutations or modifying PR states.
    
3. **Branch protection rules:** The target branch might restrict PR modifications to specific users or apps.
    

Using a custom **Personal Access Token (PAT)** or a **GitHub App token** bypasses these `GITHUB_TOKEN` limitations entirely.

## How to Verify It (Quick PAT Test)

The fastest way to test if `GITHUB_TOKEN` restrictions are the culprit is to temporarily swap in a Personal Access Token (PAT).

### Step 1: Create a Personal Access Token

1. Go to your GitHub profile **Settings** $\rightarrow$ **Developer settings** $\rightarrow$ **Personal access tokens** $\rightarrow$ **Fine-grained tokens** (or Tokens Classic).
    
2. Click **Generate new token**.
    
3. Select your repository under **Repository access**.
    
4. Set the following permissions:
    
    - **Pull requests:** Read and write
        
    - **Contents:** Read-only
        
5. Generate and copy the token.
    

### Step 2: Add the Token to Repository Secrets

1. Go to your repository's **Settings** $\rightarrow$ **Secrets and variables** $\rightarrow$ **Actions**.
    
2. Click **New repository secret**.
    
3. Name it `PAT_TOKEN` and paste your generated token.
    

### Step 3: Update Your Workflow File

Update the step in your `.github/workflows/` file to use `secrets.PAT_TOKEN` instead of the default `GITHUB_TOKEN`:

YAML

```
- name: Mark PR ready for review
  env:
    GH_TOKEN: ${{ secrets.PAT_TOKEN }}  # Swapped from GITHUB_TOKEN
    PR_NUMBER: ${{ github.event.pull_request.number }}
    GH_REPO: ${{ github.repository }}
  run: |
    gh pr ready "$PR_NUMBER" --repo "$GH_REPO"
```

### Step 4: Re-run the Workflow

Trigger or re-run the failed GitHub Action:

- **If it succeeds:** You’ve confirmed that `GITHUB_TOKEN` permission restrictions were indeed the issue.
    
- **If it fails with a new error:** Look at the exact output—it will tell you if the PAT is missing a specific scope or if a branch rule is blocking it.
    

## Next Steps: Production Best Practice

If the PAT test works:

- **For personal/solo repos:** Keeping the PAT in Repository Secrets is fine.
    
- **For team/organization repos:** Switch from a PAT to a **GitHub App Token** (using actions like `actions/create-github-app-token`). PATs are tied to individual user accounts (and break if that person leaves the team), whereas a GitHub App belongs to the org itself.


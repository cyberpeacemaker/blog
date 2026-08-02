---
created: 2026-08-02 12:08
updated: 2026-08-02 12:08
tags: []
type: reference
lang: en
status: draft
---
## Cause of the Error

The error `GraphQL: Resource not accessible by integration (markPullRequestReadyForReview)` occurs because the default `GITHUB_TOKEN` running the workflow lacks **write permissions** to modify Pull Requests, or repository-level security settings are blocking Actions from altering PR states.

## How to Fix It

### Solution 1: Grant `pull-requests: write` in your Workflow YAML

In your workflow file (located in `.github/workflows/`), explicitly grant the workflow job write access to pull requests.

Add the `permissions` block to your job (or top-level workflow file):

YAML

```
jobs:
  mark-pr-ready:
    runs-on: ubuntu-latest
    permissions:
      pull-requests: write
      contents: read
    steps:
      - name: Mark PR ready for review
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          PR_NUMBER: ${{ github.event.pull_request.number }}
          GH_REPO: ${{ github.repository }}
        run: |
          gh pr ready "$PR_NUMBER" --repo "$GH_REPO"
```

> **Important:** Ensure `GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}` is defined under `env` for the step so the `gh` CLI receives proper authentication credentials.

### Solution 2: Update Repository Workflow Permissions

If your organization or repository defaults override individual workflow permissions, adjust the repository settings:

1. Open your repository on GitHub.
    
2. Go to **Settings** $\rightarrow$ **Actions** $\rightarrow$ **General**.
    
3. Scroll down to the **Workflow permissions** section:
    
    - Select **Read and write permissions**.
        
    - Check **Allow GitHub Actions to create and approve pull requests**.
        
4. Click **Save**.
    

### Solution 3: Account for Forked Repository Pull Requests

If this workflow triggers on PRs originating from a **forked repository**:

- GitHub automatically forces `GITHUB_TOKEN` to **read-only** mode for safety reasons.
    
- **Fix:** Change the trigger event from `pull_request` to `pull_request_target` (which runs in the base repository context with write access), or pass a dedicated **Personal Access Token (PAT)** / **GitHub App token** via repository Secrets.


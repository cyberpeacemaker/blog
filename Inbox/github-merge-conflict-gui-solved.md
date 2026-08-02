---
title: "Resolve GitHub Merge Conflicts in the Web UI"
description: "Explains how to keep the current branch changes when resolving a GitHub pull request merge conflict in the browser."
created: 2026-08-02
updated: 2026-08-02
tags: [dev, git]
type: howto
lang: en
status: draft
---

> Related: [[MOC - Dev Environment]] · [[github-collaboration-pr-loop]] · [[automation-pr-merge-policy]]

# Resolve GitHub Merge Conflicts in the Web UI

To keep the **Current change**, follow these quick steps directly in the GitHub web interface:

## How to Fix

1. **Accept the Change**
    
    Click the blue **`Accept current change`** link located directly above the conflict marker. This keeps the current branch content and removes the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`) along with the incoming code.
    
2. **Mark as Resolved**
    
    Click the gray **`Mark as resolved`** button in the top-right corner of the editor.
    
3. **Commit Merge**
    
    Click the green **`Commit merge`** button that appears to finalize the resolution.
    

> Why this choice is correct:
>
> The **Current change** adds helpful safety checks: it validates the `GH_TOKEN` secret and marks draft PRs as ready before attempting to merge. The incoming change from `main` skips those extra checks.


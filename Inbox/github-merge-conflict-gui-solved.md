---
created: 2026-08-02 12:08
updated: 2026-08-02 12:08
tags: []
type: reference
lang: en
status: draft
---
To keep the **Current change**, follow these quick steps directly in the GitHub web interface:

## How to Fix

1. **Accept the Change**
    
    Click the blue **`Accept current change`** link located directly above line 29 (just above `<<<<<<< cursor/inbox-rule-application-1379`). This will automatically keep the new code and remove the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`) along with the incoming code.
    
2. **Mark as Resolved**
    
    Click the gray **`Mark as resolved`** button in the top-right corner of the editor.
    
3. **Commit Merge**
    
    Click the green **`Commit merge`** button that appears to finalize the resolution.
    

> **Why your choice is correct:**
> 
> The **Current change** adds helpful safety checks—it validates your `GH_TOKEN` secret and marks draft PRs as ready before attempting to merge. The incoming change from `main` skips those extra checks.


---
created: 2026-07-16 20:07
updated: 2026-07-16 20:07
tags: []
type: reference
lang: en
status: draft
---
Organizing your `TODO`s is a classic developer dilemma. The short answer: **it depends on the scale of the task, but generally, a hybrid approach works best.**

If you scatter `TODO.md` files in every single subfolder, you'll likely forget they exist. But if you put _every single micro-task_ in a root-level file, it becomes a cluttered mess.

Here is a breakdown of how to decide where your tasks should live.

## Root vs. Localized: The Trade-offs

|**Strategy**|**Best For**|**Pros**|**Cons**|
|---|---|---|---|
|**Root Level** (`/TODO.md` or PM Board)|High-level features, milestones, and project-wide tasks.|• Single source of truth<br><br>  <br><br>• Great for a birds-eye view<br><br>  <br><br>• Hard to lose track of|• Easily gets cluttered<br><br>  <br><br>• Lacks immediate code context|
|**Localized** (In-folder or inline comments)|Micro-tasks, refactoring, and file-specific fixes.|• High context (right where the code is)<br><br>  <br><br>• Stays with the git history of that feature|• Hard to track without search tools<br><br>  <br><br>• "Out of sight, out of mind"|

## The Best-Practice Strategy (The Hybrid Approach)

To get the best of both worlds, divide your `TODO`s by **scope** rather than choosing just one method.

### 1. Use the Root for "The What" (High-Level)

Keep a single `TODO.md` (or a Kanban board/GitHub Issues) at the **root** of your project. This should act as your roadmap.

- **What goes here:** "Implement OAuth2 authentication," "Set up CI/CD pipeline," or "Refactor the database layer."
    
- **Why:** Anyone opening your project can immediately see the major remaining milestones.
    

### 2. Use Co-located Inline Comments for "The How" (Low-Level)

For file-specific or folder-specific tasks, place them **directly inside the code** as comments (e.g., `// TODO: Optimize this query`) in the specific files.

- **What goes here:** "Fix edge case for null inputs," "Rename this variable later," or "Clean up this helper function."
    
- **Why:** Modern IDEs (like VS Code or WebStorm) have built-in "TODO tree" extensions that automatically scan your codebase and aggregate these localized comments into a single neat list for you.
    

> **The Golden Rule:**
> 
> If a task requires looking at a specific file to understand _why_ it needs to be done, keep it in that file. If it’s a milestone that defines the project's progress, keep it at the root.

To help tailor this, what kind of project are you currently building (e.g., a solo web app, a multi-package monorepo), and are you tracking these via `.md` files or inline code comments?


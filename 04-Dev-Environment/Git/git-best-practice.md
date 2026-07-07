---
created: 2026-05-27
tags: [dev, git]
type: reference
lang: en
status: draft
---

**The Solo Developer's Dilemma**
When you first learn Git, the workflow is usually simple: write code, commit to `main`, and push. When you are the only one working on a project, this feels fast and efficient. But as your project grows, this "always on main" habit becomes a dangerous trap.

**Why is working directly on Main a bad idea?**
Think of the `main` branch as your production server. It should always be perfectly stable, deployable, and bug-free.

* **Lack of Isolation:** If you are halfway through building a massive new feature on `main` and suddenly discover a critical bug in production, you are stuck. You can't fix and push the bug without also pushing your half-finished, broken feature.
* **Fear of Experimentation:** Trying out a risky new idea is stressful when it immediately overrides your working code. If the experiment fails, untangling those bad commits from `main` is a massive headache.

**The Solution: Feature Branching**
The industry standard for version control is the Feature Branch workflow. Instead of building the car engine while driving down the highway, you pull into the garage.

**How it works (and when to use it):**

* **Every new task gets a branch:** Whether it is a tiny typo fix (`bugfix/header-typo`) or a huge database migration (`feature/new-database`), you branch off from `main`.
* **The Pull Request (PR):** Once your work on the branch is done, you don't just shove it back into `main`. You open a Pull Request. A PR is a formal request to merge your code. In teams, this is where code review happens. For solo devs, it gives you a beautiful side-by-side comparison of exactly what lines of code you changed before you finalize it.
* **Keep Main Pristine:** Your `main` branch only ever receives completed, reviewed, and fully functional code.

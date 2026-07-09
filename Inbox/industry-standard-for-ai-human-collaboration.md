---
created: 2026-07-09 09:07
tags: []
type: reference
lang:
status: draft
---
## The Industry Standard for AI & Human Collaboration

When working with autonomous AI agents, letting them write directly to a live local repository or a production branch is a recipe for chaos (often called the "vibe-coding trap," where an unmonitored AI accidentally breaks three things while trying to fix one).

The industry-standard ("edge") workflow for collaborating with AI agents centers around **decoupled execution and automated guardrails**:

### 1. The "Draft PR" Loop (The Gold Standard)

The most common industrial standard is to let the AI operate exactly like a junior developer:

- You trigger the automation (either via Cursor, Slack, or a GitHub event).
    
- The AI spins up its own branch, handles the task, runs your local test suite to ensure the build isn't broken, and **automatically opens a Draft Pull Request (PR)** on your remote repository (e.g., GitHub).
    
- This keeps your local workspace perfectly clean and allows you to review the AI's diff asynchronously via a code review platform before merging it.
    

### 2. Plan Mode Over Blind Execution

For complex tasks, industrial workflows enforce a "Plan-First" architecture. The AI is instructed to generate a Markdown text plan detailing exactly _which_ files it intends to change and _why_. It saves this plan (e.g., in `.cursor/plans/`), waits for human approval, and only begins writing code once a human clears the plan.

### 3. Git Discipline & Atomic Commits

If you _do_ use AI tools locally, the best practice is to use automatic staging or frequent micro-commits. If an agent runs through a multi-step task and goes completely off the rails on step 7, having atomic commits from steps 1 through 6 means you can instantly roll back the mistake without losing the useful work.

What kind of tasks are you planning to hand off to this automation next—are you building out code features, or focusing primarily on repository maintenance like the triage workflow in `image_57b224.jpg`?


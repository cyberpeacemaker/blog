---
created: 2026-05-21
tags: [ai, agents]
type: reference
lang: en
status: draft
---

In AI developer tools (like VS Code Copilot, Cursor, or similar agentic IDEs), **"Steer with Message"** is a course-correction feature that allows you to redirect an autonomous AI agent mid-execution.

When an agent is running a multi-step task—as indicated by the **"Working"** status in your screenshot—the standard "Send" button changes into a dynamic action dropdown (`↑ ∨`).

---

### How it Works

If you type a prompt and choose **Steer with Message**, the interface instructs the agent to pause and listen to you:

1. **Yields Control:** The agent completes its *current* micro-task or tool execution (e.g., finishes reading the specific file it is currently looking at) and then pauses.
2. **Injects New Context:** The agent reads your new message immediately.
3. **Redirects Path:** It pivots and adjusts its upcoming actions based on your feedback, rather than continuing down its original path.

### Why it's Useful (Context from your Screenshot)

In your specific scenario, the agent is actively working on recreating `PLAN.md`. However, you have already manually copied it over.

If you didn't have this feature, your options would be to let it run (wasting time/tokens and potentially overwriting your work) or completely hard-cancel the run (which might wipe out other good progress the agent just made).

By using **Steer with Message**, you essentially tap the agent on the shoulder mid-task, say *"Hey, skip this file and move to the next step,"* and it will immediately course-correct without losing its current workflow state.

---

### Alternative Actions in that Dropdown

If you click the downward chevron (`⋁`) next to that arrow, you will typically see three options for handling a message while an agent is running:

* **Steer with Message:** Pauses the agent after its current tool action to process your new instructions immediately.
* **Add to Queue:** Appends your message to a waitlist; the agent finishes its entire current plan uninterrupted, then reads your message right after.
* **Stop and Send:** Hard-cancels the agent's current request entirely and fires off your new message instantly.
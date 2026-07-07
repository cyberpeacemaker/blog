---
created: 2026-06-09
tags: [ai, agents, claude]
type: reference
lang: en
status: draft
---

In **Claude Code**, commands (specifically called **Slash Commands**) are the primary tools you use to control the AI's behavior, manage your token budget, and direct the engineering workflow right from your terminal.

Just like typing `/` inside Discord, Slack, or Notion, typing `/` in Claude Code brings up a built-in interactive menu.

Here is a breakdown of how they work, the essential commands you must master, and how to create your own.

---

### The "Must-Know" Core Commands 🧰

While there are over 50 built-in commands, a few are critical for managing large codebases and saving token costs:

#### 1. The Context Lifesavers (`/compact` and `/clear`)

* **`/compact`**: When a long coding session starts pushing your context window limits, `/compact` compresses your chat history into a dense summary. You can even guide it: `/compact Focus on the authentication bug`.
* **`/clear`**: Wipes the chat history entirely and frees up all tokens. Use this when you are entirely done with one task and switching to something brand new.

#### 2. Workflow & Experimentation (`/plan` and `/branch`)

* **`/plan`**: Puts Claude into a **read-only mode**. It can scan files and analyze code, but it cannot make any changes. It forces Claude to present a detailed architecture report before touching a single line of code. (You can also toggle this via `Shift+Tab`).
* **`/branch`** (formerly `/fork`): Creates a conversational branch at the exact current moment. If you aren't sure if an approach will work, you can `/branch`, try it out, and if it fails, safely resume your main session without losing your progress.
* **`/rewind`**: Rolls back your conversation and/or file changes to a previous checkpoint. It's like time-travel debugging for your chat.

#### 3. Quick Asides (`/btw`)

* **`/btw <your question>`**: Allows you to ask a quick, temporary question while Claude is in the middle of a task (e.g., `/btw What does this bash flag do again?`). It answers you without bloat-injecting that random question into the permanent history of your main coding project.

---

### Creating Custom Commands 🛠️

You don't have to rely only on the built-in commands. You can create your own custom slash commands by simply adding markdown files into a specific folder in your project: `.claude/commands/`.

The filename becomes the command, and the contents tell Claude what to do. You can even use **argument placeholders** (`$0`, `$1`).

#### Example: `.claude/commands/fix-bug.md`

```markdown
---
argument-hint: [issue-number] [priority]
description: Prepares a target environment to address a known bug repository issue.
---

Locate the code related to issue #$0. 
Analyze the failure vectors with priority scale $1.
Before making changes, print your proposed fix layout.

```

Once saved, typing `/fix-bug 104 high` in your terminal will immediately trigger this command, automatically mapping `104` to `$0` and `high` to `$1`.

---

### Custom Commands vs. Custom Skills: The Difference

Since you already know about skills, it's easy to get these mixed up. Here is the golden rule for choosing between them:

* **Custom Slash Commands (`.claude/commands/`)**: Ideal for simple, repetitive prompts or shortcuts where you *always* want to trigger them manually via the `/` menu.
* **Custom Skills (`.claude/skills/`)**: Ideal for highly complex behaviors, automation scripts, and workflows. They support multi-file tracking (`SKILL.md` + reference folders) and can be triggered **automatically** by Claude when it reads your intent, rather than forcing you to type the command every time.
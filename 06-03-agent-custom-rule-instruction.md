### How to Set Up Rules in Claude Code

Claude Code uses plain markdown files to inject persistent context and rules into the agent's system prompt before it starts a session.

* **`CLAUDE.md` (Project Level):** You can place a `CLAUDE.md` file in the root of your repository (or inside a `.claude/` folder to keep the root clean). Claude reads this file at the start of every session. It is the perfect place to define framework choices, testing commands, architectural patterns, and code style.
* **Path-Scoped Rules (`.claude/rules/*.md`):** Anthropic recommends keeping your `CLAUDE.md` file under 200–300 lines so it doesn't eat up the context window. If you have extensive rules, you can place topic-specific or path-gated instructions inside the `.claude/rules/` directory. Claude will only load these rules when working on relevant files.
* **Global Instructions (`~/.claude/CLAUDE.md`):** If you have personal developer preferences (e.g., "always use `yarn` instead of `npm`" or "always write commit messages in lowercase") that you want applied to *every* project on your machine, you can define them in your global configuration directory.
* **Auto Memory:** As a bonus, Claude Code also has a self-writing feature. If you correct the agent during a session, it will automatically take notes and save them to its memory files so it doesn't make the same mistake next time.

> **Pro Tip:** You can run the `/init` command inside Claude Code to have the agent analyze your codebase and automatically generate a starter `CLAUDE.md` file for you based on the conventions it detects.

---

### What Are These Features Usually Called?

While `.cursorrules` and `CLAUDE.md` are product-specific file names, the AI and developer tooling industry generally refers to this concept using a few interchangeable terms:

| Term | Context |
| --- | --- |
| **Custom Instructions** | The most universally recognized term (popularized by ChatGPT) for user-defined guidelines that persist across all conversations. |
| **Project Rules / Agent Rules** | The standard term used in the context of AI coding assistants (like Cursor, Copilot, or Windsurf) to describe repository-level coding standards. |
| **System Prompts / System Instructions** | The technical, backend term for the foundational prompt that dictates an LLM's persona, constraints, and behavior before the user even types a message. |
| **Persistent Context** | A broader term used in agentic development to describe files, memories, or documents that automatically load into the AI's context window on launch. |
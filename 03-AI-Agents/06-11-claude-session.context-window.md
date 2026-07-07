This screenshot shows the detailed token breakdown of your **Claude Code** (or a compatible IDE extension like Damocles) session.

In short: **Your conversation has completely run out of room, and Claude is now in a "critical" state where it has to juggle what it can remember.**

## 1. The Red Alert: Context Window Overfilled

* **`213.9k / 200.0k (100%)`**
The model you are using has a maximum limit of **200,000 tokens** per turn. Your current session has reached **213.9k tokens**. Because you are at $100\%+$ capacity, the conversation is effectively "bloated," and performance or memory will begin to degrade.

## 2. Where the Tokens Are Going (The Breakdown)

The list shows exactly what is taking up space in Claude's active memory right now:

* **`Messages (234.3k · 117.2%)`:** This is your actual chat history (your prompts and Claude’s responses). It is taking up **more than the entire allowed context window by itself**.
* **`System tools` & `MCP tools` (Active):** These are the definitions and code schemas for tools Claude can actively use right now (like reading files, running bash commands, or searching).
* **`Skills` & `System prompt`:** These are the background instructions telling Claude how to behave and any custom development rules you've set up.

---

### What does "(deferred)" mean?

You will notice things like **`MCP tools (deferred)`** and **`System tools (deferred)`** taking up 0% of the active budget.

Claude Code uses an optimization feature called **Tool Search**. Instead of cramming the heavy code schemas of *every single tool* you have installed into the context window at once, it "defers" them. It only keeps their names on hand and will dynamically fetch the full tool definition only when it actually needs to use it. This is saving you from a much worse overflow!

---

## 3. How to Fix This

Because your `Messages` history is so massive, Claude is being forced to drop older parts of the conversation to keep up. To get back into a healthy state, try these steps:

* **Start a fresh session:** This is the most effective fix. If you have finished your current task, exit the terminal/chat and start a new one. This clears the massive `Messages` log.
* **Keep your `CLAUDE.md` or project rules lean:** Make sure your custom instructions aren't unnecessarily wordy.
* **Audit your MCP Servers:** If you have background tools or servers connected that you aren't using, type `/mcp` in your session and disconnect the ones you don't need. Every active tool eats up a little bit of your starting token budget.
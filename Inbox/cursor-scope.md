---
created: 2026-07-25 09:07
updated: 2026-07-25 09:07
tags: []
type: reference
lang: en
status: draft
---
Your mental model is mostly right. Here is how scope actually works in this session.

## Primary scope: this workspace

The active project is:

`C:\Users\ydnaa\Documents\Github\nics-ta-ics-cyber-range`

By default I work here:

- Read / edit / search files in this repo
- Follow this repo’s rules (e.g. `CLAUDE.md`, `.cursor/rules/`)
- Run terminal commands with this folder as the working directory
- Use project-specific MCP/config wired to this workspace

I do **not** automatically see other repos’ files, rules, or guides unless you open them, point me at them, or I explicitly read them via shell.

## Also in scope (Cursor-global / user-level)

Some things live outside the repo but are intentionally available:

| Area | Examples |
|------|----------|
| **User rules** | Rules you set in Cursor settings — injected into every chat |
| **Agent skills** | e.g. `C:\Users\ydnaa\.cursor\skills-cursor\` |
| **Cursor user settings** | Via the update-settings skill — `settings.json`, themes, format-on-save, etc. |
| **This chat’s project metadata** | e.g. agent transcripts for this project under `.cursor\projects\...` |
| **Plugins/skills cache** | e.g. GSAP skills under `.cursor\plugins\cache\` |

So yes: I can reach **Cursor global/user config** and **this project**, as you expected.

## Not in scope (unless you ask)

- Other repos under `Documents\Github\...` — not loaded by default
- Their `.cursor/rules`, `AGENTS.md`, `CLAUDE.md`, etc. — not applied unless that folder is the workspace or you give a path
- Other projects’ git history, env files, secrets — I won’t stumble on them through normal search/read

## One caveat: the terminal

Shell is not strictly sandboxed to this repo. With normal OS permissions I *could* `cd` elsewhere or read an absolute path if you ask — or if a task clearly requires it (e.g. “edit my global gitconfig”).

I won’t browse other repos on my own. If you want strict isolation, say so and I’ll stay within this workspace path unless you explicitly override.

---

**Summary:** Default scope = **this repo + Cursor user config/skills/rules**. Other repos stay out of the picture unless you open them or tell me to touch a specific path outside the workspace.

If you want, we can define a hard rule like: “never read or write outside `nics-ta-ics-cyber-range` except `settings.json`” — I can follow that for this project.


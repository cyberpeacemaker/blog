---
created: 2026-07-22 10:07
updated: 2026-07-22 10:07
tags: []
type: reference
lang: en
status: draft
---
  
  

## 2. Industry Architecture: How Teams Set This Up

  

In production environments, teams split responsibility between **In-Repo Artifacts** (shared by everyone) and **Agent-Side Capabilities** (developer environment).

  

```

                     ┌──────────────────────────────────────────────┐

                     │          DEVELOPER ENVIRONMENT               │

                     │  - CLI Authentications (gh auth login)       │

                     │  - MCP Servers (DBs, Jira, Figma APIs)       │

                     └──────────────────────┬───────────────────────┘

                                            │ Loads tools

                                            ▼

┌──────────────────────────────────────────────────────────────────────────────────┐

│                             GIT REPOSITORY (IN-REPO)                             │

│                                                                                  │

│   ├── CLAUDE.md                      <-- Global repo rules & build commands      │

│   │                                                                              │

│   ├── .claude/skills/                <-- Team-shared AI Workflows                │

│   │   └── create-pr/                                                             │

│   │       ├── SKILL.md               <-- When & how agent should act             │

│   │       ├── scripts/create-pr.sh   <-- Deterministic bash/python code          │

│   │       └── assets/template.md     <-- PR / Issue formatting templates         │

│   │                                                                              │

│   └── .github/PULL_REQUEST_TEMPLATE.md                                           │

└──────────────────────────────────────────────────────────────────────────────────┘

  

```

  

### Layer A: In-Repo (Tracked in Git)

  

This ensures every developer (and every AI agent joining the project) uses the exact same conventions without manual configuration.

  

* **Repository Instructions (`CLAUDE.md` / `.cursor/rules`):** Defines root rules like *"Always run `npm test` before committing"* or *"Use TypeScript strict mode."*

* **Skills Folders (`.claude/skills/<skill-name>/`):**

* `SKILL.md`: Frontmatter declaring triggers (e.g., *"Use when the user asks to open a PR"*) + instructions.

* `scripts/`: Deterministic Bash or Python code that the agent executes.

* `assets/`: Templates (Markdown forms, issue structures).

  
  
  

### Layer B: Agent / Environment-Side (Local Machine / CI)

  

This supplies the agent with **raw power and connectivity** (the "kitchen tools"), while the in-repo skills provide the "recipes".

  

* **Authenticated CLIs:** Tools like `gh`, `docker`, `aws`, or `kubectl` installed on the host OS with valid credentials.

* **MCP (Model Context Protocol) Servers:** Global plugins that connect the agent to external systems like PostgreSQL databases, Slack, Jira, or Sentry.

  

---

  

## The "MCP vs. Skill" Distinction

  

A common point of confusion is how **MCP** fits into this:

  

* **MCP (Model Context Protocol) = Capability / Connectivity:** Gives the AI the *tool* to perform actions (e.g., *"I can query your production database"* or *"I can call the GitHub API"*).

* **Skill = Workflow / Knowledge:** Teaches the AI *how and when* to use those capabilities safely (e.g., *"Before running a DB migration via MCP, check if backups exist, ask for user confirmation, and run `./scripts/migrate.sh`"*).

  

By pairing **In-Repo Skills + Scripts** with **Agent-Side MCP Tools**, you get an AI assistant that behaves consistently across your entire team.


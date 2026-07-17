---
title: "Frontmatter Template Suggestions for OKF"
description: "Connects lightweight documentation frontmatter with OKF-style Markdown for AI-readable knowledge repositories."
created: 2026-07-17
updated: 2026-07-17
type: reference
lang: en
status: draft
tags: [meta, ai]
---

> Related: [[frontmatter-schema]] · [[yaml-okf]] · [[MOC - AI Agents]]
Short answer: **Absolutely, yes.**

If you are managing multiple projects with growing documentation, enforcing a frontmatter template is one of the best preventative measures against "doc rot" (where documents go to die and nobody knows who wrote them, why they exist, or if they are still relevant).

However, there is a fine line between **helpful structure** and **developer-annoying bureaucracy**. If you make the template too long, people will either stop writing docs or just fill them with gibberish to get past the linting.

Here is a breakdown of why you should do this, a "Goldilocks" template to start with, and how to make it painless for your team.

## Why Frontmatter is a Game-Changer

- **Instant Context:** Anyone opening the file immediately knows the doc's status, who to ask questions (ownership), and when it was last relevant.
    
- **Programmatic Power:** If you ever want to build a internal developer portal, a custom docs site (using Astro, Docusaurus, or Next.js), or even just write a quick script to find all "deprecated" docs, frontmatter makes your Markdown files queryable like a database.
    
- **Searchability:** Standardized tags make searching through a massive repository infinitely easier than relying on full-text search alone.
    

## The "Goldilocks" Frontmatter Template

Keep it to the bare essentials. If it takes more than 10 seconds to fill out, it's too long.

YAML

```
---
title: "Clear, Searchable Title"
status: "draft | active | deprecated" # Helps identify stale docs
author: "@github_username"          # Who to ping for updates
created: 2026-07-17                 # Helps track document age
tags: [architecture, setup, api]    # Quick categorizers
---
```

> 💡 **Pro-Tip:** Avoid fields that require manual, frequent updates (like `last_modified`). Version control (Git) already tracks file history perfectly. Only include metadata that Git _doesn't_ capture well.

## How to Enforce It Without Being a Tyrant

If you just ask people to do it, they will forget. Instead, lower the friction to zero:

1. **IDE Snippets:** Create a shared VS Code snippet workspace configuration. Typing `front` should instantly autocomplete the template.
    
2. **Use a Generator:** If you use tools like `hygen` or `plop` for scaffolding components, add a `npm run gen:doc` command that asks three quick questions in the CLI and outputs the formatted `.md` file.
    
3. **Git Hooks / Linters:** If you want to get serious, you can use a linter (like `markdownlint` or a custom pre-commit hook) that fails the commit if a new `.md` file doesn't start with `---`. (Maybe save this step for when the habit is already partially established!).
    

What kind of projects are you building, and where do these docs usually live (e.g., GitHub wikis, a monorepo, or a dedicated docs site)?

---

## Git vs. Frontmatter: Do You Still Need "Author" and "Created"?

If you are already using Git, you can absolutely streamline these fields. However, there is a subtle difference between **Git metadata** (system-level history) and **Document metadata** (logical intent):

- **Author $\rightarrow$ Change to `owner`:** Git tracks who _committed_ a line, but this is often misleading. The person who last fixed a typo or ran a linter is technically the "author" in Git history, but they are not the Subject Matter Expert (SME). Changing this field to `owner` (or `maintainer`) explicitly tells both humans and AI agents who actually _owns_ the knowledge today.
    
- **Created $\rightarrow$ Drop it:** Git is exceptionally good at tracking file creation. You can safely drop this field unless you are building a public blog or changelog that strictly requires creation dates for frontend rendering.
    

## Supercharging Your Docs for AI Agents

Since your team collaborates heavily with AI agents, your frontmatter is no longer just for human eyes—it is an ingestion layer for your LLM context windows or RAG (Retrieval-Augmented Generation) pipelines.

To make your documentation incredibly "agent-friendly," consider adding these keys to your template:

- **`type`**: (e.g., `architecture-decision`, `onboarding`, `api-spec`, `troubleshooting`). Agents behave significantly better when they know the _genre_ of the document they are parsing.
    
- **`description`**: A highly concise, one-sentence summary. AI search tools (like semantic search) use this description field to quickly weigh the relevance of a document before grabbing the whole file.
    
- **`verified`**: (e.g., `verified: true` or `verified_by: @human`). Since you work with AI, it's vital to avoid "hallucination loops" (where an AI reads inaccurate AI-generated code or docs). This tells the agent if a human has vetted the information.
    
- **`context_scope`**: (e.g., `frontend`, `billing-service`). This helps the AI narrow down exactly which boundary of your system this file belongs to.
    

## What is the Open Knowledge Format (OKF)?

The **Open Knowledge Format (OKF)** is highly relevant to what you are building. Formalized as an open, vendor-neutral specification (v0.1), OKF is designed to standardize the **"LLM-wiki" pattern**.

OKF is a minimal standard for storing organizational knowledge as a directory of Markdown files with YAML frontmatter. It is designed to be authored by humans, generated by agents, and seamlessly consumed by both.

### The OKF Frontmatter Standard

Under the OKF specification, the **only required field** in the frontmatter is `type`.

An OKF-compliant frontmatter block looks like this:

YAML

```
---
type: "guide"                      # Required: The concept category
title: "Setting up Postgres"       # Optional: Fallback is the filename
description: "How to spin up DB." # Optional: 1-sentence summary
resource: "db://postgres-prod"     # Optional: URI of the asset being described
tags: [database, setup]            # Optional: Categorization
timestamp: 2026-07-17T14:47:00Z    # Optional: ISO 8601 of last meaningful change
---
```

### How OKF Can "Boot" Your Workflow

Adopting OKF (or a lightweight version of it) gives your projects major advantages:

1. **Semantic Graph Building:** OKF standardizes absolute, bundle-relative markdown linking (e.g., `/database/postgres.md` instead of guessing relative paths). This allows your AI agents to parse the folder and immediately map out a graph showing how your documents relate to each other.
    
2. **Zero Lock-In:** Because it relies entirely on plaintext and simple directory nesting, you are not tied to proprietary platforms.
    
3. **Agent Compatibility:** Future AI orchestration tools are moving toward supporting OKF natively to index and query local directories. By structuring your frontmatter this way now, your docs will be immediately ingestion-ready.
    

Are your AI agents currently using a custom RAG or vector-database pipeline to search these docs, or are they reading the repository files directly via standard editor context windows (like GitHub Copilot or Cursor)?
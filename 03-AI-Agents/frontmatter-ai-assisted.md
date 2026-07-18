---
title: "AI-Assisted Documentation Frontmatter Rules"
description: "Explains how Cursor rules and CLAUDE.md can enforce documentation frontmatter in AI-assisted engineering workflows."
created: 2026-07-17
updated: 2026-07-17
type: howto
lang: en
status: draft
tags: [ai, cursor]
---

> Related: [[MOC - AI Agents]] · [[MOC - Claude & Cursor]] · [[CLAUDE]]
In the modern AI-assisted engineering stack, **your documentation rules should live directly inside your project repository.** This is often called a "Git-First" or "In-Repo" context strategy.

Because you are primarily using **Cursor** and **Claude**, you have a massive advantage: both of these tools are designed to read project-level markdown configuration files to guide their behavior.

Here is exactly where to put this template and how to configure it so both tools automatically apply the frontmatter whenever they write or edit a doc.

## 1. For Cursor: Create a `.cursor/rules/` MDC File

Cursor uses the `.cursor/rules/` directory to store conditional, context-aware instructions using **MDC (Markdown Cursor)** files. This is much better than a single giant rule file because Cursor will only load the rule when you are actually editing markdown files, saving your context window.

Create a file named `.cursor/rules/documentation-standards.mdc` at the root of your project:

Markdown

````
---
description: "Enforces standard YAML frontmatter whenever creating or editing Markdown documentation files"
globs: ["**/*.md", "docs/**/*.md", "wiki/**/*.md"]
alwaysApply: false
---

### Standard Documentation Frontmatter Rule

Whenever you create a new Markdown (`.md`) file, or edit an existing one, you MUST ensure it begins with the following YAML frontmatter block:

```yaml
---
title: "Action-oriented, highly searchable title"
type: "guide | architecture-decision | onboarding | api-spec | troubleshooting"
owner: "@github_username"
verified: false
tags: [core-concept, setup, deployment]
---
````

### Rules for the Fields:

- **title**: Summarize the purpose of the doc in 60 characters or less.
    
- **type**: Strictly choose from the categories above. This helps downstream RAG pipelines index the document correctly.
    
- **owner**: Input the GitHub handle of the developer responsible for this knowledge.
    
- **verified**: Set to `false` by default. When a human reviews and verifies this AI-generated or modified doc, they will flip it to `true`.
    
- **tags**: Provide 2-4 tags in lowercase.
    

### Why this works brilliantly in Cursor:
Because of the `globs: ["**/*.md"]` parameter in the rule's frontmatter, the moment you open a markdown file or ask Cursor's Composer (`Cmd + I`) to create a new doc, Cursor will silently load this rule and **pre-write the frontmatter for you**.


---

## 2. For Claude: Use a `CLAUDE.md` File

If you are using **Claude Code** (Anthropic's terminal agent) or standard Claude integrations, they look for a file in your root directory named `CLAUDE.md`. This file serves as a system instruction guide for Claude when working in your repo.

Add a `# Documentation Standards` section to your root `CLAUDE.md` file:

```markdown
# Project Commands and Rules

... (your build/test commands here) ...

## Documentation Standards
Whenever creating or updating a Markdown documentation file, you must strictly prepend our standardized YAML frontmatter.

### The Frontmatter Template:
```yaml
---
title: "Action-oriented, highly searchable title"
type: "guide | architecture-decision | onboarding | api-spec | troubleshooting"
owner: "@github_username"
verified: false
tags: [core-concept, setup, deployment]
---
````

Ensure all fields are filled. Do not leave placeholder text.


> 💡 **Using Claude.ai Web Projects?** If you are using the web interface with Claude "Projects", upload this `CLAUDE.md` file into the Project Files, or copy-paste the markdown above directly into the **Project Instructions** panel in the UI.

---

## Summary of the Workflow

To tie this all together:

1. **Commit them to Git:** Put both `.cursor/rules/documentation-standards.mdc` and `CLAUDE.md` into your Git repository.
2. **Zero Overhead for the Team:** Because they are in Git, anyone on your team who clones the repo will immediately have their Cursor and Claude instances aligned.
3. **The "AI Hand-off":** When you tell Cursor, *"Write a guide on how to configure our new Postgres DB,"* the AI will read its own system rules, construct the markdown file, prepopulate the frontmatter with `type: "guide"`, and leave `verified: false` so you know to double-check its work.

Are you hoping to use these YAML fields to eventually build a searchable developer dashboard, or is the main goal right now just keeping the project files clean and searchable?


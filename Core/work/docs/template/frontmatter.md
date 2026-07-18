---
type: guide
title: Frontmatter Guide
description: Schema and conventions for YAML frontmatter in documentation and other compatible text files.
status: active
tags: [documentation, metadata]
timestamp: 2026-07-18T07:16:00Z
---

# Scope

Add YAML frontmatter when creating files in formats that natively support it (for example, Markdown, MDX, and static-site content).

Do not add YAML frontmatter to source code, configuration files, or other formats that do not support it.

# Required fields

| Field | Description |
| --- | --- |
| `type` | Document genre. Examples: `guide`, `architecture-decision`, `onboarding`, `api-spec`, `troubleshooting`. |
| `description` | One-sentence summary. Used for relevance checks before reading the full file. |
| `status` | Lifecycle state. Allowed values: `draft`, `active`, `deprecated`. |

# Optional fields

| Field | Description |
| --- | --- |
| `title` | Display title. Defaults to the filename when omitted. |
| `tags` | List of categorization labels. |
| `resource` | URI of the asset being described (for example, `db://postgres-prod`). |
| `context_scope` | System boundary (for example, `frontend`, `billing-service`). |
| `verified` | Boolean. Set to `true` when a human has vetted the content. |
| `verified_by` | Identifier of the verifier (for example, `@human`). |
| `timestamp` | ISO 8601 UTC time of the last meaningful change (for example, `2026-07-18T07:16:00Z`). Set on creation; update when content changes materially. |

# Status values

- **`active`**: Default for new, ready-to-use documents.
- **`draft`**: Intentionally unfinished work. Agents ignore draft files in this project.
- **`deprecated`**: Retained for history but no longer authoritative.

# Example

```yaml
---
type: guide
title: Setting up Postgres
description: How to spin up the local Postgres database.
tags: [database, setup]
status: active
resource: db://postgres-prod
context_scope: backend
verified: true
timestamp: 2026-07-18T07:16:00Z
---
```

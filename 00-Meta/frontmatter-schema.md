---
created: 2026-07-09
tags: [meta, workflow, reference]
type: reference
lang: en
status: published
---

> Related: [[Tag Taxonomy]] · [[inbox-triage-rules]] · [[Daily Workflow]] · [[yaml-okf]]

# Frontmatter Schema

Canonical YAML frontmatter reference for this vault. Optimized for human browsing (Obsidian), agent context (Cursor), and future retrieval (embeddings).

## Tier 1 — required on every triaged note

| Field | Required | Notes |
|-------|----------|-------|
| `title` | At triage | Infer from first `# H1` or filename |
| `description` | At triage | One sentence: what + why — highest ROI for search |
| `created` | Yes | `YYYY-MM-DD`; source of truth for capture date |
| `updated` | At triage | `YYYY-MM-DD`; set to triage date if missing |
| `type` | Yes | `reference` \| `howto` \| `hub` \| `daily` \| `concept` |
| `lang` | Yes | `en` \| `zh` |
| `status` | Yes | `draft` \| `published` |
| `tags` | Yes | From [[Tag Taxonomy]] — domain lives here, not a separate field |

```yaml
---
title: "Human-readable title"
description: "One sentence: what + why"
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: reference
lang: en
status: draft
tags: [ai, workflow]
---
```

**Capture vs triage:** `Ctrl+N` applies Tier 1 minimal via `default-note.md` (no `title`/`description` at capture). Triage automation or weekly review completes Tier 1.

## Tier 2 — optional for high-value notes

Add during triage for howtos and agent-reusable references.

| Field | Notes |
|-------|-------|
| `prerequisites` | Wikilink slugs to read first: `[yaml-markdown, tag-taxonomy]` |
| `summary` | 2–3 bullet key takeaways (body or YAML string) |

Do **not** add `relations:` — wikilinks, `Related:` blocks, and MOC hub pages are the OKF index graph.

## Tier 3 — future (no consumer yet)

Copy from [`tier3-future-note.md`](templates/tier3-future-note.md) when building an embedding pipeline or visibility filter.

| Field | Values | Future consumer |
|-------|--------|-----------------|
| `visibility` | `private` \| `internal` \| `public` | `.cursorignore` + MCP vault-search filter |
| `embedding` | `true` \| `false` | Vector index build script |
| `canonical` | `true` \| `false` | Dedup / authoritative-note resolver |

## Design principles

| Principle | Rule |
|-----------|------|
| **Metadata before RAG** | Don't build vector RAG before structured metadata — fix `title`, `description`, MOC links first |
| **One graph** | Don't duplicate the link graph in YAML — wikilinks + MOCs are the OKF index; `relations:` will drift |
| **Consumer required** | Don't add fields without a reader — each field needs a triage prompt, Dataview query, or script |
| **MCP ≠ metadata** | Don't conflate MCP with metadata — MCP routes tools; frontmatter helps file *selection* |
| **Touch-only migration** | Don't bulk-migrate ~164 notes — enrich on triage touch only |

## Concept map

| Concept | What it is | What frontmatter helps |
|---------|-----------|------------------------|
| **OKF** | Minimal YAML + markdown wiki | `type`, `title`, `description`, MOC maps |
| **RAG** | Retrieve relevant chunks at query time | `description`, `tags`, `updated` |
| **MCP** | Protocol for tools (files, APIs, browser) | `type` helps agents choose which file to read |
| **A2A** | Agents talking to other agents | `prerequisites` on complex notes |

Background: [[yaml-okf]] · [[rag-okf-wiki]]

## Templates

| Template | Trigger | Tier |
|----------|---------|------|
| [`default-note.md`](templates/default-note.md) | `Ctrl+N` → `Inbox/` (Templater auto) | 1 minimal |
| [`daily-note.md`](templates/daily-note.md) | Calendar / `Ctrl+Shift+D` | 1 + daily body |
| [`howto-note.md`](templates/howto-note.md) | Command palette → Insert template | 1 + 2 + steps scaffold |
| [`reference-note.md`](templates/reference-note.md) | Command palette → Insert template | 1 + 2 + summary scaffold |
| [`tier3-future-note.md`](templates/tier3-future-note.md) | **Reference only** — do not auto-apply | 1 + 2 + 3 placeholder |

See [[Daily Workflow]] § Editing templates for Templater setup.

## Migration

- **New/triaged notes:** full Tier 1; Tier 2 when valuable
- **Existing notes:** leave as-is until touched; add `description` opportunistically
- **Never require** Tier 2 or Tier 3 on short inbox captures

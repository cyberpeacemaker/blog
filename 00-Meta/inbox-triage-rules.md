---
created: 2026-07-08
tags: [meta, workflow, inbox]
type: reference
lang: en
status: published
---

> Related: [[Daily Workflow]] · [[Inbox]] · [[Tag Taxonomy]] · [[frontmatter-schema]]

# Inbox Triage Rules

Instructions for organizing notes from `Inbox/` into topic folders. Used by weekly manual review and the **Daily Inbox Triage** Cursor Automation.

## Skip list

Do **not** move:

- `Inbox/Inbox.md` (hub page)
- Empty files (no body content)
- Files already in topic folders `00-Meta/` through `09-Personal/`

## Date inference

| Filename pattern                  | `created` value                                             |
| --------------------------------- | ----------------------------------------------------------- |
| `MM-DD-slug.md`                   | `2026-MM-DD` (use current year)                             |
| `slug.md` (no date prefix)        | Previous calendar day, or explicit date from body if stated |
| Frontmatter already has `created` | Keep existing value                                         |

Never add date prefixes to topic filenames after triage.

## Frontmatter schema

Canonical reference: [[frontmatter-schema]]. Capture uses [`default-note.md`](templates/default-note.md) (Tier 1 minimal). Triage completes Tier 1 and adds Tier 2 when the note is high-value.

### Tier 1 — required on every triaged note

```yaml
---
title: "Human-readable title"           # infer from first H1 or filename
description: "One sentence: what + why"
created: YYYY-MM-DD
updated: YYYY-MM-DD                     # set to triage date if missing
type: reference                         # reference | howto | hub | daily | concept
lang: en                                # en | zh — infer from body
status: draft                           # draft | published
tags: [ai, workflow]                    # from Tag Taxonomy — domain lives in tags
---
```

### Tier 2 — optional for high-value notes (howtos, agent-reusable references)

```yaml
prerequisites: []        # wikilink slugs: [yaml-markdown, tag-taxonomy]
summary: ""              # 2–3 bullet key takeaways
```

Do **not** add `relations:` — wikilinks, `Related:` blocks, and MOC updates build the graph. Do **not** add a separate `domain:` field — use `tags` per [[Tag Taxonomy]].

### Concept map (what fields actually serve)

| Concept | Frontmatter role |
|---------|------------------|
| **OKF** | `type`, `title`, `description` + MOC hub maps |
| **RAG / search** | `description`, `tags`, `updated` improve retrieval |
| **MCP** | `type` helps agents pick which file to read — MCP itself routes tools |
| **A2A** | `prerequisites` on complex notes; handoff is runtime design |

Add a `Related:` block pointing to the relevant MOC, not `[[Inbox]]`.

## Folder routing

| Keywords / topic | Destination folder |
|------------------|-------------------|
| Malcolm, Zeek, Suricata, Arkime, OpenSearch, NSM | `01-NSM-Malcolm/` |
| Threat hunting, DFIR, MITRE, CTF, forensics, C2, malware, beacon | `02-Threat-Hunting-DFIR/` |
| Claude, Cursor, AI agents, RAG, harness | `03-AI-Agents/` |
| Git, GitHub, Python, VS Code, testing, dev env | `04-Dev-Environment/` (use subfolders `Git/`, `Python/`, `VS-Code/`) |
| CI/CD, architecture, agile, MVP, software engineering | `05-Software-Engineering/` |
| UI/UX, p5.js, design, creative | `06-Design-Creative/` |
| Slack, meetings, Obsidian, productivity tools | `07-Productivity-Work/` |
| Career, presentations, talks | `08-Career-Presentations/` |
| Personal, hobby, non-work | `09-Personal/` |
| Vault setup, MOCs, templates, workflow meta | `00-Meta/` |

When uncertain, prefer the most specific match. Flag ambiguous notes in the summary instead of guessing.

## Per-file checklist

1. Add or fix frontmatter (`title`, `description`, `created`, `updated`, `tags`, `type`, `lang`, `status`); add Tier 2 (`prerequisites`, `summary`) for high-value howtos/references
2. Strip `MM-DD-` prefix from filename if present
3. Move with `git mv Inbox/slug.md destination/slug.md`
4. Replace `Related: [[Inbox]]` with the relevant MOC link
5. Add 1–2 wikilinks to related existing notes
6. Append entry to the relevant MOC / hub page (see below)

## MOC update rules

| Destination | Update hub |
|-------------|------------|
| `02-Threat-Hunting-DFIR/` | [[MOC - Threat Hunting]] |
| `04-Dev-Environment/` | [[MOC - Dev Environment]] |
| `07-Productivity-Work/` | [[07-Productivity-Work]] |
| `05-Software-Engineering/` | [[05-Software-Engineering]] |
| `01-NSM-Malcolm/` | [[MOC - Malcolm & NSM]] |
| `03-AI-Agents/` | [[MOC - Claude & Cursor]] or [[MOC - AI Agents]] |
| `00-Meta/` | [[Home]] or [[Daily Workflow]] as appropriate |

Do not duplicate MOC entries if the note is already listed.

## Merge rules

- Very short notes (< 15 lines) that duplicate an existing note in the destination folder → merge into the existing note, delete the inbox copy
- Flag potential duplicates in the summary; do not auto-merge long notes

## Post-triage

- If **3 or more** files were moved, run:
  ```bash
  python scripts/build-vault-canvas.py --all
  ```
- Do **not** promote content from `daily/` → topic folders (weekly manual step)

## Git policy

Manual triage: **organize only.** Do not run `git add`, `git commit`, or `git push`; leave changes unstaged for human review.

Cursor Automation daily triage: follow [[automation-prompt-suggestion]] and [[automation-pr-merge-policy]]. The automation may commit by phase on the cloud branch, verify the result, push the branch, and open a PR for human review.

Do **not** enable auto-merge for inbox triage PRs. A human should review and merge the PR manually.

## Summary format

End every triage run with:

```
## Inbox Triage Summary
- Moved: [list of source → destination]
- Merged: [list if any]
- Skipped: [list if any]
- MOCs updated: [list]
- Needs review: [ambiguous items, duplicates flagged]
```

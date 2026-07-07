---
created: 2026-07-07
tags: [meta, workflow]
type: reference
lang: en
status: published
---

# Daily Workflow

How to capture, link, and maintain notes in this vault.

## Capture

1. Open [[Home]] or the relevant MOC for your current work
2. **Quick capture:** save to `Uncategorized/` or use Calendar daily notes (`Uncategorized/daily/YYYY-MM-DD.md`)
3. **Named notes:** use a semantic slug — `malcolm-query.md`, not a date prefix
4. Set `created: YYYY-MM-DD` in frontmatter (see [[YAML-markdown]] and [[Tag Taxonomy]])

## Link

1. Before finishing a note, add **1–2 wikilinks** to related notes
2. If the note is important, add it to the relevant MOC
3. AI workflow notes should link to [[CLAUDE]] (agent instruction template)

## Commit

1. **Obsidian Git** auto-commits every 30 minutes (configurable in Settings → Obsidian Git)
2. Or commit manually: `git add . && git commit -m "2026-07-07"` then `git push`
3. **Git is source of truth** — pull before editing on another machine

## Review (Weekly)

1. Open **Graph view** — find orphan notes with no connections
2. Move inbox notes from [[Uncategorized]] into the right topic folder
3. Connect orphans to a MOC or archive to [[09-Personal]]
4. Merge duplicates (see list below)

## Folder Guide

| Folder | Use for |
|--------|---------|
| `00-Meta/` | Home, MOCs, templates, guidelines |
| `01-NSM-Malcolm/` | Zeek, Suricata, Arkime, OpenSearch, Malcolm |
| `02-Threat-Hunting-DFIR/` | MITRE, forensics, CTF, hunt notes |
| `03-AI-Agents/` | Claude, Cursor, agents, RAG |
| `04-Dev-Environment/` | Git, Python, VS Code, testing |
| `05-Software-Engineering/` | Architecture, agile, MVP |
| `06-Design-Creative/` | UI/UX, p5.js, visual tools |
| `07-Productivity-Work/` | Slack, meetings, work tools |
| `08-Career-Presentations/` | Talks, transcripts, career |
| `09-Personal/` | Personal notes (optional separate vault later) |
| `Uncategorized/` | Inbox, daily notes, unsorted captures |

## Naming Convention

| Pattern | Example | Use |
|---------|---------|-----|
| `slug.md` | `malcolm-orchestration.md` | Topic notes — date lives in frontmatter |
| `YYYY-MM-DD.md` | `2026-07-07.md` | Daily notes only (Calendar) |
| No date prefix | `Home.md`, `MOC - Malcolm & NSM.md` | Hub pages |

## Known Duplicates to Clean Up

- [[tracking]] + [[tracking-ori]]
- [[python-venv]] + [[python-venv-v2]]
- [[ai-workflow]] + [[ai-workflow-v2]]
- [[vscode-tips]] + [[vscode-tips-v2]]
- [[harness]] + [[harness-v2]]

## Plugins

| Plugin | Status | Purpose |
|--------|--------|---------|
| Obsidian Git | Enabled | Auto-commit to Git |
| Calendar | Enabled | Daily notes in `Uncategorized/daily/` |
| Templater | Enabled | Note templates |
| Tag Wrangler | Enabled | Rename/merge tags |
| Advanced Canvas | Enabled | Attack-surface / concept maps |
| Dataview | Optional | Query by `created` frontmatter |
| IOC Lens / SOC Toolkit | When actively hunting | Threat intel enrichment |

## Obsidian Sync vs Git

- **Git** = canonical backup and version history for this repo
- **Obsidian Sync** = optional for mobile/second machine
- Avoid editing the same note on two machines without pulling first

See also: [[obsidian]] for Sync vs Git decision guide.

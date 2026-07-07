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
2. Create a new note in the correct folder (or use Calendar daily notes in `00-Meta/daily/`)
3. Use the `MM-DD-slug` naming convention to match existing notes

## Link

1. Before finishing a note, add **1–2 wikilinks** to related notes
2. If the note is important, add it to the relevant MOC
3. AI workflow notes should link to [[06-06-CLAUDE]] (agent instruction template)

## Commit

1. **Obsidian Git** auto-commits every 30 minutes (configurable in Settings → Obsidian Git)
2. Or commit manually: `git add . && git commit -m "07-07"` then `git push`
3. **Git is source of truth** — pull before editing on another machine

## Review (Weekly)

1. Open **Graph view** — find orphan notes with no connections
2. Connect orphans to a MOC or archive to [[09-Personal]]
3. Merge duplicates (see list below)

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

## Known Duplicates to Clean Up

- [[05-08-tracking]] + [[05-08-tracking-ori]]
- [[05-20-python-venv]] + [[05-21-python-venv]]
- [[05-21-ai-workflow]] + [[05-22-ai-workflow]]
- [[05-20-vscode-tips]] + [[05-22-vscode-tips]]
- [[03-AI-Agents/Harness-DevSecOps/06-10-harness]] + [[03-AI-Agents/Harness-DevSecOps/06-11-harness]]

## Plugins

| Plugin | Status | Purpose |
|--------|--------|---------|
| Obsidian Git | Enabled | Auto-commit to Git |
| Calendar | Enabled | Daily notes in `00-Meta/daily/` |
| Tag Wrangler | Install when needed | Rename/merge tags |
| Templater | Optional (2–4 weeks) | Note templates |
| Dataview | Optional (2–4 weeks) | Query by frontmatter |
| IOC Lens / SOC Toolkit | When actively hunting | Threat intel enrichment |

## Obsidian Sync vs Git

- **Git** = canonical backup and version history for this repo
- **Obsidian Sync** = optional for mobile/second machine
- Avoid editing the same note on two machines without pulling first

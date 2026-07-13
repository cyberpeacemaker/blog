---
created: 2026-07-09
tags: [workflow, meta]
type: hub
lang: zh
status: published
visibility: private
---

> Related: [[Home]] · [[Daily Workflow]] · [[self-report-retro]]

# Core

Operational workspace — long-lived rolling docs where you work **from**. Not a knowledge topic folder (`01–09`); not Obsidian core settings or `00-Meta/`.

## Work

- [[work/todo]] — work action backlog
- [[Core/work/random]] — work thinking stream (may promote to `Inbox/` or topic folders when mature)

## Personal

- [[personal/todo]] — personal errands and tasks
- [[Core/personal/random]] — personal quick thoughts

## Reflection

- [[journal]] — periodic reflection (dated sections); raw day log stays in `daily/`
- [[brag]] — living accomplishments list; methodology in [[self-report-retro]]

## Capture boundaries

| File | Purpose | Not this |
|------|---------|----------|
| `work/todo.md` | Work action backlog | `Inbox/` — inbox items become topic notes |
| `work/scratch.md` | Work thinking in progress | `Inbox/` — scratch may never promote |
| `personal/todo.md` | Personal errands | `09-Personal/` — reference notes, not tasks |
| `personal/scratch.md` | Personal quick thoughts | same |
| `journal.md` | Periodic reflection | `daily/` — raw day log |
| `brag.md` | Living accomplishments | [[self-report-retro]] — methodology only |

**Promotion rule:** When scratch content matures, extract to `Inbox/` or the right `01–09` folder and leave `Promoted to [[note]]` in scratch.

**Automation:** Daily inbox triage does not touch `Core/` (see `scripts/validate-triage-paths.sh`).

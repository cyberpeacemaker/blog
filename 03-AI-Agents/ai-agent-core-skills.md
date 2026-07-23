---
title: "AI Agent Core Skills"
description: "Recommends a compact set of reusable skills for daily AI-assisted engineering workflows."
created: 2026-07-22
updated: 2026-07-22
tags: [ai, agents, claude]
type: reference
lang: en
status: draft
---

> Related: [[MOC - Claude & Cursor]] · [[MOC - AI Agents]] · [[claude-skills]] · [[deterministic-tooling-pattern]]

You are spot-on. The **Skill + Template + Script** pattern has quickly become the standard architecture in modern AI-assisted engineering.

  

Frameworks like **Claude Code**, **Cursor**, and **MCP (Model Context Protocol)** all use this exact layout.

  

---

  

## 1. Core & Essential Skills Every Dev Agent Needs

  

When building out your agent toolkit, you don't need dozens of skills. Starting with **5 core workflow skills** covers 90% of daily engineering tasks:

  

| Skill | Description / Purpose | Tools/Scripts Triggered |

| --- | --- | --- |

| **`feature-spec-to-code`** | Takes a high-level requirement or issue, breaks it into a step-by-step task checklist, and writes tests first. | Reads specs, creates local plan file. |

| **`interactive-review`** | Scans `git diff` against team coding standards, security rules (OWASP), and test coverage before commiting. | Runs linters, static analyzers. |

| **`ci-debug-and-fix`** | Fetches failed CI build logs, identifies the breaking line, reproduces it locally, and fixes it. | `gh run view --log-failed`, local test runner. |

| **`pr-creator`** | Summarizes changes, fills out the repository PR template, formats commit messages, and opens a PR. | `scripts/create-pr.sh`, `gh pr create`. |

| **`release-and-changelog`** | Collects merged PRs since the last tag, categorizes changes (Features, Fixes), and updates `CHANGELOG.md`. | `git log`, `gh release create`. |

  

---


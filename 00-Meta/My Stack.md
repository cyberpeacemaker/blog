---
created: 2026-07-07
tags: [meta, stack, tools]
type: hub
lang: en
status: published
---

# My Stack

Living index of tools and how they connect. Expanded from [[2026-06-08-tools]].

## Secure Ops & Communication

- **Signal & Telegram** — out-of-band secure comms; Telegram for threat intel channels
- **Slack & Asana / Jira** — team collaboration and project tracking
  - See [[2026-07-06-slack-asana-jira]], [[2026-07-06-slack]], [[2026-07-06-business-productive-tool]]

## Threat Intel Brain (Obsidian)

Using Obsidian with **IOC Lens**, **SOC Toolkit**, and **VirusTotal Enrichment** for a local interconnected threat intelligence knowledge base.

- Map threat actors, malware behavior, and vulnerabilities
- Parse IOCs from raw logs directly in markdown
- See [[MOC - Threat Hunting]] for hunt methodology
- See [[2026-05-13-env-setup]] for Obsidian + Canvas setup

## NSM & Hunting Stack

- **Malcolm** — NSM orchestration → [[MOC - Malcolm & NSM]]
- **Zeek / Suricata / Arkime / OpenSearch** — sensor-to-index pipeline
- **Wireshark / tshark** — PCAP analysis

## Modern Dev & Code Acceleration

- **Claude & Cursor** — AI-assisted coding → [[MOC - Claude & Cursor]]
- **Hermes** — local LLM for function-calling agents → [[2026-06-08-hermes-claude]]
- See [[MOC - AI Agents]] for agent frameworks

## Code Management & AI Infrastructure

- **Git & GitHub** — version control → [[MOC - Dev Environment]]
- **Hugging Face & Ollama** — local model deployment (zero data leakage)

## Design & Creative

- **Figma / Asana** — design workflow → [[2026-06-05-asana-figma]]
- **p5.js / Three.js** — creative coding → [[2026-06-08-p5js]]

## The Big Picture

This stack represents a **SecDevAnomalist** workflow: enterprise PM for organization, high-speed AI coding for execution, private local LLMs for sensitive data, and Obsidian as a local SIEM/threat hunting companion.

## Related MOCs

- [[MOC - Malcolm & NSM]]
- [[MOC - Threat Hunting]]
- [[MOC - AI Agents]]
- [[MOC - Claude & Cursor]]
- [[MOC - Dev Environment]]

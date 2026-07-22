---
created: 2026-07-22 11:07
updated: 2026-07-22 11:07
tags: []
type: reference
lang: en
status: draft
---
The best choice depends on **portability** vs. **standard developer conventions**.

In practice, a **hybrid approach** is the industry standard: keep AI-exclusive helpers inside the skill folder, and keep standard/shared tools at the root level.

## Decision Matrix: Where to Put What

|**Location**|**Use Case**|**Why?**|
|---|---|---|
|**Inside Skill Folder**<br><br>  <br><br>`.claude/skills/<skill-name>/`|• AI-only scripts<br><br>  <br><br>• Custom LLM prompt templates<br><br>  <br><br>• Skill-specific JSON schemas|**Portability & Modular:** You can copy/paste `.claude/skills/<skill-name>/` into another project, and the skill works immediately with zero broken dependencies.|
|**Root Level**<br><br>  <br><br>`/scripts/` or `.github/`|• Standard PR/Issue templates<br><br>  <br><br>• Scripts human devs run manually<br><br>  <br><br>• Build/deployment scripts|**GitHub Integration & Convention:** GitHub _requires_ templates to be in `.github/` to render them in the web UI. Human developers also expect root `/scripts/`.|

## Recommended Hybrid Directory Layout

Here is how a clean, production-grade repository structures both:

Plaintext

```
my-project/
├── .github/
│   └── PULL_REQUEST_TEMPLATE.md      <-- GitHub reads this natively for humans & web UI
│
├── .claude/
│   ├── CLAUDE.md                     <-- High-level repo instructions
│   └── skills/
│       ├── create-pr/
│       │   ├── SKILL.md              <-- Tells agent how/when to use the skill
│       │   └── assets/
│       │       └── pr_prompt_format.md <-- AI-specific prompt instructions (if any)
│       │
│       └── security-audit/
│           ├── SKILL.md
│           └── scripts/
│               └── parse_sec_logs.py <-- AI-exclusive helper script
│
└── scripts/                          <-- Shared scripts humans & AI both run
    ├── create-pr.sh
    └── test-all.sh
```

## Rules of Thumb

1. **If GitHub needs to see it natively:** Put it in `.github/` (e.g., standard PR/Issue templates).
    
2. **If human developers run it directly in terminal:** Put it in root `/scripts/` (e.g., setup, build, or deployment scripts).
    
3. **If it ONLY exists to help the AI perform that specific skill:** Put it inside `.claude/skills/<skill>/` (e.g., a Python script that parses diffs specifically for the agent's context).


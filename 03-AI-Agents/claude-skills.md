---
created: 2026-06-09
tags: [claude, skills, ai]
type: howto
lang: en
status: draft
---

> Related: [[MOC - Claude & Cursor]] · [[CLAUDE]] · [[claude-skills-example]] · [[claude-skill-command]]

**Skills** extend Claude's capabilities by bundling custom instructions, templates, and scripts. Create a `SKILL.md` file in `~/.claude/skills/<skill-name>/` or `.claude/skills/` (project-level), and Claude loads it automatically when relevant or when you invoke it with `/skill-name`. Skills support dynamic context injection (running commands and inlining output), supporting files, and frontmatter configuration to control invocation. Unlike `CLAUDE.md`, skill content loads only when used, reducing token costs for large reference material.

---

Good catch! The directory structure allows **supporting files**. A skill can include:

```
~/.claude/skills/deploy-to-aws/
├── SKILL.md          (main skill definition)
├── deploy.sh         (script called by the skill)
├── config.json       (config file referenced in SKILL.md)
└── templates/        (template files)
```

The skill uses `${CLAUDE_SKILL_DIR}` to reference these files. So the directory isn't redundant—it's designed to bundle related assets together. If your skill is just a prompt with no supporting files, you could theoretically flatten it, but the directory structure keeps everything organized and makes it easy to add scripts or configs later.
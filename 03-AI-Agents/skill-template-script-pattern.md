---
title: "Skill Template Script Pattern"
description: "Describes the three-part agent workflow pattern that combines skills, templates, and deterministic scripts."
created: 2026-07-22
updated: 2026-07-22
tags: [ai, agents, workflow]
type: reference
lang: en
status: draft
---

> Related: [[MOC - Claude & Cursor]] · [[MOC - AI Agents]] · [[deterministic-tooling-pattern]] · [[agent-architecture-folder]]

Yes, absolutely! Incorporating templates completes the architecture. Combining **Templates + Scripts + Skills** creates a robust, production-grade AI workflow pattern.

Adding templates solves the last major problem with AI-generated text: **formatting drift**. Without templates, an AI might structure a PR description beautifully one day, and completely omit key sections (like testing steps or breaking changes) the next.

## The 3-Tier Pattern Explained

When you bring all three components together, each layer has a distinct responsibility:

```
┌────────────────────────────────────────────────────────┐
│                      1. SKILL                          │
│ - Reads context (e.g., git diff, commit history)       │
│ - Fills out specific dynamic fields (Summary, Tests)   │
└──────────────────────────┬─────────────────────────────┘
                           │ Passes structured variables
                           ▼
┌────────────────────────────────────────────────────────┐
│                     2. TEMPLATE                        │
│ - Defines rigid structure (.github/PULL_REQUEST.md)   │
│ - Contains placeholders: {{SUMMARY}}, {{TEST_NOTES}}   │
└──────────────────────────┬─────────────────────────────┘
                           │ Merged file
                           ▼
┌────────────────────────────────────────────────────────┐
│                      3. SCRIPT                         │
│ - Validates inputs and environment                     │
│ - Executes `gh pr create --body-file /tmp/pr.md`       │
└────────────────────────────────────────────────────────┘
```

## Why This Works So Well

- **Team Alignment:** You can reuse existing repository templates (like `.github/PULL_REQUEST_TEMPLATE.md` or issue templates). The AI automatically complies with your team’s existing contribution rules.
    
- **Higher Prompt Efficiency:** Instead of asking the AI to _"write a detailed PR description,"_ your skill prompt simply instructs it to: _"Analyze the git diff and provide 2 bullet points for `{{SUMMARY}}` and a checklist for `{{TESTING}}`."_ Focused tasks yield much higher quality output.
    
- **Flawless `gh` Execution:** Passing a complex, multi-line PR body directly inside a shell command (`gh pr create -b "..."`) is prone to escaping bugs. Combining a template into a temporary markdown file and passing `--body-file` to `gh` is virtually bulletproof.
    

## Practical Example

### 1. Template (`.github/templates/pr.md`)

Markdown

```
## Summary
<!-- SUMMARY_PLACEHOLDER -->

## Type of Change
- [ ] Bug fix
- [x] New feature

## How Has This Been Tested?
<!-- TESTING_PLACEHOLDER -->
```

### 2. Script (`scripts/create-pr.sh`)

Bash

```
#!/bin/bash
# Replaces placeholders, creates temporary file, executes gh command
TEMP_BODY=$(mktemp)
sed -e "s/<!-- SUMMARY_PLACEHOLDER -->/$1/" \
    -e "s/<!-- TESTING_PLACEHOLDER -->/$2/" \
    .github/templates/pr.md > "$TEMP_BODY"

gh pr create --title "$3" --body-file "$TEMP_BODY"
rm "$TEMP_BODY"
```

### 3. Skill Definition

> _"When creating a PR, analyze `git diff`, generate a summary and testing notes, and pass them to `./scripts/create-pr.sh`."_

Are you setting this up for a specific project/team repository that already uses PR/Issue templates, or are you creating a fresh workflow from scratch?


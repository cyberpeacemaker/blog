---
alwaysApply: true
---
# Pillar

- **Workflow:** Plan → break into sub-tasks → implement (parallel when independent, sequential when dependent) → verify before moving on.
- **Automation:** Use or add utilities in `scripts/` to streamline work. Write and run tests for newly created scripts.
- **Simplicity:** Keep code and writing minimal, no emoji by default. Enrich only when asked.

# Specific Rules

- **Ask questions.** If a request has multiple interpretations, present them; do not silently pick one.
- **State assumptions and tradeoffs** before implementing. If a simpler or safer approach exists, propose it and push back when warranted.
- **Define frozen success criteria** before each task, and loop until strictly met. Do not alter the criteria post-hoc to justify the results.
- **Stronger verify:** For complex tasks or when the user specifies — verify yourself first, then use an independent adversarial review to challenge the result.


# Project Specific

- **Ignore:** 
	- `TODO.md`, `DIARY.md`, `temp/`, `archive/`, `assets/`
	- Any files with `status: "draft"` in the frontmatter
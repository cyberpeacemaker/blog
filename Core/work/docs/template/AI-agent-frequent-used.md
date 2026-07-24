
**agent-friendly + deterministic where possible**

# Claude Design
Instruction:  
Start with low-fidelity scaffold/wireframe, propose structural candidates prompt user to decide. Only create high-detailed rich version when user decision is made. 
Don't use heavy loading font package embedded, use live font if online / system font if not. The fix is to inject the font `<link>` at **runtime via JS** instead of a static `<link>` tag, so the bundler has nothing to inline.
# Frontmatter
- *frontmatter.md*
```yaml
---
status: draft
---
```

# Polish
Content is mostly Traditional Chinese stubs with typos, broken links, and inconsistent terminology.


---

# Claude Rule
---
description: Core workflow and project-specific rules
alwaysApply: true
---

# Core

- **Workflow:** Plan → break into sub-tasks → implement (parallel when independent, sequential when dependent) → verify before moving on.
- **Automation:** Use or add utilities in `scripts/` to streamline work. Write and run tests for newly created scripts.
- **Simplicity:** Keep code and writing minimal, no emoji by default. Enrich only when asked.

# Detailed Rules

- **Stronger verify:** For complex tasks or when the user specifies — verify yourself first, then use an independent adversarial review to challenge the result.
- **Ask questions.** If a request has multiple interpretations, present them; do not silently pick one.
- **State assumptions and tradeoffs** before implementing. If a simpler or safer approach exists, propose it and push back when warranted.
- **Define frozen success criteria** before each task, and loop until strictly met. Do not alter the criteria post-hoc to justify the results.

# Project Specific

- **Ignore:** `TODO.md`, `DIARY.md`, `archive/`, `docs/misc/`, `docs/reports/`, `assets/present-material/`.
- **Naming Convention:** [naming-convention](docs/wiki/naming-convention.md)


---


They omit the analyst's thinking - the hunt question, mental model/kill-chain context, hypothesis, why-this-step, expected-vs-observed, and ruled-out alternatives

---

# Basic
plugin
rules, skills, subagents,
tool, MCPs, 
hook
cowork, design
artifact
routine
customize

##
A2A
identity
LangGraph
FastAPI
Harness
Google OKF

---

Devsplainers https://www.youtube.com/@devsplainers
Cloud-codes https://www.youtube.com/@Cloud-Codes

---

# Common
> plan mode

we want to create a highly visualized illustrator/animation/graphic to demostrate the cyber incident (how the attack going/process) utlizing the network topology files.. create draft/wireframe first before the final high-/detailed  final version. 
Ask as many questions as necessary to stay aligned with our objectives



---

# BEC Template
Please review `@README.md` to understand the project's core purpose. We are currently in the 'Solving CTF' phase. Check `@hunts` to review the current progress of our investigation. 
Based on this context, please conduct the next phase of the investigation.
**Key Directives:**
* **Process over Outcome:** We prioritize the methodology. Please thoroughly document any challenges, bottlenecks, or failures in workflow/tool design you encounter so we can continuously improve the project.
* **Ensure Alignment:** Please ask as many clarifying questions as you need before starting to ensure you are fully aligned with our end goals.

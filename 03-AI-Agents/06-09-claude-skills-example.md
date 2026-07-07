Here is exactly how a `SKILL.md` file is structured.

Notice the **YAML frontmatter** blocked off by the triple dashes (`---`) at the very top. This is the crucial snippet Claude reads at startup to decide whether or not it needs to load the rest of your instructions.

```markdown
---
name: pr-reviewer
description: Generates a thorough, structured code review for GitHub Pull Requests. It focuses on performance, edge cases, security vulnerabilities, and adherence to clean code standards.
arguments:
  - name: code_diff
    description: The diff or code file to review.
    required: true
---

# PR Reviewer Skill

You are an expert software engineer and code reviewer. Your goal is to provide actionable, constructive, and highly technical feedback on code submissions.

## Objective
Analyze the provided code changes (`code_diff`) to identify bugs, architectural flaws, security risks, and optimization opportunities. Balance your feedback by highlighting good practices as well as areas of improvement.

## Execution Steps

1. **High-Level Summary:** Begin with a 2-3 sentence overview of what the code changes accomplish and an overall assessment (e.g., Approve, Request Changes).
2. **Security & Performance Check:** 
   - Scan for potential injection vulnerabilities, memory leaks, or unhandled promise rejections.
   - Look for inefficient loops or redundant DB queries ($O(N^2)$ complexities).
3. **Edge Case Analysis:** Identify at least two scenarios where the inputs could cause the code to crash (e.g., null values, empty arrays, extreme bounds).
4. **Code Quality & Style:** Verify readability, naming conventions, and proper error handling.

## Output Format

Always format your response using the following Markdown template:

### 📊 Summary Assessment
[Your overview here]

### 🚨 Critical Issues (Must Fix)
*   **[File Path:Line] Issue Title:** Detail the issue.
```javascript
    // Show a quick refactor snippet if applicable
    ```

### 💡 Suggestions & Optimizations
*   **[File Path:Line] Suggestion Title:** Non-breaking improvements.

### 👏 Good Work
*   Highlight 1-2 elements of the code that were exceptionally well-written.

```

---

### Key Things to Notice in This Example:

* **The Description is the Hook:** The `description` in the frontmatter is the only thing Claude holds in its active memory initially. It uses everyday semantic matching—so if you say *"Hey Claude, can you look over this code diff for me?"*, it triggers this specific skill because the description explicitly matches "Pull Requests" and "code review."
* **The Arguments Block:** The `arguments` define what the skill expects. In standard environments or command-line interfaces like Claude Code, this allows you to pass variables or files directly into the skill using slash commands (e.g., `/pr-reviewer code_diff=main.py`).
* **The Formatting Template:** By embedding an explicit output template at the bottom of the `SKILL.md`, you guarantee that Claude will always structure its final answer identically every single time the skill runs.
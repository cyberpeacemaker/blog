我的解題絲路

看到題目，腦海中自然會有些直覺的想法
可以裂成checklist
每個獨立嘗試 > 觀察結果

可以在交叉驗證

---

# Deliverable 1 - The guideline: `module_writeup_guide.md` (new, repo root)

A single doc that defines the augmented `### Solution` structure and a quality checklist. It complements `module_create_template.md` (execution mechanics) by adding the narrative the latter omits. The required `### Solution` shape becomes:

- **Hunt question** - restate the challenge as the question the analyst is actually answering.
- **Where this sits** - one-paragraph kill-chain/scenario context + a small Mermaid mindmap tying the module to the baseline and adjacent modules.
- **Hypothesis** - what we expect to find and why (sourced from the investigation brief), stated *before* running anything.
- **Investigation** - the existing numbered steps, but each annotated with:
  - *Why this step*
  - *Expected*
  - *Observed* (the script command + intermediate output is the evidence)
  - *What it tells us*
- **Alternatives ruled out** - dead ends and why they're rejected (e.g. other scanned hosts, SMBv1 vs SMBv2).
- **Answer & confidence** - the projected answer, how confident, and how to falsify it.
- **Final workflow** - keep the existing Option A / Option B blocks verbatim.

Plus a **good-writeup checklist** (every step states intent + expectation; at least one alternative ruled out; answer cites evidence; scripts are evidence, not narration) and the contract that the `select.py` field/template strings stay unchanged.
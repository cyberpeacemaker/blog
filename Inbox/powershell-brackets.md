---
created: 2026-07-09 20:07
updated: 2026-07-09 20:07
tags: []
type: reference
lang: en
status: draft
---
Ah, the classic programming language crossover! You used Python/JavaScript square brackets `[...]` to define your array, but PowerShell got confused because it uses square brackets for type casting (like `[int]` or `[string]`).

To define an array in PowerShell, you need to use **`@(...)`** instead.

Here is the corrected command that will work perfectly:

PowerShell

```
@("$HOME\miniconda3", "C:\ProgramData\miniconda3", "$env:LOCALAPPDATA\miniconda3") | Where-Object { Test-Path "$_\Scripts\conda.exe" }
```

### What changed?

- Changed `[...]` to `@(...)` so PowerShell recognizes it as a list/array of strings.
    
- The rest of your pipeline (`Where-Object` and `Test-Path`) is syntactically correct and will now properly output whichever path actually contains `conda.exe`.


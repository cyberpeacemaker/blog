---
created: 2026-08-01 19:08
updated: 2026-08-01 19:08
tags: []
type: reference
lang: en
status: draft
---
AI models often output the legacy **`config.json`** format because older documentation used JSON. Modern versions of Continue have transitioned to **`config.yaml`**.

### The Converted `config.yaml` Format

Here is your exact JSON configuration translated into the proper `config.yaml` structure for Continue:

YAML

```
name: Ollama Local Config
version: 1.0.0
schema: v1

models:
  - name: PoC Fast Check (SmolLM2 135M)
    provider: ollama
    model: smollm2:135m
    apiBase: http://localhost:11434
    roles:
      - chat
      - edit

  - name: Threat Rule Engine (Qwen2.5 7B)
    provider: ollama
    model: qwen2.5-coder:7b
    apiBase: http://localhost:11434
    roles:
      - chat
      - edit

  - name: Qwen 1.5B Autocomplete
    provider: ollama
    model: qwen2.5-coder:1.5b
    apiBase: http://localhost:11434
    roles:
      - autocomplete
```

### How to Apply It

1. **Open Continue Config in VS Code / JetBrains:**
    
    - Click the **Continue icon** on your sidebar.
        
    - Click the **gear/settings icon** next to "Local Config" at the bottom of the Continue panel (or top right of the chat box).
        
    - This will open your global `config.yaml` file in your editor.
        
2. **File Location (Manual Path):**
    
    - **macOS / Linux:** `~/.continue/config.yaml`
        
    - **Windows:** `%USERPROFILE%\.continue\config.yaml`
        
3. **Paste & Save:**
    
    Replace the file contents with the YAML code block above and save it (`Ctrl+S` or `Cmd+S`). Continue reloads the configuration automatically.
    

### Key Structural Differences to Keep in Mind

- **`title` $\rightarrow$ `name`**: YAML uses `name` for model labels.
    
- **`tabAutocompleteModel` $\rightarrow$ `roles: [autocomplete]`**: Instead of having a dedicated top-level autocomplete object, YAML assigns models to specific roles (e.g., `chat`, `edit`, or `autocomplete`).
    
- **Header Fields**: Modern YAML configs require `name`, `version`, and `schema: v1` at the top.


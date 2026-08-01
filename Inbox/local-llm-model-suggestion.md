---
created: 2026-08-01 19:08
updated: 2026-08-01 19:08
tags: []
type: reference
lang: en
status: draft
---

The rumor that "Chinese models aren't good" is actually outdated when it comes to open-source coding models.

In fact, **Chinese open-weight models (specifically Alibaba's Qwen series and DeepSeek) currently dominate open-source coding benchmarks**, often outperforming Western open-source models of similar sizes.

There are two distinct angles to consider regarding Chinese models:

1. **Performance & Quality:** For local coding with Continue, **`qwen2.5-coder`** is widely considered the best overall open-source model family per gigabyte of RAM.
    
2. **Privacy & Security:** Because you run these models **locally on your machine via Ollama**, **your code never leaves your computer** regardless of who developed the weights. However, if your employer or client has strict compliance policies forbidding Chinese-authored software/weights, you will need non-Chinese alternatives.
    

### Recommended Configurations for Continue

Continue works best when you split roles between a fast **Autocomplete** model (Fill-in-the-Middle format) and a smart **Chat/Edit** model.

#### Option A: Top Overall Stack (Best Performance)

If you have no policy restrictions, this is the current gold standard setup for local AI coding:

|**Role**|**Model (ollama pull)**|**Why it's recommended**|
|---|---|---|
|**Tab Autocomplete**|`qwen2.5-coder:1.5b`|Blazing fast latency with surprisingly high completion accuracy.|
|**Chat & Edit (8–16GB RAM)**|`qwen2.5-coder:7b`|Excellent balance of coding logic and low VRAM usage.|
|**Chat & Edit (16–32GB RAM)**|`qwen2.5-coder:14b`|The sweet spot for complex refactoring and deep reasoning.|

#### Option B: Western / Non-Chinese Stack (Strict Compliance / Policy Safe)

If you prefer models developed in the US or Europe:

|**Role**|**Model (ollama pull)**|**Developer / Origin**|
|---|---|---|
|**Tab Autocomplete**|`codegemma:2b` or `starcoder2:3b`|Google (US) / BigCode (Open Community)|
|**Chat & Edit (8–16GB RAM)**|`llama3.1:8b` or `phi4`|Meta (US) / Microsoft (US)|
|**Chat & Edit (16–32GB RAM)**|`codestral` (22B)|Mistral AI (France)|

### Quick YAML Snippet (Western / Llama Stack)

If you want to stick with non-Chinese models in your `config.yaml`:

YAML

```
name: Western Local Stack
version: 1.0.0
schema: v1

models:
  - name: Llama 3.1 8B (Chat/Edit)
    provider: ollama
    model: llama3.1:8b
    apiBase: http://localhost:11434
    roles:
      - chat
      - edit

  - name: CodeGemma 2B (Autocomplete)
    provider: ollama
    model: codegemma:2b
    apiBase: http://localhost:11434
    roles:
      - autocomplete
```

What hardware specs (RAM and GPU/VRAM) are you running Ollama on? I can tailor the exact parameter sizes to fit your machine smoothly.


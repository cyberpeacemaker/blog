---
created: 2026-07-27 13:07
updated: 2026-07-27 13:07
tags: []
type: reference
lang: en
status: draft
---
Here is your step-by-step setup playbook. Because you have 32 GB of system RAM, your CPU will comfortably handle up to 7B or 8B parameter models. We will start with a tiny 135M model to verify the plumbing in under 60 seconds, then switch to `qwen2.5-coder:7b` for actual threat hunting rule generation.

### Phase 1: Verify & Spin Up Ollama

1. **Install Ollama** (if you haven't already):
    
    Download and run the installer from [ollama.com](https://ollama.com/).
    
2. **Pull the Ultra-Light PoC Model:**
    
    Open PowerShell and run:
    
    PowerShell
    
    ```
    ollama run smollm2:135m
    ```
    
    _(This downloads in seconds and opens an interactive chat prompt.)_
    
3. **Verify Local API Endpoint:**
    
    Type `/bye` to exit the terminal chat. Open your browser and navigate to:
    
    `http://localhost:11434`
    
    You should see a plain text page displaying: `Ollama is running`.
    

### Phase 2: Install & Configure Continue in VS Code

1. **Install Extension:**
    
    - Open **VS Code**.
        
    - Press `Ctrl + Shift + X` to open Extensions.
        
    - Search for **Continue** (by Continue.dev) and click **Install**.
        
    - You will see the Continue icon (a small box with an arrow) appear on your left sidebar.
        
2. **Configure Models in `config.json`:**
    
    - Click the **gear icon** $\mathbf{\ gear\ }$ at the bottom right of the Continue sidebar panel (or directly edit `%USERPROFILE%\.continue\config.json` in Windows).
        
    - Replace or update the `"models"` section in your configuration file with the following snippet:
        

JSON

```
{
  "models": [
    {
      "title": "PoC Fast Check (SmolLM2 135M)",
      "provider": "ollama",
      "model": "smollm2:135m",
      "apiBase": "http://localhost:11434"
    },
    {
      "title": "Threat Rule Engine (Qwen2.5 7B)",
      "provider": "ollama",
      "model": "qwen2.5-coder:7b",
      "apiBase": "http://localhost:11434"
    }
  ],
  "tabAutocompleteModel": {
    "title": "Qwen 1.5B Autocomplete",
    "provider": "ollama",
    "model": "qwen2.5-coder:1.5b"
  }
}
```

### Phase 3: Execute the PoC Validation

#### Step A: Validate Integration Plumbing

1. In the VS Code Continue sidebar, click the model selector dropdown at the bottom and select **PoC Fast Check (SmolLM2 135M)**.
    
2. Type a basic message in the chat box: `ping`
    
3. If you get an instantaneous response back in VS Code, **your VS Code $\leftrightarrow$ Continue $\leftrightarrow$ Ollama pipeline is 100% functional.**
    

#### Step B: Load the Target Threat-Hunting Model

1. In PowerShell, download the full coding model:
    
    PowerShell
    
    ```
    ollama pull qwen2.5-coder:7b
    ```
    
2. In the Continue sidebar dropdown in VS Code, switch to **Threat Rule Engine (Qwen2.5 7B)**.
    

#### Step C: Run the Benchmark Test

Paste the threat hunting test prompt directly into the Continue sidebar:

> "Convert this threat hypothesis into a SIGMA rule and a KQL query for Microsoft Sentinel: Detect unauthorized Modbus function code 16 (Write Multiple Registers) sent to PLC IP 192.168.1.50."

### Hardware Optimization Tip for CPU-Only Execution

Because your Intel Core 7 150U uses CPU system RAM rather than a dedicated Nvidia GPU, **generation speed will rely heavily on memory bandwidth.**

- `qwen2.5-coder:7b` will generate roughly 8–15 tokens per second on 32 GB RAM, which is completely usable for threat hunting tasks.
    
- If you ever test `qwen2.5-coder:14b`, generation will drop to ~2–4 tokens per second. Keep `7b` as your primary local workhorse.


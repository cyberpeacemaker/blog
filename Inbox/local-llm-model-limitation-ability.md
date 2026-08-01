---
created: 2026-08-01 19:08
updated: 2026-08-01 19:08
tags: []
type: reference
lang: en
status: draft
---
The error occurs because **Agent mode** is currently toggled on in Continue, but `smollm2:135m` does not support **tool/function calling** in Ollama.

## 🔍 What's Going On

1. **Agent Mode is Active:** In the left Continue panel, the prompt bar has the `Agent` chip selected. Agent mode allows the model to perform automated actions (like reading/writing files or running commands) by passing **tools** to the LLM.
    
2. **Model Limitation:** `SmolLM2 135M` is an ultra-lightweight model designed purely for basic text completion and fast checks. It lacks the fine-tuning and template support required for Ollama's tool-use API.
    
3. **The Rejection:** When Continue sends the prompt along with tool definitions to Ollama, Ollama rejects the request with `"smollm2:135m does not support tools"`.
    

## 🛠️ How to Fix It

### Option 1: Disable Agent Mode (To keep using SmolLM2)

If you just want a quick, lightweight check using `SmolLM2 135M`:

1. Click the **`Agent`** chip/dropdown in the prompt box on the left panel.
    
2. Switch it back to **Chat** or standard prompt mode (disabling agent tool calls).
    

### Option 2: Use a Tool-Capable Model (To keep using Agent Mode)

If you need Agent capabilities (file access, code execution, multi-step actions):

1. Switch your active model dropdown from `PoC Fast Check (SmolLM2 135M)` to **`Threat Rule Engine (Qwen2.5 7B)`**.
    
2. Models like **Qwen2.5 (7B+)**, **Llama 3.1 (8B)**, or **Mistral** support Ollama function calling natively and will work seamlessly in Agent mode.


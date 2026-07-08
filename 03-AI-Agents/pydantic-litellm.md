---
created: 2026-07-08 19:07
tags: []
type: reference
lang:
status: draft
---
Starting with a flat folder and a couple of script files is completely normal for a scratchpad. But to build a product that can seamlessly pivot from Claude to a local model, we need to transition that script into a modular architecture.

The strategy requires a **"Separation of Concerns"** layout. You want your data definitions, your AI prompts, and your application configuration living in entirely separate files.

## 📂 The Model-Agnostic Project Layout

If you initialize a modern Python project using **`uv`** (by running `uv init --app my-ai-product`), your repository should be organized to look like this:

Plaintext

```
my-ai-product/
├── .env                  # Your master control panel (API keys & model choices)
├── .gitignore            # CRITICAL: Keeps your .env file off GitHub
├── pyproject.toml        # Lists packages (uv, pydantic, litellm, etc.)
└── src/
    ├── __init__.py
    ├── config.py         # Safely loads variables from your .env file
    ├── schemas/          # The data "contracts" (Pydantic models)
    │   ├── __init__.py
    │   └── output_types.py
    ├── agents/           # Where prompts and LLM orchestrations live
    │   ├── __init__.py
    │   └── core_agent.py
    └── main.py           # Application entry point (triggers the automation)
```

## 🔍 Breaking Down the Structure

### 1. `.env` (The Master Switch)

Instead of writing your Claude API keys or the model name inside your Python files, you put them here.

Bash

```
# During PoC Phase:
LLM_MODEL_NAME="claude-3-5-sonnet"
ANTHROPIC_API_KEY="sk-ant-..."

# When you migrate to Local Phase later, you'll literally just change it to:
# LLM_MODEL_NAME="ollama/gemma4"
# OPENAI_API_BASE="http://localhost:11434"
```

### 2. `src/config.py` (The Environment Reader)

This script reads the `.env` file and makes those variables cleanly accessible across your application using standard python settings.

### 3. `src/schemas/output_types.py` (The Contract)

This is where you tell your app _exactly_ what kind of data structure you expect back from the AI. By using **Pydantic**, you define a standard Python class.

Python

```
from pydantic import BaseModel, Field

class AutomationTaskResult(BaseModel):
    summary: str = Field(description="A brief summary of what was processed")
    status: str = Field(description="Must be either 'success', 'failed', or 'requires_review'")
    extracted_data: list[str] = Field(description="List of key points extracted")
```

### 4. `src/agents/core_agent.py` (The Abstraction Layer)

This is the magic file. Instead of using Anthropic's specific code library, you use an abstraction tool like **LiteLLM**. It doesn't care if the model is from Claude or running locally on your laptop—it uses the exact same Python syntax.

Python

```
import os
import litellm
from src.schemas.output_types import AutomationTaskResult

def execute_ai_task(raw_input_text: str) -> AutomationTaskResult:
    # 1. Fetch whatever model is active in the .env file
    active_model = os.getenv("LLM_MODEL_NAME")
    
    # 2. Call the LLM (LiteLLM handles translating the request under the hood)
    response = litellm.completion(
        model=active_model,
        messages=[
            {"role": "system", "content": "You are a structured automation assistant."},
            {"role": "user", "content": raw_input_text}
        ],
        # Force the model to output the exact Pydantic schema structure
        response_format=AutomationTaskResult 
    )
    
    # 3. Return the clean, structured data
    return response.choices[0].message.content
```

### 5. `src/main.py` (The Orchestrator)

This is your actual automation engine. It loads your files, passes them to your agent, and performs the final action (like updating a database or saving a file). It has **zero idea** whether Claude or a local model did the heavy lifting.

## 🚀 Why This Protects You

By splitting your project this way, you achieve absolute independence. If you decide tomorrow that Claude is too expensive, or data credentials require you to move local immediately, you **do not touch** `main.py`, you **do not touch** `output_types.py`.

You spin up your local model server, edit the `LLM_MODEL_NAME` line in your `.env` file, and your entire application scales with the new backend instantly.

To help you lay this out on your computer: **What does your automation script currently do (e.g., parsing emails, generating code, reading files), and do you already have a framework you prefer using?**


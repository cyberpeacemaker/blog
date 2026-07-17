


```YAML
---
type: "guide"                      # Required: The concept category
title: "Setting up Postgres"       # Optional: Fallback is the filename
description: "How to spin up DB." # Optional: 1-sentence summary
tags: [database, setup]            # Optional: Categorization
status: "draft | active | deprecated" # Helps identify stale docs
resource: "db://postgres-prod"     # Optional: URI of the asset being described
timestamp: 2026-07-17T14:47:00Z    # Optional: ISO 8601 of last meaningful change
---
```

---

# Explanation
- **`type`**: (e.g., `architecture-decision`, `onboarding`, `api-spec`, `troubleshooting`). Agents behave significantly better when they know the _genre_ of the document they are parsing.    
- **`description`**: A highly concise, one-sentence summary. AI search tools (like semantic search) use this description field to quickly weigh the relevance of a document before grabbing the whole file.    
- **`verified`**: (e.g., `verified: true` or `verified_by: @human`). Since you work with AI, it's vital to avoid "hallucination loops" (where an AI reads inaccurate AI-generated code or docs). This tells the agent if a human has vetted the information.
- **`context_scope`**: (e.g., `frontend`, `billing-service`). This helps the AI narrow down exactly which boundary of your system this file belongs to.
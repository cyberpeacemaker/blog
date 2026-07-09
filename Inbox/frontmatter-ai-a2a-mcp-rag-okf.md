---
created: 2026-07-09 09:07
tags: []
type:
lang:
status: draft
---
Ah, designing for the **AI-as-a-reader** era! That changes the game completely. When you are optimizing for MCP (Model Context Protocol), RAG (Retrieval-Augmented Generation), and Agent-to-Agent (A2A) workflows, frontmatter isn't just metadata anymore—it is a **semantic API contract** for the LLM.

An LLM or an MCP server will read your frontmatter first to decide whether it even _needs_ to ingest or chunk the rest of the file. If your frontmatter is highly structured, it saves token context, speeds up vector DB filtering, and builds a better knowledge graph.

With that lens, your current schema is a great base, but we can make it highly performant for AI agents without ruining it for humans.

Here are the critical upgrades for an AI/RAG/MCP-first workflow:

## 1. The AI-Optimized Upgrades

### `domain` or `namespace` (For RAG Pre-filtering)

In RAG, doing a vector search across your _entire_ vault can surface irrelevant noise. If the AI can instantly pre-filter metadata by a high-level domain (e.g., `coding/python`, `business/finance`), the retrieval accuracy skyrockets.

### `relations` or `links` (For Knowledge Graphs & MCP)

Agents excel at traversing graphs. If a `howto` note depends on a `concept` note, explicitly stating that relationship in the frontmatter allows an AI agent to fetch the pre-requisite context using MCP tools without having to parse the raw markdown body text first.

### `visibility` or `security` (For Agent Privacy)

In A2A and RAG workflows, data leakage is a massive risk. An explicit visibility tag ensures your local MCP server or external AI agents know exactly what they are allowed to share, summarize, or expose to the public.

## The AI + Human Hybrid Schema

Here is how to structure it so it's clean for you to write, but highly functional for an LLM:

YAML

```
---
title: "Clear, Semantic Title"
description: "Punchy SEO summary + core semantic intent for RAG/vector filtering."
created: YYYY-MM-DD
updated: YYYY-MM-DD        # Crucial for AI to know if the knowledge is stale
type: howto                # reference | howto | hub | concept — vital for MCP routers
lang: en
draft: true

# --- AI & Agent Enhanced Fields (Infer these where possible!) ---
domain: ""                 # e.g., tech/ai, life/health — narrows RAG search scope
relations: []              # [slug-of-parent, slug-of-related] — builds the AI graph
prerequisites: []          # What the human (or agent) needs to know before reading
visibility: "private"      # private | internal | public — guards against AI data leakage
tags: []                   # For hybrid (keyword + vector) RAG search
---
```

## Why this works so well for AI:

- **The Router Advantage (`type`):** If a user asks an MCP agent, _"How do I set up Docker?"_, the agent can query your database to only look at files where `type: howto`. It instantly ignores `reference` or `hub` files, saving time and tokens.
    
- **The Freshness Factor (`updated`):** If an agent is answering a question based on your notes, it can check `updated`. If it sees the note is from 3 years ago, the agent can intelligently warn the user: _"Based on your notes (which haven't been updated since 2023)..."_
    
- **Context Truncation (`description`):** When an agent is looking at a list of 50 potential files via an MCP tool, it can just read the `title` and `description` of those 50 files to choose the best 3, rather than reading the full text of all 50.
    

Since you mentioned inferring fields like `type`, `lang`, and `tags`, you could easily write a small Python script or use an LLM pipeline to automatically populate the `domain` and `relations` fields based on the links in the body text as well.

What kind of system or agent pipeline are you building to ingest these files? (e.g., a custom LangChain/LlamaIndex RAG, an Anthropic MCP server, or something like Obsidian/Logseq with AI plugins?)


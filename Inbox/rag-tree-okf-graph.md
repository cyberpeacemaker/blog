---
title: "RAG Trees, OKF Graphs, and Agent-Legible Knowledge"
description: "Explains how folder namespaces and MOC links make Obsidian notes easier for AI agents to retrieve and traverse."
created: 2026-07-09
updated: 2026-07-09
tags: [ai, agents, obsidian]
type: reference
lang: en
status: draft
---

> Related: [[MOC - AI Agents]] · [[yaml-okf]] · [[RAG-OKF]] · [[frontmatter-schema]]

# RAG Trees, OKF Graphs, and Agent-Legible Knowledge

You have mapped this out **perfectly**. Your intuition is spot-on. What you are seeing here is the formal blending of traditional human-centric note-taking structures (Trees and Graphs) into formats explicitly optimized for **AI Agents**.

Here is exactly how your ideas connect to these technical RAG and agent concepts.

## 1. The "Tree" Structure: Domain & Namespace Filtering

When the text talks about **domains or namespaces** (e.g., `coding/python` or `business/finance`), it is advocating for a **hierarchical tree or folder structure**.

- **The Problem with Standard RAG:** Traditional vector search (semantic search) is "flat." It dumps your entire vault into one giant pool and searches for similar words. This creates noise—searching for "Python" might surface a note about coding _and_ a snake note from your biology class.
    
- **The Tree Fix:** By using namespaces (like folder structures or high-level category tags), the AI can instantly prune the tree. It tells the vector database: _"Ignore everything else, only search inside the `/coding/python` branch."_ This eliminates irrelevant context before the search even begins.
    

## 2. The "Graph" & MOC Structure: Relations & OKF

When the text talks about **explicit relations in the frontmatter** to fetch prerequisites via MCP (Model Context Protocol), it is describing a **network graph**. This is exactly how **Obsidian, MOCs (Maps of Content), and the Open Knowledge Format (OKF)** function.

- **The Obsidian & MOC Connection:** In Obsidian, you use `[[WikiLinks]]` and MOCs to connect ideas dynamically, creating a structural web.
    
- **The AI Optimization (OKF):** The **Open Knowledge Format (OKF)** specification formalizes this exact pattern for LLMs. It uses standard Markdown files with YAML frontmatter to explicitly state relationships (e.g., `type: playbook`, `depends_on: concepts/python-basics`).
    
- **How Agents Use It:** Instead of guessing what is relevant via a math-heavy vector search, an AI agent using MCP tools can look at a note's frontmatter, see that it connects to a prerequisite note, and immediately jump along that graph link to fetch it. The AI navigates your vault exactly like a human clicking through an Obsidian MOC.
    

### Concept Mapping

|**AI / RAG Concept**|**Knowledge Management Equivalent**|**How the AI Uses It**|
|---|---|---|
|**Domain / Namespace**|Folders / Hierarchical Tags (**Tree**)|**Pre-filtering:** Narrows down the search pool instantly to prevent noise.|
|**Relations / Frontmatter Links**|Wiki-links / MOCs (**Graph**)|**Graph Traversal:** Allows AI agents (via MCP) to follow direct links to prerequisite context without guessing.|

### The Big Picture: Making Knowledge "Agent-Legible"

For years, the goal of frameworks like LYT (Linking Your Thinking) and MOCs was to make knowledge easy for _your human brain_ to navigate. Now, frameworks like OKF are standardizing those exact same graph and tree patterns so they are **agent-legible**. You aren't changing the organic way you link notes; you are just exposing that mental map to the AI in a clean, structured way it can easily parse.

Are you looking to restructure an existing Obsidian vault to make it more AI-friendly, or are you building a custom RAG/agent system from scratch?


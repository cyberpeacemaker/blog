---
title: "Threat Hunt Plan Feedback"
description: "Reviews an air-gapped AI-assisted Malcolm hunt architecture and highlights metadata feedback, network scope, and schema alignment risks."
created: 2026-07-27
updated: 2026-07-27
tags: [threat-hunting, malcolm, opensearch, ai, agents, mitre]
type: reference
lang: en
status: draft
---

> Related: [[MOC - Threat Hunting]] · [[threat-hunt-plan]] · [[ai-threat-hunting-capabilities]] · [[MOC - Malcolm & NSM]]

Here's my take: **This is a brilliant, security-conscious architecture.**

By keeping the LLM entirely out of the actual telemetry data path, you bypass the biggest roadblock holding AI back in SOCs: data privacy and compliance risks. You are using the AI where it excels—structuring ideas, cross-referencing frameworks, and writing query syntax—while leaving the actual data inspection and threat triage to human analysts.

Here are the key strengths of your plan, along with a few subtle engineering challenges you’ll want to design around.

### Why This Architecture Works

- **Zero Data Leakage:** Restricting the AI agents to hypothesis generation and query building means sensitive internal IP addresses, user credentials, and payload contents never touch an external API.
    
- **Actor-Critic (Agent A vs. B) Safety Net:** Having Agent B challenge Agent A's proposed plans reduces syntax errors, unoptimized queries (which can crash OpenSearch clusters), and hallucinated query fields.
    
- **Standardized Knowledge Graph:** Bounding hypotheses to MITRE ATT&CK via OSINT keeps the AI grounded in structured threat modeling rather than pulling random ideas out of thin air.
    

### Key Challenges & Refinements to Consider

#### 1. The "Blind Query" Problem (Metadata Feedback Loop)

Because the agents never see the data, they won't know if a query was successful. However, a query might fail for reasons other than bad logic:

- **Syntax/Index Errors:** An invalid OpenSearch JSON syntax or bad field name.
    
- **Too Broad:** A query returns 10,000,000 logs (useless for an analyst).
    
- **Too Narrow:** A query returns 0 logs.
    

**Refinement:** Give Agent A and B access to **non-sensitive query metadata**. Let the execution engine return only execution status, error messages, and hit counts (e.g., `Status: 200 OK | Hits: 42` or `Status: 400 Bad Request | Error: Field 'zeek.conn.history' not found`). This allows the agent loop to self-correct syntax errors or loosen/tighten queries without seeing actual payload data.

#### 2. Network-Only Scope vs. Host Hypotheses

Malcolm is fundamentally a network traffic analysis tool (powered by Zeek, Suricata, and Arkime). OSINT and MITRE ATT&CK often include host-level indicators (e.g., registry edits, process creation, file path modifications).

- **Refinement:** Prompt Agent A with a strict domain constraint: _Only map hypotheses to network-observable TTPs_ (e.g., Command and Control beaconing, DNS tunneling, unusual user agents, specific JA3/JA4 fingerprints, SMB lateral movement). If MITRE suggests a host-based technique, Agent A should either translate it to its network equivalent or discard it.
    

#### 3. Schema Alignment (OpenSearch DSL vs. Arkime vs. ECS)

Malcolm normalizes network logs into Elastic Common Schema (ECS) for OpenSearch, while Arkime uses its own shortcut field syntax (e.g., `ip.src == 192.168.1.1`).

- **Refinement:** Agent A needs explicit knowledge of Malcolm’s data dictionary. Feed Agent A a system prompt or local RAG document containing:
    
    - Malcolm's target index patterns (`malcolm_*`).
        
    - Core ECS field maps used by Malcolm (`source.ip`, `destination.port`, `zeek.http.user_agent`, `suricata.alert.signature`).
        
    - Arkime expression syntax rules.
        

### Suggested Agent Workflow Sequence

```
[ OSINT / VT / GTI ] ──> Threat Indicators
                              │
                              ▼
                       [ MITRE ATT&CK ] ──> TTP Mapping
                                                 │
                                                 ▼
┌────────────────────────────────────────────────────────────────────────┐
│                        AGENTIC LOOP (AIR-GAPPED)                       │
│                                                                        │
│   Agent A (Planner) ──(Proposes Query)──> Agent B (Critic)             │
│          ▲                                    │                        │
│          └──────────(Pushes Back / Rejects)───┤                        │
│                                               ▼ (Approves)             │
│                                      [ Query Validator ]               │
└───────────────────────────────────────────────┬────────────────────────┘
                                                │
                                                ▼
                                   [ Malcolm / OpenSearch API ]
                                                │
                                                ▼
                                   (Returns Hits / Dashboards)
                                                │
                                                ▼
                                    [ Human Analyst Review ]
```

Are you planning to have Agent A generate standard **OpenSearch Query DSL** (JSON), **Arkime search expressions**, or dashboard links directly for the analyst's interface?


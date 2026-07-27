---
created: 2026-07-27 14:07
updated: 2026-07-27 14:07
tags: []
type: reference
lang: en
status: draft
---
Here is your updated, streamlined threat hunting plan incorporating your refinements:

### Refined Threat Hunting Plan

**Phase 1: OSINT & TTP Mapping**

- **Ingest & Enrich:** Query VirusTotal / GTI APIs for OSINT indicators (hashes, IPs, domains).
    
- **MITRE Mapping:** Map OSINT to MITRE ATT&CK TTPs.
    
- **Network Scope Filter:** Agent A translates host-based techniques into network-observable equivalents or explicitly flags them as **"unreachable"** (out of scope for Malcolm).
    

**Phase 2: Agentic Query Synthesis (Agent A vs. B)**

- **Hypothesis & Query Formulation (Agent A):** Drafts hypothesis and proposed Malcolm query parameters (OpenSearch DSL / Arkime syntax) based on valid network TTPs.
    
- **Adversarial Review (Agent B):** Challenges Agent A's query logic, safety, and field mapping. Rejects back to Agent A for revision until approved.
    

**Phase 3: Automated Execution & Metadata Feedback**

- **API Execution:** Send approved queries to Malcolm’s APIs (OpenSearch / Arkime).
    
- **Metadata Loop:** Return **non-sensitive execution metadata only** (HTTP status codes, syntax/field errors, total hit counts) back to Agents A & B so they can self-correct broken syntax or over/under-scoped queries automatically.
    

**Phase 4: Air-Gapped Human Investigation**

- **Data Boundary:** Raw telemetry, payloads, and internal log contents never leave Malcolm or touch the LLM.
    
- **Analyst Triage:** Human analysts log into Malcolm to view the populated query results and conduct the actual threat investigation.
    

Would you like to draft the system prompt for Agent A's TTP translation step, or focus on defining Agent B's validation criteria first?


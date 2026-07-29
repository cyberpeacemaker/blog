---
title: "Malcolm API Scripting Strategy"
description: "Splits Malcolm automation between OpenSearch APIs for aggregations and Arkime APIs for packet-level evidence."
created: 2026-07-28
updated: 2026-07-28
tags: [malcolm, nsm, opensearch]
type: reference
lang: en
status: draft
---

> Related: [[MOC - Malcolm & NSM]] · [[malcolm-api-example]] · [[arkime-api]] · [[opensearch-api-dsl-dev-tools]]

Here is my recommendation: **Split your API strategy based on the task.** Use the **Arkime Viewer API** when your script needs raw PCAPs or packet-level payloads, but query the **OpenSearch REST API** directly when automating macro analytics, aggregations, or reports.

Even though you _can_ hit Arkime’s underlying aggregation endpoints (like `/spiview.json`), OpenSearch is vastly superior for scripting macro views.

## 1. Scripting Macro Views & Aggregations: Use OpenSearch API

When writing scripts for metrics, alerting, statistical reporting, or threat hunting across Malcolm, target OpenSearch directly (either via standard port `9200` or through Malcolm's proxy endpoint at `/mapi/opensearch/`).

### Why OpenSearch API is better for scripting macro data:

- **Full Aggregations DSL:** Arkime’s API only returns simplified term counts tailored for its own UI widgets. The OpenSearch API gives you full access to native Aggregation DSL—including multi-level bucket aggregations (e.g., _Group by Source IP $\rightarrow$ sub-group by SSL Issuer_), metric aggregations (`avg`, `sum`, `percentiles`, `cardinality`), and pipeline aggregations.
    
- **Standardized SDKs:** You can use official, well-maintained client libraries like `opensearch-py` (Python) or `@opensearch-project/opensearch` (Node.js) rather than writing custom HTTP wrappers for Arkime's internal UI endpoints.
    
- **Broader Log Access:** OpenSearch API lets you query non-PCAP logs in Malcolm simultaneously—such as Suricata signatures, standalone Zeek protocol logs (`dns.log`, `kerberos.log`), YARA matches, and file extraction metadata.
    

Python

```
# Example: Using Python's opensearch-py to fetch Top 10 Zeek Notices
from opensearchpy import OpenSearch

client = OpenSearch(
    hosts=[{'host': 'malcolm-host', 'port': 9200}],
    http_auth=('username', 'password'),
    use_ssl=True, verify_certs=False
)

query = {
    "size": 0,  # Don't return individual documents, just the aggregation
    "query": { "term": { "event.dataset": "notice" } },
    "aggs": {
        "top_notices": {
            "terms": { "field": "zeek.notice.note.keyword", "size": 10 }
        }
    }
}

response = client.search(body=query, index="malcolm_zeek_*")
```

## 2. Scripting Micro Views & PCAPs: Use Arkime API

When your script needs to act on specific network sessions or retrieve actual packet data, target the **Arkime Viewer API** (accessible directly or via Malcolm’s `/arkime/api/` proxy route).

### Best scripting tasks for Arkime API:

- **Downloading PCAP Files:** Fetching raw binary `.pcap` files for a given session ID or time frame (e.g., `GET /sessions.pcap?ids=...`).
    
- **Extracting Reassembled Payloads:** Getting decoded TCP streams in ASCII, hex, or raw formats for deep payload inspection.
    
- **Session Management:** Automatically adding tags, notes, or state markers to sessions inside the Arkime database during an incident response workflow.
    

Bash

```
# Example: Fetching a raw PCAP file for a session via Arkime API
curl -s -u "user:pass" \
  "https://malcolm-host/arkime/api/sessions.pcap?ids=240425-Qgw8-dSZF0oWvlkuEnDLkw" \
  -o evidence.pcap
```

## Scripting Strategy Summary

Plaintext

```
                       ┌─────────────────────────┐
                       │  Your Python / Bash     │
                       │    Automation Script    │
                       └────────────┬────────────┘
                                    │
           ┌────────────────────────┴────────────────────────┐
           │                                                 │
  (Macro / Aggregations)                          (Micro / Raw PCAPs)
           │                                                 │
           ▼                                                 ▼
┌─────────────────────┐                           ┌─────────────────────┐
│  OpenSearch API     │                           │   Arkime Viewer     │
│  (/mapi/opensearch) │                           │   (/arkime/api)     │
└──────────┬──────────┘                           └──────────┬──────────┘
           │                                                 │
           ▼                                                 ▼
 Returns: Metrics, Buckets,                        Returns: Raw .pcap bytes,
 JSON Aggregations, Logs                           Session Payloads, Tags
```

Are you looking to write a python script for automated threat hunting, or are you trying to build a pipeline that extracts PCAPs based on specific triggered alerts?


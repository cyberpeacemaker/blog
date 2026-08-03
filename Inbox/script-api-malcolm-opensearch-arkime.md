---
created: 2026-08-03 16:08
updated: 2026-08-03 16:08
tags: []
type: reference
lang: en
status: draft
---
**No, you do not have to search OpenSearch first and pivot.**

You can interact **100% via Arkime’s API** if your tool’s main goal is to query session metadata or download raw PCAP files.

However, whether you should use **Arkime’s API**, **OpenSearch’s API**, or a **Hybrid Approach** depends entirely on what data your script needs to consume.

## Choosing the Right API for Your Script

|**API Approach**|**Best Used For**|**Key Capabilities**|**Limitations**|
|---|---|---|---|
|**Arkime REST API**|• Pulling session summaries<br><br>  <br><br>• Automating raw PCAP downloads<br><br>  <br><br>• Triggering background payload regex hunts|• Native Arkime expression queries (`ip.src == 10.0.0.1`)<br><br>  <br><br>• Directly streams `.pcap` byte streams<br><br>  <br><br>• Handles session aggregation out of the box|• Cannot query raw Zeek fields or Suricata alerts that aren't mapped to Arkime's schema.|
|**OpenSearch REST API**|• Protocol log ingestion & analysis<br><br>  <br><br>• Suricata alert parsing<br><br>  <br><br>• Custom metrics, aggregations, & dashboards|• Full access to _every_ raw field in Zeek (`zeek.dns`, `zeek.ssl`) and Suricata (`suricata.eve`)<br><br>  <br><br>• Complex Lucene / PPL queries|• **Cannot extract raw PCAPs** from disk.|

## 3 Common Scripting Design Patterns

### Pattern A: Arkime API Only (PCAP & Session Extraction)

If your script just wants connection metadata or needs to carve raw `.pcap` files based on IP addresses, ports, or timeframes, **use Arkime's API directly**.

- **How it works:** Your script sends a request to Arkime's viewer API endpoint (`/api/v1/sessions` or `/sessions.pcap?expression=...`).
    
- **Under the hood:** Arkime’s API handler queries OpenSearch internally, extracts the session pointers, fetches the raw PCAP bytes from disk if requested, and returns JSON or a downloadable `.pcap` binary stream.
    

Bash

```
# Example: Using Arkime API to download a PCAP directly via curl
curl -u admin:password \
  "https://malcolm.local/arkime/sessions.pcap?expression=ip==192.168.1.50&date=-1" \
  -o traffic.pcap
```

### Pattern B: OpenSearch API Only (Analytics & Alert Ingestion)

If your script is a SIEM connector or anomaly detection bot that analyzes logs, count statistics, or alert hits, **query OpenSearch's REST API directly**.

- **How it works:** Query the OpenSearch indices directly (e.g., `POST /malcolm_zeek-*/_search`).
    
- **Why do this?** It gives your script complete, unformatted access to custom Zeek protocol fields (e.g., DNS query response codes, TLS certificate validation states, HTTP user-agents) that Arkime’s abstraction layers omit.
    

### Pattern C: Hybrid Workflow (Automated Alert-to-PCAP Pipeline)

This is the most common pattern for **SOAR playbooks and automated incident response scripts**:

```
[ Step 1: OpenSearch API ]                   [ Step 2: Extract ID ]              [ Step 3: Arkime API ]
 Query raw Zeek/Suricata logs    ----->    Grab the `community_id`     ----->   Fetch raw PCAP file using
 for high-severity threat alerts           or session timestamp + 5-tuple        the identifier as the query
```

1. **Query OpenSearch** to detect complex events (e.g., a specific Suricata rule firing alongside an unusual Zeek HTTP transfer).
    
2. **Extract the `community_id`** (a standardized hash shared across Malcolm's logs) from the search result.
    
3. **Query Arkime API** passing `community_id == <hash>` to instantly download the exact raw PCAP segment corresponding to that alert.
    

What programming language (Python, Go, Bash) are you planning to write your script in, and are you aiming to extract raw PCAPs or parse log statistics?


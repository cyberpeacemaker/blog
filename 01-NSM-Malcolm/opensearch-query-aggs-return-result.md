---
title: "OpenSearch Query Aggregations and Returned Results"
description: "Explains OpenSearch search endpoints, size zero responses, and aggregations for grouped summary results."
created: 2026-07-23
updated: 2026-07-24
tags: [opensearch, nsm]
type: reference
lang: en
status: draft
---

> Related: [[MOC - OpenSearch Querying]] · [[opensearch-request]] · [[arkime-query-opensearch]]

Now that you have the **`query`** (the filter logic) down, you are looking at the overall **Search & Aggregation structure**.

In SQL terms, the `query` part is your `WHERE` clause, while this outer part controls **how many raw rows you return** and **how you perform a `GROUP BY`** on the filtered results.

## 1. The Endpoint: `POST arkime_sessions3-*/_search`

- **`arkime_sessions3-*`**: The target index pattern. The asterisk (`*`) is a wildcard, meaning this query searches across **all indices** starting with `arkime_sessions3-` (e.g., daily logs like `arkime_sessions3-240425`).
    
- **`/_search`**: The standard REST API endpoint used to run searches in OpenSearch / Elasticsearch.
    

## 2. Top-Level `"size": 0`

- **What it does:** Tells OpenSearch: _"Return **0 raw documents** (hits) in the response."_
    
- **Why use it?** Since you only care about summary statistics (counts of IPs), you don't want the server sending thousands of raw log lines back over the network. Setting `"size": 0` drastically speeds up response time and saves memory.
    

## 3. `"aggs"` (Aggregations = `GROUP BY`)

The `"aggs"` block allows you to group data and compute metrics. Think of it like a **Pivot Table in Excel** or a **`GROUP BY` in SQL**.

### Breakdown of the Aggregation Block:

- **`"all_unknown_private_ips"`**:
    
    This is a **custom label** chosen by the person who wrote the query. You can name this anything (e.g., `"top_ips"` or `"ip_summary"`). OpenSearch will use this name as the key in the JSON response.
    
- **`"terms"` Aggregation**:
    
    > ⚠️ **Crucial Distinction:**
    > 
    > Earlier we saw **`term`** (singular) in a query, which means _"Find an exact match"_.
    > 
    > Here, **`terms`** (plural) inside an `aggs` block means _"Group by unique values in this field"_.
    
- **`"field": "destination.ip"`**:
    
    Tells OpenSearch which column/field to group by.
    
- **`"size": 200`** _(Inside aggs)_:
    
    Limits the aggregation output to the **top 200 unique IP buckets**.
    
- **`"order": {"_count": "desc"}`**:
    
    Sorts the resulting IP groups by the number of log events (`_count`) in **descending** order. The destination IPs with the highest traffic volume appear at the top.
    

## Putting It All Together (Plain English)

This entire query tells OpenSearch:

> _"Look across all `arkime_sessions3-*` log indices. Filter for logs tagged **BEC** from **April 25–26, 2024**, targeting **internal private IPs** (excluding the specified subnets). **Don't show me the individual log entries** (`size: 0`). Instead, **group the results by destination IP** and give me the **top 200 most frequent target IPs**, sorted from highest count to lowest."_

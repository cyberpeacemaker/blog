---
title: "OpenSearch Term Range and Match Queries"
description: "Compares term, range, and match query clauses and when to use exact, boundary, or full-text search."
created: 2026-07-23
updated: 2026-07-24
tags: [opensearch, nsm]
type: reference
lang: en
status: draft
---

> Related: [[MOC - OpenSearch Querying]] · [[opensearch-request]] · [[opensearch-must-filter]]

## Is "term" an Abbreviation?

**No, `term` is the full name.**

It is not an acronym or short for anything. In Information Retrieval (the science behind search engines), a **"term"** refers to a single, exact token or word saved in a search engine’s inverted index.

## 1. `term` Query (Exact Match)

- **What it does:** Searches for an **exact match** for a specific single token stored in the database.
    
- **Text Analysis:** **Does NOT analyze** the search input. It checks the value character-for-character as provided.
    
- **Best used for:** Machine-readable data, tags, status codes, user IDs, dates, or boolean flags (usually stored in `keyword` data types).
    

JSON

```
{"term": {"status": "active"}}
```

> **How it behaves:** Looks for documents where the `status` field is exactly the string `"active"`. If the field has `"Active"` (capital A), it won't match unless the index stored it in lowercase.

## 2. `range` Query (Boundary Filtering)

- **What it does:** Finds documents where a field falls **within a specified numerical, date, or IP range**.
    
- **Parameters used:**
    
    - `gte`: Greater than or equal to ($\ge$)
        
    - `gt`: Greater than ($>$)
        
    - `lte`: Less than or equal to ($\le$)
        
    - `lt`: Less than ($<$)
        
- **Best used for:** Numbers, timestamps, prices, dates, IP ranges.
    

JSON

```
{
  "range": {
    "price": {
      "gte": 10,
      "lte": 50
    }
  }
}
```

> **How it behaves:** Finds all products priced between $10 and $50, inclusive.

## 3. `match` Query (Full-Text Search)

- **What it does:** Performs a **full-text search** designed for human language.
    
- **Text Analysis:** **Applies an analyzer** to your query string before searching. It converts text to lowercase, breaks sentences into individual words, removes punctuation, and can handle stemming (e.g., matching "running" with "run").
    
- **Best used for:** Unstructured human-readable text like blog posts, email bodies, product descriptions, or log messages (stored in `text` data types).
    

JSON

```
{"match": {"description": "quick brown fox"}}
```

> **How it behaves:** Elasticsearch analyzes `"quick brown fox"` into three separate terms (`quick`, `brown`, `fox`). It will find documents containing **any** of those words by default.

## Summary Comparison

| **Query**   | **What It Looks For**             | **Analyzer Used?** | **Typical Field Type** | **Example Use Case**                                  |
| ----------- | --------------------------------- | ------------------ | ---------------------- | ----------------------------------------------------- |
| **`term`**  | Exact value match                 | **No**             | `keyword`, `integer`   | User ID (`1234`), Status (`"SUCCESS"`), Tag (`"BEC"`) |
| **`range`** | Values between upper/lower bounds | **No**             | `long`, `date`, `ip`   | Timestamps, price ranges, IP subnets                  |
| **`match`** | Human text (words, phrases)       | **Yes**            | `text`                 | Searching article content or email bodies             |

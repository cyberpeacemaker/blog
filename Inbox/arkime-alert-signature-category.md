---
created: 2026-07-21 16:07
updated: 2026-07-21 16:07
tags: []
type: reference
lang: en
status: draft
---
To find Suricata alerts in OpenSearch when you don't know the exact field name or full alert title, you can use **wildcards** and **phrase matching**.

Depending on whether you are using the **OpenSearch Dashboards UI** or the **OpenSearch REST API (Query DSL)**, here is how to construct your search.

## 1. Using the OpenSearch Dashboards UI (Search Bar)

If you are using the Discover tab or search bar in OpenSearch Dashboards, use standard **Lucene syntax**.

### **All-Field Wildcard Search (Easiest)**

If you have no idea what field the text lives in, search across all fields:

Plaintext

```
*dnp3* OR "*pulse off*"
```

- **`*dnp3*`**: Matches `dnp3` anywhere inside a word or string (e.g., `SURICATA DNP3 Request`, `dnp3_read`).
    
- **`"*pulse off*"`**: The quotes ensure the phrase `"pulse off"` is searched together, and the surrounding `*` wildcards capture any text before or after it.
    

### **Targeting Common Suricata Fields**

Suricata alert names are almost always stored in `alert.signature` (or `alert.category` / `payload`). If you want a cleaner search targeting the most likely fields:

Plaintext

```
alert.signature: (*dnp3* OR "*pulse off*")
```

## 2. Using the OpenSearch REST API (Query DSL)

If you are querying OpenSearch programmatically or through Dev Tools, the **`query_string`** query is the most flexible option because it supports wildcards and boolean operators across all fields.

### **Query Example**

JSON

```
GET /suricata-*/_search
{
  "query": {
    "query_string": {
      "query": "*dnp3* OR \"pulse off\"",
      "analyze_wildcard": true
    }
  }
}
```

### **Targeting Specific Fields (Recommended for Performance)**

If you want to restrict the search to fields typical for Suricata events without needing the exact field name, you can use wildcards in the field names using a `multi_match` query:

JSON

```
GET /suricata-*/_search
{
  "query": {
    "multi_match": {
      "query": "dnp3",
      "fields": ["alert.*", "payload*"],
      "type": "phrase_prefix"
    }
  }
}
```

## Quick Tips for Suricata in OpenSearch

- **Case Sensitivity:** Wildcard searches (using `*`) on `keyword` fields are case-sensitive by default, whereas standard `text` fields are lowercase-analyzed. Using lower-case terms (e.g., `dnp3` instead of `DNP3`) usually yields better results.
    
- **Common Field Names to Inspect:** If you want to check where your alerts usually land, look at these standard fields in your document:
    
    - `alert.signature` (The rule title)
        
    - `alert.category` (e.g., `A Network Trojan was Detected`)
        
    - `payload_printable` or `raw_data`
        

Are you querying through the **OpenSearch Dashboards UI** or via **API/Dev Tools**? If you're seeing unexpected results, I can help you tune the query based on your index mapping.


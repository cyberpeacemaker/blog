---
created: 2026-05-27
tags: [arkime, opensearch]
type: reference
lang: en
status: draft
---

> Related: [[MOC - OpenSearch Querying]] · [[MOC - Malcolm & NSM]] · [[06-03-arkime-api]] · [[05-27-malcolm-opensearch-json-dsl]]

Arkime (formerly Moloch) sits on top of the exact same OpenSearch/Elasticsearch backend as Malcolm, so the final destination is the same: **it all has to become an OpenSearch JSON Query DSL.** However, *how* Arkime gets there is completely different.

While Malcolm’s Dashboards pass your Lucene/DQL searches fairly directly to the database, Arkime uses its own custom, highly engineered expression parser built into its Node.js Viewer application.

Here is exactly how Arkime handles the translation from what you type to what the database sees.

### 1. The Custom Arkime Parser

When you type an expression into Arkime like `ip.src == 10.0.0.5 && port == 443`, you aren't writing Lucene. You are writing Arkime’s proprietary query language.

When you hit search, the Arkime Viewer backend parses that string, maps those field aliases (`ip.src` to `source.ip`), and automatically builds the OpenSearch JSON payload for you.

### 2. Heavy Bias Toward `filter` Context

Because Arkime is designed specifically to chew through massive amounts of network packet metadata (PCAPs), it is obsessed with speed.

Unlike a standard text search where you might want to "score" how relevant a log is, network data is highly structured. An IP address either matches or it doesn't. A port is either 443 or it isn't. You rarely care about "relevance scoring" in packet analysis.

Because of this, **Arkime forces almost everything into the `filter` block of the JSON DSL.** By wrapping your IP, port, protocol, and byte-count searches into strict `filter` clauses alongside your time window, Arkime ensures that OpenSearch bypasses all the expensive scoring math and relies entirely on lightning-fast, cached bitsets.

### 3. What Arkime's JSON Looks Like

If you search Arkime for a specific source IP over a specific timeframe, Arkime's Node.js viewer quietly compiles it into a payload that looks remarkably similar to this:

```json
{
  "query": {
    "bool": {
      "filter": [
        {
          "range": {
            "firstPacket": {
              "gte": 1716336000000,
              "lte": 1716422400000
            }
          }
        },
        {
          "term": {
            "source.ip": "10.0.0.5"
          }
        }
      ]
    }
  }
}

```

*Notice there isn't even a `must` clause here.* Because there is no fuzzy text to score, Arkime just builds an array of strict filters.

### The Exception: Global Text Searches

If you *do* force Arkime to do a global text search or a wildcard string match (e.g., searching for `payload == "*password*"`), Arkime's parser will recognize that it needs to evaluate text. In those specific scenarios, it will drop a `query_string` or `wildcard` clause into the `must` block so the database can actually parse and score the text strings.

**In short:** Arkime acts as a very smart middleman. It takes a syntax designed for network analysts and writes the most highly optimized OpenSearch JSON possible, heavily leaning on `filter` caching to keep your packet searches fast.

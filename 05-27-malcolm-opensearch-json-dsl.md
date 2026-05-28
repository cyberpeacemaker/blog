Yes, absolutely. You've got it exactly right.

In the Malcolm web GUI (which is powered by OpenSearch Dashboards, a fork of Kibana), everything you interact with visually on the dashboard is ultimately compiled into a single, unified JSON payload. This payload is written in **OpenSearch Query DSL** (Domain Specific Language) and is sent directly via an API request to the OpenSearch backend document store.

Here is exactly how the dashboard translates your visual inputs into that single JSON DSL format.

### The GUI to JSON Mapping

When you execute a search, OpenSearch wraps all your inputs into a single boolean (`bool`) query structure.

| Malcolm GUI Element | OpenSearch JSON DSL Clause | How it works under the hood |
| --- | --- | --- |
| **Search Bar (Lucene)** | `query_string` | The one-line text bar takes your Lucene syntax and wraps it in a parser that the backend can understand. |
| **Time Window** | `range` | The time picker is translated into a strict greater-than-or-equal-to (`gte`) and less-than-or-equal-to (`lte`) boundary, usually applied to the `@timestamp` field. |
| **UI Filters (Pills)** | `term`, `terms`, or `match` | The clickable filters you add below the search bar are appended as exact-match filters to ensure the backend only returns data matching those specific fields. |

---

### What the Unified JSON Looks Like

If you were to intercept the network request your browser makes to the Malcolm backend, or if you wanted to query the OpenSearch API directly yourself via the command line, the compiled JSON DSL would look something like this:

```json
{
  "query": {
    "bool": {
      "must": [
        {
          "query_string": {
            "query": "destination.port: 443 OR source.ip: 10.0.0.5",
            "analyze_wildcard": true
          }
        }
      ],
      "filter": [
        {
          "range": {
            "@timestamp": {
              "gte": "2026-05-20T00:00:00.000Z",
              "lte": "2026-05-27T23:59:59.999Z"
            }
          }
        },
        {
          "term": {
            "network.transport": "tcp"
          }
        }
      ]
    }
  }
}

```

**Breaking down the JSON:**

* **`bool`**: The parent wrapper that tells the backend "I have multiple conditions that must be met."
* **`must`**: This array contains your **Lucene search bar** query. It scores how well the documents match your search string.
* **`filter`**: This array contains your **time window** (`range`) and your **dashboard filters** (`term`). Filters act as strict yes/no gates and are heavily cached by the backend for performance, which is why the time window and UI filters are separated from the text search bar in the JSON structure.

So, whenever you are clicking around in Malcolm, you are essentially just visually building this exact JSON DSL structure!
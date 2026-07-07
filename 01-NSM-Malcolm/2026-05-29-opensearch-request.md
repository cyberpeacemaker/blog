---
created: 2026-05-29
tags: [malcolm, nsm, opensearch]
type: reference
lang: en
status: draft
---

Instead of returning individual logs, this query acts like a specialized report. It filters for a specific timeframe and protocol, and then summarizes (aggregates) the top email subjects, senders, recipients, and encryption statuses.

Here is a step-by-step breakdown of what each part of the query does:

### 1. The Endpoint

```json
POST /arkime_sessions3-*/_search

```

* This tells OpenSearch to run a search across all indices that match the pattern `arkime_sessions3-*`. These are standard indices used by Arkime to store network session metadata.

### 2. Search Size

```json
"size": 0,

```

* This instructs OpenSearch **not** to return the actual raw documents (logs) that match the search. Setting the size to `0` makes the query run much faster because it only calculates and returns the mathematical summaries (aggregations) requested at the bottom of the query.

### 3. The Query (Filters)

```json
"query": {
  "bool": {
    "filter": [
      ...
    ]
  }
}

```

The `bool` -> `filter` context is used for exact matching. It acts as a strict "Yes/No" gateway. Documents must pass all three of the following conditions to be included in the results:

* **`{"term": {"tags": "BEC"}}`**: Only includes network sessions that have been explicitly tagged with "BEC" (Business Email Compromise).
* **`{"range": {"@timestamp": {"gte": "2024-04-25T00:00:00+08:00", "lte": "2024-04-27T00:00:00+08:00"}}}`**: Restricts the search to a specific 48-hour window: from midnight on April 25, 2024, to midnight on April 27, 2024. The `+08:00` specifies the timezone (e.g., CST/Taiwan time).
* **`{"term": {"network.protocol": "smtp"}}`**: Ensures that only SMTP traffic (email routing protocol) is analyzed, filtering out web traffic (HTTP), DNS, etc.

### 4. The Aggregations (Summaries)

```json
"aggs": { ... }

```

This section groups the filtered data to provide statistical summaries, similar to a `GROUP BY` clause in SQL. It utilizes fields parsed by Zeek (a network security monitor often integrated with Arkime).

* **`"subjects"`**: Looks at the `zeek.smtp.subject.keyword` field and returns the top 20 most frequent email subjects found in this BEC traffic.
* **`"tls_breakdown"`**: Looks at the `zeek.smtp.tls` field (usually a boolean: true/false) to show how many of these malicious/suspicious emails were sent over an encrypted TLS connection versus in plain text.
* **`"senders"`**: Looks at the `zeek.smtp.mailfrom.keyword` field and returns a list of the top 20 most frequent sender email addresses.
* **`"recipients"`**: Looks at the `zeek.smtp.rcptto.keyword` field and returns a list of the top 20 most frequent recipient email addresses being targeted.

### Summary of Intent

If a security analyst runs this, they are asking the system: *"Give me a summary report of the top 20 senders, recipients, and subject lines for all SMTP email traffic tagged as 'BEC' between April 25 and April 27, 2024, and tell me if those emails were encrypted or not."*
---
created: 2026-07-23 22:07
updated: 2026-07-23 22:07
tags: []
type: reference
lang: en
status: draft
---
**No, this will not work.** Elasticsearch will throw a syntax/parsing error.

Here is why it fails and how to fix it:

## Why It Fails

Every item inside an array in Elasticsearch expects a **query clause type** (like `term`, `range`, `match`, or `bool`).

`"should"` is **not** a standalone query clause—it is a parameter that _only_ exists inside a `"bool"` wrapper. Elasticsearch doesn't know what to do with `"should"` on its own because it needs the `"bool"` container to know how to process that logical block.

## The Corrected Version

You must wrap the `"should"` array inside a `"bool"` object:

JSON

```
"filter": [
  { "term": { "tags": "BEC" } },
  {
    "bool": {                                     // <-- This wrapper is REQUIRED
      "should": [
        { "range": { "destination.ip": { "gte": "10.0.0.0", "lte": "10.255.255.255" } } },
        { "range": { "destination.ip": { "gte": "192.168.0.0", "lte": "192.168.255.255" } } }
      ]
    }
  }
]
```

### Summary Rule of Thumb

- **Query Clauses** (What kind of search?): `term`, `range`, `match`, `bool`
    
- **Boolean Parameters** (How to evaluate?): `must`, `must_not`, `filter`, `should` _(these must always sit inside a `bool`)_


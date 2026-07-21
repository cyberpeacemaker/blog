---
title: "OpenSearch API, Query DSL, and Dev Tools"
description: "Clarifies how OpenSearch REST APIs, JSON Query DSL payloads, and the Dev Tools console work together."
created: 2026-07-20
updated: 2026-07-20
tags: [opensearch, malcolm]
type: reference
lang: en
status: draft
---

> Related: [[MOC - OpenSearch Querying]] · [[lucene-dql-json-dsl]] · [[opensearch-request]]

These three concepts represent different layers of the same ecosystem, working together to let you communicate with OpenSearch.

The relationship between them can be explained through a simple communication analogy:

- **OpenSearch API** is the **communication protocol** (the mail system).
    
- **OpenSearch Query DSL** is the **language** written inside the message (the letter).
    
- **Dev Tools Panel** is the **interactive desk** where you comfortably write and send the letter (the writing station).
    

## Breakdown of the Components

### 1. OpenSearch API (The Messenger)

The **OpenSearch API** is the underlying RESTful HTTP interface exposed by the OpenSearch cluster. Everything OpenSearch does—indexing documents, checking cluster health, creating mappings, or running searches—happens by sending a request to an API endpoint using HTTP methods like `GET`, `POST`, `PUT`, or `DELETE`.

- _Example API endpoint:_ `POST /my-index/_search`
    

### 2. OpenSearch Query DSL (The Message Payload)

**Query DSL (Domain Specific Language)** is the JSON-based language used to write precise, complex queries. While basic commands can be sent via simple URL parameters, deep searches, filtering, and aggregations require you to write a structured JSON payload using Query DSL and pass it into the body of an API search request.

- _Example DSL:_ `{"query": {"match": {"status": "active"}}}`
    

### 3. OpenSearch Dev Tools Panel (The Interface)

The **Dev Tools Panel** is a UI application built inside OpenSearch Dashboards (the visualization web interface). Instead of forcing developers to construct messy `cURL` commands in a terminal or use external tools like Postman, Dev Tools provides an editor with auto-complete, syntax highlighting, and auto-formatting specifically designed for writing OpenSearch commands.

## How They Work Together (The Workflow)

When you look at a typical workflow in the Dev Tools console, you are seeing all three concepts operating at the exact same time:

HTTP

```
# 1. Dev Tools is the interactive console you are typing this into.
# 2. "GET /movies/_search" is the OpenSearch API endpoint you are targeting.
# 3. The JSON block below is the Query DSL defining the search parameters.

GET /movies/_search
{
  "query": {
    "match": {
      "genre": "Sci-Fi"
    }
  }
}
```

### The Chain of Interaction

1. You open the **Dev Tools Panel** in your browser.
    
2. You write out the specific **OpenSearch API** endpoint you want to talk to.
    
3. You fill the body of that request with **Query DSL** to define your data filters.
    
4. You hit the "Play" button in **Dev Tools**, which sends the API request directly to the cluster and renders the JSON response right on your screen.


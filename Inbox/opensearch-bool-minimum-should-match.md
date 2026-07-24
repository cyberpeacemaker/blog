---
created: 2026-07-23 22:07
updated: 2026-07-23 22:07
tags: []
type: reference
lang: en
status: draft
---
You're building a great mental model! Spotting the JSON structure like that is half the battle with Elasticsearch queries.

Here is the breakdown of those specific terms to help everything click.

## 1. What does `"term"` mean?

In Elasticsearch, **`term` = Exact Match**.

- **What it does:** It searches for an exact, un-analyzed value in your index. It doesn't do smart text processing (like lowercasing, splitting full sentences into words, or handling typos).
    
- **Intuition:** Think of it like an exact lookup in an Excel column.
    
- **In your query:** `{"term": {"tags": "BEC"}}` literally means: _"Find documents where the `tags` field is exactly the string `'BEC'`."_
    

## 2. What does `"bool"` mean?

In Elasticsearch, **`bool` = Logic Container (Boolean Logic)**.

- **What it does:** Standard JSON lists can't natively express logic like `AND`, `OR`, or `NOT`. A `bool` query is simply a wrapper or "box" that lets you group conditions using Boolean operators:
    
    - `must` / `filter` = **AND** (Conditions that _must_ match)
        
    - `should` = **OR** (Conditions where _any_ can match)
        
    - `must_not` = **NOT** (Conditions that _cannot_ match)
        
- **Intuition:** Whenever you need to combine logic (e.g., _"Filter by tag AND date AND (IP range A OR IP range B)"_), you open a `bool` block to organize those rules.
    

## 3. Why is `"minimum_should_match": 1` there?

Think of `minimum_should_match: 1` as **"The Strict Enforcer."**

- **The Catch:** Inside a `bool` block, a `should` array lists options. However, when `should` is used inside certain nested queries, Elasticsearch can treat it as _optional_—using it to boost relevance scores rather than filtering out documents.
    
- **The Fix:** By explicitly setting `"minimum_should_match": 1`, you force Elasticsearch to treat the `should` block as a mandatory filter:
    
    > _"Out of the IP range options listed in this `should` array, a valid document **must match at least 1** of them."_
    

This guarantees that the block behaves as a strict **logical OR**: `Range 1` **OR** `Range 2` **OR** `Range 3`.


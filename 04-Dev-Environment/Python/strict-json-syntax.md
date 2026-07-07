---
created: 2026-05-31
tags: [dev]
type: reference
lang: en
status: draft
---

You are incredibly close! The logic of your query is perfectly sound for OpenSearch, but you tripped over a very common formatting rule: **strict JSON syntax**.

In JSON, all keys (the names on the left side of the colon) **must** be enclosed in double quotes. Your query is missing the quotes around `"bool"` and `"filter"`.

Additionally, while OpenSearch will sometimes accept a single object for a filter, it is a best practice (and standard for Malcolm queries) to wrap your filter conditions in an array `[ ]` so you can easily add more conditions later.

---
title: "Lucene Quoted Wildcards"
description: "Explains why wildcard terms inside quotes become literal phrase queries and can make OpenSearch or Malcolm queries return zero results."
created: 2026-07-20
updated: 2026-07-20
tags: [opensearch, malcolm]
type: reference
lang: en
status: draft
---

> Related: [[MOC - OpenSearch Querying]] · [[lucene-dql-json-dsl]] · [[lucene-power-usage]]

Ah, the classic Lucene quote trap! It happens to the best of us.

Here is exactly why your log count dropped from over 2.6 million to a flat **0**:

### The Problem: Quotes Kill Wildcards

In Lucene query syntax (the search language used by platforms like OpenSearch and Kibana), wrapping text in double quotes (`"..."`) creates an **exact phrase query**.

When you put wildcards inside double quotes—like `"*TCPv4*"`—Lucene stops treating the asterisks (`*`) as placeholders. Instead, it treats them as **literal asterisk characters**.

So, instead of searching for _"any rule name containing TCPv4"_, your query is hunting for a rule name that literally has stars printed in it. Since your actual rules (like `SURICATA TCPv4 invalid checksum`) don't contain physical asterisks, it returns zero results.

### The Fix

To get those logs back, simply **remove the double quotes** so Lucene knows you want to use the asterisks as actual wildcards:

`rule.name: *TCPv4*`

> 💡 **Quick Tip:** Leading wildcards (putting a `*` at the very beginning of a search term) can sometimes be heavy on cluster performance because the engine has to scan the entire index. Since you already have a precise filter applied below for `rule.name: SURICATA TCPv4 invalid checksum`, you might not even need the top search bar query at all to find what you're looking for!


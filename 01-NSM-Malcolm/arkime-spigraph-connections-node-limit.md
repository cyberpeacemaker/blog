---
title: "Arkime SPI Graph Connections Node Limit"
description: "Explains how Arkime Connections query size can hide low-volume source IP nodes from the graph sample."
created: 2026-07-16
updated: 2026-07-16
type: howto
lang: en
status: draft
tags: [malcolm, nsm]
---

> Related: [[MOC - Malcolm & NSM]] · [[arkime]] · [[arkime-query-opensearch]]

At first glance, it looks like a bug—you clearly have three source IPs in your SPI data, but only one source IP is showing up on your Connections graph.

The culprit here is the **Query Size** limit setting on your Connections panel.

### The Breakdown

If you look at the top-left corner of your Connections panel (your second image), you will see a setting called **Query Size** which is currently set to its default of **`100`**.

Arkime uses this limit to determine how many raw session records to retrieve from the database to build the node-link graph. A smaller query size executes much faster, but it only represents a tiny, incomplete sample of your overall traffic.

Based on your SPI data (your first image), your traffic is overwhelmingly dominated by just one source IP:

|**Source IP**|**Sessions**|**Percentage of Total**|**Will it show up in the top 100?**|
|---|---|---|---|
|**192.168.60.2**|744,412|**~98.6%**|Yes (completely dominates the sample)|
|**192.168.60.4**|6,880|**~0.9%**|No|
|**192.168.60.66**|3,519|**~0.5%**|No|

Because **192.168.60.2** makes up more than 98% of your 754,822 total sessions, when Arkime queries the database for the first 100 sessions to construct the graph, **every single one of those 100 records** is a connection between `192.168.60.2` and `192.168.60.3`. The other two IPs simply don't make the cut in such a tiny sample.

### How to Fix It

To see all of your source IPs on the graph, you need to increase the database query limit so Arkime pulls enough records to include the minority traffic:

1. Go to the **Connections** tab.
    
2. Click the **Query Size** dropdown on the top left (which currently says `100`).
    
3. Change this value to a much larger number, such as **`10000`** or **`50000`**.
    
4. Allow the graph a few moments to reload.
    

Once you expand the query size, Arkime will retrieve enough session data to catch the traffic from `192.168.60.4` and `192.168.60.66`, and they will display as nodes on your graph!

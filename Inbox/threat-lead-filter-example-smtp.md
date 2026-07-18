---
created: 2026-07-18 18:07
updated: 2026-07-18 18:07
tags: []
type: reference
lang: en
status: draft
---
To find other Suricata alerts related to SMTP without locking yourself into a single exact signature, you can leverage OpenSearch's flexible filtering options.

Based on the interface you are currently using, here are the best filters you can apply:

### 1. Broaden the Rule Name Filter

Right now, your filter is set to an exact match (`is`). You can change this to catch _any_ rule that mentions SMTP:

- **Field:** `rule.name`
    
- **Operator:** `contains`
    
- **Value:** `SMTP`
    

### 2. Filter by Network Protocol

Instead of searching by the alert's name, you can look for any alert triggered on SMTP traffic:

- **Field:** `network.protocol` (or `proto` depending on the schema version)
    
- **Operator:** `is`
    
- **Value:** `smtp`
    

### 3. Filter by Email Ports

You can target standard email traffic directly by filtering for common SMTP ports:

- **Field:** `destination.port`
    
- **Operator:** `is one of`
    
- **Value:** `25, 465, 587`
    

### 4. Isolate Suricata Events

If you remove your current `rule.name` filter and find yourself flooded with standard Zeek logs, you can explicitly lock the view down to Suricata alerts:

- **Field:** `event.provider`
    
- **Operator:** `is`
    
- **Value:** `suricata`
    

### Alternative: Using the Lucene Search Bar

Instead of clicking "Add filter," you can type broad queries directly into the search bar at the top (where the `*` is currently located). Since you already have `tags: BEC` applied, these text queries will work alongside it:

|**Query Style**|**Example Syntax**|**What it does**|
|---|---|---|
|**Wildcard Search**|`rule.name: *SMTP*`|Matches any alert rule containing "SMTP"|
|**Protocol Search**|`network.protocol: "smtp"`|Filters all logs strictly classified under the SMTP protocol|
|**Combined Search**|`event.provider: "suricata" AND smtp`|Finds any Suricata log that contains the word "smtp" anywhere in its data|

Are you trying to hunt for a specific type of malicious email behavior within this BEC campaign, or are you just exploring what Suricata managed to flag in this traffic?


---
title: "Arkime DNP3 Field Mismatch"
description: "Explains why DNP3 queries can return no results when Arkime native fields and Malcolm ECS fields are mixed."
created: 2026-07-18
updated: 2026-07-19
tags: [malcolm, nsm, opensearch]
type: howto
lang: en
status: draft
prerequisites: [arkime-query-opensearch, ecs-translation]
summary:
  - "Use `protocols == dnp3` for native Arkime sessions and `event.dataset,contains=dnp3` for Malcolm Zeek mappings."
  - "`event.dataset` is an ECS field, so standalone Arkime searches against it return no results."
---

> Related: [[MOC - Malcolm & NSM]] · [[arkime-query-opensearch]] · [[ecs-translation]]

It is always frustrating when you run a query expecting a treasure trove of industrial traffic and get hit with radio silence.

The reason you are seeing "nothing" usually comes down to one of two things: **field mismatches** between native Arkime and external loggers, or a lack of that specific sub-protocol traffic in your environment.

## The Core Issue: Native Arkime vs. Zeek (Malcolm)

The field `event.dataset` is **not a native Arkime field**. It belongs to the Elastic Common Schema (ECS).

- **If you are running standalone Arkime:** The `event.dataset` field does not exist in the native session database. Searching for it will always return zero results.
    
- **If you are running Malcolm:** (the popular network analysis stack combining Arkime and Zeek), Malcolm _does_ map Zeek logs into Arkime using `event.dataset`. If you are using Malcolm, that field maps to the CISA `icsnpp-dnp3` plugin, which breaks DNP3 traffic out into `dnp3`, `dnp3_control`, and `dnp3_objects`. Seeing "nothing" here simply means no explicit DNP3 control commands (like Select/Operate) were captured in your selected time frame.
    

## How to Successfully Find DNP3 in Arkime

Depending on your setup and what you are trying to find, you should pivot to Arkime's native filtering syntax:

### 1. The Global "Catch-All" Query

To see _all_ DNP3 traffic regardless of whether it came from a native PCAP parser or a Zeek log mapping, use Arkime's native protocol field:

Code snippet

```
protocols == dnp3
```

### 2. The Broad Zeek Dataset Query (Malcolm Only)

If you want to look at the logs but aren't sure if any specific control functions occurred, look for the main DNP3 activity log first:

Code snippet

```
event.dataset == dnp3
```

### 3. Use the "Contains" Modifier (The Safe Bet)

Arkime doesn't support standard wildcards (like `*dnp3*`) for string fields. Instead, it uses trailing string modifiers. If you want to catch `dnp3`, `dnp3_control`, and `dnp3_objects` all in one sweep, format it like this:

Code snippet

```
event.dataset,contains=dnp3
```

## Advanced DNP3 Filtering

If you are running Arkime v6.4.0 or newer, the native packet parser includes a massive upgrade for ICS protocols. You no longer need to rely purely on Zeek logs to find control operations; you can look directly at decoded function names via PCAP:

> **Native Field:** `dnp3.funcName`

### Quick DNP3 Query Reference

|**What you want to find**|**The Arkime Query to use**|**Environment**|
|---|---|---|
|**All DNP3 Traffic**|`protocols == dnp3`|Native Arkime & Malcolm|
|**Specific Control Functions**|`dnp3.funcName == "READ"` _(or "WRITE")_|Native Arkime (v6.4.0+)|
|**Any Zeek DNP3 Log**|`event.dataset,contains=dnp3`|Malcolm Only|
|**Zeek Control Logs Explicitly**|`event.dataset == "dnp3_control"`|Malcolm Only (Requires active control traffic)|

Switching your query over to `protocols == dnp3` or `event.dataset,contains=dnp3` will quickly reveal if the data is actually there.


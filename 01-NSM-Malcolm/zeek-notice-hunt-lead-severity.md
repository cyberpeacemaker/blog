---
title: "Zeek Notice Hunt Lead Severity"
description: "Explains why high raw severity should drive Zeek Notice triage ordering before event count."
created: 2026-07-28
updated: 2026-07-28
tags: [malcolm, nsm, threat-hunting]
type: reference
lang: en
status: draft
---

> Related: [[MOC - Malcolm & NSM]] · [[MOC - Threat Hunting]] · [[zeek-notice-hunt-lead-algorithm]]

Short answer: Yes, absolutely — sorting this table by **High Raw Severity in descending order** makes much more sense for security triage.

Here is why the current order is counterproductive for threat hunting:

### The Problem with the Current View

Right now, the dashboard is sorted by **Count in descending order** (from 1,408 down to 8):

- **Top Row (1,408 events):** `LongConnection::found` has a low severity score of **20**. This is high-volume background noise (like a long-lived database connection or streaming session) that rarely requires immediate action.
    
- **Bottom Row (8 events):** `ATTACK::Lateral_Movement...` has the highest severity score of **155**. This is low-volume, high-impact threat activity that requires immediate isolation and investigation.
    

Sorting by volume buries your critical security threats at the bottom of the screen under a mountain of noise — a classic trigger for alert fatigue.

### How it Should Be Ordered

For effective incident response, you want a **High Severity Descending** sort:

1. **Primary Sort — High Raw Severity (Descending):** Places the most dangerous threats (score **155**) at the very top so analysts see them immediately.
    
2. **Secondary Sort — Count (Descending):** If multiple categories share the same severity score (like the four categories tied at **80**), sorting by count breaks the tie by showing the most frequent high-severity events first.
    

**Quick fix:** Click the **High Raw Severity** column header (the small arrow next to it) to flip the sort direction so 155 sits on top.

Are you able to adjust the underlying query or table settings to set "High Raw Severity descending" as the default view?


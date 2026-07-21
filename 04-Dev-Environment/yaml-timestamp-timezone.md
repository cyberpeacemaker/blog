---
title: "YAML Timestamps and Taipei Time"
description: "Explains ISO 8601 UTC timestamps, UTC+8 conversion, and YAML timestamp versus string syntax."
created: 2026-07-21
updated: 2026-07-21
tags: [dev]
type: reference
lang: en
status: draft
---

> Related: [[MOC - Dev Environment]] · [[YAML]] · [[timezone]]

Here is what that timestamp means, along with how to write it for Taipei time in YAML.

## 1. What `2026-07-18T07:16:00Z` Means

This is a standard **ISO 8601** formatted timestamp:

- **`2026-07-18`**: The date (July 18, 2026).
    
- **`T`**: The separator indicating that time follows the date.
    
- **`07:16:00`**: Time in 24-hour format (7:16 AM and 0 seconds).
    
- **`Z`**: Stands for **Zero offset** or **Zulu time** (UTC / Coordinated Universal Time).
    

> **YAML Behavior:** Unquoted ISO 8601 timestamps like this are automatically parsed as **Datetime objects** (not plain strings) in most YAML parsers.

## 2. Converting to UTC+8 (Taipei)

To convert `07:16:00 UTC` to Taipei time, add **8 hours**:

$$\text{07:16 UTC} + \text{8 hours} = \text{15:16 (3:16 PM) Taipei time}$$

So the equivalent time in Taipei is **July 18, 2026, at 15:16:00**.

## 3. How to Write This in YAML

Depending on what your application expects, you have two main ways to write it:

### Option A: Standard ISO 8601 with Offset (Recommended)

You can specify the `+08:00` offset directly in YAML. Most parsers will recognize this as a Datetime object set specifically to UTC+8:

YAML

```
# Parsed as a Datetime object set to Taipei time (+08:00)
timestamp: 2026-07-18T15:16:00+08:00
```

### Option B: Plain String in 24-Hour Local Time

If your application or database just expects a literal local time string without timezone math:

YAML

```
# Parsed as a simple string
timestamp: "2026-07-18 15:16:00"
```

## Quick Comparison

|**Goal**|**YAML Syntax**|**Parsed As**|
|---|---|---|
|**UTC (Original)**|`timestamp: 2026-07-18T07:16:00Z`|Datetime (07:16 UTC)|
|**Taipei with Offset**|`timestamp: 2026-07-18T15:16:00+08:00`|Datetime (15:16 UTC+8)|
|**Taipei as String**|`timestamp: "2026-07-18 15:16:00"`|String ("2026-07-18 15:16:00")|


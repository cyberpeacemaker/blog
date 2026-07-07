---
created: 2026-05-22
tags: [malcolm, nsm]
type: reference
lang: en
status: draft
---

## 1. What time is it in the Malcolm GUI?

By default, OpenSearch Dashboards (the GUI Malcolm uses) automatically translates the raw database timestamps into your **browser's local timezone**.

The image shows: `May 20, 2026 @ 18:30:00.000 → now`

* **What it means:** This represents **6:30 PM in your local timezone** up until the exact current moment (`now`).
* If your local timezone is **CST (UTC+8)**, this local 18:30:00 corresponds exactly to **10:30:00 UTC**.

---

## 2. How to correspond it to your API query

To accurately replicate this GUI range filter in your API `POST` request, you have two great options.

### Option A: Use the `time_zone` parameter (Recommended)

This is the cleanest approach. You don't have to manually do time-zone math or change the numbers; you just write the time exactly as it appears in the GUI and pass your timezone offset (e.g., `+08:00`).

*(Note: OpenSearch knows that `"lte": "now"` is always evaluated as the universal current time, so the `time_zone` rule will safely only recalculate your absolute `gte` string).*

```json
POST /arkime_sessions3-*/_search
{
  "query": {
    "bool": {
      "must": [
        { "match": { "tags": "BEC" } },
        {
          "range": {
            "@timestamp": {
              "gte": "2026-05-20T18:30:00.000",
              "lte": "now",
              "time_zone": "+08:00"
            }
          }
        }
      ],
      "must_not": [
        { "match": { "network.protocol": "modbus" } }
      ]
    }
  },
  "size": 20
}

```

---

### Option B: Convert the time manually to UTC (Using `Z`)

If you prefer keeping the standard **`Z`** (Zulu/UTC) format at the end of your string without using a standalone timezone parameter, you have to subtract your timezone offset hours from the local time manually.

Assuming a **UTC+8** timezone context:
`18:30:00 minus 8 hours = 10:30:00 UTC`

```json
POST /arkime_sessions3-*/_search
{
  "query": {
    "bool": {
      "must": [
        { "match": { "tags": "BEC" } },
        {
          "range": {
            "@timestamp": {
              "gte": "2026-05-20T10:30:00.000Z",
              "lte": "now"
            }
          }
        }
      ],
      "must_not": [
        { "match": { "network.protocol": "modbus" } }
      ]
    }
  },
  "size": 20
}

```
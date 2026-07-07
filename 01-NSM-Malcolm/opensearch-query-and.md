---
created: 2026-05-27
tags: [malcolm, nsm, opensearch]
type: reference
lang: en
status: draft
---

Yes, by default, having multiple separate filter pills in OpenSearch Dashboards acts as an **AND** condition.

Because of this, your current setup is looking for a single log entry that has *both* of those exact `event.id` values at the same time. Since `event.id` is usually a unique identifier, this will likely return zero results.

Here are three ways to change this to an **OR** condition so it matches *any* of the IDs:

### Method 1: The Visual UI (Easiest)

Instead of creating separate pills, you can combine them into one using the "is one of" operator.

1. Hover over one of the `event.id` filter pills and delete it (using the `x`).
2. Click the remaining `event.id` pill and click **Edit filter**.
3. At the top right of that pop-up, click **Edit filter values** (to switch away from the JSON DSL view).
4. Set the operator to **`is one of`**.
5. Paste both of your IDs into the value box and click Save.

### Method 2: The Search Bar (Lucene)

You can use the search bar at the very top (where the `*` currently is) to write a simple boolean query.

1. Keep your `tags: BEC` filter pill, but delete both `event.id` filter pills.
2. In the top search bar, type this exact query:
`event.id:("CsZN7WRpE9A1srXL7" OR "Ff9lMQl7UkL5EiOJi")`
3. Hit Enter.

### Method 3: Edit the Query DSL

Since you already have the Query DSL editor open, you can change the underlying JSON to a `terms` query, which automatically acts as an "OR" list for a specific field.

1. Delete your second `event.id` pill so you only have one.
2. In the DSL editor for the remaining pill, replace the `match_phrase` JSON with this `terms` JSON:

```json
{
  "query": {
    "terms": {
      "event.id": [
        "CsZN7WRpE9A1srXL7",
        "Ff9lMQl7UkL5EiOJi"
      ]
    }
  }
}

```
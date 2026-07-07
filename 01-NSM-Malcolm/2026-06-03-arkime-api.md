---
created: 2026-06-03
tags: [malcolm, arkime, opensearch]
type: howto
lang: en
status: draft
---

> Related: [[MOC - Malcolm & NSM]] · [[2026-05-27-arkime]] · [[2026-05-27-arkime-query-opensearch]] · [[2026-05-27-malcolm-orchestration]]

### 1. The `/arkime` Prefix

Because Malcolm heavily utilizes reverse proxies (like Nginx) to route traffic to its various tools, Arkime doesn't sit at the root of the web server—it sits at `/arkime/`. By fixing that prefix, you successfully routed your script past Malcolm's front door and directly to the Arkime backend. That is why your basic BEC session stats and OT records started connecting and pulling correctly.

### 2. The SPA HTML Fallback (Why the test "passed")

The secondary bug you spotted is a side effect of Arkime's frontend architecture. Arkime uses a **Single Page Application (SPA)** framework (Vue.js).

When working with traditional APIs, if you hit an endpoint that doesn't exist (like `/api/ip.src/unique`), the server throws a `404 Not Found` or returns a JSON error. Your script would normally catch that error and fail the test immediately.

However, Arkime's web server is configured with a "catch-all" fallback route. When it receives a request for a path it doesn't recognize as a hardcoded API route, it assumes the user is just navigating or refreshing a frontend UI page. Instead of throwing an error, it returns the raw `index.html` of the application so the browser's router can handle it. Because your smoke test didn't explicitly validate the `Content-Type` of the response (HTML vs. JSON), it blindly accepted the data and "passed" the test.

### 3. Fixing the API Endpoints

You correctly identified that Arkime v5.x handles target fields via query parameters rather than URL path variables.

* **For Unique Values:**
Moving from `/api/{field}/unique` to `/api/unique?exp={field}` (e.g., `/api/unique?exp=ip.src`) is exactly the right move. This hits a recognized API route and passes the target expression as an argument.
* **For SPIGraph:**
You will need to apply the exact same logic to `get_spigraph()`. The correct endpoint is simply `/api/spigraph` (or `/spigraph.json` depending on the exact route wrapper). To retrieve the graph data, format the request like this:
`/api/spigraph?exp={field}`

> **Pro Tip:** Arkime APIs often accept both `exp` (the frontend search expression, like `ip.src`) and `field` (the raw OpenSearch/Elasticsearch database field, like `a1`). Sticking to `exp` is usually best because it maps exactly to what you type in the Arkime UI search bar.

Have you been able to successfully parse the JSON payload from the correct SPIGraph endpoint yet, or are you still fine-tuning the time ranges and data bins in your query?

[Threat Hunting with Malcolm: SPIView and SPIGraph in Arkime](https://www.youtube.com/watch?v=m6v7i1XfkQg)
This video demonstrates how to visually utilize SPIView and SPIGraph for threat hunting within Malcolm, which might provide helpful context on how the data you are pulling via the API is structured.
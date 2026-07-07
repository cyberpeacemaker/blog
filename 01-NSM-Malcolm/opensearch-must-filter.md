---
created: 2026-05-27
tags: [malcolm, nsm, opensearch]
type: reference
lang: en
status: draft
---

To understand why OpenSearch (and Elasticsearch, which it’s based on) separates `must` and `filter` clauses, you have to look at the two different ways the database evaluates data: **Query Context** and **Filter Context**.

The separation isn't just for organization; it is the fundamental secret to why these databases can search billions of logs in milliseconds.

Here is a deeper look at the mechanics behind both.

### 1. The `must` Clause (Query Context & Scoring)

When you type a phrase into the Malcolm search bar, that text is sent to the `must` block. This block operates in the **Query Context**.

It asks the database: *"How **well** does this document match the query?"*

* **Relevance Scoring:** Instead of just saying "yes" or "no," the database calculates a relevance score (using an algorithm called BM25) for every single document. If you search for `"connection reset"`, a log containing that exact phrase three times will get a higher score than a log containing it only once.
* **Resource Heavy:** Because the backend has to mathematically calculate a score for every matching document, this process is computationally expensive.
* **No Caching:** The results of scoring queries are generally not cached because scores change dynamically depending on the exact text and the entire dataset.

### 2. The `filter` Clause (Filter Context & Caching)

When you use the time picker or click a specific IP address filter pill in Malcolm, those inputs are sent to the `filter` block. This operates in the **Filter Context**.

It asks the database a simple, binary question: *"Does this document match the query? **Yes or No?***"

* **Binary Logic (No Scoring):** The database doesn't care *how well* a document matches. If you filter for `destination.port: 443`, the document either has port 443 or it doesn't. There is no "score" to calculate.
* **Incredibly Fast:** Because it skips the complex math of relevance scoring, filtering is lightning-fast.
* **Aggressive Caching (Bitsets):** This is the biggest advantage. OpenSearch builds cached "bitsets" (essentially arrays of 1s and 0s) in memory for frequently used filters. If you frequently filter by `network.protocol: tcp`, the database caches a massive checklist of exactly which documents are TCP. The next time you apply that filter, it takes almost zero processing power.

---

### The Synergy: Why They Work Together

By separating the JSON into `must` and `filter` blocks, the Malcolm GUI is forcing the backend to be as efficient as possible. Here is the order of operations when you run a combined search:

1. **Filter First:** The database looks at your `filter` array first. It uses its highly optimized, cached bitsets to instantly throw out 99% of the logs (e.g., "Ignore everything outside of the last 24 hours, and ignore everything that isn't port 443").
2. **Score Second:** Now, instead of calculating relevance scores across billions of logs, the `must` block only has to run its expensive scoring algorithm on the few thousand logs that survived the filter.

**In summary:** Put your exact matches, numbers, and timestamps in the `filter` block to quickly carve down the dataset for free. Save the `must` block exclusively for fuzzy text searches where you actually care about sorting the results by relevance.
---
created: 2026-06-03
tags: [dev]
type: reference
lang: en
status: draft
---

Changing from a strict equality (`==`) to a greater-than-or-equal-to (`>=`) changes how your project handles future updates to that library. Here is a breakdown of the trade-offs:

### Strict Pinning (`==2.3.1`)

* **What it does:** Forces pip to install exactly version 2.3.1, every single time.
* **Pros:** Guarantees absolute stability. Your code in `utils/opensearch_client.py` will behave exactly the same across all environments because the underlying library never changes.
* **Cons:** You miss out on security patches, bug fixes, and performance improvements unless you manually update the version number.

### Unbounded Range (`>=2.3.1`)

* **What it does:** Tells pip to install version 2.3.1 *or any newer version available*.
* **Pros:** You automatically get bug fixes and new features whenever you reinstall dependencies.
* **Cons:** **High risk of breaking changes.** If the developers of `opensearch-py` release a major version (e.g., `3.0.0`) that removes or renames functions you are using, your app will suddenly break the next time someone runs `pip install`.

---

### Better Alternatives

If you want the flexibility of updates without the risk of your code unexpectedly breaking, it is generally safer to use a **bounded range** instead of an unbounded `>=`.

Here are two highly recommended approaches:

**1. The "Minor and Patch Updates Only" Approach (Recommended)**

```text
opensearch-py>=2.3.1, <3.0.0  # OpenSearch client (utils/opensearch_client.py)

```

This allows updates like `2.4.0` or `2.8.5` (which usually contain safe, backward-compatible features and fixes) but stops before `3.0.0` (where breaking API changes usually happen).

**2. The "Compatible Release" Approach (Patch Updates Only)**

```text
opensearch-py~=2.3.1          # OpenSearch client (utils/opensearch_client.py)

```

The `~=` operator acts as a shorthand for `>=2.3.1, ==2.3.*`. This is very conservative; it only allows patch updates (like `2.3.2` or `2.3.9` for bug fixes) but won't jump to `2.4.0`.

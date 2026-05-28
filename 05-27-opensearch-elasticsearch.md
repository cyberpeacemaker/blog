I am glad you found the Malcolm breakdown helpful! The relationship between **Elasticsearch** and **OpenSearch** is one of the most famous (and dramatic) stories in modern open-source software.

Think of them as siblings who grew up in the same house but had a massive falling out, moved to different cities, and now have completely different approaches to life.

Here is the history, how they compare today, and why Malcolm supports both.

### 1. The Shared Origin (Pre-2021)

For years, **Elasticsearch** (created by the company Elastic) was the undisputed king of search engines and log analytics. It was licensed under the highly permissive Apache 2.0 open-source license.

Because it was open-source, massive cloud providers—specifically Amazon Web Services (AWS)—took the Elasticsearch code, hosted it on their cloud, and made a fortune selling it as a managed service ("Amazon Elasticsearch Service") without contributing much back to Elastic financially. Elastic grew increasingly frustrated by this.

### 2. The Great Fork (2021)

In January 2021, Elastic decided they had enough. To block cloud providers from monetizing their software for free, Elastic changed the license of Elasticsearch from Apache 2.0 to the Server Side Public License (SSPL). This explicitly prohibited companies from offering Elasticsearch as a managed cloud service unless they open-sourced all of their surrounding cloud infrastructure (a non-starter for AWS).

**The AWS Response:** Because SSPL was not recognized as a "true" open-source license by the Open Source Initiative (OSI), AWS retaliated. They took the last open-source version of Elasticsearch (version 7.10.2), made a clean copy of the code, and announced **OpenSearch**. OpenSearch retained the permissive Apache 2.0 license, allowing anyone (including AWS) to continue building and monetizing it freely.

### 3. The Present Day (2024–2026)

Since the fork, the two platforms have aggressively developed in different directions:

* **OpenSearch Goes Community:** In late 2024, AWS transferred the governance of OpenSearch to the **Linux Foundation**. This proved OpenSearch wasn't just an "Amazon clone," but a genuinely community-driven, vendor-neutral project.
* **Elastic Returns to Open Source:** Realizing that developers still care deeply about open-source purity, Elastic updated its licensing again in late 2024. They added the **AGPLv3** license as an option. AGPL is an officially recognized open-source license, meaning Elasticsearch is officially "open source" again, though AGPL is a "copyleft" license (stricter than Apache 2.0) that still protects Elastic's commercial interests.

---

### Comparison: Elasticsearch vs. OpenSearch Today

Despite sharing the same core DNA (both are built on top of Apache Lucene), they have diverged significantly in features, APIs, and philosophy.

| Feature | Elasticsearch | OpenSearch |
| --- | --- | --- |
| **Primary License** | AGPLv3 / SSPL / Elastic License (Stricter) | Apache 2.0 (Highly Permissive) |
| **Governance** | Controlled purely by Elastic NV | The Linux Foundation (Community/AWS) |
| **Philosophy** | A tightly integrated, premium platform (Enterprise Search, SIEM, APM out of the box). | A highly configurable, modular engine. Relies heavily on community plugins. |
| **Vector/AI Search** | Extremely polished, proprietary RAG and native ML integrations. | Relies on open-source vector engines (like Faiss) and modular AI plugins. |
| **Cost to Self-Host** | Free for core features, but advanced features (like Cross-Cluster Replication) require a paid enterprise license. | 100% free. Advanced features like Cross-Cluster Replication and Alerting are included out of the box. |

### How This Relates to Malcolm

Because Malcolm is an open-source cybersecurity tool built for the community (originally developed by CISA/Idaho National Laboratory), it inherently gravitates toward frictionless, highly permissive open-source software.

When Elastic changed its license in 2021, the Malcolm developers pivoted to make **OpenSearch** the default backend to ensure users could deploy it anywhere without worrying about enterprise licensing traps. However, because their underlying APIs are still somewhat similar, Malcolm thoughtfully maintains support for Elasticsearch for organizations that already pay for and run an Elastic ecosystem.


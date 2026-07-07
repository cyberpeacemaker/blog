This sentence describes a common methodological challenge in network forensics using **Arkime** (formerly Moloch): the danger of relying on sampled data to prove a negative, and how to properly work around it.

Here is a detailed breakdown of what that sentence means, translated from network-analyst shorthand into a clearer explanation.

### 1. "Arkime /sessions is length-capped..."

When you query Arkime for network traffic, the system limits (caps) the number of session records it pulls back for broad searches. It does this to prevent crashing the UI or overloading the backend Elasticsearch database. For example, if millions of sessions occurred, Arkime might only show you the first 10,000.

### 2. "...S3/S4 dst distributions are samples..."

"S3/S4" likely refers to specific search queries, datasets, or time windows (e.g., Scenario 3 vs. Scenario 4) being compared.
Because the `/sessions` results are length-capped, any statistical breakdown—such as the distribution of Destination IPs ("dst distributions")—is inherently just a **sample** of the data, not a complete census. It shows you the stats for the capped subset, not every single packet that crossed the wire.

### 3. "...so true before-absence was proven..."

The analyst was trying to prove that traffic to a specific location definitively **did not exist** before a certain point in time ("before-absence").

### 4. "...not by the capped diff alone."

This is the core trap the analyst avoided. You cannot just run a broad "Before" search and a broad "After" search, look at the difference (the "diff"), and say: *"Look, the IP address isn't in the Before list, but it is in the After list."* Because the broad lists are capped/sampled, the IP might have actually existed in the "Before" timeframe, but simply got truncated out of the results by the length cap. **Absence from a sample is not proof of absence from the whole.**

### 5. "...by a separate targeted `ip.dst==10.99.40.20` recordsFiltered probe..."

To definitively prove the IP wasn't there, the analyst couldn't rely on the broad searches. Instead, they had to run a surgical, targeted query looking *only* for that specific destination IP (`ip.dst==10.99.40.20`).

They then looked at the **`recordsFiltered`** metadata. In API and database terms, `recordsFiltered` tells you the absolute total number of matches found in the backend database, regardless of how many results are actually returned to your screen. By running this exact query and seeing that `recordsFiltered` equaled **0**, the analyst definitively proved the traffic did not exist in that timeframe.

---

### The TL;DR

*"Because Arkime limits how many results it shows for broad searches, we couldn't just look at the general 'Before' and 'After' lists to prove an IP wasn't there—it might have just been cut off by the search limits. To definitively prove the IP was completely absent beforehand, we had to run a highly specific query just for that exact IP and confirm the backend database registered exactly zero hits."*
---
created: 2026-07-18 10:07
updated: 2026-07-18 10:07
tags: []
type: reference
lang: en
status: draft
---

## A Practical Threat Hunting Workflow Example

  

Drive by a hypothesis: *An attacker is using DNS tunneling to steal data from your network.*

  

1. **The Prep:** You use **Sigma** to craft a behavioral logic flow looking for unusually large DNS TXT record responses.

2. **The Search:** You translate that logic into an **OpenSearch Query** and run it against your log repository.

3. **The Pivot:** OpenSearch flags a suspicious internal IP address. You dive into the **Zeek** DNS logs inside OpenSearch to analyze the queries.

4. **The Proof:** You pivot to **Arkime** using the timestamp and IP address to look at the raw packet payload and see exactly what data was smuggled out.

5. **The Clean-up:** You pull a file hash from that network stream and deploy a **YARA** rule across your host endpoints to find the specific malware executing on the compromised machine.
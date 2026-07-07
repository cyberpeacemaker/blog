---
created: 2026-05-25
tags: [malcolm, nsm, zeek]
type: reference
lang: en
status: draft
---

These three tools—**Zeek**, **Splunk**, and **Velociraptor**—are heavyweights in the cybersecurity world, specifically in Security Operations Centers (SOCs), Incident Response (IR), and threat hunting. While they each serve a distinct purpose, they complement each other perfectly to provide full visibility across a network.

Here is a breakdown of what each tool does, its strengths, and how they fit into the broader security landscape.

---

### ## 1. Zeek (The Network Watcher)

Formerly known as Bro, Zeek is a powerful, open-source **Network Security Monitoring (NSM)** tool. Instead of just looking for known bad signatures (like a traditional Intrusion Detection System such as Snort or Suricata), Zeek acts more like a "flight data recorder" for your network.

* **What it does:** It passively sniffs network traffic, interprets the protocols being used (HTTP, DNS, TLS, SMB, etc.), and generates highly structured, compact, and readable transaction logs.
* **Key Features:**
* **Rich Protocol Parsing:** It doesn't just record that a connection happened; it extracts the metadata (e.g., the exact URL requested in an HTTP session, or the domain queried in DNS).
* **Scripting Engine:** It has its own Turing-complete scripting language, allowing security teams to write custom scripts to detect specific anomalies or behaviors.
* **File Extraction:** It can automatically extract files transferred over the network (like a downloaded `.exe`) so they can be hashed or sent to a sandbox for malware analysis.


* **Primary Use Case:** Network visibility, traffic analysis, and generating the network telemetry that analysts need to investigate an alert.

### ## 2. Velociraptor (The Endpoint Investigator)

Velociraptor is an advanced, open-source **Digital Forensics and Incident Response (DFIR)** tool (now backed by Rapid7). It gives you deep visibility into the actual endpoints (laptops, servers, workstations) on your network.

* **What it does:** It uses a client-server architecture to deploy lightweight agents to endpoints. Analysts can then query these endpoints in real-time to hunt for malware, gather forensic artifacts, or respond to breaches.
* **Key Features:**
* **VQL (Velociraptor Query Language):** This is the heart of the tool. It allows analysts to write custom queries to search for very specific indicators of compromise (IoCs) across thousands of machines simultaneously (e.g., "Find any machine where *this* specific registry key was modified in the last 24 hours").
* **Live Response:** You can use it to pull memory dumps, fetch specific files, or execute remediation scripts on an infected machine without needing physical access to it.
* **Offline Triage:** It can be run from a USB drive to collect artifacts from a completely disconnected, compromised machine.


* **Primary Use Case:** Endpoint threat hunting, rapid incident response, and forensic artifact collection at scale.

### ## 3. Splunk (The Central Brain / SIEM)

Splunk is a massive, commercial data platform primarily used as a **Security Information and Event Management (SIEM)** system in this context (recently acquired by Cisco). It is the central hub where the data from Zeek, Velociraptor, and thousands of other systems is sent.

* **What it does:** It ingests, indexes, and correlates massive volumes of machine-generated data from across the entire IT environment.
* **Key Features:**
* **SPL (Search Processing Language):** A highly flexible query language used to search through petabytes of log data quickly.
* **Dashboards and Alerting:** Analysts build custom dashboards to visualize trends and set up alerts based on correlation rules (e.g., "Alert me if a user fails to log in 10 times and then successfully logs in from a new IP address").
* **SOAR Integration:** Often paired with Splunk SOAR (Security Orchestration, Automation, and Response) to automate the initial response to the alerts it generates.


* **Primary Use Case:** Log aggregation, correlation, alerting, and providing a single pane of glass for security analysts to investigate incidents.

---

### ## How They Work Together in a SOC

If a company is breached, here is how an analyst would use all three in tandem:

1. **The Alert (Splunk):** **Splunk** generates an alert because a correlation rule fired. It noticed a user's machine making an unusual amount of outbound connections to a foreign IP address.
2. **The Network Context (Zeek):** The analyst checks the **Splunk** dashboards, which are populated by **Zeek** logs. The Zeek data reveals that the machine is communicating over port 443, but Zeek's protocol analyzer flags that the traffic isn't actually standard TLS—it's an obfuscated command-and-control (C2) beacon.
3. **The Endpoint Investigation (Velociraptor):** The analyst pivots to **Velociraptor** and pushes a VQL query to that specific machine. They pull the running process list, memory map, and recent file execution history. They identify the malicious payload running in memory, isolate the machine from the network, and pull a copy of the malware for reverse engineering.

### ## Quick Comparison

| Feature | Zeek | Velociraptor | Splunk |
| --- | --- | --- | --- |
| **Domain** | Network (NSM) | Endpoint (DFIR) | Aggregation/SIEM |
| **Data Source** | Network Traffic (PCAP/Taps) | Host Artifacts (Files, Registry, Memory) | Everything (Logs, APIs, Agents) |
| **Primary Function** | Extracts metadata from network packets | Queries endpoints for forensics | Indexes, searches, and alerts on logs |
| **Cost** | Open-Source | Open-Source | Commercial (Expensive at scale) |
| **Core Engine/Language** | Zeek Script | VQL | SPL |
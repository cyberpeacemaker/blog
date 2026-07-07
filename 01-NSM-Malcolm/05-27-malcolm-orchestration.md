---
created: 2026-05-27
tags: [malcolm, nsm, arkime]
type: reference
lang: en
status: draft
---

> Related: [[MOC - Malcolm & NSM]] · [[05-26-zeek-suricata-arkime-opensearch]] · [[06-03-arkime-api]] · [[MOC - OpenSearch Querying]]

Ah, adding **Arkime** to the mix gives us the complete picture of how the data flows! You are essentially looking at the core engines that make **Malcolm** such a powerhouse for network traffic analysis.

Here is how all four of these pieces fit together to capture, store, and visualize network data.

### 1. Arkime (The Capture and Investigation Engine)

Formerly known as Moloch, **Arkime** is a massive-scale, open-source tool for indexed packet capture and search. In the Malcolm stack, Arkime has two main jobs:

* **Data Capture & Processing:** Arkime ingests full packet capture (PCAP) files or live network traffic. It saves the raw PCAP data to disk so you don't lose the exact packets, and simultaneously extracts the session metadata (like IPs, ports, protocols, and bytes transferred).
* **The Viewer (UI):** Arkime provides a highly optimized, browser-based interface that analysts use to hunt through network sessions and drill down into the raw packets of suspected security incidents.

### 2. OpenSearch & Elasticsearch (The Brain/Database)

Arkime generates a massive amount of metadata—but it doesn't store that metadata itself. That is where **OpenSearch** or **Elasticsearch** comes in.

* Arkime takes the session metadata it just extracted and indexes it directly into OpenSearch/Elasticsearch.
* Because OpenSearch/Elasticsearch are lightning-fast search and analytics engines, they allow Arkime's Viewer (and other dashboards) to search through billions of network events in milliseconds.
* *(As a reminder: Malcolm defaults to OpenSearch, but seamlessly supports Elasticsearch if you already have an Elastic stack).*

### 3. Malcolm (The Orchestrator)

**Malcolm** isn't a standalone tool; it is a meticulously configured suite that glues everything together using Docker or Kubernetes containers.

* Malcolm takes **Arkime** (for PCAPs), **Zeek** and **Suricata** (for network logs and intrusion detection), and pipes all of their output into **OpenSearch/Elasticsearch**.
* It normalizes and enriches the data (adding GeoIP info, MAC address hardware lookups, etc.) so that whether the data came from Arkime or Zeek, it is perfectly correlated in the database.
* Finally, Malcolm provides **OpenSearch Dashboards** alongside the **Arkime Viewer**, giving you a unified toolkit to either look at high-level dashboard charts or dig deep into the granular packets.

---

### The Data Flow in a Nutshell

If you were to trace a single network packet through this stack, it looks like this:

1. **Packet Arrives:** Malcolm's forwarders or sensors capture a packet.
2. **Arkime Processes:** Arkime writes the raw packet to disk and extracts the metadata.
3. **Indexing:** Arkime (and tools like Zeek via Logstash) sends the structured metadata to **OpenSearch/Elasticsearch**.
4. **Analysis:** You log into Malcolm's web interface. You use **OpenSearch Dashboards** to see a spike in weird traffic, then seamlessly pivot to the **Arkime Viewer** to query **OpenSearch/Elasticsearch** and pull up the exact raw packets from disk to see what the attacker actually did.


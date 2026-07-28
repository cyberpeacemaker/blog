---
created: 2026-07-28 21:07
updated: 2026-07-28 21:07
tags: []
type: reference
lang: en
status: draft
---
Spot on — your diagram accurately shows how Arkime interacts with the storage and database layer inside Malcolm. Arkime queries OpenSearch for indexed metadata and reaches out directly to disk whenever you need to view raw packet payloads.

To see the complete picture, we just need to add the **ingestion and analysis pipeline** that sits upstream of storage.

Here is how live network traffic or an uploaded PCAP file actually flows through Malcolm step-by-step:

Plaintext

```
               [ Live Traffic / Uploaded PCAP ]
                              │
         ┌────────────────────┼────────────────────┐
         │                    │                    │
         ▼                    ▼                    ▼
  ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
  │    Arkime    │     │     Zeek     │     │   Suricata   │
  │   Capture    │     │    Engine    │     │    Engine    │
  └──────┬───────┘     └──────┬───────┘     └──────┬───────┘
         │                    │                    │
  Raw    │ Session            │ Protocol           │ Signature
  PCAPs  │ Metadata           │ Logs               │ Alerts
         │                    ▼                    ▼
         │             ┌──────────────────────────────────┐
         │             │             Logstash             │
         │             │ (Normalizes via ECS, adds GeoIP, │
         │             │  Community ID & Malcolm fields)  │
         │             └──────────────────┬───────────────┘
         │                                │
         ▼                                ▼
┌─────────────────┐             ┌───────────────────┐
│   PCAP Files    │             │    OpenSearch     │
│     on Disk     │             │     Database      │
└────────┬────────┘             └─────────┬─────────┘
         │                                │
         │      ┌─────────────────────────┴─────────┐
         │      │                                   │
         ▼      ▼                                   ▼
  ┌───────────────────┐               ┌───────────────────┐
  │   Arkime Viewer   │               │    OpenSearch     │
  │  (UI for PCAPs &  │               │    Dashboards     │
  │   Unified Logs)   │               │ (Analytics & Maps)│
  └───────────────────┘               └───────────────────┘
```

### Step 1: Parsing & Analysis

When traffic enters Malcolm (either captured live off an interface or uploaded as a PCAP file), three distinct engines analyze it simultaneously:

1. **Arkime Capture:** Reads packet headers, indexes flow metadata (IPs, ports, protocols), and writes the raw binary packet stream (`.pcap`) directly to disk.
    
2. **Zeek:** Performs deep protocol analysis. It extracts metadata and triggers detections (generating logs like `conn.log`, `http.log`, `ssl.log`, and `notice.log`).
    
3. **Suricata:** Performs signature-based threat detection using IDS rules (generating alert logs in JSON format).
    

### Step 2: Normalization (Logstash)

Zeek logs and Suricata alerts pass through **Logstash**. Logstash:

- Maps standard fields into Malcolm's Elastic Common Schema (ECS).
    
- Calculates a shared `network.community_id` hash for cross-tool correlation.
    
- Adds GeoIP data, ASN context, and Malcolm tags.
    
- Pushes all normalized events into **OpenSearch**.
    

### Step 3: Dual Storage

- **OpenSearch DB:** Stores _all metadata_—Arkime session indexes, Zeek protocol/notice logs, and Suricata alerts.
    
- **Disk Storage:** Holds the actual raw `.pcap` files written by Arkime Capture.
    

### Step 4: Presentation

- **Arkime Viewer:** When you search inside Arkime, it queries OpenSearch to display session lists and Zeek/Suricata metadata (like the `Malcolm Common Fields` from your previous screenshot). If you expand a session to view packet details, Arkime pulls the raw byte stream directly from the PCAP file on disk.
    
- **OpenSearch Dashboards:** Queries OpenSearch directly to render visual analytics, maps, threat timelines, and aggregate statistics across all logged events.
    

Are you looking to tweak how Malcolm captures live interface traffic, or are you primarily working with offline PCAP uploads?


---
created: 2026-08-03 16:08
updated: 2026-08-03 16:08
tags: []
type: reference
lang: en
status: draft
---
You are **spot on** with the core concept! There is just one key architectural nuance to adjust: **Arkime does not store its index on disk—it stores its session index inside OpenSearch alongside Zeek and Suricata.**

Only the **raw binary PCAP files** reside directly on the disk filesystem.

## Data Architecture & Storage Breakdown

Here is how Malcolm handles, stores, and indexes your captured network data:

|**Data Category**|**Log Source**|**Stored On Disk?**|**Indexed In OpenSearch?**|**Primary Threat Hunting Use Case**|
|---|---|---|---|---|
|**Raw Packets**|PCAPs / Live Captures|**Yes**|No (Referenced by file path)|Reconstructing raw payload byte streams.|
|**Session Metadata**|Arkime|Temporary PCAP cache|**Yes**|Flow tracking, connection graphing, and payload pivoting.|
|**Protocol Logs**|Zeek|Transitory|**Yes**|Deep behavioral protocol analysis (DNS queries, TLS certs, HTTP headers).|
|**IDS Alerts**|Suricata|Transitory|**Yes**|Rule- and signature-based threat detections.|

## What Do We Call These Captured Logs?

When talking to colleagues, writing threat reports, or setting up hunting queries, security analysts usually group them under these terms:

- **Network Telemetry / NSM Artifacts**: The general umbrella term for all logs captured by Malcolm.
    
- **PCAP / Full Packet Capture**: Refers strictly to raw, unparsed packet files stored on disk.
    
- **Protocol Metadata (or Zeek Logs)**: Refers to transaction-level logs (e.g., `zeek.dns`, `zeek.http`, `zeek.conn`) parsed by Zeek.
    
- **IDS / Alert Logs (or Suricata Alerts)**: Refers to signature hits (e.g., `suricata.eve`) triggered by known malicious patterns.
    
- **Session / Flow Records**: Refers to connection-level summaries indexed by Arkime.
    

## How Malcolm Retrieves Them

When you run a hunt inside Malcolm:

1. **OpenSearch Dashboards** searches the unified OpenSearch database to query Zeek protocol metadata, Suricata alerts, and Arkime flow indices together.
    
2. **Arkime** searches OpenSearch for matching network sessions. When you click on a session to inspect the actual payload, Arkime reaches onto the **disk** to stream the corresponding **raw PCAP bytes** directly onto your screen.
    

Are you looking to write custom search queries (like Lucene or PPL) for a specific protocol in OpenSearch Dashboards, or are you trying to pivot from an alert into Arkime for PCAP extraction?


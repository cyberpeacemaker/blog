---
created: 2026-08-03 16:08
updated: 2026-08-03 16:08
tags: []
type: reference
lang: en
status: draft
---
**No, Arkime GUI does not do everything OpenSearch Dashboards can do.**

While Arkime is the only interface capable of streaming and extracting raw PCAP files from disk, **OpenSearch Dashboards** provides macro-level analytics, protocol-specific dashboards, and custom visualization capabilities that Arkime cannot replicate.

In Malcolm, these two user interfaces are designed to be **complementary tools** used together during an investigation.

## Tool Comparison: OpenSearch Dashboards vs. Arkime GUI

|**Capability**|**OpenSearch Dashboards**|**Arkime GUI**|
|---|---|---|
|**Primary Focus**|Macro-level log analytics, aggregations, & protocol dashboards.|Micro-level session tracking, payload inspection, & connection graphing.|
|**Data Sources Viewed**|All Zeek protocol logs, Suricata alerts, and system events.|Arkime Session indices + raw PCAP on disk.|
|**Raw PCAP Extraction**|❌ No (Cannot stream/download raw bytes from disk).|✅ **Yes** (Inline ASCII/Hex view and `.pcap` export).|
|**Custom Visualizations**|✅ **Yes** (Build custom pie charts, histograms, heatmaps, and datatables).|❌ No (Fixed views: Sessions, SPI View, SPI Graph, Connections).|
|**Protocol-Specific Depth**|✅ **High** (Dedicated dashboards for DNS, TLS, HTTP, Kerberos, ICS/OT, etc.).|⚠️ **Medium** (Focuses primarily on connection-level SPI fields).|
|**Payload Regex Search**|❌ No (Searches indexed fields only).|✅ **Yes** (The "Hunt" feature searches regex directly against raw PCAP on disk).|
|**Query Syntax**|DQL, Apache Lucene, PPL, and SQL.|Arkime Search Syntax (e.g., `ip.src == 192.168.1.10`).|

## What OpenSearch Dashboards Does That Arkime Can't

1. **Protocol-Specific Deep Dives:** Zeek generates detailed log streams for specific protocols (e.g., DNS queries/responses, HTTP user agents, TLS certificate fingerprints, SMB file shares, and OT protocols like Modbus). Malcolm comes with dozens of prebuilt OpenSearch dashboards specifically tailored to spot anomalies in these logs.
    
2. **Custom Visualizations & Metrics:** If you want to create a bar chart showing the _Top 10 unusual DNS queries by length_ or a heatmap of _failed SMB logins over time_, you do that in OpenSearch Dashboards.
    
3. **Cross-Log Correlation:** OpenSearch Dashboards allows you to query across multiple index patterns simultaneously using languages like DQL or PPL.
    

## What Arkime GUI Does That OpenSearch Dashboards Can't

1. **Inline Payload Viewing:** Arkime reconstructs TCP/UDP sessions and displays the actual ASCII, Hex, or UTF-8 payload bytes of the traffic.
    
2. **PCAP Download:** You can highlight a session or time window in Arkime and download a clean `.pcap` file straight to your local machine for analysis in Wireshark.
    
3. **PCAP Payload Hunting:** Arkime can perform a low-level background job ("Hunt") that runs pattern matching or regular expressions against unindexed payload bytes stored inside raw PCAP files on disk.
    
4. **Interactive Network Graphs:** Arkime includes built-in force-directed graphs (Connections tab) to visualize network top talkers and endpoint relationships visually.
    

## Recommended Malcolm Threat Hunting Workflow

Because both tools serve distinct roles, an effective hunting workflow typically looks like this:

```
[ OpenSearch Dashboards ]  --->  [ Arkime GUI ]        --->  [ Wireshark / Local Tools ]
     (Macro Hunt)                    (Micro Inspection)            (Deep Forensics)
 Spot anomaly in Zeek/Suricata   Inspect TCP session stream &   Carve downloaded PCAP file
 via aggregated metrics          view inline payload            for file extraction
```

Would you like to see how to pivot directly from a suspicious event in OpenSearch Dashboards into Arkime to view its PCAP?


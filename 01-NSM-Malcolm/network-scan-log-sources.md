---
title: "Network Scan Log Sources"
description: "Maps horizontal network scanning behavior to Zeek Notice, Suricata ET SCAN alerts, and Zeek weird logs."
created: 2026-07-20
updated: 2026-07-20
tags: [malcolm, nsm, threat-hunting]
type: reference
lang: en
status: draft
---

> Related: [[MOC - Malcolm & NSM]] · [[zeek-suricata]] · [[malcolm-threat-hunting-poi]]

Based on the scenario of attacker IPs performing a horizontal, network-wide scan to map out an environment, here is how each log type handles and categorizes this activity:

### 1. Zeek Notice (The Exact Match)

A **Zeek Notice** is the most direct and accurate mechanism for high-level behavioral detection like this.

- **`Scan::Address_Scan`**: This is the exact notice triggered when a single source IP attempts to connect to many different _destination IP addresses_ across the network. This represents a horizontal sweep designed to find active targets or open services.
    
- **`Scan::Port_Scan`**: (Alternative) This triggers if they are scanning multiple ports on a _single_ host (vertical scan) rather than sweeping the whole network.
    

### 2. Suricata Alert

Suricata relies on signature-based rules (most commonly the Emerging Threats ruleset). A network-wide scan will fire alerts under the **`ET SCAN`** classification:

- `ET SCAN Behavioral Host Discovery`
    
- `ET SCAN Rapid outbound connection source`
    
- `ET SCAN Potential SSH Scan` (or RDP / SMB / VNC, depending on the targeted port)
    
- `ET SCAN Masscan Nmap User-Agent Observed` (if the attackers used default settings on standard scanning tools)
    

### 3. Zeek Weird

Zeek's `weird.log` monitors protocol anomalies and state mismatches, not high-level malicious intent. A network-wide scan will flood this log with low-level anomalies because the scanners are hitting dead IPs or tearing down connections abruptly, but it will **not** explicitly label it a "scan". You would typically see massive spikes in:

- `connection_originator_SYN_ack` (classic indicator of SYN/stealth scanning)
    
- `spontaneous_RST`
    
- `active_connection_reuse`
    

> **Summary:** If you are trying to match this specific sentence to a log signature or filter, focus on a **Zeek Notice** containing **`Scan::Address_Scan`** or a **Suricata Alert** categorized as **`ET SCAN`**.


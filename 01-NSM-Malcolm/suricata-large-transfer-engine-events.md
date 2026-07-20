---
title: "Suricata Engine Events During Scans and Large Transfers"
description: "Interprets invalid checksum and established-state SYN resend events as scan artifacts or sensor overload clues during large transfers."
created: 2026-07-20
updated: 2026-07-20
tags: [malcolm, nsm, threat-hunting]
type: reference
lang: en
status: draft
---

> Related: [[MOC - Malcolm & NSM]] · [[suricata-stream-established-syn-resend]] · [[ip-fragmentation-detection]]

These two entries are **Suricata Engine Events** (specifically from the decoder and stream reassembly layers) rather than traditional, signature-based exploit alerts. They indicate low-level TCP/IP stack anomalies.

Given your previous context of **network-wide scans** and a **large file transfer**, these alerts provide highly relevant technical context about what is happening on the wire.

### 1. SURICATA TCPv4 invalid checksum (Count: 56)

This alert triggers when Suricata receives an IPv4 packet where the TCP checksum calculation fails.

- **Connection to the Scan:** Attackers frequently use advanced scanning tools (like `nmap` or `masscan`) configured to deliberately send malformed packets or custom TCP flags to probe how firewalls and operating systems react (OS fingerprinting).
    
- **Connection to the Large File Transfer:** If this happened during the heavy file transfer, it is highly likely a **sensor artifact**. When a network tap or SPAN port is overwhelmed by a massive file transfer, or if **Hardware Checksum Offloading** is enabled on the monitoring NIC, Suricata will miscalculate checksums and throw these alerts.
    
- **The Verdict:** Because the count is low (56), it points toward a brief probing attempt by the scanner or a minor packet drop/offloading blip during the file transfer, rather than a broken network.
    

### 2. SURICATA STREAM ESTABLISHED SYN resend (Count: 8)

This alert means Suricata's stream engine saw a `SYN` packet (used to _initiate_ a connection) on a TCP flow that Suricata already tracks as being in an `ESTABLISHED` state.

- **Connection to the Scan:** Scanners often rapidly cycle through target ports. If a scanning tool attempts to force open or reuse an ephemeral port combination that was just active, Suricata gets confused by the sudden overlapping `SYN` packet.
    
- **Connection to the Large File Transfer:** This is a classic symptom of **packet loss on your monitoring infrastructure**. During the large file transfer, if your TAP/SPAN port dropped packets, Suricata may have missed the `FIN` or `RST` packets that cleanly closed the connection. When the compromised host later opened a _new_ connection using the exact same source/destination port combination, Suricata saw the new `SYN` packet and assumed it was an illegal resend on the old, unclosed connection.
    

### 🔍 Analyst Summary

These alerts are the digital "exhaust" of the activity you previously detected.

The low volume (56 and 8) suggests these are not continuous network errors. Instead, they act as supporting evidence: either the attacker's scanning tools were attempting to manipulate TCP states to evade detection, or the sheer volume of the large file transfer briefly overwhelmed the monitoring interface, causing Suricata's stream engine to lose track of packet states (`SYN resend`) and timing (`invalid checksum`).


---
title: "Zeek Weird SYN Inside Connection"
description: "Explains Zeek SYN_inside_connection weird.log events and Malcolm triage pivots for repeated TCP SYNs."
created: 2026-07-18
updated: 2026-07-18
tags: [malcolm, nsm]
type: howto
lang: en
status: draft
---

> Related: [[MOC - Malcolm & NSM]] · [[zeek-suricata]] · [[malcolm-threat-hunting-poi]]

## What is `SYN_inside_connection`?

In Zeek (the network analysis engine inside Malcolm), `SYN_inside_connection` is an event generated in the **`weird.log`**. It means Zeek's TCP state machine observed a packet with the `SYN` flag set on a connection tuple (a specific source/destination IP and port combo) that it _already_ considers active, established, or mid-stream.

Under normal TCP operations, a `SYN` packet should only appear at the very beginning of a conversation (the three-way handshake). Seeing it "inside" a live connection is a protocol anomaly.

## Possible Reasons for the Trigger

The technical culprits for this event range from harmless network noise to intentional evasion techniques:

### 1. Connection Reuse (The "Fast Recycle")

- **What happens:** A client connects to a server, finishes its transaction, closes the socket, and immediately opens a _new_ connection using the **exact same source port** to the same destination.
    
- **Why Zeek flags it:** If Zeek hasn't timed out or cleaned up the state of the _previous_ connection from its memory tables yet, it treats the new `SYN` packet as if it belonged to the old session, triggering the "weird" event. This is incredibly common with aggressive IoT devices, high-frequency APIs, or heavy proxy server traffic.
    

### 2. Sensor Misordering & Packet Drops

- **What happens:** The network tap, packet broker, or the Malcolm capture interface experiences a momentary packet buffer delay or dropped packets.
    
- **Why Zeek flags it:** If a data packet gets processed by Zeek _before_ the handshake's `SYN` packet arrives (forcing Zeek to spin up a partial mid-stream connection), the late-arriving `SYN` packet will look like it is jumping into the middle of a live stream.
    

### 3. Asymmetric Routing or Missing Teardowns

- **What happens:** Zeek only sees one side of the network traffic, or a minor network disruption causes Zeek to miss the `FIN` or `RST` packets that ended an original session.
    
- **Why Zeek flags it:** Because Zeek never saw the connection end, it keeps it alive as a "zombie" session in its memory. When the host legitimately spins up a brand-new connection on that same port later, it collides with the zombie session and flags the alert.
    

### 4. Malicious NSM/IDS Evasion (TCP Splicing)

- **What happens:** An attacker intentionally injects a spoofed or raw `SYN` packet into an already active session.
    
- **Why Zeek flags it:** Legacy intrusion detection systems often get confused by unexpected handshakes mid-stream and completely drop state tracking for that traffic session. Attackers use this tactic to try and "blind" network sensors so they don't analyze subsequent malicious payloads. Zeek explicitly logs this so you know something is violating protocol standards.
    

## 🔍 How to Triage this in Malcolm

`weird.log` entries are often just network quirks rather than active exploits. To determine if this is a real threat, filter for this specific connection UID in Arkime or OpenSearch Dashboards:

1. **Check the History field:** Look at the connection's history string (e.g., `ShAdD` vs `SsHhA...`). If you see multiple capital `S` characters scattered out of order, you are dealing with multiple SYNs.
    
2. **Analyze the Temporal Context:** If the multiple `SYN` packets are seconds apart on a high-traffic port (like 80 or 443), it’s likely benign connection reuse or a noisy web application.
    
3. **Cross-reference with your Hunting Leads:** If this `SYN_inside_connection` involves an internal host that recently touched a suspicious phishing link or domain (like the `sel.com` lead from earlier), treat it with **high priority**. It could indicate custom malware or a C2 beacon trying to use evasion techniques to mask its traffic.


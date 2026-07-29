---
title: "Zeek, Arkime, and OpenSearch ID Pivots"
description: "Maps OpenSearch document IDs, Zeek UIDs, and network endpoints for pivoting from Malcolm alerts into session evidence."
created: 2026-07-28
updated: 2026-07-28
tags: [malcolm, nsm, opensearch]
type: reference
lang: en
status: draft
---

> Related: [[MOC - Malcolm & NSM]] · [[zeek-connection-id]] · [[zeek-fuid-cuid]] · [[arkime-opensearch-roles]]


This image shows a **Zeek Notice alert** indexed into OpenSearch via **Arkime** (formerly Moloch, indicated by the index name `arkime_sessions3-240425`).

Here is how all the IDs and network identifiers we discussed map directly to this log entry:

### 1. `_id` (`240425-PDU0LfLs5wrFp06Cw1gG5w`)

- **What it is:** The **OpenSearch Document Identifier**.
    
- **Why it looks like this:** Arkime generates custom `_id` values by prefixing the session date (`240425-` for April 25, 2024) followed by a unique hash string.
    
- **Goal & Usage:** OpenSearch uses this to pinpoint this exact record in the database. If Arkime re-indexes or updates this session record, it uses this `_id` to prevent duplicate documents.
    

### 2. `event.id` (`CuE12U2mZAu5eB87j`, `FY3IJ14pp1TcbZV88`)

- **What it is:** These are **Zeek UIDs**.
    
- **Why there are two:** `CuE12U2mZAu5eB87j` is the classic 18-character Zeek connection UID format. The notice framework attached these session identifiers to the alert message.
    
- **Goal & Usage:** This is your primary **pivot key**. If you want to see the full SSL handshake details or connection metrics for this specific alert, you copy `CuE12U2mZAu5eB87j` and filter by `zeek.uid` or `uid` in your `ssl.log` or `conn.log` indices.
    

### 3. `source.ip` and `destination.ip`

- **What it is:** The IP address components of Zeek's 4-tuple **`id`** (`id.orig_h` $\rightarrow$ `192.168.65.55` and `id.resp_h` $\rightarrow$ `10.99.32.103`), mapped into ECS (Elastic Common Schema) format.
    
- **Goal & Usage:** It tells you directionality. `192.168.65.55` (Originator) initiated an SSL/TLS connection to `10.99.32.103` (Responder), but the server provided an untrusted/self-signed cert (`unable to get local issuer certificate`).
    

### How to use this during an investigation

1. You see this alert in OpenSearch indicating an **Invalid Server Cert**.
    
2. You take the **`event.id`** (`CuE12U2mZAu5eB87j`) and search your Zeek `ssl.log` to see the exact certificate issuer details and server name (SNI).
    
3. You take the OpenSearch **`_id`** or open the Arkime link to jump straight to the full PCAP (raw packet capture) for that exact connection.
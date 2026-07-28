---
created: 2026-07-28 20:07
updated: 2026-07-28 20:07
tags: []
type: reference
lang: en
status: draft
---
In Zeek (formerly Bro), **`id`** refers to the **`conn_id`** record type—the core data structure Zeek uses to represent the endpoints of a network connection.

Instead of traditional "source" and "destination," Zeek uses the concepts of **Originator** (the party initiating the flow) and **Responder** (the party accepting/replying to the flow).

## What is `id`?

At its core, `id` is a 4-tuple record containing the network socket information for both ends of a conversation. Defined in Zeek's scripting language, it looks like this:

Code snippet

```
type conn_id: record {
    orig_h: addr;  # Originator IP address
    orig_p: port;  # Originator port
    resp_h: addr;  # Responder IP address
    resp_p: port;  # Responder port
};
```

Whenever Zeek raises an event or generates a log for a connection, the `id` record is attached to the parent `connection` object (accessible as `c$id`).

> **Note:** Do not confuse `id` with `uid`.
> 
> - **`id`** is the 4-tuple network endpoint record (`orig_h`, `orig_p`, `resp_h`, `resp_p`).
>     
> - **`uid`** is a unique, randomly generated alphanumeric string (e.g., `C1a2B3c4D5e`) assigned to every distinct connection session to make log joining easier.
>     

## The Goal of `id`

Zeek uses the `id` record to achieve several design goals:

1. **Directional Awareness:** Traditional packet capturing labels traffic by static source and destination. Zeek tracks state to determine who _initiated_ the session (`orig`) and who _responded_ (`resp`). This makes policy enforcement and threat hunting vastly clearer.
    
2. **Context Persistence Across Protocol Parsers:** A single TCP connection might trigger DNS, TLS, and HTTP loggers. Using a standardized `id` across all event handlers ensures protocol analyzers have a consistent way to reference the underlying flow.
    
3. **Structured Event Routing:** In Zeek scripts, event handlers pass around the connection context. Having a unified identifier allows scripts to query IP addresses or ports easily without re-parsing raw packet headers.
    

## How `id` is Used

### 1. In Log Files

Virtually every protocol log that Zeek generates (`conn.log`, `http.log`, `dns.log`, `ssl.log`, etc.) flattens the `id` record into four standard log columns:

|**Log Field**|**Meaning**|**Example**|
|---|---|---|
|`id.orig_h`|Originator (Client) IP|`192.168.1.50`|
|`id.orig_p`|Originator Source Port|`52140`|
|`id.resp_h`|Responder (Server) IP|`142.250.190.46`|
|`id.resp_p`|Responder Destination Port|`443`|

### 2. In Zeek Scripting

When writing custom Zeek scripts, you interact with `c$id` within event handlers to inspect traffic, filter connections, or trigger alerts.

**Example:** Triggering an alert when a specific IP tries to access SSH:

Code snippet

```
event ssh_auth_successful(c: connection, auth_method: string) {
    # Check if the originator IP is in a sensitive subnet
    if ( c$id$orig_h in 10.0.0.0/8 ) {
        print fmt("Internal host %s authenticated via SSH to %s:%s", 
                  c$id$orig_h, c$id$resp_h, c$id$resp_p);
    }
}
```

### 3. In Log Correlation & Threat Hunting

While `uid` is preferred for fast database indexing (like in SIEMs or Elasticsearch), the `id` tuple lets analysts pivot directly between Zeek logs and other network tools (like Wireshark or firewall logs) using standard 4-tuple IP/port filtering.


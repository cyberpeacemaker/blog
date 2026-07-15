---
title: "Velociraptor and Wazuh"
description: "Compares Velociraptor and Wazuh roles across endpoint collection, DFIR, and SIEM-style monitoring."
created: 2026-07-15 10:07
updated: 2026-07-15
type: reference
lang: en
status: draft
tags: [nsm, dfir, siem]
---

> Related: [[MOC - Malcolm & NSM]] · [[zeek-velociraptor-splunk]] · [[soc-tool]]

# Velociraptor and Wazuh
While Snort and Suricata battle it out on the wire, **Wazuh** and **Velociraptor** are titans on the endpoints themselves.

However, comparing them directly is slightly unfair because **they are not direct competitors—they are actually the ultimate complementary duo**. Wazuh is a continuous Security Information and Event Management (SIEM) and Extended Detection and Response (XDR) platform that acts as your daily alarm system. Velociraptor is a surgical Digital Forensics and Incident Response (DFIR) platform built to hunt threats and pull evidence at scale when that alarm goes off.

If Wazuh is the smoke detector, Velociraptor is the arson investigator.

## At-a-Glance Comparison

|**Feature**|**Wazuh**|**Velociraptor**|
|---|---|---|
|**Primary Category**|SIEM / XDR|Digital Forensics & Incident Response (DFIR)|
|**Operational Model**|Continuous, real-time log ingestion & alerts|On-demand forensic querying & "hunting"|
|**Core Query Engine**|XML-based Rules / Decoders|Velociraptor Query Language (VQL)|
|**Server Resource Usage**|**Very High** (Requires OpenSearch indexing)|**Extremely Low** (Queries are run client-side)|
|**Primary Strength**|Log management, vulnerability scans, compliance|Raw disk analysis, memory hunting, rapid triage|
|**Automated Response**|"Active Response" (e.g., block IP, kill process)|Custom script/VQL execution (e.g., isolate host)|

## Wazuh: The Continuous Sentinel

Wazuh is built on top of the legacy OSSEC host-intrusion detection system. It aggregates endpoint telemetry, parses system logs, monitors file integrity, and correlates everything back to a central OpenSearch dashboard.

### Pros of Wazuh

- **Unified SIEM + XDR Framework:** You get log aggregation, file integrity monitoring (FIM), vulnerability assessment, and compliance mapping (MITRE ATT&CK, PCI-DSS) in one single platform.

- **Massive Out-of-the-Box Ruleset:** Comes packed with over 3,000 pre-configured detection rules. You don't have to start from scratch to detect basic ransomware behavior, brute-force attacks, or policy violations.

- **Active Response:** Can trigger automated actions instantly. If it detects a brute-force attack from a specific IP, it can automatically trigger a firewall rule on the endpoint to block it.


### Cons of Wazuh

- **Infrastructure Heavy:** Running Wazuh at scale requires a massive server footprint. The OpenSearch backend requires heavy CPU, RAM, and storage optimization to prevent indexing delays.

- **No Deep Forensics:** Wazuh tells you _that_ a file was changed or a process was spawned. However, it lacks the ability to pull raw memory dumps, analyze deep Master File Table (MFT) records, or carve out deleted files.

- **Rigid Configurations:** Making changes to decoders or custom rules often requires a full system restart of the Wazuh manager, which can create friction in fast-moving operations.


## Velociraptor: The Forensic Surgeon

Velociraptor (maintained by Rapid7) is built around the concept of "hunting". Rather than streaming every event to a central database continuously, it keeps its agent asleep until an investigator fires off a query.

### Pros of Velociraptor

- **Surgical Precision with VQL:** Velociraptor Query Language (VQL) is incredibly powerful. You can write a query to search the registry, dump memory of a specific process, parse event logs, and fetch target files—simultaneously across 10,000 machines—in under five minutes.

- **Lightweight Storage Footprint:** Because you are pulling data _on-demand_ rather than continuously collecting trillions of raw logs, the server infrastructure is lightweight and incredibly cost-effective to host.

- **Rapid Threat Hunting:** If a new zero-day exploit drops, you can write or download a custom VQL "Artifact" from the community exchange and immediately sweep your entire fleet to find compromised machines.

- **Collaborative Notebooks:** Built-in Jupyter-like notebooks allow incident response teams to collaborate and parse evidence directly in the console.


### Cons of Velociraptor

- **Extremely Steep Learning Curve:** VQL is essentially its own programming language. To leverage Velociraptor's full potential, you must write complex queries and understand advanced, low-level OS forensics (like USN journals, Shimcache, and Prefetch).

- **Not a Log Aggregator:** It is not meant to be your long-term audit trail. It will not act as a central repository for years of general Windows event logs or network traffic logs.

- **High Operator Risk:** Because Velociraptor allows you to execute raw, low-level system commands and script actions directly on endpoints, a poorly written VQL query can consume 100% CPU on target systems or accidentally modify crucial system files if not tested properly.


## The Verdict: Which to Deploy?

In a mature Security Operations Center (SOC), **you don't choose between them—you run both**.

> **Deploy Wazuh if:**
>
> - You need a daily driver for continuous monitoring, compliance reporting, and vulnerability scanning across your infrastructure.
>
> - You want an all-in-one SIEM/XDR dashboard out of the box with minimal customization required to start alerting.
>

> **Deploy Velociraptor if:**
>
> - You are actively responding to incidents, performing digital forensics, or proactively hunting for sophisticated threats across your endpoints.
>
> - You have a mature security engineering team that can utilize VQL to inspect deep system state on-demand.
>

Many organizations use Wazuh to continuously monitor the fleet, and when a high-severity alert is triggered, an analyst fires up Velociraptor to surgically investigate and triage the affected endpoint.

What kind of environment are you planning to secure, and are you looking to build a daily monitoring setup or prepare a dedicated incident response toolkit?

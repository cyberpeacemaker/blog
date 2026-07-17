---
title: "Choose RITA for Threat Hunting Integrations"
description: "Explains why RITA is a better development integration target than AC-Hunter for custom security dashboards and pipelines."
created: 2026-07-17
updated: 2026-07-17
type: reference
lang: en
status: draft
tags: [threat-hunting, nsm]
---

> Related: [[MOC - Threat Hunting]] · [[zeek-rita]] · [[malcolm-rita-integration]]
If your goal is to build a development project centered around integration—such as tying threat data into a SIEM, automating incident response via SOAR, or building a custom security dashboard—**RITA is unequivocally the better choice.**

While AC-Hunter is a fantastic out-of-the-box solution for security analysts who want a ready-to-use interface, it is ultimately a proprietary tool. RITA, on the other hand, is designed like an open engine meant to be wired into larger systems.

## Why RITA is a Developer's Best Friend

### 1. Powered by ClickHouse (Open & Accessible)

RITA uses **ClickHouse** as its backend database. ClickHouse is an incredibly fast, open-source columnar database.

- **The Integration Win:** Because the database is fully open, you aren't restricted to a limiting API. Your code can connect directly to ClickHouse using native database drivers (Python, Go, Node.js, etc.) to query beaconing scores, DNS tunneling data, or long connections using standard SQL.
    

### 2. True Open-Source Freedom

RITA is free and open-source on GitHub.

- **The Integration Win:** You don't have to worry about hitting license caps, paywalls, or restrictive terms of service as your project scales. If you need to change how RITA parses logs or aggregates its behavioral math to fit your specific project, you can fork the source code and modify it directly.
    

### 3. Highly Scriptable Pipelines

RITA operates seamlessly via the command line and configuration files.

- **The Integration Win:** It natively ingests standard Zeek logs (TSV or JSON). You can easily build automated ETL pipelines (using Python, Bash, or cron jobs) that grab network telemetry, feed it into RITA (`rita import`), run the analytics (`rita analyze`), and export the results programmatically.
    

## The Roadblocks with AC-Hunter for Developers

Trying to build a third-party development project around AC-Hunter will likely run you into a couple of walls:

- **Closed Ecosystem:** AC-Hunter is a commercial product. Even with the free Community Edition, you don't have back-end code visibility.
    
- **API Paywalls:** Accessing raw threat data programmatically often requires enterprise-tier API access, which is restrictive for a lean development or open-source project.
    

## Inspiring Project Ideas You Can Build Around RITA

- **Custom Threat Dashboards:** Query RITA’s ClickHouse database directly to build custom network threat visualization maps in **Grafana** or a custom **React** front-end.
    
- **SOAR Automated Containment:** Write an integration script that checks RITA's high-severity beacon scores every hour. If an internal IP score crosses a specific threshold, your script automatically talks to a firewall or EDR API to isolate the host.
    
- **SIEM Log Forwarder:** Build a lightweight pipeline app that takes RITA's finished analytical outputs, formats them into Syslog/JSON, and streams them into platforms like Splunk, Elastic, or Microsoft Sentinel.
    

What kind of app or platform are you planning to integrate this threat data into?


---
title: "Zeek Notice Hunt Lead Algorithm"
description: "Interprets a Zeek Notice summary row as a prioritized threat-hunting lead with MITRE context."
created: 2026-07-28
updated: 2026-07-28
tags: [malcolm, nsm, threat-hunting, mitre]
type: reference
lang: en
status: draft
---

> Related: [[MOC - Malcolm & NSM]] · [[MOC - Threat Hunting]] · [[zeek-notice-hunt-lead-severity]]

Here's how to interpret this summary panel from your security dashboard (commonly seen in Network Detection and Response tools like Corelight/Zeek or SIEMs like Splunk):

### **Overview**

This table provides an aggregated view of high-priority security notices triggered on your network, mapped directly to the **MITRE ATT&CK® framework**. It indicates that potential attacker activity inside your internal network was detected.

### **Column Breakdown**

- **Notice Category (`ATTACK::Lateral_Movement_...`)**
    
    - **Meaning:** This refers to the **MITRE ATT&CK Lateral Movement** tactic (TA0008).
        
    - **Context:** Lateral movement occurs when an adversary, having already compromised an initial system, attempts to pivot to other hosts on the network to access sensitive data or gain higher privileges (e.g., via SMB/PsExec, SSH, RDP, WMI, or pass-the-hash techniques).
        
- **Count (`8`)**
    
    - **Meaning:** Exactly **8 individual alert notices** matching this category were triggered within the selected timeframe.
        
- **High Raw Severity (`155`)**
    
    - **Meaning:** This is the highest raw numerical risk/severity score calculated among those 8 notices. In threat-scoring models (such as Zeek's notice framework or SIEM correlation rules), a score around 155 signifies a high-confidence or high-risk event that demands analyst investigation.
        

### **Recommended Next Steps**

1. **Drill into the Event Details:** Click into this category row to inspect the individual log entries. Identify the **Source IP**, **Destination IP**, and **User Accounts** associated with the 8 notices.
    
2. **Identify the Vectors:** Check what protocol or tool was used (e.g., abnormal SMB admin share usage, unusual SSH sessions, PSExec, or remote management tools).
    
3. **Correlate with EDR Logs:** Cross-reference the source and destination hosts with your Endpoint Detection and Response (EDR) platform to see what processes executed around the time of the alerts.
    
4. **Contain if Necessary:** If the activity is unapproved or malicious, isolate the originating host to prevent further movement across the network.
    

Are you looking to write a specific query to drill into these 8 events, or do you already have the detailed logs available?


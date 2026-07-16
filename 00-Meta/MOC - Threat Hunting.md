---
created: 2026-07-07
tags: [threat-hunting, dfir, mitre, moc]
type: hub
lang: en
status: published
---

# MOC - Threat Hunting

Threat hunting methodology, forensics, CTF, and write-up standards.

## Methodology & Frameworks
- [[ai-threat-hunting-capabilities]] — AI capabilities in threat hunting detection

- [[threat-hunt-evolution]] — threat hunting maturity model
- [[mitre]] — MITRE ATT&CK / CTI reference
- [[writeup-guideline]] — write-up quality framework (no time-travel analysis)
- [[qa-infosec]] — infosec Q&A reference

## Forensics & Investigation

- [[cross-id-analysis]] — Zeek UID and Community ID pivots across logs and PCAP
- [[zeek-seen-bytes]] — volumetric profiling with Zeek `seen_bytes`
- [[raw-tcp-spoofed-http-c2]] — high-entropy raw TCP traffic masquerading as HTTP
- [[wireshark-export-object-multipart-fix]] — recover payloads from multipart Export Objects output
- [[bec-lab-pcap-dedup]] — duplicate BEC lab PCAP ingestion and session reasoning
- [[bec-pcap-analysis-summary]] — BEC lab PCAP and JAS5 session analysis summary
- [[ip-fragmentation-evasion]] — IP fragmentation as an inspection evasion technique
- [[forensic-remote-control]] — C2 forensics (Caldera)
- [[forensic-same-mac-dhcp]] — same MAC / DHCP forensics
- [[c2ma]] — C2 malware analysis
- [[inforensic-1m-review]] — inforensic review
- [[windows-user-determine]] — Windows folder ownership / SID forensics

## Malware & Offense
- [[threat-hunting-c2-volume-beacon]] — C2 volume beacon traffic profile
- [[c2-turns-traffic-profile]] — packet and stream turns as a C2 behavior profile
- [[powershell-encodedcommand]] — PowerShell EncodedCommand decoding and detection context
- [[zeek-rita]] — Zeek logs feeding RITA beacon analytics
- [[caldera-beacon-visualization]] — interpret Caldera beacon visualizations
- [[caldera-sandcat-powershell-decode]] — decode Sandcat PowerShell C2 command examples

- [[MobileRAT]] — mobile RAT analysis
- [[cyberstalker]] — cyberstalker case
- [[persistent]] — persistence techniques
- [[tracking]] — tracking methodology
- [[tracking-ori]] — tracking (original notes)
- [[beacon]] — C2 beacon detection (behavioral / statistical)
- [[anti-virus]] — AV false positives during malware research
- [[YARA]] — malware pattern matching and threat hunting rules

## Encrypted Traffic Analysis

- [[eta-threat-hunting-overview]] — encrypted traffic analysis overview for threat hunting
- [[eta-advanced-scenarios]] — advanced ETA scenarios for C2 and anomaly hunting
- [[eta-splunk-kql-alpn]] — Splunk, KQL, and ALPN query ideas for ETA
- [[eta-tls13-ech-markov]] — TLS 1.3, ECH, and Markov behavior modeling
- [[eta-markov-hmm]] — Markov and HMM modeling for encrypted traffic
- [[eta-ja4-ja4l-session-resumption]] — JA4, JA4L, and session resumption fingerprints
- [[bec-encrypted-traffic-analysis]] — BEC case study for encrypted traffic behavior analysis

## Threat Intel

- [[google-threat-intelligence]] — Google Threat Intelligence

## CTF

- [[CTF-roadmap]] — CTF learning roadmap
- [[threat-hunting-ctf-get-started]] — CTF vs real-world threat hunting

## Related

- [[MOC - Malcolm & NSM]] — data sources for hunting
- [[My Stack]] — Obsidian threat intel plugins (IOC Lens, SOC Toolkit)

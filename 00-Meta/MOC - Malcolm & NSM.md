---
title: "MOC - Malcolm & NSM"
description: "Maps Network Security Monitoring, Malcolm, Arkime, OpenSearch, sensors, and OT/ICS notes."
created: 2026-07-07
updated: 2026-07-27
tags: [malcolm, nsm, opensearch, moc]
type: hub
lang: en
status: published
---

# MOC - Malcolm & NSM

Network Security Monitoring stack: sensors, indexing, PCAP analysis, and Malcolm orchestration.

## Pipeline & Architecture

- [[zeek-suricata-arkime-opensearch]] — full NSM pipeline overview
- [[malcolm-orchestration]] — Malcolm deployment and orchestration
- [[malcolm-rita-integration]] — Malcolm, Zeek, OpenSearch, and RITA integration paths
- [[malcolm-threat-stack-integration]] — Malcolm, Suricata, Zeek, and RITA stack roles
- [[nsm]] — NSM fundamentals
- [[zeek-suricata]] — Zeek and Suricata sensors
- [[suricata-snort]] — Suricata and Snort IDS comparison
- [[critial-infrastructure]] — critical infrastructure context

## Arkime & PCAP

- [[arkime-dnp3-field-mismatch]] — DNP3 query pivots across native Arkime fields and Malcolm ECS datasets
- [[arkime-spigraph-connections-node-limit]] — Query Size sampling limits in Arkime Connections graphs
- [[arkime]] — Arkime overview
- [[arkime-http-md5]] — Arkime `http.md5` triage, deduplication, and threat intel pivots
- [[arkime-http-md5-bypass]] — hash-only detection bypass patterns
- [[arkime-session-splitting]] — raw PCAP fallback for late keep-alive tasks
- [[arkime-split-session-large-upload]] — interpret split Arkime rows as one high-volume upload flow
- [[arkime-root-session-pcap-download]] — prefer root session IDs when exporting PCAPs
- [[arkime-http-post-file-carving]] — export split sessions and carve HTTP POST payloads
- [[arkime-parser-keepalive-bug]] — HTTP parser state reset failure mode
- [[arkime-time-zoom-panel]] — timeline zoom workflow
- [[arkime-api]] — Malcolm `/arkime` API debugging
- [[malcolm-api-example]] — scripting options for Arkime, OpenSearch, and upload APIs behind Malcolm
- [[arkime-query-opensearch]] — Arkime queries via OpenSearch
- [[arkime-cap-sample]] — PCAP sample analysis
- [[wireshark-contain]] — Wireshark containment filters
- [[wireshark-tcp-reassembly]] — TCP reassembly and IP fragmentation distinctions
- [[wireshark-follow-stream-yaml]] — Follow Stream YAML packet mapping and export fields
- [[wireshark-pcap-file-extract]] — file extraction limits and payload analysis in PCAPs
- [[ftp-tcp]] — FTP control and data channels over TCP

## OpenSearch & Indexing

- [[suricata-opensearch-alert-search]] — wildcard and Query DSL patterns for uncertain Suricata alert fields
- [[malcolm-it-ot-subnet-filter]] — OpenSearch and Arkime filters for IT/OT subnet traffic boundaries
- [[opensearch-elasticsearch]] — OpenSearch vs Elasticsearch
- [[opensearch-index-patterns]] — index pattern and dashboard management concepts
- [[malcolm-opensearch-json-dsl]] — Malcolm GUI to JSON DSL
- [[opensearch-api-dsl-dev-tools]] — relationship between OpenSearch APIs, Query DSL, and Dev Tools
- [[opensearch-lucene-quoted-wildcards]] — why quoted Lucene wildcards return zero matches
- [[elasticsearch-bool-should]] — why `should` must live inside a bool query wrapper
- [[opensearch-bool-minimum-should-match]] — force bool `should` clauses to behave as required OR filters
- [[opensearch-term-range-match]] — compare term, range, and match query clauses
- [[opensearch-query-aggs-return-result]] — combine search endpoints, `size: 0`, and aggregations for grouped results
- [[threat-lead-filter-example-smtp]] — OpenSearch filters for broad SMTP Suricata lead expansion
- [[metadata-indexing]] — metadata indexing
- [[duplicated-id]] — duplicated ID issues
- See also: [[MOC - OpenSearch Querying]]

## Sensors & Log Sources

- [[mime-http]] — MIME type fundamentals for HTTP and file classification
- [[http-md5-zeek-mime-type]] — Arkime `http.md5` versus Zeek `mime_type`
- [[zeek-weird-syn-inside-connection]] — Zeek `SYN_inside_connection` causes and Malcolm triage pivots
- [[suricata-alert-smtp-invalid-reply]] — Suricata SMTP invalid reply parser event triage
- [[suricata-large-transfer-engine-events]] — scan and large-transfer context for Suricata engine events
- [[suricata-stream-established-syn-resend]] — Suricata established-state SYN resend anomaly contexts
- [[network-scan-log-sources]] — map scan behavior to Zeek Notice, Suricata, and Zeek weird logs
- [[zeek-files-mime-type-mz]] — Zeek MIME labels and Windows MZ magic bytes
- [[zeek-fuid-cuid]] — Zeek connection UID and file FUID pivots
- [[zeek-file-reassembler]] — ranged downloads and Zeek file reassembly
- [[syslog]] — syslog configuration
- [[filter]] — log filtering
- [[ecs-translation]] — ECS field translation
- [[malcolm-timezone]] — Malcolm timezone handling
- [[zeek-velociraptor-splunk]] — Zeek + Velociraptor + Splunk
- [[tshark-env-path]] — tshark environment path
- [[ip-fragmentation-detection]] — Snort, Suricata, Zeek, and Wireshark fragmentation detection
- [[lldp-tlv]] — LLDP TLV analysis

## OT / ICS

- [[industrial-annual-maintenance]] — Chinese annual maintenance term and high-risk OT maintenance windows
- [[scada-rtac-ews]] — SCADA, RTAC, and EWS roles in industrial automation
- [[modbus-s7comm]] — Modbus and Siemens S7comm protocol comparison
- [[proprietary-protocol]] — proprietary protocol definition and tradeoffs
- [[plc-security-logs]] — PLC telemetry versus security log constraints and OT cost tradeoffs
- [[siemens-delta-port-config]] — Chinese notes on Siemens and Delta OT lab box port mapping differences
- [[dnp3-unknown-object]] — triage Suricata DNP3 unknown object alerts with packet evidence
- [[ot-hmi-ews-plc-rtu]] — OT HMI/EWS/PLC/RTU
- [[ics-historian-jumpbox]] — ICS historian jumpbox

## SOC Tools

- [[soc-tool]] — SOC tooling overview
- [[velociraptor-wazuh]] — endpoint DFIR and SIEM-style monitoring roles
- [[malcolm-cyberchef-magic]] — CyberChef Magic constraints in Malcolm automation
- [[hostname]] — hostname handling

## Related

- [[MOC - Threat Hunting]] — hunt methodology using this stack
- [[MOC - OpenSearch Querying]] — query syntax deep dive
- [[My Stack]] — full tool inventory

---
created: 2026-07-07
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
- [[nsm]] — NSM fundamentals
- [[zeek-suricata]] — Zeek and Suricata sensors
- [[critial-infrastructure]] — critical infrastructure context

## Arkime & PCAP

- [[arkime]] — Arkime overview
- [[arkime-http-md5]] — Arkime `http.md5` triage, deduplication, and threat intel pivots
- [[arkime-http-md5-bypass]] — hash-only detection bypass patterns
- [[arkime-session-splitting]] — raw PCAP fallback for late keep-alive tasks
- [[arkime-parser-keepalive-bug]] — HTTP parser state reset failure mode
- [[arkime-time-zoom-panel]] — timeline zoom workflow
- [[arkime-api]] — Malcolm `/arkime` API debugging
- [[arkime-query-opensearch]] — Arkime queries via OpenSearch
- [[arkime-cap-sample]] — PCAP sample analysis
- [[wireshark-contain]] — Wireshark containment filters

## OpenSearch & Indexing

- [[opensearch-elasticsearch]] — OpenSearch vs Elasticsearch
- [[malcolm-opensearch-json-dsl]] — Malcolm GUI to JSON DSL
- [[metadata-indexing]] — metadata indexing
- [[duplicated-id]] — duplicated ID issues
- See also: [[MOC - OpenSearch Querying]]

## Sensors & Log Sources

- [[mime-http]] — MIME type fundamentals for HTTP and file classification
- [[http-md5-zeek-mime-type]] — Arkime `http.md5` versus Zeek `mime_type`
- [[zeek-files-mime-type-mz]] — Zeek MIME labels and Windows MZ magic bytes
- [[zeek-fuid-cuid]] — Zeek connection UID and file FUID pivots
- [[zeek-file-reassembler]] — ranged downloads and Zeek file reassembly
- [[syslog]] — syslog configuration
- [[filter]] — log filtering
- [[ecs-translation]] — ECS field translation
- [[malcolm-timezone]] — Malcolm timezone handling
- [[zeek-velociraptor-splunk]] — Zeek + Velociraptor + Splunk
- [[tshark-env-path]] — tshark environment path
- [[lldp-tlv]] — LLDP TLV analysis

## OT / ICS

- [[ot-hmi-ews-plc-rtu]] — OT HMI/EWS/PLC/RTU
- [[ics-historian-jumpbox]] — ICS historian jumpbox

## SOC Tools

- [[soc-tool]] — SOC tooling overview
- [[hostname]] — hostname handling

## Related

- [[MOC - Threat Hunting]] — hunt methodology using this stack
- [[MOC - OpenSearch Querying]] — query syntax deep dive
- [[My Stack]] — full tool inventory

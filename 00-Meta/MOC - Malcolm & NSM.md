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

- [[2026-05-26-zeek-suricata-arkime-opensearch]] — full NSM pipeline overview
- [[2026-05-27-malcolm-orchestration]] — Malcolm deployment and orchestration
- [[2026-05-22-nsm]] — NSM fundamentals
- [[2026-05-22-zeek-suricata]] — Zeek and Suricata sensors
- [[2026-07-02-critial-infrastructure]] — critical infrastructure context

## Arkime & PCAP

- [[2026-05-27-arkime]] — Arkime overview
- [[2026-06-03-arkime-api]] — Malcolm `/arkime` API debugging
- [[2026-05-27-arkime-query-opensearch]] — Arkime queries via OpenSearch
- [[2026-06-15-arkime-cap-sample]] — PCAP sample analysis
- [[2026-06-24-wireshark-contain]] — Wireshark containment filters

## OpenSearch & Indexing

- [[2026-05-27-opensearch-elasticsearch]] — OpenSearch vs Elasticsearch
- [[2026-05-27-malcolm-opensearch-json-dsl]] — Malcolm GUI to JSON DSL
- [[2026-05-28-metadata-indexing]] — metadata indexing
- [[2026-05-28-duplicated-id]] — duplicated ID issues
- See also: [[MOC - OpenSearch Querying]]

## Sensors & Log Sources

- [[2026-05-20-syslog]] — syslog configuration
- [[2026-05-20-filter]] — log filtering
- [[2026-05-20-ecs-translation]] — ECS field translation
- [[2026-05-22-malcolm-timezone]] — Malcolm timezone handling
- [[2026-05-25-zeek-velociraptor-splunk]] — Zeek + Velociraptor + Splunk
- [[2026-06-03-tshark-env-path]] — tshark environment path
- [[2026-06-24-lldp-tlv]] — LLDP TLV analysis

## OT / ICS

- [[2026-05-28-ot-hmi-ews-plc-rtu]] — OT HMI/EWS/PLC/RTU
- [[2026-05-27-ics-historian-jumpbox]] — ICS historian jumpbox

## SOC Tools

- [[2026-07-03-soc-tool]] — SOC tooling overview
- [[2026-05-29-hostname]] — hostname handling

## Related

- [[MOC - Threat Hunting]] — hunt methodology using this stack
- [[MOC - OpenSearch Querying]] — query syntax deep dive
- [[My Stack]] — full tool inventory

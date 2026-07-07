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

- [[05-26-zeek-suricata-arkime-opensearch]] — full NSM pipeline overview
- [[05-27-malcolm-orchestration]] — Malcolm deployment and orchestration
- [[05-22-nsm]] — NSM fundamentals
- [[05-22-zeek-suricata]] — Zeek and Suricata sensors
- [[07-02-critial-infrastructure]] — critical infrastructure context

## Arkime & PCAP

- [[05-27-arkime]] — Arkime overview
- [[06-03-arkime-api]] — Malcolm `/arkime` API debugging
- [[05-27-arkime-query-opensearch]] — Arkime queries via OpenSearch
- [[06-15-arkime-cap-sample]] — PCAP sample analysis
- [[06-24-wireshark-contain]] — Wireshark containment filters

## OpenSearch & Indexing

- [[05-27-opensearch-elasticsearch]] — OpenSearch vs Elasticsearch
- [[05-27-malcolm-opensearch-json-dsl]] — Malcolm GUI to JSON DSL
- [[05-28-metadata-indexing]] — metadata indexing
- [[05-28-duplicated-id]] — duplicated ID issues
- See also: [[MOC - OpenSearch Querying]]

## Sensors & Log Sources

- [[05-20-syslog]] — syslog configuration
- [[05-20-filter]] — log filtering
- [[05-20-ecs-translation]] — ECS field translation
- [[05-22-malcolm-timezone]] — Malcolm timezone handling
- [[05-25-zeek-velociraptor-splunk]] — Zeek + Velociraptor + Splunk
- [[06-03-tshark-env-path]] — tshark environment path
- [[06-24-lldp-tlv]] — LLDP TLV analysis

## OT / ICS

- [[05-28-ot-hmi-ews-plc-rtu]] — OT HMI/EWS/PLC/RTU
- [[05-27-ics-historian-jumpbox]] — ICS historian jumpbox

## SOC Tools

- [[07-03-soc-tool]] — SOC tooling overview
- [[05-29-hostname]] — hostname handling

## Related

- [[MOC - Threat Hunting]] — hunt methodology using this stack
- [[MOC - OpenSearch Querying]] — query syntax deep dive
- [[My Stack]] — full tool inventory

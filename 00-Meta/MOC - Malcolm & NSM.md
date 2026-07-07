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

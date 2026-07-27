---
created: 2026-07-27 13:07
updated: 2026-07-27 13:07
tags: []
type: reference
lang: en
status: draft
---
Here's my recommendation: the best API approach depends on whether you are querying high-level network session data, fetching raw log documents, or uploading files programmatically.

Because Malcolm bundles Arkime and OpenSearch behind an NGINX reverse proxy, you have three primary ways to interact with it via scripts.

### Option 1: Use the Arkime API (Best for Session Queries & PCAPs)

If your goal is to search network sessions using Arkime's filter syntax (e.g., `ip == 192.168.1.50 && protocols == "dns"`), download PCAP files, or manage tags, call the **Arkime REST API** exposed through Malcolm.

#### Python Example (`requests`)

Python

```
import urllib3
import requests

# Suppress warnings if using Malcolm's default self-signed certs
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

MALCOLM_URL = "https://<MALCOLM_IP_OR_HOSTNAME>"
AUTH = ("analyst", "your_password")  # Set during ./scripts/auth_setup

# Query Arkime sessions
endpoint = f"{MALCOLM_URL}/sessions.json"
params = {
    "expression": 'protocols == "http" && ip.src == 192.168.1.100',
    "date": "-1",  # -1 searches all time; or use startTime/stopTime in Epoch seconds
    "length": 50,  # Number of sessions to return
    "facets": 0,
}

response = requests.get(endpoint, auth=AUTH, params=params, verify=False)

if response.status_code == 200:
    results = response.json()
    print(f"Total sessions found: {results.get('recordsTotal')}")

    for session in results.get("data", []):
        src_ip = session.get("a1")
        dst_ip = session.get("a2")
        proto = session.get("pr")
        print(f"[{proto}] {src_ip} -> {dst_ip}")
else:
    print(f"Error {response.status_code}: {response.text}")
```

### Option 2: Use the OpenSearch API (Best for Raw Logs & Aggregations)

If you need to perform complex JSON DSL queries, aggregate statistics across Zeek/Suricata logs, or query indices directly, connect directly to the **OpenSearch REST API**.

#### Python Example (`opensearch-py`)

First install the client: `pip install opensearch-py`

Python

```
from opensearchpy import OpenSearch

# Connect to Malcolm's OpenSearch endpoint (Port 9200 or via proxy)
client = OpenSearch(
    hosts=[{"host": "<MALCOLM_IP>", "port": 9200}],
    http_auth=("analyst", "your_password"),
    use_ssl=True,
    verify_certs=False,  # Set True if custom CA bundle is configured
)

# Search across Arkime sessions or Zeek/Suricata indices
query = {
    "size": 10,
    "query": {
        "bool": {
            "must": [
                {"term": {"event.provider": "zeek"}},
                {"range": {"@timestamp": {"gte": "now-24h"}}},
            ]
        }
    },
}

response = client.search(body=query, index="malcolm_*")
for hit in response["hits"]["hits"]:
    print(hit["_source"])
```

### Option 3: Malcolm Upload API (Best for Submitting PCAPs/Logs)

Malcolm provides an HTTP upload endpoint for programmatically pushing PCAP files or log archives for ingestion.

Python

```
import requests

url = "https://<MALCOLM_IP>/upload"
auth = ("analyst", "your_password")
files = {"file": open("sample_capture.pcap", "rb")}

response = requests.post(url, auth=auth, files=files, verify=False)
print(response.json())
```

### Key Production Tips

- **Authentication:** Malcolm uses HTTP Basic Authentication. Ensure you use the analyst credentials created during `./scripts/auth_setup`.
    
- **TLS Certificates:** By default, Malcolm generates self-signed X.509 certificates. Pass your custom CA path to `verify="/path/to/ca.crt"` in Python instead of disabling SSL verification in production environments.
    
- **Pagination in Arkime:** When querying large datasets in Arkime, pass `start` (offset) and `length` (limit) parameters to step through results without overloading memory.
    

What specific automation workflow are you looking to build (e.g., auto-extracting PCAPs, running threat hunting scripts, or bulk log ingestion)?


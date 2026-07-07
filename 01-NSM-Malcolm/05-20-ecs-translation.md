You just saved yourself hours of hair-pulling! This is exactly why checking the mapping is so critical.

Your discovery confirms a major structural detail: **Malcolm is translating all network traffic into ECS (Elastic Common Schema) format.** Because the database is using ECS, your original script would have sent requests for fields like `srcIp` and `dstPort`, OpenSearch would have said *"I don't know what those are,"* and returned exactly **0 results** without throwing an error.

Here is what your mapping data tells us, and exactly how to update your files to make them work perfectly.

---

## 1. The ECS Translation Key

Based on finding `source.ip` instead of `srcIp`, the rest of your network fields follow a predictable pattern. Use this translation key to update the field names:

| Old Script Field | New ECS Field Name | Description |
| --- | --- | --- |
| `timestamp` | **`@timestamp`** | The main event time used by the dashboard |
| `srcIp` | **`source.ip`** | Source IP address |
| `dstIp` | **`destination.ip`** | Destination IP address |
| `dstPort` | **`destination.port`** | Destination port |
| `protocol` | **`network.protocol`** | Network protocol (e.g., modbus, dnp3) |
| `bytes` | **`network.bytes`** | Total bytes transferred |
| `packets` | **`network.packets`** | Total packets transferred |

---

## 2. Updates Needed in `opensearch_client.py`

You need to make two sets of quick edits inside your wrapper script.

### Update 1: The Timestamp Filters

Everywhere you see a `"range"` block in your queries (inside `query_bec_traffic`, `scroll_bec_traffic`, `get_unique_values`, and `get_bec_stats`), change `"timestamp"` to **`"@timestamp"`**.

For example, your range blocks should look like this:

```json
"range": {
    "@timestamp": {
        "gte": start_time,
        "lte": end_time
    }
}

```

### Update 2: The `get_bec_stats` Aggregations

Scroll down to your `get_bec_stats` method and update the field names inside the `"aggs"` block so they match the ECS format:

```python
"aggs": {
    "src_ips": {"cardinality": {"field": "source.ip"}},
    "dst_ips": {"cardinality": {"field": "destination.ip"}},
    "protocols": {"terms": {"field": "network.protocol", "size": 20}},
    "ports": {"terms": {"field": "destination.port", "size": 20}},
    "bytes_stats": {"stats": {"field": "network.bytes"}},
    "packets_stats": {"stats": {"field": "network.packets"}}
}

```

---

## 3. Updates Needed in `test_opensearch.py`

Don't forget your test script! It also references the old field names when it prints out the final values.

### Update 1: Unique Values Field

Near the bottom of `test_opensearch.py` (around line 52), change the field being analyzed from `"srcIp"` to **`"source.ip"`**:

```python
# Old: src_ips = client.get_unique_values("srcIp", start_time, end_time, size=20)
# New:
src_ips = client.get_unique_values("source.ip", start_time, end_time, size=20)

```

---

## Ready for Ignition 🚀

Once you save these changes across both files, your Python script will be speaking the exact same language as your Malcolm OpenSearch database.

Go ahead and run your test script in your terminal:

```powershell
python test_opensearch.py

```
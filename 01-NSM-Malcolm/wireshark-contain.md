---
created: 2026-06-24
tags: [malcolm, nsm]
type: reference
lang: en
status: draft
---

To find packets containing **"HMI"** or **"PLC"** in Wireshark—specifically within the LLDP (Link Layer Discovery Protocol) System Description field or across other layers—you can use two main methods: **Display Filters** (highly recommended for isolating packets) or the **Find Packet tool** (for jumping between them).

---

## Method 1: Using Wireshark Display Filters (Recommended)

Display filters are the most efficient option because they instantly hide the noise and display only the relevant devices. You can type these directly into the green filter bar at the top of Wireshark.

### 1. Specific to LLDP System Description

If you want to isolate packets where the device explicitly states it is an HMI or PLC within the LLDP System Description field (as highlighted in your screenshot), use:

* **To find HMIs:** `lldp.tlv.system.desc contains "HMI"`
* **To find PLCs:** `lldp.tlv.system.desc contains "PLC"`
* **To find Both:** `lldp.tlv.system.desc contains "HMI" or lldp.tlv.system.desc contains "PLC"`

### 2. Case-Insensitive Search (Regex)

The `contains` operator is **case-sensitive**. If a vendor configures a device name in lowercase (e.g., `hmi` or `plc`), the above filters might miss it. To search without worrying about capitalization, use the `matches` operator with a regular expression:

* `lldp.tlv.system.desc matches "(?i)HMI|PLC"`

### 3. Broad Protocol Search

If a device lists its role somewhere else in the LLDP tree (like the *System Name* or *Port Description* fields), you can search the entire LLDP block:

* `lldp contains "HMI" or lldp contains "PLC"`

### 4. Broadest Network Search

If you want to find *any* packet in the entire capture file that mentions "HMI" or "PLC" (which is incredibly useful if devices are also communicating over **PROFINET**, **S7Comm**, or **HTTP**), filter by the entire frame text:

* `frame contains "HMI" or frame contains "PLC"`

---

## Method 2: Using the "Find Packet" Tool (Ctrl + F)

If you don't want to filter out your packet list but instead want to step through the packet timeline one by one, use the search toolbar.

1. Press **Ctrl + F** (or go to **Edit** > **Find Packet...**).
2. A new search bar will appear directly above your packet list. Configure its dropdown settings exactly like this:
* Change the first dropdown from **Display Filter** to **String**.
* Change the "Search In" dropdown to **Packet details**.
* Set "Case sensitive" if desired (leaving it unchecked is usually safer).


3. Type `HMI` or `PLC` into the search field and press **Enter** (or click **Find**).

> 💡 **Pro-Tip:** Once the first packet is found, you can simply press **Ctrl + N** to jump to the *Next* matching packet, or **Ctrl + B** to go *Back* to the previous one.
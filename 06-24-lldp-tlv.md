An industrial CTF, especially a Siemens-themed one, loves to test your knowledge of Layer 2 discovery protocols. When a challenge mentions **"every device's LLDP self-description,"** it is pointing you directly toward how network devices introduce themselves to the rest of the network.

Here is a breakdown of what LLDP "self-description" means, what to look for, and how to track it down for your flag.

---

## What is LLDP and the "Self-Description"?

**LLDP (Link Layer Discovery Protocol - IEEE 802.1AB)** is a vendor-neutral, Layer 2 protocol. Network devices (like Siemens Scalance switches, PLCs, and routers) use it to periodically broadcast information about themselves to their directly connected neighbors.

Think of LLDP as a device shouting its digital resume into the local network every 30 seconds.

Instead of a giant block of text, LLDP organizes this "resume" using **TLVs (Type-Length-Value)** blocks. The "self-description" the CTF is referring to is almost certainly contained within these specific TLV fields.

### Key "Self-Description" TLVs to Look For

When a device describes itself, it populates several standard TLVs. In a CTF context, the flag or the clue is usually hidden in one of these four:

| TLV Type | Name | What it Contains | Why CTFs Care |
| --- | --- | --- | --- |
| **TLV 1** | **Chassis ID** | The unique identifier for the device (often its primary MAC address). | Helps map unique hardware. |
| **TLV 2** | **Port ID** | The specific physical port sending the packet (e.g., `FastEthernet0/1`). | Crucial for mapping network topology. |
| **TLV 5** | **System Name** | The configured hostname of the device (e.g., `Siemens-Scalance-Switch-01`). | Often contains the naming convention or actual flag. |
| **TLV 6** | **System Description** | Detailed info about the device: Manufacturer, model number, hardware version, and firmware/OS version. | **High Probability Target.** Usually reveals the exact Siemens model (like *SCALANCE X204*) or firmware revision. |

---

## How to Solve This in the CTF

Depending on what artifacts the CTF provided you, here is how you extract that self-description data:

### Scenario A: You were given a PCAP (Packet Capture) file

If you are analyzing a Wireshark capture:

1. Open the file in **Wireshark**.
2. In the display filter bar at the top, type **`lldp`** and hit enter.
3. Click on any of the resulting packets.
4. In the packet details pane (the middle window), expand the **Link Layer Discovery Protocol** tree.
5. Look closely at the **System Name** and **System Description** fields. If the question asks for "every device's" description, you will need to look at LLDP packets coming from different source MAC addresses.

### Scenario B: You have access to a CLI / Terminal

If you are logged into a simulated or live Siemens switch (like a SCALANCE running ROS or SINEC OS):

* Run commands like `show lldp local-info` to see how *this* device describes itself.
* Run `show lldp neighbors detail` to see the self-descriptions of every *other* device connected to it.

---

Are you looking at a Wireshark PCAP capture for this challenge, or do you have access to a text-based device configuration/CLI dump?

---

That specific list—where Type 1 is Chassis ID and Type 5 is System Name—belongs **strictly to LLDP** (defined by the IEEE 802.1AB standard).

TLV itself is just a generic **design pattern**. Dozens of completely unrelated network protocols use the exact same TLV structure, but they map the "Type" numbers to completely different meanings.

To see how different they can be, look at how **LLDP** compares to **DHCP** (which also uses TLVs, though it calls them "Options"):

| Type Number | Meaning in **LLDP** | Meaning in **DHCP** |
| --- | --- | --- |
| **Type 1** | Chassis ID (MAC address) | Subnet Mask (e.g., `255.255.255.0`) |
| **Type 3** | Time to Live (TTL) | Router / Default Gateway IP |
| **Type 6** | Management Address | DNS Name Server IP |
| **Type 127** | Custom / Vendor Specific | Proprietary Vendor Extensions |

---

## Other Places You'll Meet TLVs

As you do more CTFs or deep-dive into networking, you will see the TLV pattern everywhere:

* **Wi-Fi (802.11):** Beacon frames use TLVs to broadcast supported data rates and encryption types.
* **Routing Protocols (OSPF / IS-IS):** Use TLVs to pass routing metrics and neighbor states.
* **Cryptographic Protocols (TLS/SSL):** Use TLVs for handshake extensions (like SNI - Server Name Indication).

## Back to Your CTF

Because your CTF question specifically asked about a device's **"LLDP self-description,"** you now know exactly what blueprint to use. You are looking for a packet using the LLDP type map, and you want to look at **Type 6 (System Description)**.

Did the CTF give you a packet capture (`.pcap`) file to analyze, or are you looking at a text output from a configuration file?

---

Yes, absolutely! You can see it directly in the raw bytes. It is hidden in plain sight inside the first two bytes of that pink highlighted section.

In your hex dump on row `0050`, look at where the pink highlight starts: **`0c 4a`**.

Here is exactly how Wireshark decodes those two bytes into **Type 6** and **Length 74**.

---

## The 16-Bit LLDP Header Formula

LLDP combines the Type and the Length into a single **2-byte (16-bit) header** to save space:

* The first **7 bits** = The TLV Type
* The next **9 bits** = The TLV Length

---

## Step-by-Step Binary Breakdown

Let's convert those first two highlighted bytes, `0c 4a`, into binary to see how the math works.

### 1. Convert Hex to Binary

* `0c` in binary is `0000 1100`
* `4a` in binary is `0100 1010`

Put them together into a 16-bit sequence:

```text
0000110001001010

```

### 2. Slice out the Type (First 7 Bits)

Take the first 7 bits from that sequence:

```text
0000110

```

Convert `0000110` from binary to decimal, and you get **6**. That is your **TLV Type 6 (System Description)**.

### 3. Slice out the Length (Remaining 9 Bits)

Take the remaining 9 bits:

```text
001001010

```

Convert `001001010` from binary to decimal:

* $64 + 8 + 2 = \mathbf{74}$

That is your **TLV Length (74 bytes)**.

---

## Reading the Payload

Immediately following those two header bytes (`0c 4a`), the actual data payload begins.

If you look at the very next bytes in row `0050`:
`53 69 65 6d 65 6e 73 2c 20...`

In ASCII translation (shown on the far right pane):

* `53` = **S**
* `69` = **i**
* `65` = **e**
* `6d` = **m**
* `65` = **e**
* `6e` = **n**
* `73` = **s**
* `2c` = **,**
* `20` = **[Space]**

Wireshark reads exactly 74 bytes of this ASCII text, resulting in the flag/clue you see highlighted: `Siemens, SIMATIC HMI, KTP700 Basic...`
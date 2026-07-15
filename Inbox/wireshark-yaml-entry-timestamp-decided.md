---
created: 2026-07-15 09:07
updated: 2026-07-15 09:07
tags: []
type: reference
lang: en
status: draft
---
It can definitely be a bit confusing to trace how Wireshark maps raw network frames to application-layer streams! You have actually reverse-engineered this perfectly.

Here is the breakdown of exactly what is happening under the hood.

### 1. "Frame" vs. "Packet" — Are they the same?

Technically, they represent different layers of the networking stack, but **in this context, yes, they refer to the same physical capture unit.**

- **In Networking Theory:** A **Frame** is Layer 2 (Data Link layer, e.g., Ethernet), while a **Packet** is Layer 3 (Network layer, e.g., IP).
    
- **In Wireshark's UI:** Wireshark uses **Frame** in its main packet list (on the left) to represent each individual row of recorded data. However, when you export or follow a stream in YAML (on the right), Wireshark labels these indexes as `packet: <number>`.
    
- Therefore, `- packet: 9` in your YAML window is pointing directly to **Frame 9** in your packet list.
    

### 2. Is the message of `packet: 9` reassembled from two packets?

**Yes, it is.**

As you spotted in the TCP details pane:

> `[2 Reassembled TCP Segments (244 bytes): #7(152), #9(92)]`

Because TCP is a stream-oriented protocol, large application-layer messages (like HTTP requests or responses) are often sliced up and sent across multiple TCP segments.

- **Frame 7** carried the first chunk (152 bytes).
    
- **Frame 9** carried the final chunk (92 bytes).
    

Wireshark’s engine is smart enough to automatically stitch these chunks back together to show you the complete, unified 244-byte application payload under `- packet: 9`.

### 3. How is the timestamp decided?

**Your intuition is 100% correct: it is decided by the last packet.**

The timestamp of your YAML entry (`1714067127.449414000`) perfectly matches the arrival time of **Frame 9** (`1714067127.449414`).

Here is why Wireshark does this:

- An application-layer message is not complete or usable until the **very last piece** of data arrives.
    
- Since the reassembly is only finished when **Frame 9** arrives, Wireshark associates the entire reassembled block (and its timestamp) with that final, completing frame.


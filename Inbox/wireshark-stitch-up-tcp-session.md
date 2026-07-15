---
created: 2026-07-15 09:07
updated: 2026-07-15 09:07
tags: []
type: reference
lang: en
status: draft
---

The process behind this "magic" is called **TCP Reassembly** (or desegmentation). It is a collaborative effort between Wireshark’s TCP analysis engine and the application-layer parser (called a "dissector").

Here is exactly how Wireshark stitches those frames together step-by-step:

## Step 1: Grouping the Conversation (The 4-Tuple)

Before Wireshark can reassemble anything, it has to make sure the packets belong to the exact same conversation. It does this by tracking the **TCP 4-tuple**:

- Source IP Address
    
- Source Port
    
- Destination IP Address
    
- Destination Port
    

If these match, Wireshark groups the packets into a single logical "flow," which is why you see them labeled under `tcp.stream eq 0`.

## Step 2: Tracking the Byte Stream (Sequence Numbers)

TCP does not understand "messages" or "files"; it only understands a continuous, raw stream of numbered bytes. Wireshark monitors this stream using two TCP header fields:

1. **Sequence Number (Seq):** The byte-offset of the data in this packet.
    
2. **Segment Length:** The size of the raw TCP data payload (calculated as: _IP Total Length - IP Header - TCP Header_).
    

Using these, Wireshark does some quick math:

$$\text{Next Expected Seq} = \text{Current Seq} + \text{Segment Length}$$

- **Frame 7** arrives with a payload of 152 bytes. Wireshark calculates the sequence number where the _next_ chunk should start.
    
- **Frame 9** arrives, and Wireshark checks its Sequence Number. It is a perfect match for the expected sequence number, meaning no bytes were lost in between.
    

## Step 3: The Application Demands More (Subdissectors)

While the TCP layer is busy aligning sequence numbers, the application-layer **dissector** (such as HTTP) is the one calling the shots.

> **How does Wireshark know the message isn't finished yet?**
> 
> When Frame 7 arrives, the HTTP dissector begins reading the header. It reads a field like `Content-Length: 244` (or notices that the HTTP headers themselves haven't ended with a double return `\r\n\r\n`).
> 
> The HTTP dissector tells Wireshark: _"I need 244 bytes to read this message, but you only gave me 152."_

This triggers Wireshark to label Frame 7 as `[TCP segment of a reassembled PDU]` (Protocol Data Unit) and hold its payload in a temporary memory buffer.

## Step 4: The Stitch-Up

Once **Frame 9** arrives with the remaining 92 bytes, the total bytes in Wireshark's virtual buffer reach the requested 244 bytes ($152 + 92 = 244$).

1. **Concatenation:** Wireshark physically merges the data payload of Frame 7 and Frame 9 in memory.
    
2. **Delivery:** It hands the completed 244-byte block back to the HTTP parser to fully decode.
    
3. **UI Mapping:** It displays the entire reassembled message on **Frame 9** (the frame that completed the puzzle) and adds the helpful metadata links pointing back to Frame 7.

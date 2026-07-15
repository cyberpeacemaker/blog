---
title: "FTP over TCP"
description: "Summarizes FTP control and data channel behavior over TCP for packet analysis."
created: 2026-07-15
updated: 2026-07-15
type: reference
lang: en
status: draft
tags: [nsm]
---

> Related: [[MOC - Malcolm & NSM]] · [[wireshark-pcap-file-extract]] · [[wireshark-contain]]

# FTP over TCP
FTP (File Transfer Protocol) goes with **TCP** (Transmission Control Protocol).

## Why TCP?

When you're transferring files, you need to make sure the entire file actually arrives intact. A single missing byte can corrupt an entire zip file, image, or software installer.

- **Reliability:** TCP guarantees that all data packets arrive in the exact order they were sent and without errors. If a packet gets lost in transit, TCP automatically requests a retransmission.

- **Connection-Oriented:** FTP establishes a stable, verified connection between the client and server before any data starts moving.


If FTP used **UDP** (which is "fire-and-forget" and doesn't guarantee delivery), your file transfers would be incredibly risky—like throwing pages of a book out a window and hoping they all land on your friend's balcony in the right order.

## How FTP Uses TCP Ports

FTP actually sets up **two** separate TCP connections to get the job done:

- **Port 21 (Control Connection):** Used for sending commands and responses (like typing in your password, changing directories, or requesting a file).

- **Port 20 (Data Connection):** Used for the actual raw file transfer itself.


> 💡 **The Exception to the Rule:** There _is_ a stripped-down file transfer protocol that uses UDP. It is called **TFTP** (Trivial File Transfer Protocol). It is used for very simple, low-overhead tasks—like booting up diskless computers or sending configuration files to network switches—where the complexity of TCP isn't needed.

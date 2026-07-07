---
created: 2026-05-28
tags: [malcolm, nsm]
type: reference
lang: en
status: draft
---

Based on the network diagram you provided, the image illustrates a standard Purdue Model-style architecture used to segment IT (Information Technology) and OT (Operational Technology) networks.

Here is a breakdown of what **HMI**, **EWS**, and **PLC/RTU** mean within that OT environment:

### **1. HMI (Human-Machine Interface)**

* **What it is:** The HMI is the digital dashboard or graphical user interface (GUI) that human operators use to interact with the industrial control system.
* **Its Role:** It translates complex data from the physical machines into readable visual representations (like charts, gauges, and process flows). Operators use the HMI to monitor the state of the physical processes, acknowledge alarms, and send control commands (e.g., opening a valve or changing a temperature setpoint).
* **Note on the image:** The red hat and glasses icon over the HMI in your diagram is a common cybersecurity symbol for an attacker or "Red Team." In the context of this image, it likely indicates that the HMI is a simulated compromised asset, a target for an attacker, or a pivot point being used to manipulate the physical processes.

### **2. EWS (Engineering Workstation)**

* **What it is:** The EWS is a highly privileged, specialized computer used by control system engineers.
* **Its Role:** While an HMI is used by *operators* for day-to-day control, the EWS is used by *engineers* to design, configure, program, and troubleshoot the actual control devices (the PLCs and RTUs). Engineers use the EWS to write logic code, update firmware, and push configuration changes directly to the controllers out in the field. Because of its deep level of access, it is a highly critical asset to secure.

### **3. OT PLC/RTU Connections**

* **What it is:** This refers to the network links connecting the supervisory OT network to the physical controllers out in the field or factory floor.
* **PLC (Programmable Logic Controller):** A ruggedized industrial computer that directly interfaces with and controls physical machinery (like robotic arms, conveyor belts, or motors) based on the logic programmed into it via the EWS.
* **RTU (Remote Terminal Unit):** Similar to a PLC but typically used in geographically dispersed environments (like oil pipelines or power grids). They collect telemetry data from remote field sensors and transmit it back to the central system (often via wireless/radio communication, which explains the antenna icon in the diagram).
* **Its Role:** The "connections" represent the fieldbus, industrial ethernet, or wireless telemetry pathways that allow the HMI and EWS to communicate with the hardware that is actually touching the physical world.
---
created: 2026-06-08
tags: [design]
type: reference
lang: en
status: draft
---

**AVEVA PI Server** (formerly known as the **OSIsoft PI Server**) is the powerhouse engine at the center of the **AVEVA PI System**.

Think of it as a massive, ultra-fast *industrial historian* and data brains-of-the-operation. It is designed to capture, store, enrich, and analyze real-time, time-series operational data from physical assets, sensors, and control systems.

Whether it's a wind turbine, a pharmaceutical batch reactor, or an entire oil refinery, the PI Server transforms raw sensor data into a structured "single source of truth" for an enterprise.

---

## The Core Components of AVEVA PI Server

Instead of just dumping data into a standard database, the PI Server uses a suite of tightly integrated features to give that data meaning:

* **PI Data Archive:** This is the foundational storage engine. It is highly optimized to ingest and compress millions of data streams (tags) per second and securely store decades of sub-second historical data without losing original precision. It even supports future timestamps for forecasting.
* **Asset Framework (AF):** Raw sensor tags (like `TI-1024.PV`) are cryptic. Asset Framework is a no-code tool that lets you build a logical blueprint (a digital twin) of your physical world. It maps those raw tags to human-friendly labels like *“Boiler 2 Temperature,”* organizing them into intuitive asset hierarchies.
* **Asset Analytics:** This layer allows engineers to create real-time, centralized calculations and KPIs without complex coding. It can track anything from simple rolling averages to complex efficiency metrics and equipment health models.
* **Event Frames:** Instead of scrolling through weeks of data, Event Frames automatically bookmark specific operational events based on triggers—such as a machine startup, a downtime event, or a product batch run. This makes it easy to compare performance across different cycles.
* **Notifications:** Built directly on top of Event Frames, this feature sends real-time alerts to operators or external systems (like generating a maintenance work order) the moment a process deviates from safe or efficient parameters.

---

## Why Is It So Widely Used?

Standard relational databases (like SQL) often crawl to a halt when trying to process millions of high-frequency sensor updates. AVEVA PI Server excels exactly where they fail.

> **Industrial Impact:** Over two-thirds of the industrial Fortune 500 rely on the PI System. It’s the industry standard in heavy sectors like power utilities, chemical manufacturing, mining, and pharma.

### Key Benefits:

* **Vendor-Neutral Integration:** It connects seamlessly to almost any legacy or modern control system (SCADA, PLC, DCS) or IIoT device using hundreds of pre-built interfaces and adapters.
* **Hybrid & Cloud Ready:** While traditionally deployed on-premises for critical operations, the modern PI Server integrates natively with cloud-based industrial intelligence platforms like CONNECT to securely share data across remote teams and AI analytics tools.
* **Data Integrity:** It uses advanced data buffering and high-availability architecture to ensure that even if a network drops, operational data is safely held at the edge and never lost.

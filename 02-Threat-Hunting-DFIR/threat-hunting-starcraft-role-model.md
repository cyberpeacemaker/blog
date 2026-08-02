---
title: "Threat Hunting StarCraft Role Model"
description: "Maps StarCraft-inspired Arbiter, Executor, and Witness roles to threat-hunting governance and peer review."
created: 2026-08-01
updated: 2026-08-02
type: concept
lang: en
status: draft
tags: [threat-hunting, dfir, workflow]
---

> Related: [[MOC - Threat Hunting]] · [[data-sensitive-opsec]] · [[threat-hunting-arbiter-executor-roles]]

Ah, Protoss lore! That makes the structure click instantly. You're drawing directly from the **Judicator Caste**, the **Executors**, and units like **Observers/Witnesses**.

Using StarCraft as a structural metaphor actually works surprisingly well for cybersecurity. It gives you a clean way to maintain **Separation of Duties (SoD)** and **privacy compliance (GDPR/PII)** while introducing built-in peer review.

Here is how your framework maps onto StarCraft lore, along with refined English terms that keep the sci-fi flair intact without losing professional clarity.

### StarCraft-Inspired Role Mapping

#### 1. Judicator / Chief Arbiter (審判長)

- **StarCraft Lore:** The Judicator Caste (e.g., Aldaris) or Arbiter unit. Operates from high above the battlefield, strictly following protocol and big-picture strategy without getting down into the tactical dirt.
    
- **Threat Hunting Role:** Works exclusively with anonymized/de-identified telemetry. Formulates hypotheses, sets scope, and designs hunting plans without being biased by user identities or sensitive data.
    
- **Suggested English Terms:** `Judicator`, `Chief Arbiter`, or `Strategic Arbiter`.
    

#### 2. Templar Executor / Executor (White) (執行官 - 白)

- **StarCraft Lore:** High Templar leadership (e.g., Artanis, Selendis). Direct battlefield commanders executing the central plan out in the light.
    
- **Threat Hunting Role:** The frontline investigator. Unlocks access to PII and real identities to test the Judicator's hypothesis and conduct deep-dive subjective analysis.
    
- **Suggested English Terms:** `High Executor`, `Templar Executor`, or `Executor (Primary)`.
    

#### 3. Nerazim Executor / Executor (Black) (執行官 - 黑)

- **StarCraft Lore:** Dark Templar / Nerazim leaders (e.g., Zeratul). Operating from the shadows, questioning rigid dogma, and challenging assumptions.
    
- **Threat Hunting Role:** The internal adversary / peer reviewer. Subjectively challenges the findings of the High Executor to eliminate confirmation bias, false positives, or flawed logic.
    
- **Suggested English Terms:** `Shadow Executor`, `Dark Executor`, or `Adversarial Executor`.
    

#### 4. Observer / Witness (見證者)

- **StarCraft Lore:** The cloaked Observer/Witness units that record battlefield telemetry and reveal hidden truths.
    
- **Threat Hunting Role:** The audit and logging layer. Non-intrusive monitoring that documents every action taken by the Executors for legal, compliance, and reporting purposes.
    
- **Suggested English Terms:** `Observer`, `Witness`, or `Audit Observer`.
    

### Suggested Terminology Sets for Your Documentation

Depending on how much StarCraft flavor you want in your final documentation, here are two naming schemes:

|**Chinese Role**|**Option A: SC-Flavored Professional**|**Option B: Full Sci-Fi Lore**|
|---|---|---|
|**審判長**|**Chief Arbiter**|**Judicator**|
|**執行官 (白)**|**Lead Executor**|**Templar Executor**|
|**執行官 (黑)**|**Adversarial Executor**|**Shadow Executor**|
|**見證者**|**Audit Observer**|**Witness**|

Would you like help drafting the operational workflow (like a step-by-step sequence diagram or playbook) showing how a hunt passes from the **Arbiter** down to the **Witness**?


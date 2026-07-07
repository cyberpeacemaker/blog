---
created: 2026-06-04
tags: [threat-hunting, mitre, zeek, suricata]
type: reference
lang: en
status: draft
---

> Related: [[MOC - Threat Hunting]] · [[mitre]] · [[writeup-guideline]] · [[MOC - Malcolm & NSM]]

# My Threat Hunting Attempts and Evolution

1. **Collected all data and ingested it all at once into the engine** > The engine crashed/overloaded.
2. **Ingested independent data sources separately into the engine** > Anomalies did not surface on their own. I realized that continuous drill-down and pivoting are necessary to make accurate judgments. Additionally, without a normal baseline for the environment, it is difficult to identify anomalies. > *Later discovered that this approach is best suited for finding interesting entry points.*
3. **Approaching via hypotheses and using filters made anomalies much easier to spot** > This started as a viable solution. > *Later, I realized there are roughly a few different approaches:*
* **Exploratory:** (Casual exploration. EX: Spotting periodic connections in visualizations, resembling programmed beaconing behavior)
* **Framework:** (EX: Systematically checking each sub-technique based on the MITRE ATT&CK framework)
* **Alert-driven:** (EX: Triggered by `zeek.weird`, `suricata.alert`)
* **Experience-based:** (EX: Knowing phishing is the most common attack vector, thus actively checking for phishing indicators)
4. **Leveraging the MITRE ATT&CK framework to explore every phase of the entire kill chain** > A very solid approach. Once the project infrastructure is fully established, combining this with script automation will likely be the optimal setup.
5. **Utilizing additional context (EX: `zeek.weird`, `suricata.log`, network topology, past experience, etc.) to dive in from interesting data points** > A very solid approach. For a human operator analyzing via a GUI, this is probably the ultimate/peak version of threat hunting.


---

### Phase 1: The "Trial by Fire" (Steps 1 & 2)

* **The Data Dump (Step 1):** Every analyst has tried this. The realization that "collect everything" leads to crashed engines, burned-out licenses, and alert fatigue is a rite of passage. You quickly learned the difference between a raw Data Lake and a finely-tuned SIEM.
* **The Baseline Epiphany (Step 2):** Realizing that anomalies don't just "jump out" without context is a major milestone. You cannot spot the abnormal if you do not define the normal. Your realization that independent data is best used as an *entry point* for pivoting rather than a definitive answer is spot on.

### Phase 2: The Maturity Leap (Step 3)

Moving to a **hypothesis-driven** approach is where real threat hunting begins. Your breakdown of the four approaches is excellent, though I will add a bit of industry terminology to frame them:

* **Exploratory (Data-Driven):** Relying on data visualization (like spotting beaconing via jitter/interval graphs). Highly effective for finding unknown unknowns.
* **Framework (Methodology-Driven):** Systematic and comprehensive, ensuring you aren't leaving gaping blind spots.
* **Experience-based (Intel/TTP-Driven):** Leveraging Threat Intelligence (CTI) and historical trends.
* **Alert-driven (Hybrid):** *A gentle correction here:* In strict security terminology, if an alert triggers an investigation, it is typically classified as **Triage or Incident Response (IR)**, not proactive hunting. *However*, using low-fidelity alerts (like `zeek.weird` or informational Suricata tags) as a pivot point to launch a broader, proactive hunt is absolutely a valid hunting strategy.

### Phase 3: The "Peak" State (Steps 4 & 5)

* **MITRE + Automation (Step 4):** You are describing **Continuous Hunting** or **Detection as Code**. By automating the checks for specific MITRE sub-techniques, you free up the human brain to do what it does best: contextual analysis. *One word of caution:* Don't treat MITRE ATT&CK as a bingo card. Achieving 100% coverage is impossible and impractical; focus on the techniques most relevant to your specific environment and industry.
* **Context-Rich Pivoting (Step 5):** You are 100% correct. The peak of human-operated threat hunting is taking an interesting artifact (a weird user-agent, an odd DNS request, a rare parent-child process tree) and pivoting through enriched data (network topologies, EDR logs, identity context) to build a narrative. The GUI is just the canvas; your intuition and the enriched data are the paint.

---

Your progression shows a deep understanding of both the technical limitations of security tooling and the analytical mindset required to actually find bad actors.


---
created: 2026-06-04
tags: [threat-hunting, dfir]
type: reference
lang: en
status: draft
---

Comparing certifications to **CTFs (Capture The Flag)** is tricky because while certifications are a "test of knowledge," CTFs are a "test of ingenuity." 

Think of a **certification** as a textbook final exam, and a **CTF** as being dropped into an escape room where the locks keep changing.

### 1. The Entry Level: "Learning the Ropes"
*   **Platforms:** **picoCTF**, **OverTheWire (Bandit)**.
*   **Difficulty vs. Certs:** These are roughly equivalent to **Security+** in terms of knowledge, but much more practical. 
*   **The Difference:** In Security+, you learn what "SSH" is. In *OverTheWire*, you actually use SSH to find a hidden password in a file you don't have permission to read.

### 2. The Mid-Tier: "The Daily Grind"
*   **Platforms:** **TryHackMe**, **Hack The Box (Easy/Medium machines)**.
*   **Difficulty vs. Certs:** These are the training grounds for **CEH** and **OSCP**. 
*   **The Difference:** **CEH** asks you which flag to use in a tool. **TryHackMe** gives you a "Guided Path" to use that tool. **Hack The Box** removes the guide and just says, "Get in." 
*   **Comparison:** Solving a "Medium" machine on Hack The Box is often harder than anything you will see on the CEH exam.

### 3. The Professional Level: "The Real Test"
*   **Platforms:** **Hack The Box (Hard/Insane)**, **Pro Labs**, **VulnHub**.
*   **Difficulty vs. Certs:** This is the level of the **OSCP**. 
*   **The Difference:** The OSCP is essentially a 24-hour CTF. If you can consistently root "Hard" machines on Hack The Box without looking at a walkthrough, you are more than ready for the OSCP. 
*   **CISSP Note:** CISSP has **zero** comparison to CTFs. You can be a world-class CTF player and fail CISSP because you don't know the proper procedure for fire suppression in a server room.

### 4. The Elite Tier: "The Black Olympics"
*   **Competitions:** **DEF CON CTF**, **Google CTF**, **PlaidCTF**.
*   **Difficulty vs. Certs:** These make the **OSCP** look like a tutorial.
*   **The Difference:** These aren't just about finding a vulnerability; they often involve "Attack/Defense" where you must patch your own code while simultaneously exploiting others. These require deep knowledge of assembly, custom exploit development, and kernel-level programming—stuff that isn't even covered in the certifications we discussed.

---

### Comparison Summary Table

| CTF / Platform | Equivalent Cert Level | Style |
| :--- | :--- | :--- |
| **picoCTF** | CompTIA Security+ | Educational / Beginner |
| **TryHackMe** | CEH / CND | Guided / Educational |
| **Hack The Box (Medium)** | OSCP | Raw Technical Skill |
| **DEF CON CTF** | *Off-the-charts* | Professional Team Competition |

### Which is better for your career?
*   **Certifications** get you the **interview**. They prove to HR that you meet a standard.
*   **CTF experience** gets you the **job**. They prove to the technical lead that you can actually solve a problem when the "standard" fails.

If you are just starting, I recommend **picoCTF** alongside your **Security+** studies. It makes the boring theory come to life.
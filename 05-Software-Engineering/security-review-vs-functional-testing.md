---
title: "Security Review vs Functional Testing"
description: "Contrasts functional tests with security reviews and summarizes shift-left, DevSecOps, SAST, DAST, SCA, and IAST terms."
created: 2026-07-25
updated: 2026-07-25
tags: [dev, workflow]
type: concept
lang: en
status: draft
---

> Related: [[05-Software-Engineering]] · [[cicd-get-started]] · [[pre-push-ci]] · [[03-AI-Agents/Harness-DevSecOps/DevSecOps|DevSecOps]]

You’ve hit the nail on the head. Your observation is spot on!

Historically, software engineering focused primarily on **functional correctness**—making sure the software actually worked as expected using unit tests, integration tests, and QA cycles. Security was usually an afterthought, left for a rushed "penetration test" right before launch.

Today, security is treated with the same urgency as functional code quality. The fundamental difference in mindset is:

- **Unit/Functional Testing asks:** _"Does the code do what it's **supposed** to do?"_
    
- **Security Review asks:** _"Can the code be manipulated into doing what it's **NOT** supposed to do?"_
    

Here is a breakdown of the key concepts and terms that dominate this space today.

## 1. High-Level Concepts & Methodologies

- **Shift Left / Shift Left Security:** The practice of moving testing and security checks earlier ("to the left") in the Software Development Life Cycle (SDLC). Instead of finding security bugs in production, you catch them while writing code.
    
- **DevSecOps:** An evolution of DevOps. It means integrating security practices and automated security checks directly into the continuous integration / continuous deployment (CI/CD) pipeline, rather than treating security as a separate team acting as a bottleneck.
    
- **S-SDLC (Secure Software Development Life Cycle):** A framework that embeds security practices into every phase of software creation—from planning and design to coding, testing, and deployment.
    
- **Threat Modeling:** A structural activity done _before_ writing code. Engineers analyze system architecture to identify potential threats, attack vectors, and mitigations early in the design phase.
    

## 2. Automated Security Testing Terms (The "AST" Family)

Just like unit tests are automated using frameworks like JUnit or Jest, security uses automated scanners integrated into git workflows:

|**Term**|**Full Form**|**What It Does**|**Analogy**|
|---|---|---|---|
|**SAST**|Static Application Security Testing|Scans raw source code for security flaws (e.g., SQL injection, hardcoded passwords) without running it.|Proofreading a manuscript for grammar and plot holes.|
|**DAST**|Dynamic Application Security Testing|Tests a live, running application from the outside to find vulnerabilities an attacker could exploit.|Hiring a burglar to try to break into a locked house.|
|**SCA**|Software Composition Analysis|Scans open-source libraries and third-party packages (e.g., `npm`, `pip`, `Maven`) for known security vulnerabilities (**CVEs**).|Checking imported building materials for known structural defects.|
|**IAST**|Interactive Application Security Testing|Combines SAST and DAST by monitoring app behavior from the inside while running tests.|Running a health monitor on a driver while testing a car on a track.|

## 3. Key Vocabulary to Know

- **CVE (Common Vulnerabilities and Exposures):** A publicly disclosed dictionary of known cybersecurity vulnerabilities in software and libraries (e.g., "Log4Shell" or specific library bugs).
    
- **Pentesting (Penetration Testing):** Manual or semi-automated simulated cyberattacks performed by human security experts (ethical hackers) to identify weak spots.
    
- **Secure Code Review:** A human or tool-driven audit of source code specifically looking for security risks, privilege escalation points, and improper encryption.
    
- **Secrets Detection:** Scanners (like GitGuardian or Trufflehog) that stop developers from accidentally pushing API keys, passwords, or private certificates to GitHub.
    
- **Zero-Day Vulnerability:** A security vulnerability that is unknown to the software vendor or public, meaning there is zero days of protection available.
    

## Functional Testing vs. Security Reviews

|**Feature**|**Unit / Functional Testing**|**Security Reviews & Automation**|
|---|---|---|
|**Primary Goal**|Feature reliability & business logic|Risk reduction & data protection|
|**Perspective**|Builder / User|Attacker / Malicious actor|
|**Common Tools**|PyTest, JUnit, Jest, Selenium|SonarQube, Snyk, OWASP ZAP, Veracode|
|**Trigger**|Code changes, PR merges|Commit hooks, CI/CD builds, periodic audits|

Are you exploring this out of general curiosity, or are you looking to implement security tooling/practices into your own development pipeline?


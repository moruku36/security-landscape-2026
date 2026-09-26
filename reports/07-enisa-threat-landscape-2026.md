---
publisher: "ENISA"
edition: "ENISA Threat Landscape 2026"
publication_date: "2026-09-22"
observation_period: "2025-01-01 to 2025-12-31"
dataset_or_scope: "Cyber incidents and events affecting the European Union, analyzed under ENISA's threat-landscape methodology"
geography: "European Union / Europe-focused"
language: "en"
primary_source: "https://www.enisa.europa.eu/publications/enisa-threat-landscape-2026"
last_verified: "2026-09-27"
---

# ENISA Threat Landscape 2026

[日本語版](07-enisa-threat-landscape-2026.ja.md)

## Why this report matters

ENISA provides a different perspective from commercial security vendors. As the European Union Agency for Cybersecurity, it emphasizes **critical/essential entities, geopolitical context, public-sector exposure, resilience, NIS2 relevance, dependencies, hacktivism, cybercrime, and state-aligned operations**.

That makes ENISA especially useful for governance and resilience decisions where the question is not only "How do attackers get in?" but also:

- Which sectors are systemically important?
- Which incidents most affect availability and public services?
- How do dependencies increase systemic risk?
- How do cybercrime, espionage, and geopolitical hacktivism interact?

## Evidence profile

| Field | Value |
|---|---|
| Observation period | Jan 1-Dec 31, 2025 |
| Geography | EU-focused |
| Source type | ENISA-collected/analyzed cyber incidents and events |
| Best use | Critical-sector risk, geopolitical context, resilience, NIS2-relevant governance |
| Main limitation | EU/public-policy perspective differs from vendor IR telemetry |

## Executive summary

ENISA's 2026 Threat Landscape describes an EU environment where traditional threats remain highly relevant but **digital dependencies amplify impact**.

Ransomware remains the most impactful incident type in the short term. Public administration is the most frequently targeted sector, heavily influenced by ideology-driven DDoS. A large majority of targeted organizations fall into NIS2 "essential" or "important" categories.

The report also shows distinct threat ecosystems:

- financially motivated cybercrime;
- state-aligned intrusion activity;
- geopolitical hacktivism;
- information manipulation;
- growing malicious use of AI.

For enterprise architects, the central ENISA lesson is that cybersecurity needs to be designed for **availability, dependency failure, and service continuity**, not only confidentiality and endpoint compromise.

## Key findings

| Finding | Observation context |
|---|---|
| **73%** of targeted organizations were NIS2 essential or important entities | 2025 incidents/events |
| Public administration was the most targeted sector at **32%** | EU incidents |
| Business services and transport each represented **8%**, manufacturing 7%, finance/banking 6% | Sector distribution |
| Ideology-driven DDoS accounted for **82%** of recorded public-administration events | Public-administration subset |
| Cybercrime represented **36%** of total analyzed events | Threat-category analysis |
| Within financially motivated activity, ransomware deployment represented **40%**, data breaches 31%, fraud/impersonation 19% | Cybercrime analysis |
| State-nexus intrusion sets primarily conducted intrusion operations (**87%**) and phishing campaigns (12%) | State-aligned activity |
| ENISA recorded **4,709 hacktivist claims** against EU Member States; more than **89%** involved DDoS | Hacktivism analysis |
| More than **48,000 new CVEs** were published in 2025, a **22% increase** from the prior year | Vulnerability landscape |
| Ransomware remained the most short-term impactful incident type | ENISA assessment |
| Emerging AI models are expected to increasingly support malicious activity | ENISA outlook |

Primary evidence: [ENISA Threat Landscape 2026](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2026) and [ENISA press release](https://www.enisa.europa.eu/news/exploring-the-evolution-of-the-cyber-threat-landscape-how-dependencies-weaken-our-digital-resilience).

## Detailed analysis

### 1. NIS2 essential/important entities dominate the target population

The 73% figure is strategically important because it shows how heavily cyber activity affects organizations that deliver services society depends on.

Examples include sectors such as:

- public administration;
- transport;
- finance;
- health;
- digital infrastructure/ICT management;
- water and wastewater;
- space and other critical domains.

Security design for these sectors must include operational continuity and dependency resilience, not only data-loss prevention.

### 2. Public administration is heavily shaped by hacktivist DDoS

Public administration accounted for 32% of targeted organizations, and 82% of the public-administration events were ideology-driven DDoS.

This can distort how sector risk is interpreted. A high event count does not necessarily mean every event involved deep compromise.

For defenders, however, DDoS still matters because availability is the security objective.

Architecture should cover:

- upstream DDoS protection;
- rate limiting;
- CDN/Anycast capacity;
- alternate communications;
- failover;
- service degradation modes;
- crisis communications.

### 3. Cybercrime remains a major operational threat

Cybercrime represented 36% of total events.

Within financially motivated activity, ENISA highlights ransomware, data breaches, and fraud/impersonation.

This aligns with Microsoft and IBM: most organizations are more likely to face economically motivated operations than nation-state espionage.

The difference is that ENISA places this activity in a critical-sector/public-service context, where operational impact can cascade beyond one company.

### 4. State-aligned actors prioritize intrusion

State-nexus sets were reported primarily conducting intrusion operations, with phishing a secondary activity.

For high-value organizations, the relevant design problem is long-term access and intelligence collection.

Useful controls include:

- strong identity;
- long-term logging;
- segmentation;
- asset criticality;
- supplier monitoring;
- threat hunting;
- detection of credential/session abuse.

### 5. Hacktivism follows geopolitical events

ENISA recorded thousands of hacktivist claims, overwhelmingly DDoS, often aligned with elections, protests, international tensions, and support for Ukraine.

This is a reminder that threat likelihood can change because of **external events**, not because of any change in the organization's own technology.

Risk governance therefore benefits from:

- geopolitical intelligence;
- event-based readiness levels;
- pre-planned DDoS capacity increases;
- communications playbooks;
- monitoring of threat-actor claims.

### 6. Vulnerability volume keeps increasing

More than 48,000 CVEs in 2025, up 22%, means raw vulnerability count is becoming less useful as a management metric.

Organizations need prioritization based on:

- exploitability;
- exposure;
- active exploitation;
- business criticality;
- reachability;
- compensating controls.

This aligns with the exposure-management conclusions from DBIR, M-Trends, and IBM.

### 7. AI has a dual role: enabler and new attack surface

ENISA notes increasing malicious use of AI across cybercrime, state-aligned operations, and information manipulation.

AI can support:

- content creation;
- translation;
- synthetic audio/video;
- social engineering;
- scale.

At the same time, enterprise AI systems create new targets and dependencies.

For governance, the key is not to treat AI as a separate universe. It should be incorporated into:

- asset inventory;
- supplier risk;
- identity;
- data governance;
- incident response;
- resilience planning.

### 8. Dependencies are the architectural headline

ENISA's framing emphasizes that cyber dependencies expand the attack surface and weaken resilience.

Dependencies include:

- cloud providers;
- managed services;
- telecommunications;
- SaaS;
- identity providers;
- software suppliers;
- supply chains;
- shared digital infrastructure.

A highly secure service can still fail if a critical dependency becomes unavailable or compromised.

## Enterprise Security Architecture implications

### Resilience

- Model critical-service dependencies.
- Define acceptable degraded-service modes.
- Test dependency failure, not only local system failure.

### Governance / NIS2

- Assign ownership for critical services, risk acceptance, incident reporting, and supplier dependencies.
- Maintain evidence that controls are operating.

### Availability

- Treat DDoS and upstream provider failure as architecture scenarios.
- Ensure alternate communication and operational continuity.

### Exposure Management

- Prioritize the rapidly expanding CVE population using exploitability and business context.

### Threat Intelligence

- Incorporate geopolitical triggers for relevant sectors.
- Adjust monitoring/readiness when external events increase targeting likelihood.

## Recommended actions

1. Build a dependency map for critical business services.
2. Identify NIS2-relevant/critical functions and their supporting identities, platforms, suppliers, and networks.
3. Exercise DDoS, cloud/SaaS outage, and supplier-compromise scenarios.
4. Use exploit-informed vulnerability prioritization instead of vulnerability counts.
5. Retain long-term telemetry for high-value state/espionage targets.
6. Incorporate geopolitical context into threat readiness.
7. Add AI services and suppliers to normal asset and third-party governance.

## ATT&CK relevance

- T1190 — Exploit Public-Facing Application
- T1078 — Valid Accounts
- T1566 — Phishing
- T1498 — Network Denial of Service
- T1486 — Data Encrypted for Impact
- T1195 — Supply Chain Compromise

## Caveats

- ENISA is EU-focused and has a public-policy/critical-sector perspective.
- Event counts include categories such as DDoS claims that differ in technical depth from confirmed data breaches.
- The report should not be compared directly with commercial vendor IR percentages.
- Threat categories and geopolitical attribution require contextual interpretation.

## Primary sources

- https://www.enisa.europa.eu/publications/enisa-threat-landscape-2026
- https://www.enisa.europa.eu/topics/cyber-threats/threat-landscape
- https://www.enisa.europa.eu/news/exploring-the-evolution-of-the-cyber-threat-landscape-how-dependencies-weaken-our-digital-resilience

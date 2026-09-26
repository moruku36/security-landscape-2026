---
publisher: "Verizon"
edition: "2026 Data Breach Investigations Report"
publication_date: "2026-05-18"
observation_period: "2024-11-01 to 2025-10-31"
dataset_or_scope: "31,000+ security incidents; 22,000+ confirmed breaches; organizations in 145 countries"
geography: "Global"
language: "en"
primary_source: "https://www.verizon.com/business/resources/reports/dbir/"
last_verified: "2026-09-27"
---

# Verizon 2026 Data Breach Investigations Report

[日本語版](02-verizon-dbir-2026.ja.md)

## Why this report matters

The Verizon DBIR is the broadest statistical baseline in this repository. The 19th edition analyzes more than **31,000 real-world security incidents**, including more than **22,000 confirmed data breaches** across organizations in **145 countries**. Data is contributed by law enforcement, forensic firms, law firms, cyber insurers, information-sharing groups, Verizon's own VTRAC caseload, and other partners.

That scale makes DBIR useful for understanding **prevalence** across many industries and geographies. It is less suited than M-Trends or Unit 42 for reconstructing the deepest technical details of an individual intrusion, but it is excellent for testing whether a threat observed by one IR provider is showing up broadly across the ecosystem.

## Evidence profile

| Field | Value |
|---|---|
| Edition | 19th DBIR |
| Observation period | Nov 1, 2024-Oct 31, 2025 |
| Population | 31,000+ incidents; 22,000+ confirmed breaches |
| Geography | 145 countries |
| Collection | Multi-contributor, normalized with the VERIS framework |
| Best use | Broad prevalence, industry/region comparisons, breach patterns |
| Main limitation | Contributor mix and regional visibility vary; an "incident" is not the same as a confirmed "breach" |

## Executive summary

The defining DBIR 2026 shift is that **software vulnerability exploitation became the leading breach entry point**, overtaking stolen credentials. At the same time, ransomware remained extremely common, third-party involvement increased sharply, and mobile-origin social engineering outperformed traditional email simulations.

The report also shows that AI is entering both sides of the attack surface. Adversaries are using GenAI across multiple techniques, employees are increasingly using unsanctioned AI tools, and AI-related bot traffic is growing. Yet the central defensive lesson is conventional: organizations need stronger asset inventory, faster remediation, identity controls, third-party governance, and resilience.

## Key findings

| Finding | Observation context |
|---|---|
| More than **31,000** incidents and **22,000** confirmed breaches across **145 countries** | 2026 DBIR dataset |
| Vulnerability exploitation reached **31%** of breaches and became the leading initial-access vector | Confirmed breach population |
| The 31% vulnerability figure represented a **55% increase** from the prior year | Year-over-year |
| **48%** of breaches involved ransomware | Confirmed breaches |
| Threat actors verifiably used GenAI in connection with **15 distinct attack techniques** | DBIR GenAI analysis |
| Mobile-based phishing/simulation entry points produced **40% higher median successful click rates** than email | Phishing simulation analysis |
| Third-party involvement rose **60%** year over year and was present in **48%** of breaches | DBIR third-party analysis |
| Employee use of unapproved "shadow AI" reportedly tripled to **45%** | DBIR AI analysis |
| AI bot traffic grew **21% month over month** in the cited analysis | DBIR AI/bot context |
| Median time to fully resolve a critical vulnerability was **43 days**, almost two weeks longer than the prior year | Vulnerability-remediation analysis |

Primary evidence: [Verizon 2026 DBIR](https://www.verizon.com/business/resources/reports/dbir/) and Verizon's [2026 DBIR announcement](https://www.verizon.com/about/news/breach-industry-wide-dbir-finds).

## Detailed analysis

### 1. Vulnerability exploitation becoming #1 is an architecture problem, not only a patching problem

A 31% breach entry share means the organization cannot treat Internet-facing vulnerability management as a back-office hygiene process.

The more useful prioritization question is not "What has the highest CVSS?" but:

```text
Exploitability
+ Internet exposure
+ Known exploitation
+ Reachable privilege
+ Business criticality
+ Third-party dependency
+ Compensating controls
= Remediation priority
```

The 43-day median time to fully resolve a critical vulnerability reinforces the gap between vulnerability discovery and actual risk reduction.

For enterprise architects, this pushes toward:

- continuous external attack-surface inventory;
- emergency patch paths for Internet-facing services;
- segmentation of management interfaces;
- immutable ownership of every exposed asset;
- compensating controls when remediation cannot be immediate.

### 2. Ransomware remains common even as payment behavior changes

Ransomware appeared in 48% of breaches. Verizon also notes that payouts are shrinking and more organizations refuse payment.

This should not be interpreted as ransomware becoming less consequential. It suggests that **resilience and negotiation economics are changing**, while attackers continue to rely on data theft, operational disruption, and extortion.

The architecture requirement is therefore not simply anti-malware. It is:

- rapid containment;
- segmented privilege;
- protected backups;
- recoverability testing;
- business-continuity planning;
- evidence preservation for extortion/data-theft cases.

### 3. Third-party risk is becoming direct attack-path risk

Third-party involvement increased 60% and was present in 48% of breaches according to Verizon's 2026 summary materials.

This matters because "third-party risk" can no longer live only in procurement questionnaires. The technical relationship itself must be modeled:

```text
Vendor identity
→ SaaS integration
→ API/OAuth permission
→ enterprise data
→ downstream operational dependency
```

Useful controls include:

- an inventory of integrations and external trust;
- least-privilege API/OAuth scopes;
- vendor-specific identities;
- emergency revoke procedures;
- contractual logging and security requirements;
- continuous monitoring of high-impact supplier connections.

### 4. Mobile social engineering changes the human attack surface

The 40% higher median click success for mobile-origin entry points is important because many enterprise awareness programs remain email-centric.

Mobile channels add:

- SMS;
- voice calls;
- messaging apps;
- QR codes;
- MFA fatigue and help-desk interaction;
- smaller screens and reduced context for link inspection.

The control response should combine awareness with technical constraints: phishing-resistant authentication, verified account recovery, conditional access, session/device context, and stronger help-desk processes.

### 5. GenAI appears across the attack lifecycle, but the bigger enterprise risk may be uncontrolled use

DBIR identifies 15 distinct attack techniques where threat actors verifiably researched or used GenAI. Verizon's summary also highlights "shadow AI" growth among employees.

There are two separate risks:

**Offensive acceleration**
- reconnaissance;
- vulnerability research;
- lure generation;
- malware/script assistance;
- translation and personalization.

**Enterprise AI exposure**
- users pasting confidential data into unapproved tools;
- browser extensions or AI apps obtaining broad permissions;
- credentials or tokens stored in AI tooling;
- ungoverned third-party data processing.

The second category is an architecture/governance issue, not merely a threat-intelligence trend.

### 6. DBIR still shows that human and technical risk must be designed together

It would be a mistake to read "vulnerabilities surpassed credentials" as evidence that identity is less important. The same report shows strong mobile social-engineering effectiveness and large third-party involvement.

The correct reading is:

> **The enterprise must defend both unauthenticated technical entry paths and authenticated trust paths.**

That means Exposure Management and Identity Security are complementary, not competing priorities.

## Enterprise Security Architecture implications

### Exposure Management

- Maintain a continuously reconciled inventory of Internet-facing assets.
- Prioritize KEV/active exploitation, public exposure, reachable privilege, and business importance.
- Measure remediation age, not only open vulnerability count.

### Identity Plane

- Require phishing-resistant methods for privileged/high-risk workflows.
- Harden account recovery, help desk, and mobile-origin verification.
- Monitor session and token context, not only password events.

### Supply Chain / SaaS

- Model technical third-party connectivity, not only vendor risk scores.
- Assign an owner and expiration/review cycle to integrations.
- Test emergency revocation.

### AI Governance

- Discover enterprise AI usage.
- Define approved services, data classes, and connector permissions.
- Treat AI SaaS credentials and OAuth grants like other enterprise SaaS identities.

### Recovery

- Test recovery under ransomware and supplier outage scenarios.
- Include identity and cloud/SaaS dependencies in business-continuity exercises.

## Recommended actions

1. Establish an Internet-facing asset SLA tied to exploitability and business criticality.
2. Track critical vulnerability resolution time and exceptions.
3. Treat third-party integrations as architecture objects with owner, permissions, telemetry, and revocation.
4. Expand phishing defense to voice, SMS, messaging apps, and account-recovery workflows.
5. Implement an enterprise AI-service inventory and shadow-AI discovery process.
6. Validate ransomware recovery, including identity and SaaS dependencies.
7. Use DBIR industry/region data for context, but keep enterprise-specific architecture decisions based on your own attack paths.

## ATT&CK relevance

Representative mapping:

- T1190 — Exploit Public-Facing Application
- T1078 — Valid Accounts
- T1566 — Phishing
- T1528 — Steal Application Access Token
- T1486 — Data Encrypted for Impact
- T1490 — Inhibit System Recovery

## Caveats

- DBIR distinguishes "incidents" from confirmed "breaches"; mixing those denominators leads to misleading comparisons.
- Data visibility varies by geography and contributor.
- Regional/industry percentages should not be generalized to every organization.
- DBIR's large population is a strength for prevalence, but it does not provide the same deep forensic detail as a dedicated IR case report.

## Primary sources

- https://www.verizon.com/business/resources/reports/dbir/
- https://www.verizon.com/about/news/breach-industry-wide-dbir-finds
- Japanese DBIR page: https://www.verizon.com/business/ja-jp/resources/reports/dbir/

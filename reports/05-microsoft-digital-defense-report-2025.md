---
publisher: "Microsoft"
edition: "Microsoft Digital Defense Report 2025"
publication_date: "2025-10-16"
observation_period: "Primarily July 2024 to June 2025, with report-specific datasets and later operational examples"
dataset_or_scope: "Microsoft security, identity, cloud, fraud, incident-response, and threat-intelligence telemetry"
geography: "Global"
language: "en"
primary_source: "https://www.microsoft.com/en-us/security/security-insider/threat-landscape/microsoft-digital-defense-report-2025"
last_verified: "2026-09-27"
---

# Microsoft Digital Defense Report 2025

[日本語版](05-microsoft-digital-defense-report-2025.ja.md)

> This is the latest annual Microsoft Digital Defense Report available at the repository snapshot date of 2026-09-26.

## Why this report matters

Microsoft Digital Defense Report (MDDR) is broader than a pure incident-response report. It combines Microsoft's global product and service telemetry, threat intelligence, incident response, identity signals, cloud telemetry, fraud data, and nation-state tracking.

That breadth makes it especially useful for **strategic security architecture**: it connects cybercrime, identity, cloud, AI, nation-state activity, business resilience, fraud, and secure-by-default engineering.

Microsoft's scale is itself part of the evidence context. The company states that it processes around **100 trillion security signals per day**, blocks approximately **4.5 million net-new malware files per day**, analyzes about **38 million identity-risk detections on an average day**, and works with more than **15,000 security ecosystem partners**.

## Evidence profile

| Field | Value |
|---|---|
| Core reporting period | Primarily Jul 2024-Jun 2025 |
| Telemetry scale | 100T security signals/day; 38M identity-risk detections/day |
| Sources | Microsoft security products/services, IR, Digital Crimes Unit, Threat Intelligence, cloud/fraud telemetry |
| Geography | Global |
| Best use | Strategic trends, identity/cloud/AI, cybercrime ecosystem, resilience |
| Main limitation | Multiple datasets with different denominators and time windows |

## Executive summary

MDDR 2025 argues that cybersecurity is now a problem of **speed, scale, resilience, and trust**.

Most investigated attacks with known motivation were financially driven rather than espionage. Attackers used familiar entry paths—phishing/social engineering, unpatched web assets, exposed remote services—but combined them with faster exploitation, infostealers, cybercrime-as-a-service, identity abuse, cloud attacks, and AI.

The report also treats AI as a three-sided issue:

- a tool for attackers;
- a defensive automation capability;
- a new attack surface that includes models, applications, agents, data, and prompts.

For enterprise architecture, the most important Microsoft theme is that **identity and cloud resilience must be designed together**. A compromised human or workload identity can become a cloud control-plane compromise, while destructive cloud campaigns can directly affect business continuity.

## Key findings

| Finding | Observation context |
|---|---|
| Microsoft processes about **100 trillion security signals per day** | Global Microsoft security ecosystem |
| About **4.5 million net-new malware files** are blocked daily | Microsoft telemetry |
| About **38 million identity-risk detections** are analyzed on an average day | Microsoft identity telemetry |
| Only **4%** of investigated incidents with known motivation were espionage-driven | Microsoft Incident Response |
| Data theft was observed in **37%** of attacks with identified motivations | Microsoft IR |
| **33%** had an extortion component | Microsoft IR |
| Ransomware or destructive activity appeared in **19%** | Microsoft IR |
| **28%** of breaches started with phishing/social engineering | Microsoft IR initial access |
| **18%** started through unpatched web assets | Microsoft IR |
| **12%** used exposed remote services | Microsoft IR |
| **97%** of identity attacks in the cited data were password-spray attacks | Identity-threat analysis |
| Disruptive/destructive cloud campaigns increased **87%** between compared 100-day periods in 2025 | Defender for Cloud telemetry |
| Overall observed cloud incident volume increased **26%** between those periods | Azure/Defender for Cloud telemetry |
| AI-driven phishing was reported as **3x more effective** than traditional campaigns | MDDR summary |
| More than **40%** of ransomware attacks had a hybrid component | MDDR summary |
| AI-driven identity forgeries increased **195% globally** | Fraud/synthetic-identity analysis |
| Microsoft says it thwarted **$4B** in fraud attempts and blocked **1.6M bot/fake account sign-ups per hour** | Microsoft fraud-defense data |

Primary evidence: [Microsoft Digital Defense Report 2025](https://www.microsoft.com/en-us/security/security-insider/threat-landscape/microsoft-digital-defense-report-2025).

## Detailed analysis

### 1. Most attacks are economically motivated—but nation-state risk remains structurally important

Only 4% of incidents with known motivation were espionage-only, while data theft, extortion, and ransomware/destructive activity were much more common.

For enterprise planning, this means the baseline architecture should primarily assume:

- credential theft;
- extortion;
- data theft;
- ransomware/destructive operations;
- monetization of access.

Nation-state defense still matters, especially for government, research, critical infrastructure, technology, and communications sectors, but the everyday threat model should not be designed as though every attacker is a sophisticated intelligence service.

### 2. Initial access still comes from familiar weaknesses

Microsoft IR observed:

- 28% phishing/social engineering;
- 18% unpatched web assets;
- 12% exposed remote services.

This aligns with other 2026 reports. The architecture lesson is not "buy a new category of security product." It is that **basic exposure, identity, and remote-access controls remain decisive**.

ClickFix, device-code phishing, and other interactive techniques show that authentication workflows themselves are now attack surfaces.

### 3. Identity attacks are still dominated by simple techniques

The report notes that 97% of observed identity attacks in the cited analysis were password-spray attacks.

This is strategically important because it demonstrates a recurring industry pattern: sophisticated platforms can still be compromised through weak, reused, or overexposed credentials.

A modern identity program should therefore combine:

- passwordless/phishing-resistant authentication;
- legacy authentication reduction;
- Conditional Access/context evaluation;
- anomalous sign-in detection;
- dormant identity removal;
- password spray and credential-stuffing defenses;
- session/token monitoring.

### 4. Workload identities are the next identity horizon

Microsoft explicitly highlights a shift from end-user identities toward **workload identities**: applications, services, scripts, automation, and cloud workloads.

These identities can have high privilege but weaker lifecycle controls.

Important risk patterns include:

- app-consent phishing;
- malicious OAuth grants;
- device-code phishing;
- secrets exposed through applications;
- Key Vault/secret-store pivoting;
- long-lived service-principal credentials.

This is directly relevant to cloud architecture, CI/CD, SaaS integrations, and AI agents.

### 5. Cloud attacks are increasingly destructive

Microsoft Defender for Cloud telemetry showed a 26% increase in observed cloud incidents between the first and second 100-day periods of 2025, with an 87% rise in disruptive/destructive campaigns including ransomware, mass deletion, and other destructive actions.

This moves cloud security beyond "misconfiguration prevention."

The control plane needs:

- strong organization/tenant guardrails;
- JIT privilege;
- protected break-glass access;
- workload identity governance;
- central audit;
- deletion protection and immutable recovery;
- cross-account/subscription/project recovery planning.

### 6. Cybercrime is an industrial ecosystem

Microsoft describes a cybercrime economy with:

- access brokers;
- ransomware operators;
- data-extortion groups;
- infostealers;
- commodity malware;
- fraud ecosystems.

Lumma Stealer is highlighted as a prevalent infostealer, and Microsoft's Digital Crimes Unit worked with international law enforcement to disrupt its infrastructure.

For architecture, the important point is that a low-severity infostealer event can become an enterprise-access event when stolen browser credentials, tokens, cookies, or passwords are resold.

### 7. AI expands both offensive and defensive capability

Microsoft frames AI as "a tool, threat, and vulnerability."

Offensive uses include:

- more convincing phishing;
- synthetic identity/fraud;
- deepfake voice/video;
- malware assistance;
- scalable social engineering.

Defensive uses include:

- faster triage;
- fraud detection;
- phishing detection;
- automated account suspension;
- AI-agent response.

Microsoft also warns about AI-specific attack surfaces:

- adversarial prompts;
- data poisoning;
- model manipulation;
- AI applications and agents;
- sensitive data exposure.

The architectural implication is that AI adoption should be governed through the same security planes as any other privileged software system.

### 8. Resilience is part of cyber defense, not a separate continuity discipline

Microsoft's "assume breach" framing and the rise in destructive cloud campaigns make business continuity part of security architecture.

A resilient design should answer:

- Can trusted administration be restored after identity compromise?
- Can cloud resources be recovered after mass deletion?
- Are recovery credentials independent?
- Are critical SaaS/cloud dependencies represented in BCP/DR?
- Can the organization operate when primary identity or collaboration services are unavailable?

## Enterprise Security Architecture implications

### Identity Plane

- Move toward phishing-resistant/passwordless authentication.
- Include workload/service identities in the same governance model as human identities.
- Review OAuth consent, device-code flows, application credentials, and secret access.

### Cloud Control Plane

- Protect tenant/org root authority.
- Enforce secure-by-default policy and least privilege.
- Monitor high-impact changes and deletion operations.

### AI Security

- Maintain an inventory of AI applications, models, agents, and connectors.
- Protect data flows and agent/tool permissions.
- Treat AI agents as non-human identities with auditable authority.

### Recovery

- Design for destructive cloud events and identity loss.
- Separate production and recovery trust where possible.

### Governance

- Treat cybersecurity as a business-resilience and trust problem, not only an IT control problem.
- Align security, cloud, identity, legal, fraud, risk, and continuity teams.

## Recommended actions

1. Eliminate weak/legacy authentication for privileged workflows.
2. Inventory workload identities, service principals, and application grants.
3. Implement JIT/PIM for cloud and identity administration.
4. Monitor cloud deletion, role change, secret access, and mass-resource operations.
5. Build a formal AI security framework covering discovery, data, apps, agents, models, and governance.
6. Design recovery for tenant/identity/control-plane loss, not only workload failure.
7. Use automated response for high-confidence events, but keep destructive actions behind strong policy/human gates.
8. Integrate cyber resilience with business-continuity governance.

## ATT&CK relevance

- T1078 — Valid Accounts
- T1110.003 — Password Spraying
- T1528 — Steal Application Access Token
- T1550 — Use Alternate Authentication Material
- T1098 — Account Manipulation
- T1190 — Exploit Public-Facing Application
- T1566 — Phishing
- T1490 — Inhibit System Recovery

## Caveats

- MDDR combines multiple datasets with different scopes; percentages should not be treated as if they all share one denominator.
- The report is Microsoft-centric by visibility, even though many conclusions are multi-cloud and provider-neutral.
- This edition predates several 2026 annual reports in the repository, but it remained Microsoft's latest annual edition at the snapshot date.

## Primary sources

- https://www.microsoft.com/en-us/security/security-insider/threat-landscape/microsoft-digital-defense-report-2025
- https://www.microsoft.com/en-us/corporate-responsibility/cybersecurity/microsoft-digital-defense-report-2025/
- https://blogs.microsoft.com/on-the-issues/2025/10/16/mddr-2025/

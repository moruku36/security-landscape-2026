---
publisher: "Google Cloud / Mandiant"
edition: "M-Trends 2026"
publication_date: "2026-03-23"
observation_period: "2025-01-01 to 2025-12-31"
dataset_or_scope: "500,000+ hours of Mandiant frontline incident investigations"
geography: "Global"
language: "en"
primary_source: "https://cloud.google.com/security/resources/m-trends-executive-edition"
last_verified: "2026-09-27"
---

# Mandiant M-Trends 2026

[日本語版](01-m-trends-2026.ja.md)

## Why this report matters

M-Trends is one of the strongest sources in this repository for understanding **what attackers actually did inside breached enterprises**. It is based on more than 500,000 hours of Mandiant frontline investigations conducted during 2025, so its value is different from a broad survey or product-telemetry report: it provides a detailed incident-response view of initial access, attacker dwell time, recovery disruption, infrastructure persistence, and investigative blind spots.

The most important message is not simply that attacks are becoming faster. Mandiant observed a **split in attacker operating models**:

- financially motivated groups are optimizing for rapid hand-off, extortion, and deliberate recovery denial;
- espionage groups and North Korean IT-worker operations are optimizing for long-term persistence, often in places where EDR has little or no visibility.

That combination creates two very different defensive requirements: **machine-speed containment for fast attacks** and **long-retention, infrastructure-level telemetry for stealthy persistence**.

## Evidence profile

| Field | Value |
|---|---|
| Observation period | Jan 1-Dec 31, 2025 |
| Population | Mandiant Consulting targeted-attack investigations |
| Scale | 500,000+ frontline investigation hours |
| Geography | Global |
| Best use | Incident-response patterns, attacker tradecraft, dwell time, infrastructure blind spots |
| Main limitation | Organizations that engage Mandiant are not a random sample of all enterprises |

## Executive summary

M-Trends 2026 describes an environment where endpoint-centric security is no longer enough. Exploitation of vulnerabilities remained the leading initial infection vector for the sixth year in a row, while voice phishing sharply increased. At the same time, attackers increasingly operated through edge appliances, virtualization infrastructure, SaaS tokens, identity services, and legitimate administrative functionality that can sit outside traditional endpoint controls.

The report also reframes ransomware as a **resilience problem**. Modern operators do not merely encrypt files. They target identity infrastructure, hypervisor management, cloud backup objects, recovery catalogs, and administrative pathways in order to prevent restoration. This makes backup architecture, privileged identity, virtualization, and recovery administration part of the same Tier-0 design problem.

AI is important, but Mandiant is explicit that the majority of successful 2025 intrusions were still enabled by familiar weaknesses. AI primarily reduced attacker friction in reconnaissance, social engineering, malware development, and post-compromise activity.

## Key findings

| Finding | Observation context |
|---|---|
| Exploits accounted for **32%** of initial infections, remaining #1 for the sixth consecutive year | 2025 investigations |
| Voice phishing rose to **11%**, the second-most observed vector | 2025 investigations |
| Email phishing declined from 14% in 2024 to **6%** in 2025 | 2025 investigations |
| In ransomware-related incidents, **prior compromise** was the most common initial infection vector at **30%** | Ransomware subset |
| Global median dwell time rose from 11 to **14 days** | 2024 vs 2025 |
| Cyber-espionage and DPRK IT-worker cases each had a median dwell time of **122 days** | 2025 investigations |
| Median time from initial access to secondary-group hand-off fell to **22 seconds**, from more than eight hours in 2022 | Cybercrime hand-off cases |
| BRICKSTORM-related investigations averaged **393 days** of dwell time | Relevant Mandiant cases |
| Organizations first detected malicious activity internally in **52%** of investigations, up from 43% | 2025 vs 2024 |
| High tech became the most frequently targeted industry at **17%**, ahead of finance at **14.6%** | 2025 investigations |
| Financially motivated clusters represented **41%** of observed clusters; espionage clusters rose to **16%** | 2025 clusters |
| Observed malware families: backdoors **36%**, downloaders 11%, ransomware 10%, droppers 10%, credential stealers 9% | 2025 malware observations |

Primary evidence: [M-Trends 2026 Executive Edition](https://cloud.google.com/security/resources/m-trends-executive-edition) and [M-Trends 2026 blog](https://cloud.google.com/blog/topics/threat-intelligence/m-trends-2026).

## Detailed analysis

### 1. Initial access is shifting from inbox-only defense to exposure + interactive identity defense

The most important initial-access finding is the coexistence of two patterns.

First, exploitation remains dominant. Public-facing systems, network appliances, and edge infrastructure continue to be attractive because successful exploitation can bypass human interaction entirely. This supports aggressive inventory and patch governance for Internet-facing assets rather than relying on periodic vulnerability-management queues.

Second, **voice phishing** became the second-most observed vector. This matters because interactive social engineering is harder to stop with email controls. An attacker can call an employee or help desk, manipulate MFA reset or account recovery processes, and then enter the environment using legitimate identity paths.

The architectural lesson is that "phishing-resistant MFA" is necessary but incomplete. Organizations also need:

- hardened help-desk and account-recovery workflows;
- identity proofing for high-impact resets;
- controls around new authentication methods and device registration;
- visibility into session and token issuance after a social-engineering event.

### 2. The 22-second hand-off changes alert prioritization

Mandiant observed a median of only 22 seconds between initial access and hand-off to a secondary threat group. This indicates tighter coordination between initial-access specialists and follow-on operators.

The practical consequence is that a detection that looks low impact—malvertising, fake browser update, commodity downloader, or a single infected workstation—may be the start of a pre-arranged ransomware or extortion operation.

Traditional SOC severity models often score the first event based on what has already happened. M-Trends suggests that teams should also ask:

> **What high-impact actor or capability can this foothold become connected to next?**

That favors rapid isolation of high-confidence initial-access events, even before hands-on-keyboard activity is visible.

### 3. Ransomware has become Recovery Denial

The report's strongest architecture message is the transition from encryption to **recovery denial**.

Attackers were observed targeting:

- identity services and certificate infrastructure;
- virtualization management planes;
- backup systems and backup catalogs;
- cloud backup objects and recovery points;
- hypervisor datastores;
- emergency / break-glass administrative paths.

This creates a failure mode where production, identity, virtualization, and backup all share the same compromised trust boundary.

A backup is therefore not a resilience control if the same production administrator—or the same compromised IdP—can destroy it.

### 4. Hypervisors are now Tier-0 security assets

Mandiant emphasizes virtualization because hypervisors operate below guest operating systems and frequently cannot run standard EDR.

An attacker with hypervisor-level access may be able to:

- clone virtual disks and extract sensitive data without logging into the guest;
- retrieve directory databases or secrets from offline disk images;
- create rogue virtual machines;
- deploy persistence in hypervisor shells;
- encrypt datastores and disable many servers at once.

This is a structural blind spot. Hypervisor management should therefore be treated like a domain controller or cloud organization root: isolated administration, phishing-resistant privileged access, dedicated telemetry, and minimal dependence on ordinary corporate identity.

### 5. Edge and network devices can host an almost endpoint-free attack lifecycle

Network appliances, firewalls, VPNs, routers, and similar systems are valuable precisely because host-based security tooling is often unavailable.

Mandiant describes attackers using native device functionality, administrative subshells, packet capture, and lightweight/in-memory malware. In some cases, significant reconnaissance and collection can occur without ever moving to a normal workstation or server.

That means the SOC needs:

- administrative/configuration logs from network infrastructure;
- centralized forwarding before attackers can clear local logs;
- vulnerability ownership for appliances;
- network-device-specific IR playbooks;
- sufficiently long log retention to support investigations.

Mandiant specifically recommends retaining administrative logs long enough to investigate long-term intrusions; its examples make standard 90-day retention clearly inadequate.

### 6. SaaS integrations and tokens create a cascading supply-chain path

The cloud-first enterprise introduces a different form of third-party risk. Attackers can compromise a SaaS provider or integration, obtain long-lived OAuth tokens, personal access tokens, API keys, or session cookies, and then pivot into downstream customer environments.

This can bypass password resets and MFA because the attacker is reusing already-authorized material.

The defensive model therefore needs:

- SaaS and OAuth application inventory;
- owner and business-purpose metadata for integrations;
- end-user app-consent restrictions;
- short-lived tokens where possible;
- rapid integration revocation;
- audit visibility into third-party application access.

### 7. AI is an accelerator and is also being weaponized inside compromised environments

Mandiant saw attackers using AI for reconnaissance, social engineering, and malware development. A particularly important example is **QUIETVAULT**, a credential stealer observed checking compromised systems for local AI CLI tools and using predefined prompts to locate configuration files and tokens such as GitHub and NPM credentials.

This is a useful enterprise lesson: local AI tooling is not merely a productivity application. If it can read code, environment variables, repositories, or developer credentials, it belongs in the endpoint/developer threat model.

## Enterprise Security Architecture implications

### Identity Plane

- Protect password reset, MFA reset, and account recovery as privileged workflows.
- Continuously review SaaS grants, service principals, remote contractors, and non-human identities.
- Treat session/token theft as a first-class incident, not just password compromise.

### Control Plane

- Classify hypervisor, backup, edge-management, and cloud organization roots as Tier-0-equivalent.
- Separate infrastructure administration from normal corporate administration.
- Reduce standing privilege and use JIT/PIM where practical.

### Recovery Plane

- Separate production authority from recovery authority.
- Maintain immutable/offline recovery copies.
- Test recovery after loss of the primary IdP, virtualization layer, and production admin plane—not only after a server failure.

### Telemetry Plane

- Centralize logs from IdP, SaaS, edge, hypervisor, backup, and cloud control planes.
- Retain high-value administrative telemetry well beyond standard endpoint retention.
- Alert when a previously reliable log source unexpectedly stops reporting.

### SecOps

- Correlate low-impact initial-access signals with identity, cloud, network, and SaaS context.
- Pre-authorize reversible containment for high-confidence initial-access cases.
- Threat hunt for legitimate administrative behavior being used from abnormal contexts.

## Recommended actions

1. Build a complete Internet-facing and edge-device inventory with clear patch ownership.
2. Harden help-desk identity verification and high-impact MFA/account recovery.
3. Isolate hypervisor and backup administration from ordinary corporate identity where feasible.
4. Centralize and extend retention of network, identity, virtualization, SaaS, and backup audit logs.
5. Inventory OAuth apps, API keys, service principals, and SaaS integrations.
6. Design recovery exercises around total identity/control-plane compromise.
7. Treat local developer AI tools as part of the developer credential and secret threat model.
8. Update SOC severity models so low-impact initial access can trigger high-priority containment.

## ATT&CK relevance

Representative repository mapping:

- T1190 — Exploit Public-Facing Application
- T1078 — Valid Accounts
- T1528 — Steal Application Access Token
- T1550 — Use Alternate Authentication Material
- T1098 — Account Manipulation
- T1490 — Inhibit System Recovery
- T1486 — Data Encrypted for Impact

See [MITRE ATT&CK crosswalk](../frameworks/mitre-attack.md).

## Caveats

- Mandiant engagements skew toward organizations that required specialist incident response.
- Percentages should not be compared directly with DBIR, CrowdStrike, or Unit 42 because the populations differ.
- Some infrastructure and persistence findings come from notable incident clusters; they show what is possible and operationally important, not necessarily prevalence across every enterprise.

## Primary sources

- https://cloud.google.com/security/resources/m-trends-executive-edition
- https://cloud.google.com/blog/topics/threat-intelligence/m-trends-2026
- Japanese overview: https://cloud.google.com/blog/ja/topics/threat-intelligence/m-trends-2026?hl=ja

---
publisher: "IBM X-Force"
edition: "X-Force Threat Intelligence Index 2026"
publication_date: "2026-02-25"
observation_period: "2025 incident-response, investigation, vulnerability, dark-web, and threat-intelligence observations"
dataset_or_scope: "IBM X-Force global threat intelligence and incident observations"
geography: "Global"
language: "en"
primary_source: "https://www.ibm.com/reports/threat-intelligence"
last_verified: "2026-09-27"
---

# IBM X-Force Threat Intelligence Index 2026

[日本語版](06-ibm-xforce-2026.ja.md)

## Why this report matters

IBM X-Force provides a useful bridge between **incident response, vulnerability exploitation, dark-web credential ecosystems, ransomware, supply-chain risk, and AI security**.

Its 2026 message is unusually consistent with M-Trends and DBIR: AI is accelerating attacks, but the most consequential failures still come from basic security gaps—public exposure, weak identity controls, misconfiguration, credential theft, and excessive trust.

## Evidence profile

| Field | Value |
|---|---|
| Observation period | 2025 |
| Sources | X-Force IR/investigations, threat intelligence, vulnerability and dark-web observations |
| Geography | Global |
| Best use | Exploitation trends, identity risk, supply chain, ransomware fragmentation, AI credential ecosystem |
| Main limitation | IBM visibility is vendor-specific and different metrics use different source populations |

## Executive summary

X-Force saw **exploitation of public-facing applications become the leading initial access vector**, with a 44% year-over-year increase. Vulnerability risk is amplified by the fact that 56% of disclosed vulnerabilities in IBM's cited analysis did not require authentication for successful exploitation.

At the same time, AI services have become ordinary enterprise SaaS from an attacker's perspective. X-Force observed more than 300,000 ChatGPT credential sets advertised for sale, mostly associated with infostealer ecosystems. This turns AI accounts, chat history, connected data, and reused credentials into a conventional identity-security problem.

The report also highlights growing supply-chain compromise and fragmentation in the ransomware/extortion ecosystem.

## Key findings

| Finding | Observation context |
|---|---|
| Exploitation of public-facing software/system applications increased **44% YoY** | 2025 X-Force observations |
| Vulnerability exploitation accounted for **40%** of incidents observed by X-Force | 2025 incident observations |
| **56%** of disclosed vulnerabilities in the cited analysis did not require authentication for successful exploitation | Vulnerability analysis |
| More than **300,000 ChatGPT credential sets** were advertised on the dark web | 2025 credential observations |
| Active ransomware/extortion groups increased **49%** year over year | 2025 |
| X-Force identified **109 distinct extortion groups**, up from 73 in 2024 | Ransomware/extortion ecosystem |
| Publicly disclosed ransomware/extortion victim counts rose about **12%** | 2025 |
| The share of activity attributed to the top 10 groups dropped **25%**, indicating fragmentation | Ecosystem concentration |
| Major supply-chain incidents increased **nearly fourfold** over five years | Multi-year trend |
| Manufacturing remained the most targeted industry, followed by financial services/insurance | 2025 |
| North America accounted for nearly **one-third** of observed activity | 2025 geographic distribution |

Primary evidence: [IBM X-Force Threat Intelligence Index 2026](https://www.ibm.com/reports/threat-intelligence) and [IBM analysis](https://www.ibm.com/think/x-force/threat-intelligence-index-2026-securing-identities-ai-detection-risk-management).

## Detailed analysis

### 1. Public-facing exploitation is a foundational control failure amplified by AI

IBM's 44% increase in public-facing exploitation and 40% incident share reinforces the shift seen in DBIR.

Attackers benefit from:

- large Internet-facing inventories;
- slow patching;
- unauthenticated vulnerabilities;
- configuration drift;
- forgotten applications;
- exposed management interfaces.

AI does not create this exposure. It can make discovery, prioritization, and exploit adaptation faster.

This argues for continuous attack-surface management tied directly to vulnerability ownership.

### 2. Unauthenticated vulnerabilities deserve special priority

The 56% figure is significant because an unauthenticated exploit can remove the need for stolen credentials.

A risk model should explicitly increase priority when a flaw is:

- Internet accessible;
- unauthenticated;
- known exploited;
- reachable to a high-privilege management plane;
- present in an edge/network device;
- difficult to monitor with EDR.

This is more useful than raw CVSS ranking.

### 3. AI accounts have become ordinary high-value credentials

More than 300,000 ChatGPT credential sets advertised for sale illustrates how quickly AI services have joined the credential-stealing economy.

Potential impact extends beyond account takeover:

- chat history may contain business context;
- users may paste source code or secrets;
- enterprise AI tools may be connected to files or SaaS;
- credentials may be reused elsewhere;
- connected plugins/connectors may provide downstream access.

Organizations should therefore include AI accounts in:

- SSO/federation;
- credential monitoring;
- offboarding;
- session controls;
- data-classification policy;
- SaaS discovery.

### 4. Identity security must include human and non-human identities

IBM explicitly recommends monitoring both human and machine identities.

Non-human identity scope includes:

- service accounts;
- application identities;
- automation;
- API credentials;
- CI/CD identities;
- cloud workload identities;
- AI agents.

A useful governance model is:

```text
identity
+ owner
+ purpose
+ credential type
+ privilege
+ target resources
+ last use
+ expiry
+ revocation path
```

### 5. Supply-chain compromise is about trusted execution and connectivity

Major supply-chain incidents have nearly quadrupled over five years according to IBM.

Modern supply-chain paths include:

- compromised developer identities;
- CI/CD platforms;
- malicious or compromised dependencies;
- SaaS integrations;
- downstream trust relationships.

This means SBOM and SCA are necessary but insufficient. Security architecture must also cover release authority, identity federation, secrets, provenance, and trusted SaaS connectivity.

### 6. Ransomware is fragmenting

X-Force identified 109 extortion groups in 2025, up from 73, while the dominance of the top 10 groups declined.

Fragmentation can create:

- lower barriers to entry;
- more opportunistic affiliates;
- inconsistent sophistication;
- rapidly changing infrastructure and branding.

Defenders should therefore avoid overfitting controls to a short list of famous ransomware brands. Detection should focus on behavior: identity abuse, privilege escalation, staging, backup manipulation, exfiltration, and impact.

### 7. AI defense is useful only when foundations are strong

IBM recommends autonomous/agentic SOC capabilities, AI-enhanced identity detection, vulnerability testing, and AI platform security.

The report's own data supports a sequencing principle:

> **Do not automate around unresolved asset, identity, and logging gaps.**

AI can accelerate a mature operating model, but it does not fix absent inventory, weak ownership, or missing telemetry.

## Enterprise Security Architecture implications

### Exposure

- Treat unauthenticated Internet-facing vulnerabilities as an explicit priority class.
- Map applications to owners and business services.

### Identity

- Extend identity governance to AI accounts and non-human identities.
- Reduce credential reuse and static secrets.

### DevSecOps / Supply Chain

- Protect developer identities and CI/CD authority.
- Use short-lived federation and signed/provenanced releases.
- Inventory SaaS and build-system trust relationships.

### AI Security

- Bring AI platforms into SSO, monitoring, data policy, and SaaS governance.
- Detect credential leakage associated with AI services.

### SecOps

- Use AI/automation to enrich and contain, but first establish reliable telemetry and asset identity.

## Recommended actions

1. Create a special remediation lane for unauthenticated Internet-facing vulnerabilities.
2. Inventory AI accounts/services and integrate approved platforms with enterprise identity.
3. Hunt for stolen enterprise and AI credentials in external exposure sources.
4. Move CI/CD and workload access from static keys toward federation.
5. Build a supply-chain trust graph including developer, pipeline, package, SaaS, and vendor relationships.
6. Detect ransomware behavior rather than relying on actor names/signatures.
7. Use agentic SOC capabilities only with strong audit, authorization, and rollback.

## ATT&CK relevance

- T1190 — Exploit Public-Facing Application
- T1078 — Valid Accounts
- T1555 / credential-store techniques — Credentials from Password Stores
- T1528 — Steal Application Access Token
- T1550 — Use Alternate Authentication Material
- T1195 — Supply Chain Compromise
- T1486 — Data Encrypted for Impact

## Caveats

- Different X-Force metrics come from different datasets; do not assume one denominator.
- Dark-web credential counts indicate exposure/availability, not confirmed enterprise compromise.
- Industry/geographic distributions reflect IBM's visibility.
- Product recommendations should be separated from the underlying threat observations.

## Primary sources

- https://www.ibm.com/reports/threat-intelligence
- https://www.ibm.com/think/x-force/threat-intelligence-index-2026-securing-identities-ai-detection-risk-management
- https://newsroom.ibm.com/2026-02-25-ibm-2026-x-force-threat-index-ai-driven-attacks-are-escalating-as-basic-security-gaps-leave-enterprises-exposed
- Japanese page: https://www.ibm.com/jp-ja/reports/threat-intelligence

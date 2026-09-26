---
publisher: "CrowdStrike"
edition: "2026 Global Threat Report"
publication_date: "2026-02-24"
observation_period: "2025"
dataset_or_scope: "CrowdStrike Counter Adversary Operations threat intelligence and telemetry; 280+ named adversaries tracked"
geography: "Global"
language: "en"
primary_source: "https://www.crowdstrike.com/en-us/global-threat-report/"
last_verified: "2026-09-27"
---

# CrowdStrike 2026 Global Threat Report

[日本語版](03-crowdstrike-global-threat-report-2026.ja.md)

## Why this report matters

CrowdStrike's Global Threat Report is strongly **adversary-centric**. It is useful for understanding attacker tradecraft, breakout speed, malware-free operations, state/eCrime behavior, cross-domain movement, edge targeting, and cloud-aware intrusions.

The 2026 edition's central argument is that attackers are increasingly **logging in, moving across trusted domains, and using legitimate tools**, while AI accelerates their work and also becomes a new attack surface.

## Evidence profile

| Field | Value |
|---|---|
| Observation period | 2025 |
| Source | CrowdStrike Counter Adversary Operations intelligence and telemetry |
| Adversary tracking | 280+ named adversaries |
| Geography | Global |
| Best use | Threat actor behavior, breakout speed, malware-free/cross-domain tradecraft |
| Main limitation | Vendor telemetry and intelligence visibility are not a random sample of all organizations |

## Executive summary

Three themes dominate.

First, **speed**: average eCrime breakout time fell to 29 minutes and the fastest observed case was 27 seconds. That leaves little room for a workflow where detections wait in a queue for manual enrichment.

Second, **identity and trusted infrastructure**: 82% of 2025 detections were malware-free, and CrowdStrike describes attackers moving through trusted identities, SaaS, cloud, supply chains, and edge infrastructure.

Third, **AI has a dual role**. AI-enabled adversary activity rose 89%, while attackers also targeted and abused legitimate AI platforms. This means AI must be treated both as a threat-actor productivity tool and as an enterprise control/data plane that needs its own identity, vulnerability, and monitoring controls.

## Key findings

| Finding | Observation context |
|---|---|
| Fastest observed eCrime breakout time: **27 seconds** | 2025 |
| Average eCrime breakout time: **29 minutes** | 2025 |
| Average breakout speed improved for attackers by **65%** vs 2024 | 2025 vs 2024 |
| AI-enabled adversary activity increased **89%** year over year | 2025 |
| **82%** of detections were malware-free | 2025 detections |
| Exploitation of zero-days before public disclosure increased **42%** | 2025 |
| **40%** of vulnerabilities exploited by China-nexus actors targeted edge devices | 2025 |
| Cloud-conscious intrusions by state-nexus actors increased **266%** | 2025 |
| Legitimate AI tools were abused at **90+ organizations** | CrowdStrike intelligence |
| ChatGPT was mentioned in criminal forums **550% more** than any other model in CrowdStrike's cited analysis | Underground ecosystem signal |
| The report highlights a record **$1.46B cryptocurrency heist** | 2025 threat activity |

Primary evidence: [CrowdStrike Global Threat Report](https://www.crowdstrike.com/en-us/global-threat-report/) and [2026 press release](https://www.crowdstrike.com/en-us/press-releases/2026-crowdstrike-global-threat-report/).

## Detailed analysis

### 1. Breakout time is now an architectural constraint

"Breakout time" measures how long an attacker takes to move from an initially compromised system to another system.

A 29-minute average and 27-second fastest observation mean defenders cannot depend on:

```text
alert
→ queue
→ analyst opens ticket
→ manual enrichment
→ manager approval
→ containment
```

for every high-confidence scenario.

A mature design should support:

- automatic enrichment;
- identity/cloud/endpoint correlation;
- confidence scoring;
- reversible containment;
- pre-authorized actions for narrowly defined cases;
- human approval for destructive or business-critical actions.

### 2. Malware-free operations make identity and behavior more important than file detection

CrowdStrike reports 82% of detections as malware-free. This fits a broader industry pattern: attackers can use valid accounts, built-in tools, SaaS sessions, cloud APIs, remote-management tools, and legitimate administrative interfaces.

Detection therefore needs to focus on:

- who/what is acting;
- where the session originated;
- which resources are being accessed;
- whether the privilege and behavior are normal for that identity;
- whether actions cross endpoint/cloud/SaaS boundaries.

The key question is no longer simply "Is this executable malicious?"

It is:

> **Is this legitimate authority being used legitimately?**

### 3. Edge targeting exposes the limits of endpoint-only defense

Forty percent of vulnerabilities exploited by China-nexus actors targeted edge devices in the cited dataset.

Edge devices are attractive because they often:

- face the Internet;
- have high network visibility;
- cannot run normal EDR;
- are operationally difficult to patch;
- have sparse local logs;
- expose administrative services.

For enterprise architecture, network infrastructure must be included in:

- asset inventory;
- vulnerability governance;
- privileged-access design;
- SIEM logging;
- configuration monitoring;
- incident-response exercises.

### 4. Cloud-conscious intrusion growth shows that cloud is not a separate attack domain

State-nexus cloud-conscious intrusions increased 266%. "Cloud-conscious" is important language: adversaries increasingly understand the cloud control plane and use cloud-native mechanisms, rather than simply attacking a VM that happens to run in a cloud provider.

Typical architectural risk paths include:

```text
stolen identity
→ SaaS session
→ cloud role
→ secret store
→ workload identity
→ data / infrastructure
```

Defenders need cross-domain telemetry and should model cloud IAM, API calls, federation, workload identity, and SaaS as one trust graph.

### 5. Zero-day and pre-disclosure exploitation compress patch decision time

A 42% rise in zero-days exploited before public disclosure emphasizes that "patch after advisory publication" cannot be the only control.

Organizations also need:

- attack-surface reduction;
- segmentation;
- behavior/anomaly detection;
- management-plane restrictions;
- exploit mitigation;
- emergency isolation;
- asset ownership.

This is especially critical for edge devices where exploitation can precede vendor remediation.

### 6. AI is both an accelerator and a target

CrowdStrike observed:

- 89% growth in AI-enabled adversary activity;
- legitimate GenAI tools abused in 90+ organizations;
- malicious prompt use for command generation and credential/cryptocurrency theft;
- exploitation of AI development platforms;
- malicious AI servers impersonating trusted services.

That creates two security programs that should meet in the middle:

**AI-assisted threat activity**
- reconnaissance;
- credential theft;
- social engineering;
- evasion;
- scripting.

**AI platform security**
- agent/tool identity;
- model/application vulnerability management;
- data and secret handling;
- trusted connector/server inventory;
- prompt/tool telemetry.

## Enterprise Security Architecture implications

### Identity Plane

- Treat identity behavior and session context as primary detection signals.
- Protect human and non-human identities consistently.
- Correlate endpoint identity with SaaS and cloud identity.

### Control Plane

- Monitor cloud role changes, federation, secrets, and organization-level policy.
- Treat edge/network management as privileged infrastructure.

### Telemetry Plane

- Join endpoint/XDR, IdP, SaaS, cloud audit, and edge telemetry.
- Design for seconds-to-minutes containment where confidence is high.

### AI Security

- Inventory AI tools and development platforms.
- Apply normal software supply-chain, identity, secret, and vulnerability controls.
- Monitor privileged AI tool/agent actions.

## Recommended actions

1. Define measurable detection-to-containment objectives for high-confidence intrusion patterns.
2. Automate reversible response steps such as token/session revocation and endpoint/network isolation where operationally safe.
3. Extend vulnerability management to edge and AI-development infrastructure.
4. Correlate cloud, identity, SaaS, and endpoint events.
5. Threat model AI tools as both applications and privileged integration surfaces.
6. Build hunt content around malware-free administrative behavior.

## ATT&CK relevance

- T1078 — Valid Accounts
- T1550 — Use Alternate Authentication Material
- T1528 — Steal Application Access Token
- T1190 — Exploit Public-Facing Application
- T1219 — Remote Access Software
- T1098 — Account Manipulation

## Caveats

- The fastest breakout time is an extreme observation, not a typical value.
- "Malware-free" does not mean harmless or tool-free; it often means legitimate or native capabilities were abused.
- State/eCrime attribution reflects CrowdStrike intelligence assessments.
- The report's population reflects CrowdStrike's visibility and should not be treated as global census data.

## Primary sources

- https://www.crowdstrike.com/en-us/global-threat-report/
- https://www.crowdstrike.com/en-us/resources/reports/global-threat-report-executive-summary-2026/
- https://www.crowdstrike.com/en-us/press-releases/2026-crowdstrike-global-threat-report/
- Japanese page: https://www.crowdstrike.com/ja-jp/global-threat-report/

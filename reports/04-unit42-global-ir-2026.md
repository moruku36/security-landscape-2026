---
publisher: "Palo Alto Networks Unit 42"
edition: "2026 Global Incident Response Report"
publication_date: "2026-02-17"
observation_period: "2024-10-01 to 2025-09-30"
dataset_or_scope: "750+ incident-response engagements across 50+ countries; trend comparisons include earlier casework"
geography: "Global"
language: "en"
primary_source: "https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report"
last_verified: "2026-09-27"
---

# Unit 42 Global Incident Response Report 2026

[日本語版](04-unit42-global-ir-2026.ja.md)

## Why this report matters

Unit 42 is one of the closest peers to M-Trends because it is grounded in high-stakes incident-response work. The 2026 edition analyzes more than 750 engagements across more than 50 countries and focuses on a modern enterprise reality: attacks rarely remain in one security product or one technical domain.

Its core value is the connection between **identity, browser activity, endpoints, networks, cloud, SaaS, applications, humans, and third parties**.

## Evidence profile

| Field | Value |
|---|---|
| Main observation period | Oct 1, 2024-Sep 30, 2025 |
| Scale | 750+ IR engagements |
| Geography | 50+ countries |
| Best use | Multi-surface attack paths, identity, attack speed, SaaS/browser/third-party risk |
| Main limitation | IR engagements are high-impact cases, not a random sample of enterprises |

## Executive summary

Unit 42 identifies four major trends:

1. **AI is a force multiplier** that compresses the attack lifecycle.
2. **Identity is the most reliable path to attacker success.**
3. **Supply-chain risk has expanded from vulnerable code to trusted connectivity.**
4. **Nation-state actors are adapting persistence to modern infrastructure and virtualization.**

The report's most important operational conclusion is that enterprise complexity is helping attackers. In 87% of intrusions, activity crossed at least two attack surfaces. Nearly half of investigations involved browser activity, and identity appeared in almost 90%.

This makes fragmented security operations a structural risk: if identity, endpoint, network, cloud, SaaS, and browser signals cannot be correlated, investigators are reconstructing a multi-domain attack from disconnected partial views.

## Key findings

| Finding | Observation context |
|---|---|
| Identity was involved in **89%** of investigated intrusions | Attack-surface involvement |
| **65%** of initial access was identity-driven | Initial-access analysis |
| Vulnerability exploitation represented **22%** of initial access | Initial-access analysis |
| **87%** of intrusions crossed at least two attack surfaces | 750+ engagements |
| **67%** crossed three or more attack surfaces | 2025 casework |
| **43%** crossed four or more attack surfaces | 2025 casework |
| Endpoint activity appeared in **61%**, network 50%, human 45%, email 27%, application 26%, cloud 20% | Attack-surface table |
| Browser-based activity appeared in **48%**, up from 44% in 2024 | 2025 investigations |
| In the fastest observed quartile/cases, initial access to data exfiltration fell to about **72 minutes**, roughly 4x faster than the prior year | Speed analysis |
| Attackers leveraged third-party SaaS applications in **23%** of incidents | Supply-chain/trusted-connectivity analysis |
| More than **90%** of breaches were materially enabled by preventable gaps such as incomplete visibility, inconsistent controls, or excessive trust | Unit 42 assessment |
| Encryption-based extortion declined **15%** from the prior year as more actors moved directly to data theft/disruption | Extortion analysis |

Primary evidence: [Unit 42 2026 Global Incident Response Report](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report).

## Detailed analysis

### 1. Identity is not one stage of the attack—it is the attack path

Unit 42's identity findings are stronger than simply saying "credentials are important."

Identity can serve as:

```text
Initial access
→ privilege escalation
→ lateral movement
→ persistence
→ cloud/SaaS access
→ data access
```

The relevant identity population includes:

- employees;
- administrators;
- service accounts;
- workload identities;
- API keys;
- SaaS/OAuth integrations;
- sessions/tokens;
- embedded AI applications.

This explains why fragmented identity estates are dangerous. An enterprise may have strong controls in its primary IdP while leaving service accounts, SaaS integrations, browser sessions, CI/CD identities, or legacy roles under-governed.

### 2. 65% identity-driven initial access changes the perimeter model

Identity-driven initial access includes social engineering, credential misuse, brute force, previously compromised credentials, IAM misconfiguration, insider risk, and related techniques.

The architecture implication is not to abandon patching—vulnerabilities still account for 22% of initial access—but to treat Identity Security and Exposure Management as two main entry-path programs.

### 3. Multi-surface attacks expose organizational silos

Unit 42's attack-surface table is especially useful:

| Surface | Incidents involving the surface |
|---|---:|
| Identity | 89% |
| Endpoint | 61% |
| Network | 50% |
| Human | 45% |
| Email | 27% |
| Application | 26% |
| Cloud | 20% |
| SecOps | 10% |
| Database | 1% |

Because these categories overlap, they do not add to 100%.

The important point is that 87% crossed multiple surfaces. A SIEM or XDR program therefore needs a common investigation model rather than separate endpoint, cloud, IAM, and SaaS queues.

### 4. The browser is now a security control point

Browser activity appeared in 48% of cases.

The browser connects:

- user identity;
- password/session material;
- SaaS;
- email;
- cloud consoles;
- extensions;
- downloaded content;
- third-party applications.

It therefore sits at the human/identity/SaaS boundary. Browser hardening, extension governance, isolation, session controls, and SaaS visibility become more important as attacks shift away from executable malware.

### 5. Trusted connectivity expands the supply-chain model

Unit 42 argues that supply-chain security is no longer only an OSS/package problem.

Attackers can use:

- third-party SaaS applications;
- vendor tools;
- administrative integrations;
- application dependencies;
- delegated identities;
- service credentials.

The 23% third-party SaaS figure illustrates the problem.

A mature architecture needs a **connection inventory** in addition to an SBOM:

```text
integration
+ owner
+ authentication method
+ scopes
+ data access
+ write authority
+ downstream dependency
+ revoke procedure
+ logs
```

### 6. The 72-minute race requires SOC automation, but not uncontrolled automation

When high-impact exfiltration can occur in roughly an hour in the fastest cases, manual workflow latency becomes a security control failure.

Useful automation:

- context enrichment;
- identity/session risk correlation;
- disabling or revoking suspicious sessions;
- temporary endpoint isolation;
- blocking known malicious infrastructure;
- preserving forensic data.

Actions that can create business disruption—mass account disablement, destructive changes, production shutdown—should remain bounded by confidence and human approval.

### 7. Extortion is becoming quieter

Unit 42 notes a decline in encryption-based extortion as some attackers prefer direct data theft and disruption.

This reduces the usefulness of "ransomware encryption" as the main detection moment. Organizations need earlier detection of:

- staging;
- anomalous data access;
- privilege escalation;
- cloud/SaaS export;
- archive creation;
- large transfers;
- abuse of legitimate admin tools.

## Enterprise Security Architecture implications

### Identity Plane

- Discover both human and non-human identities continuously.
- Remove legacy and standing privilege.
- Shorten credential/token lifetimes.
- Correlate identity actions across IdP, SaaS, cloud, endpoint, and browser.

### Control Plane

- Map which identities can change cloud, SaaS, backup, and infrastructure.
- Use zero-trust/JIT access to reduce implicit trust.

### Supply Chain

- Inventory trusted connections, not only packages.
- Assign owners to every high-impact integration.
- Test revocation.

### Telemetry

- Build an investigation schema across identity, endpoint, network, SaaS, browser, and cloud.
- Measure whether responders can reconstruct one timeline from multiple data sources.

### SecOps

- Optimize for time-to-contain, not alert closure count.
- Use reversible machine-speed containment for narrow, high-confidence scenarios.

## Recommended actions

1. Build a complete human + non-human identity inventory.
2. Remove standing admin and stale service-account permissions.
3. Create a trusted-connection inventory for SaaS/vendor integrations.
4. Add browser/SaaS telemetry to high-value detection scenarios.
5. Centralize cross-domain evidence into a common investigation model.
6. Pre-authorize safe, reversible containment.
7. Measure exfiltration/containment speed during purple-team and tabletop exercises.
8. Shift from "ransomware detection" toward earlier identity, staging, and exfiltration detection.

## ATT&CK relevance

- T1078 — Valid Accounts
- T1528 — Steal Application Access Token
- T1550 — Use Alternate Authentication Material
- T1098 — Account Manipulation
- T1190 — Exploit Public-Facing Application
- T1566 — Phishing
- T1041 / related exfiltration techniques — Exfiltration Over C2 Channel / enterprise-specific channels

## Caveats

- Unit 42 cases are incident-response engagements, which skew toward serious incidents.
- Product/platform recommendations from Palo Alto Networks should be separated from the underlying empirical observations.
- The attack-surface percentages overlap by design; they are not mutually exclusive categories.
- Different Unit 42 publications sometimes summarize "fastest" speed using slightly different phrasing; this repository preserves the report's main point rather than treating those values as universal medians.

## Primary sources

- https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report
- https://www.paloaltonetworks.com/blog/2026/02/unit-42-global-ir-report/
- https://www.paloaltonetworks.com/company/press/2026/unit-42-report--ai-and-attack-surface-complexity-fuel-majority-of-breaches

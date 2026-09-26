---
publisher: "IBM X-Force"
edition: "Threat Intelligence Index 2026"
publication_date: "2026-02-25"
observation_period: "2025 incident-response, investigation, vulnerability and threat-intelligence data"
dataset_or_scope: "IBM X-Force global threat intelligence and incident observations"
geography: "Global"
primary_source: "https://www.ibm.com/reports/threat-intelligence"
last_verified: "2026-09-26"
---

# IBM X-Force Threat Intelligence Index 2026

## Positioning

X-Force combines incident response, vulnerability/exploitation intelligence, dark-web observations, ransomware ecosystem data, and broader threat intelligence.

## Key findings

| Finding | Observation context | Evidence |
|---|---|---|
| Exploitation of public-facing software/system applications increased **44% YoY** | 2025 vs prior year | [IBM](https://www.ibm.com/reports/threat-intelligence) |
| **56%** of disclosed vulnerabilities did not require authentication to exploit successfully | Vulnerability analysis | [IBM](https://www.ibm.com/reports/threat-intelligence) |
| **300,000** AI-chatbot credentials were observed for sale on the dark web | X-Force observation | [IBM](https://www.ibm.com/reports/threat-intelligence) |
| Active ransomware/extortion groups increased **49% YoY** | Ecosystem observation | [IBM](https://newsroom.ibm.com/2026-02-25-ibm-2026-x-force-threat-index-ai-driven-attacks-are-escalating-as-basic-security-gaps-leave-enterprises-exposed) |
| Large supply-chain and third-party compromises nearly quadrupled since 2020 | Longitudinal observation | [IBM newsroom](https://newsroom.ibm.com/2026-02-25-ibm-2026-x-force-threat-index-ai-driven-attacks-are-escalating-as-basic-security-gaps-leave-enterprises-exposed) |

## Interpretation

IBM's data reinforces the repository's central thesis: AI changes speed and scale, while basic exposure and credential weaknesses remain highly effective.

AI-chatbot credential resale is particularly important because AI services should be treated as a new SaaS identity surface, not as an isolated experimentation environment.

## Architecture actions

- External attack-surface inventory and exploit-informed remediation.
- Identity/token lifecycle management for AI services.
- Secret scanning and credential hygiene.
- Third-party/SaaS integration inventory.
- Supply-chain and CI/CD identity hardening.
- Ransomware-resistant recovery.

## ATT&CK relevance

- T1190 Exploit Public-Facing Application
- T1078 Valid Accounts
- T1528 Steal Application Access Token
- T1486 Data Encrypted for Impact
- T1490 Inhibit System Recovery

## Limitations

- Metrics come from different X-Force data sets; they do not necessarily share one denominator.
- Dark-web observations measure what X-Force observed, not the total market.
- Longitudinal supply-chain trends should be read as directional intelligence.

## Sources

- https://www.ibm.com/reports/threat-intelligence
- https://www.ibm.com/think/x-force/threat-intelligence-index-2026-securing-identities-ai-detection-risk-management
- https://newsroom.ibm.com/2026-02-25-ibm-2026-x-force-threat-index-ai-driven-attacks-are-escalating-as-basic-security-gaps-leave-enterprises-exposed
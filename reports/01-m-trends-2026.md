---
publisher: "Google Cloud / Mandiant"
edition: "M-Trends 2026"
publication_date: "2026-03-23"
observation_period: "2025-01-01 to 2025-12-31"
dataset_or_scope: "500,000+ hours of Mandiant frontline incident investigations"
geography: "Global"
primary_source: "https://cloud.google.com/security/resources/m-trends-executive-edition"
last_verified: "2026-09-26"
---

# Mandiant M-Trends 2026

## Positioning

M-Trends is a frontline incident-response report. Its value is not broad population prevalence; it is detailed observation of organizations that required Mandiant investigation and response.

## Key findings

| Finding | Observation context | Evidence |
|---|---|---|
| Exploits were the leading initial infection vector at **32%**, for the sixth consecutive year | 2025 Mandiant investigations | [Google Cloud](https://cloud.google.com/security/resources/m-trends-executive-edition) |
| Voice phishing rose to **11%**, becoming the second-most observed vector; email phishing fell to **6%** | 2025 investigations | [Google Cloud](https://cloud.google.com/security/resources/m-trends-executive-edition) |
| Global median dwell time rose from 11 to **14 days** | 2025 vs 2024 | [Google Cloud](https://cloud.google.com/blog/topics/threat-intelligence/m-trends-2026/) |
| Cyber-espionage and DPRK IT-worker incidents each had a median dwell time of **122 days** | 2025 investigations | [Google Cloud](https://cloud.google.com/security/resources/m-trends-executive-edition) |
| Median initial-access-to-secondary-group handoff fell to **22 seconds** | 2025, compared with 8+ hours in 2022 | [Google Cloud](https://cloud.google.com/security/resources/m-trends-executive-edition) |
| BRICKSTORM-related cases averaged **393 days** of dwell time | Relevant Mandiant cases | [Google Cloud](https://cloud.google.com/security/resources/m-trends-executive-edition) |

## What the source says

Mandiant describes a split in attacker pacing:

- high-velocity cybercrime optimized for fast handoff, impact, extortion, and recovery denial;
- long-lived espionage / insider-style access optimized for persistence in infrastructure with limited visibility.

Edge devices and infrastructure outside normal endpoint telemetry receive particular attention.

The report also explicitly argues that 2025 was **not** a year in which most successful breaches were directly caused by AI. AI is an accelerator, while foundational security gaps remain the dominant enabler.

## Architecture interpretation

### Identity Plane

Vishing, credential theft, SaaS integration tokens, and OAuth consent mean identity controls must include recovery/helpdesk paths and token governance—not only passwords and MFA.

### Control Plane

Edge devices, hypervisors, network appliances, and SaaS integrations can sit outside endpoint tooling while retaining broad authority.

### Recovery Plane

M-Trends' recovery-denial theme supports treating backup and recovery administration as a separate high-trust plane.

### Telemetry Plane

A 90-day retention model is incompatible with cases where dwell time can extend to many months or more than a year.

## Recommended architecture actions

- Forward edge/network administrative logs centrally.
- Collect hypervisor-level telemetry.
- Extend retention for identity, edge, virtualization, and Tier-0 logs.
- Restrict unverified end-user OAuth/app consent.
- Treat low-impact initial-access detections as potential precursors to high-impact intrusion.
- Separate production and recovery authority.

## ATT&CK relevance

Repository mapping:

- T1190 Exploit Public-Facing Application
- T1078 Valid Accounts
- T1528 Steal Application Access Token
- T1550 Use Alternate Authentication Material
- T1490 Inhibit System Recovery

See [MITRE ATT&CK crosswalk](../frameworks/mitre-attack.md).

## Limitations

- The population is Mandiant Consulting investigations, not all global incidents.
- Organizations engaging Mandiant may be biased toward higher-impact or more complex incidents.
- Some sub-themes reflect specific incident clusters and should not be interpreted as universal prevalence.

## Sources

- https://cloud.google.com/security/resources/m-trends-executive-edition
- https://cloud.google.com/blog/topics/threat-intelligence/m-trends-2026/
---
publisher: "Microsoft"
edition: "Microsoft Digital Defense Report 2025"
publication_date: "2025-10-16"
observation_period: "multiple Microsoft telemetry and intelligence datasets; report-specific periods"
dataset_or_scope: "Microsoft security, identity, cloud, fraud and threat-intelligence telemetry"
geography: "Global"
primary_source: "https://www.microsoft.com/en-us/security/security-insider/threat-landscape/microsoft-digital-defense-report-2025"
last_verified: "2026-09-27"
---

# Microsoft Digital Defense Report 2025

> This is the latest annual Microsoft Digital Defense Report available as of the repository snapshot date, 2026-09-26.

## Positioning

MDDR is broader than a pure incident-response report. It combines cybercrime, nation-state activity, identity, cloud, AI, fraud, resilience, and geopolitical context.

## Key findings highlighted by Microsoft

| Finding | Context | Evidence |
|---|---|---|
| Destructive campaigns targeting cloud increased **87%** | Microsoft report summary | [Microsoft](https://www.microsoft.com/en-us/security/security-insider/threat-landscape/microsoft-digital-defense-report-2025) |
| AI-driven phishing was reported as **3× more effective** than traditional campaigns | Report summary | [Microsoft](https://www.microsoft.com/en-us/security/security-insider/threat-landscape/microsoft-digital-defense-report-2025) |
| More than **40%** of ransomware attacks had a hybrid component | Report summary | [Microsoft](https://www.microsoft.com/en-us/security/security-insider/threat-landscape/microsoft-digital-defense-report-2025) |
| AI-driven forgeries increased **195% globally** | Synthetic-identity section | [Microsoft](https://www.microsoft.com/en-us/security/security-insider/threat-landscape/microsoft-digital-defense-report-2025) |\n| **28%** of Microsoft IR breaches began with phishing/social engineering, **18%** with unpatched web assets, and **12%** with exposed remote services | Microsoft Incident Response | [Microsoft](https://www.microsoft.com/en-us/security/security-insider/threat-landscape/microsoft-digital-defense-report-2025) |\n| Only **4%** of incidents with a known motivation were espionage-driven | Microsoft Incident Response | [Microsoft](https://www.microsoft.com/en-us/security/security-insider/threat-landscape/microsoft-digital-defense-report-2025) |

## Strategic themes

Microsoft frames the defensive response around:

- innovation;
- resilience;
- collaboration;
- speed and scale.

The report explicitly calls out identity and cloud resilience, secure-by-default practices, and automated response.

## Architecture interpretation

### Identity + Cloud

Identity compromise and cloud destructive activity should be modeled together. A privileged identity is a control-plane credential.

### Business continuity

Microsoft's "assume breach" resilience message aligns with separating recovery architecture from the normal production trust boundary.

### AI

Microsoft describes AI as:

- attacker accelerator;
- defensive automation mechanism;
- new attack surface.

This supports managing agent identity, data access, model/app security, and tool authority as part of normal enterprise controls.

## Architecture actions

- Secure-by-default platform guardrails.
- Identity and cloud-resilience integration.
- Automated response for time-critical, high-confidence events.
- AI security framework covering discovery, protection, data, agents, applications, and models.
- Cross-industry / CERT / government collaboration for disruption and intelligence.

## Limitations

- This edition predates several 2026 reports in the repository.
- Microsoft uses multiple telemetry populations rather than one uniform incident sample.
- It should therefore be used for strategic context, not direct percentage comparison with IR-only reports.

## Sources

- https://www.microsoft.com/en-us/security/security-insider/threat-landscape/microsoft-digital-defense-report-2025
- https://www.microsoft.com/en-us/security/security-insider/threat-landscape/microsoft-digital-defense-report-archives
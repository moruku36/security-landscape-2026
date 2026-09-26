---
publisher: "Verizon"
edition: "2026 Data Breach Investigations Report"
publication_date: "2026-05-18"
observation_period: "2024-11-01 to 2025-10-31"
dataset_or_scope: "Global incident and breach data contributed by law enforcement, forensic firms, insurers, industry groups, VTRAC and other partners"
geography: "Global"
primary_source: "https://www.verizon.com/business/resources/reports/dbir/"
last_verified: "2026-09-26"
---

# Verizon 2026 Data Breach Investigations Report

## Positioning

DBIR is the broadest statistical baseline in this repository. Its strength is contributor diversity and a large global incident/breach population rather than deep technical reconstruction of a single IR provider's cases.

## Key findings

| Finding | Observation context | Evidence |
|---|---|---|
| **31%** of breaches started with software vulnerabilities | 2026 DBIR breach population | [Verizon](https://www.verizon.com/business/resources/reports/dbir/) |
| **48%** of breaches involved ransomware | 2026 DBIR | [Verizon](https://www.verizon.com/business/resources/reports/dbir/) |
| Generative AI augmented **15%** of attack techniques | 2026 DBIR | [Verizon](https://www.verizon.com/business/resources/reports/dbir/) |
| Mobile-targeted social engineering produced **40% higher click rates** | 2026 DBIR | [Verizon](https://www.verizon.com/business/resources/reports/dbir/) |

Verizon states that the in-scope incident period for the 2026 edition is **2024-11-01 through 2025-10-31**.

## Interpretation

DBIR reinforces two parallel realities:

1. Human-targeted attacks remain relevant and are moving toward mobile and interactive channels.
2. Exploitation of exposed software has become a leading initial-access path.

The architecture implication is that organizations should not frame the problem as "people versus vulnerabilities." Both identity controls and exposure reduction are core.

## Architecture actions

### Exposure

Move from CVSS-only patch queues toward:

```text
Severity
+ Internet exposure
+ Known exploitation
+ Reachable privilege
+ Business criticality
+ Compensating controls
= Priority
```

### Identity

- phishing-resistant MFA;
- helpdesk/recovery hardening;
- session/token controls;
- mobile-aware social-engineering defense.

### Resilience

The continued prevalence of ransomware supports recovery testing as an architecture requirement, not only a backup-operations task.

## ATT&CK relevance

- T1190 Exploit Public-Facing Application
- T1078 Valid Accounts
- T1486 Data Encrypted for Impact
- T1490 Inhibit System Recovery

## Limitations

- "Incident" and "breach" are distinct DBIR concepts; not every incident becomes a confirmed breach.
- Contributor mix and geography affect annual patterns.
- DBIR prevalence should not be directly compared with percentages from vendor-specific IR casework.

## Sources

- https://www.verizon.com/business/resources/reports/dbir/
- https://www.verizon.com/business/resources/reports/
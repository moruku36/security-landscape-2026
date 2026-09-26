# CIS Controls v8.1 crosswalk

CIS Controls v8.1 is a prioritized set of safeguards for common cyber attacks. CIS describes Implementation Groups (IG1–IG3) as a way to prioritize implementation based on enterprise risk and resources.

Primary source: https://www.cisecurity.org/controls/v8-1

This document maps the 2026 architecture themes to representative CIS Controls. It is a practical crosswalk, not a substitute for the official CIS Navigator.

## Theme mapping

| 2026 theme | Representative CIS Controls v8.1 |
|---|---|
| Internet-facing asset visibility | **1 Enterprise Assets**, **2 Software Assets**, **7 Continuous Vulnerability Management** |
| Secure control planes / configuration | **4 Secure Configuration**, **12 Network Infrastructure Management** |
| Human + non-human identity governance | **5 Account Management**, **6 Access Control Management** |
| Central telemetry | **8 Audit Log Management**, **13 Network Monitoring and Defense** |
| Recovery Plane | **11 Data Recovery** |
| SaaS / vendor / trusted connectivity | **15 Service Provider Management** |
| DevSecOps / application security | **16 Application Software Security** |
| Incident operating model | **17 Incident Response Management** |
| Red team / validation | **18 Penetration Testing** |

## Example: Identity

2026 evidence:

- stolen credentials and tokens remain effective;
- OAuth/delegated access creates persistence and lateral movement;
- non-human identities can hold high privilege.

CIS-oriented response:

- maintain account inventory;
- centralize access-control processes;
- disable dormant identities;
- enforce MFA where applicable;
- separate administrative accounts;
- review and revoke unnecessary access.

Architecture extension:

> Apply the same governance logic to service accounts, OAuth clients, workload roles, and AI agents even where a safeguard was originally written with traditional accounts in mind.

## Example: Recovery

2026 evidence:

- ransomware remains prevalent;
- recovery mechanisms can be attacked directly;
- hypervisor and cloud recovery paths are in scope.

CIS Control 11 provides the operational anchor, while this repository extends the architecture to:

- separate recovery identities;
- immutable/offline copies;
- control-plane loss exercises;
- backup-policy telemetry;
- destructive-action dual control.

## Example: Service providers and SaaS

Trusted SaaS and vendor connectivity is an attack path, not only a procurement issue.

Use Control 15 as the governance anchor for:

- provider inventory;
- security requirements;
- ownership;
- access review;
- incident-disconnection procedures;
- audit/logging requirements.

Then connect it to Controls 5/6 (identity/access), 8 (logs), 16 (software), and 17 (incident response).

## Example: Detection engineering

CIS is most useful when safeguards generate measurable evidence.

```text
Safeguard
→ required telemetry
→ detection hypothesis
→ validation
→ incident runbook
→ metric
```

This connects Controls 8, 13, 17, and 18 to the [Detection Engineering](../operations/detection-engineering.md) lifecycle.

## Implementation Groups

Use IGs as an implementation-priority aid, not as a reason to ignore high-impact architecture risk.

A smaller organization may still need an advanced safeguard if it operates:

- privileged cloud control planes;
- internet-facing critical services;
- sensitive SaaS integrations;
- high-impact recovery infrastructure;
- autonomous or privileged AI agents.

Risk context should remain primary.

## Official mapping tools

CIS provides the Controls Navigator, and NIST maintains Informative References including CIS 8.1-to-CSF 2.0 mappings.

- https://www.cisecurity.org/controls/cis-controls-navigator/v8
- https://www.nist.gov/cyberframework/informative-references
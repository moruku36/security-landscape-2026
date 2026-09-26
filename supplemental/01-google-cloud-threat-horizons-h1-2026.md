---
publisher: "Google Cloud"
edition: "Cloud Threat Horizons H1 2026"
publication_date: "2026-03-10"
observation_period: "Primarily H2 2025"
scope: "Cloud and SaaS threat intelligence from Google Cloud OCSO, GTIG, Mandiant and product/security teams"
language: "en"
primary_source: "https://cloud.google.com/security/report/resources/cloud-threat-horizons-report-h1-2026"
last_verified: "2026-09-27"
---

# Google Cloud Threat Horizons H1 2026

[日本語版](01-google-cloud-threat-horizons-h1-2026.ja.md)

## Why it belongs here

This report fills a gap that the core annual reports only partially cover: **cloud-native incident paths and forensic readiness**. It is explicitly multi-cloud in intent even though it is published by Google Cloud.

## Key findings

- Third-party software exploitation became the leading cloud initial-access vector in H2 2025 at **44.5%**, up from **2.9%** in H1.
- Weak/missing credentials fell from **47.1%** to **27.2%**.
- RCE rose from **2.9%** to **13.6%**.
- Misconfiguration fell from **29.4%** to **21%**; exposed sensitive UI/API fell from **11.8%** to **4.9%**.
- Identity issues enabled initial access in **83%** of major cloud/SaaS incidents in the cited Mandiant engagements.
- Data was targeted in **73%** of cloud-related incidents.
- Vishing appeared in **17%** of the platform-agnostic initial-access cases discussed.
- The report highlights a CI/CD-to-cloud compromise where attackers abused OIDC trust and excessive role permissions.

## Architecture interpretation

The report strongly supports four design ideas:

1. **Cloud security is becoming an application/exposure problem as well as an IAM problem.**
2. **CI/CD federation must be least-privileged and independently auditable.**
3. **Forensic readiness must be pre-provisioned.** Waiting for permissions, logs, snapshots, or volatile evidence after detection creates hours or days of delay.
4. **Cloud IR should be automated around evidence preservation.**

A useful architecture pattern is:

```text
Detection
→ pre-authorized IR identity
→ snapshot / memory / log preservation
→ normalized timeline
→ context-aware containment
```

rather than creating access only after an incident starts.

## Recommended actions

- Pre-create least-privileged IR roles at organization scope.
- Centralize cloud audit logs outside the same blast radius as production.
- Treat CI/CD OIDC trust as a privileged federation path.
- Add third-party framework/app exposure to cloud attack-surface management.
- Automate snapshot, log, and volatile-data collection.
- Test response when the compromised workload is autoscaled, deleted, or rebooted.

## Why it complements M-Trends

M-Trends explains what happened in enterprise incidents. Threat Horizons adds more cloud-specific mechanics: cloud initial-access distribution, CI/CD/OIDC pivots, forensic collection delays, and cloud-native response design.

## Primary sources

- https://cloud.google.com/security/report/resources/cloud-threat-horizons-report-h1-2026
- https://cloud.google.com/blog/products/identity-security/cloud-ciso-perspectives-new-threat-horizons-report-highlights-current-cloud-threats

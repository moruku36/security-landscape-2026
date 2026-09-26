---
publisher: "Sophos X-Ops"
edition: "Active Adversary Report 2026"
publication_date: "2026-02-24"
observation_period: "2024-11-01 to 2025-10-31"
scope: "661 IR and MDR cases across 70 countries and 34 industries"
language: "en"
primary_source: "https://www.sophos.com/en-us/blog/2026-sophos-active-adversary-report"
last_verified: "2026-09-27"
---

# Sophos Active Adversary Report 2026

[日本語版](02-sophos-active-adversary-2026.ja.md)

## Why it belongs here

Sophos adds a useful IR/MDR perspective on **identity, after-hours attacker activity, Active Directory speed, firewall telemetry, and log retention**.

## Key findings

- **67%** of investigated incidents were rooted in identity-related causes.
- Exploited vulnerabilities accounted for **16%** of initial access; brute force was nearly equal at **15.6%**.
- MFA was missing where it mattered in **59%** of cases.
- Median dwell time fell to **3 days**.
- Attackers reached Active Directory in just **3.4 hours** after entering the environment.
- **88%** of ransomware payload deployments and **79%** of data-exfiltration activity occurred outside normal business hours.
- Missing logs caused by retention problems doubled year over year.
- Firewall appliances were a major cause of missing telemetry, sometimes retaining only seven days or even 24 hours.
- In incidents starting with a CVE, more than two-thirds involved a single repeatedly exploited SonicWall vulnerability; median time from vendor patch/advisory to exploitation across confirmed exploited vulnerabilities was **322 days**.

## Architecture interpretation

Sophos reinforces three practical points.

### Identity

Identity compromise is not a specialized IAM problem. It is the dominant root-cause family across real incidents. MFA coverage and configuration quality matter as much as deploying an MFA product.

### 24x7 response

If ransomware and exfiltration disproportionately happen outside office hours, security architecture needs operational coverage that survives nights and weekends.

### Log retention

A firewall that retains seven days of logs can become a forensic blind spot even when the device itself is functioning correctly. Retention is therefore a security control, not merely a storage-cost decision.

## Recommended actions

- Require phishing-resistant MFA for privileged and externally reachable access.
- Monitor identity infrastructure 24x7.
- Retain edge/firewall logs centrally for meaningful investigation windows.
- Measure time from initial access to AD/control-plane reachability.
- Patch edge devices aggressively, but also verify old exposures are actually remediated.
- Ensure off-hours containment can occur without waiting for business-day staffing.

## Primary sources

- https://www.sophos.com/en-us/blog/2026-sophos-active-adversary-report
- https://www.sophos.com/ja-jp/press/press-releases/sophos-active-adversary-report-2026-identity-attacks-dominate-as-threat-groups-proliferate

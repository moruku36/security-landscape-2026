---
publisher: "Palo Alto Networks Unit 42"
edition: "2026 Global Incident Response Report"
publication_date: "2026-02-17"
observation_period: "2024-10-01 to 2025-09-30"
dataset_or_scope: "750+ Unit 42 incident-response cases across 50+ countries; comparisons include earlier cases back to 2021"
geography: "Global (50+ countries)"
primary_source: "https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report"
last_verified: "2026-09-27"
---

# Unit 42 Global Incident Response Report 2026

## Positioning

Unit 42 is one of the closest peers to M-Trends in this repository: an incident-response-centric view, with strong emphasis on multi-surface attacks, identity, browser/SaaS activity, cloud, and third-party connectivity.

## Four major trends

1. AI acts as a force multiplier and compresses attack lifecycle.
2. Identity is the most reliable path to attacker success.
3. Supply-chain risk extends beyond vulnerable code to trusted connectivity.
4. Nation-state actors are moving deeper into infrastructure and virtualization.

## Key findings

| Finding | Observation context | Evidence |
|---|---|---|
| Identity weaknesses played a material role in **nearly 90%** of investigations | 2025 casework | [Unit 42](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report) |
| **87%** of intrusions involved activity across two or more attack surfaces | 750+ IR engagements | [Unit 42](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report) |\n| In **87%** of investigations, responders reviewed evidence from two or more distinct data sources | 2025 casework | [Unit 42](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report) |
| **48%** of investigations involved browser-based activity | 2025 | [Unit 42](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report) |
| Fastest quartile reached exfiltration in **72 minutes**, down from **285 minutes** in 2024 | Calendar-year 2025 vs 2024 IR data | [Unit 42](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report) |
| More than **90%** of incidents were materially enabled by preventable gaps / inconsistent controls | 2025 | [Unit 42](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report) |
| Phishing and vulnerability exploitation each accounted for **22%** of initial access | 2025 incidents | [Unit 42](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report) |

## Identity interpretation

Identity is not merely initial access. Unit 42 describes identity as a path for:

```text
Initial access
→ privilege escalation
→ lateral movement
→ persistence
```

The scope includes non-human identities such as service accounts, automation roles, and API keys.

## Supply-chain interpretation

"Supply chain" should not be reduced to compromised packages.

The attack surface includes:

- SaaS integrations;
- vendor tools;
- application dependencies;
- trusted administrative connectivity;
- service credentials.

This argues for a **connection inventory** alongside SBOM/SCA.

## Telemetry interpretation

The 87% multi-source finding supports a unified investigation model. Endpoint, network, cloud, identity, browser, and SaaS signals must be correlatable before an incident.

## Architecture actions

- Continuous non-human identity discovery.
- Reduce static credential lifetime.
- Exposure management focused on exploitable/business-critical assets.
- Browser/SaaS security visibility.
- Integration ownership and emergency revocation.
- Unified telemetry and automated response.

## ATT&CK relevance

- T1078 Valid Accounts
- T1528 Steal Application Access Token
- T1550 Use Alternate Authentication Material
- T1098 Account Manipulation
- T1190 Exploit Public-Facing Application

## Limitations

- Incident-response casework is not a random sample of enterprises.
- Palo Alto product recommendations appear alongside incident findings; architecture conclusions should be separated from product selection.

## Sources

- https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report
- https://www2.paloaltonetworks.com/resources/research/2026-incident-response-report-executive-edition
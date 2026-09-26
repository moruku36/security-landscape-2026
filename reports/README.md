# Annual security reports

This directory contains **detailed English and Japanese analyses** of the major annual security reports used by this repository.

The goal is not to reproduce the original reports. Each note separates:

1. the publisher's observation boundary and statistics;
2. a detailed explanation of the major themes;
3. repository-authored Enterprise Security Architecture implications;
4. actionable controls;
5. limitations and primary-source links.

## Reports / レポート一覧

| Report | English | 日本語 |
|---|---|---|
| Mandiant M-Trends 2026 | [English](01-m-trends-2026.md) | [日本語](01-m-trends-2026.ja.md) |
| Verizon 2026 DBIR | [English](02-verizon-dbir-2026.md) | [日本語](02-verizon-dbir-2026.ja.md) |
| CrowdStrike 2026 Global Threat Report | [English](03-crowdstrike-global-threat-report-2026.md) | [日本語](03-crowdstrike-global-threat-report-2026.ja.md) |
| Unit 42 2026 Global Incident Response Report | [English](04-unit42-global-ir-2026.md) | [日本語](04-unit42-global-ir-2026.ja.md) |
| Microsoft Digital Defense Report 2025 | [English](05-microsoft-digital-defense-report-2025.md) | [日本語](05-microsoft-digital-defense-report-2025.ja.md) |
| IBM X-Force Threat Intelligence Index 2026 | [English](06-ibm-xforce-2026.md) | [日本語](06-ibm-xforce-2026.ja.md) |
| ENISA Threat Landscape 2026 | [English](07-enisa-threat-landscape-2026.md) | [日本語](07-enisa-threat-landscape-2026.ja.md) |

## How to read the numbers

Before comparing statistics across reports, check:

1. **Observation period** — calendar year, rolling period, or report-specific window.
2. **Population** — incidents, confirmed breaches, IR engagements, telemetry detections, identities, vulnerabilities, or threat clusters.
3. **Geography** — global, customer-specific, or region-specific.
4. **Statistic type** — count, percentage, median, average, fastest observation, or year-over-year delta.
5. **Collection method** — frontline IR, product telemetry, contributor consortium, threat intelligence, or public-sector event collection.

A percentage in one report is **not automatically comparable** to the same-looking percentage in another.

For example:

- DBIR distinguishes a security **incident** from a confirmed **breach**.
- M-Trends and Unit 42 analyze specialist incident-response casework.
- CrowdStrike emphasizes adversary intelligence and detections.
- Microsoft combines multiple large telemetry populations.
- ENISA includes EU-focused incidents and events, including availability-oriented activity such as DDoS.

## Evidence model

Each detailed report contains:

- YAML metadata for scope and verification date;
- an **Evidence Profile**;
- an **Executive Summary**;
- a **Key Findings** table;
- **Detailed Analysis**;
- **Enterprise Security Architecture implications**;
- **Recommended Actions**;
- ATT&CK relevance;
- caveats;
- primary-source links.

Source-derived facts and repository-authored interpretation are intentionally separated.

## Update workflow

Use:

- [English template](_template.md)
- [日本語テンプレート](_template.ja.md)

When updating an edition:

- preserve the publisher's original measurement type;
- use exact observation periods where available;
- keep counts, percentages, medians, averages, and fastest observations distinct;
- never compare vendor percentages without checking denominators;
- link important claims to primary/official evidence;
- update both English and Japanese versions together;
- update `last_verified` only after checking the source again.

See also [../SOURCES.md](../SOURCES.md).

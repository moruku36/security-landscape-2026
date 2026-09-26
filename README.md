# Security Landscape 2026

> 2026-09-26 snapshot — major annual cybersecurity reports and conferences, summarized and interpreted from an Enterprise IT / Cloud / Security / Operations perspective.

## Purpose

2026年9月26日時点で公開済みの主要セキュリティ年次レポートと、2026年に開催された代表的なカンファレンスを横断し、単なる要約ではなく「Enterprise Security Architectureとして何を変えるべきか」まで整理する。

このリポジトリでは、ベンダーごとの観測差を意識しつつ、複数ソースで繰り返し現れるシグナルを重視する。

## Executive summary

2026年の共通メッセージは **AIがすべてを置き換えた** ではない。むしろ、既存の弱点をAIと自動化が高速・大規模化している。

特に重要な変化は次の通り。

1. **Identity is the practical perimeter** — 人間だけでなく、Service Account / API Key / OAuth / Session Token / AI AgentなどNon-Human Identityまで攻撃面になった。
2. **Internet-facing / Edge / Virtualizationが主戦場** — VPN、Firewall、Web Asset、Hypervisorなど、EDRの外側にある基盤が狙われる。
3. **Cloud / SaaS / Supply Chainが一体化** — OAuth連携、SaaS Integration、Vendor Tool、OSS依存関係が横展開経路になる。
4. **攻撃速度が人間の手動運用を追い越す** — 数十秒単位のhandoff/breakout、数十分〜数時間のexfiltrationが現実化。
5. **RecoveryがSecurity Architectureの一部になる** — Backupがあるだけでは足りず、Identity・Virtualization・Recovery PlaneをProductionから分離する必要がある。
6. **Telemetryの死角が致命傷になる** — Endpointだけでなく、IdP、Edge、Hypervisor、Cloud Control Plane、SaaS、AI Toolまで観測対象にする。
7. **AI Securityは二面性** — 攻撃者のforce multiplierであると同時に、SOC/CTI/Exposure Managementの自動化にも使える。Agentic AIでは「モデル」よりTool Access、Identity、Authorization、Auditが重要。

## Contents

### Annual reports

- [Mandiant M-Trends 2026](reports/01-m-trends-2026.md)
- [Verizon 2026 DBIR](reports/02-verizon-dbir-2026.md)
- [CrowdStrike 2026 Global Threat Report](reports/03-crowdstrike-global-threat-report-2026.md)
- [Palo Alto Networks Unit 42 2026 Global Incident Response Report](reports/04-unit42-global-ir-2026.md)
- [Microsoft Digital Defense Report 2025 — latest annual edition as of 2026-09-26](reports/05-microsoft-digital-defense-report-2025.md)
- [IBM X-Force Threat Intelligence Index 2026](reports/06-ibm-xforce-2026.md)
- [ENISA Threat Landscape 2026](reports/07-enisa-threat-landscape-2026.md)

### Conferences

- [RSAC 2026](conferences/01-rsac-2026.md)
- [Black Hat USA 2026](conferences/02-black-hat-usa-2026.md)
- [DEF CON 34](conferences/03-def-con-34.md)
- [FIRST CTI 2026](conferences/04-first-cti-2026.md)
- [FIRSTCON26](conferences/05-firstcon26.md)

### Cross-source analysis

- [Cross-report trend matrix](analysis/cross-report-trends.md)
- [Enterprise Security Architecture implications](analysis/enterprise-architecture-implications.md)
- [Cloud / Security / DevSecOps focus](analysis/moruku-focus.md)
- [2026 priority backlog](analysis/security-priorities-2026.md)
- [Sources and methodology](SOURCES.md)

## One-line architecture takeaway

```text
Endpoint Security
      ↓
Identity + Cloud/SaaS + Edge + Virtualization + Recovery + AI Control Plane
      ↓
Unified Telemetry / Exposure Management / Detection Engineering / Automated Response
```

2026年は「EDRを強くする」年というより、**EDRの外側にあるControl PlaneをTier-0として再設計する年**と捉えると、各レポートの主張がつながる。

## Scope note

- これは2026-09-26時点のスナップショット。
- 各社の統計母集団・観測方法は異なるため、数字を直接比較してランキング化しない。
- Microsoft Digital Defense Reportは、この日付時点で公開されている最新年次版として2025 editionを採用。
- カンファレンスは全セッションの逐語要約ではなく、公式プログラム・公式recap・代表的な技術セッションからテーマを抽出している。

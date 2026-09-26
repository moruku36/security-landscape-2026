---
publisher: "ENISA"
edition: "ENISA Threat Landscape 2026"
publication_date: "2026-09-22"
observation_period: "2025-01-01 to 2025-12-31"
dataset_or_scope: "EUに影響するCyber Incident / EventをENISA Methodologyで分析"
geography: "European Union / Europe-focused"
language: "ja"
translation_of: "07-enisa-threat-landscape-2026.md"
primary_source: "https://www.enisa.europa.eu/publications/enisa-threat-landscape-2026"
last_verified: "2026-09-27"
---

# ENISA Threat Landscape 2026 — 日本語解説

[English](07-enisa-threat-landscape-2026.md)

## このレポートを読む意味

ENISA Threat Landscapeは、Commercial Vendorとは異なる視点を提供します。

ENISAはEU Cybersecurity Agencyとして、

- Critical / Essential Entity
- Public Administration
- NIS2
- Geopolitics
- Hacktivism
- Cybercrime
- State-aligned Activity
- Resilience
- Dependency

を重視しています。

そのため「どう侵入されたか」だけでなく、

> **どの社会機能が狙われ、AvailabilityやDependencyがどうBusiness / Public Serviceへ波及するか**

を見るのに向いています。

## Evidence Profile

| 項目 | 内容 |
|---|---|
| 観測期間 | 2025年1月1日〜12月31日 |
| 地域 | EU中心 |
| 情報源 | ENISAが収集・分析したCyber Incident / Event |
| 強み | Critical Sector、Geopolitics、Resilience、NIS2 |
| 注意点 | Vendor IRとは異なるPublic Policy / EU Perspective |

## エグゼクティブサマリー

ENISA 2026の中心テーマは、**Digital DependencyがAttack SurfaceとImpactを拡大している**ことです。

RansomwareはShort-term Impactが最も大きいIncident Typeと評価されています。

Public Administrationは最もTargetedなSectorで、そこではIdeology-driven DDoSの割合が非常に高くなっています。

Target Organizationの73%がNIS2上のEssential / Important Entityであり、Cybersecurityは個社のRiskだけでなく社会サービス継続のRiskになっています。

AIもCybercrime、State Actor、Information Manipulationで使われる一方、AI System自体も新たなAttack Surfaceになります。

## 主要データ

| Findings | 内容 |
|---|---|
| NIS2 Essential / Important Entity | Targetの**73%** |
| Public Administration | **32%**で最多 |
| Business Services | 8% |
| Transport | 8% |
| Manufacturing | 7% |
| Finance / Banking | 6% |
| Public Administration DDoS | Eventの**82%**がIdeology-driven |
| Cybercrime | Total Eventの**36%** |
| Financially Motivated Activity | Ransomware 40%、Data Breach 31%、Fraud/Impersonation 19% |
| State-nexus | Intrusion Operation **87%**、Phishing 12% |
| Hacktivist Claim | **4,709件** |
| Hacktivism DDoS | **89%超** |
| New CVE | **48,000件超**、前年比**22%増** |
| Most Short-term Impactful | Ransomware |

一次情報:
- https://www.enisa.europa.eu/publications/enisa-threat-landscape-2026
- https://www.enisa.europa.eu/news/exploring-the-evolution-of-the-cyber-threat-landscape-how-dependencies-weaken-our-digital-resilience

## 詳細解説

### 1. NIS2対象EntityがTargetの中心

Target Organizationの73%がNIS2上のEssential / Important Entityです。

これは、

- Public Administration
- Transport
- Finance
- Health
- Digital Infrastructure
- ICT Management
- Water
- Space

など、社会が依存するServiceがAttack対象であることを示します。

このようなSectorではConfidentialityだけでなく**Availability / Continuity**が第一級Security Objectiveになります。

### 2. Public AdministrationとDDoS

Public Administrationは32%で最多Sector。

そのEventの82%がIdeology-driven DDoSです。

ここで注意すべきなのは、Event Countが高いからといってすべてDeep Compromiseではないことです。

しかしPublic ServiceではAvailability自体がCriticalです。

必要なのは、

- DDoS Protection
- CDN / Anycast
- Rate Limit
- Failover
- Degraded Service Mode
- Alternate Communication
- Crisis Communication

です。

### 3. Cybercrimeは依然としてOperational Risk

CybercrimeはTotal Eventの36%。

Financially Motivated Activityでは、

- Ransomware 40%
- Data Breach 31%
- Fraud/Impersonation 19%

が大きなCategoryです。

Microsoft / IBM同様、通常のEnterpriseが日常的に直面するRiskはFinancial Motivationが中心です。

### 4. State ActorではLong-term Intrusionを意識する

State-nexus Setは主にIntrusion Operation（87%）を実施し、Phishingは12%でした。

High-value Sectorでは、

- Long-term Persistence
- Credential Abuse
- Supplier Access
- Intelligence Collection

を考慮する必要があります。

そのため、

- Long-term Logging
- Segmentation
- Threat Hunt
- High-value Asset Classification

が重要になります。

### 5. HacktivismはGeopoliticsでRiskが変動

2025年に4,709件のHacktivist Claimが記録され、その89%超がDDoSでした。

Campaignは、

- Election
- Protest
- Geopolitical Tension
- Ukraine Support

など政治イベントに連動しています。

つまりTechnologyが変わっていなくても、**外部情勢によってThreat Likelihoodが急上昇する**ことがあります。

Security OperationはGeopolitical IntelligenceもReadiness Triggerとして利用できます。

### 6. CVE Volumeが増え続ける

2025年には48,000件超のCVEが公開され、前年比22%増。

Vulnerability CountそのものをKPIにすると、増え続ける母数に負けます。

必要なのは、

- Exploitability
- Internet Exposure
- Active Exploitation
- Business Criticality
- Reachability
- Compensating Control

を使ったPriority付けです。

### 7. AIのDual Role

ENISAはMalicious ActorによるAI利用拡大を観測しています。

- AI-generated Text
- Translation
- Synthetic Audio/Video
- Information Manipulation
- Cyber Operation支援

などです。

同時にEnterpriseへのAI導入によりAttack Surfaceも拡張します。

したがってAIを、

- Asset Inventory
- Identity
- Supplier Risk
- Data Governance
- Incident Response
- Resilience

へ組み込む必要があります。

### 8. DependencyがArchitecture上の最重要Theme

ENISA 2026のTitle-level MessageはDependencyです。

Dependencyには、

- Cloud Provider
- Managed Service
- Telecom
- SaaS
- Identity Provider
- Software Supplier
- Shared Infrastructure

などがあります。

自社SystemがSecureでも、Dependencyが落ちればServiceは止まります。

そのためCyber ResilienceではDependency Graphが必要です。

## Enterprise Security Architectureへの示唆

### Resilience

- Critical Service Dependency Map
- Degraded Mode
- Provider Failure Exercise

### Governance / NIS2

- Critical FunctionのOwner
- Supplier Dependency
- Risk Acceptance
- Incident Reporting
- Evidence

### Availability

- DDoS / Upstream FailureをArchitecture Scenario化
- Alternate Communication / Failover

### Exposure Management

- CVE CountではなくExploit-informed Priority

### Threat Intelligence

- Geopolitical EventをReadiness Triggerへ

## 優先アクション

1. Critical Business Service Dependency Mapを作る
2. NIS2/Critical FunctionとIdentity / Platform / Supplierを紐付ける
3. DDoS / SaaS Outage / Supplier Compromise Exercise
4. Exploit-informed Vulnerability Management
5. Espionage Target向けLong-term Telemetry
6. Geopolitical ContextをThreat Readinessへ
7. AI Service / Supplierを通常のThird-party Governanceへ

## ATT&CK対応

- T1190 — Exploit Public-Facing Application
- T1078 — Valid Accounts
- T1566 — Phishing
- T1498 — Network Denial of Service
- T1486 — Data Encrypted for Impact
- T1195 — Supply Chain Compromise

## 注意点

- EU中心のPublic Policy / Critical Sector Perspectiveです。
- DDoS ClaimなどもEvent Countに含まれるため、Confirmed Breachとは性質が異なります。
- Commercial IR ReportのPercentageと直接比較すべきではありません。
- Geopolitical AttributionはContext依存です。

## Primary Sources

- https://www.enisa.europa.eu/publications/enisa-threat-landscape-2026
- https://www.enisa.europa.eu/topics/cyber-threats/threat-landscape
- https://www.enisa.europa.eu/news/exploring-the-evolution-of-the-cyber-threat-landscape-how-dependencies-weaken-our-digital-resilience

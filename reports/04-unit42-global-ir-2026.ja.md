---
publisher: "Palo Alto Networks Unit 42"
edition: "2026 Global Incident Response Report"
publication_date: "2026-02-17"
observation_period: "2024-10-01 to 2025-09-30"
dataset_or_scope: "50か国超・750件超のIncident Response Engagement"
geography: "Global"
language: "ja"
translation_of: "04-unit42-global-ir-2026.md"
primary_source: "https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report"
last_verified: "2026-09-27"
---

# Unit 42 Global Incident Response Report 2026 — 日本語解説

[English](04-unit42-global-ir-2026.md)

## このレポートを読む意味

Unit 42の2026 Global Incident Response Reportは、M-Trendsと非常に近い性格を持ちます。

50か国超・750件超の高ImpactなIR案件を分析し、

- Identity
- Endpoint
- Network
- Cloud
- SaaS
- Browser
- Human
- Third-party

を跨ぐAttack Pathを詳細に扱っています。

このレポートの最大の特徴は、**Enterprise Complexityそのものが攻撃者の武器になっている**と整理していることです。

## Evidence Profile

| 項目 | 内容 |
|---|---|
| 主な観測期間 | 2024年10月1日〜2025年9月30日 |
| IR Engagement | 750件超 |
| 地域 | 50か国超 |
| 強み | Identity / Multi-surface / Browser / SaaS / Attack Speed |
| 注意点 | Serious Incident中心でありRandom Sampleではない |

## エグゼクティブサマリー

Unit 42は2026年を形作る4つのTrendを挙げています。

1. **AIがForce MultiplierになりAttack Lifecycleを圧縮**
2. **Identityが最も確実なAttack Path**
3. **Supply Chain RiskがCodeからTrusted Connectivityへ拡大**
4. **Nation-stateがInfrastructure / Virtualizationへ深く侵入**

最も重要な数字は、87%のIntrusionが複数Attack Surfaceを跨いでいたことです。

Identity、Endpoint、Network、Cloud、SaaS、Browserを別々のSecurity TeamやToolで管理し、Eventを相互に結び付けられない状態そのものがRiskになります。

## 主要データ

| Findings | 内容 |
|---|---|
| Identity Surface | **89%**のIntrusionに関与 |
| Identity-driven Initial Access | **65%** |
| Vulnerability Exploitation | Initial Accessの**22%** |
| Multi-surface | **87%**が2つ以上 |
| 3 Surface以上 | **67%** |
| 4 Surface以上 | **43%** |
| Endpoint | 61% |
| Network | 50% |
| Human | 45% |
| Email | 27% |
| Application | 26% |
| Cloud | 20% |
| Browser | **48%**、2024年44%から上昇 |
| Fast Attack | Initial AccessからExfiltrationまで約**72分**のFastest Case群 |
| Third-party SaaS | **23%**のIncidentで悪用 |
| Preventable Gap | **90%超**のBreachでMaterialに関与 |
| Encryption-based Extortion | 前年比**15%減** |

一次情報:
- https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report
- https://www.paloaltonetworks.com/blog/2026/02/unit-42-global-ir-report/

## 詳細解説

### 1. IdentityはInitial Accessだけではない

Unit 42のIdentity論点は非常に重要です。

Identityは、

```text
Initial Access
→ Privilege Escalation
→ Lateral Movement
→ Persistence
→ Cloud/SaaS Access
→ Data Access
```

の全段階で使われます。

対象もHumanだけではありません。

- Service Account
- Workload Identity
- API Key
- OAuth Grant
- Session Token
- AI Application

などが含まれます。

### 2. Initial Accessの65%がIdentity-driven

Identity-driven Techniqueには、

- Social Engineering
- Credential Misuse
- Brute Force
- Previously Compromised Credential
- IAM Misconfiguration
- Insider Risk

などが含まれます。

Vulnerabilityも22%あるため、

> **Identity Security vs Vulnerability Management**

の二択ではなく、両方を主要Entry Pathとして設計する必要があります。

### 3. Multi-surface Attackが普通になっている

Attack Surface別では、

| Surface | 割合 |
|---|---:|
| Identity | 89% |
| Endpoint | 61% |
| Network | 50% |
| Human | 45% |
| Email | 27% |
| Application | 26% |
| Cloud | 20% |
| SecOps | 10% |
| Database | 1% |

となっています。

これは排他的Categoryではないため合計100%にはなりません。

重要なのは、87%が複数Surfaceを跨ぐことです。

Endpoint Queue、Cloud Queue、IAM Queueを別々に処理するSOCでは、同じ攻撃を別Incidentとして扱ってしまう可能性があります。

### 4. BrowserがPrimary Battleground

Browser-based Activityは48%。

Browserは、

- User Identity
- Password / Cookie
- SaaS
- Email
- Cloud Console
- Extension
- Download
- Third-party App

の交点です。

Browser Hardening、Extension Governance、Session Control、SaaS Visibilityが重要になります。

### 5. Supply Chain = Trusted Connectivity

Unit 42はSupply ChainをPackage CVEだけで捉えていません。

- SaaS Integration
- Vendor Tool
- Application Dependency
- Delegated Identity
- Service Credential

まで含めています。

23%のIncidentでThird-party SaaSが利用されたというデータは、この問題をよく表しています。

必要なのはSBOMだけでなくConnection Inventoryです。

```text
Integration
+ Owner
+ Auth Method
+ Scope
+ Data Access
+ Write Authority
+ Revoke Procedure
+ Audit Log
```

### 6. 72分のRace

Fast CaseではInitial AccessからData Exfiltrationまで約72分です。

そのためSOCはManual Investigationだけでは間に合わない可能性があります。

Automationすべきもの:

- Enrichment
- Identity Risk Correlation
- Session Revocation
- Endpoint Isolation
- Malicious Domain Blocking
- Forensic Preservation

一方、Production ShutdownなどBusiness Impactが大きいActionにはHuman Approvalが必要です。

### 7. ExtortionがEncryptionからData Theftへ

Encryption-based Extortionが15%減少し、Data Theft / Disruptionへ直接進むActorが増えています。

したがって「Encryption開始」をRansomware Detectionの主なタイミングとするのは遅いです。

より早く、

- Privilege Escalation
- Data Staging
- SaaS Export
- Large Transfer
- Archive Creation

を検知する必要があります。

## Enterprise Security Architectureへの示唆

### Identity Plane

- Human + Non-human Identity Inventory
- Standing Privilege削減
- Token/Credential Lifetime短縮
- IdP/SaaS/Cloud/Browser ContextをCorrelation

### Control Plane

- Cloud / SaaS / Backup / Infrastructure AuthorityをGraph化
- JIT / Zero TrustでImplicit Trustを削減

### Supply Chain

- PackageだけでなくTrusted ConnectionをInventory
- High-impact IntegrationへOwnerとRevoke Procedureを付与

### Telemetry

- Identity / Endpoint / Network / SaaS / Browser / Cloudを1 Timelineで再構成可能にする

### SecOps

- Alert Closure CountよりTime-to-Containを重視
- Reversible ActionをHigh-confidence Scenarioで自動化

## 優先アクション

1. Human + Non-human Identity Inventory
2. Standing Admin / Legacy Permission削除
3. SaaS/Vendor Trusted Connection Inventory
4. Browser/SaaS Telemetry追加
5. Cross-domain Investigation Schema
6. Reversible Containmentの事前承認
7. Purple TeamでExfiltration/Containment Speedを測定
8. Encryptionより前のIdentity/Staging/Exfiltration Detectionへ移行

## ATT&CK対応

- T1078 — Valid Accounts
- T1528 — Steal Application Access Token
- T1550 — Use Alternate Authentication Material
- T1098 — Account Manipulation
- T1190 — Exploit Public-Facing Application
- T1566 — Phishing

## 注意点

- IR Caseは重大Incidentへ偏ります。
- Palo Alto製品推奨とEmpirical Findingは分けて読む必要があります。
- Attack Surface Percentageは重複Categoryです。
- Speed指標はFastest Case群であり、全IncidentのMedianではありません。

## Primary Sources

- https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report
- https://www.paloaltonetworks.com/blog/2026/02/unit-42-global-ir-report/
- https://www.paloaltonetworks.com/company/press/2026/unit-42-report--ai-and-attack-surface-complexity-fuel-majority-of-breaches

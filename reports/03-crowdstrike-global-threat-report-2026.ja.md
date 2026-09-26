---
publisher: "CrowdStrike"
edition: "2026 Global Threat Report"
publication_date: "2026-02-24"
observation_period: "2025"
dataset_or_scope: "CrowdStrike Counter Adversary OperationsのThreat Intelligence / Telemetry、280超のNamed Adversary"
geography: "Global"
language: "ja"
translation_of: "03-crowdstrike-global-threat-report-2026.md"
primary_source: "https://www.crowdstrike.com/ja-jp/global-threat-report/"
last_verified: "2026-09-27"
---

# CrowdStrike 2026 Global Threat Report — 日本語解説

[English](03-crowdstrike-global-threat-report-2026.md)

## このレポートを読む意味

CrowdStrike Global Threat Reportは**Adversary-centric**なレポートです。

特に強いのは、

- Threat ActorのTradecraft
- Breakout Time
- Malware-free Activity
- Identity / Cloud / SaaSを跨ぐCross-domain Attack
- Edge Device
- State Actor / eCrime

の分析です。

2026年版では、攻撃者が「Malwareで侵入する」よりも、**Trusted IdentityでLoginし、正規ToolやCloud/SaaSを使って動く**ケースが強調されています。

## Evidence Profile

| 項目 | 内容 |
|---|---|
| 観測期間 | 2025年 |
| 情報源 | CrowdStrike Counter Adversary Operations |
| Tracked Adversary | 280超 |
| 地域 | Global |
| 強み | Breakout Speed、Adversary Tradecraft、Malware-free、Cloud/Edge |
| 注意点 | CrowdStrikeのCustomer/Telemetry Visibilityに依存 |

## エグゼクティブサマリー

中心テーマは3つです。

1. **Speed** — eCrimeのAverage Breakout Timeは29分、最速は27秒。
2. **Malware-free / Identity-based Attack** — 2025年のDetectionの82%はMalware-free。
3. **AI Dual Threat** — AI-enabled Adversary Activityは89%増加し、AI Platform自体も攻撃対象になった。

これによりSOCは「Alertを見つける」だけでは足りません。

**Seconds-to-MinutesのContainment、Identity/Cloud/SaaS Correlation、Edge Visibility**がArchitecture Requirementになります。

## 主要データ

| Findings | 内容 |
|---|---|
| Fastest eCrime Breakout | **27秒** |
| Average Breakout | **29分** |
| Breakout Speed | 2024比**65%高速化** |
| AI-enabled Adversary Activity | **89%増** |
| Malware-free Detection | **82%** |
| Pre-disclosure Zero-day Exploitation | **42%増** |
| China-nexus Exploited Vulnerability | **40%がEdge Device** |
| State-nexus Cloud-conscious Intrusion | **266%増** |
| Legitimate AI Tool Abuse | **90超の組織** |
| Criminal Forum | ChatGPTへの言及が他Modelより**550%多い** |
| Crypto | **14.6億ドル**規模のHeistをHighlight |

一次情報:
- https://www.crowdstrike.com/ja-jp/global-threat-report/
- https://www.crowdstrike.com/ja-jp/press-releases/2026-crowdstrike-global-threat-report/

## 詳細解説

### 1. 29分のBreakout TimeはArchitecture Constraint

Breakout Timeは、最初のCompromised Systemから別Systemへ攻撃者が横展開するまでの時間です。

Average 29分、Fastest 27秒という状況では、

```text
Alert
→ Queue
→ Analyst確認
→ Manual Enrichment
→ Approval
→ Containment
```

をすべて人間だけで行うのは現実的ではありません。

必要になるのは、

- Auto Enrichment
- Identity/Cloud/Endpoint Correlation
- Confidence Scoring
- Reversible Containment
- High-confidence ScenarioのPre-approval

です。

### 2. Malware-free 82%の意味

Malware-freeとは「何も使わない」ことではなく、正規機能を使うことです。

例:

- Valid Account
- Cloud API
- PowerShell
- Remote Management Tool
- SaaS Session
- Native Admin Function
- Browser Cookie

そのためDetectionの中心はFile HashからBehaviorへ移ります。

重要なのは、

> **CredentialがValidかではなく、そのAuthorityの使われ方がValidか**

です。

### 3. Edge DeviceはEndpoint Securityの外側

China-nexus Actorが悪用したVulnerabilityの40%がEdge Device向けでした。

Edge Deviceには以下の特徴があります。

- Internet-facing
- High Privilege
- EDRを入れにくい
- Patchが難しい
- Local Logが少ない
- Admin Interfaceを持つ

そのためFirewall/VPN/Network Applianceを通常のInfrastructure Inventoryから外してはいけません。

### 4. Cloud-conscious Intrusion 266%増

Cloud-consciousという言葉は重要です。

単にCloud上のVMを攻撃するのではなく、攻撃者がCloud IAM / API / Federation / Secret / SaaS Relationを理解しているという意味です。

典型的には、

```text
Stolen Identity
→ SaaS Session
→ Cloud Role
→ Secret Store
→ Workload Identity
→ Data / Infrastructure
```

というPathになります。

### 5. Zero-dayのPre-disclosure Exploitation

公開前Zero-day悪用が42%増加しています。

Patch公開後に対応するだけでは、初動を防げないケースがあります。

補完策として、

- Attack Surface Reduction
- Segmentation
- Behavior Detection
- Management Interface Restriction
- Emergency Isolation

が必要です。

### 6. AIはAcceleratorでありAttack Surface

CrowdStrikeは、

- AI-enabled Adversary Activity +89%
- Legitimate AI Toolを90超の組織で悪用
- AI Development PlatformのVulnerability悪用
- Malicious AI ServerによるData Interception

を報告しています。

つまりAI Securityには2つの側面があります。

**AIを使う攻撃者への対応**

と

**企業内AI Platform自体の保護**

です。

## Enterprise Security Architectureへの示唆

### Identity Plane

- Identity Behavior / Session ContextをPrimary Signalへ
- Human / Workload / SaaS Identityを同じGraphで見る

### Control Plane

- Cloud Role / Federation / Secret / Organization Policyを監視
- Edge ManagementをPrivileged Infrastructureとして扱う

### Telemetry Plane

- Endpoint / IdP / SaaS / Cloud / EdgeをCorrelation
- Seconds〜Minutes単位のResponseを設計

### AI Security

- AI Tool / Development Platform Inventory
- Agent / Tool Identity
- Secret / Token Handling
- AI Platform Vulnerability Management

## 優先アクション

1. Detection-to-ContainmentのSLOを定義
2. Session Revocation / Endpoint Isolation等のReversible Responseを自動化
3. EdgeとAI Development InfrastructureをVulnerability Management対象へ
4. Cloud/Identity/SaaS/Endpoint Eventを統合
5. Malware-free Admin Behavior向けThreat Huntを作る
6. AI ToolをApplication + Privileged IntegrationとしてThreat Model化

## ATT&CK対応

- T1078 — Valid Accounts
- T1550 — Use Alternate Authentication Material
- T1528 — Steal Application Access Token
- T1190 — Exploit Public-Facing Application
- T1219 — Remote Access Software
- T1098 — Account Manipulation

## 注意点

- 27秒はFastest Observationであり平均ではありません。
- Malware-freeはTool-freeではありません。
- State/eCrime AttributionはCrowdStrikeのIntelligence Assessmentです。
- CrowdStrike Visibilityを世界全体の母集団とみなすべきではありません。

## Primary Sources

- https://www.crowdstrike.com/ja-jp/global-threat-report/
- https://www.crowdstrike.com/ja-jp/press-releases/2026-crowdstrike-global-threat-report/
- https://www.crowdstrike.com/en-us/global-threat-report/

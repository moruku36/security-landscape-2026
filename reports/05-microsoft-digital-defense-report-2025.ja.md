---
publisher: "Microsoft"
edition: "Microsoft Digital Defense Report 2025"
publication_date: "2025-10-16"
observation_period: "主に2024年7月〜2025年6月。章ごとに追加の観測期間あり"
dataset_or_scope: "Microsoft Security / Identity / Cloud / Fraud / IR / Threat Intelligence Telemetry"
geography: "Global"
language: "ja"
translation_of: "05-microsoft-digital-defense-report-2025.md"
primary_source: "https://www.microsoft.com/en-us/security/security-insider/threat-landscape/microsoft-digital-defense-report-2025"
last_verified: "2026-09-27"
---

# Microsoft Digital Defense Report 2025 — 日本語解説

[English](05-microsoft-digital-defense-report-2025.md)

> このRepositoryの基準日である2026年9月26日時点では、Microsoft Digital Defense Reportの最新年次版は2025 Editionです。

## このレポートを読む意味

Microsoft Digital Defense Report（MDDR）は、単一のIncident Response Datasetだけを扱うレポートではありません。

Microsoftが持つ、

- Endpoint / Cloud Security Telemetry
- Identity Risk
- Incident Response
- Microsoft Threat Intelligence
- Digital Crimes Unit
- Fraud
- Email / Collaboration
- Nation-state Tracking

などを横断したStrategic Reportです。

Microsoftは、1日あたり約**100兆件のSecurity Signal**を処理し、約**450万件のNet-new Malware File**をBlockし、平均**3,800万件のIdentity Risk Detection**を分析しているとしています。

このScaleを背景に、MDDRはCybercrime、Identity、Cloud、AI、Nation-state、Fraud、Resilienceを一つのLandscapeとして扱っています。

## Evidence Profile

| 項目 | 内容 |
|---|---|
| 主なReporting Period | 2024年7月〜2025年6月 |
| Security Signal | 約100兆件/日 |
| Identity Risk Detection | 約3,800万件/日 |
| 情報源 | Microsoft Security / IR / Threat Intelligence / Cloud / Fraud |
| 地域 | Global |
| 強み | Strategic Trend、Identity、Cloud、AI、Cybercrime Ecosystem、Resilience |
| 注意点 | 複数Datasetのため全数値が同一母集団ではない |

## エグゼクティブサマリー

MDDR 2025の中心テーマは、**Speed / Scale / Resilience / Trust**です。

Microsoft IRでは、Motivationが判明したAttackの多くはEspionageではなくFinancially Motivatedでした。

Initial Accessも、

- Phishing / Social Engineering
- Unpatched Web Asset
- Exposed Remote Service

といった既知の経路が中心です。

一方、AI、Infostealer、Cybercrime-as-a-Service、Cloud Destruction、Workload Identityなどにより、Attack Lifecycleが高速・大規模化しています。

Enterprise Architecture上で最も重要なのは、**IdentityとCloud Resilienceを同じ問題として設計すること**です。

Human IdentityやWorkload Identityを奪われると、Cloud Control Planeへの侵害につながり、Mass DeletionやRansomwareなどBusiness Continuityへ直接影響します。

## 主要データ

| Findings | 内容 |
|---|---|
| Security Signal | 約**100兆件/日** |
| Net-new Malware Block | 約**450万件/日** |
| Identity Risk Detection | 約**3,800万件/日** |
| Espionage | Known Motivationのうち**4%** |
| Data Theft | **37%** |
| Extortion Component | **33%** |
| Ransomware / Destructive Activity | **19%** |
| Phishing / Social Engineering Initial Access | **28%** |
| Unpatched Web Asset | **18%** |
| Exposed Remote Service | **12%** |
| Password Spray | Identity Attackの**97%** |
| Cloud Incident Volume | 2025年前半の比較期間で**26%増** |
| Disruptive Cloud Campaign | **87%増** |
| AI-driven Phishing | 従来Campaignより**3倍効果的**と報告 |
| Hybrid Ransomware | **40%超** |
| AI-driven Forgery | Globalで**195%増** |
| Fraud Prevention | **40億ドル**規模を阻止 |
| Fake/Bot Account | **160万件/時**をBlock |

一次情報:
- https://www.microsoft.com/en-us/security/security-insider/threat-landscape/microsoft-digital-defense-report-2025
- https://blogs.microsoft.com/on-the-issues/2025/10/16/mddr-2025/

## 詳細解説

### 1. 日常的なAttackの中心はFinancial Motivation

Motivationが確認できたIncidentのうち、Espionage-onlyは4%でした。

一方で、

- Data Theft
- Extortion
- Ransomware
- Destructive Activity

が大きな割合を占めています。

もちろんNation-state RiskはTechnology、Government、Research、Critical Infrastructure等では非常に重要です。

ただし通常のEnterprise Baselineとしては、まず**Credential Theft / Extortion / Data Theft / Ransomware**へ耐える設計を優先する合理性があります。

### 2. Initial Accessは依然として「基本対策」で決まる

Microsoft IRでは、

- Phishing / Social Engineering 28%
- Unpatched Web Asset 18%
- Exposed Remote Service 12%

でした。

高度なAI Attackだけを見ると、現実の大多数のAttack Pathを見失います。

ClickFix、Device Code Phishingなど、Authentication Workflowを悪用する手口も増えています。

必要なのは、

- Exposure Management
- Phishing-resistant Authentication
- Secure Remote Access
- Help Desk / Recovery Hardening

です。

### 3. Identity Attackの97%がPassword Spray

MicrosoftのIdentity分析では、97%がPassword Sprayでした。

これは「高度なIdentity Attackばかりではない」という重要な示唆です。

基本的なWeak Password / Password Reuse / Legacy Authが残っていれば、大規模な攻撃を受け続けます。

Identity Architectureでは、

- Passwordless
- Phishing-resistant MFA
- Legacy Authentication削減
- Conditional Access
- Dormant Account削除
- Password Spray Detection
- Session / Token Monitoring

がBaselineになります。

### 4. Workload Identityが次のBlind Spot

Microsoftは、人間Userだけでなく、

- Application
- Service
- Script
- Automation
- Cloud Workload

といったWorkload Identityを重要なThreat Surfaceとして扱っています。

問題になるのは、

- OAuth Consent Phishing
- Device Code Phishing
- App Credential
- Secret Store Pivot
- Service Principal
- Long-lived Secret

などです。

これはCloud、CI/CD、SaaS、AI Agentに直結します。

### 5. Cloud AttackはDestructive化

Microsoft Defender for Cloudでは、2025年の前半100日と次の100日を比較した際、

- Incident Volume +26%
- Disruptive / Destructive Campaign +87%

が観測されています。

Mass DeletionやRansomwareのようなAttackは、Cloud Securityを「Misconfiguration Prevention」だけで考えられないことを示します。

必要なのは、

- Org/Tenant Guardrail
- JIT Admin
- Break-glass
- Workload Identity Governance
- Central Audit
- Deletion Protection
- Immutable Recovery

です。

### 6. Cybercrimeは分業された産業になっている

MicrosoftはCybercrime Economyを、

- Access Broker
- Ransomware Operator
- Data Extortion
- Infostealer
- Malware-as-a-Service

のような分業構造として整理しています。

Lumma StealerのようなInfostealerでBrowser CredentialやCookieが盗まれると、その情報がAccess Brokerを通じて別Actorへ渡されます。

したがってCommodity MalwareをLow Riskと決めつけるべきではありません。

### 7. AIはTool / Threat / Vulnerability

MicrosoftはAIを3つの側面で扱います。

**Attacker Tool**
- Phishing
- Deepfake
- Synthetic Identity
- Malware支援
- Scale

**Defender Tool**
- Detection
- Fraud Prevention
- Automated Response
- AI AgentによるAccount Suspension

**New Attack Surface**
- Prompt Injection
- Data Poisoning
- Model Manipulation
- Agent
- AI Application
- Sensitive Context

Enterprise側ではAIを特別扱いするより、Identity / Authorization / Data / Telemetry / Incident Responseへ統合する方が安全です。

### 8. ResilienceはCybersecurityの一部

Destructive Cloud Campaignが増えると、BCP/DRとCybersecurityを別組織で分ける設計に限界が出ます。

確認すべきなのは、

- IdPが失われてもAdminを復旧できるか
- Cloud Mass Deletionから戻せるか
- Recovery Credentialが独立しているか
- SaaS/Cloud DependencyがBCPに含まれるか

です。

## Enterprise Security Architectureへの示唆

### Identity Plane

- Passwordless / Phishing-resistantへ移行
- Workload IdentityもHumanと同じGovernanceへ
- OAuth / Device Code / App Credentialを監視

### Cloud Control Plane

- Tenant/Org RootをTier-0として保護
- JIT / Secure-by-default Guardrail
- Mass Delete / Role Change / Secret AccessをDetection

### AI Security

- AI App / Agent / Model / Connector Inventory
- Data FlowとTool Permission管理
- AgentをNon-human IdentityとしてAudit

### Recovery

- Tenant / Identity / Control Plane Lossを想定
- ProductionとRecoveryのTrustを分離

### Governance

- SecurityをIT RiskだけでなくBusiness Resilienceとして扱う
- Security / Cloud / Identity / Legal / Fraud / BCPを横断

## 優先アクション

1. Privileged WorkflowでLegacy/Weak Authenticationを排除
2. Workload Identity / Service Principal / App Grantを棚卸し
3. Cloud AdminをPIM/JIT化
4. Cloud Mass Delete / Role Change / Secret Accessを監視
5. AI Security Frameworkを策定
6. Identity/Tenant Lossを含むRecovery Exercise
7. High-confidence EventのAutomated Response
8. Cyber ResilienceをBCP Governanceへ統合

## ATT&CK対応

- T1078 — Valid Accounts
- T1110.003 — Password Spraying
- T1528 — Steal Application Access Token
- T1550 — Use Alternate Authentication Material
- T1098 — Account Manipulation
- T1190 — Exploit Public-Facing Application
- T1566 — Phishing
- T1490 — Inhibit System Recovery

## 注意点

- 複数Datasetのため全Percentageを同一母集団として扱えません。
- Microsoft由来のVisibility Biasがあります。
- 2025 Editionですが、2026年9月26日時点の最新Annual Editionとして扱っています。

## Primary Sources

- https://www.microsoft.com/en-us/security/security-insider/threat-landscape/microsoft-digital-defense-report-2025
- https://www.microsoft.com/en-us/corporate-responsibility/cybersecurity/microsoft-digital-defense-report-2025/
- https://blogs.microsoft.com/on-the-issues/2025/10/16/mddr-2025/

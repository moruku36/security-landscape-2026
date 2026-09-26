---
publisher: "IBM X-Force"
edition: "X-Force Threat Intelligence Index 2026"
publication_date: "2026-02-25"
observation_period: "2025年のIR / Investigation / Vulnerability / Dark Web / Threat Intelligence"
dataset_or_scope: "IBM X-ForceのGlobal Threat Intelligence / Incident Observation"
geography: "Global"
language: "ja"
translation_of: "06-ibm-xforce-2026.md"
primary_source: "https://www.ibm.com/jp-ja/reports/threat-intelligence"
last_verified: "2026-09-27"
---

# IBM X-Force Threat Intelligence Index 2026 — 日本語解説

[English](06-ibm-xforce-2026.md)

## このレポートを読む意味

IBM X-Forceのレポートは、

- Incident Response
- Vulnerability Exploitation
- Dark Web Credential
- Ransomware
- Supply Chain
- AI Security

を横断するのが特徴です。

2026年版の主張はM-TrendsやDBIRとかなり一致しています。

> **AIは攻撃を高速化するが、最終的に攻撃成功を決めているのは、Public Exposure、Weak Identity、Misconfiguration、Credential Theft、Excessive Trustなどの基本的なGapである。**

## Evidence Profile

| 項目 | 内容 |
|---|---|
| 観測期間 | 2025年 |
| 情報源 | X-Force IR / Investigation / Vulnerability / Dark Web / Threat Intelligence |
| 地域 | Global |
| 強み | Exploitation、Identity、Supply Chain、Ransomware Fragmentation、AI Credential |
| 注意点 | Metricごとに母集団が異なる |

## エグゼクティブサマリー

X-Forceでは、Public-facing ApplicationのExploitationがLeading Initial Accessとなり、前年比44%増加しました。

さらに、分析対象のDisclosed Vulnerabilityの56%はSuccessful ExploitationにAuthenticationを必要としないとされています。

AI Serviceも通常のEnterprise SaaSと同様にCredential Theftの対象になりました。

2025年には、30万件超のChatGPT Credential SetがDark Webで販売されているのをX-Forceが観測しています。

また、Supply Chain Incidentは過去5年で約4倍、Ransomware/Extortion Groupも増加・分散しています。

## 主要データ

| Findings | 内容 |
|---|---|
| Public-facing Exploitation | 前年比**44%増** |
| Vulnerability Exploitation | X-Forceが観測したIncidentの**40%** |
| No-auth Vulnerability | **56%** |
| ChatGPT Credential | **30万件超**がDark Webで販売 |
| Active Ransomware/Extortion Group | **49%増** |
| Distinct Extortion Group | 2024年73 → 2025年**109** |
| Publicly Disclosed Victim | 約**12%増** |
| Top 10 Group Concentration | **25%低下** |
| Major Supply Chain Incident | 5年で**約4倍** |
| Most Targeted Industry | Manufacturing |
| Geography | North Americaが約**3分の1** |

一次情報:
- https://www.ibm.com/jp-ja/reports/threat-intelligence
- https://www.ibm.com/think/x-force/threat-intelligence-index-2026-securing-identities-ai-detection-risk-management

## 詳細解説

### 1. Public-facing Exploitationが基本対策の弱さを突く

Public-facing Software / System ApplicationのExploitationが44%増加しています。

主な背景は、

- Internet-facing Assetの増加
- Patch遅延
- Misconfiguration
- Application Stack複雑化
- Forgotten Service
- Exposed Management Interface

です。

AIはExposure自体を作るわけではありませんが、DiscoveryやExploit Developmentを高速化します。

### 2. No-auth VulnerabilityをPriority Classにする

56%のDisclosed VulnerabilityがAuthentication不要でExploit可能という点は重要です。

以下を満たすVulnerabilityは優先順位を上げるべきです。

- Internet-facing
- No-auth
- Known Exploited
- Privileged Control PlaneへReachable
- Edge Device
- EDR Visibilityが弱い

これはCVSS単独より実務的です。

### 3. AI AccountがCredential Economyへ組み込まれた

30万件超のChatGPT CredentialがDark Webで販売されたという事実は、AI Serviceが既に一般的なSaaS Accountと同じ攻撃対象であることを示します。

影響はAccount Takeoverだけではありません。

- Chat History
- Source Code
- Internal Context
- Connected File
- Connector / Plugin
- Password Reuse

へ波及する可能性があります。

Approved AIはEnterprise SSOへ統合し、OffboardingやSession Controlの対象にすべきです。

### 4. Human + Non-human Identity

IBMはHuman IdentityだけでなくMachine Identityを監視する必要性を強調しています。

対象:

- Service Account
- Application Identity
- Automation
- API Key
- CI/CD Identity
- Workload Identity
- AI Agent

おすすめのInventory Fieldは、

```text
Identity
+ Owner
+ Purpose
+ Credential Type
+ Privilege
+ Target Resource
+ Last Use
+ Expiry
+ Revocation Path
```

です。

### 5. Supply Chain = Trusted Execution / Connectivity

Major Supply Chain Incidentは5年間で約4倍。

攻撃経路は、

- Developer Identity
- CI/CD Platform
- Dependency
- SaaS Integration
- Downstream Trust

です。

SBOM/SCAだけではなく、

- Release Authority
- Signing
- Provenance
- Pipeline Identity
- SaaS Connector
- Secret

を守る必要があります。

### 6. Ransomware EcosystemがFragmentation

Extortion Groupは73から109へ増え、Top 10 GroupのDominanceは低下しています。

有名なActor名やIOCに依存したDefenseは脆くなります。

より安定したDetection Targetは、

- Identity Abuse
- Privilege Escalation
- Data Staging
- Backup Manipulation
- Exfiltration
- Encryption

です。

### 7. AI Defenseの前にFoundation

IBMはAgentic SOC、AI-enhanced Identity Detection、AISPMなどを推奨しています。

ただし同じレポートのDataが示しているのは、

> **Asset / Identity / Logging / PatchというFoundationが弱いままAIを追加しても根本Riskは消えない**

ということです。

## Enterprise Security Architectureへの示唆

### Exposure

- No-auth + Internet-facing VulnerabilityをSpecial Priority
- Asset Owner / Business Serviceと紐付け

### Identity

- AI AccountをEnterprise IAMへ
- Human + Non-human Identityを統合Governance
- Static Secret削減

### DevSecOps / Supply Chain

- Developer Identity / CI/CD Authorityを保護
- Federation / Signed Release / Provenance
- SaaS/Build Trust RelationをInventory

### AI Security

- AI PlatformをSSO / Monitoring / Data Policy対象へ
- AI Credential Leakageを監視

### SecOps

- AI Automation導入前にTelemetry / Asset Identityを整える
- Actor名よりBehavior中心のDetection

## 優先アクション

1. No-auth Internet-facing Vulnerability用の緊急Remediation Lane
2. AI Account / Service Inventory
3. External Credential Exposure Monitoring
4. CI/CDをStatic KeyからFederationへ
5. Supply Chain Trust Graphを作る
6. Ransomware Behavior Detection
7. Agentic SOCにAudit / Authorization / Rollbackを持たせる

## ATT&CK対応

- T1190 — Exploit Public-Facing Application
- T1078 — Valid Accounts
- T1555 — Credentials from Password Stores
- T1528 — Steal Application Access Token
- T1550 — Use Alternate Authentication Material
- T1195 — Supply Chain Compromise
- T1486 — Data Encrypted for Impact

## 注意点

- X-ForceのMetricは同一Datasetとは限りません。
- Dark Web Credential Countは必ずしもEnterprise Compromise数ではありません。
- Industry / GeographyはIBM Visibilityに依存します。
- Product RecommendationとThreat Observationは分けて読むべきです。

## Primary Sources

- https://www.ibm.com/jp-ja/reports/threat-intelligence
- https://www.ibm.com/reports/threat-intelligence
- https://www.ibm.com/think/x-force/threat-intelligence-index-2026-securing-identities-ai-detection-risk-management
- https://newsroom.ibm.com/2026-02-25-ibm-2026-x-force-threat-index-ai-driven-attacks-are-escalating-as-basic-security-gaps-leave-enterprises-exposed

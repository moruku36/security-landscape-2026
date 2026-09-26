---
publisher: "Verizon"
edition: "2026 Data Breach Investigations Report"
publication_date: "2026-05-18"
observation_period: "2024-11-01 to 2025-10-31"
dataset_or_scope: "31,000件超のSecurity Incident、22,000件超のConfirmed Breach、145か国"
geography: "Global"
language: "ja"
translation_of: "02-verizon-dbir-2026.md"
primary_source: "https://www.verizon.com/business/ja-jp/resources/reports/dbir/"
last_verified: "2026-09-27"
---

# Verizon 2026 Data Breach Investigations Report — 日本語解説

[English](02-verizon-dbir-2026.md)

## このレポートを読む意味

Verizon DBIRは、このRepositoryの中で最も**広い母集団を持つ統計レポート**です。

第19版となる2026 DBIRは、

- 31,000件超の実際のSecurity Incident
- 22,000件超のConfirmed Data Breach
- 145か国

を分析しています。

データはLaw Enforcement、Forensics Firm、Law Firm、Cyber Insurance、情報共有組織、Verizon VTRACなど多数のContributorから提供され、VERIS Frameworkで正規化されます。

M-TrendsやUnit 42が「侵害の中で何が起きたか」を深く見るのに対し、DBIRは**どの攻撃経路が世界規模でどの程度広く発生しているか**を把握するのに向いています。

## Evidence Profile

| 項目 | 内容 |
|---|---|
| Edition | 第19版 |
| 観測期間 | 2024年11月1日〜2025年10月31日 |
| Incident | 31,000件超 |
| Confirmed Breach | 22,000件超 |
| 対象国 | 145か国 |
| Method | VERISによる正規化、多数Contributor |
| 強み | Global Prevalence、Industry/Region比較 |
| 注意点 | IncidentとBreachは異なる。地域ごとにVisibility差がある |

## エグゼクティブサマリー

2026 DBIRで最も大きな変化は、**Software Vulnerability ExploitationがStolen Credentialを抜いて最大のBreach Entry Pointになった**ことです。

一方でRansomwareは依然として非常に多く、Third-party関与も大幅に増加しています。

Human Riskも消えていません。むしろMobileを起点とするSocial EngineeringはEmailより高いClick Rateを示しています。

またGenAIは攻撃者側だけでなく企業側のAttack Surfaceも広げています。攻撃者は15種類のAttack TechniqueでGenAIを利用し、企業内ではShadow AIの利用が拡大しています。

つまり防御側の優先順位は、

> **Exposure Management + Identity + Third-party Trust + AI Governance + Recovery**

を並列で強化することです。

## 主要データ

| Findings | 内容 |
|---|---|
| Dataset | 31,000件超のIncident / 22,000件超のBreach / 145か国 |
| Vulnerability Exploitation | Breachの**31%**。Initial Access #1 |
| YoY | Vulnerability Exploitationは前年比**55%増** |
| Ransomware | Breachの**48%**に関与 |
| GenAI | **15種類**のAttack Techniqueで利用を確認 |
| Mobile Social Engineering | EmailよりMedian Successful Click Rateが**40%高い** |
| Third-party | 関与するBreachが前年比**60%増**、全体の**48%** |
| Shadow AI | Unapproved AI利用が3倍となり**45%** |
| AI Bot Traffic | 月次**21%増** |
| Critical Vulnerability Resolution | Median **43日** |

一次情報:
- https://www.verizon.com/business/ja-jp/resources/reports/dbir/
- https://www.verizon.com/about/news/breach-industry-wide-dbir-finds

## 詳細解説

### 1. Vulnerabilityが最大入口になった意味

31%という数字は、Vulnerability Managementを「月次Patch作業」だけで考えることの限界を示します。

実務ではCVSSだけではなく、

```text
Exploitability
+ Internet Exposure
+ Known Exploitation
+ Reachable Privilege
+ Business Criticality
+ Third-party Dependency
+ Compensating Control
= Remediation Priority
```

で判断した方が合理的です。

Critical Vulnerabilityの完全解消中央値が43日というデータも、DetectionとRemediationの間に大きなGapがあることを示します。

### 2. Ransomwareは依然として48%

Ransomwareが48%のBreachに関与しています。

一方、VerizonはRansom Paymentが縮小し、支払いを拒否する企業が増えていると説明しています。

これは「Ransomwareが弱くなった」という意味ではありません。

攻撃者は、

- Data Theft
- Extortion
- Operational Disruption
- Encryption

を組み合わせて圧力をかけるため、防御側にはRecoveryだけでなくData Exfiltration Detectionも必要です。

### 3. Third-partyがAttack Pathになっている

Third-party関与が60%増加し、全Breachの48%に達したという点は非常に重要です。

従来のThird-party Risk ManagementはQuestionnaire中心になりがちでした。

しかし技術的には、

```text
Vendor Identity
→ SaaS Integration
→ OAuth/API Permission
→ Enterprise Data
→ Operational Dependency
```

というAttack Pathです。

必要なのは、

- Integration Inventory
- Vendor-specific Identity
- Least Privilege
- Emergency Revoke
- Audit Log
- Security Requirementを契約へ反映

です。

### 4. Mobile Social Engineering

Mobile OriginのPhishing Simulationでは、Emailより成功Click RateのMedianが40%高いと報告されています。

Mobileでは、

- SMS
- Voice
- Messaging App
- QR Code
- MFA Fatigue
- Help Desk Interaction

が主要経路になります。

従来の「怪しいメールを開かない」教育だけでは不十分です。

Phishing-resistant MFA、Device Context、Account Recovery Verification、Help Desk Verificationまで含む必要があります。

### 5. GenAIはAttack Techniqueを高速化している

攻撃者は15種類のAttack TechniqueでGenAIを使用したとされています。

用途は、

- Reconnaissance
- Vulnerability Research
- Lure Generation
- Malware / Script支援
- Translation
- Personalization

などです。

ただし企業側で特に重要なのはShadow AIです。

Unapproved AIへ、

- Source Code
- Credential
- Internal Document
- Customer Data

が入力されると、AI Toolが新しいData Egress Channelになります。

### 6. Human vs Vulnerabilityという二択ではない

「VulnerabilityがCredentialを抜いた」ことから、Identity Securityの重要性が下がったと読むのは誤りです。

同じDBIRで、

- Mobile Social Engineering
- Third-party Trust
- Shadow AI

が大きなテーマになっています。

したがって、

> **Unauthenticated Technical EntryとAuthenticated Trust Abuseを同時に守る**

必要があります。

## Enterprise Security Architectureへの示唆

### Exposure Management

- Internet-facing AssetをContinuous Inventory化
- KEV/Active Exploitation/Reachable PrivilegeでPriority付け
- Vulnerability CountではなくRemediation AgeをKPI化

### Identity Plane

- Privileged WorkflowにPhishing-resistant MFA
- Mobile/Voiceを含むAccount Recovery対策
- PasswordだけでなくSession/Token Contextを監視

### Supply Chain / SaaS

- Third-party IntegrationをArchitecture Objectとして管理
- Owner / Permission / Log / Revoke Procedureを持つ

### AI Governance

- Approved AI Catalog
- Shadow AI Discovery
- Data Classification Policy
- AI OAuth / Connector権限管理

### Recovery

- RansomwareだけでなくVendor Outage / SaaS CompromiseもExercise対象へ

## 優先アクション

1. Internet-facing AssetのRemediation SLAを定義
2. Critical Vulnerability Resolution Timeを測定
3. Third-party Integration Inventoryを作成
4. SMS/Voice/Messagingを含むSocial Engineering対策へ拡張
5. AI Service InventoryとShadow AI Discoveryを導入
6. Ransomware Recovery ExerciseをIdentity/SaaS依存込みで実施
7. DBIRのGlobal Dataと自社Attack Pathを分けてRisk判断する

## ATT&CK対応

- T1190 — Exploit Public-Facing Application
- T1078 — Valid Accounts
- T1566 — Phishing
- T1528 — Steal Application Access Token
- T1486 — Data Encrypted for Impact
- T1490 — Inhibit System Recovery

## 注意点

- DBIRではIncidentとConfirmed Breachを明確に区別しています。
- Contributorや地域によってVisibilityが異なります。
- Industry/Region固有のPercentageをそのまま自社へ当てはめるべきではありません。
- 大規模統計に強い一方、個々の攻撃のForensic DetailはM-Trends/Unit 42の方が詳しいです。

## Primary Sources

- https://www.verizon.com/business/ja-jp/resources/reports/dbir/
- https://www.verizon.com/business/resources/reports/dbir/
- https://www.verizon.com/about/news/breach-industry-wide-dbir-finds

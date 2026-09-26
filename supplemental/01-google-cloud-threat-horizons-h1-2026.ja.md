---
publisher: "Google Cloud"
edition: "Cloud Threat Horizons H1 2026"
publication_date: "2026-03-10"
observation_period: "主に2025年下半期"
language: "ja"
translation_of: "01-google-cloud-threat-horizons-h1-2026.md"
primary_source: "https://cloud.google.com/security/report/resources/cloud-threat-horizons-report-h1-2026"
last_verified: "2026-09-27"
---

# Google Cloud Threat Horizons H1 2026 — 日本語解説

[English](01-google-cloud-threat-horizons-h1-2026.md)

## 追加する価値

Core 7でやや薄かった**Cloud-native Attack PathとForensic Readiness**を補うレポートです。Google Cloud発行ですが、Cloud Provider全般へ適用できるRecommendationを意図しています。

## 主要データ

- H2 2025のCloud Initial AccessではThird-party Software Exploitationが**44.5%**で最多。H1は**2.9%**。
- Weak/Missing Credentialは**47.1% → 27.2%**。
- RCEは**2.9% → 13.6%**。
- Misconfigurationは**29.4% → 21%**。
- Exposed Sensitive UI/APIは**11.8% → 4.9%**。
- Major Cloud/SaaS Incidentの**83%**でIdentity IssueがInitial Accessに関与。
- Cloud-related Incidentの**73%**でDataがTarget。
- Vishingは該当分析の**17%**。
- CI/CDのOIDC Trustと過剰権限を悪用したGitHub→Cloud Pivotを解説。

## Architecture上の意味

重要なのは次の4点です。

1. Cloud SecurityはIAMだけでなく**Application Exposure**の問題にもなっている。
2. CI/CD Federationは短命Credentialでも、Roleが過剰なら危険。
3. Incident発生後に権限やLogを準備するのでは遅い。
4. Snapshot / Log / Volatile DataのEvidence Collectionは自動化できる。

推奨Model:

```text
Detection
→ 事前準備済みIR Identity
→ Snapshot / Memory / Log保全
→ Timeline統合
→ Context-aware Containment
```

## 優先アクション

- Organization ScopeのIR Roleを事前作成
- Productionと別Blast RadiusへAudit Log保存
- CI/CD OIDC TrustをPrivileged Federation Pathとして管理
- Third-party FrameworkをCloud Exposure Management対象へ
- Snapshot / Log Collectionを自動化
- Auto Scaling / Reboot / Delete時にもEvidenceを残せるか検証

## Core Reportとの関係

M-TrendsがEnterprise IR全体を見せるのに対し、Threat Horizonsは**Cloud Initial Access / OIDC / CI/CD / Forensics**を具体化します。

## Primary Sources

- https://cloud.google.com/security/report/resources/cloud-threat-horizons-report-h1-2026
- https://cloud.google.com/blog/products/identity-security/cloud-ciso-perspectives-new-threat-horizons-report-highlights-current-cloud-threats

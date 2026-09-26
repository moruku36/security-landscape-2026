---
publisher: "Cloudflare / Cloudforce One"
edition: "2026 Cloudflare Threat Report"
publication_date: "2026-03-03"
observation_period: "主に2025年 + 2026 Outlook"
language: "ja"
translation_of: "03-cloudflare-threat-report-2026.md"
primary_source: "https://blog.cloudflare.com/2026-threat-report/"
last_verified: "2026-09-27"
---

# Cloudflare 2026 Threat Report — 日本語解説

[English](03-cloudflare-threat-report-2026.md)

## 追加する価値

Cloudflareは通常のIR Reportで薄くなりやすい、**Internet-scale Traffic / SaaS Abuse / Session Token / Deepfake Insider / DDoS**を補います。

特に重要なのは、攻撃が「Break in」から**「Log inしてTrusted Serviceの中で活動する」**方向へ移っているという整理です。

## 主要テーマ

1. AIによるHigh-velocity Attack
2. Critical InfrastructureへのPre-positioning
3. Over-privileged SaaS Integration
4. Trusted Cloud Toolの悪用
5. Deepfake Remote Worker
6. Session Token TheftによるMFA Bypass
7. Mail Relay Identity Gap
8. Hyper-volumetric DDoS

## 代表的なデータ

- DDoSは**31.4 Tbps**規模まで到達。
- 該当TelemetryではLoginの**63%**が既に別経路でCompromiseされたCredentialを含む。
- Login Attemptの**94%**がBot起点。
- 分析Emailの約**46%**がDMARC Failure。
- Over-privileged SaaS Integrationにより1つのAPI Compromiseが多数顧客へ波及するRiskを指摘。

## Architecture上の意味

### IdentityはMFAの後も続く

AttackerがSession Cookie/Tokenを盗めば、MFA済み状態を再利用できます。

そのため必要なのは、

- Session Lifetime
- Device/Context Binding
- Token Revocation
- Post-auth Behavior Detection
- Browser / Endpoint Hygiene

です。

### Trusted SaaSがAttack Infrastructureになる

Google Calendar、Dropbox、GitHub、Google Drive、Teams、Azure Web Apps、S3など、正規ServiceがHosting/C2/Deliveryへ使われると、Reputation-based Filterだけでは難しくなります。

### Remote Worker OnboardingはSecurity Boundary

Deepfake / Fraudulent Identity / Laptop Farmにより、採用からEndpoint EnrollmentまでがIdentity Securityになります。

### DDoSはHuman Responseの外側

31.4 Tbps級では人間が見てから止める設計は成立しません。Always-on Mitigationが必要です。

## 優先アクション

- Session/Token TelemetryをIdentity Detectionへ
- SaaS-to-SaaS Grant Inventory
- Trusted SaaSを使う異常C2/Data Staging検知
- Remote Worker Identity Proofing強化
- DMARC/DKIM/SPFとRelay再検証
- Critical ServiceへAlways-on DDoS Defense

## Primary Sources

- https://blog.cloudflare.com/2026-threat-report/
- https://www.cloudflare.com/lp/threat-report-2026/

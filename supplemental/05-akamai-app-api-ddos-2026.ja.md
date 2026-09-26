---
publisher: "Akamai"
edition: "State of the Internet / Security 2026 — Prepare for the Convergence Crisis"
publication_date: "2026-03-17"
observation_period: "主に2023-2025 Trend + 2026 Analysis"
language: "ja"
translation_of: "05-akamai-app-api-ddos-2026.md"
primary_source: "https://www.akamai.com/blog/security/apps-apis-ddos-2026-industrialization-cyberattack-campaigns"
last_verified: "2026-09-27"
---

# Akamai SOTI 2026 — Apps / APIs / AI / DDoS 日本語解説

[English](05-akamai-app-api-ddos-2026.md)

## 追加する価値

Core 7で薄かった**API Security**を補うSourceです。API Abuse、Web Attack、DDoS、DNS、AI-assisted Developmentが一体化している点を扱います。

## 主要データ

- AkamaiはAPIをReport上の**No.1 Attack Surface**として位置付け。
- Layer 7 DDoS Surgeは2年間で**104%増**。
- Web Attack Volumeは2023→2025で**73%増**。
- Shadow / Zombie APIによるData Leak / Authorization Risk。
- Multi-layer / Multi-protocol DDoS。
- Security ReviewなしのVibe CodingがMisconfigurationをProductionへ持ち込むRisk。

## Architecture上の意味

### API Inventory = Asset Inventory

最低限、

- Owner
- Environment
- Auth Method
- Data Class
- Consumer
- Internet Exposure
- Version / Deprecation
- Rate Limit
- Behavioral Baseline

を持つべきです。

### WAFだけでは不足

API Abuseは正しいHTTP SyntaxでBusiness Logicを悪用する場合があります。

必要なのは、

- Identity / Context
- Object Authorization
- Sequence / Volume Anomaly
- Schema
- Sensitive Data Access

の観測です。

### AI CodingはPipeline Controlで守る

AI Codingを禁止するより、SAST / SCA / IaC Scan / Test / Review / PolicyをCI/CDへ移す方が実務的です。

## 優先アクション

- API Inventory
- Shadow/Zombie API Detection
- CI/CDへAPI Authorization / Behavior Test
- L3/L4/L7 DDoS Control
- Dangling DNS/CNAME Monitoring
- AI-generated CodeのSecurity Gate
- API TelemetryをIdentity/Application Observabilityへ統合

## Primary Source

- https://www.akamai.com/blog/security/apps-apis-ddos-2026-industrialization-cyberattack-campaigns

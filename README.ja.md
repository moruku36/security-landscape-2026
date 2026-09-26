# Security Landscape 2026

> 2026年9月26日時点の主要セキュリティ年次レポートとカンファレンスを横断し、Cloud / Identity / SecOps / DevSecOps / Recovery / AIを含むEnterprise Security Architectureへ落とし込んだリファレンス。

[English](README.md)

## このリポジトリの目的

一般的な脅威レポート要約は「何が起きたか」で終わりがちです。このリポジトリでは、さらに次を扱います。

- 独立した複数ソースで繰り返される傾向は何か
- どのAttack Pathが構造的に重要になっているか
- 何をTier-0相当のSecurity Planeとして設計すべきか
- MITRE ATT&CK / NIST CSF 2.0 / CIS Controls v8.1へどう対応するか
- Azure / AWS / GCP / SaaS / CI/CD / AI Agentで何を実装すべきか
- Machine-speed attackへ対応するため、どのTelemetryとDetectionが必要か

ベンダーの優劣比較ではなく、**複数の観測結果をEnterprise Architectureへ変換すること**が目的です。

## 2026年の中心命題

2026年の変化は「AIが従来型攻撃を置き換えた」ことではありません。むしろ、**すでに有効だったAttack Pathの各段階をAIと自動化が高速・大規模化している**ことです。

```mermaid
flowchart LR
    A[Internet-facing<br/>Human interaction] --> B[Credential<br/>Session<br/>Token]
    B --> C[Identity / SaaS / Cloud<br/>Control Plane]
    C --> D[Edge / Hypervisor /<br/>Management Plane]
    D --> E[Data theft<br/>Ransomware<br/>Recovery denial]
    AI[AI / Automation] -. 高速化 .-> A
    AI -. 高速化 .-> B
    AI -. 高速化 .-> C
    AI -. 高速化 .-> D
    AI -. 高速化 .-> E
```

横断すると特に重要なのは次の7点です。

1. **Identityが実質的なPerimeterになった。** 人間だけでなく、Service Account、OAuth Grant、Session Token、API Key、AI Agentまで攻撃面。
2. **Internet-facing / Edgeが主要入口。** VPN、Firewall、Web Asset、Network Appliance、Management Interfaceが重要。
3. **Cloud / SaaS / Supply Chainが一体化。** Trusted IntegrationやDelegated Accessが横展開経路になる。
4. **攻撃速度が圧縮されている。** 高確度イベントを人間だけで処理するSOCモデルでは間に合わないケースが増える。
5. **RecoveryはSecurity Plane。** Backupが存在することと、IdentityやHypervisorまで侵害された状態から復旧できることは別。
6. **製品数よりTelemetry Coverage。** IdP、Cloud Control Plane、SaaS、Edge、Hypervisor、Backup、CI/CD、AI Toolを横断して観測できることが重要。
7. **AI SecurityはIdentity / Authorization Engineeringへ。** モデル選定より、Agent Identity、Tool Permission、Token、Audit、Human Approval Boundaryが基礎になる。

## コンテンツ

### 年次レポート — 詳細日本語版 / English

- Mandiant M-Trends 2026 — [日本語](reports/01-m-trends-2026.ja.md) / [EN](reports/01-m-trends-2026.md)
- Verizon 2026 DBIR — [日本語](reports/02-verizon-dbir-2026.ja.md) / [EN](reports/02-verizon-dbir-2026.md)
- CrowdStrike 2026 Global Threat Report — [日本語](reports/03-crowdstrike-global-threat-report-2026.ja.md) / [EN](reports/03-crowdstrike-global-threat-report-2026.md)
- Unit 42 2026 Global Incident Response Report — [日本語](reports/04-unit42-global-ir-2026.ja.md) / [EN](reports/04-unit42-global-ir-2026.md)
- Microsoft Digital Defense Report 2025 — [日本語](reports/05-microsoft-digital-defense-report-2025.ja.md) / [EN](reports/05-microsoft-digital-defense-report-2025.md) — 2026-09-26時点の最新年次版
- IBM X-Force Threat Intelligence Index 2026 — [日本語](reports/06-ibm-xforce-2026.ja.md) / [EN](reports/06-ibm-xforce-2026.md)
- ENISA Threat Landscape 2026 — [日本語](reports/07-enisa-threat-landscape-2026.ja.md) / [EN](reports/07-enisa-threat-landscape-2026.md)
- [Report Index / Evidence Guide](reports/README.md)

### カンファレンス

- [RSAC 2026](conferences/01-rsac-2026.md)
- [Black Hat USA 2026](conferences/02-black-hat-usa-2026.md)
- [DEF CON 34](conferences/03-def-con-34.md)
- [FIRST CTI 2026](conferences/04-first-cti-2026.md)
- [FIRSTCON26](conferences/05-firstcon26.md)

### 横断分析・設計

- [Consensus Matrix](analysis/cross-report-trends.md)
- [Attack Paths](analysis/attack-paths.md)
- [2026 Timeline](analysis/trend-timeline.md)
- [Enterprise Architectureへの示唆](analysis/enterprise-architecture-implications.md)
- [Enterprise Architect Perspective](analysis/enterprise-architect-perspective.md)
- [Reference Architecture](architecture/reference-architecture.md)
- [Security Planes](architecture/security-planes.md)
- [Identity Architecture](architecture/identity.md)
- [Recovery Architecture](architecture/recovery.md)
- [Azure / AWS / GCP Control Mapping](architecture/cloud-controls.md)
- [Telemetry Architecture](architecture/telemetry.md)

### Framework / AI / Operations

- [MITRE ATT&CK](frameworks/mitre-attack.md)
- [NIST CSF 2.0](frameworks/nist-csf.md)
- [CIS Controls v8.1](frameworks/cis-controls.md)
- [NIST × CIS × 2026 Threat Crosswalk](frameworks/nist-cis-crosswalk.md)
- [AI Security Architecture](ai-security/README.md)
- [AI Agent Security](ai-security/agent-security.md)
- [MCP Security](ai-security/mcp-security.md)
- [Detection Engineering](operations/detection-engineering.md)
- [2026 Security Priorities](operations/security-priorities.md)

## 設計モデル

```mermaid
flowchart TB
    G[Governance / Risk]
    I[Identity Plane<br/>誰・何が実行できるか]
    C[Control Plane<br/>何が基盤を変更できるか]
    D[Data Plane<br/>何を読み出せるか]
    R[Recovery Plane<br/>独立して復旧できるか]
    T[Telemetry Plane<br/>全Planeの行動を再構成できるか]

    G --> I
    G --> C
    G --> D
    G --> R
    T --- I
    T --- C
    T --- D
    T --- R
```

2026年を一言で表すなら、

> **Endpoint Securityの延長として考えるのではなく、Identity、Cloud/SaaS Control Plane、Edge/Virtualization、Recovery、Privileged AI Agentを独立したSecurity Boundaryとして再設計する。**

ということです。

## Evidenceの扱い

- **Major** — レポートの主要テーマ・主要発見
- **Observed** — 明確な観測はあるが中心テーマではない
- **Not emphasized** — 今回確認した範囲では主要論点ではない

各ベンダーの母集団・地域・Incident Definitionが異なるため、統計値そのものをベンダー間ランキングには使いません。

詳細は [SOURCES.md](SOURCES.md)、年次レポートの言語別一覧は [reports/README.md](reports/README.md)、更新方法は [CONTRIBUTING.md](CONTRIBUTING.md) を参照してください。

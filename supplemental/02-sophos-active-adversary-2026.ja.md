---
publisher: "Sophos X-Ops"
edition: "Active Adversary Report 2026"
publication_date: "2026-02-24"
observation_period: "2024-11-01 to 2025-10-31"
scope: "70か国・34業種・661件のIR/MDR Case"
language: "ja"
translation_of: "02-sophos-active-adversary-2026.md"
primary_source: "https://www.sophos.com/ja-jp/press/press-releases/sophos-active-adversary-report-2026-identity-attacks-dominate-as-threat-groups-proliferate"
last_verified: "2026-09-27"
---

# Sophos Active Adversary Report 2026 — 日本語解説

[English](02-sophos-active-adversary-2026.md)

## 追加する価値

Sophosは**Identity、営業時間外Attack、AD到達速度、Firewall Telemetry、Log Retention**という運用寄りの視点を補ってくれます。

## 主要データ

- Incidentの**67%**がIdentity-related Root Cause。
- Initial AccessはVulnerability Exploitation **16%**、Brute Force **15.6%**。
- **59%**のCaseで重要箇所にMFAがなかった。
- Median Dwell Timeは**3日**。
- Intrusion後、AD Server到達まで**3.4時間**。
- Ransomware Payloadの**88%**、Data Exfiltrationの**79%**が営業時間外。
- Retention不足によるMissing Logは前年比2倍。
- FirewallのDefault Retentionが7日、場合によって24時間というCaseもあった。
- CVE起点Incidentの3分の2超が同一SonicWall Vulnerabilityに集中。Confirmed Exploited VulnerabilityではPatch/Advisory公開からExploitationまでの中央値が**322日**。

## Architecture上の意味

### Identity

Identity CompromiseはIAM Teamだけの問題ではなく、Incident Root Causeの中心です。MFAも「導入済み」ではなくCoverage / Method / Recovery Flowまで見ます。

### 24x7 Response

Night/Weekendに攻撃が集中するなら、SOC Architectureには24x7のDetection/Containment能力が必要です。

### Log Retention

Firewall Logが7日しかなければ、Deviceが正常でもForensicsは失敗します。RetentionはStorage CostではなくSecurity Controlです。

## 優先アクション

- Privileged / External AccessへPhishing-resistant MFA
- Identity Infrastructureの24x7 Monitoring
- Edge/Firewall LogをCentral保存
- Initial Access→AD/Control Plane到達時間をPurple Teamで測定
- Edge Patch後のExposure解消をVerify
- Off-hoursでもContainment可能な権限とRunbookを準備

## Primary Sources

- https://www.sophos.com/ja-jp/press/press-releases/sophos-active-adversary-report-2026-identity-attacks-dominate-as-threat-groups-proliferate
- https://www.sophos.com/en-us/blog/2026-sophos-active-adversary-report

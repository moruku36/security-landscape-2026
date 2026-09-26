---
publisher: "Google Cloud / Mandiant"
edition: "M-Trends 2026"
publication_date: "2026-03-23"
observation_period: "2025-01-01 to 2025-12-31"
dataset_or_scope: "Mandiantによる50万時間超のインシデント調査"
geography: "Global"
language: "ja"
translation_of: "01-m-trends-2026.md"
primary_source: "https://cloud.google.com/security/resources/m-trends-executive-edition"
last_verified: "2026-09-27"
---

# Mandiant M-Trends 2026 — 日本語解説

[English](01-m-trends-2026.md)

## このレポートを読む意味

M-Trendsは、実際に侵害を受けた組織にMandiantが入り、インシデントレスポンスを行った結果をもとにした年次レポートです。2026年版は、2025年に実施された**50万時間超の最前線のインシデント調査**を基礎にしています。

そのため、DBIRのように世界全体の「発生割合」を広く見るレポートとは役割が異なります。M-Trendsが強いのは、侵入後に攻撃者がどのように動き、どこに潜伏し、どこを壊し、なぜ検知できなかったかという**内部侵害の実態**です。

2026年版で特に重要なのは、攻撃者の動きが二極化していることです。

- 金銭目的の攻撃者は、Initial Accessから次の攻撃グループへの引き継ぎを極端に高速化し、短時間で恐喝・暗号化・復旧妨害へ進む。
- サイバーエスピオナージや北朝鮮ITワーカー系では、Edge機器やVirtualizationなど可視性の弱い場所に長期間潜伏する。

したがって、防御側には**秒〜分単位のContainment能力**と、**数カ月〜1年以上を追跡できる長期Telemetry**の両方が必要になります。

## Evidence Profile

| 項目 | 内容 |
|---|---|
| 観測期間 | 2025年1月1日〜12月31日 |
| 母集団 | Mandiant Consultingが対応した標的型攻撃・侵害調査 |
| 規模 | 50万時間超のインシデント調査 |
| 地域 | Global |
| 強み | Initial Access、Dwell Time、Recovery Denial、Infrastructure Persistence |
| 注意点 | 全企業を無作為抽出した統計ではなく、Mandiantへ調査依頼が来た案件が中心 |

## エグゼクティブサマリー

M-Trends 2026の中心メッセージは、**Endpoint中心の防御だけでは足りない**ということです。

脆弱性悪用は6年連続で最大の初期侵入経路でした。一方、Voice Phishingが急増し、従来のメールセキュリティだけでは止めにくい対話型攻撃が目立ちました。

さらに、攻撃者はEDRを導入できないEdge機器、Hypervisor、SaaS Token、Identity Service、Backup Infrastructureなどへ活動領域を広げています。

ランサムウェアも単純な暗号化ではなく、**Recovery Denial**へ進化しています。Identity、Virtualization、Backup、Cloud StorageのRecovery Pointなど、復旧に必要な仕組み自体を破壊し、「払うか、ゼロから再構築するか」という状態に追い込む戦術が目立ちます。

AIは重要な要素ですが、Mandiantは「2025年の侵害の大半がAIによって直接引き起こされたわけではない」と明示しています。AIは主として偵察、Social Engineering、Malware Development、侵害後作業を高速化するForce Multiplierです。

## 主要データ

| Findings | 内容 |
|---|---|
| Exploit | 初期感染の**32%**。6年連続1位 |
| Voice Phishing | **11%**まで上昇し2位 |
| Email Phishing | 2024年14% → 2025年**6%** |
| Ransomware関連 | Initial VectorはPrior Compromiseが**30%**で最多 |
| Global Median Dwell Time | 11日 → **14日** |
| Espionage / DPRK IT Worker | Median Dwell Time **122日** |
| Initial AccessからSecondary Groupへのhandoff | 中央値**22秒**。2022年は8時間超 |
| BRICKSTORM関連 | 平均Dwell Time **393日** |
| 内部検出 | 2024年43% → 2025年**52%** |
| Target Industry | High Tech **17%**、Finance **14.6%** |
| Threat Cluster | Financially motivated 41%、Espionage 16% |
| Malware Type | Backdoor 36%、Downloader 11%、Ransomware 10%、Dropper 10%、Credential Stealer 9% |

一次情報:
- https://cloud.google.com/security/resources/m-trends-executive-edition
- https://cloud.google.com/blog/ja/topics/threat-intelligence/m-trends-2026?hl=ja

## 詳細解説

### 1. Initial Accessは「メール対策」からExposure + Identityへ

脆弱性悪用が32%で最大ということは、Internet-facing Assetの管理が依然として最優先です。

ただし同時にVoice Phishingが11%へ上昇しています。これは攻撃者がメールフィルタを避け、電話やHelp Deskとの会話を通じて以下を狙うことを意味します。

- MFA Reset
- Password Reset
- Device Registration
- Account Recovery
- SaaS Access
- Temporary Access Passなどの認証補助経路

つまりIdentity Securityは、PasswordとMFAだけでは完結しません。**Recovery FlowそのものをPrivileged Workflowとして保護する必要があります。**

### 2. 22秒のhandoffはSOCの優先順位を変える

Initial Access PartnerからSecondary Threat Groupへの引き継ぎ中央値が22秒まで短縮しています。

これにより、Malvertising、Fake Browser Update、Commodity Downloader、単一Endpoint感染のような「低Severityに見えるAlert」が、短時間でRansomwareやData Theftへつながる可能性があります。

従来のSOCでは、

```text
Alert発生
→ Severity判定
→ Queue
→ Analyst確認
→ Escalation
→ Containment
```

という流れになりがちですが、22秒の世界では遅すぎます。

必要なのは、**「現時点の被害」だけでなく「このFootholdが次に何へ接続されるか」**を評価する考え方です。

### 3. RansomwareはRecovery Denialへ

M-Trends 2026で特に重要なのがこの変化です。

攻撃対象はFileだけではありません。

- Identity Service
- AD Certificate Services
- Hypervisor
- Virtualization Management
- Backup Platform
- Backup Catalog
- Cloud Backup Object
- Recovery Point
- Break-glass Account

Production AdminとBackup Adminが同じIdentity Planeに依存している場合、1回のIdentity侵害でProductionとRecoveryを同時に失う可能性があります。

したがって、

> **Backupがあることと、Recoveryできることは別**

です。

### 4. HypervisorはTier-0 Asset

HypervisorはGuest OSの下に位置し、通常のEDRを入れられないケースが多いです。

攻撃者がHypervisorを取ると、

- VM DiskをCloneしてGuest OSへログインせずDataを取得
- AD DatabaseやSecretをOffline Diskから抽出
- Rogue VMを作成
- Hypervisor ShellにPersistenceを設置
- Datastore単位で暗号化
- Guest OSのRebuild後もPersistenceを残す

といった攻撃が可能です。

そのためHypervisor管理はDomain ControllerやCloud Organization Rootと同等に扱うべきです。

### 5. Edge / Network DeviceはEDRの死角

Firewall、VPN、Router、Network ApplianceはInternet-facingでありながらEndpoint Agentを入れにくい典型的なBlind Spotです。

MandiantはNative Shell、Packet Capture、In-memory Malware、Built-in Admin Functionなどの悪用を指摘しています。

必要なのは、

- Device Inventory
- Vulnerability Ownership
- Admin LogのCentral Forwarding
- Configuration Change Monitoring
- Network Appliance専用IR Playbook
- 長期Log Retention

です。

### 6. SaaS IntegrationがSupply Chain化している

SaaS時代のThird-party Riskは、Vendor Assessmentだけでは不十分です。

攻撃者は、

```text
Third-party SaaS
→ OAuth Token / PAT / API Key
→ Customer SaaS
→ Data / Admin Function
```

という経路を使えます。

Password Reset後もTokenが有効であれば、MFAを通さずに継続アクセスできます。

したがって、

- OAuth App Inventory
- API Key / Service Principal Ownership
- End-user Consent Restriction
- Token Lifetime
- Integration Revocation
- SaaS Audit

が必要になります。

### 7. AI Tool自体が侵害後の攻撃手段になる

QUIETVAULTは、侵害端末上にAI CLI Toolが存在するか確認し、それを利用して設定ファイルやGitHub/NPM Tokenを検索する動作が観測されています。

これはDeveloper向けAI Toolを単なる生産性ツールとして扱えないことを示します。

AI CLIがCode、Environment Variable、Repository、Credentialへアクセスできるなら、そのToolはDeveloper Security / Endpoint SecurityのThreat Modelに含める必要があります。

## Enterprise Security Architectureへの示唆

### Identity Plane

- MFA Reset / Account RecoveryをPrivileged Operationとして保護
- SaaS Grant / Service Principal / Remote Contractorを継続監査
- Session / Token TheftをPassword Compromiseと同等以上に扱う

### Control Plane

- Hypervisor / Backup / Edge Management / Cloud RootをTier-0相当へ
- Corporate AdminとInfrastructure Adminを分離
- Standing Privilegeを減らしPIM/JIT化

### Recovery Plane

- Production AuthorityとRecovery Authorityを分離
- Immutable / Offline Recovery Copyを維持
- Primary IdP喪失を前提にRestore Test

### Telemetry Plane

- IdP / SaaS / Edge / Hypervisor / Backup / Cloud AuditをSIEMへ
- 90日より長い高価値Log Retentionを設計
- Log Source停止自体をDetection対象にする

### SecOps

- Low-impact Initial AccessとIdentity / Cloud / SaaS EventをCorrelation
- High-confidenceなInitial Accessに対しReversible Containmentを事前承認
- Native Admin Toolの異常利用をThreat Hunt

## 優先アクション

1. Internet-facing / Edge Asset Inventoryを完成させる
2. Help DeskのIdentity Verificationを強化する
3. HypervisorとBackup AdministrationをCorporate Identityから可能な範囲で分離する
4. Network / Identity / Virtualization / SaaS / Backup Logを長期集中保存する
5. OAuth App、API Key、Service Principal、SaaS Integrationを棚卸しする
6. Identity / Hypervisor喪失を含むRecovery Exerciseを実施する
7. Developer AI ToolをCredential/Secret Threat Modelへ含める
8. Commodity Malwareを「Lowだから後回し」にしないSOC設計へ変更する

## ATT&CK対応

- T1190 — Exploit Public-Facing Application
- T1078 — Valid Accounts
- T1528 — Steal Application Access Token
- T1550 — Use Alternate Authentication Material
- T1098 — Account Manipulation
- T1490 — Inhibit System Recovery
- T1486 — Data Encrypted for Impact

[MITRE ATT&CK Crosswalk](../frameworks/mitre-attack.md)も参照。

## 注意点

- Mandiant案件は、高Impact・複雑な侵害に偏る可能性があります。
- DBIRやCrowdStrike等と母集団が異なるため、Percentageを直接比較すべきではありません。
- 一部のInfrastructure/Persistence論点は特定Campaignから得られたものであり、全企業での発生割合を示すものではありません。

## Primary Sources

- https://cloud.google.com/security/resources/m-trends-executive-edition
- https://cloud.google.com/blog/ja/topics/threat-intelligence/m-trends-2026?hl=ja
- https://cloud.google.com/blog/topics/threat-intelligence/m-trends-2026

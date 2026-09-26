# Verizon 2026 Data Breach Investigations Report (DBIR)

Source: https://www.verizon.com/business/resources/reports/dbir/

## Positioning

多数の組織から集めた侵害データを統計的に見るレポート。単一ベンダーのIR観測より母集団が広く、経営層への説明やrisk prioritizationに向く。

2026 editionの対象期間は2024-11-01〜2025-10-31。

## Key findings

- Breachの31%がsoftware vulnerabilityから始まり、stolen credentialを上回った。
- Breachの48%にransomwareが関与。
- Generative AIが15%のattack techniquesを増強していると整理。
- Mobile social engineeringはtraditional emailより高い成功率を示す傾向が強まり、smishing/vishingへの移行が目立つ。

## Interpretation

DBIRは「Human riskだけ見ていればよい」という古い説明から、**Vulnerability / Internet-facing asset / Mobile / AI augmentation**を組み合わせた説明へ移っている。

重要なのは、phishing trainingをやめることではなく、次の二つを同時に強くすること。

- Human/Identity controls: phishing-resistant MFA、helpdesk verification、session protection
- Exposure controls: asset inventory、patch SLA、external attack surface、third-party visibility

## Architecture implication

脆弱性管理を「月次パッチ運用」ではなく、internet exposureとexploitabilityを使った優先順位付けに変える必要がある。CVSSだけでなく、KEV/EPSS、外部公開の有無、Identityへの到達可能性を加味する設計が合う。

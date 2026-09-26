# Security priorities — 2026 backlog

## P0 — do first

| Priority | Action | Why |
|---|---|---|
| P0 | Internet-facing asset inventory + rapid patch SAA | DBIR/M-Trends/IBMでexploitが主要入口 |
| P0 | Phishing-resistant MFA for privileged/high-risk users | Identity-driven intrusion対策 |
| P0 | IdP / Edge / Hypervisor / Backup logsをcentralize | EDR外のblind spot対策 |
| P0 | Tier-0 management plane segmentation | Edge/virtualization/identity compromiseのblast radius制限 |
| P0 | Immutable backup + restore exercise | Ransomware/Recovery denial対策 |
| P0 | OAuth / API / machine identity inventory | SaaS/Cloud/AIの新しい横展開経路 |

## P1 — build the operating model

| Priority | Action | Why |
|---|---|---|
| P1 | Detection-as-Code | CTI→Detection→IRの閉ループ化 |
| P1 | JIT privilege / standing admin削減 | Credential compromise時のimpact縮小 |
| P1 | SaaS integration ownership + revoke runbook | Supply-chain incident時の即時切断 |
| P1 | Cloud entitlement review | Over-permissionの縮小 |
| P1 | Edge/virtualization threat hunting | Long-term persistence対策 |
| P1 | External attack surface + KEV/EPSS prioritization | CVSS-only運用から脱却 |

## P2 — prepare for agentic security

| Priority | Action | Why |
|---|---|---|
| P2 | AI agent identity and tool policy | Agentic AIを通常IAMへ統合 |
| P2 | MCP / connector allowlist | Tool poisoning / over-broad access対策 |
| P2 | AI red team / prompt-tool abuse scenario | New attack path検証 |
| P2 | AI/API telemetry to SIEM | Living-off-AIの可視化 |
| P2 | Reversible automated containment | Machine-speed attackへの対応 |

## Suggested KPI shift

古いKPI:

- Number of alerts
- Number of vulnerabilities closed
- EDR deployment rate

2026向けKPI:

- Internet-facing critical exposure age
- Privileged standing access count
- Unowned OAuth/SaaS integrations
- Mean time to contain high-confidence intrusion
- Tier-0 telemetry coverage
- Restore success / RTO validation rate
- Machine identity with long-lived credential

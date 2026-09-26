# Security priorities — 2026 architecture backlog

This backlog translates the cross-source findings into an implementation sequence.

## P0 — close high-impact attack paths

| Action | Why | Primary plane |
|---|---|---|
| Internet-facing asset inventory + rapid exploit-informed remediation | Exploitation is a leading initial-access path across DBIR, M-Trends, IBM and other sources. | Control |
| Phishing-resistant MFA for privileged/high-risk users | Reduces credential-led identity compromise. | Identity |
| High-assurance helpdesk/recovery verification | Vishing and account-recovery abuse can bypass strong sign-in controls. | Identity |
| Centralize IdP / Edge / Hypervisor / Backup audit logs | Removes non-EDR blind spots. | Telemetry |
| Segment Tier-0 management planes | Limits blast radius from identity/edge/virtualization compromise. | Control |
| Immutable recovery + full restore exercise | Addresses ransomware and recovery-denial paths. | Recovery |
| OAuth / API / machine-identity inventory | Makes SaaS/cloud/AI delegated authority visible. | Identity |

## P1 — build the operating model

| Action | Why |
|---|---|
| Detection-as-Code lifecycle | Turns CTI into repeatable detection and response. |
| JIT privilege / reduce standing admin | Limits impact of stolen valid credentials. |
| SaaS integration ownership + revoke runbook | Enables rapid supply-chain/trusted-connectivity containment. |
| Cloud entitlement review | Reduces over-permissioned human and machine identities. |
| Edge/virtualization threat hunting | Addresses long-lived persistence outside normal EDR. |
| External attack surface + KEV/EPSS/context prioritization | Moves beyond CVSS-only queues. |
| CI/CD workload federation | Removes static cloud credentials from pipelines. |
| Recovery-plane change monitoring | Detects destructive preparation before full impact. |

## P2 — prepare for privileged agents

| Action | Why |
|---|---|
| Agent identity and tool policy | Integrates agentic AI into normal IAM governance. |
| Approved MCP/connector registry | Reduces server/tool supply-chain and over-broad access risk. |
| Prompt/tool abuse red-team scenarios | Tests new trust boundaries. |
| AI/API telemetry to SIEM | Makes agent/tool activity investigable. |
| Reversible automated containment | Matches machine-speed attack windows without handing destructive authority to automation. |
| Token audience/scope validation | Limits credential replay and confused-deputy paths. |

## KPI shift

Traditional KPI:

- number of alerts;
- number of vulnerabilities closed;
- EDR deployment rate.

2026-oriented KPI:

- age of internet-facing critical exploitable exposure;
- standing privileged-access count;
- ownerless/high-scope OAuth and SaaS integrations;
- mean time to contain high-confidence intrusion;
- Tier-0 telemetry coverage;
- restore success and validated RTO/RPO;
- count/percentage of long-lived machine credentials;
- percentage of privileged agents with explicit tool policy and auditable identity;
- time to revoke a compromised SaaS/MCP integration.

## Suggested 90-day sequence

### Days 0–30

- Inventory internet-facing critical services.
- Inventory privileged human/non-human identities.
- Identify Tier-0 management and recovery planes.
- Verify logging coverage.
- Test emergency token/session/integration revocation.

### Days 31–60

- Remove high-risk standing privilege.
- Fix critical external exposures.
- Establish SaaS/OAuth ownership.
- Build recovery-loss scenarios.
- Implement first high-confidence automated containment playbooks.

### Days 61–90

- Add edge/hypervisor hunting.
- Add AI/MCP registry and telemetry requirements.
- Map top attack paths to ATT&CK and tested detections.
- Establish NIST/CIS target-profile tracking.
- Run an end-to-end exercise: exploit/identity → cloud/SaaS → recovery impact.
# Enterprise Architect perspective

This chapter translates the 2026 threat landscape for architects and senior engineers working across **Enterprise IT, Cloud, Security, DevSecOps, and Operations**. The goal is to connect threat evidence to design decisions, operating models, and measurable controls—not to prescribe a single vendor stack.

## 1. Hybrid identity architecture is the highest-leverage control domain

Multiple reports converge on identity, credentials, sessions, tokens, and delegated trust.

Architecture questions:

- Do we inventory human and non-human identities?
- Can Entra/AD, AWS, GCP, SaaS, and CI/CD trust paths be reconstructed?
- Where does standing privilege remain?
- Can privileged access be made eligible/JIT?
- Which OAuth grants and service identities are ownerless?
- Can sessions or tokens be revoked quickly?
- Are recovery identities separate from production identities?

## 2. Cloud Control Plane Security should be designed as a graph

Do not reduce "cloud security" to workload vulnerability scanning.

The attack graph includes:

```text
IAM
↕
Organization / Tenant policy
↕
Audit logs
↕
CI/CD identity
↕
SaaS integration
↕
Vendor connectivity
↕
Workload / data
```

The cloud control plane determines what can be changed, delegated, exposed, or recovered.

## 3. SecOps maturity is source coverage × detection lifecycle

A SIEM purchase is not the same as detection capability.

Priority log sources:

- IdP / authentication.
- Cloud audit.
- SaaS audit.
- Edge appliance.
- Hypervisor.
- EDR/XDR.
- CI/CD.
- Backup platform.
- AI-agent and tool invocation.

Then build a lifecycle:

```text
Threat intelligence
→ hypothesis
→ detection-as-code
→ validation
→ response
→ incident feedback
→ control improvement
```

## 4. Exposure management should reduce attack paths, not close tickets

A more useful prioritization model than severity alone:

```text
Technical severity
+ Internet exposure
+ Known exploitation
+ Privilege reachable
+ Business criticality
+ Compensating controls
+ Recovery dependency
= Remediation priority
```

## 5. DevSecOps and OSS security should include identity and provenance

Supply-chain defense is broader than package CVEs.

Architecture scope:

- SCA and dependency pinning.
- SBOM.
- Provenance and attestation.
- Secret scanning.
- Build-time behavior review.
- CI/CD identity least privilege.
- Short-lived federation from pipelines.
- Release signing.
- Trusted integration inventory.

## 6. AI engineering security should become a platform standard

The "allow or ban AI" phase is no longer enough.

Enterprise standards should cover:

- Approved model/service catalog.
- Data classification and allowed destinations.
- Agent identity.
- Tool allowlist.
- MCP/server trust.
- Prompt/tool telemetry.
- Secret/token isolation.
- Human approval boundary.
- Revocation and incident response.

## Architect mental model

Use four security planes plus one cross-cutting telemetry plane:

```text
Identity Plane   — who or what may act?
Control Plane    — what can change infrastructure and policy?
Data Plane       — what can be read, modified, or exfiltrated?
Recovery Plane   — can the business recover independently?

Telemetry Plane  — can activity across all four be reconstructed?
```

This model is intentionally cloud-provider neutral and can then be implemented with Azure, AWS, GCP, SaaS, and on-premises controls.

## Domain-by-domain architect lens

| Domain | 2026 design question | Architecture artifact | Useful evidence / KPI |
|---|---|---|---|
| Enterprise IT | Which management systems become Tier-0 if compromised? | Trust-boundary / admin-path diagram | Tier-0 assets with isolated admin path and centralized audit |
| Cloud | Can a compromised identity traverse org/tenant boundaries or assume broader roles? | Cloud identity + organization-policy model | Standing privilege, external trust, workload key count, guardrail exceptions |
| Security / SecOps | Can an incident be reconstructed across endpoint, identity, cloud, SaaS, edge, virtualization, and recovery? | Telemetry coverage matrix + detection catalogue | High-value source coverage, MTTD/MTTC, investigation data-source count |
| DevSecOps | Can CI/CD or dependency trust modify production without short-lived, attributable authority? | Software supply-chain trust model | Federated pipeline identities, signed releases, secret age, provenance coverage |
| Operations / Resilience | Can the service recover after identity/control-plane compromise? | Recovery dependency graph + restore runbook | Restore success, RTO validation, recovery credential isolation |
| AI Engineering | Is every agent/tool action attributable, authorized, bounded, and revocable? | Agent identity + tool authorization model | Unowned agents/connectors, broad scopes, human-gated destructive actions |

## Design review questions

A cross-domain architecture review should be able to answer:

1. **Identity:** Which human and non-human identities can reach each critical control plane?
2. **Privilege:** Which of those permissions are standing, and which can be JIT/time-bound?
3. **Trust:** Which third-party, OAuth, SaaS, CI/CD, and federation relationships can transitively grant access?
4. **Exposure:** Which Internet-facing assets lead to privileged or high-value paths?
5. **Telemetry:** Can each privilege-changing or recovery-destructive action be reconstructed?
6. **Containment:** Which high-confidence actions can be safely automated and reversed?
7. **Recovery:** Can trusted administration be restored without depending on the compromised production plane?
8. **Ownership:** Does every service account, integration, agent, and exception have a responsible owner and review date?

## Suggested architecture deliverables

For a practical enterprise program, the threat landscape should produce concrete artifacts:

- Tier-0 / high-trust asset inventory;
- human + non-human identity inventory;
- SaaS/OAuth/vendor integration register;
- external attack-surface inventory;
- multi-cloud organization guardrail baseline;
- telemetry coverage matrix;
- ATT&CK-linked detection catalogue;
- recovery-plane trust diagram;
- CI/CD and OSS supply-chain trust model;
- AI agent / MCP registry and authorization policy;
- prioritized remediation backlog tied to attack-path reduction.

The value of the annual reports is highest when they change one of these artifacts, not when they only add another slide to a threat briefing.

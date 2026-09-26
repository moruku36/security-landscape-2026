# Enterprise Architect perspective

This chapter translates the 2026 threat landscape for architects working across **Enterprise IT, Cloud, Security, DevSecOps, and Operations**.

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
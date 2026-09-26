# Azure / AWS / GCP control mapping

This table maps provider-neutral architecture goals to representative native controls. It is **not** a claim of exact feature equivalence.

| Architecture goal | Microsoft Azure / Entra | AWS | Google Cloud |
|---|---|---|---|
| Workforce federation | Microsoft Entra ID | IAM Identity Center / external IdP federation | Workforce Identity Federation / Cloud Identity federation |
| JIT privileged access | Entra Privileged Identity Management | Temporary role sessions + centralized federation / approval workflow as designed | Privileged Access Manager |
| Phishing-resistant access policy | Conditional Access authentication strengths | MFA + federated IdP policy; enforce session/role design centrally | Federated IdP policy + IAM / access-context controls |
| Workload identity without static keys | Managed identities / workload identity federation | IAM roles / STS temporary credentials | Workload Identity Federation / attached service accounts |
| Detect excessive / external permissions | Entra ID Governance / access reviews + Azure IAM review patterns | IAM Access Analyzer | IAM Recommender / Policy Intelligence patterns |
| Organization guardrails | Management groups / Azure Policy | AWS Organizations / SCPs | Resource hierarchy / Organization Policy |
| Context-aware access | Conditional Access | IAM policy conditions / identity-provider context | Access Context Manager / IAM Conditions |
| Audit control plane | Azure Activity Log + Entra audit/sign-in logs | CloudTrail + service logs | Cloud Audit Logs |
| Cloud security posture | Defender for Cloud and policy ecosystem | Security Hub CSPM and Config ecosystem | Security Command Center and Organization Policy ecosystem |

## Design notes

### Microsoft

Microsoft Entra PIM is explicitly designed to reduce standing privileged access and provide as-needed/JIT activation. Authentication strength in Conditional Access can require phishing-resistant MFA for selected users/apps.

Primary references:

- https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/
- https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-guests-mfa-strength
- https://learn.microsoft.com/en-us/entra/id-governance/identity-governance-overview

### AWS

AWS IAM best practices explicitly recommend:

- federation and temporary credentials for human users;
- temporary role credentials for workloads;
- least privilege;
- IAM Access Analyzer for external/public access and unused access.

Primary references:

- https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html
- https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-findings.html
- https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html

### Google Cloud

Google Cloud differentiates:

- **Workforce Identity Federation** for user/workforce identities.
- **Workload Identity Federation** for non-human/workload identities.
- **Privileged Access Manager** for temporary JIT elevation.
- **Organization Policy** for centralized configuration guardrails.
- **Access Context Manager** for context-based access controls and service perimeters.

Primary references:

- https://cloud.google.com/iam/docs/workforce-identity-federation
- https://cloud.google.com/iam/docs/workload-identity-federation
- https://cloud.google.com/iam/docs/pam-overview
- https://cloud.google.com/organization-policy/overview
- https://cloud.google.com/access-context-manager/docs/overview

## Provider-neutral architecture pattern

```mermaid
flowchart LR
    IDP[Enterprise IdP] --> FED[Federation]
    FED --> TEMP[Short-lived session]
    TEMP --> JIT[JIT privilege]
    JIT --> CP[Cloud control plane]
    CP --> LOG[Central audit telemetry]
    LOG --> DET[Detection / response]
```

The goal is not to standardize product names. The goal is to standardize **identity lifetime, privilege lifetime, policy boundary, evidence, and revocation behavior** across providers.

## Multi-cloud review checklist

- Is workforce identity federated rather than duplicated?
- Are workload credentials short-lived?
- Is standing admin minimized?
- Can external and unused access be identified?
- Are organization-level guardrails centrally managed?
- Are audit logs centrally retained and correlated?
- Can privileged sessions be revoked quickly?
- Do CI/CD systems use workload federation rather than static cloud keys?
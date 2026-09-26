# Cloud / Security / DevSecOps focus

この章は、Enterprise IT × Cloud × Security × Operationsを横断するアーキテクト向けに、2026年の動向を実務へ変換したもの。

## Most relevant areas

### 1. Hybrid Identity Architecture

最重要。M-Trends、Unit 42、Microsoft、IBMの方向が重なる。

見るべきもの:

- Human + Non-Human Identity inventory
- Entra/AD/Cloud IAM/SaaS Identity間のtrust path
- PIM/JIT
- FIDO2/passkey
- OAuth grant
- Session/token
- Break-glass identity

### 2. Cloud Control Plane Security

Workload vulnerabilityだけでなく、IAM・Organization/Tenant policy・Audit log・CI/CD・SaaS integrationを一つのattack graphとして見る。

### 3. Detection Engineering / SecOps Platform

SIEM導入そのものより、source coverageとdetection lifecycleが重要。

重点log source:

- IdP / authentication
- Cloud audit
- SaaS audit
- Edge appliance
- Hypervisor
- EDR/XDR
- CI/CD
- Backup platform
- AI agent/tool invocation

### 4. Exposure Management

脆弱性管理をticket処理からattack-path reductionへ移す。

```text
Severity
+ Internet exposure
+ Known exploitation
+ Privilege reachable
+ Business criticality
+ Compensating controls
= Priority
```

### 5. DevSecOps / OSS Supply Chain

Unit 42のtrusted connectivityとtransitive dependency問題はDevSecOpsに直結。

- SCA / dependency pinning
- SBOM
- Provenance / attestation
- Secret scanning
- Build-time behavior review
- CI/CD identity least privilege
- Release signing

### 6. AI Engineering Security

2026年はAIを「利用禁止/許可」の二択で扱う段階を過ぎた。

Enterprise向けには、

- Approved model/service catalog
- AI data classification
- Agent identity
- Tool allowlist
- MCP/server trust
- Prompt/tool telemetry
- Secret/token isolation
- Human approval boundary

をplatform standardとして設計した方がよい。

## Architect's mental model

2026年に一番使いやすい見方は、Security Productを並べることではなく、4つのplaneで考えること。

```text
Identity Plane     — who/what may act?
Control Plane      — what can change infrastructure?
Data Plane         — what can be read/exfiltrated?
Recovery Plane     — can the business recover independently?
```

これにTelemetry Planeを横断させる。

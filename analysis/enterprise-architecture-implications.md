# Enterprise Security Architecture implications

## 1. Redefine Tier-0

従来のDomain Controllerだけでなく、以下をTier-0相当として扱う。

- Enterprise IdP / federation
- Privileged Access platform
- Hypervisor / virtualization management
- Backup / recovery control plane
- Network security management plane
- Cloud organization / tenant root
- CI/CD signing / release authority
- AI agent orchestration with privileged tool access

## 2. Identity-first, but not Identity-only

Identityはperimeterだが、Identityだけ守ればよいわけではない。

設計原則:

- Phishing-resistant MFA
- JIT/JEA/PIM
- Conditional / continuous access evaluation
- Short-lived credential
- Machine identity inventory
- OAuth / API grant governance
- Session/token monitoring

## 3. Treat edge and virtualization as first-class telemetry

Endpoint agentが置けない装置を「監視できないので仕方ない」にしない。

- Admin/auth log forwarding
- Configuration change monitoring
- Management-plane network segmentation
- Dedicated admin path / PAW
- Firmware / appliance exposure management

## 4. Cloud/SaaS inventory must include relationships

Asset inventoryをVMやSaaS名の一覧で終わらせない。

必要なのはrelationship graph。

```text
User ↔ Role ↔ SaaS ↔ OAuth App ↔ API ↔ Data
             ↕
        Cloud Account
             ↕
       CI/CD / Vendor
```

攻撃者が使うのは「資産」より「信頼関係」。

## 5. Design recovery as an isolated security plane

Backup is not recovery.

- Immutable / offline recovery point
- Separate identity boundary
- Separate admin credential
- Restore test
- Hypervisor/IdP loss scenario
- SaaS configuration/data recovery

## 6. Detection-as-Code + Automated containment

数十秒単位のattack progressionに対し、完全手動SOCは構造的に不利。

Automationの順序は、

1. enrich
2. correlate
3. score confidence
4. contain reversible actions
5. escalate destructive/high-impact action to human

が現実的。

## 7. AI Agent = privileged software identity

AI Agent securityではモデル精度より先に以下を確認する。

- Who is the agent?
- What tools can it call?
- What data can it read/write?
- Can it delegate to another agent?
- Can it create/refresh credentials?
- Is every action attributable and auditable?
- Can a human stop/revoke it quickly?

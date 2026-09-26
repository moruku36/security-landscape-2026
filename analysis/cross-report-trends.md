# Cross-report trend matrix

## 2026 consensus map

| Theme | M-Trends | DBIR | CrowdStrike | Unit 42 | Microsoft | IBM | ENISA | Conference signal |
|---|---|---|---|---|---|---|---|---|
| AI accelerates offense | Strong | Strong | Strong | Strong | Strong | Strong | Emerging | RSAC / Black Hat / DEF CON / FIRST |
| Identity / credential / token | Strong | Strong | Strong | Very strong | Strong | Strong | Medium | Black Hat / RSAC / FIRST |
| Vulnerability / exposed asset | Strong | Very strong | Strong | Strong | Strong | Very strong | Strong | Black Hat / DEF CON |
| Edge / network appliance | Very strong | Medium | Very strong | Strong | Medium | Medium | Medium | DEF CON |
| Cloud / SaaS | Strong | Strong | Very strong | Very strong | Very strong | Strong | Medium | RSAC / Cloud Village / FIRST |
| Supply chain / trusted connectivity | Strong | Strong | Medium | Very strong | Strong | Medium | Strong | RSAC / Black Hat / FIRST |
| Ransomware / extortion | Strong | Very strong | Strong | Strong | Strong | Strong | Very strong | FIRST / DEF CON |
| Recovery / resilience | Very strong | Strong | Strong | Strong | Very strong | Strong | Very strong | RSAC / FIRST |
| Machine-speed response | Very strong | Strong | Very strong | Very strong | Strong | Strong | Medium | Black Hat / FIRST |
| Long-term / non-EDR telemetry | Very strong | Medium | Strong | Strong | Strong | Medium | Medium | FIRST / DEF CON |

## The key synthesis

各社は違うデータを見ているが、2026年は次のattack pathへ収束している。

```text
Internet-facing / Human interaction
            ↓
   Credential / Session / Token
            ↓
 Identity + SaaS + Cloud Control Plane
            ↓
 Edge / Virtualization / Management Plane
            ↓
 Data theft / Ransomware / Recovery denial
```

そしてAIは、このattack pathそのものを置き換えるというより、各フェーズのfrictionを下げている。

## What changed from the classic model

### Classic

```text
Phishing → Endpoint malware → AD → Data / Ransomware
```

### 2026

```text
Exploit / Vishing / OAuth / Session Theft
  → IdP / Cloud / SaaS
  → Edge / Hypervisor / RMM / Vendor Integration
  → Data + Identity + Backup + Recovery
```

「Endpoint侵害を中心に世界を見る」モデルではcoverageが不足する。

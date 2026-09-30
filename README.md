# Security Landscape 2026

> A 2026-09-26 snapshot of major cybersecurity reports and conferences, translated into an Enterprise Security Architecture reference for Cloud, Identity, SecOps, DevSecOps, Recovery, and AI systems.

[日本語版](README.ja.md)

## Why this repository exists

Most annual threat reports answer **what happened**. This repository also asks:

- Which findings are repeated across independent data sets?
- Which attack paths are becoming structurally important?
- Which security planes should architects treat as Tier 0?
- How do the findings map to MITRE ATT&CK, NIST CSF 2.0, and CIS Controls v8.1?
- What should change in Azure, AWS, GCP, SaaS, CI/CD, and AI-agent environments?
- Which telemetry and detection capabilities are required to respond at machine speed?

The result is not a vendor ranking. It is a cross-source architecture synthesis.

### Architecture lens

The repository intentionally uses a **generalist architect lens across Enterprise IT × Cloud × Security × DevSecOps × Operations**. Threat intelligence is translated into trust boundaries, identity design, control-plane guardrails, telemetry, recovery, and operating-model decisions.

## 2026 thesis

The central 2026 shift is not that AI replaced traditional intrusion methods. Instead, **AI and automation are reducing friction across already-effective attack paths**.

```mermaid
flowchart LR
    A[Internet-facing assets<br/>Human interaction] --> B[Credentials<br/>Sessions<br/>Tokens]
    B --> C[Identity / SaaS / Cloud<br/>Control Plane]
    C --> D[Edge / Hypervisor /<br/>Management Plane]
    D --> E[Data theft<br/>Ransomware<br/>Recovery denial]
    AI[AI / Automation] -. accelerates .-> A
    AI -. accelerates .-> B
    AI -. accelerates .-> C
    AI -. accelerates .-> D
    AI -. accelerates .-> E
```

Seven themes recur across the 2026 evidence base:

1. **Identity is the practical perimeter.** Human and non-human identities, OAuth grants, session tokens, API keys, service accounts, and agents are all part of the attack surface.
2. **Internet-facing and edge infrastructure is a high-value entry point.** VPNs, firewalls, web assets, network appliances, and exposed management interfaces remain critical.
3. **Cloud, SaaS, and supply chain are converging.** Trusted integrations and delegated access can become lateral-movement paths.
4. **Attack speed is compressing.** Human-only triage and response models are increasingly too slow for high-confidence events.
5. **Recovery is a security plane.** Backup existence is not equivalent to recoverability when identity, hypervisor, and recovery infrastructure are compromised together.
6. **Telemetry blind spots matter more than product count.** IdP, cloud control plane, SaaS, edge, hypervisor, backup, CI/CD, and AI-tool activity need to be observable.
7. **AI security is becoming identity and authorization engineering.** Agent identity, tool permissions, token handling, auditability, and human approval boundaries are more fundamental than model choice alone.

## Repository map

### Evidence — detailed reports in English and Japanese

- Mandiant M-Trends 2026 — [EN](reports/01-m-trends-2026.md) / [JA](reports/01-m-trends-2026.ja.md)
- Verizon 2026 DBIR — [EN](reports/02-verizon-dbir-2026.md) / [JA](reports/02-verizon-dbir-2026.ja.md)
- CrowdStrike 2026 Global Threat Report — [EN](reports/03-crowdstrike-global-threat-report-2026.md) / [JA](reports/03-crowdstrike-global-threat-report-2026.ja.md)
- Unit 42 2026 Global Incident Response Report — [EN](reports/04-unit42-global-ir-2026.md) / [JA](reports/04-unit42-global-ir-2026.ja.md)
- Microsoft Digital Defense Report 2025 — [EN](reports/05-microsoft-digital-defense-report-2025.md) / [JA](reports/05-microsoft-digital-defense-report-2025.ja.md) — latest annual edition available as of 2026-09-26
- IBM X-Force Threat Intelligence Index 2026 — [EN](reports/06-ibm-xforce-2026.md) / [JA](reports/06-ibm-xforce-2026.ja.md)
- ENISA Threat Landscape 2026 — [EN](reports/07-enisa-threat-landscape-2026.md) / [JA](reports/07-enisa-threat-landscape-2026.ja.md)
- [Report index and evidence guide](reports/README.md)

### Supplemental 2026 research

- [Google Cloud Threat Horizons H1 2026](supplemental/01-google-cloud-threat-horizons-h1-2026.md) — cloud / CI/CD / forensic readiness
- [Sophos Active Adversary 2026](supplemental/02-sophos-active-adversary-2026.md) — identity / IR / off-hours / log retention
- [Cloudflare Threat Report 2026](supplemental/03-cloudflare-threat-report-2026.md) — SaaS / token theft / trusted cloud / DDoS
- [Cloudflare DDoS H1 2026](supplemental/04-cloudflare-ddos-h1-2026.md) — availability / DNS / hyper-volumetric DDoS
- [Akamai Apps/APIs/DDoS 2026](supplemental/05-akamai-app-api-ddos-2026.md) — API / app / DNS / AI coding
- [Akamai Agentic Threat Landscape 2026](supplemental/06-akamai-agentic-threat-landscape-2026.md) — agent / MCP / browser / nonhuman identity
- [Check Point Cyber Security Report 2026](supplemental/07-check-point-cyber-security-report-2026.md) — AI / MCP / edge / hybrid attack paths
- [Fortinet Global Threat Landscape 2026](supplemental/08-fortinet-global-threat-landscape-2026.md) — exploit velocity / network / legitimate tools
- [Japan active cyber defense: October 2026 implementation](supplemental/09-japan-active-cyber-defense-2026.md) — staged commencement / critical infrastructure / reporting readiness (verified 2026-09-30)
- [Supplemental research index](supplemental/README.md)

### Conferences

- [RSAC 2026](conferences/01-rsac-2026.md)
- [Black Hat USA 2026](conferences/02-black-hat-usa-2026.md)
- [DEF CON 34](conferences/03-def-con-34.md)
- [FIRST CTI 2026](conferences/04-first-cti-2026.md)
- [FIRSTCON26](conferences/05-firstcon26.md)

### Cross-source analysis

- [Consensus matrix](analysis/cross-report-trends.md)
- [Attack paths](analysis/attack-paths.md)
- [2026 timeline](analysis/trend-timeline.md)
- [Enterprise architecture implications](analysis/enterprise-architecture-implications.md)
- [Enterprise architect perspective](analysis/enterprise-architect-perspective.md)

### Architecture

- [Reference architecture](architecture/reference-architecture.md)
- [Security planes](architecture/security-planes.md)
- [Identity architecture](architecture/identity.md)
- [Recovery architecture](architecture/recovery.md)
- [Azure / AWS / GCP control mapping](architecture/cloud-controls.md)
- [Telemetry architecture](architecture/telemetry.md)

### Framework crosswalks

- [MITRE ATT&CK](frameworks/mitre-attack.md)
- [NIST CSF 2.0](frameworks/nist-csf.md)
- [CIS Controls v8.1](frameworks/cis-controls.md)
- [NIST CSF 2.0 × CIS Controls v8.1 × 2026 Threat Crosswalk](frameworks/nist-cis-crosswalk.md)

### AI security

- [AI Security Architecture](ai-security/README.md)
- [Agent security](ai-security/agent-security.md)
- [MCP security](ai-security/mcp-security.md)

### Operations

- [Detection engineering](operations/detection-engineering.md)
- [2026 security priorities](operations/security-priorities.md)

## Architecture model

```mermaid
flowchart TB
    G[Governance / Risk]
    I[Identity Plane<br/>Who or what may act?]
    C[Control Plane<br/>What can change infrastructure?]
    D[Data Plane<br/>What can be read or exfiltrated?]
    R[Recovery Plane<br/>Can the business recover independently?]
    T[Telemetry Plane<br/>Can activity across every plane be reconstructed?]

    G --> I
    G --> C
    G --> D
    G --> R
    T --- I
    T --- C
    T --- D
    T --- R
```

The practical architecture takeaway is:

> **Treat identity, cloud/SaaS control planes, edge/virtualization management, recovery, and privileged AI-agent orchestration as first-class security boundaries—not as extensions of endpoint security.**

## Evidence model

The cross-report matrix uses explicit evidence labels rather than subjective scores:

- **Major** — a primary theme or prominent finding in the source.
- **Observed** — supported by the source but not a dominant theme.
- **Not emphasized** — not a meaningful focus in the reviewed material.

Vendor statistics are not ranked against one another because each report uses a different observation population, methodology, geography, and incident definition.

## Scope and methodology

- Snapshot date: **2026-09-26 JST**
- Primary and official sources are preferred.
- Important statistics are paired with their source and observation period inside each report note.
- Cross-source conclusions require repeated evidence or an explicit analytical rationale.
- Conference notes summarize official programs, recaps, and representative technical sessions; they are not verbatim coverage of every talk.
- Framework mappings are architectural crosswalks, not claims that the source reports themselves used those frameworks.
- See [SOURCES.md](SOURCES.md) for the source register and [reports/README.md](reports/README.md) for the bilingual report index.

## Maintenance

This is intended to remain reproducible rather than become a one-off summary. See [CONTRIBUTING.md](CONTRIBUTING.md) for the update workflow.


## When to update next

The repository is intended to be **event-driven first, calendar-driven second**.

### Recommended next review window: late October–November 2026

Do a focused refresh when one of the following happens:

- Microsoft publishes the next annual Digital Defense Report;
- a major vendor publishes a materially revised 2026 threat/IR report;
- a major post-conference research release changes the current architecture conclusions;
- MITRE ATT&CK, NIST CSF, CIS Controls, MCP, or major cloud-provider security guidance changes in a way that affects the mappings in this repository.

If none of those triggers occur, the next scheduled refresh should be **December 2026–January 2027** to close out the 2026 landscape.

### Annual refresh window: February–May 2027

The next large rebuild should happen when the 2027 annual-report cycle begins. At that point:

1. add the new annual editions;
2. keep the 2026 editions for historical comparison;
3. create a 2026 → 2027 change analysis;
4. update the consensus matrix and architecture implications only where the evidence changes;
5. review whether the current five-plane architecture still explains the new attack paths.

## What to do next

Recommended backlog, in order:

1. **Year-end 2026 synthesis**  
   Add a short document that separates:
   - trends that strengthened through the year;
   - trends that remained stable;
   - trends that were over-hyped or did not materially change enterprise architecture.

2. **2026 → 2027 delta analysis**  
   Create a version-to-version comparison instead of rewriting history. Track changes in:
   - initial access;
   - identity abuse;
   - cloud/SaaS activity;
   - edge/virtualization;
   - ransomware/recovery denial;
   - AI-assisted attack and defense;
   - response speed.

3. **Conference bilingual expansion**  
   Add Japanese editions for RSAC, Black Hat, DEF CON, FIRST CTI, and FIRSTCON using the same bilingual pattern as `reports/`.

4. **Source-change automation — implemented**  
   The repository now includes a monthly [security source monitor](monitor/README.md) that checks official landing pages for next-edition markers and opens a GitHub Issue when a likely refresh is detected. Continue expanding the registry for frameworks and cloud-security guidance as needed.

5. **Release/version discipline**  
   Add `CHANGELOG.md` and GitHub releases/tags for meaningful repository snapshots, for example:
   - `2026-09-snapshot`
   - `2026-year-end`
   - `2027-q1-refresh`

6. **Keep architecture conclusions evidence-driven**  
   Do not add a new security domain simply because it is fashionable. Add or change architecture only when multiple independent sources, or a strong technical development, justify it.

## Update checklist

For each refresh:

- [ ] Check all seven core annual-report publishers for a newer edition.
- [ ] Review the supplemental-report monitor results.
- [ ] Check major conference follow-up material and published research.
- [ ] Re-verify important statistics and observation periods.
- [ ] Update English and Japanese report editions together.
- [ ] Update [SOURCES.md](SOURCES.md).
- [ ] Re-run the cross-report consensus matrix.
- [ ] Review ATT&CK / NIST / CIS mappings.
- [ ] Review Azure / AWS / GCP implementation references.
- [ ] Review AI-agent / MCP security guidance.
- [ ] Re-run link-check CI.
- [ ] Record the change in a release note or changelog.

The goal is to keep this repository useful as a **living architecture reference**, not to maximize update frequency.


---
publisher: "Akamai"
edition: "State of the Internet / Security 2026 — Prepare for the Convergence Crisis"
publication_date: "2026-03-17"
observation_period: "Primarily 2023-2025 trend data with 2026 analysis"
scope: "Application, API, DNS, and DDoS telemetry"
language: "en"
primary_source: "https://www.akamai.com/blog/security/apps-apis-ddos-2026-industrialization-cyberattack-campaigns"
last_verified: "2026-09-27"
---

# Akamai SOTI 2026 — Apps, APIs, AI and DDoS

[日本語版](05-akamai-app-api-ddos-2026.ja.md)

## Why it belongs here

Akamai fills a major gap in the core set: **API security as an enterprise attack surface**, plus the convergence of API abuse, web attacks, DDoS, DNS risk, and AI-assisted application development.

## Key findings

- Akamai describes APIs as the **number-one attack surface** in the report's framing.
- Layer 7 DDoS surges increased **104% over two years**.
- Web attack volume increased **73% from 2023 through 2025**.
- Shadow and zombie APIs create data-leak and authorization risk.
- DDoS increasingly mixes layers and protocols.
- "Vibe-coded" applications can introduce production misconfiguration and insecure-by-default behavior when AI-generated code is shipped without adequate review.

## Architecture interpretation

### API inventory is now asset inventory

An organization cannot secure APIs it does not know exist. API governance should include:

- owner;
- environment;
- authentication method;
- data class;
- consumers;
- internet exposure;
- version/deprecation status;
- rate limits;
- behavioral baseline.

### WAF alone is not enough

Traditional web controls are optimized for known request patterns and signatures. API abuse often uses legitimate syntax with malicious business logic.

Detection needs:

- identity/context;
- object/resource authorization;
- abnormal sequence/volume;
- schema deviations;
- sensitive-data access patterns.

### AI-generated application development changes DevSecOps risk

AI-assisted coding increases delivery speed, which can increase the speed at which misconfigurations and unsafe patterns reach production. The architecture answer is not banning AI coding; it is **moving validation into pipelines**.

## Recommended actions

- Create an API inventory with ownership and lifecycle state.
- Detect shadow/zombie APIs.
- Add API authorization and behavior testing to CI/CD.
- Protect L3/L4/L7 with coordinated DDoS controls.
- Monitor dangling DNS/CNAME records and ownership changes.
- Require security tests for AI-generated code before production.
- Tie API telemetry into identity and application observability.

## Primary sources

- https://www.akamai.com/blog/security/apps-apis-ddos-2026-industrialization-cyberattack-campaigns

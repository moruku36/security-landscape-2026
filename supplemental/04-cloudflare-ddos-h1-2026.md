---
publisher: "Cloudflare / Cloudforce One"
edition: "DDoS Threat Report H1 2026"
publication_date: "2026-08-11"
observation_period: "2026-01-01 to 2026-06-30"
scope: "Cloudflare network DDoS telemetry"
language: "en"
primary_source: "https://blog.cloudflare.com/ddos-threat-report-2026-h1/"
last_verified: "2026-09-27"
---

# Cloudflare DDoS Threat Report H1 2026

[日本語版](04-cloudflare-ddos-h1-2026.ja.md)

## Why it belongs here

The annual Cloudflare report gives the strategic picture; the H1 DDoS report provides **current 2026 operational evidence** on availability attacks.

## Key finding

Cloudflare mitigated **935 network-layer DDoS attacks exceeding 1 Tbps** during H1 2026, with a **519% quarter-over-quarter increase** in these attacks from Q1 to Q2.

The report also emphasizes DNS floods and geopolitical drivers.

## Architecture interpretation

DDoS architecture should assume:

- extremely short attack ramp-up;
- botnet capacity beyond local network links;
- simultaneous network and application-layer pressure;
- geopolitical/event-driven changes in targeting;
- DNS as a critical dependency.

This pushes organizations toward provider/upstream mitigation rather than appliance-only defense.

## Recommended actions

- Use upstream/Anycast scrubbing rather than relying solely on on-prem capacity.
- Protect authoritative DNS and test provider failover.
- Monitor L3/L4 and L7 independently.
- Predefine rate-limit and degraded-service policies.
- Include major geopolitical/business events in readiness planning.
- Exercise DDoS during peak-demand scenarios, not only quiet maintenance windows.

## Primary sources

- https://blog.cloudflare.com/ddos-threat-report-2026-h1/
- Japanese edition: https://blog.cloudflare.com/ja-jp/ddos-threat-report-2026-h1/

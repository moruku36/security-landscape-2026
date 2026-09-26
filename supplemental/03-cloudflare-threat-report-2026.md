---
publisher: "Cloudflare / Cloudforce One"
edition: "2026 Cloudflare Threat Report"
publication_date: "2026-03-03"
observation_period: "Primarily 2025 with 2026 strategic outlook"
scope: "Threat intelligence and trillions of network signals across Cloudflare's global network"
language: "en"
primary_source: "https://blog.cloudflare.com/2026-threat-report/"
last_verified: "2026-09-27"
---

# Cloudflare 2026 Threat Report

[日本語版](03-cloudflare-threat-report-2026.ja.md)

## Why it belongs here

Cloudflare contributes a perspective that is underrepresented in traditional IR reports: **Internet-scale traffic, SaaS abuse, session-token theft, trusted cloud tooling, deepfake-enabled insider access, and hyper-volumetric DDoS**.

Its framing is useful for architects because the report describes a shift from "breaking in" to **"logging in" and living inside trusted services**.

## Major themes

Cloudflare identifies eight major trends for 2026:

1. AI automates high-velocity attacker operations.
2. State actors pre-position in critical infrastructure.
3. Over-privileged SaaS integrations increase blast radius.
4. Trusted SaaS/IaaS/PaaS tools are weaponized to hide malicious activity.
5. Deepfake personas enable hostile remote workers.
6. Session-token theft neutralizes traditional MFA.
7. Mail-relay identity gaps enable trusted-brand spoofing.
8. Hyper-volumetric DDoS exceeds human response speed.

## Representative findings

- Cloudflare highlights DDoS attacks reaching **31.4 Tbps**.
- In the cited login telemetry window, **63%** of logins involved credentials already compromised elsewhere.
- **94%** of login attempts originated from bots.
- Nearly **46%** of analyzed emails failed DMARC in the cited email-telemetry analysis.
- The report describes SaaS-to-SaaS compromise where one over-privileged integration can cascade across many customer environments.

## Architecture interpretation

### Identity beyond MFA

A live authenticated session can be more valuable than a password. If infostealers steal session cookies/tokens, the attacker may bypass the factor that was already satisfied.

Therefore identity protection must include:

- session lifetime;
- device/context binding;
- token revocation;
- post-authentication behavior;
- browser and endpoint hygiene.

### SaaS as attacker infrastructure

Cloudflare describes attackers using legitimate services such as Google Calendar, Dropbox, GitHub, Google Drive, Teams, Azure Web Apps, and Amazon S3 for hosting, command-and-control, redirection, delivery, or coordination.

This creates a detection problem because reputation-based filtering may see "trusted" domains.

### Insider / remote-worker trust

Deepfake identities, rented identities, and laptop farms turn the hiring process into an access-control boundary. HR, IT onboarding, identity proofing, endpoint enrollment, and privileged-access policy need to be connected.

### DDoS as autonomous-speed risk

At 31.4 Tbps scale, manual intervention is irrelevant. Capacity and automated mitigation must exist before the attack.

## Recommended actions

- Add session/token telemetry to identity detection.
- Inventory and constrain SaaS-to-SaaS grants.
- Detect unusual use of trusted SaaS as C2/data-staging channels.
- Harden remote-worker identity proofing and device enrollment.
- Enforce DMARC/DKIM/SPF and re-verification across relay paths.
- Use always-on automated DDoS mitigation for critical Internet services.
- Correlate bot, credential, session, network, and SaaS telemetry.

## Primary sources

- https://blog.cloudflare.com/2026-threat-report/
- https://www.cloudflare.com/lp/threat-report-2026/
- https://www.cloudflare.com/press/press-releases/2026/cloudflare-2026-threat-intelligence-report-nation-state-actors-and/

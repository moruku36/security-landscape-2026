---
event: "DEF CON 34"
date: "2026-08-06 to 2026-08-09"
location: "Las Vegas Convention Center, Las Vegas"
evidence_type: "Community technical research / villages / hands-on competitions"
primary_source: "https://forum.defcon.org/node/253965"
last_verified: "2026-09-26"
---

# DEF CON 34

## Positioning

DEF CON is a hands-on adversarial research signal. Its value is in exposing where **real-world trust assumptions break** across AI, cloud, identity, OT/ICS, hardware, protocols, and operational tooling.

Because DEF CON is decentralized across villages, this note uses official/community event sources rather than treating one page as a complete program.

## 2026 signals

### AI agents become offensive actors

AI Village's **HalCTF: Hostile Autonomous Layer CTF** required participants to build autonomous agents and deploy them against sandboxed challenges.

That is a meaningful shift in threat modeling:

```text
Human operator
→ tool

becomes

Human/operator objective
→ autonomous agent
→ tool chain
→ target
```

The defensive question therefore becomes:

- what authority can the agent obtain?
- how does it choose tools?
- what telemetry exists for autonomous actions?
- what safety boundary exists when the model behaves unexpectedly?

### Cloud remains a first-class hacking surface

Cloud Village at DEF CON 34 ran talks, workshops, labs, and CTFs around offensive and defensive cloud security.

This is consistent with CrowdStrike, Unit 42, Microsoft, and M-Trends signals that cloud control planes and trusted cloud/SaaS relationships are attack paths—not merely hosting locations.

### Recon and exposed AI infrastructure are converging

Recon-oriented community research included exposed inference endpoints and leaked API-key style scenarios.

Architecture implication:

> AI infrastructure must be part of external attack-surface management and secrets governance.

### OT/ICS, identity, runtime, and protocol trust remain active research areas

DEF CON villages continue to demonstrate that trusted protocols and operational technology can become attack surfaces when assumptions are not continuously validated.

## Enterprise use

Translate DEF CON signals into **red-team hypotheses**, not immediate panic.

Recommended flow:

```text
Novel research
→ identify prerequisite
→ test enterprise exposure
→ map reachable privilege
→ add telemetry
→ validate mitigations
```

## Evidence caveat

Village and competition programs are forward-looking technical signals. They are not evidence that a technique is prevalent in enterprise incidents.

## Sources

- https://forum.defcon.org/node/253965
- https://aivillage.org/events/defcon-34/
- https://www.cloud-village.org/dc34
- https://reconvillage.org/reconvillage-2026-defcon-34/talks
- https://defcon.outel.org/dcwp/dc34/activities/dctalkslist/ — community-maintained index
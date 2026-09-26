---
publisher: "Akamai"
edition: "State of the Internet / Security 2026 — Speed, Scale, and Nonhuman Identity: The Agentic Threat Landscape"
publication_date: "2026-09-22"
observation_period: "2026 enterprise AI/agent observations"
scope: "Agentic AI, browser, MCP, API and nonhuman identity risk"
language: "en"
primary_source: "https://www.akamai.com/blog/security/2026/sep/beyond-identity-governing-the-agentic-enterprise"
last_verified: "2026-09-27"
---

# Akamai SOTI 2026 — Agentic Threat Landscape

[日本語版](06-akamai-agentic-threat-landscape-2026.ja.md)

## Why it belongs here

This is one of the most directly relevant 2026 sources for this repository's AI architecture thesis: **agent security is an identity + authorization + API-governance problem**.

## Key findings

- MCP gives agents standardized "hands" to invoke tools and APIs, but can blur the boundary between data and executable instructions.
- More than **40% of enterprise users** in Akamai's cited observations had installed browser AI tools/extensions.
- **25%** of installed extensions changed permissions within 12 months.
- More than **6% of AI chatbot conversations on enterprise devices contained sensitive data**.
- Akamai argues that enterprises need real-time governance of machine-to-machine activity and API authorization, not only initial identity verification.

## Architecture interpretation

Traditional IAM answers:

> Who are you, and may you access this resource?

Agentic systems add:

> What sequence of actions may this autonomous identity perform, through which tools, using whose delegated authority, and under what approval boundary?

That turns security into continuous authorization.

Useful policy attributes include:

- agent identity;
- user/trigger identity;
- tool/server identity;
- action type;
- target resource;
- data classification;
- environment;
- risk score;
- approval state;
- delegation chain.

## Recommended actions

- Maintain a registry of agents, MCP servers, connectors, and browser AI extensions.
- Separate read/write/admin tool capabilities.
- Re-authorize at the tool boundary; never treat prompt content as authorization.
- Log agent → tool → API → resource chains.
- Detect unexpected permission changes in extensions/connectors.
- Put destructive, privileged, external-communication, and credential-management actions behind stronger gates.
- Apply short-lived credentials and explicit scopes to machine identities.

## Repository linkage

This report directly supports:

- [AI Security Architecture](../ai-security/README.md)
- [MCP Security](../ai-security/mcp-security.md)
- [Identity Architecture](../architecture/identity.md)

## Primary source

- https://www.akamai.com/blog/security/2026/sep/beyond-identity-governing-the-agentic-enterprise

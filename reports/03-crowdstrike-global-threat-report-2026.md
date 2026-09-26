# CrowdStrike 2026 Global Threat Report

Source: https://www.crowdstrike.com/en-us/resources/reports/global-threat-report-executive-summary-2026/

## Positioning

Adversary-centric。Threat actor、breakout、cloud/edgeを跨ぐmovement、malware-free tradecraftを見るのに強い。

## Key findings

- Fastest observed eCrime breakout time: 27秒。
- AI-enabled adversary attacks: +89%。
- Public disclosure前にexploitされたzero-day vulnerability: +42%。
- China-nexus actorがexploitしたvulnerabilityの40%はedge deviceを標的。
- State-nexus actorによるcloud-conscious intrusion: +266%。

## Interpretation

「Endpointで検知して、人が調査して、数十分後に隔離」という運用モデルでは追いつかないケースが現実にある。

2026年のSOCは、検知精度だけでなく **time-to-contain** がarchitecture requirementになる。

## Architecture implication

- Endpoint / Identity / Cloud telemetryを別々のqueueに置かずcorrelationする。
- High-confidence signalはautomated containmentできる設計にする。
- Edge deviceをunmanaged infrastructureとして放置しない。
- Cloud control plane activityとworkload activityを同一incidentに束ねる。

# Unit 42 Global Incident Response Report 2026

Source: https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report

## Positioning

750件超のmajor IR engagementからattack lifecycleを分析。Cloud / SaaS / Identity / Browserを横断した「複数attack surface」の見方が特徴。

## Four major trends

1. AI is a force multiplier.
2. Identity is the most reliable path to attacker success.
3. Supply-chain risk is expanding from code to trusted connectivity.
4. Nation-state actors are moving deeper into infrastructure and virtualization.

## Key findings

- Identity weaknessが約90%のinvestigationで重要な役割。
- 87%のintrusionが複数attack surfaceを横断。
- 48%にbrowser-based activityが関与。
- 90%超でpreventable gapが侵害を実質的に助けた。
- Fastest 25%のintrusionはexfiltrationまで1.2時間。前年4.8時間から大幅短縮。
- SaaS dataが関係したcaseは23%まで増加。
- Cloud identity分析では99%のuser/role/serviceに過剰権限が存在したと報告。

## Especially important: identity

Identityは「入口」だけでなく、privilege escalation、lateral movement、persistenceの経路そのもの。

対象はhuman accountだけではない。

- Service Account
- Automation Role
- API Key
- OAuth Grant
- Session Token
- AI Agent / Machine Identity

## Especially important: supply chain

Supply chainはpackage compromiseだけではなく、OAuth app、RMM/MDM、vendor management plane、SaaS connectorまで含む。

そのため必要なのはSBOMだけではなく、**connection inventory / effective permission / break-glass revocation / audit telemetry**。

## Architecture implication

Zero Trustをnetwork segmentationの言い換えにせず、Identity trustを最小化する設計として実装することが重要。

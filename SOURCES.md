# Sources and methodology

Checked: **2026-09-27 (JST)**

This source register separates **threat evidence**, **conference signals**, **framework references**, and **implementation references**.

## Annual reports

| Source | Edition | Observation scope / note | Official URL |
|---|---|---|---|
| Google Cloud / Mandiant | M-Trends 2026 | Mandiant investigations conducted 2025-01-01 through 2025-12-31; 500k+ frontline investigation hours | https://cloud.google.com/security/resources/m-trends-executive-edition |
| Verizon | 2026 DBIR | In-scope incidents 2024-11-01 through 2025-10-31; 22,000+ breaches across 145 countries highlighted in official materials | https://www.verizon.com/business/resources/reports/dbir/ |
| CrowdStrike | 2026 Global Threat Report | 2025 adversary observations | https://www.crowdstrike.com/en-us/resources/reports/global-threat-report-executive-summary-2026/ |
| Palo Alto Networks Unit 42 | 2026 Global Incident Response Report | 750+ IR cases from 2024-10-01 through 2025-09-30 across 50+ countries | https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report |
| Microsoft | Digital Defense Report 2025 | Latest annual edition available as of 2026-09-26 | https://www.microsoft.com/en-us/security/security-insider/threat-landscape/microsoft-digital-defense-report-2025 |
| IBM X-Force | Threat Intelligence Index 2026 | 2025 X-Force threat intelligence / incident observations | https://www.ibm.com/reports/threat-intelligence |
| ENISA | Threat Landscape 2026 | Events/incidents observed 2025-01-01 through 2025-12-31; published 2026-09-22 | https://www.enisa.europa.eu/publications/enisa-threat-landscape-2026 |

## Conferences

### RSAC 2026

- https://www.rsaconference.com/events/2026-usa
- https://path.rsaconference.com/flow/rsac/us26/FullAgenda/page/catalog/session/1765809740965001q2tz
- https://path.rsaconference.com/flow/rsac/us26/FullAgenda/page/catalog/session/1756095334761001u5K4

### Black Hat USA 2026

- https://blackhat.com/us-26/briefings.html
- https://blackhat.com/us-26/schedule.html
- https://blackhat.com/html/press/2026-06-02.html

### DEF CON 34

- https://forum.defcon.org/node/253965
- https://aivillage.org/events/defcon-34/
- https://www.cloud-village.org/dc34
- https://reconvillage.org/reconvillage-2026-defcon-34/talks
- https://defcon.outel.org/dcwp/dc34/activities/dctalkslist/ — community-maintained program index

### FIRST CTI 2026

- https://www.first.org/conference/firstcti26/
- https://www.first.org/conference/firstcti26/program
- https://www.first.org/newsroom/releases/20260423

### FIRSTCON26

- https://www.first.org/conference/2026/
- https://www.first.org/conference/2026/program
- https://www.first.org/conference/2026/welcome

## Framework references

### MITRE ATT&CK

- Enterprise ATT&CK: https://attack.mitre.org/
- Exploit Public-Facing Application (T1190): https://attack.mitre.org/techniques/T1190/
- Valid Accounts (T1078): https://attack.mitre.org/techniques/T1078/
- Steal Application Access Token (T1528): https://attack.mitre.org/techniques/T1528/
- Use Alternate Authentication Material (T1550): https://attack.mitre.org/techniques/T1550/
- Account Manipulation (T1098): https://attack.mitre.org/techniques/T1098/
- Data Encrypted for Impact (T1486): https://attack.mitre.org/techniques/T1486/
- Inhibit System Recovery (T1490): https://attack.mitre.org/techniques/T1490/

### NIST CSF 2.0

- Resource center: https://www.nist.gov/cyberframework
- Informative References: https://www.nist.gov/cyberframework/informative-references
- CSF 2.0 publication: https://doi.org/10.6028/NIST.CSWP.29

### CIS Controls

- CIS Controls v8.1: https://www.cisecurity.org/controls/v8-1
- CIS Controls Navigator: https://www.cisecurity.org/controls/cis-controls-navigator/v8

## Cloud implementation references

### Microsoft Azure / Entra

- Entra PIM: https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/
- Identity Governance: https://learn.microsoft.com/en-us/entra/id-governance/identity-governance-overview
- Conditional Access authentication strength: https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-guests-mfa-strength

### AWS

- IAM security best practices: https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html
- IAM Access Analyzer findings: https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-findings.html
- IAM Identity Center: https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html

### Google Cloud

- Workforce Identity Federation: https://cloud.google.com/iam/docs/workforce-identity-federation
- Workload Identity Federation: https://cloud.google.com/iam/docs/workload-identity-federation
- Service account security: https://cloud.google.com/iam/docs/best-practices-service-accounts
- Privileged Access Manager: https://cloud.google.com/iam/docs/pam-overview
- Access Context Manager: https://cloud.google.com/access-context-manager/docs/overview
- Organization Policy: https://cloud.google.com/organization-policy/overview

## AI / MCP implementation references

- MCP Authorization specification (2026-07-28): https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization
- MCP Security Best Practices: https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices
- MCP 2026-07-28 conformance status: https://plan.modelcontextprotocol.io/conformance
- MCP SEP/status register: https://plan.modelcontextprotocol.io/seps
- MCP roadmap (2026-08-22): https://blog.modelcontextprotocol.io/posts/mcp-roadmap/

## Methodology

- Primary/official sources are preferred.
- Vendor statistics are scoped to their own observation populations and are not used for direct vendor ranking.
- Themes repeated in independent sources are treated as cross-source signals.
- Conference material is used as a forward-looking technical signal and kept distinct from incident statistics.
- Framework mappings are repository analysis unless explicitly supplied by the original source.
- Product-specific cloud guidance is subordinate to provider-neutral architecture principles.
- Important statistics should record the observation context, denominator/population where available, and official evidence in the report note.
- Counts, percentages, medians, averages, fastest observations, incident counts, breach counts and attack-technique counts are preserved as different measurement types; they are not normalized without source support.

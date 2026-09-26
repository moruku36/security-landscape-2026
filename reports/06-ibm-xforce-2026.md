# IBM X-Force Threat Intelligence Index 2026

Source: https://www.ibm.com/reports/threat-intelligence

## Key findings

- Public-facing software/system application exploitation: +44% YoY。
- Disclosed vulnerabilityの56%はsuccessful exploitationにauthentication不要。
- Dark webで販売が確認されたAI chatbot credential: 300,000。
- Active ransomware groups: +49%。

## IBM's recommended directions

- Autonomous security
- Identity security
- Vulnerability testing
- AI security
- Data security

## Interpretation

IBMの数字から見えるのは、AI時代になっても**Public-facing Asset + Credential + Ransomware**という基礎問題が消えていないこと。

AI chatbot credentialの流通は、AIを新しいSaaSとして考える必要性を示す。AIへのSSO、token lifecycle、secret scanning、data access governanceが必要になる。

## Architecture implication

AI Securityを「prompt injection対策」だけに限定しない。AI service account、API key、connector、data plane、loggingまで通常のEnterprise IAM/Secrets Managementへ組み込む。

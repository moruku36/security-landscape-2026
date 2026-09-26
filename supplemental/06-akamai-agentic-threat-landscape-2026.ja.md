---
publisher: "Akamai"
edition: "State of the Internet / Security 2026 — Speed, Scale, and Nonhuman Identity"
publication_date: "2026-09-22"
language: "ja"
translation_of: "06-akamai-agentic-threat-landscape-2026.md"
primary_source: "https://www.akamai.com/blog/security/2026/sep/beyond-identity-governing-the-agentic-enterprise"
last_verified: "2026-09-27"
---

# Akamai SOTI 2026 — Agentic Threat Landscape 日本語解説

[English](06-akamai-agentic-threat-landscape-2026.md)

## 追加する価値

このRepositoryのAI Security方針である、

> **Agent Security = Identity + Authorization + API Governance**

を直接補強する2026年Sourceです。

## 主要データ

- MCPはAgentにAPI/Toolを実行する「Hands」を与える一方、DataとInstructionの境界を曖昧にするRisk。
- Akamaiの該当観測ではEnterprise Userの**40%超**がBrowser AI Tool/Extensionを導入。
- Install済みExtensionの**25%**が12か月以内にPermissionを変更。
- Enterprise Device上のAI Chatbot Conversationの**6%超**にSensitive Data。
- Initial LoginだけでなくMachine-to-Machine ActionをReal-timeでGovernする必要性を指摘。

## Architecture上の意味

従来IAM:

> Who are you? このResourceへAccessしてよいか?

Agentic Security:

> このAgentは、誰のDelegationで、どのToolを通じ、どのResourceに、どのAction Sequenceまで実行してよいか?

つまりContinuous Authorizationが必要です。

Policy Contextには、

- Agent ID
- Trigger/User ID
- Tool/MCP Server
- Action
- Target
- Data Class
- Environment
- Risk
- Approval
- Delegation Chain

を含めます。

## 優先アクション

- Agent / MCP / Connector / Browser AI Extension Registry
- Read / Write / Admin Tool分離
- Tool BoundaryでAuthorization再評価
- Agent→Tool→API→Resource Audit
- Permission Change Monitoring
- Delete / IAM / Credential / External SendへHuman Gate
- Machine IdentityをShort-lived / Scoped Credentialへ

## 関連ドキュメント

- [AI Security Architecture](../ai-security/README.md)
- [MCP Security](../ai-security/mcp-security.md)
- [Identity Architecture](../architecture/identity.md)

## Primary Source

- https://www.akamai.com/blog/security/2026/sep/beyond-identity-governing-the-agentic-enterprise

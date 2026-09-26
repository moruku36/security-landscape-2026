# FIRST Cyber Threat Intelligence Conference 2026

Sources:
- https://www.first.org/conference/firstcti26/
- https://www.first.org/conference/firstcti26/program
- https://www.first.org/newsroom/releases/20260423

Munich, 2026-04-21〜23.

## Positioning

CTIを「レポートを書く仕事」ではなく、Detection / IR / Decisionへ接続するoperational disciplineとして扱うカンファレンス。

## Dominant themes

### From signal to action

FIRST公式recapでは、Operationalizing Intelligenceがdominant theme。Collectionをstakeholder requirementに合わせること、enrichment自動化、noise削減など、意思決定につながらないintelは価値が低いという実務的な方向。

### AI + CTI

- LLM / RAG / cognitive automationによるanalyst productivity
- Poisoned OSINT
- CTI RAG pipelineのintegrity
- AI-assisted analysisへのadversarial manipulation

### Detection Engineering

ProgramにはSigmaを使ったDetection Engineering workshop、Open SourceによるCloud Forensics lab on GCPなどが含まれた。

## Interpretation

CTI、SIEM、Detection Engineering、IRを別々の機能として分割しすぎない方がよい。

```text
PIR / Intelligence Requirement
        ↓
Collection / Enrichment
        ↓
Detection-as-Code
        ↓
Investigation / Response
        ↓
Feedback to Controls
```

この閉ループがSecOpsの成熟度を決める。

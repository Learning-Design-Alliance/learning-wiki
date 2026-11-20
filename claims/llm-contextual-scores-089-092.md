---
type: claim
title: The prompt-based method achieves contextual relevance scores of 0.89 to 0.92 across the four LLMs on the GPT-4 based scoring metric
description: The prompt-based method achieves contextual relevance scores of 0.89 to 0.92 across the four LLMs on the GPT-4 based scoring metric
id: llm-contextual-scores-089-092
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: kaito-tanaka-2024
    resource: "https://doi.org/10.48550/arXiv.2408.06874"
    title: "Kaito Tanaka, Benjamin Tan, Brian Wong. (2024). Leveraging Language Models for Emotion and Behavior Analysis in Education. [doi:10.48550/arXiv.2408.06874](https://doi.org/10.48550/arXiv.2408.06874)"
    author: Kaito Tanaka, Benjamin Tan, Brian Wong
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The prompt-based method achieves contextual relevance scores of 0.89 to 0.92 across the four LLMs on the GPT-4 based scoring metric

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` GPT-4 based contextual scores for the proposed method were 0.89 for Qwen, 0.91 for ChatGPT, 0.90 for Claude2, and 0.92 for GPT-4. [→ Kaito Tanaka 2024](#kaito-tanaka-2024)

## Evidence

### Kaito Tanaka 2024

Kaito Tanaka, Benjamin Tan, Brian Wong. (2024). Leveraging Language Models for Emotion and Behavior Analysis in Education. [doi:10.48550/arXiv.2408.06874](https://doi.org/10.48550/arXiv.2408.06874)

`q2 · i?` · `design · r2`

Section 4.4.2 reports the GPT-4 score, a metric assessing contextual relevance of predictions, for the proposed method on each LLM. The article states the method "demonstrates a deeper understanding of the contextual nuances in student text data".

> "With scores of 0.89 for Qwen, 0.91 for ChatGPT, 0.90 for Claude2, and 0.92 for GPT-4, our method demonstrates a deeper understanding of the contextual nuances in student text data."

## Discussion


## Related Claims
- [Tailored prompt engineering consistently outperforms base models and chain-of-thought prompting across four LLMs for educational emotion and behavior analysis](prompt-engineering-outperforms-baselines-llm-emotion-analysis.md) — a broader claim this one bears on

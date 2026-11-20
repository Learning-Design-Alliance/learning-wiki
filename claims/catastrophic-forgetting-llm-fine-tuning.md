---
type: claim
title: Catastrophic forgetting is prevalent when fine-tuning LLMs, risking loss of general knowledge in customized educational models
description: Catastrophic forgetting is prevalent when fine-tuning LLMs, risking loss of general knowledge in customized educational models
id: catastrophic-forgetting-llm-fine-tuning
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: weak
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: lee-2024
    resource: "https://doi.org/10.48550/arXiv.2407.11203"
    title: "Lee, J., Hicke, Y., Yu, R., Brooks, C., & Kizilcec, R. F. (2024). The Life Cycle of Large Language Models: A Review of Biases in Education. Originally published 2023. [doi:10.48550/arXiv.2407.11203](https://doi.org/10.48550/arXiv.2407.11203)"
    author: "Lee, J., Hicke, Y., Yu, R., Brooks, C., & Kizilcec, R. F."
    q: 2
    i: "?"
    kind: review
    rigour: "?"
---

# Catastrophic forgetting is prevalent when fine-tuning LLMs, risking loss of general knowledge in customized educational models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · review `r?` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Fine-tuning LLMs can cause the model to overly adapt to the new dataset and forget broader generalizations, a phenomenon the review reports was found prevalent when fine-tuning Llama-7b and Alpaca-7B. [→ Lee 2024](#lee-2024)

## Evidence

### Lee 2024

Lee, J., Hicke, Y., Yu, R., Brooks, C., & Kizilcec, R. F. (2024). The Life Cycle of Large Language Models: A Review of Biases in Education. Originally published 2023. [doi:10.48550/arXiv.2407.11203](https://doi.org/10.48550/arXiv.2407.11203)

`q2 · i?` · `review · r?`

The review reports, citing Luo et al. (2023), an empirical investigation finding catastrophic forgetting prevalent when fine-tuning Llama-7b and Alpaca-7B. The review also cites Zhai et al. (2023) finding that fine-tuning multi-modal LLMs can lead to increased hallucinations.

> "Luo et al. (2023) conducted an empirical investigation and discovered that catastrophic forgetting is prevalent when ﬁne-tuning LLMs such as Llama-7b and Alpaca-7B."

## Discussion


## Related Claims
- [Language models catastrophically forget L1 when exposure ceases, unlike humans past the critical period](lms-catastrophic-l1-attrition-sequential.md) — related
- [Adaptation through prompt injection avoids fine-tuning, so the system works with any OpenAI-compatible LLM and its logic is transparent to educators](prompt-engineering-adaptation-transparency-tradeoff.md) — related

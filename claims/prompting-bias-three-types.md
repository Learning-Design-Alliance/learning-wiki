---
type: claim
title: "Prompt customization introduces at least three types of prompting bias: majority label, recency, and common token bias"
description: "Prompt customization introduces at least three types of prompting bias: majority label, recency, and common token bias"
id: prompting-bias-three-types
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
    q: 1
    i: "?"
    kind: review
    rigour: 2
---

# Prompt customization introduces at least three types of prompting bias: majority label, recency, and common token bias

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · review `r2` · `q1`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q1 i?` Prompt tuning can give rise to majority label bias, recency bias, and common token bias, which can cause pre-trained LLMs to exhibit representation bias toward specific responses. [→ Lee 2024](#lee-2024)

## Evidence

### Lee 2024

Lee, J., Hicke, Y., Yu, R., Brooks, C., & Kizilcec, R. F. (2024). The Life Cycle of Large Language Models: A Review of Biases in Education. Originally published 2023. [doi:10.48550/arXiv.2407.11203](https://doi.org/10.48550/arXiv.2407.11203)

`q1 · i?` · `review · r2`

The review's descriptive account of prompting bias in prompt customization, citing Z. Zhao et al. (2021). It adds that a final response prompt containing a negative label may influence the model to predict negative language, and cites Kotek et al. (2023) proposing a 15-prompt paradigm to test gender bias.

> "However, this technique can give rise to at least three types ofprompting bias: majority label bias, recency bias (overemphasizing the importance of the latest information), and common token bias (Z. Zhao et al. 2021)."

## Discussion


## Related Claims
- [Fine-tuned PLMs outperform prompted LLMs in rubric-based teaching quality scoring accuracy, while LLMs better preserve score variability](plms-outperform-llms-qof-scoring-accuracy.md) — related
- [Within prompt–response AI interfaces, students without guidance rarely move beyond prompt tuning, yielding interactions of limited educational value and increased reliance on outputs](prompt-response-interface-limits-learning-value.md) — related
- [Adaptation through prompt injection avoids fine-tuning, so the system works with any OpenAI-compatible LLM and its logic is transparent to educators](prompt-engineering-adaptation-transparency-tradeoff.md) — related
- [Only two EduBehaviors configurations reach macro-F1 comparable to the fine-tuned RoBERTa encoder (0.76) trained on expert-labelled TalkMoves data](edubehaviors-underperforms-finetuned-encoder.md) — related
- [The best-scoring prompt-engineered approaches did not match the fine-tuned models on emotion detection and Gibbs cycle tasks](papagai-finetuned-outperforms-gpt3-davinci.md) — related
- [Error detection accuracy rises with the likelihood score LLMs assign to a solution, which the authors interpret as the cause of conformity bias](likelihood-score-predicts-detection-accuracy.md) — related

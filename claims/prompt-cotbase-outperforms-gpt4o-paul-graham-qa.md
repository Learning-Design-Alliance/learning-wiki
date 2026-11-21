---
type: claim
title: A LangChain-based Prompt-CoT model achieves higher accuracy than GPT-4o and BERT on the Paul Graham Essay question-answering benchmark
description: A LangChain-based Prompt-CoT model achieves higher accuracy than GPT-4o and BERT on the Paul Graham Essay question-answering benchmark
id: prompt-cotbase-outperforms-gpt4o-paul-graham-qa
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: wenqi-guan-and-yang-fang-2025
    resource: "https://doi.org/10.4108/eai.21-11-2024.2354589"
    title: "Wenqi Guan and Yang Fang. (2025). Optimizing Web-Based AI Query Retrieval with GPT Integration in LangChain: A CoT-Enhanced Prompt Engineering Approach. Originally published 2024. [doi:10.4108/eai.21-11-2024.2354589](https://doi.org/10.4108/eai.21-11-2024.2354589)"
    author: Wenqi Guan and Yang Fang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A LangChain-based Prompt-CoT model achieves higher accuracy than GPT-4o and BERT on the Paul Graham Essay question-answering benchmark

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the Paul Graham Essay QA dataset, the LangChain-based Prompt-CoTBase model reached 96.36% accuracy, 89.66% precision and 0.87 mAP, versus 79.09% accuracy, 61.23% precision and 0.52 mAP for GPT-4o. [→ Wenqi Guan and Yang Fang 2025](#wenqi-guan-and-yang-fang-2025)

## Evidence

### Wenqi Guan and Yang Fang 2025

Wenqi Guan and Yang Fang. (2025). Optimizing Web-Based AI Query Retrieval with GPT Integration in LangChain: A CoT-Enhanced Prompt Engineering Approach. Originally published 2024. [doi:10.4108/eai.21-11-2024.2354589](https://doi.org/10.4108/eai.21-11-2024.2354589)

`q2 · i?` · `design · r2`

Benchmark evaluation on the Paul Graham Essay Question Answering dataset (22 questions) comparing GPT-3.5 Turbo, GPT-4o, BERT and Prompt-CoTBase (Table 1). The authors report the LangChain model "achieved a significant performance boost" over the GPT-4o baseline (temperature = 0).

> "the model based on LangChain achieved a significant performance boost with an accuracy of 96.36%, a precision of 89.66%, and an mAP of 0.87, compared to 79.09% accuracy, 61.23% precision, and 0.52 mAP for GPT-4o."

## Discussion


## Related Claims
- [On Google's Natural Questions long-answer test, Prompt-CoTBase attains a higher F1 score than GPT-4o and BERT](prompt-cotbase-higher-f1-natural-questions.md) — related
- [Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance](curricular-cot-improves-accuracy-larger-models.md) — related
- [Chain-of-Thought prompting improves LLM performance on complex reasoning questions by eliciting step-by-step breakdowns](cot-prompting-improves-complex-reasoning.md) — a broader claim this one bears on

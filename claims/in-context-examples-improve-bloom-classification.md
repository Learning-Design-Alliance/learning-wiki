---
type: claim
title: "In-context examples improve LLM Bloom classification: three-shot and ten-shot prompting outperform zero-shot across datasets"
description: "In-context examples improve LLM Bloom classification: three-shot and ten-shot prompting outperform zero-shot across datasets"
id: in-context-examples-improve-bloom-classification
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: abdolali-faraji-2026
    resource: "https://arxiv.org/abs/2606.13684"
    title: "Abdolali Faraji, Mohammadreza Molavi, Zohreh Rasoulkhani, Mohammadreza Tavakoli, and Gábor Kismihók. (2026). Cross-Dataset Bloom Question Classification: Supervised Models and Prompted LLMs. https://arxiv.org/abs/2606.13684"
    author: Abdolali Faraji, Mohammadreza Molavi, Zohreh Rasoulkhani, Mohammadreza Tavakoli, and Gábor Kismihók
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# In-context examples improve LLM Bloom classification: three-shot and ten-shot prompting outperform zero-shot across datasets

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Both three-shot and ten-shot prompting outperform zero-shot prompting across datasets, though zero-shot still yields reasonable performance. [→ Abdolali Faraji 2026](#abdolali-faraji-2026)

## Evidence

### Abdolali Faraji 2026

Abdolali Faraji, Mohammadreza Molavi, Zohreh Rasoulkhani, Mohammadreza Tavakoli, and Gábor Kismihók. (2026). Cross-Dataset Bloom Question Classification: Supervised Models and Prompted LLMs. https://arxiv.org/abs/2606.13684

`q2 · i?` · `causal · r2`

RQ2 evaluation across five datasets and five prompting strategies (Table 3). Few-shot prompts with examples drawn from the same dataset beat zero-shot; zero-shot GPT-5 still achieved weighted F1 around 0.75 on most datasets.

> "Both three-shot and ten-shot prompting outperform zero-shot prompting across datasets, suggesting that additional contextual information helps to align model predictions with Bloom's cognitive levels."

## Discussion


## Related Claims
- [LLMs show robust zero- and few-shot Bloom classification of OOD AI-assisted questions compared with ML and BERT models](llms-robust-ood-bloom-classification.md) — related
- [Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance](curricular-cot-improves-accuracy-larger-models.md) — related
- [The selected-questions-verbs prompting strategy yields the strongest LLM Bloom classification, reaching weighted F1 up to 0.84](selected-questions-verbs-best-prompt.md) — related

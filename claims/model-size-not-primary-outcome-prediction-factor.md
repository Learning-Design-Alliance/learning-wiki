---
type: claim
title: Model size is not the primary factor in outcome-prediction performance
description: Model size is not the primary factor in outcome-prediction performance
id: model-size-not-primary-outcome-prediction-factor
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: michal-štefánik-2026
    resource: "https://arxiv.org/abs/2609.20484"
    title: "Michal Štefánik, Jan Nehyba, Jirina Karasova, Martin Fico, Lucie Škarková, Markéta Košatková, David Kosatka. (2026). Edustories: A Collection of Real-world Case Studies from Classroom Practices. https://arxiv.org/abs/2609.20484"
    author: Michal Štefánik, Jan Nehyba, Jirina Karasova, Martin Fico, Lucie Škarková, Markéta Košatková, David Kosatka
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Model size is not the primary factor in outcome-prediction performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` The larger Llama-3.3-70B underperformed the smaller Llama-3.2-3B on outcome prediction, suggesting architectural choices and training refinements matter more than scale alone. [→ Michal Štefánik 2026](#michal-stefanik-2026)

## Evidence

### Michal Štefánik 2026

Michal Štefánik, Jan Nehyba, Jirina Karasova, Martin Fico, Lucie Škarková, Markéta Košatková, David Kosatka. (2026). Edustories: A Collection of Real-world Case Studies from Classroom Practices. https://arxiv.org/abs/2609.20484

`q2 · i?` · `design · r2`

Comparative analysis of the six evaluated models' accuracies on the 310-case benchmark. The article reports the size inversion as an observed result and hypothesizes that "outcome prediction may depend more on general reasoning capability".

> "For example, the larger Llama-3.3-70B underperforms the smaller Llama-3.2-3B, suggesting that architectural choices, training data and other training refinements play a more important role than scale alone."

## Discussion


## Related Claims
- [Current LLMs fall short of human experts in predicting classroom intervention outcomes](llms-below-expert-outcome-prediction.md) — related
- [Under identical LoRA hyperparameters and training data, the 27B Gemma model outperforms the 70B LLaMA model on every computed essay-scoring metric](model-scale-not-predictor-lora-scoring.md) — related
- [LLaMA's LoRA adaptation compresses its prediction range to roughly 2.0–4.0, while Gemma maintains a broader distribution closer to the ground truth](llama-prediction-range-compression.md) — related
- [CDPK performance scales with model size, with a sharp Pareto-frontier drop-off below around 8B parameters](cdpk-scales-with-model-size-dropoff-below-8b.md) — reports the opposite
- [Larger Llama Guard models outperform smaller ones on education-prompt classification, with the 8B model best in accuracy, recall, and F1](llama-guard-scaling-trend-education-classification.md) — reports the opposite

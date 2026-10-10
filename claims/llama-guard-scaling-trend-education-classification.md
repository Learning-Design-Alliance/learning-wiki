---
type: claim
title: Larger Llama Guard models outperform smaller ones on education-prompt classification, with the 8B model best in accuracy, recall, and F1
description: Larger Llama Guard models outperform smaller ones on education-prompt classification, with the 8B model best in accuracy, recall, and F1
id: llama-guard-scaling-trend-education-classification
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: haein-kong-2026
    resource: "https://arxiv.org/abs/2607.00395"
    title: "Haein Kong. (2026). Child Safety in Generative AI: An Expert-Guided and Incident-Grounded Evaluation Framework. HEAL@CHI, April 2026, Barcelona. https://arxiv.org/abs/2607.00395"
    author: Haein Kong
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Larger Llama Guard models outperform smaller ones on education-prompt classification, with the 8B model best in accuracy, recall, and F1

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` A scaling trend was observed: the 8B model outperforms the 1B and 7B models in accuracy, recall, and F1 on the education-domain test set. [→ Haein Kong 2026](#haein-kong-2026)

## Evidence

### Haein Kong 2026

Haein Kong. (2026). Child Safety in Generative AI: An Expert-Guided and Incident-Grounded Evaluation Framework. HEAL@CHI, April 2026, Barcelona. https://arxiv.org/abs/2607.00395

`q2 · i?` · `design · r2`

Binary classification evaluation of three Llama Guard models (1B, 7B, 8B) on the generated education test set, reported in the Results section and Figure 1. The article states "models with larger parameter sizes perform better than smaller ones" and names the 8B model as outperforming the 1B and 7B models on three metrics. No effect size is printed.

> "The results reveal a scaling trend: models with larger parameter sizes perform better than smaller ones. For example, the 8B model outperforms the 1B and 7B models in accuracy, recall, and F1."

## Discussion


## Related Claims
- [Llama Guard models misclassify subtle, context-dependent unsafe education prompts (e.g., exam-answer and cheating requests) as safe](llama-guard-failure-cases-subtle-education-risks.md) — related
- [CDPK performance scales with model size, with a sharp Pareto-frontier drop-off below around 8B parameters](cdpk-scales-with-model-size-dropoff-below-8b.md) — related
- [Model size is not the primary factor in outcome-prediction performance](model-size-not-primary-outcome-prediction-factor.md) — reports the opposite
- [Predictive performance of sensor configurations does not change monotonically with the number of sensing streams; preferred configuration depends on target metric and sensing cost](sensor-stream-performance-non-monotonic.md) — reports the opposite

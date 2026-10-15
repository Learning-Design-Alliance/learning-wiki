---
type: claim
title: Adaptation gains grow monotonically with model capacity under the same LoRA recipe, though three data points cannot establish a scaling law
description: Adaptation gains grow monotonically with model capacity under the same LoRA recipe, though three data points cannot establish a scaling law
id: adaptation-gains-grow-with-model-capacity
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: rashid-azraf-jahin-2026
    resource: "https://doi.org/10.48550/arxiv.2610.00664"
    title: "Rashid Azraf Jahin, Saadman Sajid, Khan Raiyan Ibne Reza, Sumaiya Tabassum Nimi. (2026). PhysicsMate: A Curriculum-Grounded Bengali Benchmark for Secondary Physics QA with Small-Model Adaptation. IEEE CSDE 2026. https://arxiv.org/abs/2610.00664 [doi:10.48550/arxiv.2610.00664](https://doi.org/10.48550/arxiv.2610.00664)"
    author: Rashid Azraf Jahin, Saadman Sajid, Khan Raiyan Ibne Reza, Sumaiya Tabassum Nimi
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Adaptation gains grow monotonically with model capacity under the same LoRA recipe, though three data points cannot establish a scaling law

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Accuracy improvements increase monotonically with parameter count (+5.5, +15.0, +23.3 pp from 0.6B to 4B), observed across accuracy, Token F1 and BERTScore. [→ Rashid Azraf Jahin 2026](#rashid-azraf-jahin-2026)

## Evidence

### Rashid Azraf Jahin 2026

Rashid Azraf Jahin, Saadman Sajid, Khan Raiyan Ibne Reza, Sumaiya Tabassum Nimi. (2026). PhysicsMate: A Curriculum-Grounded Bengali Benchmark for Secondary Physics QA with Small-Model Adaptation. IEEE CSDE 2026. https://arxiv.org/abs/2610.00664 [doi:10.48550/arxiv.2610.00664](https://doi.org/10.48550/arxiv.2610.00664)

`q2 · i?` · `causal · r2`

Numerical results reported with Fig. 2 across three Qwen3 scales under one fixed LoRA configuration (r = 16, α = 32, dropout 0.05). The authors state "Three data points is not enough to prove a scaling law" but the trend is monotonic across all three metrics.

> "Figure 2 shows that adaptation gains grow with model capacity. The accuracy improvement trajectory is: ∆Acc : +5 .5 pp → +15.0 pp → +23.3 pp"

## Discussion


## Related Claims
- [LoRA adaptation significantly increases closed-book accuracy on the PhysicsMate test set at all three Qwen3 scales](lora-adaptation-raises-bengali-physics-qa-accuracy-all-scales.md) — a narrower finding that bears on this claim
- [CDPK performance scales with model size, with a sharp Pareto-frontier drop-off below around 8B parameters](cdpk-scales-with-model-size-dropoff-below-8b.md) — a broader claim this one bears on
- [Model family and instruction-tuning approach appear better predictors of tutoring quality than parameter count alone](model-family-beats-parameter-count-for-tutoring-quality.md) — related
- [LoRA fine-tuning on control systems course data increases lexical and semantic similarity between model responses and course reference answers at both 3B and 7B model sizes](lora-improves-reference-answer-similarity-control-systems.md) — related
- [Adaptation benefits structured curricular knowledge (quantities, laws, definitions) most and loosely specified entity-level knowledge least](structured-knowledge-benefits-most-from-adaptation.md) — related

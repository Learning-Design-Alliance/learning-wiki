---
type: claim
title: Model clustering performance rises monotonically with hidden dimensionality, with the steepest gains over the first three dimensions
description: Model clustering performance rises monotonically with hidden dimensionality, with the steepest gains over the first three dimensions
id: hidden-dimensionality-monotonic-vmeasure-rise
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: weak
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: frank-lihui-tan-youngah-do-2024
    resource: "https://doi.org/10.48550/arXiv.2407.18501"
    title: "Frank Lihui Tan & Youngah Do. (2024). The formation of perceptual space in early phonetic acquisition: a cross-linguistic modeling approach. Originally published 2023. [doi:10.48550/arXiv.2407.18501](https://doi.org/10.48550/arXiv.2407.18501)"
    author: "Frank Lihui Tan & Youngah Do"
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Model clustering performance rises monotonically with hidden dimensionality, with the steepest gains over the first three dimensions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In a dimensionality search from 1 to 15, V-measure rose consistently and monotonically with hidden dimension, with the fastest increase over the first three values; dimensionality 3 was chosen where the steep increase ceases. [→ Frank Lihui Tan & Youngah Do 2024](#frank-lihui-tan-youngah-do-2024)

## Evidence

### Frank Lihui Tan & Youngah Do 2024

Frank Lihui Tan & Youngah Do. (2024). The formation of perceptual space in early phonetic acquisition: a cross-linguistic modeling approach. Originally published 2023. [doi:10.48550/arXiv.2407.18501](https://doi.org/10.48550/arXiv.2407.18501)

`q2 · i?` · `design · r2`

Dimensionality search (hidden dimensions 1-15, 50 epochs each, evaluated by clustering V-measure on the validation set) shown in Figure 9. The authors chose dimension 3 for similarity to human learning rather than optimal performance, and report the overall pattern held at larger dimensionalities.

> "As anticipated, the model's efficacy and language learning capabilities increased with a larger hidden dimension. The results plot as shown in Figure 9 illustrates a rather consistent, monotonic rise in performance."

## Discussion


## Related Claims
- [Diagnostic model performance remains relatively stable across moderate hyperparameter ranges, with 8 attention heads and a 512 hidden dimension yielding optimal results](hyperparameter-stability-oral-diagnostic-model.md) — related

---
type: claim
title: Stopping algorithm performance is weaker for middle placement categories (labels 4 and 5)
description: Stopping algorithm performance is weaker for middle placement categories (labels 4 and 5)
id: weaker-stopping-performance-middle-labels
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2021
recheck_by: 2024
sources:
  - id: matayoshi-2021
    resource: "https://doi.org/10.1007/s40593-021-00240-8"
    title: "Matayoshi, J., Cosyn, E., & Uzun, H. (2021). Are We There Yet? Evaluating the Effectiveness of a Recurrent Neural Network-Based Stopping Algorithm for an Adaptive Assessment. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-021-00240-8"
    author: "Matayoshi, J., Cosyn, E., & Uzun, H."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Stopping algorithm performance is weaker for middle placement categories (labels 4 and 5)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Best stopping results occur for extreme labels 1 and 6; gains are not as large for labels 4 and 5, likely due to greater variability in those categories. [→ Matayoshi 2021](#matayoshi-2021)

## Evidence

### Matayoshi 2021

Matayoshi, J., Cosyn, E., & Uzun, H. (2021). Are We There Yet? Evaluating the Effectiveness of a Recurrent Neural Network-Based Stopping Algorithm for an Adaptive Assessment. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-021-00240-8

`q2 · i?` · `design · r2`

Table 4 partitions stopping statistics by ground truth label on held-out test data (GRU, α = 0.99). Label 1 averages 17.48 questions and label 6 averages 15.68, versus 24.47 and 25.34 for labels 4 and 5 respectively. The article attributes this to greater variability for labels 4 and 5 found in Doble et al. (2019).

> "The best results, in terms of both assessment length and accuracy, are for the extreme labels 1 and 6, with the average assessment length showing a substantial reduction in both cases. In comparison, while still being acceptable, the gains are not nearly as large for labels 4 and 5."

## Discussion


## Related Claims
- [Feeding ALEKS assessment state to an RNN classifier yields a large boost in placement accuracy over the assessment alone at early stopping points](rnn-boost-over-aleks-alone-early-stopping.md) — related
- [An RNN-based stopping algorithm reduces ALEKS PPL assessment length by over 26% while maintaining high accuracy](rnn-stopping-reduces-aleks-assessment-length.md) — related
- [AI scoring shows a quality-conditioned pattern: strong agreement on fully correct and fully incorrect responses but substantial degradation on mid-range responses](ai-mid-range-scoring-degradation-u-shape.md) — possibly the same claim (merge candidate)
- [Scattering varies with intelligence-age level: smallest at the lowest mental ages and possibly largest in the middle range, with age-level differences exceeding diagnostic-category differences](scattering-varies-with-mental-age-level.md) — related

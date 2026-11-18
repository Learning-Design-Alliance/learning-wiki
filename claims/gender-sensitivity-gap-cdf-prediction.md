---
type: claim
title: "Model sensitivity for predicting CDF physics outcomes is about 10% higher for men than for women"
description: "Model sensitivity for predicting CDF physics outcomes is about 10% higher for men than for women"
id: gender-sensitivity-gap-cdf-prediction
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: moderate
newest_evidence: 2020
recheck_by: 2023
sources:
  - id: seth-devore-2020
    resource: "https://doi.org/10.48550/arXiv.2002.01964"
    title: "Seth DeVore, Jie Yang, and John Stewart. (2020). Extending Machine Learning to Predict Unbalanced Physics Course Outcomes. [doi:10.48550/arXiv.2002.01964](https://doi.org/10.48550/arXiv.2002.01964)"
    author: Seth DeVore, Jie Yang, and John Stewart
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Model sensitivity for predicting CDF physics outcomes is about 10% higher for men than for women

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2023**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The random forest model correctly predicts when men will receive a C, D, or F at about a 10% higher rate than women, a gap insensitive to downsampling. [→ Seth DeVore 2020](#seth-devore-2020)

## Evidence

### Seth DeVore 2020

Seth DeVore, Jie Yang, and John Stewart. (2020). Extending Machine Learning to Predict Unbalanced Physics Course Outcomes. [doi:10.48550/arXiv.2002.01964](https://doi.org/10.48550/arXiv.2002.01964)

`q2 · i?` · `associational · r2`

Bootstrap random forest analysis comparing models including and excluding the gender variable predicting CDF outcomes (Fig. 5). The authors report the sensitivity "diﬀers by about 10% between men and women", while accuracy and specificity are higher for women; the differences were insensitive to downsampling.

> "The average sensitivity (Fig. 5(a)) diﬀers by about 10% between men and women; the model correctly predicts when men will receive a C, D, or F at a 10% higher rate than women."

## Discussion


## Related Claims
- [Classification accuracy of the optimized physics-grade model varies across demographic subgroups](subgroup-variation-physics-grade-classification.md) — possibly the same claim (merge candidate)
- [Downsampling improved minority-outcome sensitivity but was not adopted by the optimized classifier, and upsampling was ineffective](resampling-effects-physics-grade-classifier.md) — related
- [Low importance of demographic variables in physics grade prediction was not caused by sample imbalance](demographic-variable-importance-not-sample-imbalance.md) — related
- [An optimized random forest classifier for physics grades used a 50% test-train split, no downsampling, and tuned decision thresholds](optimized-rf-classifier-physics-grades.md) — related

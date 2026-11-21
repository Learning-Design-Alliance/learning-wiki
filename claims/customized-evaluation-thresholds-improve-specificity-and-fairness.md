---
type: claim
title: "Customized evaluation thresholds improve deployed transfer models: overall-optimal and group-optimal thresholds improve specificity without compromising MCC, and group-optimal thresholds further enhance fairness"
description: "Customized evaluation thresholds improve deployed transfer models: overall-optimal and group-optimal thresholds improve specificity without compromising MCC, and group-optimal thresholds further enhance fairness"
id: customized-evaluation-thresholds-improve-specificity-and-fairness
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
sources:
  - id: chengyuan-yao-2025
    title: Chengyuan Yao 2025
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: chengyuan-yao-2025-2
    title: Chengyuan Yao 2025 (2)
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Customized evaluation thresholds improve deployed transfer models: overall-optimal and group-optimal thresholds improve specificity without compromising MCC, and group-optimal thresholds further enhance fairness

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 1 causal `r2`, 1 design `r2` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Compared to the default threshold, both group-optimal and overall-optimal threshold methods improve specificity (WTNDD failed), with no substantial difference between the two; MCC distributions show no notable difference across thresholds (WTNDD passed). [→ Chengyuan Yao 2025](#chengyuan-yao-2025)
`q2 i?` Group-optimal thresholds enhance fairness, evidenced by lower Equalized Odds scores across gender and URM/non-URM groups compared to both the default and overall-optimal thresholds (WTNDD failed). [→ Chengyuan Yao 2025 (2)](#chengyuan-yao-2025-2)

## Evidence

### Chengyuan Yao 2025

Chengyuan Yao, Carmen Cortez, and Renzhe Yu. 2025. Towards Fair and Privacy-Aware Transfer Learning for Educational Predictive Modeling: A Case Study on Retention Prediction in Community Colleges. In LAK25: The 15th International Learning Analytics and Knowledge Conference (LAK 2025), March 03–07, 2025, Dublin, Ireland. ACM, New York, NY, USA, 17 pages. https://doi.org/10.1145/3706468.3706567

`q2 · i?` · `causal · r2`

Evaluation-phase comparison of default, overall-optimal, and group-optimal thresholds on direct transfer models for specificity, MCC (Fig. 9), and Equalized Odds for male vs. female and URM vs. non-URM (Fig. 10); no notable difference in EO between default and overall-optimal (WTNDD passed).

> "employing overall-optimal and group-optimal thresholds can effectively improve the model's specificity without compromising overall performance, and employing group-optimal thresholds can further enhance fairness compared to overall-optimal thresholds."

### Chengyuan Yao 2025 (2)

Chengyuan Yao, Carmen Cortez, and Renzhe Yu. 2025. Towards Fair and Privacy-Aware Transfer Learning for Educational Predictive Modeling: A Case Study on Retention Prediction in Community Colleges. In LAK25: The 15th International Learning Analytics and Knowledge Conference (LAK 2025), March 03–07, 2025, Dublin, Ireland. ACM, New York, NY, USA, 17 pages. https://doi.org/10.1145/3706468.3706567

`q2 · i?` · `design · r2`

Fairness evaluation of threshold methods on direct transfer models for gender and URM/non-URM groups, where lower EO scores indicate better model fairness; group-optimal thresholds produced "lower EO scores" than both alternatives.

> "The results indicate that the use of group-optimal thresholds enhances fairness, as evidenced by lower EO scores across gender and URM/non-URM groups compared to both the default and overall-optimal thresholds (WTNDD failed)."

## Discussion


## Related Claims
- [Default random forest settings classify only 16% of DFW students correctly in Sample 1, and tuning the decision threshold raises DFW accuracy to 43%](default-rf-poor-dfw-tuning-raises-43-percent.md) — related
- [An optimized random forest classifier for physics grades used a 50% test-train split, no downsampling, and tuned decision thresholds](optimized-rf-classifier-physics-grades.md) — related
- [Optimizing the classification threshold improves cross-dataset mind wandering detection, raising person-level correlation from 0.48 to 0.8](threshold-optimization-improves-cross-dataset-detection.md) — related
- [Classification accuracy of the optimized physics-grade model varies across demographic subgroups](subgroup-variation-physics-grade-classification.md) — related

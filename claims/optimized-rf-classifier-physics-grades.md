---
type: claim
title: "An optimized random forest classifier for physics grades used a 50% test-train split, no downsampling, and tuned decision thresholds"
description: "An optimized random forest classifier for physics grades used a 50% test-train split, no downsampling, and tuned decision thresholds"
id: optimized-rf-classifier-physics-grades
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

# An optimized random forest classifier for physics grades used a 50% test-train split, no downsampling, and tuned decision thresholds

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2023**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The optimized classification model combined a 50% test-train split, no downsampling, and decision thresholds of 0.30 (DF) and 0.45 (CDF). [→ Seth DeVore 2020](#seth-devore-2020)

## Evidence

### Seth DeVore 2020

Seth DeVore, Jie Yang, and John Stewart. (2020). Extending Machine Learning to Predict Unbalanced Physics Course Outcomes. [doi:10.48550/arXiv.2002.01964](https://doi.org/10.48550/arXiv.2002.01964)

`q2 · i?` · `associational · r2`

Bootstrap-based random forest modeling of 7184 Physics 1 students' institutional records. The authors state the optimal model used a 50% test-train split, no downsampling, and the tuned thresholds, and report "a balance of sensitivity and PPV" with κ in the moderate-agreement range for CDF and fair-agreement range for DF.

> "This model has a balance of sensitivity and PPV. For the CDF outcome, the overall accuracy is slightly better than that found for only institutional variables in Study 1"

## Discussion


## Related Claims
- [Adjusting the random forest decision threshold raises correct classification of D or F physics outcomes to 46%](decision-threshold-tuning-raises-df-sensitivity.md) — related
- [Downsampling improved minority-outcome sensitivity but was not adopted by the optimized classifier, and upsampling was ineffective](resampling-effects-physics-grade-classifier.md) — related
- [Model sensitivity for predicting CDF physics outcomes is about 10% higher for men than for women](gender-sensitivity-gap-cdf-prediction.md) — related
- [Classification accuracy of the optimized physics-grade model varies across demographic subgroups](subgroup-variation-physics-grade-classification.md) — related
- [Model performance metrics stabilize once the minority outcome training sample reaches roughly 100 students](minority-sample-size-100-threshold-physics-prediction.md) — related
- [Default random forest settings classify only 16% of DFW students correctly in Sample 1, and tuning the decision threshold raises DFW accuracy to 43%](default-rf-poor-dfw-tuning-raises-43-percent.md) — related
- [Demographic variables (gender, URM, first-generation, SES) were of low importance in the DFW classification models, and subgroup classification accuracy was approximately equal to the overall model](demographic-variables-low-importance-dfw-models.md) — related
- [Customized evaluation thresholds improve deployed transfer models: overall-optimal and group-optimal thresholds improve specificity without compromising MCC, and group-optimal thresholds further enhance fairness](customized-evaluation-thresholds-improve-specificity-and-fairness.md) — related

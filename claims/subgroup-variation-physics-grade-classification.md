---
type: claim
title: Classification accuracy of the optimized physics-grade model varies across demographic subgroups
description: Classification accuracy of the optimized physics-grade model varies across demographic subgroups
id: subgroup-variation-physics-grade-classification
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
  - id: seth-devore-2020-2
    resource: "https://doi.org/10.48550/arXiv.2002.01964"
    title: "Seth DeVore, Jie Yang, and John Stewart. (2020). Extending Machine Learning to Predict Unbalanced Physics Course Outcomes. [doi:10.48550/arXiv.2002.01964](https://doi.org/10.48550/arXiv.2002.01964)"
    author: Seth DeVore, Jie Yang, and John Stewart
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Classification accuracy of the optimized physics-grade model varies across demographic subgroups

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2023**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The optimized model showed substantially lower sensitivity and higher specificity for women than the overall model when predicting CDF outcomes. [→ Seth DeVore 2020](#seth-devore-2020)
`q2 i?` For URM and non-CalReady students, model sensitivity was substantially higher and specificity lower than the overall model. [→ Seth DeVore 2020 (2)](#seth-devore-2020-2)

## Evidence

### Seth DeVore 2020

Seth DeVore, Jie Yang, and John Stewart. (2020). Extending Machine Learning to Predict Unbalanced Physics Course Outcomes. [doi:10.48550/arXiv.2002.01964](https://doi.org/10.48550/arXiv.2002.01964)

`q2 · i?` · `associational · r2`

Characterization of the optimized classifier, trained on the full training set, on each minority subgroup in the test dataset (Table V). The authors report "substantially lower sensitivity and higher speciﬁcity for women with approximately equal PPV"; the abstract gives 61% sensitivity for women predicting CDF.

> "For the CDF outcome, the models have substantially lower sensitivity and higher speciﬁcity for women with approximately equal PPV consistent with Fig. 5."

### Seth DeVore 2020 (2)

Seth DeVore, Jie Yang, and John Stewart. (2020). Extending Machine Learning to Predict Unbalanced Physics Course Outcomes. [doi:10.48550/arXiv.2002.01964](https://doi.org/10.48550/arXiv.2002.01964)

`q2 · i?` · `associational · r2`

Same subgroup characterization of the optimized classifier (Table V). The authors report that for URM and non-CalReady students "the model’s sensitivity is substantially higher and speciﬁcity lower than the overall model"; the abstract gives 67% sensitivity for URM and 78% for first-generation students predicting CDF.

> "Conversely, for both URM students and non-CalReady students, the model’s sensitivity is substantially higher and speciﬁcity lower than the overall model."

## Discussion


## Related Claims
- [Model sensitivity for predicting CDF physics outcomes is about 10% higher for men than for women](gender-sensitivity-gap-cdf-prediction.md) — possibly the same claim (merge candidate)
- [An optimized random forest classifier for physics grades used a 50% test-train split, no downsampling, and tuned decision thresholds](optimized-rf-classifier-physics-grades.md) — related
- [Downsampling improved minority-outcome sensitivity but was not adopted by the optimized classifier, and upsampling was ineffective](resampling-effects-physics-grade-classifier.md) — related
- [Demographic variables (gender, URM, first-generation, SES) were of low importance in the DFW classification models, and subgroup classification accuracy was approximately equal to the overall model](demographic-variables-low-importance-dfw-models.md) — reports the opposite
- [Default random forest settings classify only 16% of DFW students correctly in Sample 1, and tuning the decision threshold raises DFW accuracy to 43%](default-rf-poor-dfw-tuning-raises-43-percent.md) — related

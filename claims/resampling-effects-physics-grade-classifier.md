---
type: claim
title: Downsampling improved minority-outcome sensitivity but was not adopted by the optimized classifier, and upsampling was ineffective
description: Downsampling improved minority-outcome sensitivity but was not adopted by the optimized classifier, and upsampling was ineffective
id: resampling-effects-physics-grade-classifier
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: mixed
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

# Downsampling improved minority-outcome sensitivity but was not adopted by the optimized classifier, and upsampling was ineffective

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2023**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Downsampling the majority class decreased accuracy, specificity, and PPV while increasing correct prediction of the minority DF outcome. [→ Seth DeVore 2020](#seth-devore-2020)
`q2 i?` Upsampling was ineffective for this sample, and grid search led the optimized classifier to use no downsampling. [→ Seth DeVore 2020 (2)](#seth-devore-2020-2)

## Evidence

### Seth DeVore 2020

Seth DeVore, Jie Yang, and John Stewart. (2020). Extending Machine Learning to Predict Unbalanced Physics Course Outcomes. [doi:10.48550/arXiv.2002.01964](https://doi.org/10.48550/arXiv.2002.01964)

`q2 · i?` · `associational · r2`

Bootstrap random forest analysis varying the majority-to-minority training ratio for the DF outcome (Fig. 2). The authors report that as the majority class was downsampled, accuracy and specificity decreased, correct prediction of the minority outcome dramatically increased, and "PPV... also decreases with downsampling".

> "The PPV, the fraction of correct positive predictions, also decreases with downsampling. This may be a result of less data being provided to train the algorithm resulting in more incorrect classiﬁcations."

### Seth DeVore 2020 (2)

Seth DeVore, Jie Yang, and John Stewart. (2020). Extending Machine Learning to Predict Unbalanced Physics Course Outcomes. [doi:10.48550/arXiv.2002.01964](https://doi.org/10.48550/arXiv.2002.01964)

`q2 · i?` · `associational · r2`

Bootstrap random forest analysis replicating minority-class students to balance the DF training sample. The authors report "upsampling was completely inef- fective at producing the changes in model performance that downsampling produced"; a grid search over downsampling rate and decision threshold led the optimized classifier to use no downsampling.

> "For this sample, upsampling was completely inef- fective at producing the changes in model performance that downsampling produced."

## Discussion


## Related Claims
- [Adjusting the random forest decision threshold raises correct classification of D or F physics outcomes to 46%](decision-threshold-tuning-raises-df-sensitivity.md) — related
- [Model sensitivity for predicting CDF physics outcomes is about 10% higher for men than for women](gender-sensitivity-gap-cdf-prediction.md) — related
- [Model performance metrics stabilize once the minority outcome training sample reaches roughly 100 students](minority-sample-size-100-threshold-physics-prediction.md) — related
- [An optimized random forest classifier for physics grades used a 50% test-train split, no downsampling, and tuned decision thresholds](optimized-rf-classifier-physics-grades.md) — related
- [An expert dataset of 4803 annotated chest compressions from 10 experts was collected and downsampled to 3434 samples to train the mistake-detection models](cpr-tutor-expert-dataset-4803-ccs.md) — related
- [Hungarian transformer models achieve slightly lower overall score (about 68%) but better minority-class sensitivity than shallow models](transformers-better-minority-class-sensitivity.md) — related
- [Classification accuracy of the optimized physics-grade model varies across demographic subgroups](subgroup-variation-physics-grade-classification.md) — related

---
type: claim
title: Model performance metrics stabilize once the minority outcome training sample reaches roughly 100 students
description: Model performance metrics stabilize once the minority outcome training sample reaches roughly 100 students
id: minority-sample-size-100-threshold-physics-prediction
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

# Model performance metrics stabilize once the minority outcome training sample reaches roughly 100 students

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2023**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Precision of random forest performance metrics increases with minority outcome training sample size up to approximately 100, then becomes approximately constant. [→ Seth DeVore 2020](#seth-devore-2020)

## Evidence

### Seth DeVore 2020

Seth DeVore, Jie Yang, and John Stewart. (2020). Extending Machine Learning to Predict Unbalanced Physics Course Outcomes. [doi:10.48550/arXiv.2002.01964](https://doi.org/10.48550/arXiv.2002.01964)

`q2 · i?` · `associational · r2`

Bootstrap analysis downsampling the training dataset while holding the test dataset fixed, plotting accuracy, sensitivity, specificity, and PPV against minority outcome training size (Fig. 1). The authors report performance measures become "approximately constant" above roughly 100 minority cases; 220 minority students gave sensitivity precision of 0.025 for CDF.

> "For all performance metrics, there is a weak increase up to a minority outcome sample size of approximately 100 with all performance measures becoming approximately constant above his value."

## Discussion


## Related Claims
- [Random forest achieves the highest mean test accuracy (0.9590) of all models compared for predicting exam grade categories from physiological signals](random-forest-highest-accuracy-physiological-exam-prediction.md) — related
- [Downsampling improved minority-outcome sensitivity but was not adopted by the optimized classifier, and upsampling was ineffective](resampling-effects-physics-grade-classifier.md) — related
- [An optimized random forest classifier for physics grades used a 50% test-train split, no downsampling, and tuned decision thresholds](optimized-rf-classifier-physics-grades.md) — related

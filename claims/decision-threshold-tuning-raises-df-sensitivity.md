---
type: claim
title: "Adjusting the random forest decision threshold raises correct classification of D or F physics outcomes to 46%"
description: "Adjusting the random forest decision threshold raises correct classification of D or F physics outcomes to 46%"
id: decision-threshold-tuning-raises-df-sensitivity
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

# Adjusting the random forest decision threshold raises correct classification of D or F physics outcomes to 46%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2023**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Tuning the decision threshold of a random forest classifier improved sensitivity for the unbalanced D or F outcome in introductory physics. [→ Seth DeVore 2020](#seth-devore-2020)

## Evidence

### Seth DeVore 2020

Seth DeVore, Jie Yang, and John Stewart. (2020). Extending Machine Learning to Predict Unbalanced Physics Course Outcomes. [doi:10.48550/arXiv.2002.01964](https://doi.org/10.48550/arXiv.2002.01964)

`q2 · i?` · `associational · r2`

Bootstrap-based random forest analysis of institutional records for Physics 1 students, plotting performance metrics against decision threshold (Fig. 3). The authors report that a "decision threshold of 0 .3 provided a balance of sensitivity and PPV (and optimizes the F1 statistics)" for the DF outcome; the abstract states the correct classification rate rose to 46%.

> "A decision threshold around 0 .15 provides a balance of sensitivity and speciﬁcity; however, at this threshold the PPV is poor. A decision threshold of 0 .3 provided a balance of sensitivity and PPV (and optimizes the F1 statistics)."

## Discussion


## Related Claims
- [An optimized random forest classifier for physics grades used a 50% test-train split, no downsampling, and tuned decision thresholds](optimized-rf-classifier-physics-grades.md) — related
- [Downsampling improved minority-outcome sensitivity but was not adopted by the optimized classifier, and upsampling was ineffective](resampling-effects-physics-grade-classifier.md) — related
- [Default random forest settings classify only 16% of DFW students correctly in Sample 1, and tuning the decision threshold raises DFW accuracy to 43%](default-rf-poor-dfw-tuning-raises-43-percent.md) — related

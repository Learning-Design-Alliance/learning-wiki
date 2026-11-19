---
type: claim
title: "Default random forest settings classify only 16% of DFW students correctly in Sample 1, and tuning the decision threshold raises DFW accuracy to 43%"
description: "Default random forest settings classify only 16% of DFW students correctly in Sample 1, and tuning the decision threshold raises DFW accuracy to 43%"
id: default-rf-poor-dfw-tuning-raises-43-percent
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: moderate
newest_evidence: 2020
recheck_by: 2023
sources:
  - id: jie-yang-2020
    resource: "https://doi.org/10.1103/physrevphyseducres.16.020130"
    title: "Jie Yang, Seth DeVore, Dona Hewagallage, Paul Miller, Qing X. Ryan, and John Stewart. (2020). Using Machine Learning to Identify the Most At-Risk Students in Physics Classes. [doi:10.1103/physrevphyseducres.16.020130](https://doi.org/10.1103/physrevphyseducres.16.020130)"
    author: Jie Yang, Seth DeVore, Dona Hewagallage, Paul Miller, Qing X. Ryan, and John Stewart
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: jie-yang-2020-2
    resource: "https://doi.org/10.1103/physrevphyseducres.16.020130"
    title: "Jie Yang, Seth DeVore, Dona Hewagallage, Paul Miller, Qing X. Ryan, and John Stewart. (2020). Using Machine Learning to Identify the Most At-Risk Students in Physics Classes. [doi:10.1103/physrevphyseducres.16.020130](https://doi.org/10.1103/physrevphyseducres.16.020130)"
    author: Jie Yang, Seth DeVore, Dona Hewagallage, Paul Miller, Qing X. Ryan, and John Stewart
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Default random forest settings classify only 16% of DFW students correctly in Sample 1, and tuning the decision threshold raises DFW accuracy to 43%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2023**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Using the default 50% voting threshold, the Sample 1 random forest identified only 16% of actual DFW students, a result of the unbalanced outcome. [→ Jie Yang 2020](#jie-yang-2020)
`q2 i?` Tuning the decision threshold to 32% of trees voting DFW improved DFW accuracy to 43% with kappa = 0.36 and AUC = 0.68. [→ Jie Yang 2020 (2)](#jie-yang-2020-2)

## Evidence

### Jie Yang 2020

Jie Yang, Seth DeVore, Dona Hewagallage, Paul Miller, Qing X. Ryan, and John Stewart. (2020). Using Machine Learning to Identify the Most At-Risk Students in Physics Classes. [doi:10.1103/physrevphyseducres.16.020130](https://doi.org/10.1103/physrevphyseducres.16.020130)

`q2 · i?` · `associational · r2`

Random forest classification of Sample 1 (N = 7184, introductory mechanics, 2000–2018) using the default randomForest package threshold. The article reports "only 16% of the DFW students identified" and attributes this to the unbalanced outcome, with only 12% DFW.

> "The model has very poor DFW accuracy with only 16% of the DFW students identified. It also has fairly poor κ and AUC. This poor performance results from the unbalanced DFW outcome where only 12% of the students receive a D, F, or W."

### Jie Yang 2020 (2)

Jie Yang, Seth DeVore, Dona Hewagallage, Paul Miller, Qing X. Ryan, and John Stewart. (2020). Using Machine Learning to Identify the Most At-Risk Students in Physics Classes. [doi:10.1103/physrevphyseducres.16.020130](https://doi.org/10.1103/physrevphyseducres.16.020130)

`q2 · i?` · `associational · r2`

Threshold-tuned Sample 1 model balancing DFW accuracy and precision. The article reports DFW accuracy improved to 43%, "κ = 0.36 represented fair agreement", and AUC = 0.68, below the 0.80 threshold for excellent discrimination.

> "A threshold of 32% of trees voting for the DFW classification produced the Overall model which balanced DFW accuracy and precision. This model substantially improved DFW accuracy to 43% at the expense of lower DFW precision and had substantially better κ and AUC; κ = 0.36 represented fair agreement; however, the AUC value of 0.68 was well below Hosmer's threshold of 0.80 for excellent discrimination."

## Discussion


## Related Claims
- [An optimized random forest classifier for physics grades used a 50% test-train split, no downsampling, and tuned decision thresholds](optimized-rf-classifier-physics-grades.md) — related
- [Adjusting the random forest decision threshold raises correct classification of D or F physics outcomes to 46%](decision-threshold-tuning-raises-df-sensitivity.md) — related
- [Downsampling improved minority-outcome sensitivity but was not adopted by the optimized classifier, and upsampling was ineffective](resampling-effects-physics-grade-classifier.md) — related
- [A random forest restricted to the variable set available for Sample 3 performed more weakly, with DFW accuracy reduced by 7%, indicating richer institutional data improves classification](restricted-variable-set-reduces-dfw-accuracy-7-percent.md) — related
- [Classification accuracy of the optimized physics-grade model varies across demographic subgroups](subgroup-variation-physics-grade-classification.md) — related
- [A random forest model trained on U.S. PISA data identifies top-decile U.S. science achievers with 71.6% accuracy](us-trained-model-71-6-accuracy-top-decile.md) — related

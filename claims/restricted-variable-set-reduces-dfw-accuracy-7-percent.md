---
type: claim
title: "A random forest restricted to the variable set available for Sample 3 performed more weakly, with DFW accuracy reduced by 7%, indicating richer institutional data improves classification"
description: "A random forest restricted to the variable set available for Sample 3 performed more weakly, with DFW accuracy reduced by 7%, indicating richer institutional data improves classification"
id: restricted-variable-set-reduces-dfw-accuracy-7-percent
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
---

# A random forest restricted to the variable set available for Sample 3 performed more weakly, with DFW accuracy reduced by 7%, indicating richer institutional data improves classification

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2023**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The Restricted model built on a subset of Sample 1 variables similar to Sample 3's had DFW accuracy reduced by 7% relative to the Overall model. [→ Jie Yang 2020](#jie-yang-2020)

## Evidence

### Jie Yang 2020

Jie Yang, Seth DeVore, Dona Hewagallage, Paul Miller, Qing X. Ryan, and John Stewart. (2020). Using Machine Learning to Identify the Most At-Risk Students in Physics Classes. [doi:10.1103/physrevphyseducres.16.020130](https://doi.org/10.1103/physrevphyseducres.16.020130)

`q2 · i?` · `associational · r2`

Sample 1 classification model restricted to variables comparable to those available for Sample 3 (commonly supplied institutional variables). The article reports DFW accuracy was "reduced by 7%" relative to the Overall model.

> "As one might expect, the Restricted model using fewer variables performed more weakly than the Overall model with DFW accuracy reduced by 7%."

## Discussion


## Related Claims
- [Default random forest settings classify only 16% of DFW students correctly in Sample 1, and tuning the decision threshold raises DFW accuracy to 43%](default-rf-poor-dfw-tuning-raises-43-percent.md) — related
- [Combining institutional and in-class data gave the highest DFW classification performance in Sample 2, improving over institutional-only models by 3% in week 1 to 18% in week 8](institutional-plus-inclass-data-highest-dfw-performance.md) — related
- [Demographic variables (gender, URM, first-generation, SES) were of low importance in the DFW classification models, and subgroup classification accuracy was approximately equal to the overall model](demographic-variables-low-importance-dfw-models.md) — related
- [In-class-only DFW models perform more weakly than institutional-only models early in the semester but exceed them after the first test in week 5](inclass-only-models-exceed-institutional-after-test1.md) — related

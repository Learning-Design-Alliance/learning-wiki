---
type: claim
title: Recursive feature elimination finds the optimum predictive model uses only two features — taking modern physics and taking an engineering course as a physics major
description: Recursive feature elimination finds the optimum predictive model uses only two features — taking modern physics and taking an engineering course as a physics major
id: rfe-two-feature-optimum-model
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: moderate
newest_evidence: 2019
recheck_by: 2022
sources:
  - id: john-m-aiken-2019
    resource: "https://doi.org/10.1103/physrevphyseducres.15.010128"
    title: "John M. Aiken, Rachel Henderson, and Marcos D. Caballero. (2019). Modeling student pathways in a physics bachelor's degree program. [doi:10.1103/physrevphyseducres.15.010128](https://doi.org/10.1103/physrevphyseducres.15.010128)"
    author: John M. Aiken, Rachel Henderson, and Marcos D. Caballero
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Recursive feature elimination finds the optimum predictive model uses only two features — taking modern physics and taking an engineering course as a physics major

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2019 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2022**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Recursive feature elimination identified a two-feature optimum; including additional features reduced accuracy, though a few added small AUC gains. [→ John M. Aiken 2019](#john-m-aiken-2019)

## Evidence

### John M. Aiken 2019

John M. Aiken, Rachel Henderson, and Marcos D. Caballero. (2019). Modeling student pathways in a physics bachelor's degree program. [doi:10.1103/physrevphyseducres.15.010128](https://doi.org/10.1103/physrevphyseducres.15.010128)

`q2 · i?` · `associational · r2`

Recursive Model: RFE applied to the full data set (N=1422) using grid-searched parameters, producing AUC and accuracy curves across feature counts (Figure 4). The article reports AUC increased slightly at a small expense of accuracy when adding high physics 1, 2, and calculus 2 grades, calculus 2 timing, and gender.

> "the optimum model had two features: taking modern physics and taking an engineering course as a physics major (Figure 4). Including any additional features reduced the accuracy of the model."

## Discussion


## Related Claims
- [Taking an engineering course while registered as a physics major is the second most important predictor of switching from physics to an engineering degree](engineering-course-while-physics-major-predicts-switch.md) — related
- [Taking the third-semester modern physics course is the single most important feature in a random forest model predicting whether a declared physics major earns a physics or an engineering degree](modern-physics-course-most-important-predictor-physics-degree.md) — related
- [Taking modern physics has the highest, though still relatively small, effect size in a contingency table analysis of physics versus engineering graduates](modern-physics-highest-effect-size-contingency.md) — related

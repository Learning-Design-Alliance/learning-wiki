---
type: claim
title: "A conditional inference random forest model predicts physics PhD admissions decisions on held-out data with 75.8% average accuracy"
description: "A conditional inference random forest model predicts physics PhD admissions decisions on held-out data with 75.8% average accuracy"
id: random-forest-predicts-physics-phd-admissions-75-8-percent
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: moderate
newest_evidence: 2020
recheck_by: 2023
sources:
  - id: nicholas-t-young-and-marcos-d-caballero-2020
    resource: "https://doi.org/10.1119/perc.2019.pr.young"
    title: "Nicholas T. Young and Marcos D. Caballero. (2020). Using machine learning to understand physics graduate school admissions. Originally published 2019. [doi:10.1119/perc.2019.pr.young](https://doi.org/10.1119/perc.2019.pr.young)"
    author: Nicholas T. Young and Marcos D. Caballero
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# A conditional inference random forest model predicts physics PhD admissions decisions on held-out data with 75.8% average accuracy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2023**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across 30 runs, the model's average accuracy on held-out data was 75.8% ± 0.6% and its average AUC was .821 ± .002. [→ Nicholas T. Young and Marcos D. Caballero 2020](#nicholas-t-young-and-marcos-d-caballero-2020)

## Evidence

### Nicholas T. Young and Marcos D. Caballero 2020

Nicholas T. Young and Marcos D. Caballero. (2020). Using machine learning to understand physics graduate school admissions. Originally published 2019. [doi:10.1119/perc.2019.pr.young](https://doi.org/10.1119/perc.2019.pr.young)

`q2 · i?` · `associational · r1`

Numerical modeling result from the Results section of a supervised machine learning analysis of 512 domestic applicants to one physics PhD program, using a conditional inference forest with 500 trees and 70% training splits. The article reports the accuracy "75.8% ± 0.6%" and the average AUC ".821 ± .002" on held-out data.

> "Across the 30 runs, the average accuracy of our model pre- dicting on the held-out data was 75.8% ± 0.6% and the aver- age AUC was .821 ± .002."

## Discussion


## Related Claims
- [A two-factor model using only undergraduate GPA and physics GRE matches the full model's predictive performance](two-factor-gpa-physics-gre-model-matches-full-model.md) — related
- [A reduced model using only the five meaningful features performs nearly as well as the full 44-feature model](five-feature-model-nearly-full-performance.md) — related
- [After rubric implementation, admissions decisions from application data could not be acceptably modeled, even with hyperparameter tuning](post-rubric-application-data-unmodelable.md) — related
- [A conditional inference forest acceptably models pre-rubric physics graduate admissions decisions, with physics GRE score, quantitative GRE score, and undergraduate GPA the only meaningful features](pre-rubric-admissions-model-quantitative-metrics-meaningful.md) — related
- [The conditional inference forest achieves mostly outstanding AUC (>0.9) stable across cut-offs, and three features suffice for AUC near 0.9](cif-auc-stable-three-features.md) — related

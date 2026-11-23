---
type: claim
title: A reduced model using only the five meaningful features performs nearly as well as the full 44-feature model
description: A reduced model using only the five meaningful features performs nearly as well as the full 44-feature model
id: five-feature-model-nearly-full-performance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: moderate
newest_evidence: 2019
recheck_by: 2022
sources:
  - id: nicholas-t-young-2019
    resource: "https://doi.org/10.1103/physrevphyseducres.15.010114"
    title: "Nicholas T. Young, Grant Allen, John M. Aiken, Rachel Henderson, and Marcos D. Caballero. (2019). Identifying features predictive of faculty integrating computation into physics courses. [doi:10.1103/physrevphyseducres.15.010114](https://doi.org/10.1103/physrevphyseducres.15.010114)"
    author: Nicholas T. Young, Grant Allen, John M. Aiken, Rachel Henderson, and Marcos D. Caballero
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# A reduced model using only the five meaningful features performs nearly as well as the full 44-feature model

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2019 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2022**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` A conditional inference forest using only the five meaningful variables achieved average accuracy of 76.4%±0.4% and AUC of 0.818±0.002, compared with 77.4%±0.5% and 0.838±0.002 for the full model. [→ Nicholas T. Young 2019](#nicholas-t-young-2019)

## Evidence

### Nicholas T. Young 2019

Nicholas T. Young, Grant Allen, John M. Aiken, Rachel Henderson, and Marcos D. Caballero. (2019). Identifying features predictive of faculty integrating computation into physics courses. [doi:10.1103/physrevphyseducres.15.010114](https://doi.org/10.1103/physrevphyseducres.15.010114)

`q2 · i?` · `associational · r2`

Validation rerun of the conditional inference forest restricted to the five meaningful variables, 30 trials as printed; the article notes the five-variable AUC remained above 0.8.

> "we then reran the cforest algorithm 30 times with just these ﬁve variables. We obtained an average accuracy of 76.4%± 0.4% and an AUC of 0.818 ± 0.002."

## Discussion


## Related Claims
- [A reduced model using only the six top-ranked predictors maintains relatively similar MD prediction performance (AUC .776)](six-predictor-md-model-auc-776.md) — related
- [The most predictive factors of faculty having experience teaching computation are using computation in research with students, not personally using computation, and beliefs that computation brings new physics and new problems to the classroom](meaningful-factors-faculty-computation-teaching.md) — related
- [A conditional inference random forest model predicts physics PhD admissions decisions on held-out data with 75.8% average accuracy](random-forest-predicts-physics-phd-admissions-75-8-percent.md) — related
- [A two-factor model using only undergraduate GPA and physics GRE matches the full model's predictive performance](two-factor-gpa-physics-gre-model-matches-full-model.md) — related
- [A conditional inference forest acceptably models pre-rubric physics graduate admissions decisions, with physics GRE score, quantitative GRE score, and undergraduate GPA the only meaningful features](pre-rubric-admissions-model-quantitative-metrics-meaningful.md) — related
- [The conditional inference forest achieves mostly outstanding AUC (>0.9) stable across cut-offs, and three features suffice for AUC near 0.9](cif-auc-stable-three-features.md) — related

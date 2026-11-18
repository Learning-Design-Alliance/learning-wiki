---
type: claim
title: "A two-factor model using only undergraduate GPA and physics GRE matches the full model's predictive performance"
description: "A two-factor model using only undergraduate GPA and physics GRE matches the full model's predictive performance"
id: two-factor-gpa-physics-gre-model-matches-full-model
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
    rigour: 2
---

# A two-factor model using only undergraduate GPA and physics GRE matches the full model's predictive performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2023**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Rerunning the model 30 times with only physics GRE score and GPA as predictors gave 75.8% ± 0.6% accuracy and AUC .817 ± .003, not statistically different from the fourteen-factor model. [→ Nicholas T. Young and Marcos D. Caballero 2020](#nicholas-t-young-and-marcos-d-caballero-2020)

## Evidence

### Nicholas T. Young and Marcos D. Caballero 2020

Nicholas T. Young and Marcos D. Caballero. (2020). Using machine learning to understand physics graduate school admissions. Originally published 2019. [doi:10.1119/perc.2019.pr.young](https://doi.org/10.1119/perc.2019.pr.young)

`q2 · i?` · `associational · r2`

Verification rerun of the conditional inference random forest using only two predictors, reported in the Results section. The article reports "75.8% ± 0.6%" accuracy and ".817 ± .003" AUC, statistically indistinguishable from the full model's performance.

> "Our average accuracy was then 75.8% ± 0.6% and our average area under the curve was .817 ± .003, which are not statistically different from the values we found using all fourteen factors shown in table I."

## Discussion


## Related Claims
- [Physics GRE score and undergraduate GPA are the only meaningful admissions factors at the studied program](physics-gre-and-gpa-only-meaningful-admissions-factors.md) — possibly the same claim (merge candidate)
- [A conditional inference random forest model predicts physics PhD admissions decisions on held-out data with 75.8% average accuracy](random-forest-predicts-physics-phd-admissions-75-8-percent.md) — related
- [A reduced model using only the five meaningful features performs nearly as well as the full 44-feature model](five-feature-model-nearly-full-performance.md) — related

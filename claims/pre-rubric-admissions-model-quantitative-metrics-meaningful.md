---
type: claim
title: A conditional inference forest acceptably models pre-rubric physics graduate admissions decisions, with physics GRE score, quantitative GRE score, and undergraduate GPA the only meaningful features
description: A conditional inference forest acceptably models pre-rubric physics graduate admissions decisions, with physics GRE score, quantitative GRE score, and undergraduate GPA the only meaningful features
id: pre-rubric-admissions-model-quantitative-metrics-meaningful
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2021
recheck_by: 2024
sources:
  - id: nicholas-t-young-2021
    resource: "https://doi.org/10.48550/arXiv.2112.06886"
    title: "Nicholas T. Young, N. Verboncoeur, Dao Chi Lam, and Marcos D. Caballero. (2021). Rubric-based holistic review represents a change from traditional graduate admissions approaches in physics. [doi:10.48550/arXiv.2112.06886](https://doi.org/10.48550/arXiv.2112.06886)"
    author: Nicholas T. Young, N. Verboncoeur, Dao Chi Lam, and Marcos D. Caballero
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: nicholas-t-young-2021-2
    resource: "https://doi.org/10.48550/arXiv.2112.06886"
    title: "Nicholas T. Young, N. Verboncoeur, Dao Chi Lam, and Marcos D. Caballero. (2021). Rubric-based holistic review represents a change from traditional graduate admissions approaches in physics. [doi:10.48550/arXiv.2112.06886](https://doi.org/10.48550/arXiv.2112.06886)"
    author: Nicholas T. Young, N. Verboncoeur, Dao Chi Lam, and Marcos D. Caballero
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# A conditional inference forest acceptably models pre-rubric physics graduate admissions decisions, with physics GRE score, quantitative GRE score, and undergraduate GPA the only meaningful features

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r1`–`r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` A random forest model of pre-rubric admissions data achieved acceptable predictive performance (testing AUC 0.756). [→ Nicholas T. Young 2021](#nicholas-t-young-2021)
`q2 i?` Recursive backward elimination identified physics GRE score, quantitative GRE score, and undergraduate GPA as the only meaningful factors predictive of admission before the rubric. [→ Nicholas T. Young 2021 (2)](#nicholas-t-young-2021-2)

## Evidence

### Nicholas T. Young 2021

Nicholas T. Young, N. Verboncoeur, Dao Chi Lam, and Marcos D. Caballero. (2021). Rubric-based holistic review represents a change from traditional graduate admissions approaches in physics. [doi:10.48550/arXiv.2112.06886](https://doi.org/10.48550/arXiv.2112.06886)

`q2 · i?` · `associational · r2`

Conditional inference forest analysis of 512 domestic applications to enroll 2014-2017 (48% admitted), run 30 times with 70% training splits. The "average testing AUC was 0.756±.006", above the 0.7 threshold the authors use for an acceptable model, and accuracy exceeded the null accuracy of 52.7%.

> "Across the 30 runs, the average accuracy of our model predicting on the held-out data was 75 .6%± 0.6%, the average training AUC was 0.849±0.002, and the average testing AUC was 0.756±.006."

### Nicholas T. Young 2021 (2)

Nicholas T. Young, N. Verboncoeur, Dao Chi Lam, and Marcos D. Caballero. (2021). Rubric-based holistic review represents a change from traditional graduate admissions approaches in physics. [doi:10.48550/arXiv.2112.06886](https://doi.org/10.48550/arXiv.2112.06886)

`q2 · i?` · `associational · r1`

Feature-importance analysis of the same pre-rubric admissions model. A three-feature model using only these factors achieved testing accuracy of 75.4%±0.6% and AUC 0.754±0.006, "not statistically diﬀerent from the values we found using all fourteen factors".

> "Using recursive backward elimination to determine the meaningful factors, we ﬁnd the applicant's physics GRE score, quantitative GRE score, and their undergraduate GPA to be the only meaningful factors."

## Discussion


## Related Claims
- [After rubric implementation, admissions decisions from application data could not be acceptably modeled, even with hyperparameter tuning](post-rubric-application-data-unmodelable.md) — related
- [A conditional inference random forest model predicts physics PhD admissions decisions on held-out data with 75.8% average accuracy](random-forest-predicts-physics-phd-admissions-75-8-percent.md) — related
- [Models built from faculty rubric ratings also failed to reach acceptable predictive performance, with physics GRE score and quality of work the meaningful features](rubric-rating-data-unmodelable.md) — related
- [Physics GRE score and undergraduate GPA are the only meaningful admissions factors at the studied program](physics-gre-and-gpa-only-meaningful-admissions-factors.md) — related
- [A reduced model using only the five meaningful features performs nearly as well as the full 44-feature model](five-feature-model-nearly-full-performance.md) — related
- [Admissions predictions show a rough physics GRE cutoff around 700 that high GPA can partially compensate below](rough-physics-gre-cutoff-700-gpa-compensation.md) — related
- [The authors interpret their modeling results as evidence that rubric-based holistic review could make physics graduate admissions more equitable](rubric-holistic-review-could-increase-equity.md) — related
- [Removing Tomek Links improved model metrics for all three data sets, but post-rubric models remained below acceptable performance](tomek-links-improve-metrics-insufficiently.md) — related
- [Rubric-based holistic review that considers more than test scores and GPA increased the demographic diversity of admitted graduate students at the University of Michigan](rubric-holistic-review-diversity-gains.md) — related

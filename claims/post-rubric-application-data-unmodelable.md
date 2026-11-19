---
type: claim
title: After rubric implementation, admissions decisions from application data could not be acceptably modeled, even with hyperparameter tuning
description: After rubric implementation, admissions decisions from application data could not be acceptably modeled, even with hyperparameter tuning
id: post-rubric-application-data-unmodelable
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
    rigour: 1
---

# After rubric implementation, admissions decisions from application data could not be acceptably modeled, even with hyperparameter tuning

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The model of post-rubric application data had a testing AUC of 0.626, below the 0.7 threshold for a reasonable model, and accuracy only slightly above the null accuracy. [→ Nicholas T. Young 2021](#nicholas-t-young-2021)

## Evidence

### Nicholas T. Young 2021

Nicholas T. Young, N. Verboncoeur, Dao Chi Lam, and Marcos D. Caballero. (2021). Rubric-based holistic review represents a change from traditional graduate admissions approaches in physics. [doi:10.48550/arXiv.2112.06886](https://doi.org/10.48550/arXiv.2112.06886)

`q2 · i?` · `associational · r1`

Conditional inference forest analysis of 511 domestic applications to enroll 2018-2020 (34% admitted), the same modeling procedure as the pre-rubric data set. The null accuracy was 66.0%, so the model was "only doing slightly better than if it were to predict everyone was not admitted".

> "the average accuracy of our model predicting on the held-out data was 71 .4%± 0.6%, the average training AUC was 0.720±0.004, and the average testing AUC was 0.626±.006, which is less than the minimum of 0.7 for a reasonable model."

## Discussion


## Related Claims
- [Cross-dataset testing and the 5x2 cv combined F-test indicate the admissions process changed after rubric implementation](model-comparison-indicates-process-changed.md) — related
- [A conditional inference forest acceptably models pre-rubric physics graduate admissions decisions, with physics GRE score, quantitative GRE score, and undergraduate GPA the only meaningful features](pre-rubric-admissions-model-quantitative-metrics-meaningful.md) — related
- [Removing Tomek Links improved model metrics for all three data sets, but post-rubric models remained below acceptable performance](tomek-links-improve-metrics-insufficiently.md) — related
- [Models built from faculty rubric ratings also failed to reach acceptable predictive performance, with physics GRE score and quality of work the meaningful features](rubric-rating-data-unmodelable.md) — related
- [A conditional inference random forest model predicts physics PhD admissions decisions on held-out data with 75.8% average accuracy](random-forest-predicts-physics-phd-admissions-75-8-percent.md) — related
- [The authors interpret their modeling results as evidence that rubric-based holistic review could make physics graduate admissions more equitable](rubric-holistic-review-could-increase-equity.md) — related

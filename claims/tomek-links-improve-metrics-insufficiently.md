---
type: claim
title: Removing Tomek Links improved model metrics for all three data sets, but post-rubric models remained below acceptable performance
description: Removing Tomek Links improved model metrics for all three data sets, but post-rubric models remained below acceptable performance
id: tomek-links-improve-metrics-insufficiently
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

# Removing Tomek Links improved model metrics for all three data sets, but post-rubric models remained below acceptable performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r1`–`r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` For data set 0, Tomek Links removal raised testing AUC and accuracy by 0.05, moving the AUC from fair to about 0.8 (good). [→ Nicholas T. Young 2021](#nicholas-t-young-2021)
`q2 i?` For data sets 1a and 1b, Tomek Links raised metrics by roughly 0.05 and 0.04 respectively, but the 1a model remained poor and 1b only reached fair. [→ Nicholas T. Young 2021 (2)](#nicholas-t-young-2021-2)

## Evidence

### Nicholas T. Young 2021

Nicholas T. Young, N. Verboncoeur, Dao Chi Lam, and Marcos D. Caballero. (2021). Rubric-based holistic review represents a change from traditional graduate admissions approaches in physics. [doi:10.48550/arXiv.2112.06886](https://doi.org/10.48550/arXiv.2112.06886)

`q2 · i?` · `associational · r2`

Tomek Links removal on the pre-rubric data set, with MICE imputation and HVDM distance, models run 30 times and pooled with Rubin's Rules. Testing AUC reached 0.809±0.009 and testing accuracy 0.806±0.009.

> "First, we notice that for data set 0, using Tomek Links increased the testing AUC and testing accuracy by 0.05 over the original model. The testing AUC is now about 0.8 which is considered "good" compared to "fair" for the original model [50]."

### Nicholas T. Young 2021 (2)

Nicholas T. Young, N. Verboncoeur, Dao Chi Lam, and Marcos D. Caballero. (2021). Rubric-based holistic review represents a change from traditional graduate admissions approaches in physics. [doi:10.48550/arXiv.2112.06886](https://doi.org/10.48550/arXiv.2112.06886)

`q2 · i?` · `associational · r1`

Tomek Links applied to the post-rubric data sets; 15%-18% of cases dropped for 1a and 12%-17% for 1b. Testing AUC reached 0.670±0.015 for 1a (still poor) and 0.704±0.014 for 1b, which the authors classify as fair.

> "Likewise, using Tomek Links also results in an approximately 0.05 increase in the testing AUC and testing accuracy for data set 1a. However, the AUC is still in the poor range and the testing accuracy is only slightly better than the null accuracy."

## Discussion


## Related Claims
- [After rubric implementation, admissions decisions from application data could not be acceptably modeled, even with hyperparameter tuning](post-rubric-application-data-unmodelable.md) — related
- [A conditional inference forest acceptably models pre-rubric physics graduate admissions decisions, with physics GRE score, quantitative GRE score, and undergraduate GPA the only meaningful features](pre-rubric-admissions-model-quantitative-metrics-meaningful.md) — related
- [Cross-dataset testing and the 5x2 cv combined F-test indicate the admissions process changed after rubric implementation](model-comparison-indicates-process-changed.md) — related

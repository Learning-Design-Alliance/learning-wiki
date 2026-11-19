---
type: claim
title: Cross-dataset testing and the 5x2 cv combined F-test indicate the admissions process changed after rubric implementation
description: Cross-dataset testing and the 5x2 cv combined F-test indicate the admissions process changed after rubric implementation
id: model-comparison-indicates-process-changed
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2021
sources:
  - id: nicholas-t-young-2021
    resource: "https://doi.org/10.48550/arXiv.2112.06886"
    title: "Nicholas T. Young, N. Verboncoeur, Dao Chi Lam, and Marcos D. Caballero. (2021). Rubric-based holistic review represents a change from traditional graduate admissions approaches in physics. [doi:10.48550/arXiv.2112.06886](https://doi.org/10.48550/arXiv.2112.06886)"
    author: Nicholas T. Young, N. Verboncoeur, Dao Chi Lam, and Marcos D. Caballero
    q: 2
    i: "?"
    kind: causal
    rigour: 1
  - id: nicholas-t-young-2021-2
    resource: "https://doi.org/10.48550/arXiv.2112.06886"
    title: "Nicholas T. Young, N. Verboncoeur, Dao Chi Lam, and Marcos D. Caballero. (2021). Rubric-based holistic review represents a change from traditional graduate admissions approaches in physics. [doi:10.48550/arXiv.2112.06886](https://doi.org/10.48550/arXiv.2112.06886)"
    author: Nicholas T. Young, N. Verboncoeur, Dao Chi Lam, and Marcos D. Caballero
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Cross-dataset testing and the 5x2 cv combined F-test indicate the admissions process changed after rubric implementation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Models built on one data set did not fit the other: the data set 0 model fit data set 0 well but not data set 1a. [→ Nicholas T. Young 2021](#nicholas-t-young-2021)
`q2 i?` The before- and after-rubric models were statistically different when tested on the before data set (corrected p = 0.01 for AUC) but not on the after data set. [→ Nicholas T. Young 2021 (2)](#nicholas-t-young-2021-2)

## Evidence

### Nicholas T. Young 2021

Nicholas T. Young, N. Verboncoeur, Dao Chi Lam, and Marcos D. Caballero. (2021). Rubric-based holistic review represents a change from traditional graduate admissions approaches in physics. [doi:10.48550/arXiv.2112.06886](https://doi.org/10.48550/arXiv.2112.06886)

`q2 · i?` · `causal · r1`

True-testing-set comparison: a model trained on data set 0 was applied to data set 1a and vice versa, 30 repetitions each. These metrics "suggest that the data set 0 model ﬁts data set 0 well but does not ﬁt data set 1a well and therefore, that the process might have changed".

> "In Figure 8A, we see that the data set 0 test AUC is larger than the data set 1a AUC, and in Figure 9A, we see that the data set 0 test accuracy is larger than the data set 0 null accuracy while the data set 1a test accuracy is smaller than the data set 1a null accuracy."

### Nicholas T. Young 2021 (2)

Nicholas T. Young, N. Verboncoeur, Dao Chi Lam, and Marcos D. Caballero. (2021). Rubric-based holistic review represents a change from traditional graduate admissions approaches in physics. [doi:10.48550/arXiv.2112.06886](https://doi.org/10.48550/arXiv.2112.06886)

`q2 · i?` · `causal · r1`

Alpaydin's 5x2 cv combined F-test with Holm-Bonferroni correction: for data set 0, F = 18.95 (AUC, corrected p = 0.01) and F = 9.70 (accuracy, corrected p = 0.03); for data set 1a, F = 1.54 (p = 0.33) and F = 4.14 (p = 0.13).

> "We ﬁnd that the models for before and after the implementation of the rubric tested on the before data set (data set 0) are statistically diﬀerent while the models for before and after the implementation of the rubric tested on the after data set (data set 1a) are not."

## Discussion


## Related Claims
- [After rubric implementation, admissions decisions from application data could not be acceptably modeled, even with hyperparameter tuning](post-rubric-application-data-unmodelable.md) — related
- [Models built from faculty rubric ratings also failed to reach acceptable predictive performance, with physics GRE score and quality of work the meaningful features](rubric-rating-data-unmodelable.md) — related
- [Help-seeking models transfer above chance across sites but perform poorly on the Costa Rican data](help-seeking-model-transfer-mixed.md) — related
- [The authors interpret their modeling results as evidence that rubric-based holistic review could make physics graduate admissions more equitable](rubric-holistic-review-could-increase-equity.md) — related
- [Removing Tomek Links improved model metrics for all three data sets, but post-rubric models remained below acceptable performance](tomek-links-improve-metrics-insufficiently.md) — related

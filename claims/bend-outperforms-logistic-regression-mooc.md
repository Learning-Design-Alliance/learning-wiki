---
type: claim
title: The βEND model outperforms logistic regression in predicting certificate-rate patterns in the FUN dataset
description: The βEND model outperforms logistic regression in predicting certificate-rate patterns in the FUN dataset
id: bend-outperforms-logistic-regression-mooc
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: moderate
newest_evidence: 2019
recheck_by: 2022
sources:
  - id: wintermute-2019
    resource: "https://doi.org/10.48550/arXiv.1905.04201"
    title: "Wintermute, E. H., Cisel, M., & Lindner, A. B. (2019). A survival model for course-course interactions in a Massive Open Online Course platform. arXiv. [doi:10.48550/arXiv.1905.04201](https://doi.org/10.48550/arXiv.1905.04201)"
    author: "Wintermute, E. H., Cisel, M., & Lindner, A. B."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: wintermute-2019-2
    resource: "https://doi.org/10.48550/arXiv.1905.04201"
    title: "Wintermute, E. H., Cisel, M., & Lindner, A. B. (2019). A survival model for course-course interactions in a Massive Open Online Course platform. arXiv. [doi:10.48550/arXiv.1905.04201](https://doi.org/10.48550/arXiv.1905.04201)"
    author: "Wintermute, E. H., Cisel, M., & Lindner, A. B."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# The βEND model outperforms logistic regression in predicting certificate-rate patterns in the FUN dataset

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2019 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2022**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` βEND-predicted certificate log-odds for co-registration cohorts correlated with observed values (r2 = 0.72), while logistic regression predictions correlated less well (r2 = 0.35). [→ Wintermute 2019](#wintermute-2019)
`q2 i?` The logistic model systematically overestimated certificate probabilities for low-probability registration events, whereas βEND predictions showed a linear relation over two orders of magnitude. [→ Wintermute 2019 (2)](#wintermute-2019-2)

## Evidence

### Wintermute 2019

Wintermute, E. H., Cisel, M., & Lindner, A. B. (2019). A survival model for course-course interactions in a Massive Open Online Course platform. arXiv. [doi:10.48550/arXiv.1905.04201](https://doi.org/10.48550/arXiv.1905.04201)

`q2 · i?` · `associational · r2`

Cross-validated model comparison on the FUN dataset (Fig. 2B): βEND predictions of co-registration cohort log odds correlated with observed values at "r2 = 0.72", while the logistic model's corresponding predictions correlated at r2 = 0.35 (Fig. 2E).

> "Predicted and observed log odds values were linearly correlated (r2 = 0.72)."

### Wintermute 2019 (2)

Wintermute, E. H., Cisel, M., & Lindner, A. B. (2019). A survival model for course-course interactions in a Massive Open Online Course platform. arXiv. [doi:10.48550/arXiv.1905.04201](https://doi.org/10.48550/arXiv.1905.04201)

`q2 · i?` · `associational · r2`

Hosmer-Lemeshow comparison (Fig. 2A) of both models fit to ~330,000 training registration events and evaluated on the test group: the βEND model tracked observed rates while the logistic model overestimated low-rate events.

> "While the βEND model predictions show a linear relation over two orders of magnitude, the logistic model systematically overestimates certificate rates for low-rate registration events."

## Discussion


## Related Claims
- [Per-course certificate rate drops in inverse proportion to registration burst size](certificate-rate-drops-with-burst-size.md) — related
- [Co-registration changes certificate rates for roughly a third of courses in each direction, with effects governed by course engagement level](co-registration-effects-governed-by-engagement.md) — related
- [Boosting models (XGBoost) achieved the highest predictive accuracy among the compared ML models, while logistic regression showed the lowest](boosting-highest-accuracy-logistic-lowest.md) — related

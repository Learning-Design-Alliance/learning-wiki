---
type: claim
title: Learning outcome can be predicted from overall BtBC via support vector regression
description: Learning outcome can be predicted from overall BtBC via support vector regression
id: btbc-predicts-learning-outcome
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-26
evidence_strength: moderate
newest_evidence: 2022
recheck_by: 2025
sources:
  - id: yafeng-pan-2022
    resource: "https://doi.org/10.1038/s41539-022-00131-0"
    title: "Yafeng Pan, Suzanne Dikker, Yi Zhu, Cuirong Yang, Yi Hu and Pavel Goldstein. (2022). Instructor-learner body coupling reflects instruction and learning. npj Science of Learning. https://doi.org/10.1038/s41539-022-00131-0"
    author: Yafeng Pan, Suzanne Dikker, Yi Zhu, Cuirong Yang, Yi Hu and Pavel Goldstein
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Learning outcome can be predicted from overall BtBC via support vector regression

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` SVR with nested cross-validation decoded learning outcome from overall BtBC, and the prediction held after controlling for instructional approach. [→ Yafeng Pan 2022](#yafeng-pan-2022)

## Evidence

### Yafeng Pan 2022

Yafeng Pan, Suzanne Dikker, Yi Zhu, Cuirong Yang, Yi Hu and Pavel Goldstein. (2022). Instructor-learner body coupling reflects instruction and learning. npj Science of Learning. https://doi.org/10.1038/s41539-022-00131-0

`q2 · i?` · `causal · r2`

Prediction analysis on the combined personalized and nonpersonalized groups using support vector regression with outer leave-one-out and inner 10-fold CV. Controlling for instructional approach, the correlation remained significant (r = 0.41, p = 0.004, R² = 0.16).

> "Support vector regression (SVR) analysis with nested cross validation (Fig. 4a) yielded a correlation coef ﬁcient of 0.44 ( p = 0.002, R2 = 0.16) between the actual and predicted learning outcome"

## Discussion


## Related Claims
- [Directional leader–follower BtBC patterns decode instructional approach better than individual motion, with peak performance at non-zero time lags](btbc-decodes-instructional-approach.md) — related
- [Learner-leading BtBC is larger under scaffolding; instructor-leading BtBC shows only a trending effect, and instructor-leading BtBC fails to predict learning under explanation](directional-btbc-exploratory-findings.md) — related
- [Instructional personalization did not significantly affect learning outcome or BtBC](personalization-null-body-coupling.md) — related

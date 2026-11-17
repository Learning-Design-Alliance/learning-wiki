---
type: claim
title: "Students' MOOC video clickstream sequences predict the length of their interaction with video lectures (engagement prediction)"
description: "Students' MOOC video clickstream sequences predict the length of their interaction with video lectures (engagement prediction)"
id: clickstream-predicts-video-engagement-mooc
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-17
evidence_strength: moderate
newest_evidence: 2014
recheck_by: 2017
sources:
  - id: sinha-2014
    resource: "https://doi.org/10.3115/v1/w14-4102"
    title: "Sinha, T., Jermann, P., Li, N., & Dillenbourg, P. (2014). Your click decides your fate: Inferring Information Processing and Attrition Behavior from MOOC Video Clickstream Interactions. [doi:10.3115/v1/w14-4102](https://doi.org/10.3115/v1/w14-4102)"
    author: "Sinha, T., Jermann, P., Li, N., & Dillenbourg, P."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: sinha-2014-2
    resource: "https://doi.org/10.3115/v1/w14-4102"
    title: "Sinha, T., Jermann, P., Li, N., & Dillenbourg, P. (2014). Your click decides your fate: Inferring Information Processing and Attrition Behavior from MOOC Video Clickstream Interactions. [doi:10.3115/v1/w14-4102](https://doi.org/10.3115/v1/w14-4102)"
    author: "Sinha, T., Jermann, P., Li, N., & Dillenbourg, P."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Students' MOOC video clickstream sequences predict the length of their interaction with video lectures (engagement prediction)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2014 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2017**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Raw clickstream n-gram, sequence-length and regular-expression features predict high versus low engagement with a video lecture with accuracy 0.81 (kappa 0.63, false negative rate 0.24). [→ Sinha 2014](#sinha-2014)
`q2 i?` Summarized behavioral action vectors achieve nearly similar engagement prediction accuracy (0.75, kappa 0.49) with a lower false negative rate (0.15) than raw clicks. [→ Sinha 2014 (2)](#sinha-2014-2)

## Evidence

### Sinha 2014

Sinha, T., Jermann, P., Li, N., & Dillenbourg, P. (2014). Your click decides your fate: Inferring Information Processing and Attrition Behavior from MOOC Video Clickstream Interactions. [doi:10.3115/v1/w14-4102](https://doi.org/10.3115/v1/w14-4102)

`q2 · i?` · `associational · r2`

Engagement prediction experiment on video lecture 4-6 of the Functional Programming in Scala MOOC: L2 regularized logistic regression with 10-fold cross validation classified equal-frequency high/low engagement from raw click features; high engagers were characterized by "re-watch=high, slow watching=low, checkback reference=low, clear concept=high" at the accuracy, kappa and false negative rate shown.

> "A)Raw Clicks 0.810.63 0.24 High (skipping=low, playrate transition=low, re-watch=high, slow watching=low, checkback reference=low, clear concept=high)"

### Sinha 2014 (2)

Sinha, T., Jermann, P., Li, N., & Dillenbourg, P. (2014). Your click decides your fate: Inferring Information Processing and Attrition Behavior from MOOC Video Clickstream Interactions. [doi:10.3115/v1/w14-4102](https://doi.org/10.3115/v1/w14-4102)

`q2 · i?` · `associational · r2`

Same experiment with level-2 summarized behavioral action vectors as features: accuracy 0.75, kappa 0.49 and false negative rate 0.15, with low engagers characterized by "skipping=high, playrate transition=high, re- watch=low"; the results text reports this false negative rate as lower than for raw clicks.

> "B)Summarized Behavioral Action Vectors 0.75 0.49 0.15 Low (skipping=high, playrate transition=high, re- watch=low, slow watching=high, checkback reference=high, clear concept=low)"

## Discussion


## Related Claims
- [Summarized behavioral action vectors from MOOC video clickstreams yield lower false negative rates than raw click features for engagement and in-video dropout prediction](behavioral-vectors-lower-fnr-than-raw-clicks.md) — related
- [Clickstream features predict students' next click state while watching MOOC video lectures](clickstream-predicts-next-click-state-mooc.md) — related
- [Students' video watching profile summarized from clickstream predicts in-video dropout](behavioral-vectors-predict-in-video-dropout.md) — related

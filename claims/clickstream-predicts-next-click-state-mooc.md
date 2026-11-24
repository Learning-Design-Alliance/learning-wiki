---
type: claim
title: "Clickstream features predict students' next click state while watching MOOC video lectures"
description: "Clickstream features predict students' next click state while watching MOOC video lectures"
id: clickstream-predicts-next-click-state-mooc
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
    rigour: 1
  - id: sinha-2014-2
    resource: "https://doi.org/10.3115/v1/w14-4102"
    title: "Sinha, T., Jermann, P., Li, N., & Dillenbourg, P. (2014). Your click decides your fate: Inferring Information Processing and Attrition Behavior from MOOC Video Clickstream Interactions. [doi:10.3115/v1/w14-4102](https://doi.org/10.3115/v1/w14-4102)"
    author: "Sinha, T., Jermann, P., Li, N., & Dillenbourg, P."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Clickstream features predict students' next click state while watching MOOC video lectures

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r1`–`r2` · `q2`
> **Currency** · newest study 2014 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2017**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Raw clickstream features predict students' next click state with accuracy 0.68 (kappa 0.57), with SeekFw among the most representative weighted features. [→ Sinha 2014](#sinha-2014)
`q2 i?` Summarized behavioral action vectors predict the next click state with accuracy 0.66 (kappa 0.54), with Ratechangefast and Ratechangeslow among representative features. [→ Sinha 2014 (2)](#sinha-2014-2)

## Evidence

### Sinha 2014

Sinha, T., Jermann, P., Li, N., & Dillenbourg, P. (2014). Your click decides your fate: Inferring Information Processing and Attrition Behavior from MOOC Video Clickstream Interactions. [doi:10.3115/v1/w14-4102](https://doi.org/10.3115/v1/w14-4102)

`q2 · i?` · `associational · r1`

Next-click prediction experiment on the same video lecture 4-6: L2 regularized logistic regression with 5-fold cross validation predicted students' next click state from features extracted up to the previous instant; SeekFw was a representative weighted feature for raw clicks at "playratetransition=low, skipping=low, fastwatching=high, clearconcept=low".

> "2. Next Click Prediction A)Raw Clicks 0.680.57 - SeekFw (playratetransition=low, skipping=low, fastwatching=high, clearconcept=low)"

### Sinha 2014 (2)

Sinha, T., Jermann, P., Li, N., & Dillenbourg, P. (2014). Your click decides your fate: Inferring Information Processing and Attrition Behavior from MOOC Video Clickstream Interactions. [doi:10.3115/v1/w14-4102](https://doi.org/10.3115/v1/w14-4102)

`q2 · i?` · `associational · r2`

With summarized behavioral action vectors as features, next-click prediction reached accuracy 0.66 and kappa 0.54, with Ratechangefast characterized by "playratetransition=high, re- watch=low, checkbackreference=low"; Ratechangeslow was characterized by high playrate transition and clear concept weights.

> "B)Summarized Behavioral Action Vectors 0.66 0.54 - Ratechangefast (playratetransition=high, re- watch=low, checkbackreference=low)"

## Discussion


## Related Claims
- [Students' MOOC video clickstream sequences predict the length of their interaction with video lectures (engagement prediction)](clickstream-predicts-video-engagement-mooc.md) — related
- [Students' video watching profile summarized from clickstream predicts in-video dropout](behavioral-vectors-predict-in-video-dropout.md) — related
- [Summarized behavioral action vectors from MOOC video clickstreams yield lower false negative rates than raw click features for engagement and in-video dropout prediction](behavioral-vectors-lower-fnr-than-raw-clicks.md) — related
- [Engagement, video play proportion and IPI trajectories predict complete course dropout in a MOOC](trajectories-predict-complete-course-dropout.md) — related
- [Average IPI differs significantly across student partitions: high versus low engagers, in-video dropouts versus non-dropouts, course dropouts versus non-dropouts, and Active versus Viewers](ipi-varies-across-student-partitions.md) — related
- [MOOC video-watching behaviors fall into four patterns that reveal different aspects of knowledge dependencies](mooc-video-watching-patterns-dependencies.md) — related
- [Students' actual video watching behaviors in MOOCs do not follow the preset course order, indicating a need for adaptive sequence recommendations](mooc-video-watching-not-following-preset-order.md) — related

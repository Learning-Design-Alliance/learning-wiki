---
type: claim
title: "Students' video watching profile summarized from clickstream predicts in-video dropout"
description: "Students' video watching profile summarized from clickstream predicts in-video dropout"
id: behavioral-vectors-predict-in-video-dropout
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

# Students' video watching profile summarized from clickstream predicts in-video dropout

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2014 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2017**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Raw clickstream features predict in-video dropout with accuracy 0.90 (kappa 0.69, false negative rate 0.19), with non-dropouts characterized by high clear concept and rewatching. [→ Sinha 2014](#sinha-2014)
`q2 i?` Summarized behavioral action vectors predict in-video dropout with accuracy 0.90 (kappa 0.70) and a lower false negative rate (0.15), with dropouts characterized by high skipping and checkback reference. [→ Sinha 2014 (2)](#sinha-2014-2)

## Evidence

### Sinha 2014

Sinha, T., Jermann, P., Li, N., & Dillenbourg, P. (2014). Your click decides your fate: Inferring Information Processing and Attrition Behavior from MOOC Video Clickstream Interactions. [doi:10.3115/v1/w14-4102](https://doi.org/10.3115/v1/w14-4102)

`q2 · i?` · `associational · r2`

In-video dropout prediction on video lecture 4-6 using cost-sensitive L2 regularized logistic regression with 10-fold cross validation: raw clicks achieved the accuracy, kappa and false negative rate shown, with non-dropouts characterized by "skipping=low, clearconcept=high,slow watching=high, Checkbackreference=low, rewatch=high".

> "A)Raw Clicks 0.900.69 0.19 Non dropouts (skipping=low, clearconcept=high,slow watching=high, Checkbackreference=low, rewatch=high, engagementfromStart=low, engagementlastClick=high)"

### Sinha 2014 (2)

Sinha, T., Jermann, P., Li, N., & Dillenbourg, P. (2014). Your click decides your fate: Inferring Information Processing and Attrition Behavior from MOOC Video Clickstream Interactions. [doi:10.3115/v1/w14-4102](https://doi.org/10.3115/v1/w14-4102)

`q2 · i?` · `associational · r2`

With summarized behavioral action vectors, in-video dropout prediction reached accuracy 0.90, kappa 0.70 and false negative rate 0.15; dropouts were characterized by "skipping=high, clearconcept=low, slow watching=low" and high checkback reference.

> "0.90 0.70 0.15 Dropouts (skipping=high, clearconcept=low, slow watching=low, engagementfromStart=high, rewatch=low, engagementlastClick=low, checkbackreference=high)"

## Discussion


## Related Claims
- [Summarized behavioral action vectors from MOOC video clickstreams yield lower false negative rates than raw click features for engagement and in-video dropout prediction](behavioral-vectors-lower-fnr-than-raw-clicks.md) — related
- [Average IPI differs significantly across student partitions: high versus low engagers, in-video dropouts versus non-dropouts, course dropouts versus non-dropouts, and Active versus Viewers](ipi-varies-across-student-partitions.md) — related
- [In-video dropouts and low engagers show significantly lower Information Processing Index values than non-dropouts and high engagers in the same video lecture](ipi-lower-for-dropouts-and-low-engagers.md) — related
- [Clickstream features predict students' next click state while watching MOOC video lectures](clickstream-predicts-next-click-state-mooc.md) — related
- [Students' MOOC video clickstream sequences predict the length of their interaction with video lectures (engagement prediction)](clickstream-predicts-video-engagement-mooc.md) — related
- [Greater IPI, increased rewatching and greater video play proportion each associate with lower MOOC dropout hazard](ipi-survival-dropout-hazard.md) — related

---
type: claim
title: Summarized behavioral action vectors from MOOC video clickstreams yield lower false negative rates than raw click features for engagement and in-video dropout prediction
description: Summarized behavioral action vectors from MOOC video clickstreams yield lower false negative rates than raw click features for engagement and in-video dropout prediction
id: behavioral-vectors-lower-fnr-than-raw-clicks
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
    title: "Sinha, T. (2014). \"Your click decides your fate\": Leveraging clickstream patterns from MOOC videos to infer students' information processing & attrition behavior. B.Tech project report, School of Computing Science and Engineering, VIT University, Chennai. [doi:10.3115/v1/w14-4102](https://doi.org/10.3115/v1/w14-4102)"
    author: Sinha, T.
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Summarized behavioral action vectors from MOOC video clickstreams yield lower false negative rates than raw click features for engagement and in-video dropout prediction

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2014 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2017**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` False negative rate is lower when using summarized behavioral action vectors (Case 1.B, Case 3.B) than raw clicks (Case 1.A, Case 3.A) for engagement and in-video dropout prediction. [→ Sinha 2014](#sinha-2014)

## Evidence

### Sinha 2014

Sinha, T. (2014). "Your click decides your fate": Leveraging clickstream patterns from MOOC videos to infer students' information processing & attrition behavior. B.Tech project report, School of Computing Science and Engineering, VIT University, Chennai. [doi:10.3115/v1/w14-4102](https://doi.org/10.3115/v1/w14-4102)

`q2 · i?` · `associational · r2`

Machine learning experiments (L2-regularized logistic regression, 10-fold cross validation annotated by student-id) on video lecture 4-6 of the Scala MOOC compare raw click features against summarized behavioral action vectors. The report states the "effectiveness of the clickstream summarization approach" in lowering FNR for engagement and in-video dropout prediction.

> "False negative rate is lower for Case 1.B and Case 3.B, as compared to Case 1.A and Case 3.A, which shows the effectiveness of the clickstream summarization approach in pre-deciphering the fate of students to some extent."

## Discussion


## Related Claims
- [Students' video watching profile summarized from clickstream predicts in-video dropout](behavioral-vectors-predict-in-video-dropout.md) — related
- [Students' MOOC video clickstream sequences predict the length of their interaction with video lectures (engagement prediction)](clickstream-predicts-video-engagement-mooc.md) — related
- [Clickstream features predict students' next click state while watching MOOC video lectures](clickstream-predicts-next-click-state-mooc.md) — related

---
type: claim
title: Including grader bias and reliability as features improves prediction of future course participation from AUC 0.93 to 0.98, capturing an engagement dimension missed by assignment grade
description: Including grader bias and reliability as features improves prediction of future course participation from AUC 0.93 to 0.98, capturing an engagement dimension missed by assignment grade
id: grader-bias-reliability-predict-future-participation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-16
evidence_strength: moderate
sources:
  - id: chris-piech-2013
    resource: "https://arxiv.org/abs/1307.2579"
    title: "Chris Piech, Jonathan Huang, Zhenghao Chen, Chuong Do, Andrew Ng, Daphne Koller. (2013). Tuned Models of Peer Assessment in MOOCs. arXiv. https://arxiv.org/abs/1307.2579"
    author: Chris Piech, Jonathan Huang, Zhenghao Chen, Chuong Do, Andrew Ng, Daphne Koller
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Including grader bias and reliability as features improves prediction of future course participation from AUC 0.93 to 0.98, capturing an engagement dimension missed by assignment grade

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`

## Subclaims
`q2 i?` In a classification task predicting whether a student participates in the next assignment, adding grader bias and reliability to a linear classifier with the student's grade improved AUC from 0.93 to 0.98 (a 5pp improvement). [→ Chris Piech 2013](#chris-piech-2013)

## Evidence

### Chris Piech 2013

Chris Piech, Jonathan Huang, Zhenghao Chen, Chuong Do, Andrew Ng, Daphne Koller. (2013). Tuned Models of Peer Assessment in MOOCs. arXiv. https://arxiv.org/abs/1307.2579

`q2 · i?` · `associational · r2`

Classification experiment on HCI dataset logs predicting next-assignment participation (dropout), using a linear SVM with grade, bias, and reliability features (Figure 4b, AUC = 0.97605 for all features). The article reports grader properties "capture a dimension of their engagement which is missed by their assignment grade".

> "Our results (Figure 4(b)) show that including grader bias and reliability improved our predictive ability by 5pp from an area under the curve (AUC) score of 0.93 to an AUC of 0.98."

## Discussion


## Related Claims
-

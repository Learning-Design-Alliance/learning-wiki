---
type: claim
title: Current-submission evidence and prior traces predict near-term persistent failure with moderate discrimination under student-disjoint evaluation
description: Current-submission evidence and prior traces predict near-term persistent failure with moderate discrimination under student-disjoint evaluation
id: persistent-failure-moderate-discrimination-student-disjoint
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: shihao-wang-2026
    resource: "https://doi.org/10.48550/arxiv.2609.29874"
    title: "Shihao Wang. (2026). A Risk-Adaptive and Evidence-Constrained Framework for Generative AI Feedback in Programming Education. https://arxiv.org/abs/2609.29874 [doi:10.48550/arxiv.2609.29874](https://doi.org/10.48550/arxiv.2609.29874)"
    author: Shihao Wang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Current-submission evidence and prior traces predict near-term persistent failure with moderate discrimination under student-disjoint evaluation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` A validation-selected logistic regression model achieved test PR-AUC of 0.550 and ROC-AUC of 0.681 for predicting persistent failure on held-out students. [→ Shihao Wang 2026](#shihao-wang-2026)

## Evidence

### Shihao Wang 2026

Shihao Wang. (2026). A Risk-Adaptive and Evidence-Constrained Framework for Generative AI Feedback in Programming Education. https://arxiv.org/abs/2609.29874 [doi:10.48550/arxiv.2609.29874](https://doi.org/10.48550/arxiv.2609.29874)

`q2 · i?` · `design · r2`

Retrospective computational study of 2993 failed-submission states from 215 students with student-disjoint 60/20/20 partitions. The validation-selected logistic regression achieved "a PR-AUC of 0.550" and ROC-AUC 0.681 with a Brier score of 0.222 on the held-out test partition.

> "On held-out students, it achieved a PR-AUC of 0.550 (student-cluster 95% CI [0.361, 0.676]), ROC-AUC of 0.681 [0.585, 0.741], and Brier score of 0.222."

## Discussion


## Related Claims
- [The selected MLP outperformed gradient boosting for persistent-failure prediction in paired student bootstrap comparison](mlp-outperformed-gradient-boosting-persistent-failure.md) — related
- Logistic regression with the best feature vector outperforms all other approaches on 4 of 9 datasets while DKT leads on the remaining 5, and Markov process methods lag behind — related
- [Secondary outcomes differed in predictability: near-term related-task performance was hardest while 7–28-day performance showed a longitudinal signal](secondary-outcomes-varied-predictability.md) — related

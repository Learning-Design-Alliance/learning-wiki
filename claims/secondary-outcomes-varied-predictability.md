---
type: claim
title: "Secondary outcomes differed in predictability: near-term related-task performance was hardest while 7–28-day performance showed a longitudinal signal"
description: "Secondary outcomes differed in predictability: near-term related-task performance was hardest while 7–28-day performance showed a longitudinal signal"
id: secondary-outcomes-varied-predictability
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: shihao-wang-2026
    resource: "https://arxiv.org/abs/2609.29874"
    title: "Shihao Wang. (2026). A Risk-Adaptive and Evidence-Constrained Framework for Generative AI Feedback in Programming Education. https://arxiv.org/abs/2609.29874"
    author: Shihao Wang
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: shihao-wang-2026-2
    resource: "https://arxiv.org/abs/2609.29874"
    title: "Shihao Wang. (2026). A Risk-Adaptive and Evidence-Constrained Framework for Generative AI Feedback in Programming Education. https://arxiv.org/abs/2609.29874"
    author: Shihao Wang
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Secondary outcomes differed in predictability: near-term related-task performance was hardest while 7–28-day performance showed a longitudinal signal

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r1`–`r2` · `q2`

## Subclaims
`q2 i?` Near-term related-task performance was the most challenging prediction target, with test ROC-AUC of 0.303 for the dedicated fusion GRU, 0.433 for logistic regression, and 0.383 for gradient boosting. [→ Shihao Wang 2026](#shihao-wang-2026)
`q2 i?` The 7–28-day related-task outcome showed promising longitudinal discrimination, with dedicated logistic regression and gradient boosting achieving ROC-AUC values of 0.691 and 0.699 across 67 test cases from 25 students. [→ Shihao Wang 2026 (2)](#shihao-wang-2026-2)

## Evidence

### Shihao Wang 2026

Shihao Wang. (2026). A Risk-Adaptive and Evidence-Constrained Framework for Generative AI Feedback in Programming Education. https://arxiv.org/abs/2609.29874

`q2 · i?` · `associational · r2`

Dedicated models on 209 test states for near-term related-task performance. "Near-term related-task performance was the most challenging prediction target", with test ROC-AUC of 0.303, 0.433, and 0.383 across the three model types.

> "Near-term related-task performance was the most challenging prediction target. The dedicated fusion GRU achieved validation PR-AUC 0.608 and test ROC-AUC 0.303; logistic regression reached ROC-AUC 0.433, and gradient boosting reached 0.383."

### Shihao Wang 2026 (2)

Shihao Wang. (2026). A Risk-Adaptive and Evidence-Constrained Framework for Generative AI Feedback in Programming Education. https://arxiv.org/abs/2609.29874

`q2 · i?` · `associational · r1`

Longitudinal related-task outcome analysis on 67 test cases from 25 students. "Dedicated logistic regression and gradient boosting achieved ROC-AUC values of 0.691 and 0.699" with wide student-cluster intervals; the authors call for further longitudinal validation with larger samples.

> "Dedicated logistic regression and gradient boosting achieved ROC-AUC values of 0.691 and 0.699, respectively , with student-cluster intervals extending from approximately 0.49 to 0.85."

## Discussion


## Related Claims
- [The selected MLP outperformed gradient boosting for persistent-failure prediction in paired student bootstrap comparison](mlp-outperformed-gradient-boosting-persistent-failure.md) — related
- [Current-submission evidence and prior traces predict near-term persistent failure with moderate discrimination under student-disjoint evaluation](persistent-failure-moderate-discrimination-student-disjoint.md) — related
- [On the CASED challenge test set, all participating engagement-prediction methods converge near random-chance performance, with the best F1 Macro at 0.52](cased-challenge-methods-near-random-chance.md) — related

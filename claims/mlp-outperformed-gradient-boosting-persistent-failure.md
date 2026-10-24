---
type: claim
title: The selected MLP outperformed gradient boosting for persistent-failure prediction in paired student bootstrap comparison
description: The selected MLP outperformed gradient boosting for persistent-failure prediction in paired student bootstrap comparison
id: mlp-outperformed-gradient-boosting-persistent-failure
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
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

# The selected MLP outperformed gradient boosting for persistent-failure prediction in paired student bootstrap comparison

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In a paired student bootstrap, the MLP showed a PR-AUC difference of 0.082 over gradient boosting (95% interval [0.009, 0.132]). [→ Shihao Wang 2026](#shihao-wang-2026)

## Evidence

### Shihao Wang 2026

Shihao Wang. (2026). A Risk-Adaptive and Evidence-Constrained Framework for Generative AI Feedback in Programming Education. https://arxiv.org/abs/2609.29874 [doi:10.48550/arxiv.2609.29874](https://doi.org/10.48550/arxiv.2609.29874)

`q2 · i?` · `design · r2`

Paired bootstrap model comparison on the student-disjoint test set for persistent failure. "The selected MLP outperformed gradient boosting" with a PR-AUC difference of 0.082 and interval [0.009, 0.132].

> "The selected MLP outperformed gradient boosting in the paired student bootstrap, with a PR-AUC difference of 0.082 and a 95% interval of [0.009, 0.132]."

## Discussion


## Related Claims
- [Secondary outcomes differed in predictability: near-term related-task performance was hardest while 7–28-day performance showed a longitudinal signal](secondary-outcomes-varied-predictability.md) — related
- Simple classifiers (Logistic Regression, Naive Bayes) outperformed tree-based models on this small dataset — related
- [Current-submission evidence and prior traces predict near-term persistent failure with moderate discrimination under student-disjoint evaluation](persistent-failure-moderate-discrimination-student-disjoint.md) — related

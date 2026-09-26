---
type: claim
title: The propdec adaptive student feature is highly colinear with a student intercept, capturing student individual differences without student parameters
description: The propdec adaptive student feature is highly colinear with a student intercept, capturing student individual differences without student parameters
id: propdec-colinear-with-student-intercept
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-25
evidence_strength: moderate
sources:
  - id: philip-i-pavlik-2021
    resource: "https://doi.org/10.1109/TLT.2021.3128569"
    title: "Philip I. Pavlik, Jr., Luke G. Eglington, and Leigh M. Harrell-Williams. (2021). Logistic Knowledge Tracing: A Constrained Framework for Learner Modeling. IEEE Transactions on Learning Technologies. https://doi.org/10.1109/TLT.2021.3128569"
    author: Philip I. Pavlik, Jr., Luke G. Eglington, and Leigh M. Harrell-Williams
    q: 2
    i: "?"
---

# The propdec adaptive student feature is highly colinear with a student intercept, capturing student individual differences without student parameters

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q2` quasi-experiment

## Subclaims
`q2 i?` Combining the intercept and propdec features provided little additional benefit, suggesting propdec is highly colinear with the intercept as a representation of student differences. [→ Philip I. Pavlik 2021](#philip-i-pavlik-2021)

## Evidence

### Philip I. Pavlik 2021

Philip I. Pavlik, Jr., Luke G. Eglington, and Leigh M. Harrell-Williams. (2021). Logistic Knowledge Tracing: A Constrained Framework for Learner Modeling. IEEE Transactions on Learning Technologies. https://doi.org/10.1109/TLT.2021.3128569

`q2 · i?`

Initial comparison of nine student-variance-only models (Table IV, McFadden's R2) evaluating adaptive methods against fixed and random intercepts across the datasets. The article reports the fits of intercept-based and adaptive measures were similar and "the propdec feature is highly colinear with the intercept".

> "The sixth model shows how little additional beneﬁt is provided by combining the intercept and the propdec features, suggesting that the propdec feature is highly colinear with the intercept."

## Discussion


## Related Claims
- [Ablation study: removing any component lowers evaluation AUC, and removing all additional features yields the lowest public and private AUCs](ablation-all-features-maximize-auc.md) — related
- [Ablation of feature-vector models: time-window features add no predictive power to logistic regression but boost a feedforward network, and total count features substantially boost performance on all datasets](time-window-features-null-for-lr-boost-nonlinear.md) — related

---
type: claim
title: Models able to weight performance by recency fit better on the Assistments and KDD datasets, without explicit memory-decay terms being necessary
description: Models able to weight performance by recency fit better on the Assistments and KDD datasets, without explicit memory-decay terms being necessary
id: recency-weighting-models-better-assistments-kdd
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
  - id: philip-i-pavlik-2021-2
    resource: "https://doi.org/10.1109/TLT.2021.3128569"
    title: "Philip I. Pavlik, Jr., Luke G. Eglington, and Leigh M. Harrell-Williams. (2021). Logistic Knowledge Tracing: A Constrained Framework for Learner Modeling. IEEE Transactions on Learning Technologies. https://doi.org/10.1109/TLT.2021.3128569"
    author: Philip I. Pavlik, Jr., Luke G. Eglington, and Leigh M. Harrell-Williams
    q: 2
    i: "?"
---

# Models able to weight performance by recency fit better on the Assistments and KDD datasets, without explicit memory-decay terms being necessary

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · `q2` quasi-experiment

## Subclaims
`q2 i?` In the Assistments dataset, R-PFA (model 9) and memory-feature models (models 10-12) were not significantly different from each other but were generally better than other models, suggesting recency weighting was important. [→ Philip I. Pavlik 2021](#philip-i-pavlik-2021)
`q2 i?` In the KDD cup dataset, models 1-3 tended to fit worse than more complex models, and recency-weighting features helped while explicit memory decay was not as relevant. [→ Philip I. Pavlik 2021 (2)](#philip-i-pavlik-2021-2)

## Evidence

### Philip I. Pavlik 2021

Philip I. Pavlik, Jr., Luke G. Eglington, and Leigh M. Harrell-Williams. (2021). Logistic Knowledge Tracing: A Constrained Framework for Learner Modeling. IEEE Transactions on Learning Technologies. https://doi.org/10.1109/TLT.2021.3128569

`q2 · i?`

Analysis of the Assistments dataset (580,785 observations from 912 middle school students learning mathematics, 23% retained after filtering to first attempts). The article reports the better models were "generally better than the other models", a pattern suggesting recency weighting was important.

> "With the Assistments dataset, R-PFA (model 9) and models with memory features (models 10–12) were not signiﬁcantly different in ﬁt from each other. However, they were generally better than the other models."

### Philip I. Pavlik 2021 (2)

Philip I. Pavlik, Jr., Luke G. Eglington, and Leigh M. Harrell-Williams. (2021). Logistic Knowledge Tracing: A Constrained Framework for Learner Modeling. IEEE Transactions on Learning Technologies. https://doi.org/10.1109/TLT.2021.3128569

`q2 · i?`

Analysis of random subsets of the KDD cup 2005/2006 dataset (809,694 observations; 120 of 574 students per run), students learning algebra with the Cognitive Tutor system. The article reports "models 1–3 tended to provide worse ﬁts than more complex models" and recency-weighting features were superior.

> "In the KDD cup dataset, models 1–3 tended to provide worse ﬁts than more complex models. As was found with the Assistments dataset, superior models included features that could weight performance according to recency, but explicitly accounting for memory decay was not as relevant."

## Discussion


## Related Claims
-

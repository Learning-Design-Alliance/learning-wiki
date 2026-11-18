---
type: claim
title: "In simulated data, a question's DI drops when the total is defined only by a subset of questions, showing DI depends on which questions define the total"
description: "In simulated data, a question's DI drops when the total is defined only by a subset of questions, showing DI depends on which questions define the total"
id: simulation-di-depends-on-question-subset
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: weak
newest_evidence: 2019
recheck_by: 2022
sources:
  - id: joshi-2019
    resource: "https://doi.org/10.48550/arXiv.1906.07941"
    title: "Joshi, P.K., Jain, Y., Khunyakari, R. and Basu, S. (2019). A novel alternative to analyzing multiple choice questions via discrimination index. [doi:10.48550/arXiv.1906.07941](https://doi.org/10.48550/arXiv.1906.07941)"
    author: Joshi, P.K., Jain, Y., Khunyakari, R. and Basu, S.
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# In simulated data, a question's DI drops when the total is defined only by a subset of questions, showing DI depends on which questions define the total

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2019 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2022**: tool and model accuracy changes quickly

## Subclaims
`q1 i?` In a constructed dataset, separating a subset of questions and recomputing DI over its combinations lowered the DI of one question while the deliberately grouped questions kept DI of 1.0. [→ Joshi 2019](#joshi-2019)

## Evidence

### Joshi 2019

Joshi, P.K., Jain, Y., Khunyakari, R. and Basu, S. (2019). A novel alternative to analyzing multiple choice questions via discrimination index. [doi:10.48550/arXiv.1906.07941](https://doi.org/10.48550/arXiv.1906.07941)

`q1 · i?` · `design · r2`

In a constructed dataset of 100 students and 10 questions where the first 50 students answered the first 4 questions correctly, separating the 5-question subset showed the DI of question 10 "dropped to a low value whereas the DI for the ﬁrst 4 questions remained 1.0."

> "the DI value for question number 10 dropped to a low value whereas the DI for the ﬁrst 4 questions remained 1.0."

## Discussion


## Related Claims
- [Discrimination index values for a question are much higher when the question's own marks are included in the total used to rank students](di-depends-on-total-definition.md) — related
- [Reporting DI as an average with standard deviation over question combinations represents questions better than a single DI from the total of all marks](di-reported-as-range-average-sigma.md) — related

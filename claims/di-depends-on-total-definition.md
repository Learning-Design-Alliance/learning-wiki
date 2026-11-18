---
type: claim
title: "Discrimination index values for a question are much higher when the question's own marks are included in the total used to rank students"
description: "Discrimination index values for a question are much higher when the question's own marks are included in the total used to rank students"
id: di-depends-on-total-definition
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: moderate
newest_evidence: 2019
recheck_by: 2022
sources:
  - id: joshi-2019
    resource: "https://doi.org/10.48550/arXiv.1906.07941"
    title: "Joshi, P.K., Jain, Y., Khunyakari, R. and Basu, S. (2019). A novel alternative to analyzing multiple choice questions via discrimination index. [doi:10.48550/arXiv.1906.07941](https://doi.org/10.48550/arXiv.1906.07941)"
    author: Joshi, P.K., Jain, Y., Khunyakari, R. and Basu, S.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Discrimination index values for a question are much higher when the question's own marks are included in the total used to rank students

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2019 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2022**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In the INJSO 2017 data, DI values computed with the analyzed question's marks included in the ranking total, with negative marking, fall outside the average-with-standard-deviation range obtained from combinations excluding self marks. [→ Joshi 2019](#joshi-2019)

## Evidence

### Joshi 2019

Joshi, P.K., Jain, Y., Khunyakari, R. and Basu, S. (2019). A novel alternative to analyzing multiple choice questions via discrimination index. [doi:10.48550/arXiv.1906.07941](https://doi.org/10.48550/arXiv.1906.07941)

`q2 · i?` · `design · r2`

Comparative analysis of the INJSO 2017 Olympiad selection test computed DI with the analyzed question's marks included in the ranking total versus excluded; with self marks included, values "are much higher and outside the range" of the average with standard deviation distribution from random combinations of the remaining questions.

> "However, the DI values obtained when self marks are included in calculating the "total", and inclusion of negative marking, are much higher and outside the range."

## Discussion


## Related Claims
- [Reporting DI as an average with standard deviation over question combinations represents questions better than a single DI from the total of all marks](di-reported-as-range-average-sigma.md) — related
- [DI values vary significantly depending on how students with equal total marks are assigned to the top and bottom blocks](di-tie-handling-non-uniqueness.md) — related
- [In simulated data, a question's DI drops when the total is defined only by a subset of questions, showing DI depends on which questions define the total](simulation-di-depends-on-question-subset.md) — related

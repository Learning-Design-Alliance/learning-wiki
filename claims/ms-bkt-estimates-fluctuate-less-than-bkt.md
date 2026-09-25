---
type: claim
title: MS-BKT mastery estimates fluctuate less than classic BKT and avoid over-high estimates after long incorrect runs, in fictitious-student comparisons
description: MS-BKT mastery estimates fluctuate less than classic BKT and avoid over-high estimates after long incorrect runs, in fictitious-student comparisons
id: ms-bkt-estimates-fluctuate-less-than-bkt
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-25
evidence_strength: weak
sources:
  - id: agarwal-2020
    resource: "https://educationaldatamining.org/edm2020/"
    title: "Agarwal, D., Baker, R.S., & Muraleedharan, A. (2020). Dynamic knowledge tracing through data driven recency weights. Proceedings of The 13th International Conference on Educational Data Mining (EDM 2020). https://educationaldatamining.org/edm2020/"
    author: "Agarwal, D., Baker, R.S., & Muraleedharan, A."
    q: 1
    i: "?"
---

# MS-BKT mastery estimates fluctuate less than classic BKT and avoid over-high estimates after long incorrect runs, in fictitious-student comparisons

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q1` argument or single case

## Subclaims
`q1 i?` For fictitious students, BKT's Ln values showed significantly higher fluctuations than MS-BKT, and BKT produced extremely high estimates after incorrect histories (e.g. 0.75 for Student4 versus 0.30 for MS-BKT; 0.83 for Student7 versus 0.45). [→ Agarwal 2020](#agarwal-2020)

## Evidence

### Agarwal 2020

Agarwal, D., Baker, R.S., & Muraleedharan, A. (2020). Dynamic knowledge tracing through data driven recency weights. Proceedings of The 13th International Conference on Educational Data Mining (EDM 2020). https://educationaldatamining.org/edm2020/

`q1 · i?`

Section 4 compares the two models on fictitious student data (Table 2, Figure 3) using the same L0, G, S values. The article attributes BKT's high estimates to its fixed learning rate irrespective of responses, while MS-BKT derives learning or forgetting from data.

> "For Student4, Ln shoots up drastically to 0.75, even though there is a long history of incorrect responses on previous attempts and learning rate is only 0.1. By comparison, the Ln value is around 0.30 for the MS-BKT model."

## Discussion


## Related Claims
-

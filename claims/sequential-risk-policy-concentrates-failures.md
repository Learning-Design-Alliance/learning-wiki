---
type: claim
title: A fixed-threshold sequential risk policy concentrated persistent-failure alerts within restricted alert budgets
description: A fixed-threshold sequential risk policy concentrated persistent-failure alerts within restricted alert budgets
id: sequential-risk-policy-concentrates-failures
status: review
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
    kind: associational
    rigour: 2
  - id: shihao-wang-2026-2
    resource: "https://arxiv.org/abs/2609.29874"
    title: "Shihao Wang. (2026). A Risk-Adaptive and Evidence-Constrained Framework for Generative AI Feedback in Programming Education. https://arxiv.org/abs/2609.29874"
    author: Shihao Wang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A fixed-threshold sequential risk policy concentrated persistent-failure alerts within restricted alert budgets

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 1 associational `r2`, 1 design `r2` · `q2`

## Subclaims
`q2 i?` The sequential student-history policy triggered on 17.8% of test states with precision 0.566 and captured 25.2% of observed persistent failures. [→ Shihao Wang 2026](#shihao-wang-2026)
`q2 i?` At the planned 20% budget, the consecutive-failures rule captured 75 persistent failures (precision 0.676) versus 62 for the student-history policy (precision 0.559) and 66 for logistic regression (precision 0.595). [→ Shihao Wang 2026 (2)](#shihao-wang-2026-2)

## Evidence

### Shihao Wang 2026

Shihao Wang. (2026). A Risk-Adaptive and Evidence-Constrained Framework for Generative AI Feedback in Programming Education. https://arxiv.org/abs/2609.29874 [doi:10.48550/arxiv.2609.29874](https://doi.org/10.48550/arxiv.2609.29874)

`q2 · i?` · `associational · r2`

Sequential threshold replay over recorded test trajectories with a validation-fixed threshold of 0.500. "Applied to the test sequence, it triggered on 17.8% of states, with precision 0.566 and capture recall 0.252"; a more sensitive configuration reached 22.0% coverage and capture recall 0.333.

> "Applied to the test sequence, it triggered on 17.8% of states, with precision 0.566 and capture recall 0.252."

### Shihao Wang 2026 (2)

Shihao Wang. (2026). A Risk-Adaptive and Evidence-Constrained Framework for Generative AI Feedback in Programming Education. https://arxiv.org/abs/2609.29874

`q2 · i?` · `design · r2`

Fixed-capacity policy comparison at the planned 20% budget (111 alerts) on the labeled test pool. "Logistic regression captured 66 (precision = 0.595; recall = 0.297), while consecutive failures captured 75 (precision = 0.676; recall = 0.338)"; the student-history policy captured 62 with precision 0.559.

> "Logistic regression captured 66 (precision = 0.595; recall = 0.297), while consecutive failures captured 75 (precision = 0.676; recall = 0.338)."

## Discussion


## Related Claims
- [Recorded natural-language feedback was associated with lower odds of subsequent persistent failure than no feedback in the randomized course subset](natural-language-feedback-lower-persistent-failure-odds.md) — related
- [Threshold changes in early alert systems can drastically reshape flagged-student volume and advisor workload and should not occur informally](threshold-change-governance-impact.md) — related

---
type: claim
title: "ITAP's average hint chain length (5.62 token edits) is shorter than the token length of the teacher solution (8.27), suggesting personalized paths"
description: "ITAP's average hint chain length (5.62 token edits) is shorter than the token length of the teacher solution (8.27), suggesting personalized paths"
id: itap-hint-chains-shorter-than-teacher-solution
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
sources:
  - id: kelly-rivers-kenneth-r-koedinger-2015
    resource: "https://doi.org/10.1007/s40593-015-0070-z"
    title: "Kelly Rivers & Kenneth R. Koedinger. (2015). Data-Driven Hint Generation in Vast Solution Spaces: a Self-Improving Python Programming Tutor. International Artificial Intelligence in Education Society. https://doi.org/10.1007/s40593-015-0070-z"
    author: "Kelly Rivers & Kenneth R. Koedinger"
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# ITAP's average hint chain length (5.62 token edits) is shorter than the token length of the teacher solution (8.27), suggesting personalized paths

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On average across all problems, ITAP took 5.62 token edits to reach a correct state, compared with 8.27 tokens in the average teacher solution, indicating hints guide students along shorter, personalized paths. [→ Kelly Rivers & Kenneth R. Koedinger 2015](#kelly-rivers-kenneth-r-koedinger-2015)

## Evidence

### Kelly Rivers & Kenneth R. Koedinger 2015

Kelly Rivers & Kenneth R. Koedinger. (2015). Data-Driven Hint Generation in Vast Solution Spaces: a Self-Improving Python Programming Tutor. International Artificial Intelligence in Education Society. https://doi.org/10.1007/s40593-015-0070-z

`q2 · i?` · `design · r2`

Path-length test using the randomized-order method on the 15-problem dataset. The article compares the 5.62 average to a single-solution system that would need edits equal to the solution's token length, "which is 8.27 on average", and concludes an average below 8.27 "shows great promise".

> "On average across all problems, ITAP took 5.62 token edits to arrive at a correct state (with a standard deviation of 1.16 on average)."

## Discussion


## Related Claims
- [Canonical states shorten hint chains on average (6.00 vs 7.61 edits), though abstract chains were longer for some problems](canonical-states-shorten-hint-chains.md) — related
- [ITAP generated a full token-edit hint chain to a correct solution for 98.3% of semantically incorrect student states in submission order](itap-hint-chain-success-98-percent.md) — related
- [ITAP's hint generation improves as solution data accumulates over time, supporting its self-improving design](itap-self-improves-with-accumulated-data.md) — related
- [ITAP's path success is robust to state ordering: 99.3% of states generated complete paths across 20 randomized-order runs](itap-path-success-robust-randomized-order.md) — related

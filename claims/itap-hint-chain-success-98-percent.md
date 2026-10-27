---
type: claim
title: "ITAP generated a full token-edit hint chain to a correct solution for 98.3% of semantically incorrect student states in submission order"
description: "ITAP generated a full token-edit hint chain to a correct solution for 98.3% of semantically incorrect student states in submission order"
id: itap-hint-chain-success-98-percent
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

# ITAP generated a full token-edit hint chain to a correct solution for 98.3% of semantically incorrect student states in submission order

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Running on 294 semantically incorrect states from 15 students, ITAP produced a complete hint chain to a correct final solution for 98.3% of states, with failures concentrated in one problem. [→ Kelly Rivers & Kenneth R. Koedinger 2015](#kelly-rivers-kenneth-r-koedinger-2015)

## Evidence

### Kelly Rivers & Kenneth R. Koedinger 2015

Kelly Rivers & Kenneth R. Koedinger. (2015). Data-Driven Hint Generation in Vast Solution Spaces: a Self-Improving Python Programming Tutor. International Artificial Intelligence in Education Society. https://doi.org/10.1007/s40593-015-0070-z

`q2 · i?` · `design · r2`

Technical evaluation on a dataset of 585 program states from 15 students in an introductory programming course, of which 294 were syntactically correct but semantically incorrect. ITAP generated full chains for "98.3 % of the solution states (289/294)"; all five failures came from one problem, onlyTwoTrue.

> "For 98.3 % of the solution states (289/294), ITAP was able to generate a full token-edit hint chain to a correct final solution. All five of the chains which could not generate a full path to a correct solution"

## Discussion


## Related Claims
- [Canonical states shorten hint chains on average (6.00 vs 7.61 edits), though abstract chains were longer for some problems](canonical-states-shorten-hint-chains.md) — related
- [ITAP's path success is robust to state ordering: 99.3% of states generated complete paths across 20 randomized-order runs](itap-path-success-robust-randomized-order.md) — related
- [ITAP's average hint chain length (5.62 token edits) is shorter than the token length of the teacher solution (8.27), suggesting personalized paths](itap-hint-chains-shorter-than-teacher-solution.md) — related
- [ITAP's hint generation improves as solution data accumulates over time, supporting its self-improving design](itap-self-improves-with-accumulated-data.md) — related

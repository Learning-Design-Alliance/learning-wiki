---
type: claim
title: "ITAP's hint generation improves as solution data accumulates over time, supporting its self-improving design"
description: "ITAP's hint generation improves as solution data accumulates over time, supporting its self-improving design"
id: itap-self-improves-with-accumulated-data
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: weak
newest_evidence: 2015
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

# ITAP's hint generation improves as solution data accumulates over time, supporting its self-improving design

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2015 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Evaluating hint path lengths at three points of data accumulation (teacher solution only, half the states, all states) against a gold-standard minimum path length shows ITAP's performance improves as more student data is collected. [→ Kelly Rivers & Kenneth R. Koedinger 2015](#kelly-rivers-kenneth-r-koedinger-2015)

## Evidence

### Kelly Rivers & Kenneth R. Koedinger 2015

Kelly Rivers & Kenneth R. Koedinger. (2015). Data-Driven Hint Generation in Vast Solution Spaces: a Self-Improving Python Programming Tutor. International Artificial Intelligence in Education Society. https://doi.org/10.1007/s40593-015-0070-z

`q2 · i?` · `design · r2`

Self-improvement test measuring hint path length for every state at the beginning (teacher solution only), middle (half the states), and end (all states) of solution space construction, compared to a gold standard defined as the minimum length path seen in the 20-random-iteration test. (Detailed results were truncated in the supplied text.)

> "we evaluate changes in hint path length for every state of every problem at three different points of solution data accumulation"

## Discussion


## Related Claims
- [ITAP's average hint chain length (5.62 token edits) is shorter than the token length of the teacher solution (8.27), suggesting personalized paths](itap-hint-chains-shorter-than-teacher-solution.md) — related
- [ITAP's path success is robust to state ordering: 99.3% of states generated complete paths across 20 randomized-order runs](itap-path-success-robust-randomized-order.md) — related
- [ITAP generated a full token-edit hint chain to a correct solution for 98.3% of semantically incorrect student states in submission order](itap-hint-chain-success-98-percent.md) — related
- [Canonical states shorten hint chains on average (6.00 vs 7.61 edits), though abstract chains were longer for some problems](canonical-states-shorten-hint-chains.md) — related

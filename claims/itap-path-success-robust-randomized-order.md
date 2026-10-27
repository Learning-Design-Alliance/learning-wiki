---
type: claim
title: "ITAP's path success is robust to state ordering: 99.3% of states generated complete paths across 20 randomized-order runs"
description: "ITAP's path success is robust to state ordering: 99.3% of states generated complete paths across 20 randomized-order runs"
id: itap-path-success-robust-randomized-order
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

# ITAP's path success is robust to state ordering: 99.3% of states generated complete paths across 20 randomized-order runs

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` When states were fully randomized and ITAP run 20 times with a cleared solution space between iterations, 99.3% (5840/5880) of states generated complete paths to solution. [→ Kelly Rivers & Kenneth R. Koedinger 2015](#kelly-rivers-kenneth-r-koedinger-2015)

## Evidence

### Kelly Rivers & Kenneth R. Koedinger 2015

Kelly Rivers & Kenneth R. Koedinger. (2015). Data-Driven Hint Generation in Vast Solution Spaces: a Self-Improving Python Programming Tutor. International Artificial Intelligence in Education Society. https://doi.org/10.1007/s40593-015-0070-z

`q2 · i?` · `design · r2`

Advanced robustness test using the same 15-student dataset with states fully randomized in order and student traces split into individual states. The article reports "99.3 % (5840/5880)" complete paths, with almost all broken paths again from onlyTwoTrue (93.5% success there).

> "We ran ITAP 20 times with randomized-order data sets, clearing the solution space in between each iteration. 99.3 % (5840/5880) of the states were able to generate complete paths to solution."

## Discussion


## Related Claims
- [ITAP generated a full token-edit hint chain to a correct solution for 98.3% of semantically incorrect student states in submission order](itap-hint-chain-success-98-percent.md) — related
- [ITAP's average hint chain length (5.62 token edits) is shorter than the token length of the teacher solution (8.27), suggesting personalized paths](itap-hint-chains-shorter-than-teacher-solution.md) — related
- [ITAP's hint generation improves as solution data accumulates over time, supporting its self-improving design](itap-self-improves-with-accumulated-data.md) — related
- [Smaller local LLMs show a minor position bias toward option ordering and partially guessing-like error variation, but accuracy remains relatively stable across permutations and repeated sampling runs](minor-position-bias-and-partial-guessing-in-small-llms.md) — related
- [Canonical states shorten hint chains on average (6.00 vs 7.61 edits), though abstract chains were longer for some problems](canonical-states-shorten-hint-chains.md) — related

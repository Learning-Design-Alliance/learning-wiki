---
type: claim
title: Canonical states shorten hint chains on average (6.00 vs 7.61 edits), though abstract chains were longer for some problems
description: Canonical states shorten hint chains on average (6.00 vs 7.61 edits), though abstract chains were longer for some problems
id: canonical-states-shorten-hint-chains
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: mixed
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

# Canonical states shorten hint chains on average (6.00 vs 7.61 edits), though abstract chains were longer for some problems

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Using canonical rather than original states reduced average hint chain length from 7.61 to 6.00 edits, but for three problems (hasTwoDigits, isWeekend, onlyOneTrue) the abstract chain was longer. [→ Kelly Rivers & Kenneth R. Koedinger 2015](#kelly-rivers-kenneth-r-koedinger-2015)

## Evidence

### Kelly Rivers & Kenneth R. Koedinger 2015

Kelly Rivers & Kenneth R. Koedinger. (2015). Data-Driven Hint Generation in Vast Solution Spaces: a Self-Improving Python Programming Tutor. International Artificial Intelligence in Education Society. https://doi.org/10.1007/s40593-015-0070-z

`q2 · i?` · `design · r2`

Test comparing hint chain lengths with and without normalizing functions, using student states in their provided order. The article reports averages of 7.61 (original) versus 6.00 (canonical), with longer abstract chains by 0.8, 0.56, and 0.5 edits for three named problems.

> "we found the average length of hint chains based on original states was 7.61 while the average length of chains based on canonical states was 6.00. However, for some functions (hasTwoDigits, isWeekend, and onlyOneTrue) the abstract chain length was longer"

## Discussion


## Related Claims
- [ITAP's average hint chain length (5.62 token edits) is shorter than the token length of the teacher solution (8.27), suggesting personalized paths](itap-hint-chains-shorter-than-teacher-solution.md) — related
- [ITAP generated a full token-edit hint chain to a correct solution for 98.3% of semantically incorrect student states in submission order](itap-hint-chain-success-98-percent.md) — related
- [ITAP's hint generation improves as solution data accumulates over time, supporting its self-improving design](itap-self-improves-with-accumulated-data.md) — related
- [ITAP's path success is robust to state ordering: 99.3% of states generated complete paths across 20 randomized-order runs](itap-path-success-robust-randomized-order.md) — related
- [Canonicalization reduces solution space size, with a 60% reduction for correct states versus 26% for incorrect states](canonicalization-reduces-solution-space-size.md) — related

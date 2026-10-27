---
type: claim
title: "Canonicalization reduces solution space size, with a 60% reduction for correct states versus 26% for incorrect states"
description: "Canonicalization reduces solution space size, with a 60% reduction for correct states versus 26% for incorrect states"
id: canonicalization-reduces-solution-space-size
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

# Canonicalization reduces solution space size, with a 60% reduction for correct states versus 26% for incorrect states

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Normalizing functions reduced the number of unique states in most problems, with a much larger reduction among correct states (60%) than incorrect states (26%), indicating fewer semantically distinct correct strategies than incorrect attempts. [→ Kelly Rivers & Kenneth R. Koedinger 2015](#kelly-rivers-kenneth-r-koedinger-2015)

## Evidence

### Kelly Rivers & Kenneth R. Koedinger 2015

Kelly Rivers & Kenneth R. Koedinger. (2015). Data-Driven Hint Generation in Vast Solution Spaces: a Self-Improving Python Programming Tutor. International Artificial Intelligence in Education Society. https://doi.org/10.1007/s40593-015-0070-z

`q2 · i?` · `design · r2`

Analysis of the 15-problem dataset (Table 2) measuring percent reduction in distinct states due to canonical abstraction. The article reports a "60 % reduction rate" for correct states versus "26 %" for incorrect states, attributing this to more limited semantic variation among correct strategies.

> "this effect is much more pronounced among the correct states, with a 60 % reduction rate in comparison to the average incorrect state reduction rate of 26 %"

## Discussion


## Related Claims
- [Hint Factory MDP-generated hints gave correct next-step hints over 80% of the time and a pilot showed students solved more logic proofs with hints](hint-factory-mdp-hints-effective.md) — related
- [Canonical states shorten hint chains on average (6.00 vs 7.61 edits), though abstract chains were longer for some problems](canonical-states-shorten-hint-chains.md) — related

---
type: claim
title: Synthetic spoken fixtures received final-release aggregate AI scores of 100, 62 and 8 out of 100, with the expected qualitative ordering in both runs
description: Synthetic spoken fixtures received final-release aggregate AI scores of 100, 62 and 8 out of 100, with the expected qualitative ordering in both runs
id: calliope-fixture-aggregate-scores-ordering
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: nizam-kadir-2026
    resource: "https://doi.org/10.2139/ssrn.7524302"
    title: "Nizam Kadir. (2026). CALLIOPE: A Source-Grounded Oral Assessment System and Synthetic Readiness Evaluation. arXiv. [doi:10.2139/ssrn.7524302](https://doi.org/10.2139/ssrn.7524302)"
    author: Nizam Kadir
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Synthetic spoken fixtures received final-release aggregate AI scores of 100, 62 and 8 out of 100, with the expected qualitative ordering in both runs

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q1 i?` In the final release rehearsal, the supported, partial and misconception fixtures received aggregate AI scores of 100, 62 and 8 respectively, and the expected qualitative ordering occurred in both release runs. [→ Nizam Kadir 2026](#nizam-kadir-2026)

## Evidence

### Nizam Kadir 2026

Nizam Kadir. (2026). CALLIOPE: A Source-Grounded Oral Assessment System and Synthetic Readiness Evaluation. arXiv. [doi:10.2139/ssrn.7524302](https://doi.org/10.2139/ssrn.7524302)

`q1 · i?` · `design · r2`

Synthetic two-run rehearsal of the two-provider scoring pipeline on three machine-voiced fixtures; Table 3 records final-release aggregates of 100, 62 and 8 (values of 100G, not human grades). The article states "The expected qualitative ordering occurred in both runs" while cautioning the fixtures are not an independently labelled benchmark.

> "The expected qualitative ordering occurred in both runs, but the fixtures were deliberately constructed to differ strongly in content."

## Discussion


## Related Claims
- Across two release runs, all eight retrieved synthetic audio files were byte-identical to their inputs by SHA-256 hash — related
- [Two of three spoken fixtures were flagged for provider disagreement in each run, with maximum provider differences of 0.60 and 0.80](calliope-provider-disagreement-flags.md) — related
- Duplicate evaluation requests in the final release reported an already-submitted state without repeat evaluation in the exercised path — related

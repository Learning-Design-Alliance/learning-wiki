---
type: claim
title: "Qualitative inspection shows dAFM refinement remaps a Geometry problem's items toward side-identification KCs with plausible but partly spurious associations"
description: "Qualitative inspection shows dAFM refinement remaps a Geometry problem's items toward side-identification KCs with plausible but partly spurious associations"
id: dafm-qualitative-remapping-triangle-rectangle
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: weak
sources:
  - id: pardos-2018
    resource: "https://github.com/CAHLR/dAFM"
    title: "Pardos, Z. A., & Dadu, A. (2018). dAFM: Fusing Psychometric and Connectionist Modeling for Q-matrix Refinement. Journal of Educational Data Mining, Volume 10, No 2. https://github.com/CAHLR/dAFM"
    author: "Pardos, Z. A., & Dadu, A."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Qualitative inspection shows dAFM refinement remaps a Geometry problem's items toward side-identification KCs with plausible but partly spurious associations

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` The most improved Geometry problem, Triangle Rectangle, was re-mapped mainly to triangle-side (weight 1.05), with refinements emphasizing side identification over area computation, and one association judged spurious. [→ Pardos 2018](#pardos-2018)

## Evidence

### Pardos 2018

Pardos, Z. A., & Dadu, A. (2018). dAFM: Fusing Psychometric and Connectionist Modeling for Q-matrix Refinement. Journal of Educational Data Mining, Volume 10, No 2. https://github.com/CAHLR/dAFM

`q2 · i?` · `design · r2`

Qualitative case study of the single Geometry problem with the largest test-set RMSE improvement (38.29% per Table 10), depicting original versus refined KC associations (Figure 7). The article reports the refined weights, including compose-by-multiplication at 0.19 and pentagon-side at 0.08; no effect size applies.

> "In dAFM, it has mainly been re-mapped to identifying triangle-side (weight value = 1.05), shown in Figure 7."

## Discussion


## Related Claims
- [An expert-initialized Q-matrix refined by dAFM outperforms a Q-matrix learned from the ground-up in nearly all cases](expert-refined-qmatrix-beats-ground-up-learning.md) — related
- [Replacing the linear qk activation with ReLU sacrifices very little predictive accuracy while prohibiting negative Q-matrix values](relu-activation-preserves-dafm-accuracy.md) — related
- [Q-matrices clustered from DKT and skip-gram item embeddings do not outperform dAFM models but do outperform a randomly initialized Q-matrix](embedding-clustered-qmatrices-null-versus-dafm.md) — related

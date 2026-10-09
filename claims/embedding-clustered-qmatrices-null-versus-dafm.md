---
type: claim
title: Q-matrices clustered from DKT and skip-gram item embeddings do not outperform dAFM models but do outperform a randomly initialized Q-matrix
description: Q-matrices clustered from DKT and skip-gram item embeddings do not outperform dAFM models but do outperform a randomly initialized Q-matrix
id: embedding-clustered-qmatrices-null-versus-dafm
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

# Q-matrices clustered from DKT and skip-gram item embeddings do not outperform dAFM models but do outperform a randomly initialized Q-matrix

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` K-means clustering of DKT and skip-gram item embeddings did not produce a better-predicting Q-matrix than the dAFM models except random-init, though neither method beat even base AFM. [→ Pardos 2018](#pardos-2018)

## Evidence

### Pardos 2018

Pardos, Z. A., & Dadu, A. (2018). dAFM: Fusing Psychometric and Connectionist Modeling for Q-matrix Refinement. Journal of Educational Data Mining, Volume 10, No 2. https://github.com/CAHLR/dAFM

`q2 · i?` · `design · r2`

Development-set comparison (Table 6) of Q-matrices derived by k-means clustering of DKT and skip-gram item embeddings against dAFM variants, evaluated by validation RMSE. The article calls this a null result since neither method beat base AFM, but outperforming random-init suggests promise for ground-up learning; no effect size is printed.

> "Clustering the space into different sizes of k using these models; however, did not produce a better predicting Q-matrix than the dAFM models (except for random-init), as seen in Table 6."

## Discussion


## Related Claims
- [Base AFM with its expert Q-matrix generalizes better than a ground-up learned Q-matrix only on the large Cognitive Tutor Bridge datasets](afm-beats-random-init-only-on-large-cogtutor-datasets.md) — related
- [Fine-tuning the AFM model including its Q-matrix improves test-set prediction in four of five datasets and is the best model in eight of ten experiments](dafm-fine-tuned-improves-prediction-over-afm.md) — related
- [Qualitative inspection shows dAFM refinement remaps a Geometry problem's items toward side-identification KCs with plausible but partly spurious associations](dafm-qualitative-remapping-triangle-rectangle.md) — related
- [An expert-initialized Q-matrix refined by dAFM outperforms a Q-matrix learned from the ground-up in nearly all cases](expert-refined-qmatrix-beats-ground-up-learning.md) — related

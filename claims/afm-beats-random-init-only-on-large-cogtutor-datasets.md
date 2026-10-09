---
type: claim
title: Base AFM with its expert Q-matrix generalizes better than a ground-up learned Q-matrix only on the large Cognitive Tutor Bridge datasets
description: Base AFM with its expert Q-matrix generalizes better than a ground-up learned Q-matrix only on the large Cognitive Tutor Bridge datasets
id: afm-beats-random-init-only-on-large-cogtutor-datasets
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: moderate
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

# Base AFM with its expert Q-matrix generalizes better than a ground-up learned Q-matrix only on the large Cognitive Tutor Bridge datasets

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Base AFM generalizes better than the random-init ground-up Q-matrix model on the two large Cognitive Tutor Bridge datasets but is worse on the other three datasets in both validation and test predictions. [→ Pardos 2018](#pardos-2018)

## Evidence

### Pardos 2018

Pardos, Z. A., & Dadu, A. (2018). dAFM: Fusing Psychometric and Connectionist Modeling for Q-matrix Refinement. Journal of Educational Data Mining, Volume 10, No 2. https://github.com/CAHLR/dAFM

`q2 · i?` · `design · r2`

RMSE comparison of the dafm-afm baseline against random-init across the five primary datasets (Tables 7 and 8). The article reports the direction reverses by dataset size, with AFM better on the large Bridge sets and worse on the other three; no effect size is printed.

> "Comparing the base AFM model to random, AFM generalizes better than the ground-up learned Q-matrix model in the large Cognitive Tutor Bridge datasets, but AFM is worse in the other three in both the validation and test set predictions."

## Discussion


## Related Claims
- [Q-matrices clustered from DKT and skip-gram item embeddings do not outperform dAFM models but do outperform a randomly initialized Q-matrix](embedding-clustered-qmatrices-null-versus-dafm.md) — related
- [An expert-initialized Q-matrix refined by dAFM outperforms a Q-matrix learned from the ground-up in nearly all cases](expert-refined-qmatrix-beats-ground-up-learning.md) — related
- [Fine-tuning the AFM model including its Q-matrix improves test-set prediction in four of five datasets and is the best model in eight of ten experiments](dafm-fine-tuned-improves-prediction-over-afm.md) — related
- [Training dAFM with individualized student ability estimates yields essentially no prediction benefit over average ability](individualized-ability-no-benefit-dafm.md) — related

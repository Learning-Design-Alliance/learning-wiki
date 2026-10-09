---
type: claim
title: An expert-initialized Q-matrix refined by dAFM outperforms a Q-matrix learned from the ground-up in nearly all cases
description: An expert-initialized Q-matrix refined by dAFM outperforms a Q-matrix learned from the ground-up in nearly all cases
id: expert-refined-qmatrix-beats-ground-up-learning
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

# An expert-initialized Q-matrix refined by dAFM outperforms a Q-matrix learned from the ground-up in nearly all cases

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Comparing random-init to expert-init, the expert-refined model outperforms the KC model learned from the ground-up in all cases except the Geometry validation set. [→ Pardos 2018](#pardos-2018)

## Evidence

### Pardos 2018

Pardos, Z. A., & Dadu, A. (2018). dAFM: Fusing Psychometric and Connectionist Modeling for Q-matrix Refinement. Journal of Educational Data Mining, Volume 10, No 2. https://github.com/CAHLR/dAFM

`q2 · i?` · `design · r2`

RMSE comparison of the random-init and expert-init dAFM variants across the five primary datasets in validation and test predictions (Tables 7 and 8). The article names both sides of the comparison and reports the single Geometry validation exception; no effect size is printed.

> "Comparing a random to an expert initialized Q-matrix, the expert reﬁned model outperforms the KC model learned from the ground-up in all cases except for on the validation set of Geometry."

## Discussion


## Related Claims
- [Base AFM with its expert Q-matrix generalizes better than a ground-up learned Q-matrix only on the large Cognitive Tutor Bridge datasets](afm-beats-random-init-only-on-large-cogtutor-datasets.md) — related
- [Fine-tuning the AFM model including its Q-matrix improves test-set prediction in four of five datasets and is the best model in eight of ten experiments](dafm-fine-tuned-improves-prediction-over-afm.md) — related
- [Qualitative inspection shows dAFM refinement remaps a Geometry problem's items toward side-identification KCs with plausible but partly spurious associations](dafm-qualitative-remapping-triangle-rectangle.md) — related
- [Q-matrices clustered from DKT and skip-gram item embeddings do not outperform dAFM models but do outperform a randomly initialized Q-matrix](embedding-clustered-qmatrices-null-versus-dafm.md) — related

---
type: claim
title: Fine-tuning the AFM model including its Q-matrix improves test-set prediction in four of five datasets and is the best model in eight of ten experiments
description: Fine-tuning the AFM model including its Q-matrix improves test-set prediction in four of five datasets and is the best model in eight of ten experiments
id: dafm-fine-tuned-improves-prediction-over-afm
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

# Fine-tuning the AFM model including its Q-matrix improves test-set prediction in four of five datasets and is the best model in eight of ten experiments

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Fine-tuning the learned AFM model including its Q-matrix improves prediction on all primary datasets except Cognitive Tutor Bridge 2006-2007 and is the best model in eight of ten validation and test experiments. [→ Pardos 2018](#pardos-2018)

## Evidence

### Pardos 2018

Pardos, Z. A., & Dadu, A. (2018). dAFM: Fusing Psychometric and Connectionist Modeling for Q-matrix Refinement. Journal of Educational Data Mining, Volume 10, No 2. https://github.com/CAHLR/dAFM

`q2 · i?` · `design · r2`

Prediction-accuracy comparison of six dAFM variants across five tutoring-system datasets (Tables 7 and 8), evaluated by RMSE on held-out students. The article reports the fine-tuned variant "is the best model all-around in eight of the ten experiments"; no effect size is printed.

> "If the learned AFM model, including its Q-matrix, is ﬁne-tuned, the resultant model shows improvement in all datasets except for the CogTutor Bridge '06-'07 dataset and is the best model all-around in eight of the ten experiments (combining validation and test results)."

## Discussion


## Related Claims
- [Base AFM with its expert Q-matrix generalizes better than a ground-up learned Q-matrix only on the large Cognitive Tutor Bridge datasets](afm-beats-random-init-only-on-large-cogtutor-datasets.md) — related
- [An expert-initialized Q-matrix refined by dAFM outperforms a Q-matrix learned from the ground-up in nearly all cases](expert-refined-qmatrix-beats-ground-up-learning.md) — related
- [Q-matrices clustered from DKT and skip-gram item embeddings do not outperform dAFM models but do outperform a randomly initialized Q-matrix](embedding-clustered-qmatrices-null-versus-dafm.md) — related
- [Training dAFM with individualized student ability estimates yields essentially no prediction benefit over average ability](individualized-ability-no-benefit-dafm.md) — related
- [Replacing the linear qk activation with ReLU sacrifices very little predictive accuracy while prohibiting negative Q-matrix values](relu-activation-preserves-dafm-accuracy.md) — related

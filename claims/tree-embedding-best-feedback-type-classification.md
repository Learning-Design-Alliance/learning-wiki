---
type: claim
title: "Tree embedding-based encoding with a classifier performs best at classifying feedback types for incorrect steps, reaching 78.71% accuracy across 24 feedback types"
description: "Tree embedding-based encoding with a classifier performs best at classifying feedback types for incorrect steps, reaching 78.71% accuracy across 24 feedback types"
id: tree-embedding-best-feedback-type-classification
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2021
recheck_by: 2024
sources:
  - id: mengxue-zhang-2021
    resource: "https://doi.org/10.48550/arXiv.2104.12047"
    title: "Mengxue Zhang, Zichao Wang, Richard Baraniuk, Andrew Lan. (2021). Math Operation Embeddings for Open-ended Solution Analysis and Feedback. [doi:10.48550/arXiv.2104.12047](https://doi.org/10.48550/arXiv.2104.12047)"
    author: Mengxue Zhang, Zichao Wang, Richard Baraniuk, Andrew Lan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Tree embedding-based encoding with a classifier performs best at classifying feedback types for incorrect steps, reaching 78.71% accuracy across 24 feedback types

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the BUG subset feedback classification task with 24 feedback types, TE+C performs best (78.71±1.74) and GRU-based encoding also performs well, while TransE and TransR perform slightly worse due to shortage of training data. [→ Mengxue Zhang 2021](#mengxue-zhang-2021)

## Evidence

### Mengxue Zhang 2021

Mengxue Zhang, Zichao Wang, Richard Baraniuk, Andrew Lan. (2021). Math Operation Embeddings for Open-ended Solution Analysis and Feedback. [doi:10.48550/arXiv.2104.12047](https://doi.org/10.48550/arXiv.2104.12047)

`q2 · i?` · `design · r2`

Numerical experiment (Section 5.4.5, Table 5) with 5-fold cross-validation on the BUG subset (5,744 steps, 24 feedback types); TE+C reaches 78.71±1.74 accuracy and "the tree embedding-based encoder in conjunction with a classiﬁer performs best".

> "we see that the tree embedding-based encoder in conjunction with a classiﬁer performs best while GRU-based encoding also performs well."

## Discussion


## Related Claims
- [Training on synthetically generated steps, tree embedding-based methods significantly outperform GRU and CNN encoders when tested on real student data](synthetic-training-tree-embeddings-outperform-real-data.md) — related
- [Tree embedding-based encoding with a classifier achieves the highest math operation classification accuracy on the CogTutor OK subset and remains effective on incorrect steps](tree-embedding-classifier-best-operation-classification.md) — related
- [Tree embedding-based encoding outperforms GRU-based encoding when generalizing across question difficulty levels in equation solving](tree-embeddings-outperform-gru-across-difficulty-levels.md) — related

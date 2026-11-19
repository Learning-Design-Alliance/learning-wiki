---
type: claim
title: Tree embedding-based encoding outperforms GRU-based encoding when generalizing across question difficulty levels in equation solving
description: Tree embedding-based encoding outperforms GRU-based encoding when generalizing across question difficulty levels in equation solving
id: tree-embeddings-outperform-gru-across-difficulty-levels
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

# Tree embedding-based encoding outperforms GRU-based encoding when generalizing across question difficulty levels in equation solving

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Training on steps at one difficulty level and testing on others, TE+C outperforms GRU+C in almost every case across the six OK-subset difficulty levels. [→ Mengxue Zhang 2021](#mengxue-zhang-2021)

## Evidence

### Mengxue Zhang 2021

Mengxue Zhang, Zichao Wang, Richard Baraniuk, Andrew Lan. (2021). Math Operation Embeddings for Open-ended Solution Analysis and Feedback. [doi:10.48550/arXiv.2104.12047](https://doi.org/10.48550/arXiv.2104.12047)

`q2 · i?` · `design · r2`

Numerical experiment (Section 5.4.2, Table 3) training on steps at each of six difficulty levels (ES 01 to ES 07) and testing on other levels including incorrect steps; the article reports "TE+C overall outperforms GRU+C in almost every case".

> "We see that TE+C overall outperforms GRU+C in almost every case. This results suggest that tree embeddings are eﬀective at capturing the structural property of a math expression."

## Discussion


## Related Claims
- [Training on synthetically generated steps, tree embedding-based methods significantly outperform GRU and CNN encoders when tested on real student data](synthetic-training-tree-embeddings-outperform-real-data.md) — related
- [Tree embedding-based encoding with a classifier performs best at classifying feedback types for incorrect steps, reaching 78.71% accuracy across 24 feedback types](tree-embedding-best-feedback-type-classification.md) — related
- [Tree embedding-based encoding with a classifier achieves the highest math operation classification accuracy on the CogTutor OK subset and remains effective on incorrect steps](tree-embedding-classifier-best-operation-classification.md) — related

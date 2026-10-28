---
type: claim
title: Graph community detection over QBERT-RR embeddings yields 5,930 question communities, with 5,337 questions having no similar group
description: Graph community detection over QBERT-RR embeddings yields 5,930 question communities, with 5,337 questions having no similar group
id: wtc-5930-question-communities
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2024
sources:
  - id: zhaozhen-xu-2024
    resource: "https://doi.org/10.1007/s40593-023-00377-8"
    title: "Zhaozhen Xu, Amelia Howarth, Nicole Briggs, Nello Cristianini. (2024). Understanding Visitors' Curiosity in a Science Centre with Deep Question Processing Network. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-023-00377-8"
    author: Zhaozhen Xu, Amelia Howarth, Nicole Briggs, Nello Cristianini
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Graph community detection over QBERT-RR embeddings yields 5,930 question communities, with 5,337 questions having no similar group

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Clustering WTC questions by cosine similarity above threshold produces 5,930 communities, and 5,337 questions lack any similar question group. [→ Zhaozhen Xu 2024](#zhaozhen-xu-2024)

## Evidence

### Zhaozhen Xu 2024

Zhaozhen Xu, Amelia Howarth, Nicole Briggs, Nello Cristianini. (2024). Understanding Visitors' Curiosity in a Science Centre with Deep Question Processing Network. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-023-00377-8

`q2 · i?` · `design · r2`

Graph community detection experiment on the WTC corpus: a graph is built with question nodes and edges where pairwise cosine similarity exceeds the threshold. The article reports "There are 5,930 communities found in the WTC corpus" and 5,337 questions without similar groups.

> "There are 5,930 communities found in the WTC corpus, which represents 5,930 different questions in the corpus. Of these, 5,337 questions do not have any similar question groups in the corpus."

## Discussion


## Related Claims
- [QBERT-RR finds high-confidence one-sentence Wikipedia answers for 463 WTC questions](wtc-463-questions-answered-wikipedia.md) — related
- [QBERT-RR transfers to the unseen WTC question corpus with 90.76% equivalent-question recognition accuracy at a 0.809 threshold](qbert-transfers-to-wtc-corpus.md) — related
- [QBERT-RR outperforms the E5 embedding model on question topic and equivalence tasks while E5 leads on answer retrieval](qbert-rr-vs-e5-task-dependent.md) — a broader claim this one bears on
- [The multi-task QBERT-RR generalist achieves comparable or better accuracy than single-task SBERT models on question topic, equivalence, and answering tasks](qbert-rr-comparable-or-better-than-single-task.md) — a broader claim this one bears on
- [WTC corpus questions concentrate in Science & Mathematics (55.66%) and over half are causal HOW/WHY questions](wtc-topic-type-distribution.md) — related

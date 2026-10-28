---
type: claim
title: "QBERT-RR transfers to the unseen WTC question corpus with 90.76% equivalent-question recognition accuracy at a 0.809 threshold"
description: "QBERT-RR transfers to the unseen WTC question corpus with 90.76% equivalent-question recognition accuracy at a 0.809 threshold"
id: qbert-transfers-to-wtc-corpus
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
  - id: zhaozhen-xu-2024-2
    resource: "https://doi.org/10.1007/s40593-023-00377-8"
    title: "Zhaozhen Xu, Amelia Howarth, Nicole Briggs, Nello Cristianini. (2024). Understanding Visitors' Curiosity in a Science Centre with Deep Question Processing Network. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-023-00377-8"
    author: Zhaozhen Xu, Amelia Howarth, Nicole Briggs, Nello Cristianini
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# QBERT-RR transfers to the unseen WTC question corpus with 90.76% equivalent-question recognition accuracy at a 0.809 threshold

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` On human-labelled WTC question pairs, QBERT-RR reaches 90.76% accuracy, similar to its QQP performance of 90.13%. [→ Zhaozhen Xu 2024](#zhaozhen-xu-2024)
`q2 i?` The two annotators labelling the WTC pairs reached a Cohen's Kappa of 0.75. [→ Zhaozhen Xu 2024 (2)](#zhaozhen-xu-2024-2)

## Evidence

### Zhaozhen Xu 2024

Zhaozhen Xu, Amelia Howarth, Nicole Briggs, Nello Cristianini. (2024). Understanding Visitors' Curiosity in a Science Centre with Deep Question Processing Network. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-023-00377-8

`q2 · i?` · `design · r2`

Evaluation on 5,022 WTC question pairs sampled and labelled by two annotators (728 equivalent, 4,294 different). The article reports 90.76% accuracy at threshold 0.809, "a similar performance to QBERT-RR on the QQP dataset (90.13% accuracy)".

> "When the cosine similarity threshold is 0.809, QBERT-RR obtains 90.76% accuracy on the sampling WTC data, which is a similar performance to QBERT-RR on the QQP dataset (90.13% accuracy)."

### Zhaozhen Xu 2024 (2)

Zhaozhen Xu, Amelia Howarth, Nicole Briggs, Nello Cristianini. (2024). Understanding Visitors' Curiosity in a Science Centre with Deep Question Processing Network. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-023-00377-8

`q2 · i?` · `design · r2`

Inter-annotator agreement measured on 30 additional question pairs labelled by each of the two annotators of the WTC equivalent-question sample; the article prints "The Cohen's Kappa (Cohen, 1960) between two annotators is 0.75".

> "The Cohen's Kappa (Cohen, 1960) between two annotators is 0.75."

## Discussion


## Related Claims
- [The multi-task QBERT-RR generalist achieves comparable or better accuracy than single-task SBERT models on question topic, equivalence, and answering tasks](qbert-rr-comparable-or-better-than-single-task.md) — related
- [QBERT-RR finds high-confidence one-sentence Wikipedia answers for 463 WTC questions](wtc-463-questions-answered-wikipedia.md) — related
- [Graph community detection over QBERT-RR embeddings yields 5,930 question communities, with 5,337 questions having no similar group](wtc-5930-question-communities.md) — related
- [WTC corpus questions concentrate in Science & Mathematics (55.66%) and over half are causal HOW/WHY questions](wtc-topic-type-distribution.md) — related

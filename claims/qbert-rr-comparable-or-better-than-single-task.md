---
type: claim
title: The multi-task QBERT-RR generalist achieves comparable or better accuracy than single-task SBERT models on question topic, equivalence, and answering tasks
description: The multi-task QBERT-RR generalist achieves comparable or better accuracy than single-task SBERT models on question topic, equivalence, and answering tasks
id: qbert-rr-comparable-or-better-than-single-task
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
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

# The multi-task QBERT-RR generalist achieves comparable or better accuracy than single-task SBERT models on question topic, equivalence, and answering tasks

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` QBERT-RR, trained jointly with a round-robin curriculum, matches or exceeds single-task models on most question datasets. [→ Zhaozhen Xu 2024](#zhaozhen-xu-2024)

## Evidence

### Zhaozhen Xu 2024

Zhaozhen Xu, Amelia Howarth, Nicole Briggs, Nello Cristianini. (2024). Understanding Visitors' Curiosity in a Science Centre with Deep Question Processing Network. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-023-00377-8

`q2 · i?` · `design · r2`

Benchmark evaluation on Yahoo Topic, QQP, and WikiQA test sets (Table 4) comparing QBERT-RR against single-task QT, QE, and QA models built on the same architecture. The article reports that "QBERT-RR achieves comparable or better performance on most question datasets"; per-column accuracies are printed in the table.

> "The results show that QBERT-RR achieves comparable or better performance on most question datasets compared to the single-task model."

## Discussion


## Related Claims
- [QBERT-RR outperforms the E5 embedding model on question topic and equivalence tasks while E5 leads on answer retrieval](qbert-rr-vs-e5-task-dependent.md) — related
- [QBERT-RR transfers to the unseen WTC question corpus with 90.76% equivalent-question recognition accuracy at a 0.809 threshold](qbert-transfers-to-wtc-corpus.md) — related
- [Graph community detection over QBERT-RR embeddings yields 5,930 question communities, with 5,337 questions having no similar group](wtc-5930-question-communities.md) — a narrower finding that bears on this claim
- [Multi-task learning on a large multi-topic dataset outperforms separate topic-specific essay scoring models](mtl-multi-topic-beats-topic-specific-scoring.md) — a narrower finding that bears on this claim

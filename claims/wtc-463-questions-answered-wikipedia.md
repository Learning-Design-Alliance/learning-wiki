---
type: claim
title: QBERT-RR finds high-confidence one-sentence Wikipedia answers for 463 WTC questions
description: QBERT-RR finds high-confidence one-sentence Wikipedia answers for 463 WTC questions
id: wtc-463-questions-answered-wikipedia
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

# QBERT-RR finds high-confidence one-sentence Wikipedia answers for 463 WTC questions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` After filtering by a 0.795 cosine-similarity confidence threshold, 463 of the 8,600 WTC questions can be answered from Wikipedia Summary. [→ Zhaozhen Xu 2024](#zhaozhen-xu-2024)

## Evidence

### Zhaozhen Xu 2024

Zhaozhen Xu, Amelia Howarth, Nicole Briggs, Nello Cristianini. (2024). Understanding Visitors' Curiosity in a Science Centre with Deep Question Processing Network. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-023-00377-8

`q2 · i?` · `design · r2`

Open-domain open-book QA retrieval over roughly 21M Wikipedia Summary sentences, embedded with QBERT-RR and searched via approximate nearest neighbour. The article reports "there are 463 questions in the corpus that can ﬁnd an answer within the Wikipedia Summary" above the confidence threshold.

> "After ﬁltering the high-conﬁdence answers, there are 463 questions in the corpus that can ﬁnd an answer within the Wikipedia Summary using QBERT-RR."

## Discussion


## Related Claims
- [QBERT-RR transfers to the unseen WTC question corpus with 90.76% equivalent-question recognition accuracy at a 0.809 threshold](qbert-transfers-to-wtc-corpus.md) — related
- [QBERT-RR outperforms the E5 embedding model on question topic and equivalence tasks while E5 leads on answer retrieval](qbert-rr-vs-e5-task-dependent.md) — related
- [Raising the answer-confidence threshold reduces the number of retained MCQs but substantially improves their quality](answer-confidence-threshold-trades-quantity-for-quality.md) — related
- [Graph community detection over QBERT-RR embeddings yields 5,930 question communities, with 5,337 questions having no similar group](wtc-5930-question-communities.md) — related
- [WTC corpus questions concentrate in Science & Mathematics (55.66%) and over half are causal HOW/WHY questions](wtc-topic-type-distribution.md) — related

---
type: claim
title: AlgoRAG answered all 179 TCS exam-style questions successfully with a mean response time of 38.0 seconds and a pedagogical quality score of 0.7620
description: AlgoRAG answered all 179 TCS exam-style questions successfully with a mean response time of 38.0 seconds and a pedagogical quality score of 0.7620
id: algorag-100-success-179-tcs-questions
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: sushan-adhikari-2026
    resource: "https://arxiv.org/abs/2609.14572"
    title: "Sushan Adhikari. (2026). AlgoRAG: Retrieval-Augmented Generation for Theoretical Computer Science Education — A Comprehensive Evaluation Framework for Algorithm Analysis and Complexity Theory. arXiv preprint. https://arxiv.org/abs/2609.14572"
    author: Sushan Adhikari
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# AlgoRAG answered all 179 TCS exam-style questions successfully with a mean response time of 38.0 seconds and a pedagogical quality score of 0.7620

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` AlgoRAG achieved a 100% success rate, 38.0 s mean response time, and pedagogical quality of 0.7620 across 179 questions, with low lexical-overlap scores. [→ Sushan Adhikari 2026](#sushan-adhikari-2026)

## Evidence

### Sushan Adhikari 2026

Sushan Adhikari. (2026). AlgoRAG: Retrieval-Augmented Generation for Theoretical Computer Science Education — A Comprehensive Evaluation Framework for Algorithm Analysis and Complexity Theory. arXiv preprint. https://arxiv.org/abs/2609.14572

`q2 · i?` · `design · r2`

System evaluation on 179 expert-curated exam-style questions across seven TCS topics, each with instructor-written reference answers. The article reports "100% success rate" with 38.0 s mean response time, BLEU-4 of 0.0000, ROUGE-1 F1 of 0.0963, and pedagogical quality of 0.7620 (Table 1).

> "AlgoRAG answered all 179 questions successfully (100% success rate) with a mean response time of 38.0 seconds. Table 1 summarizes the aggregate metrics."

## Discussion


## Related Claims
- [Per-topic performance varied: NP-completeness scored highest ROUGE-1 F1 (0.1285), sorting algorithms highest pedagogical quality (0.8250), and recurrence relations lowest pedagogical quality (0.6629)](algorag-topic-specific-performance-variation.md) — a narrower finding that bears on this claim
- [BLEU-4 scored zero on all 179 mathematical-proof responses, which the authors interpret as a property of n-gram metrics rather than system failure](bleu4-zero-mathematical-proofs-metric-limitation.md) — a narrower finding that bears on this claim
- [Pedagogical-criterion breakdown shows worked examples in only about 42% of responses, the weakest criterion despite 312 practice problems in the knowledge base](algorag-worked-example-retrieval-42-percent.md) — a narrower finding that bears on this claim

---
type: claim
title: "Per-topic performance varied: NP-completeness scored highest ROUGE-1 F1 (0.1285), sorting algorithms highest pedagogical quality (0.8250), and recurrence relations lowest pedagogical quality (0.6629)"
description: "Per-topic performance varied: NP-completeness scored highest ROUGE-1 F1 (0.1285), sorting algorithms highest pedagogical quality (0.8250), and recurrence relations lowest pedagogical quality (0.6629)"
id: algorag-topic-specific-performance-variation
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

# Per-topic performance varied: NP-completeness scored highest ROUGE-1 F1 (0.1285), sorting algorithms highest pedagogical quality (0.8250), and recurrence relations lowest pedagogical quality (0.6629)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Pedagogical quality ranged 0.6629–0.8250 across topics while ROUGE-1 F1 stayed low and near-uniform (0.0876–0.1285). [→ Sushan Adhikari 2026](#sushan-adhikari-2026)

## Evidence

### Sushan Adhikari 2026

Sushan Adhikari. (2026). AlgoRAG: Retrieval-Augmented Generation for Theoretical Computer Science Education — A Comprehensive Evaluation Framework for Algorithm Analysis and Complexity Theory. arXiv preprint. https://arxiv.org/abs/2609.14572

`q2 · i?` · `design · r2`

Per-topic analysis over the 179-question test set (Table 2, Fig. 2). NP-completeness (n=21) achieved the highest "ROUGE-1 F1 (0.1285)"; sorting algorithms (n=6) scored highest pedagogical quality at 0.8250; graph algorithms (n=21) reached 0.8086; recurrence relations (n=17) scored lowest at 0.6629.

> "NP-completeness achieved the highest ROUGE-1 F1 (0.1285), likely because reduction proofs and complexity-class definitions follow comparatively standardized phrasing"

## Discussion


## Related Claims
- [AlgoRAG answered all 179 TCS exam-style questions successfully with a mean response time of 38.0 seconds and a pedagogical quality score of 0.7620](algorag-100-success-179-tcs-questions.md) — a broader claim this one bears on
- [BLEU-4 scored zero on all 179 mathematical-proof responses, which the authors interpret as a property of n-gram metrics rather than system failure](bleu4-zero-mathematical-proofs-metric-limitation.md) — related
- [Mined misconception labels match personas' assigned misconceptions at F1 ≈ 0.56, a score that does not test whether generated questions elicit the named misconception](collearn-misconception-mining-f1.md) — related

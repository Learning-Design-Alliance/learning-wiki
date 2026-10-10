---
type: claim
title: BLEU-4 scored zero on all 179 mathematical-proof responses, which the authors interpret as a property of n-gram metrics rather than system failure
description: BLEU-4 scored zero on all 179 mathematical-proof responses, which the authors interpret as a property of n-gram metrics rather than system failure
id: bleu4-zero-mathematical-proofs-metric-limitation
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

# BLEU-4 scored zero on all 179 mathematical-proof responses, which the authors interpret as a property of n-gram metrics rather than system failure

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` BLEU-4 was zero across all 179 questions because logically equivalent proofs share almost no n-grams when notation, variable names, or proof strategy differ. [→ Sushan Adhikari 2026](#sushan-adhikari-2026)

## Evidence

### Sushan Adhikari 2026

Sushan Adhikari. (2026). AlgoRAG: Retrieval-Augmented Generation for Theoretical Computer Science Education — A Comprehensive Evaluation Framework for Algorithm Analysis and Complexity Theory. arXiv preprint. https://arxiv.org/abs/2609.14572

`q2 · i?` · `design · r2`

Evaluation of all 179 AlgoRAG responses against instructor reference answers found BLEU-4 of 0.0000 on every question. The article states this shows "mathematical proofs routinely use logically equivalent but lexically distinct formulations", so n-gram precision fails for proof evaluation.

> "BLEU-4 is zero across all questions, confirming that mathematical proofs routinely use logically equivalent but lexically distinct formulations."

## Discussion


## Related Claims
- [AlgoRAG answered all 179 TCS exam-style questions successfully with a mean response time of 38.0 seconds and a pedagogical quality score of 0.7620](algorag-100-success-179-tcs-questions.md) — a broader claim this one bears on
- [Per-topic performance varied: NP-completeness scored highest ROUGE-1 F1 (0.1285), sorting algorithms highest pedagogical quality (0.8250), and recurrence relations lowest pedagogical quality (0.6629)](algorag-topic-specific-performance-variation.md) — related

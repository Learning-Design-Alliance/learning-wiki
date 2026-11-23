---
type: claim
title: Static random exemplar selection outperforms similarity-based selection, and adding more exemplars does not enhance performance
description: Static random exemplar selection outperforms similarity-based selection, and adding more exemplars does not enhance performance
id: static-random-exemplars-beat-similarity-selection
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: weak
newest_evidence: 2025
sources:
  - id: sukannya-purkayastha-2025
    resource: "https://doi.org/10.18653/v1/2025.acl-long.165"
    title: "Sukannya Purkayastha, Zhuang Li, Anne Lauscher, Lizhen Qu, Iryna Gurevych. (2025). LAZY REVIEW: A Dataset for Uncovering Lazy Thinking in NLP Peer Reviews. arXiv. [doi:10.18653/v1/2025.acl-long.165](https://doi.org/10.18653/v1/2025.acl-long.165)"
    author: Sukannya Purkayastha, Zhuang Li, Anne Lauscher, Lizhen Qu, Iryna Gurevych
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Static random exemplar selection outperforms similarity-based selection, and adding more exemplars does not enhance performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` A static strategy of fixed random examples outperformed dynamic similarity-based selection setups, especially for Mistral and Qwen. [→ Sukannya Purkayastha 2025](#sukannya-purkayastha-2025)

## Evidence

### Sukannya Purkayastha 2025

Sukannya Purkayastha, Zhuang Li, Anne Lauscher, Lizhen Qu, Iryna Gurevych. (2025). LAZY REVIEW: A Dataset for Uncovering Lazy Thinking in NLP Peer Reviews. arXiv. [doi:10.18653/v1/2025.acl-long.165](https://doi.org/10.18653/v1/2025.acl-long.165)

`q2 · i?` · `causal · r2`

RQ2 exemplar-selection comparison testing static random selection against BM25, Top-K embedding similarity, and Vote-K, with 1, 2, and 3 exemplars. Results are reported as comparative performance patterns; no effect size is printed.

> "finding that the static strategy outperforms all other setups, especially for Mistral and Qwen. Increasing exemplars does not enhance performance, support-ing Srivastava et al. (2024) that random examples yield better results than similarity-based methods."

## Discussion


## Related Claims
- [Adding positive (worked) examples to guidelines raises inter-annotator agreement and in-context learning performance](positive-examples-boost-annotation-and-icl.md) — related
- [CPIG's iterative exemplar selection consistently improves the originality of LLM responses to generated CPS items by the last round of item generation](cpig-improves-response-originality-over-iterations.md) — reports the opposite
- [System-controlled adaptive instruction does not necessarily yield higher transfer than nonadaptive static approaches](system-control-not-superior-transfer.md) — a broader claim this one bears on

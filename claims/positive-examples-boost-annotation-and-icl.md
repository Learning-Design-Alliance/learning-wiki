---
type: claim
title: Adding positive (worked) examples to guidelines raises inter-annotator agreement and in-context learning performance
description: Adding positive (worked) examples to guidelines raises inter-annotator agreement and in-context learning performance
id: positive-examples-boost-annotation-and-icl
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: sukannya-purkayastha-2025
    resource: "https://doi.org/10.18653/v1/2025.acl-long.165"
    title: "Sukannya Purkayastha, Zhuang Li, Anne Lauscher, Lizhen Qu, Iryna Gurevych. (2025). LAZY REVIEW: A Dataset for Uncovering Lazy Thinking in NLP Peer Reviews. arXiv. [doi:10.18653/v1/2025.acl-long.165](https://doi.org/10.18653/v1/2025.acl-long.165)"
    author: Sukannya Purkayastha, Zhuang Li, Anne Lauscher, Lizhen Qu, Iryna Gurevych
    q: 2
    i: "?"
    kind: design
    rigour: 3
  - id: sukannya-purkayastha-2025-2
    resource: "https://doi.org/10.18653/v1/2025.acl-long.165"
    title: "Sukannya Purkayastha, Zhuang Li, Anne Lauscher, Lizhen Qu, Iryna Gurevych. (2025). LAZY REVIEW: A Dataset for Uncovering Lazy Thinking in NLP Peer Reviews. arXiv. [doi:10.18653/v1/2025.acl-long.165](https://doi.org/10.18653/v1/2025.acl-long.165)"
    author: Sukannya Purkayastha, Zhuang Li, Anne Lauscher, Lizhen Qu, Iryna Gurevych
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Adding positive (worked) examples to guidelines raises inter-annotator agreement and in-context learning performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Incorporating positive examples for each lazy thinking class in round 3 raised Cohen's κ to 0.52, up from 0.31 and 0.38 in earlier rounds. [→ Sukannya Purkayastha 2025](#sukannya-purkayastha-2025)
`q2 i?` In-context learning with positive examples surpasses zero-shot models, with coarse-grained gains of 20 points for Gemma and 21 points for SciTülu in string-based accuracy. [→ Sukannya Purkayastha 2025 (2)](#sukannya-purkayastha-2025-2)

## Evidence

### Sukannya Purkayastha 2025

Sukannya Purkayastha, Zhuang Li, Anne Lauscher, Lizhen Qu, Iryna Gurevych. (2025). LAZY REVIEW: A Dataset for Uncovering Lazy Thinking in NLP Peer Reviews. arXiv. [doi:10.18653/v1/2025.acl-long.165](https://doi.org/10.18653/v1/2025.acl-long.165)

`q2 · i?` · `design · r3`

Annotation study round 3, in which the authors fixed the guidelines and added positive examples per class, motivated by "worked examples" research. Agreement rose across rounds (κ 0.31, 0.38, 0.52); no standardized effect size is printed.

> "For round 3, we sampled 50 new review segments and included annotated examples from the previous round, resulting in a Cohen’s κ of 0.52, indicating substantial agreement despite the task’s subjectivity"

### Sukannya Purkayastha 2025 (2)

Sukannya Purkayastha, Zhuang Li, Anne Lauscher, Lizhen Qu, Iryna Gurevych. (2025). LAZY REVIEW: A Dataset for Uncovering Lazy Thinking in NLP Peer Reviews. arXiv. [doi:10.18653/v1/2025.acl-long.165](https://doi.org/10.18653/v1/2025.acl-long.165)

`q2 · i?` · `causal · r1`

RQ2 in-context learning experiment on the same 50 instances as annotation round 3, testing static and dynamic exemplar selection with 1-3 exemplars. Gains are reported as accuracy points; no standardized effect size is printed.

> "ICL-based methods surpass zero-shot mod-els, with notable gains in coarse classification (20 points for Gemma, 21 points for SciTülu string-based accuracy (S.A.)). We also obtain positive increments across the board in fine-grained clas-sifications."

## Discussion


## Related Claims
- Reviews rewritten with lazy thinking annotations outperform original reviews on constructiveness, justification, and adherence — related
- Zero-shot LLMs struggle to identify lazy thinking classes, and target-segment-only input generally outperforms review-plus-target input — related
- Instruction-based fine-tuning on LAZY REVIEW significantly improves LLM lazy-thinking detection over zero-shot and few-shot baselines — related
- [Static random exemplar selection outperforms similarity-based selection, and adding more exemplars does not enhance performance](static-random-exemplars-beat-similarity-selection.md) — related

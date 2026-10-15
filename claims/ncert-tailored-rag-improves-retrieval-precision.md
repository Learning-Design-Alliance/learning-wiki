---
type: claim
title: "NCERT-tailored RAG preprocessing and figure-aware indexing improve retrieval precision over a generic-chunking baseline, per the authors' assertion"
description: "NCERT-tailored RAG preprocessing and figure-aware indexing improve retrieval precision over a generic-chunking baseline, per the authors' assertion"
id: ncert-tailored-rag-improves-retrieval-precision
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: siddhanth-sridhar-2026
    resource: "https://doi.org/10.48550/arxiv.2609.14408"
    title: "Siddhanth Sridhar, Shreya Chaurasia, Baddela Sai Yaswantha Reddy, Deepak Parmar, and Dr. Shylaja S S. (2026). Dynamic Learning Solutions: A System for Personalized Educational Video Generation. arXiv preprint. https://arxiv.org/abs/2609.14408 [doi:10.48550/arxiv.2609.14408](https://doi.org/10.48550/arxiv.2609.14408)"
    author: Siddhanth Sridhar, Shreya Chaurasia, Baddela Sai Yaswantha Reddy, Deepak Parmar, and Dr. Shylaja S S.
    q: 1
    i: "?"
    kind: design
    rigour: 1
---

# NCERT-tailored RAG preprocessing and figure-aware indexing improve retrieval precision over a generic-chunking baseline, per the authors' assertion

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r1` · `q1`

## Subclaims
`q1 i?` The authors assert that targeted text cleaning plus figure-aware document extraction improves retrieval precision and contextual grounding compared to a baseline RAG pipeline using generic text chunking and embedding. [→ Siddhanth Sridhar 2026](#siddhanth-sridhar-2026)

## Evidence

### Siddhanth Sridhar 2026

Siddhanth Sridhar, Shreya Chaurasia, Baddela Sai Yaswantha Reddy, Deepak Parmar, and Dr. Shylaja S S. (2026). Dynamic Learning Solutions: A System for Personalized Educational Video Generation. arXiv preprint. https://arxiv.org/abs/2609.14408 [doi:10.48550/arxiv.2609.14408](https://doi.org/10.48550/arxiv.2609.14408)

`q1 · i?` · `design · r1`

The authors' design assertion in the methodology section describing their NCERT-optimized RAG pipeline; no retrieval evaluation, metric, or test is printed. The claimed gain is "retrieval precision and contextual grounding" versus a generic-chunking baseline.

> "This optimization improves retrieval precision and contextual grounding for educational queries compared to a baseline RAG pipeline that only relies on generic text chunking and embedding."

## Discussion


## Related Claims
- [Retrieval context has a sweet spot at Top-K = 10: raising it to 15 did not improve recall but significantly worsened context precision via the distraction issue](rag-top-k-10-sweet-spot-context-precision.md) — related
- [Optimal RAG configuration differs by discipline: STEM subjects perform best with 512-character chunks and temperature 0.3 (faithfulness 0.97), while humanities require 1000-character chunks and temperature 0.1 (context recall 1.00, faithfulness 0.98)](rag-configuration-discipline-dependent-moodle-tutor.md) — related
- [Pipeline components play complementary roles: hierarchical generation has the largest effect, grounding improves specificity and factual accuracy, and cluster-informed TOC planning improves structure and audience fit](pipeline-components-complementary-ablation.md) — related

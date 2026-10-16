---
type: claim
title: The software-product reporting gap persists within each review stage, and reported precision and recall vary widely across approaches
description: The software-product reporting gap persists within each review stage, and reported precision and recall vary widely across approaches
id: software-reporting-gap-persists-across-review-stages
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: zabaleta-2026
    resource: "https://doi.org/10.48550/arxiv.2609.11559"
    title: "Zabaleta, M. & Lin, B. (2026). PRISMA-LLM: An Empirical Reporting Framework for AI-Assisted Systematic Reviews. https://arxiv.org/abs/2609.11559 [doi:10.48550/arxiv.2609.11559](https://doi.org/10.48550/arxiv.2609.11559)"
    author: "Zabaleta, M. & Lin, B."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: zabaleta-2026-2
    resource: "https://doi.org/10.48550/arxiv.2609.11559"
    title: "Zabaleta, M. & Lin, B. (2026). PRISMA-LLM: An Empirical Reporting Framework for AI-Assisted Systematic Reviews. https://arxiv.org/abs/2609.11559. [doi:10.48550/arxiv.2609.11559](https://doi.org/10.48550/arxiv.2609.11559)"
    author: "Zabaleta, M. & Lin, B."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# The software-product reporting gap persists within each review stage, and reported precision and recall vary widely across approaches

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`

## Subclaims
`q2 i?` Within each review-stage group since 2023, software/product papers report fewer evaluation items and higher no-evaluation rates; the gap is largest in screening and selection. [→ Zabaleta 2026](#zabaleta-2026)
`q2 i?` Reported precision and recall for screening and extraction are heterogeneous, with medians such as 0.884 recall for LLMs in screening but wide individual-paper dispersion. [→ Zabaleta 2026 (2)](#zabaleta-2026-2)

## Evidence

### Zabaleta 2026

Zabaleta, M. & Lin, B. (2026). PRISMA-LLM: An Empirical Reporting Framework for AI-Assisted Systematic Reviews. https://arxiv.org/abs/2609.11559 [doi:10.48550/arxiv.2609.11559](https://doi.org/10.48550/arxiv.2609.11559)

`q2 · i?` · `associational · r2`

Supplementary stage-stratified analysis (Supplementary Figure S4) of papers from 2023 onward; the authors state the stratified comparisons preserve the software-reporting gap, so the aggregate difference is not explained solely by review-stage composition.

> "The difference is largest in screening and selection: software/product papers average 3.2 evaluation items and 39.3% report no evaluation, whereas LLM papers average 7.3 items with a 3.8% no-evaluation rate."

### Zabaleta 2026 (2)

Zabaleta, M. & Lin, B. (2026). PRISMA-LLM: An Empirical Reporting Framework for AI-Assisted Systematic Reviews. https://arxiv.org/abs/2609.11559. [doi:10.48550/arxiv.2609.11559](https://doi.org/10.48550/arxiv.2609.11559)

`q2 · i?` · `associational · r2`

Exploratory inventory of parsed performance-versus-human quotations (Supplementary Figure S5 and Table S3), restricted to papers reporting both precision and recall; individual paper values span much wider ranges than group medians, across heterogeneous datasets, tasks, thresholds, and evaluation designs.

> "For screening and selection, median recall is 0.821 for custom ML, deep-learning, BERT, or rule-based methods, 0.884 for LLMs, and 0.851 for software/products; median precision is 0.742, 0.695, and 0.667, respectively."

## Discussion


## Related Claims
- Review automation has shifted toward LLM- and software-facing workflows and into review stages that can alter the evidence base — related
- [Since 2023, software/product papers report markedly less evaluation detail than LLM papers in review automation](software-product-papers-report-less-evaluation-than-llm-papers.md) — related
- Reporting coverage increases with LLM workflow complexity, from prompt-only to engineered and retrieval/adapted/agentic methods — related

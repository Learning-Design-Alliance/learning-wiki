---
type: claim
title: BM25-based recipe similarity computation runs in real time, averaging 0.8 seconds (sigma 0.1) in the worst case of 100,000 comparisons.
description: BM25-based recipe similarity computation runs in real time, averaging 0.8 seconds (sigma 0.1) in the worst case of 100,000 comparisons.
id: relex-bm25-real-time-similarity
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: weak
newest_evidence: 2025
sources:
  - id: mejia-domenzain-2025
    resource: "https://doi.org/10.1007/s40593-024-00405-1"
    title: "Mejia-Domenzain, P., Frej, J., Neshaei, S. P., Mouchel, L., Nazaretsky, T., Wambsganss, T., Bosselut, A., & Käser, T. (2025). Enhancing Procedural Writing Through Personalized Example Retrieval: A Case Study on Cooking Recipes. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-024-00405-1"
    author: "Mejia-Domenzain, P., Frej, J., Neshaei, S. P., Mouchel, L., Nazaretsky, T., Wambsganss, T., Bosselut, A., & Käser, T."
    q: 2
    i: "?"
    kind: causal
    rigour: "?"
---

# BM25-based recipe similarity computation runs in real time, averaging 0.8 seconds (sigma 0.1) in the worst case of 100,000 comparisons.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r?` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person
> **Design limits** · Mejia-Domenzain 2025: no comparison group (read from the study by two models, 2026-10-27)

## Subclaims
`q2 i?` Similarity computation over 100 random recipes in the worst-case scenario averaged 0.8 seconds (sigma = 0.1 seconds) on a laptop with an Apple M1 processor. [→ Mejia-Domenzain 2025](#mejia-domenzain-2025)

## Evidence

### Mejia-Domenzain 2025

Mejia-Domenzain, P., Frej, J., Neshaei, S. P., Mouchel, L., Nazaretsky, T., Wambsganss, T., Bosselut, A., & Käser, T. (2025). Enhancing Procedural Writing Through Personalized Example Retrieval: A Case Study on Cooking Recipes. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-024-00405-1

`q2 · i?` · `causal · r?`

Numerical timing evaluation of the BM25 Bag-of-Words similarity step, run on 100 random recipes under the worst-case filtered candidate set. As printed, computation time "was on average 0.8 seconds (σ = 0.1 seconds)". No effect size is printed.

> "we evaluated the similarity computation time for 100 random recipes in the worst-case scenario (with 100 , 000 comparisons) and we found that the computation time was on average 0.8 seconds (σ = 0.1 seconds) on a laptop with an Apple M1 processor."

## Discussion


## Related Claims
- [A complete four-skill open-model stack fits under 4 GB, runs at reading pace on the cheapest hardware by community measurements, and costs about one US cent of electricity per study hour](llmersion-feasibility-stack-pace-cost.md) — related

---
type: claim
title: Multi-label intercoder agreement measured by Jaccard similarity reached a mean pairwise 0.52 at item level, with agreement rising at coarser granularity
description: Multi-label intercoder agreement measured by Jaccard similarity reached a mean pairwise 0.52 at item level, with agreement rising at coarser granularity
id: jaccard-agreement-multilabel-codebook-052
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: liu-2026
    resource: "https://osf.io/ju59q/overview?view_only=96afb71945044b8794e113f9763cc74a"
    title: "Liu, A., Sun, M., Esbenshade, L., Xiao, M., Tian, V., Zhang, Z., & He, K. (2026). Human-LLM Collaborative Inductive Coding for Conceptualizing K-12 Educator AI Use. https://osf.io/ju59q/overview?view_only=96afb71945044b8794e113f9763cc74a"
    author: "Liu, A., Sun, M., Esbenshade, L., Xiao, M., Tian, V., Zhang, Z., & He, K."
    q: 2
    i: "?"
    kind: design
    rigour: 3
---

# Multi-label intercoder agreement measured by Jaccard similarity reached a mean pairwise 0.52 at item level, with agreement rising at coarser granularity

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q2`

## Subclaims
`q2 i?` Pairwise Jaccard similarity across three coders on a 289-message overlap set averaged 0.52 at the item level, ranging from 0.46 to 0.55 depending on granularity, with disagreement concentrated at boundaries between semantically adjacent categories. [→ Liu 2026](#liu-2026)

## Evidence

### Liu 2026

Liu, A., Sun, M., Esbenshade, L., Xiao, M., Tian, V., Zhang, Z., & He, K. (2026). Human-LLM Collaborative Inductive Coding for Conceptualizing K-12 Educator AI Use. https://osf.io/ju59q/overview?view_only=96afb71945044b8794e113f9763cc74a

`q2 · i?` · `design · r3`

Calibration analysis of three coders' multi-label coding of a 289-message hold-out set. The article reports "Mean pairwise Jaccard similarity was 0.52 at the codebook item level", with higher agreement at coarser category and domain levels.

> "Mean pairwise Jaccard similarity was 0.52 at the codebook item level, ranging from 0.46 to 0.55 depending on the granularity at which agreement is assessed"

## Discussion


## Related Claims
- [A three-phase human-LLM inductive pipeline produced a hierarchical codebook of 72 items within 19 categories and six domains from 45,000 educator-AI messages](human-llm-pipeline-72-item-educator-ai-codebook.md) — related
- [Human-LLM agreement on a complex multi-label codebook falls well below human-human agreement, while LLM-LLM agreement is comparable to human-human agreement](human-llm-agreement-gap-jaccard.md) — related
- [Human-LLM agreement is moderated by code properties, multi-model consensus, and model-reported confidence](agreement-moderators-tiers-consensus-confidence.md) — related

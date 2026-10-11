---
type: claim
title: Vibe-coded websites built for 73 distinct businesses converge into roughly a dozen recurring visual designs despite an explicit originality incentive
description: Vibe-coded websites built for 73 distinct businesses converge into roughly a dozen recurring visual designs despite an explicit originality incentive
id: vibe-coding-cohort-visual-concentration
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: léonard-boussioux-2026
    resource: "https://arxiv.org/abs/2609.38183"
    title: "Léonard Boussioux*, Ziyi Zhao*, and Kanghyun Cho*. (2026). One Tool, One Taste? How Vibe Coding Trades Collective Diversity for Individual Creativity. arXiv. https://arxiv.org/abs/2609.38183"
    author: "Léonard Boussioux*, Ziyi Zhao*, and Kanghyun Cho*"
    q: 2
    i: "?"
  - id: léonard-boussioux-2026-2
    resource: "https://arxiv.org/abs/2609.38183"
    title: "Léonard Boussioux*, Ziyi Zhao*, and Kanghyun Cho*. (2026). One Tool, One Taste? How Vibe Coding Trades Collective Diversity for Individual Creativity. arXiv. https://arxiv.org/abs/2609.38183"
    author: "Léonard Boussioux*, Ziyi Zhao*, and Kanghyun Cho*"
    q: 2
    i: "?"
---

# Vibe-coded websites built for 73 distinct businesses converge into roughly a dozen recurring visual designs despite an explicit originality incentive

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · `q2` quasi-experiment

## Subclaims
`q2 i?` Unsupervised clustering of DINOv3 embeddings recovers six visual archetypes absorbing 64 of 73 sites (88%), and effective-diversity indices put the number of distinct designs at roughly six to twelve. [→ Léonard Boussioux* 2026](#leonard-boussioux-2026)
`q2 i?` Median nearest-neighbor visual similarity (49 index points) is far higher than mean pairwise similarity (22.8), showing local concentration among look-alike sites. [→ Léonard Boussioux* 2026 (2)](#leonard-boussioux-2026-2)

## Evidence

### Léonard Boussioux* 2026

Léonard Boussioux*, Ziyi Zhao*, and Kanghyun Cho*. (2026). One Tool, One Taste? How Vibe Coding Trades Collective Diversity for Individual Creativity. arXiv. https://arxiv.org/abs/2609.38183

`q2 · i?`

Artifact-layer analysis of 73 full-page homepage screenshots embedded with DINOv3, clustered via UMAP–HDBSCAN. The article reports "six visual archetypes, which absorb 64 of 73 sites (88%)"; across 60 sensitivity configurations the cluster count ranges from 3 to 12, so the partition is used descriptively.

> "Density clustering of the embedding space recovers six visual archetypes, which absorb 64 of 73 sites (88%; Figure 5)."

### Léonard Boussioux* 2026 (2)

Léonard Boussioux*, Ziyi Zhao*, and Kanghyun Cho*. (2026). One Tool, One Taste? How Vibe Coding Trades Collective Diversity for Individual Creativity. arXiv. https://arxiv.org/abs/2609.38183

`q2 · i?`

Pairwise cosine-similarity analysis of all 2,628 pairs among the 73 embedded homepages. The article reports the median nearest-neighbor score of "49 index points, compared with 22.8 for the average pair", and 14 of 73 sites (19%) have a nearest-neighbor score above 70.

> "Each site’s closest neighbor among the other 72 has a median score of 49 index points, compared with 22.8 for the average pair (Figure 4)."

## Discussion


## Related Claims
- [Builders' perceived control, satisfaction, and perceived quality show no detectable association with their measured visual atypicality, so convergence goes unnoticed from the inside](perception-uncorrelated-with-measured-originality.md) — related
- [Business sector only weakly explains which visual archetype a vibe-coded site receives, and sector is not significantly associated with per-site originality](sector-weakly-explains-archetype-assignment.md) — related
- [Chat-driven vibe-coding builders converge on a single generate-and-check script whose dominant time cost is dead waiting for the tool](shared-generate-and-check-loop-script.md) — related

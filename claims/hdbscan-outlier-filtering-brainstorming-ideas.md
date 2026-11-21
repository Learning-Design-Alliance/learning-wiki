---
type: claim
title: HDBSCAN labels contextually unrelated brainstorming ideas as outliers, which are excluded before topic extraction
description: HDBSCAN labels contextually unrelated brainstorming ideas as outliers, which are excluded before topic extraction
id: hdbscan-outlier-filtering-brainstorming-ideas
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: melkamu-abay-mersha-2025
    resource: "https://doi.org/10.48550/arXiv.2509.16835"
    title: "Melkamu Abay Mersha, Jugal Kalita. (2025). Semantic-Driven Topic Modeling for Analyzing Creativity in Virtual Brainstorming. arXiv preprint. [doi:10.48550/arXiv.2509.16835](https://doi.org/10.48550/arXiv.2509.16835)"
    author: Melkamu Abay Mersha, Jugal Kalita
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# HDBSCAN labels contextually unrelated brainstorming ideas as outliers, which are excluded before topic extraction

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Outlier ideas/sentences lacking strong relationships with other ideas are labeled -1 and excluded from the topic modeling process. [→ Melkamu Abay Mersha 2025](#melkamu-abay-mersha-2025)

## Evidence

### Melkamu Abay Mersha 2025

Melkamu Abay Mersha, Jugal Kalita. (2025). Semantic-Driven Topic Modeling for Analyzing Creativity in Virtual Brainstorming. arXiv preprint. [doi:10.48550/arXiv.2509.16835](https://doi.org/10.48550/arXiv.2509.16835)

`q2 · i?` · `design · r2`

Processing step reported in the clustering section (Figures 3 and 4): HDBSCAN grouped reduced embeddings into clusters based on semantic similarity and labeled low-density points as outliers or noises (denoted by -1), which were then excluded while distinct clusters were preserved.

> "We do not include these outlier sentences/ideas in our topic modeling process because they exhibit weaker relationships among themselves and with other distinct clusters."

## Discussion


## Related Claims
- [Cluster-based topic extraction with refinement yields ten interpretable topics with an overall coherence of 0.617 from one program run](cluster-topic-extraction-ten-topics-coherence-0617.md) — related
- [The proposed semantic-driven topic model achieves higher topic coherence than LDA, ETM, and BERTopic on Zoom brainstorming transcripts](sbert-umap-hdbscan-model-higher-coherence-than-baselines.md) — related

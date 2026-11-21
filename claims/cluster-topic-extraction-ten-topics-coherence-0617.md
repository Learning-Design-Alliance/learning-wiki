---
type: claim
title: Cluster-based topic extraction with refinement yields ten interpretable topics with an overall coherence of 0.617 from one program run
description: Cluster-based topic extraction with refinement yields ten interpretable topics with an overall coherence of 0.617 from one program run
id: cluster-topic-extraction-ten-topics-coherence-0617
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
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

# Cluster-based topic extraction with refinement yields ten interpretable topics with an overall coherence of 0.617 from one program run

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Topic extraction from HDBSCAN clusters produced ten general topics categorizing all generated ideas, with an overall topic coherence of 0.617 (Table 1). [→ Melkamu Abay Mersha 2025](#melkamu-abay-mersha-2025)

## Evidence

### Melkamu Abay Mersha 2025

Melkamu Abay Mersha, Jugal Kalita. (2025). Semantic-Driven Topic Modeling for Analyzing Creativity in Virtual Brainstorming. arXiv preprint. [doi:10.48550/arXiv.2509.16835](https://doi.org/10.48550/arXiv.2509.16835)

`q2 · i?` · `design · r2`

Topic extraction results for Dataset1 presented in Table 1, where each cluster's top-k words were ranked by average cosine similarity; Table 1 prints an "Overall Topic Coherence 0.617" as the average of individual topic scores from a single program run.

> "Hence, we can extract the most significant insights from the meeting using these topics. In this case, we can identify the top 10 general topics in the meeting session, which categorize all the generated ideas."

## Discussion


## Related Claims
- [The proposed semantic-driven topic model achieves higher topic coherence than LDA, ETM, and BERTopic on Zoom brainstorming transcripts](sbert-umap-hdbscan-model-higher-coherence-than-baselines.md) — related
- [BERTopic clustering of medical documents produced highly distinct topics rated highly by medical experts](bertopic-clustering-high-quality-topics.md) — related
- [HDBSCAN labels contextually unrelated brainstorming ideas as outliers, which are excluded before topic extraction](hdbscan-outlier-filtering-brainstorming-ideas.md) — related

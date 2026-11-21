---
type: claim
title: The proposed semantic-driven topic model achieves higher topic coherence than LDA, ETM, and BERTopic on Zoom brainstorming transcripts
description: The proposed semantic-driven topic model achieves higher topic coherence than LDA, ETM, and BERTopic on Zoom brainstorming transcripts
id: sbert-umap-hdbscan-model-higher-coherence-than-baselines
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

# The proposed semantic-driven topic model achieves higher topic coherence than LDA, ETM, and BERTopic on Zoom brainstorming transcripts

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On Dataset1, the proposed model scored 0.687 TC(C_V) and 0.264 TC(C_npmi), exceeding LDA (0.462/0.066), ETM (0.544/0.094), and BERTopic (0.552/0.192). [→ Melkamu Abay Mersha 2025](#melkamu-abay-mersha-2025)

## Evidence

### Melkamu Abay Mersha 2025

Melkamu Abay Mersha, Jugal Kalita. (2025). Semantic-Driven Topic Modeling for Analyzing Creativity in Virtual Brainstorming. arXiv preprint. [doi:10.48550/arXiv.2509.16835](https://doi.org/10.48550/arXiv.2509.16835)

`q2 · i?` · `design · r2`

Model comparison on Dataset1 of Zoom brainstorming transcripts, with topic coherence computed for each model varying the number of topics from 2 to 10 and averaging outputs from three separate runs per interval. The table prints "Our Model 0.687 0.264" against the three baselines.

> "Model Comparison Results for Dataset1 Models TC(C_V) TC(C_npmi) LDA 0.462 0.066 ETM 0.544 0.094 BERTopic 0.552 0.192 Our Model 0.687 0.264"

## Discussion


## Related Claims
- [Cluster-based topic extraction with refinement yields ten interpretable topics with an overall coherence of 0.617 from one program run](cluster-topic-extraction-ten-topics-coherence-0617.md) — related
- [HDBSCAN labels contextually unrelated brainstorming ideas as outliers, which are excluded before topic extraction](hdbscan-outlier-filtering-brainstorming-ideas.md) — related
- [BERTopic analysis of 1,048 AIOL publications identifies research themes including adaptive learning systems, sentiment analysis, and predictive analytics](bertopic-aiol-major-research-themes.md) — related
- [BERTopic clustering of medical documents produced highly distinct topics rated highly by medical experts](bertopic-clustering-high-quality-topics.md) — related

---
type: claim
title: Clusters computed from pre-trained LLM embeddings show low overall alignment with theory-driven Knowledge Profiles of student biology responses
description: Clusters computed from pre-trained LLM embeddings show low overall alignment with theory-driven Knowledge Profiles of student biology responses
id: llm-embedding-clusters-low-alignment-kps
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: abigail-gurin-schleifer-2025
    resource: "https://doi.org/10.1007/s40593-025-00485-7"
    title: "Abigail Gurin Schleifer, Beata Beigman Klebanov, Giora Alexandron. (2025). Uncovering Measurement Biases in LLM Embedding Spaces: The Anna Karenina Principle and Its Implications for Automated Feedback. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-025-00485-7"
    author: Abigail Gurin Schleifer, Beata Beigman Klebanov, Giora Alexandron
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# Clusters computed from pre-trained LLM embeddings show low overall alignment with theory-driven Knowledge Profiles of student biology responses

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i?` Across all six combinations of three embedding models and two clustering algorithms, the Adjusted Rand Index between embeddings-based clusters and expert-defined KPs was low, with the best combination (KMeans on AlephBERT) reaching only .122 (Q1) and .191 (Q2). [→ Abigail Gurin Schleifer 2025](#abigail-gurin-schleifer-2025)

## Evidence

### Abigail Gurin Schleifer 2025

Abigail Gurin Schleifer, Beata Beigman Klebanov, Giora Alexandron. (2025). Uncovering Measurement Biases in LLM Embedding Spaces: The Anna Karenina Principle and Its Implications for Automated Feedback. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-025-00485-7

`q3 · i?` · `design · r2`

Cluster-analysis study comparing bottom-up clusters from three LLM embedding models (AlephBERT, OpenAI text-embedding-3-large, Llama3.1-8B) with two algorithms (KMeans, HDBSCAN) against gold KPs for two biology items. "the ARI is low: .122 (Q1) and .191 (Q2)" for the best configuration; other combinations showed negligible agreement.

> "However, even with the best combination – KMeans on AlephBERT embeddings, the ARI is low: .122 (Q1) and .191 (Q2). The rest of the models and clustering algorithm combinations show negligible agreement with the KPs."

## Discussion


## Related Claims
- [The Anna Karenina effect: the lower the quality of a Knowledge Profile, the less similar its responses are to each other in LLM embedding space](anna-karenina-within-kp-similarity-decreases.md) — related
- [A discoverability bias favors correct responses: the highest-quality KP is retrieved far better than all other KPs across embedding models and clustering algorithms](discoverability-bias-favors-correct-responses.md) — related
- [LLMs show discoverability bias: they accurately identify only high-quality open-ended biology responses and miss nuanced misconceptions](llm-discoverability-bias-open-ended-biology-assessment.md) — related
- [A small monolingual embedding model (AlephBERT) outperformed larger multilingual models on KP retrieval in both ARI and per-KP F1 analyses](monolingual-small-model-outperforms-multilingual-kp-retrieval.md) — a broader claim this one bears on

---
type: claim
title: A small monolingual embedding model (AlephBERT) outperformed larger multilingual models on KP retrieval in both ARI and per-KP F1 analyses
description: A small monolingual embedding model (AlephBERT) outperformed larger multilingual models on KP retrieval in both ARI and per-KP F1 analyses
id: monolingual-small-model-outperforms-multilingual-kp-retrieval
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: abigail-gurin-schleifer-2025
    resource: "https://doi.org/10.1007/s40593-025-00485-7"
    title: "Abigail Gurin Schleifer, Beata Beigman Klebanov, Giora Alexandron. (2025). Uncovering Measurement Biases in LLM Embedding Spaces: The Anna Karenina Principle and Its Implications for Automated Feedback. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-025-00485-7"
    author: Abigail Gurin Schleifer, Beata Beigman Klebanov, Giora Alexandron
    q: 3
    i: "?"
    kind: associational
    rigour: 2
---

# A small monolingual embedding model (AlephBERT) outperformed larger multilingual models on KP retrieval in both ARI and per-KP F1 analyses

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q3`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q3 i?` The monolingual AlephBERT model (768 dimensions) achieved better clustering agreement and KP retrieval than the much larger multilingual models OpAI-t3l (3072) and Lla3.1-8 (4096). [→ Abigail Gurin Schleifer 2025](#abigail-gurin-schleifer-2025)

## Evidence

### Abigail Gurin Schleifer 2025

Abigail Gurin Schleifer, Beata Beigman Klebanov, Giora Alexandron. (2025). Uncovering Measurement Biases in LLM Embedding Spaces: The Anna Karenina Principle and Its Implications for Automated Feedback. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-025-00485-7

`q3 · i?` · `associational · r2`

Cross-model comparison in the results tables (ARI, Table 2; F1, Table 3) for two biology items. The authors state the multilingual models "perform worse than the monolingual small AlephBERT model ... both in the ARI score and the per-KP F1 score analysis", implying a small expert model may outperform a large general one.

> "The multilingual large models OpAI-t3l and Lla3.1-8 (embedding dimension are 3072, 4096 respectively) use a multilingual tokenizer by OpenAI from the tiktoken library (OpenAI, 2024; Dubey et al., 2024); these perform worse than the monolingual small AlephBERT model (embedding dimension is 768) both in the ARI score and the per-KP F1 score analysis."

## Discussion


## Related Claims
- [The Anna Karenina effect: the lower the quality of a Knowledge Profile, the less similar its responses are to each other in LLM embedding space](anna-karenina-within-kp-similarity-decreases.md) — related
- [A discoverability bias favors correct responses: the highest-quality KP is retrieved far better than all other KPs across embedding models and clustering algorithms](discoverability-bias-favors-correct-responses.md) — related
- [Clusters computed from pre-trained LLM embeddings show low overall alignment with theory-driven Knowledge Profiles of student biology responses](llm-embedding-clusters-low-alignment-kps.md) — a narrower finding that bears on this claim

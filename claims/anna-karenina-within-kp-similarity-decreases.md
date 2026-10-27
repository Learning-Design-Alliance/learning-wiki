---
type: claim
title: "The Anna Karenina effect: the lower the quality of a Knowledge Profile, the less similar its responses are to each other in LLM embedding space"
description: "The Anna Karenina effect: the lower the quality of a Knowledge Profile, the less similar its responses are to each other in LLM embedding space"
id: anna-karenina-within-kp-similarity-decreases
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
sources:
  - id: abigail-gurin-schleifer-2025
    resource: "https://doi.org/10.1007/s40593-025-00485-7"
    title: "Abigail Gurin Schleifer, Beata Beigman Klebanov, Giora Alexandron. (2025). Uncovering Measurement Biases in LLM Embedding Spaces: The Anna Karenina Principle and Its Implications for Automated Feedback. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-025-00485-7"
    author: Abigail Gurin Schleifer, Beata Beigman Klebanov, Giora Alexandron
    q: 3
    i: "?"
    kind: associational
    rigour: 2
  - id: abigail-gurin-schleifer-2025-2
    resource: "https://doi.org/10.1007/s40593-025-00485-7"
    title: "Abigail Gurin Schleifer, Beata Beigman Klebanov, Giora Alexandron. (2025). Uncovering Measurement Biases in LLM Embedding Spaces: The Anna Karenina Principle and Its Implications for Automated Feedback. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-025-00485-7"
    author: Abigail Gurin Schleifer, Beata Beigman Klebanov, Giora Alexandron
    q: 3
    i: "?"
    kind: associational
    rigour: 2
---

# The Anna Karenina effect: the lower the quality of a Knowledge Profile, the less similar its responses are to each other in LLM embedding space

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q3`

## Subclaims
`q3 i?` Within-KP median cosine similarity declines as KP quality decreases, for all three embedding models and both items. [→ Abigail Gurin Schleifer 2025](#abigail-gurin-schleifer-2025)
`q3 i?` Spearman partial correlation controlling for response length between KP index and similarity-to-centroid is medium-to-strong and negative, e.g. ρ = −.482 (AlephBERT, Q1) and −.730 (Llama3.1-8B, Q2). [→ Abigail Gurin Schleifer 2025 (2)](#abigail-gurin-schleifer-2025-2)

## Evidence

### Abigail Gurin Schleifer 2025

Abigail Gurin Schleifer, Beata Beigman Klebanov, Giora Alexandron. (2025). Uncovering Measurement Biases in LLM Embedding Spaces: The Anna Karenina Principle and Its Implications for Automated Feedback. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-025-00485-7

`q3 · i?` · `associational · r2`

Numerical analysis of median pairwise cosine similarities within each KP (Table 4), for responses of 669 high-school biology students. The paper reports a "general downward trend from (Model, 1) to (Model, 6) or (Model, 7)" consistent across all three embedding models and both items, with small aberrations for Lla3.1-8. No effect size is printed for this trend.

> "Second, we observe that as the quality of a response degrades, the similarity to other responses with the same pattern of error decreases: In all cases, the value in the (Model, 6) or (Model, 7) cells, for items Q1 and Q2, respectively, is the smallest value in the row."

### Abigail Gurin Schleifer 2025 (2)

Abigail Gurin Schleifer, Beata Beigman Klebanov, Giora Alexandron. (2025). Uncovering Measurement Biases in LLM Embedding Spaces: The Anna Karenina Principle and Its Implications for Automated Feedback. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-025-00485-7

`q3 · i?` · `associational · r2`

Hypothesis-testing analysis correlating each response's cosine similarity to its KP centroid with KP ordinal index, controlling for word count. Printed partial correlations include ρ = −.482 (AlephBERT Q1), −.296 (OpenAI Q1), −.601 (Llama Q1), −.730 (Llama Q2), described as "a medium-to-strong correlation"; impact left uncoded since no standardized effect size beyond the correlations is printed for the hypothesis test.

> "The Spearman partial correlation coefﬁcient controlling for length and its p-values are presented in Table 5, indicating a medium-to-strong correlation (Xiao et al., 2016) between the quality of a ‘family of responses’ (KP) and the within-family similarity, consistent across the three embedding models."

## Discussion


## Related Claims
- [Clusters computed from pre-trained LLM embeddings show low overall alignment with theory-driven Knowledge Profiles of student biology responses](llm-embedding-clusters-low-alignment-kps.md) — related
- [A discoverability bias favors correct responses: the highest-quality KP is retrieved far better than all other KPs across embedding models and clustering algorithms](discoverability-bias-favors-correct-responses.md) — related
- [A small monolingual embedding model (AlephBERT) outperformed larger multilingual models on KP retrieval in both ARI and per-KP F1 analyses](monolingual-small-model-outperforms-multilingual-kp-retrieval.md) — related
- [LLMs show discoverability bias: they accurately identify only high-quality open-ended biology responses and miss nuanced misconceptions](llm-discoverability-bias-open-ended-biology-assessment.md) — related

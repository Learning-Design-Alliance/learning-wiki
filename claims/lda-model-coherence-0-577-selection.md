---
type: claim
title: The final LDA model for the combined corpus achieved a coherence score of 0.577, selected from 15 averaged models using the elbow method and qualitative inspection.
description: The final LDA model for the combined corpus achieved a coherence score of 0.577, selected from 15 averaged models using the elbow method and qualitative inspection.
id: lda-model-coherence-0-577-selection
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: caramaschi-2025
    resource: "https://doi.org/10.48550/arXiv.2504.02703"
    title: "Caramaschi, M. and Odden, T. O. B. (2025). Uncovering shifts in the history of Physics education: a systematic, NLP-based, thematic analysis of articles from The Physics Teacher and Physics Education journals (1966 - 2019). Originally published 2024. [doi:10.48550/arXiv.2504.02703](https://doi.org/10.48550/arXiv.2504.02703)"
    author: Caramaschi, M. and Odden, T. O. B.
    q: 2
    i: "?"
    kind: qualitative
    rigour: 2
  - id: caramaschi-2025-2
    resource: "https://doi.org/10.48550/arXiv.2504.02703"
    title: "Caramaschi, M. and Odden, T. O. B. (2025). Uncovering shifts in the history of Physics education: a systematic, NLP-based, thematic analysis of articles from The Physics Teacher and Physics Education journals (1966 - 2019). Originally published 2024. [doi:10.48550/arXiv.2504.02703](https://doi.org/10.48550/arXiv.2504.02703)"
    author: Caramaschi, M. and Odden, T. O. B.
    q: 2
    i: "?"
    kind: qualitative
    rigour: 2
---

# The final LDA model for the combined corpus achieved a coherence score of 0.577, selected from 15 averaged models using the elbow method and qualitative inspection.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · qualitative `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Model selection combined coherence scoring, the elbow method, qualitative interpretability checks, and averaging of 15 randomly initialized models. [→ Caramaschi 2025](#caramaschi-2025)
`q2 i?` Twenty topics were chosen as the optimal number after testing configurations in the range of 15 to 22 topics. [→ Caramaschi 2025 (2)](#caramaschi-2025-2)

## Evidence

### Caramaschi 2025

Caramaschi, M. and Odden, T. O. B. (2025). Uncovering shifts in the history of Physics education: a systematic, NLP-based, thematic analysis of articles from The Physics Teacher and Physics Education journals (1966 - 2019). Originally published 2024. [doi:10.48550/arXiv.2504.02703](https://doi.org/10.48550/arXiv.2504.02703)

`q2 · i?` · `qualitative · r2`

Robustness testing of the LDA model: following prior PER work, the authors generated 15 models and used a clustering algorithm to average them, selecting the model closest to the average. The selected model's "coherence score of 0.577" exceeded the 0.572 average.

> "The final model for the combined PE-TPT analysis achieved a coherence score of 0.577, slightly above the overall average (0.572), which provided additional confidence in its reliability."

### Caramaschi 2025 (2)

Caramaschi, M. and Odden, T. O. B. (2025). Uncovering shifts in the history of Physics education: a systematic, NLP-based, thematic analysis of articles from The Physics Teacher and Physics Education journals (1966 - 2019). Originally published 2024. [doi:10.48550/arXiv.2504.02703](https://doi.org/10.48550/arXiv.2504.02703)

`q2 · i?` · `qualitative · r2`

Topic-number tuning: the authors tested topic numbers from 15 to 22, reasoning that each journal independently revealed at least 15 topics, then combined the elbow method with qualitative inspection to fix the count at 20.

> "The final selection of 20 topics was made by considering both the elbow method (to compute the best coherence score range) and qualitative inspection (to ensure the interpretability of topics)."

## Discussion


## Related Claims
- [LDA topic modeling of HI/HIM AI policy documents identifies four dominant themes: academic integrity, generative AI use, AI in research, and ChatGPT engagement](lda-four-themes-hi-him-ai-policies.md) — related
- [LDA topic modelling of 6,087 written student feedback responses yields six SET-related topics](lda-six-topics-from-student-feedback.md) — related
- [Random-initialization instability in LDA was addressed by clustering topics across 500 runs and selecting the most central model](clustering-aggregation-stabilizes-lda.md) — related

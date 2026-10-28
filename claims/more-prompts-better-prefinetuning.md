---
type: claim
title: Pre-finetuning performance increases with the number of distinct prompts used, holding total pre-finetuning answers fixed
description: Pre-finetuning performance increases with the number of distinct prompts used, holding total pre-finetuning answers fixed
id: more-prompts-better-prefinetuning
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: funayama-2025
    resource: "https://doi.org/10.1007/s40593-025-00474-w"
    title: "Funayama, H., Matsubayashi, Y., Asazuma, Y., Mizumoto, T., & Inui, K. (2025). Cross-prompt Pre-finetuning of Language Models for Short Answer Scoring. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-025-00474-w"
    author: "Funayama, H., Matsubayashi, Y., Asazuma, Y., Mizumoto, T., & Inui, K."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Pre-finetuning performance increases with the number of distinct prompts used, holding total pre-finetuning answers fixed

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` With total pre-finetuning answers fixed at 1,600, model performance increased as the number of prompts (1 to 64) increased. [→ Funayama 2025](#funayama-2025)

## Evidence

### Funayama 2025

Funayama, H., Matsubayashi, Y., Asazuma, Y., Mizumoto, T., & Inui, K. (2025). Cross-prompt Pre-finetuning of Language Models for Short Answer Scoring. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-025-00474-w

`q2 · i?` · `causal · r2`

BERT experiment (Fig. 7) varying the number of pre-finetuning prompts (1, 2, 4, 8, 16, 32, 64) with total answers fixed at 1,600 and 50 finetuning instances. The article reports large SDs when few prompts were used, attributed to differences in sampled prompts.

> "The performance of the model increased as the number of prompts used for preﬁnetuning increased, indicating that the more diverse the answer and key phrases pairs are, the better the model understands their relationships."

## Discussion


## Related Claims
- [Cross-prompt finetuning of a pre-finetuned 8B LLM on 50 instances per prompt achieves average QWK of 0.85, comparable to professional human graders (0.87)](cross-prompt-finetuning-8b-human-level.md) — related
- [Two-phase cross-prompt pre-finetuning with key phrases significantly improves short answer scoring accuracy when in-prompt training data is limited](cross-prompt-prefinetuning-key-phrases-low-resource-gain.md) — related
- [LLMs cannot effectively perform in-context learning for short answer scoring, but cross-prompt pre-finetuning substantially boosts their zero-shot performance](llm-icl-insufficient-prefinetuning-boosts-zero-shot.md) — related
- [Cross-prompt pre-finetuning shows no significant benefit when sufficient (200-answer) in-prompt training data is available](prefinetuning-no-benefit-sufficient-data.md) — related
- [Pre-finetuning without key phrases does not improve scoring performance and slightly lowers it relative to the BERT baseline](prefinetuning-without-key-phrases-no-gain.md) — related

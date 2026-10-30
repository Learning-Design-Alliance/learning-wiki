---
type: claim
title: Cross-prompt finetuning of a pre-finetuned 8B LLM on 50 instances per prompt achieves average QWK of 0.85, comparable to professional human graders (0.87)
description: Cross-prompt finetuning of a pre-finetuned 8B LLM on 50 instances per prompt achieves average QWK of 0.85, comparable to professional human graders (0.87)
id: cross-prompt-finetuning-8b-human-level
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
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

# Cross-prompt finetuning of a pre-finetuned 8B LLM on 50 instances per prompt achieves average QWK of 0.85, comparable to professional human graders (0.87)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` With only 50 instances per prompt, cross-prompt finetuning matched or improved performance on 18 of 21 prompts and averaged 0.85 QWK versus human agreement of 0.87. [→ Funayama 2025](#funayama-2025)

## Evidence

### Funayama 2025

Funayama, H., Matsubayashi, Y., Asazuma, Y., Mizumoto, T., & Inui, K. (2025). Cross-prompt Pre-finetuning of Language Models for Short Answer Scoring. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-025-00474-w

`q2 · i?` · `causal · r2`

Figure 6 experiment comparing cross-prompt finetuning (combined data from 21 target prompts) versus per-prompt finetuning of the pre-finetuned 8B model. The article reports the cross-prompt setting's average QWK of 0.85 against human inter-grader agreement of 0.87.

> "For 18 out of the 21 prompts, the model performance was either the same or improved. Even though the cross-prompt ﬁnetuned model was trained on only 50 instances per prompt, it exhibited an average QWK of 0.85, which is comparable to that of professional human graders (0.87)."

## Discussion


## Related Claims
- [LLMs cannot effectively perform in-context learning for short answer scoring, but cross-prompt pre-finetuning substantially boosts their zero-shot performance](llm-icl-insufficient-prefinetuning-boosts-zero-shot.md) — related
- [Two-phase cross-prompt pre-finetuning with key phrases significantly improves short answer scoring accuracy when in-prompt training data is limited](cross-prompt-prefinetuning-key-phrases-low-resource-gain.md) — related
- [Cross-prompt pre-finetuning shows no significant benefit when sufficient (200-answer) in-prompt training data is available](prefinetuning-no-benefit-sufficient-data.md) — related
- [Pre-finetuning performance increases with the number of distinct prompts used, holding total pre-finetuning answers fixed](more-prompts-better-prefinetuning.md) — related
- [The pre-finetuned model learns a scoring principle: predicted scores correlate strongly and negatively with edit distance between answers and key phrases](model-learns-scoring-principle-key-phrase-similarity.md) — related

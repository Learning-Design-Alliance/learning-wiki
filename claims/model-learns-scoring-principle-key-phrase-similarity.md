---
type: claim
title: "The pre-finetuned model learns a scoring principle: predicted scores correlate strongly and negatively with edit distance between answers and key phrases"
description: "The pre-finetuned model learns a scoring principle: predicted scores correlate strongly and negatively with edit distance between answers and key phrases"
id: model-learns-scoring-principle-key-phrase-similarity
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
    i: 3
    kind: causal
    rigour: 2
---

# The pre-finetuned model learns a scoring principle: predicted scores correlate strongly and negatively with edit distance between answers and key phrases

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2` · `i3` large
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i3` In zero-shot settings, normalized edit distance between key phrases and annotated justification cues correlated negatively with predicted scores (r = -0.79 and r = -0.83 for the two best prompts). [→ Funayama 2025](#funayama-2025)

## Evidence

### Funayama 2025

Funayama, H., Matsubayashi, Y., Asazuma, Y., Mizumoto, T., & Inui, K. (2025). Cross-prompt Pre-finetuning of Language Models for Short Answer Scoring. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-025-00474-w

`q2 · i3` · `causal · r2`

Zero-shot behavioral analysis of the pre-finetuned key-phrase model on the two best-performing prompts (QWK 0.81 and 0.79), relating normalized edit distance to justification cues and predicted scores, with correlation coefficients of r = -0.79 and r = -0.83. The article concludes the model partially grasps that answers gain higher scores when they include expressions semantically closer to the key phrases.

> "The correlation coefﬁcients for Y14_2-2_2_3-B and Y14_1-2_1_3-D were -0.79 and -0.83, respectively, indicating a strong negative correlation between the edit distance and predicted scores."

## Discussion


## Related Claims
- [Cross-prompt finetuning of a pre-finetuned 8B LLM on 50 instances per prompt achieves average QWK of 0.85, comparable to professional human graders (0.87)](cross-prompt-finetuning-8b-human-level.md) — related
- [LLMs cannot effectively perform in-context learning for short answer scoring, but cross-prompt pre-finetuning substantially boosts their zero-shot performance](llm-icl-insufficient-prefinetuning-boosts-zero-shot.md) — related
- [Pre-finetuning without key phrases does not improve scoring performance and slightly lowers it relative to the BERT baseline](prefinetuning-without-key-phrases-no-gain.md) — related
- [Two-phase cross-prompt pre-finetuning with key phrases significantly improves short answer scoring accuracy when in-prompt training data is limited](cross-prompt-prefinetuning-key-phrases-low-resource-gain.md) — related

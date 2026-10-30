---
type: claim
title: Two-phase cross-prompt pre-finetuning with key phrases significantly improves short answer scoring accuracy when in-prompt training data is limited
description: Two-phase cross-prompt pre-finetuning with key phrases significantly improves short answer scoring accuracy when in-prompt training data is limited
id: cross-prompt-prefinetuning-key-phrases-low-resource-gain
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

# Two-phase cross-prompt pre-finetuning with key phrases significantly improves short answer scoring accuracy when in-prompt training data is limited

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Pre-finetuning with key phrases yields a maximum improvement of approximately 0.25 QWK when only 10 answers are used for finetuning, and halves the training data needed for the same performance. [→ Funayama 2025](#funayama-2025)

## Evidence

### Funayama 2025

Funayama, H., Matsubayashi, Y., Asazuma, Y., Mizumoto, T., & Inui, K. (2025). Cross-prompt Pre-finetuning of Language Models for Short Answer Scoring. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-025-00474-w

`q2 · i?` · `causal · r2`

Experiments on the RIKEN Japanese SAS dataset compared five BERT-based settings (baseline, key phrases only, 2-phase with/without key phrases, ensemble) across 10-200 finetuning instances. The article reports a maximum improvement of "approximately 0.25 QWK" at 10 answers, and that pre-finetuning with key phrases "reduced the required training data by half while maintaining the same performance."

> "The model performance was signiﬁcantly improved when the training data were limited, with a maximum improvement of approximately 0.25 QWK when 10 answers were used for ﬁnetuning compared with the performance of the baseline."

## Discussion


## Related Claims
- [Cross-prompt finetuning of a pre-finetuned 8B LLM on 50 instances per prompt achieves average QWK of 0.85, comparable to professional human graders (0.87)](cross-prompt-finetuning-8b-human-level.md) — related
- [Pre-finetuning without key phrases does not improve scoring performance and slightly lowers it relative to the BERT baseline](prefinetuning-without-key-phrases-no-gain.md) — related
- [Cross-prompt pre-finetuning shows no significant benefit when sufficient (200-answer) in-prompt training data is available](prefinetuning-no-benefit-sufficient-data.md) — related
- [LLMs cannot effectively perform in-context learning for short answer scoring, but cross-prompt pre-finetuning substantially boosts their zero-shot performance](llm-icl-insufficient-prefinetuning-boosts-zero-shot.md) — related
- [Pre-finetuning performance increases with the number of distinct prompts used, holding total pre-finetuning answers fixed](more-prompts-better-prefinetuning.md) — related
- [The pre-finetuned model learns a scoring principle: predicted scores correlate strongly and negatively with edit distance between answers and key phrases](model-learns-scoring-principle-key-phrase-similarity.md) — related

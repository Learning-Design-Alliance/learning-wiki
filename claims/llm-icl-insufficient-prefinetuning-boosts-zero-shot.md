---
type: claim
title: LLMs cannot effectively perform in-context learning for short answer scoring, but cross-prompt pre-finetuning substantially boosts their zero-shot performance
description: LLMs cannot effectively perform in-context learning for short answer scoring, but cross-prompt pre-finetuning substantially boosts their zero-shot performance
id: llm-icl-insufficient-prefinetuning-boosts-zero-shot
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
  - id: funayama-2025-2
    resource: "https://doi.org/10.1007/s40593-025-00474-w"
    title: "Funayama, H., Matsubayashi, Y., Asazuma, Y., Mizumoto, T., & Inui, K. (2025). Cross-prompt Pre-finetuning of Language Models for Short Answer Scoring. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-025-00474-w"
    author: "Funayama, H., Matsubayashi, Y., Asazuma, Y., Mizumoto, T., & Inui, K."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# LLMs cannot effectively perform in-context learning for short answer scoring, but cross-prompt pre-finetuning substantially boosts their zero-shot performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly
> **Design limits** · Funayama 2025 (2): the intervention came bundled with another change (read from the study by two models, 2026-10-28)

## Subclaims
`q2 i?` Baseline instruction-tuned LLMs showed extremely low QWK on SAS and did not improve with more in-context examples. [→ Funayama 2025](#funayama-2025)
`q2 i?` Cross-prompt pre-finetuning increased zero-shot QWK by 0.55 (8B) and 0.42 (70B), yet in-context examples did not improve the pre-finetuned LLMs. [→ Funayama 2025 (2)](#funayama-2025-2)

## Evidence

### Funayama 2025

Funayama, H., Matsubayashi, Y., Asazuma, Y., Mizumoto, T., & Inui, K. (2025). Cross-prompt Pre-finetuning of Language Models for Short Answer Scoring. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-025-00474-w

`q2 · i?` · `causal · r2`

Zero/few-shot evaluation (Table 2) of instruction-tuned Llama-3-Swallow 8B and 70B chat models with 0, 3, 5 and 10 in-context examples on the RIKEN dataset. The 8B baseline scored 0.08 zero-shot and the 70B 0.29, with no significant improvement as examples increased.

> "The result of the baseline model indicate that LLMs could not perform ICL on the SAS dataset. The 8B model exhibited extremely low performance, and there was no signiﬁcant improvement as the number of in-context examples increased."

### Funayama 2025 (2)

Funayama, H., Matsubayashi, Y., Asazuma, Y., Mizumoto, T., & Inui, K. (2025). Cross-prompt Pre-finetuning of Language Models for Short Answer Scoring. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-025-00474-w

`q2 · i?` · `causal · r2`

The same Table 2 evaluation found pre-finetuned LLMs reached 0.63 (8B) and 0.71 (70B) zero-shot QWK, but adding in-context examples did not help; the 8B model's QWK decreased with examples. The article notes a gap to human inter-grader agreement of 0.87.

> "In contrast, cross-prompt pre-ﬁnetuning signiﬁcantly enhanced the zero-shot performance of the LLMs, increasing the QWK by 0.55 and 0.42 in the 8B model and 70B models, respectively. However, despite the improvement, the in-context examples did not improve the preﬁnetuned LLMs."

## Discussion


## Related Claims
- [Cross-prompt finetuning of a pre-finetuned 8B LLM on 50 instances per prompt achieves average QWK of 0.85, comparable to professional human graders (0.87)](cross-prompt-finetuning-8b-human-level.md) — related
- [Two-phase cross-prompt pre-finetuning with key phrases significantly improves short answer scoring accuracy when in-prompt training data is limited](cross-prompt-prefinetuning-key-phrases-low-resource-gain.md) — related
- [The pre-finetuned model learns a scoring principle: predicted scores correlate strongly and negatively with edit distance between answers and key phrases](model-learns-scoring-principle-key-phrase-similarity.md) — related
- [Mid-range degradation is conditioned on task-specific adaptation: it is most severe for few-shot LLMs with few examples, decreases with more task-specific data, and is mildest for the fine-tuned encoder](task-specific-adaptation-conditions-mid-range-degradation.md) — related
- [In zero-shot evaluation, GPT-4's multi-label classification results were similar to what might be expected of fine-tuned classifiers, with SetFit and GPT-3.5 showing contrasting precision/recall patterns](gpt4-zero-shot-comparable-finetuned-classifiers.md) — related
- [Pre-finetuning performance increases with the number of distinct prompts used, holding total pre-finetuning answers fixed](more-prompts-better-prefinetuning.md) — related

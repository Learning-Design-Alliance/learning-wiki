---
type: claim
title: "Four reasoning-enhanced LLMs exceed 95% accuracy on the JNME, with Gemini 2.5 Pro highest at 97.2% and no significant pairwise differences"
description: "Four reasoning-enhanced LLMs exceed 95% accuracy on the JNME, with Gemini 2.5 Pro highest at 97.2% and no significant pairwise differences"
id: four-llms-exceed-95-jnme-2026
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: liu-mingxin-2026
    resource: "https://doi.org/10.1186/s12911-026-03370-y"
    title: "Liu Mingxin, Okuhara Tsuyoshi, Dai Zhehao, Zhao Minghong, Yin Wenqiang, Okada Hiroko, Furukawa Emi, Kiuchi Takahiro. (2026). Textbook-level medical knowledge in large language models: comparative evaluation using Japanese National Medical Examination. BMC Medical Informatics and Decision Making. https://doi.org/10.1186/s12911-026-03370-y"
    author: Liu Mingxin, Okuhara Tsuyoshi, Dai Zhehao, Zhao Minghong, Yin Wenqiang, Okada Hiroko, Furukawa Emi, Kiuchi Takahiro
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Four reasoning-enhanced LLMs exceed 95% accuracy on the JNME, with Gemini 2.5 Pro highest at 97.2% and no significant pairwise differences

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` GPT-5, Grok-4, Claude Opus 4.1, and Gemini 2.5 Pro achieved overall accuracies of 96.3%, 95.6%, 96.1%, and 97.2% respectively on 793 JNME questions, with no significant pairwise differences. [→ Liu Mingxin 2026](#liu-mingxin-2026)

## Evidence

### Liu Mingxin 2026

Liu Mingxin, Okuhara Tsuyoshi, Dai Zhehao, Zhao Minghong, Yin Wenqiang, Okada Hiroko, Furukawa Emi, Kiuchi Takahiro. (2026). Textbook-level medical knowledge in large language models: comparative evaluation using Japanese National Medical Examination. BMC Medical Informatics and Decision Making. https://doi.org/10.1186/s12911-026-03370-y

`q2 · i?` · `design · r2`

Evaluation of four LLMs on the full 2019 and 2025 JNME (793 questions) with chain-of-thought prompting; the article reports "97.2% for Gemini 2.5 Pro" as the highest overall accuracy and notes all pairwise comparisons were non-significant (all p-values > 0.05).

> "The corresponding overall accuracy rates, ranked from highest to lowest, were 97.2% for Gemini 2.5 Pro, 96.3% for GPT-5, 96.1% for Claude Opus 4.1, and 95.6% for Grok-4."

## Discussion


## Related Claims
- [Gemini 2.5 Pro significantly outperformed GPT-5 on EDAIC questions as the only significant pairwise difference after Holm correction](gemini-outperformed-gpt5-edaic-pairwise.md) — related
- [Accuracy is significantly lower on image-based than non-image-based questions for three of four LLMs](image-based-questions-lower-accuracy.md) — related
- [LLM performance does not differ significantly between 2019 and 2025 exam questions despite training-cutoff differences](no-performance-difference-exam-year.md) — related

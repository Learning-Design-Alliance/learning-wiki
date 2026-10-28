---
type: claim
title: GPT-4 outperforms GPT-3.5-turbo in a single-lesson question-detection test
description: GPT-4 outperforms GPT-3.5-turbo in a single-lesson question-detection test
id: gpt4-outperforms-gpt35-single-lesson
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: weak
newest_evidence: 2026
sources:
  - id: lehesvuori-2026
    resource: "https://doi.org/10.1007/s11423-025-10545-3"
    title: "Lehesvuori, S., Urrutia, F., Heilala, V., Araya, R., & Hämäläinen, R. (2026). Discovering technology-aided possibilities for automatic analysis of science teacher questions. Education Tech Research Dev. https://doi.org/10.1007/s11423-025-10545-3"
    author: "Lehesvuori, S., Urrutia, F., Heilala, V., Araya, R., & Hämäläinen, R."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# GPT-4 outperforms GPT-3.5-turbo in a single-lesson question-detection test

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In a one-lesson comparison, GPT-4 five-shot CoT achieved higher precision, recall, balanced accuracy and F1 than GPT-3.5-turbo five-shot CoT. [→ Lehesvuori 2026](#lehesvuori-2026)

## Evidence

### Lehesvuori 2026

Lehesvuori, S., Urrutia, F., Heilala, V., Araya, R., & Hämäläinen, R. (2026). Discovering technology-aided possibilities for automatic analysis of science teacher questions. Education Tech Research Dev. https://doi.org/10.1007/s11423-025-10545-3

`q2 · i?` · `design · r2`

Single-lesson test (Table 4): GPT-4 5-shot CoT reached F1 0.5797 and BA 0.9145 versus F1 0.51 for GPT-3.5-turbo, showing "GPT-4 outperforming the previous model."

> "The one lesson results show GPT-4 outperforming the previous model. Results also indicate that GPT-4 could challenge the HCR with the whole data, yet this experiment cannot be executed here since the high costs"

## Discussion


## Related Claims
- [In detecting teacher questions with zero-shot GPT-3.5-turbo, chain-of-thought prompting had slightly higher F1 and precision than Self-Ask but slightly lower recall and balanced accuracy](cot-outperforms-self-ask-zero-shot.md) — related
- [Few-shot chain-of-thought prompting outperforms zero-shot prompting for detecting teacher questions](few-shot-cot-outperforms-zero-shot-question-detection.md) — related
- [Few-shot LLM approaches outperform standalone supervised ML approaches, yet hand-crafted rules remain relevant](few-shot-llm-outperforms-ml-hcr-relevant.md) — related
- [Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance](curricular-cot-improves-accuracy-larger-models.md) — related

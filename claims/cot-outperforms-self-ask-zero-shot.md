---
type: claim
title: In detecting teacher questions with zero-shot GPT-3.5-turbo, chain-of-thought prompting had slightly higher F1 and precision than Self-Ask but slightly lower recall and balanced accuracy
description: In detecting teacher questions with zero-shot GPT-3.5-turbo, chain-of-thought prompting had slightly higher F1 and precision than Self-Ask but slightly lower recall and balanced accuracy
id: cot-outperforms-self-ask-zero-shot
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: weak
newest_evidence: 2026
source_checked: 2026-10-28
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

# In detecting teacher questions with zero-shot GPT-3.5-turbo, chain-of-thought prompting had slightly higher F1 and precision than Self-Ask but slightly lower recall and balanced accuracy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · checked against its sources 2026-10-28 (automated, 1 of 1 entry) · not reviewed by a person

## Subclaims
`q2 i?` With GPT-3.5-turbo zero-shot on seven lessons, CoT prompting had a higher F1 (0.2931 vs 0.2789) and precision (0.2818 vs 0.2387) than Self-Ask prompting, but lower recall (0.3054 vs 0.3352) and balanced accuracy (0.6245 vs 0.6289); the authors summarise this as CoT performing better and kept CoT for later experiments. [→ Lehesvuori 2026](#lehesvuori-2026)

## Evidence

### Lehesvuori 2026

Lehesvuori, S., Urrutia, F., Heilala, V., Araya, R., & Hämäläinen, R. (2026). Discovering technology-aided possibilities for automatic analysis of science teacher questions. Education Tech Research Dev. https://doi.org/10.1007/s11423-025-10545-3

`q2 · i?` · `design · r2`

Seven-lesson prompt comparison (Table 2): zero-shot CoT reached precision 0.2818, recall 0.3054, BA 0.6245 and F1 0.2931, versus precision 0.2387, recall 0.3352, BA 0.6289 and F1 0.2789 for Self-Ask. CoT is ahead on F1 and precision and slightly behind on recall and balanced accuracy, with no test of the differences; the article nonetheless reports "CoT performed bet- ter than SA."

> "The seven lesson test results show that with GPT-3.5-turbo zero-shots CoT performed bet- ter than SA."

## Discussion


## Related Claims
- [Few-shot chain-of-thought prompting outperforms zero-shot prompting for detecting teacher questions](few-shot-cot-outperforms-zero-shot-question-detection.md) — related
- [Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance](curricular-cot-improves-accuracy-larger-models.md) — related
- [GPT-4 outperforms GPT-3.5-turbo in a single-lesson question-detection test](gpt4-outperforms-gpt35-single-lesson.md) — related
- [In-context examples improve LLM Bloom classification: three-shot and ten-shot prompting outperform zero-shot across datasets](in-context-examples-improve-bloom-classification.md) — related
- [Chain-of-thought prompting yields higher-quality GenAI feedback on argumentative essays than Zero-shot prompting and teacher feedback](cot-prompting-higher-feedback-quality-than-zero-shot-and-teacher.md) — related
- [Zero-shot LLMs perform only marginally above random in five-class competency classification but exceed 70% accuracy on binary classification](zero-shot-llm-granularity-competency-classification.md) — related
- [Under Chain-of-Thought prompting, higher Bloom-level classification accuracy correlates with lower category consistency in generated questions](negative-correlation-classification-catcons.md) — related
- [In-context learning did not consistently improve LLM annotation reliability over zero-shot prompting for engagement coding](icl-no-better-than-zero-shot-engagement-coding.md) — related

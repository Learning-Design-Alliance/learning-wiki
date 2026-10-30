---
type: claim
title: Few-shot chain-of-thought prompting outperforms zero-shot prompting for detecting teacher questions
description: Few-shot chain-of-thought prompting outperforms zero-shot prompting for detecting teacher questions
id: few-shot-cot-outperforms-zero-shot-question-detection
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2026
source_checked: 2026-10-28
recheck_by: 2029
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

# Few-shot chain-of-thought prompting outperforms zero-shot prompting for detecting teacher questions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · checked against its sources 2026-10-28 (automated, 1 of 1 entry) · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` GPT-3.5-turbo five-shot CoT prompting achieved higher precision, recall, balanced accuracy and F1 than zero-shot prompting for detecting teacher questions. [→ Lehesvuori 2026](#lehesvuori-2026)

## Evidence

### Lehesvuori 2026

Lehesvuori, S., Urrutia, F., Heilala, V., Araya, R., & Hämäläinen, R. (2026). Discovering technology-aided possibilities for automatic analysis of science teacher questions. Education Tech Research Dev. https://doi.org/10.1007/s11423-025-10545-3

`q2 · i?` · `design · r2`

Seven-lesson test of GPT-3.5-turbo prompting variants (Table 2). The five-shot CoT model reached F1 0.4667 and balanced accuracy 0.8399, versus F1 0.2931 for zero-shot CoT, showing "the GPT-3.5-turbo five-shot approach was the best-performing classification model."

> "the GPT-3.5-turbo five-shot approach was the best-performing classification model. Five-shot prompting approach technique involved five real question examples from the data."

## Discussion


## Related Claims
- [In detecting teacher questions with zero-shot GPT-3.5-turbo, chain-of-thought prompting had slightly higher F1 and precision than Self-Ask but slightly lower recall and balanced accuracy](cot-outperforms-self-ask-zero-shot.md) — related
- [GPT-4 outperforms GPT-3.5-turbo in a single-lesson question-detection test](gpt4-outperforms-gpt35-single-lesson.md) — related
- [In-context examples improve LLM Bloom classification: three-shot and ten-shot prompting outperform zero-shot across datasets](in-context-examples-improve-bloom-classification.md) — related
- [Few-shot LLM approaches outperform standalone supervised ML approaches, yet hand-crafted rules remain relevant](few-shot-llm-outperforms-ml-hcr-relevant.md) — related

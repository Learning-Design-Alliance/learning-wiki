---
type: claim
title: "GPT models showed lower accuracy with more rubric-related errors (28% vs. 13% for Gemini 3 Flash) and near parity between false positives and negatives"
description: "GPT models showed lower accuracy with more rubric-related errors (28% vs."
id: gpt-models-more-rubric-errors-than-gemini
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: jacob-levine-2026
    resource: "https://doi.org/10.48550/arxiv.2605.19043"
    title: "Jacob Levine, Miguel Aenlle, Craig Zilles, Matthew West, and Mariana Silva. (2026). Automated Grading of Handwritten Mathematics Using Vision-Capable LLMs. https://arxiv.org/abs/2605.19043 [doi:10.48550/arxiv.2605.19043](https://doi.org/10.48550/arxiv.2605.19043)"
    author: Jacob Levine, Miguel Aenlle, Craig Zilles, Matthew West, and Mariana Silva
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# GPT models showed lower accuracy with more rubric-related errors (28% vs. 13% for Gemini 3 Flash) and near parity between false positives and negatives

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` GPT models showed lower accuracy with more rubric-related errors (28% vs. 13% for Gemini 3 Flash) and near parity between false positives and negatives, partly because rubric errors tended toward false negatives. [→ Jacob Levine 2026](#jacob-levine-2026)

## Evidence

### Jacob Levine 2026

Jacob Levine, Miguel Aenlle, Craig Zilles, Matthew West, and Mariana Silva. (2026). Automated Grading of Handwritten Mathematics Using Vision-Capable LLMs. https://arxiv.org/abs/2605.19043 [doi:10.48550/arxiv.2605.19043](https://doi.org/10.48550/arxiv.2605.19043)

`q2 · i?` · `design · r2`

Cross-model comparison from the conclusion's summary of the rubric-item-level error analysis on authentic submissions from two STEM courses. The article reports "more rubric-related errors (28% vs. 13% for Gemini 3 Flash)" for GPT models; no effect size is printed.

> "GPT models showed lower accuracy with more rubric-related errors (28% vs. 13% for Gemini 3 Flash) and near parity between false positives and negatives, partly because rubric errors tended toward false negatives."

## Discussion


## Related Claims
- [Gemini-3-flash achieved the highest rubric-item accuracy, ranging from 89% on Course 2 to over 99% on Course 1](gemini-3-flash-highest-rubric-item-accuracy.md) — related
- [Frontier LLMs achieve the best balance between detecting misconceptions in correct-answer cases and not over-flagging correct students, while fine-tuned local models achieve under 58% TM recall](frontier-llms-best-balance-tm-detection.md) — related
- [No consistent relationship was observed between false-positive and false-negative rates and either the question or the LLM model](no-consistent-fp-fn-pattern.md) — related
- [The system's error detection recall rate for complex rhythm errors was 91.2% ± 1.8%](rhythm-error-detection-recall-91-2.md) — related
- [GPT-4's error-diagnosis accuracy varies by error type: near-perfect on correct answers, weakest on Wrong Field and multiple-error responses](gpt4-diagnosis-accuracy-varies-by-error-type.md) — related
- [Validator false-negative cases reveal structural reasoning weaknesses, including answer-schema misinterpretation and internal inconsistency](code-gen-validator-fn-reasoning-weaknesses.md) — related
- [FATE benchmarks rank Gemini 2.5 Flash highest among commercial AI tutors, with actionability weakest for all models](fate-benchmark-commercial-ai-tutors.md) — related
- [Students reported first-pass false-positive deductions at a mean of 2.94 per term, normalising to about 0.6% of rubric items](student-reported-grading-errors-lata.md) — related

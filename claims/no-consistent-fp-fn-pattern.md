---
type: claim
title: No consistent relationship was observed between false-positive and false-negative rates and either the question or the LLM model
description: No consistent relationship was observed between false-positive and false-negative rates and either the question or the LLM model
id: no-consistent-fp-fn-pattern
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
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

# No consistent relationship was observed between false-positive and false-negative rates and either the question or the LLM model

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The study did not observe a consistent relationship between relative rates of false positives and false negatives and either the specific question or LLM model, contrary to expectations of systematic leniency or strictness. [→ Jacob Levine 2026](#jacob-levine-2026)

## Evidence

### Jacob Levine 2026

Jacob Levine, Miguel Aenlle, Craig Zilles, Matthew West, and Mariana Silva. (2026). Automated Grading of Handwritten Mathematics Using Vision-Capable LLMs. https://arxiv.org/abs/2605.19043 [doi:10.48550/arxiv.2605.19043](https://doi.org/10.48550/arxiv.2605.19043)

`q2 · i?` · `design · r2`

Null observational finding from the rubric-item-level error analysis across five questions and three models. The article reports no consistent relationship was observed; the authors had expected some models might be consistently more lenient or strict. No effect size or test statistic is printed.

> "Interestingly,wedidnotobserveaconsistentrelationshipbetweentherelativerates of false positives and false negatives and either the specific question or LLM model."

## Discussion


## Related Claims
- [LLM-based scoring produced fewer false negatives than Deep Tutor on a balanced test set, which the authors expect would spare students the frustration of correct explanations judged incorrect](llm-scoring-fewer-false-negatives-than-deep-tutor.md) — related
- [Some LLMs exhibit a selection bias against selecting option D on multiple-choice pedagogy questions](llm-selection-bias-against-option-d.md) — related
- [GPT models showed lower accuracy with more rubric-related errors (28% vs. 13% for Gemini 3 Flash) and near parity between false positives and negatives](gpt-models-more-rubric-errors-than-gemini.md) — related
- [AI grading errors concentrate in graphical tasks and include both false positives on incorrect equations and false negatives from misread sketches and labels](ai-grading-failure-modes-graphical-tasks.md) — related
- [Small language models used as automated judges exhibit severe leniency bias against tutoring responses](slm-judges-show-severe-leniency-bias.md) — reports the opposite
- [Validator false-negative cases reveal structural reasoning weaknesses, including answer-schema misinterpretation and internal inconsistency](code-gen-validator-fn-reasoning-weaknesses.md) — related
- [Lower-performing groups gain relative advantage because the scorer detects incorrect responses better for them, producing more false positives](lower-performers-more-false-positives-advantage.md) — related
- [81.54% of incorrectly analysed programs were incorrect programs analysed as correct](php-its-error-direction-misleading-majority.md) — related

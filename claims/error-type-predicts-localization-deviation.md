---
type: claim
title: "Error type predicts localization deviation: question-misunderstanding errors are predicted later than they occur, while missing/extra-variable errors are predicted slightly earlier"
description: "Error type predicts localization deviation: question-misunderstanding errors are predicted later than they occur, while missing/extra-variable errors are predicted slightly earlier"
id: error-type-predicts-localization-deviation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: kv-aditya-srivatsa-2025
    resource: "https://doi.org/10.18653/v1/2025.emnlp-main.553"
    title: "KV Aditya Srivatsa, Kaushal Kumar Maurya, Ekaterina Kochmar. (2025). LLMs cannot spot math errors, even when allowed to peek into the solution. [doi:10.18653/v1/2025.emnlp-main.553](https://doi.org/10.18653/v1/2025.emnlp-main.553)"
    author: KV Aditya Srivatsa, Kaushal Kumar Maurya, Ekaterina Kochmar
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Error type predicts localization deviation: question-misunderstanding errors are predicted later than they occur, while missing/extra-variable errors are predicted slightly earlier

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across models and prompt types, question-independent errors are uniformly distributed over prediction deviation, whereas misunderstanding errors overshoot and missing/extra-variable errors undershoot. [→ KV Aditya Srivatsa 2025](#kv-aditya-srivatsa-2025)

## Evidence

### KV Aditya Srivatsa 2025

KV Aditya Srivatsa, Kaushal Kumar Maurya, Ekaterina Kochmar. (2025). LLMs cannot spot math errors, even when allowed to peek into the solution. [doi:10.18653/v1/2025.emnlp-main.553](https://doi.org/10.18653/v1/2025.emnlp-main.553)

`q2 · i?` · `causal · r2`

Distribution analysis of VtG ground-truth error types against normalized error-step distance across models and prompt types (Figure 4); the article reports that "errors resulting from question misunderstanding are predicted much later than they occur".

> "question-independent errors, such as calculation or unit-conversion mistakes, are uniformly distributed regardless of prediction deviation, whereas errors resulting from question misunderstanding are predicted much later than they occur. In contrast, errors involving missing or extra variables tend to be predicted a little before they occur."

## Discussion


## Related Claims
- [Across all feedback generation methods tested, most failures occur because the LLM cannot correctly identify the error in the student's incorrect answer, especially when multiple reasoning steps are required.](llm-failure-identifying-student-error.md) — related
- [Qualitative error analysis yields five recurring error types, with over-inference most prevalent (33.5%), followed by evidence misidentification (23.4%) and hallucination (19.8%)](five-error-types-llm-diagnosis-vague-evidence.md) — related
- [A small set of latent factors (3–4) predicts individual error patterns far better than graph-type or question-type decompositions](latent-factors-outperform-design-categories.md) — related

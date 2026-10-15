---
type: claim
title: "GPT-4's error-diagnosis accuracy varies by error type: near-perfect on correct answers, weakest on Wrong Field and multiple-error responses"
description: "GPT-4's error-diagnosis accuracy varies by error type: near-perfect on correct answers, weakest on Wrong Field and multiple-error responses"
id: gpt4-diagnosis-accuracy-varies-by-error-type
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
sources:
  - id: reddig-2025
    resource: "https://doi.org/10.1007/s40593-025-00505-6"
    title: "Reddig, J. M., Arora, A., & MacLellan, C. J. (2025). Generating In-Context, Personalized Feedback for Intelligent Tutors with Large Language Models. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-025-00505-6"
    author: "Reddig, J. M., Arora, A., & MacLellan, C. J."
    q: 2
    i: "?"
    kind: design
    rigour: 3
---

# GPT-4's error-diagnosis accuracy varies by error type: near-perfect on correct answers, weakest on Wrong Field and multiple-error responses

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q2`

## Subclaims
`q2 i?` GPT-4 recognized matching correct answers 99% of the time but failed to recognize Wrong Field errors nearly 30% of the time. [→ Reddig 2025](#reddig-2025)

## Evidence

### Reddig 2025

Reddig, J. M., Arora, A., & MacLellan, C. J. (2025). Generating In-Context, Personalized Feedback for Intelligent Tutors with Large Language Models. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-025-00505-6

`q2 · i?` · `design · r3`

Error-type breakdown of the same GPT-4 diagnosis analysis across all tutoring topics (Table 4, final prompt). Correct Answer accuracy was 99.0% (238), Wrong Field 72.3% (162), and multiple-error answers 71.67% (42).

> "The LLM is most adept at identifying a correct answer, recognizing a matching answer 99% of the time, and questioning the validity of the correct answer only 1% of the time. GPT-4 performed the poorest on Wrong Field errors, unable to recognize nearly 30% of the time when a student had skipped a step in the problem solving process."

## Discussion


## Related Claims
- [Given sufficient prompt context, GPT-4 describes student errors in a College Algebra ITS with 87.8% accuracy](gpt4-diagnoses-its-errors-87-8-accuracy.md) — related
- [Adding tutor interface and skill-estimate context to the prompt substantially improves GPT-4's error-diagnosis accuracy](prompt-context-improves-gpt4-error-diagnosis.md) — related
- [GPT models showed lower accuracy with more rubric-related errors (28% vs. 13% for Gemini 3 Flash) and near parity between false positives and negatives](gpt-models-more-rubric-errors-than-gemini.md) — related
- Fine-tuned classifiers detect only about 57% of correct-answer misconceptions despite near-perfect wrong-answer classification — related
- [GPT-4 generates targeted corrective feedback for 66% of student errors, but 35% of hints are too general, incorrect, or give away the answer](gpt4-feedback-66-percent-targeted-35-percent-flawed.md) — related

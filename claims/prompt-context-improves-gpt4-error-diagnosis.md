---
type: claim
title: "Adding tutor interface and skill-estimate context to the prompt substantially improves GPT-4's error-diagnosis accuracy"
description: "Adding tutor interface and skill-estimate context to the prompt substantially improves GPT-4's error-diagnosis accuracy"
id: prompt-context-improves-gpt4-error-diagnosis
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

# Adding tutor interface and skill-estimate context to the prompt substantially improves GPT-4's error-diagnosis accuracy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q2`

## Subclaims
`q2 i?` On the complex factoring tutors, progressively adding interface information and skill estimates to the prompt raised GPT-4's diagnosis accuracy across error types. [→ Reddig 2025](#reddig-2025)

## Evidence

### Reddig 2025

Reddig, J. M., Arora, A., & MacLellan, C. J. (2025). Generating In-Context, Personalized Feedback for Intelligent Tutors with Large Language Models. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-025-00505-6

`q2 · i?` · `design · r3`

Three rounds of prompt engineering on the factoring dataset (N = 199): with basic context GPT-4 questioned whether a correct answer was correct 21% of the time; adding the interface brought correct-answer recognition to 100%, and adding the skill estimate improved logical-mistake diagnosis to 81%.

> "Table 3 demonstrates how, with additional context to situate the student's answer within the appropriate sub-problem, GPT-4's accuracy increased on a complex tutoring environment like factoring."

## Discussion


## Related Claims
- [Given sufficient prompt context, GPT-4 describes student errors in a College Algebra ITS with 87.8% accuracy](gpt4-diagnoses-its-errors-87-8-accuracy.md) — a narrower finding that bears on this claim
- [GPT-4's error-diagnosis accuracy varies by error type: near-perfect on correct answers, weakest on Wrong Field and multiple-error responses](gpt4-diagnosis-accuracy-varies-by-error-type.md) — related

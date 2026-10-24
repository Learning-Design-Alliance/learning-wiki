---
type: claim
title: "Given sufficient prompt context, GPT-4 describes student errors in a College Algebra ITS with 87.8% accuracy"
description: "Given sufficient prompt context, GPT-4 describes student errors in a College Algebra ITS with 87.8% accuracy"
id: gpt4-diagnoses-its-errors-87-8-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
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

# Given sufficient prompt context, GPT-4 describes student errors in a College Algebra ITS with 87.8% accuracy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` When given enough context to situate the student's step in the problem-solving process, GPT-4 accurately described student errors 87.8% of the time across all tutoring topics. [→ Reddig 2025](#reddig-2025)

## Evidence

### Reddig 2025

Reddig, J. M., Arora, A., & MacLellan, C. J. (2025). Generating In-Context, Personalized Feedback for Intelligent Tutors with Large Language Models. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-025-00505-6

`q2 · i?` · `design · r3`

Analysis of 6926 logged tutor transactions from College Algebra classes, of which 1307 were incorrect answers; each error was prompted to GPT-4 (gpt-4-0613) for diagnosis and human-coded as a correct or incorrect description. The final prompt achieved "87.8% accuracy" (1144 passing errors).

> "Our results show in Table 4 that when given enough context to describe what step in the problem-solving process the student is working on, GPT-4 can describe student errors with 87.8% accuracy."

## Discussion


## Related Claims
- [GPT-4's error-diagnosis accuracy varies by error type: near-perfect on correct answers, weakest on Wrong Field and multiple-error responses](gpt4-diagnosis-accuracy-varies-by-error-type.md) — related
- [Adding tutor interface and skill-estimate context to the prompt substantially improves GPT-4's error-diagnosis accuracy](prompt-context-improves-gpt4-error-diagnosis.md) — a broader claim this one bears on
- [GPT-4 generates targeted corrective feedback for 66% of student errors, but 35% of hints are too general, incorrect, or give away the answer](gpt4-feedback-66-percent-targeted-35-percent-flawed.md) — related
- [GPT-4 scoring errors clustered on multiple possible answers, unrecognized vocabulary, and missed incorrect or missing answers, while faculty were overly generous graders](gpt4-faculty-error-patterns-oeq-scoring.md) — related
- [GPT-generated feedback passes simulated-student helpfulness evaluations only about 35% of the time on real student data](gpt-feedback-passes-automated-helpfulness-35-percent.md) — related

---
type: claim
title: "GPT-4 generates targeted corrective feedback for 66% of student errors, but 35% of hints are too general, incorrect, or give away the answer"
description: "GPT-4 generates targeted corrective feedback for 66% of student errors, but 35% of hints are too general, incorrect, or give away the answer"
id: gpt4-feedback-66-percent-targeted-35-percent-flawed
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
newest_evidence: 2025
source_checked: 2026-10-17
recheck_by: 2028
sources:
  - id: reddig-2025
    resource: "https://doi.org/10.1007/s40593-025-00505-6"
    title: "Reddig, J. M., Arora, A., & MacLellan, C. J. (2025). Generating In-Context, Personalized Feedback for Intelligent Tutors with Large Language Models. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-025-00505-6"
    author: "Reddig, J. M., Arora, A., & MacLellan, C. J."
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: reddig-2025-2
    resource: "https://doi.org/10.1007/s40593-025-00505-6"
    title: "Reddig, J. M., Arora, A., & MacLellan, C. J. (2025). Generating In-Context, Personalized Feedback for Intelligent Tutors with Large Language Models. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-025-00505-6"
    author: "Reddig, J. M., Arora, A., & MacLellan, C. J."
    q: 2
    i: "?"
    kind: design
    rigour: 3
---

# GPT-4 generates targeted corrective feedback for 66% of student errors, but 35% of hints are too general, incorrect, or give away the answer

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2`–`r3` · `q2`
> **Currency** · newest study 2025 · checked against its sources 2026-10-17 (automated, 2 of 2 entries) · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` When prompted to diagnose the error first and then generate feedback, 66% of GPT-4's hints were targeted to the student's specific mistake. [→ Reddig 2025](#reddig-2025)
`q2 i?` Of the generated hints, 22.3% were general, 7.1% gave the exact answer, and 4.8% gave incorrect directions. [→ Reddig 2025 (2)](#reddig-2025-2)

## Evidence

### Reddig 2025

Reddig, J. M., Arora, A., & MacLellan, C. J. (2025). Generating In-Context, Personalized Feedback for Intelligent Tutors with Large Language Models. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-025-00505-6

`q2 · i?` · `design · r2`

Human coding (two independent coders, Cohen's Kappa 0.768) of the hints GPT-4 generated for the diagnosed student errors from the Apprentice Tutors transaction data, categorizing each hint as Targeted, General, Gives Answer, or Incorrect; "66% of the generated feedback wasTargetedto the student".

> "Using this approach, 66% of the generated feedback wasTargetedto the student and speciﬁcally addressed the mistake."

### Reddig 2025 (2)

Reddig, J. M., Arora, A., & MacLellan, C. J. (2025). Generating In-Context, Personalized Feedback for Intelligent Tutors with Large Language Models. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-025-00505-6

`q2 · i?` · `design · r3`

Same coding study of GPT-generated hints: general hints restated the field's goal, 7.1% included the exact answer with explanatory feedback, and "Incorrect directions were given in 4.8% of the feedback", typically after a misdiagnosis.

> "We classiﬁed 22.3% of hints as General – that is, a general description of how to satisfy the ﬁeld."

## Discussion

## Related Claims

- [Learners receiving ChatGPT-generated hints showed statistically significant learning gains compared to a no-hint control in an online mathematics tutoring experiment](chatgpt-hints-significant-gains-versus-control.md) — the general claim this finding bears on, with the studies behind it

- [Feedback improves learning by a medium amount on average, but its effect varies widely with the information it carries, and a substantial share of feedback effects are negative](feedback-improves-learning.md) — the general claim this finding bears on, with the studies behind it
- [Given sufficient prompt context, GPT-4 describes student errors in a College Algebra ITS with 87.8% accuracy](gpt4-diagnoses-its-errors-87-8-accuracy.md) — related
- [GPT-4o-mini natural language feedback was overwhelmingly helpful and never harmful in quality annotation](nl-feedback-quality-92-percent-helpful.md) — related
- [GPT-4's error-diagnosis accuracy varies by error type: near-perfect on correct answers, weakest on Wrong Field and multiple-error responses](gpt4-diagnosis-accuracy-varies-by-error-type.md) — related
- [Immediate-feedback tutors allow learning from errors but deny learning from their downstream consequences](immediate-feedback-limits-downstream-error-learning.md) — related
- [Hint-not-solution is the most challenging rubric dimension, with scores ranging from 6% to 81% across models](hint-not-solution-most-challenging-dimension.md) — related
- [Limiting verbose Math Agent guidance sharply reduced answer giveaway but decreased cognitive engagement](math-agent-guidance-limit-tradeoff.md) — related
- [ChatGPT 3.5 produced low-quality hints for 32% of problems, reducible to near 0% for algebra and 13% for statistics via the self-consistency technique](chatgpt-hint-error-rate-self-consistency.md) — related
- [Adding tutor interface and skill-estimate context to the prompt substantially improves GPT-4's error-diagnosis accuracy](prompt-context-improves-gpt4-error-diagnosis.md) — related
- [In a 10-student pilot, EduGuard produced higher post-test accuracy, larger normalized learning gain, lower calibration error, and lower overreliance than GPT-4o-mini Tutor](eduguard-pilot-learning-gain-overreliance.md) — related

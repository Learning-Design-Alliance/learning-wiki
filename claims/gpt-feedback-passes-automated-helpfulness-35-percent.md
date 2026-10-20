---
type: claim
title: "GPT-generated feedback passes simulated-student helpfulness evaluations only about 35% of the time on real student data"
description: "GPT-generated feedback passes simulated-student helpfulness evaluations only about 35% of the time on real student data"
id: gpt-feedback-passes-automated-helpfulness-35-percent
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: weak
sources:
  - id: reddig-2025
    resource: "https://doi.org/10.1007/s40593-025-00505-6"
    title: "Reddig, J. M., Arora, A., & MacLellan, C. J. (2025). Generating In-Context, Personalized Feedback for Intelligent Tutors with Large Language Models. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-025-00505-6"
    author: "Reddig, J. M., Arora, A., & MacLellan, C. J."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# GPT-generated feedback passes simulated-student helpfulness evaluations only about 35% of the time on real student data

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` When applied to real student data, only approximately 35% of GPT-generated feedback passed simulated student helpfulness evaluations. [→ Reddig 2025](#reddig-2025)

## Evidence

### Reddig 2025

Reddig, J. M., Arora, A., & MacLellan, C. J. (2025). Generating In-Context, Personalized Feedback for Intelligent Tutors with Large Language Models. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-025-00505-6

`q2 · i?` · `design · r2`

The article's introduction reports this result from its series of studies examining whether LLMs can autonomously evaluate the helpfulness and informativeness of the feedback they generate; the full Study 3 text was not available in the supplied excerpt.

> "when applied to real student data, GPT-generated feedback only pass simulated student helpfulness evaluations approximately 35% of the time."

## Discussion


## Related Claims
- [Immediate post-feedback improvement is near zero on average and does not differ significantly across feedback conditions](baseline-post-feedback-gains-near-zero-no-condition-differences.md) — related
- [Prompting-based student simulators maintain artificially high pass rates (~80%) from the first submission step, while fine-tuned models track real students' low-start, sharp-increase trajectories](prompted-simulators-artificially-high-pass-rates.md) — related
- [Human scoring and feedback for HDR takes about 11 minutes 30 seconds per learner, while GPT-based scoring and feedback is nearly instant](hdr-human-scoring-time-burden.md) — related
- [Differences in student pass-rate distributions between test splits explain the smaller INSIDE-over-SFT improvement on test_NP](pass-rate-distribution-explains-split-gap.md) — related
- [Fine-tuning with INSIDE internal dialogue achieves the lowest Wasserstein distances to real student code distributions on test_OP across all action-fidelity metrics](inside-lowest-wasserstein-action-fidelity-test-op.md) — related
- [Given sufficient prompt context, GPT-4 describes student errors in a College Algebra ITS with 87.8% accuracy](gpt4-diagnoses-its-errors-87-8-accuracy.md) — related
- [Students whose tutors have access to Tutor CoPilot are 4 percentage points more likely to master lesson topics (pass exit tickets) in live K-12 math tutoring](tutor-copilot-raises-exit-ticket-mastery-4pp.md) — related

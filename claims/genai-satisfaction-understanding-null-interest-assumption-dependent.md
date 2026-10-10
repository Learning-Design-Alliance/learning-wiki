---
type: claim
title: Effects of GenAI availability on self-reported understanding are insignificant; effects on interest are significant only under the transient-COVID assumption
description: Effects of GenAI availability on self-reported understanding are insignificant; effects on interest are significant only under the transient-COVID assumption
id: genai-satisfaction-understanding-null-interest-assumption-dependent
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: dumlao-2026
    resource: "https://arxiv.org/abs/2607.21534"
    title: "Dumlao, J. M. Z., Wang, M., Xie, Z., Hu, J., Bar, I., Chaney, G., III, Gold, H., & Teplitskiy, M. (2026). Generative AI Availability, Grades, and Student Satisfaction at a Large University. arXiv. https://arxiv.org/abs/2607.21534"
    author: "Dumlao, J. M. Z., Wang, M., Xie, Z., Hu, J., Bar, I., Chaney, G., III, Gold, H., & Teplitskiy, M."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Effects of GenAI availability on self-reported understanding are insignificant; effects on interest are significant only under the transient-COVID assumption

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Under persistent COVID effects, no change in median self-reported understanding, subject interest, or relative workload in more susceptible courses; under transient COVID effects, a modest increase in interest and decrease in relative workload. [→ Dumlao 2026](#dumlao-2026)

## Evidence

### Dumlao 2026

Dumlao, J. M. Z., Wang, M., Xie, Z., Hu, J., Bar, I., Chaney, G., III, Gold, H., & Teplitskiy, M. (2026). Generative AI Availability, Grades, and Student Satisfaction at a Large University. arXiv. https://arxiv.org/abs/2607.21534

`q2 · i?` · `causal · r2`

Course-evaluation DiD on median Likert scores for understanding, interest, and relative workload at the offering level. The article reports results depend on COVID modeling; the full evaluation table (Appendix F, Table 12) lies beyond the supplied text, so no effect sizes are available.

> "If COVID effects are persistent, we find no change in median self-reported understanding, subject interest, or relative workload in more susceptible courses after ChatGPT. If COVID effects are transient, we estimate a modest increase in interest and decrease in relative workload."

## Discussion


## Learner Variables
- [Motivation](../learner-variables/motivation.md) — outcome: instruction changes it

## Related Claims
- [Positive average grade effects appear only under COVID-laden treatment anchors, indicating such readings reflect the COVID shock rather than ChatGPT](covid-laden-anchors-produce-spurious-positive-grade-effect.md) — related
- [More GenAI-susceptible courses show no raised grade floor after ChatGPT: passing-margin and failing/withdrawal probabilities are null under both COVID assumptions](no-raised-grade-floor-genai-susceptible-courses.md) — related
- [GenAI availability produced no significant differential effect on final grades in more GenAI-susceptible courses relative to less susceptible ones](genai-availability-no-significant-grade-effect-susceptible-courses.md) — related
- [The share of students earning at least an A rises in more susceptible courses after ChatGPT under the preferred bound, but the shift fails parallel trends and is read as descriptive, not causal](at-least-a-share-increase-unstable-genai.md) — related
- [AI assistance reduces subjective mental effort across all tasks even when it does not reduce completion time, dissociating time and effort](ai-effort-reduction-time-effort-dissociation.md) — related

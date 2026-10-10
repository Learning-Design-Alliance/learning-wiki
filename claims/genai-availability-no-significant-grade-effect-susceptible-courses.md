---
type: claim
title: GenAI availability produced no significant differential effect on final grades in more GenAI-susceptible courses relative to less susceptible ones
description: GenAI availability produced no significant differential effect on final grades in more GenAI-susceptible courses relative to less susceptible ones
id: genai-availability-no-significant-grade-effect-susceptible-courses
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
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

# GenAI availability produced no significant differential effect on final grades in more GenAI-susceptible courses relative to less susceptible ones

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Comparing post-AI to pre-COVID periods, the grade difference between fully susceptible and fully non-susceptible courses was 0.03 grade points (SE = 0.052, not significant), with the bounded estimate ranging 0.030–0.045. [→ Dumlao 2026](#dumlao-2026)

## Evidence

### Dumlao 2026

Dumlao, J. M. Z., Wang, M., Xie, Z., Hu, J., Bar, I., Chaney, G., III, Gold, H., & Teplitskiy, M. (2026). Generative AI Availability, Grades, and Student Satisfaction at a Large University. arXiv. https://arxiv.org/abs/2607.21534

`q2 · i?` · `causal · r2`

Difference-in-differences analysis of administrative grade records from a large U.S. university (fall 2016–fall 2025), using a TWFE model with course, student, and semester fixed effects and a COVID-window interaction. The preferred estimate was "0.03 (SE = 0.052, n.s.) grade points"; the persistent-COVID bound was 0.045 (SE = 0.026, p < 0.1).

> "Comparing post-AI to the pre-COVID period, the difference between final grades in fully susceptible (Susceptibilityc = 1) and fully non-susceptible (Susceptibilityc = 0) courses was 0.03 (SE = 0.052, n.s.) grade points on average."

## Discussion


## Related Claims
- [The share of students earning at least an A rises in more susceptible courses after ChatGPT under the preferred bound, but the shift fails parallel trends and is read as descriptive, not causal](at-least-a-share-increase-unstable-genai.md) — related
- [Positive average grade effects appear only under COVID-laden treatment anchors, indicating such readings reflect the COVID shock rather than ChatGPT](covid-laden-anchors-produce-spurious-positive-grade-effect.md) — related
- [More GenAI-susceptible courses show no raised grade floor after ChatGPT: passing-margin and failing/withdrawal probabilities are null under both COVID assumptions](no-raised-grade-floor-genai-susceptible-courses.md) — related
- [Effects of GenAI availability on self-reported understanding are insignificant; effects on interest are significant only under the transient-COVID assumption](genai-satisfaction-understanding-null-interest-assumption-dependent.md) — related
- [Grade effects of GenAI availability do not differ across terciles of students' prior academic preparation, robust across multiple ability proxies](null-grade-effects-across-prior-performance-terciles.md) — related

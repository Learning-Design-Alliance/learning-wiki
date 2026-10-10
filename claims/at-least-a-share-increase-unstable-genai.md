---
type: claim
title: The share of students earning at least an A rises in more susceptible courses after ChatGPT under the preferred bound, but the shift fails parallel trends and is read as descriptive, not causal
description: The share of students earning at least an A rises in more susceptible courses after ChatGPT under the preferred bound, but the shift fails parallel trends and is read as descriptive, not causal
id: at-least-a-share-increase-unstable-genai
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

# The share of students earning at least an A rises in more susceptible courses after ChatGPT under the preferred bound, but the shift fails parallel trends and is read as descriptive, not causal

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` The probability of earning at least an A rises by 0.107 (SE = 0.046, p < 0.05) under the preferred post-AI bound, but falls to a non-significant 0.030 under the conservative net-COVID bound and fails the parallel-trends test. [→ Dumlao 2026](#dumlao-2026)

## Evidence

### Dumlao 2026

Dumlao, J. M. Z., Wang, M., Xie, Z., Hu, J., Bar, I., Chaney, G., III, Gold, H., & Teplitskiy, M. (2026). Generative AI Availability, Grades, and Student Satisfaction at a Large University. arXiv. https://arxiv.org/abs/2607.21534

`q2 · i?` · `causal · r2`

Grade-distribution DiD on the at-least-A threshold indicator. The authors state the shift "is not robustly identified in our data": the net-COVID estimate is 0.030 (SE = 0.018, n.s.), and the threshold fails parallel trends (p = 0.002 COVID-excluded).

> "The probability of earning at least an A rises by 0.107 under the preferred post-AI bound (SE = 0.046,p <0.05), close to the 13 percentage point A-share increase Chirikov (2026a) reports."

## Discussion


## Related Claims
- [More GenAI-susceptible courses show no raised grade floor after ChatGPT: passing-margin and failing/withdrawal probabilities are null under both COVID assumptions](no-raised-grade-floor-genai-susceptible-courses.md) — related
- [GenAI availability produced no significant differential effect on final grades in more GenAI-susceptible courses relative to less susceptible ones](genai-availability-no-significant-grade-effect-susceptible-courses.md) — related
- [Positive average grade effects appear only under COVID-laden treatment anchors, indicating such readings reflect the COVID shock rather than ChatGPT](covid-laden-anchors-produce-spurious-positive-grade-effect.md) — related
- [Effects of GenAI availability on self-reported understanding are insignificant; effects on interest are significant only under the transient-COVID assumption](genai-satisfaction-understanding-null-interest-assumption-dependent.md) — related

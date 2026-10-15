---
type: claim
title: Gains from verified AI materials are concentrated in the bottom quintile, which accounts for roughly three-quarters of the average effect
description: Gains from verified AI materials are concentrated in the bottom quintile, which accounts for roughly three-quarters of the average effect
id: gains-bottom-quintile-verified-ai
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: dang-2026
    resource: "https://doi.org/10.48550/arxiv.2610.07097"
    title: "Dang, C. T., & Nguyen, A. (2026). Verified, not generated: expert-verified AI study materials and the distribution of learning gains in a university course. https://arxiv.org/abs/2610.07097 [doi:10.48550/arxiv.2610.07097](https://doi.org/10.48550/arxiv.2610.07097)"
    author: "Dang, C. T., & Nguyen, A."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: dang-2026-2
    resource: "https://doi.org/10.48550/arxiv.2610.07097"
    title: "Dang, C. T., & Nguyen, A. (2026). Verified, not generated: expert-verified AI study materials and the distribution of learning gains in a university course. https://arxiv.org/abs/2610.07097. [doi:10.48550/arxiv.2610.07097](https://doi.org/10.48550/arxiv.2610.07097)"
    author: "Dang, C. T., & Nguyen, A."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Gains from verified AI materials are concentrated in the bottom quintile, which accounts for roughly three-quarters of the average effect

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`

## Subclaims
`q2 i?` Quantile difference-in-differences shows a gain of 11.0 marks at the 10th percentile (95% interval 5.0 to 13.0), 5.0 marks at the 20th, and estimates near zero from the 30th percentile upward. [→ Dang 2026](#dang-2026)
`q2 i?` Quintile decomposition attributes roughly three-quarters of the 2.34-mark average to the bottom quintile, whose difference-in-differences is 8.9 marks. [→ Dang 2026 (2)](#dang-2026-2)

## Evidence

### Dang 2026

Dang, C. T., & Nguyen, A. (2026). Verified, not generated: expert-verified AI study materials and the distribution of learning gains in a university course. https://arxiv.org/abs/2610.07097 [doi:10.48550/arxiv.2610.07097](https://doi.org/10.48550/arxiv.2610.07097)

`q2 · i?` · `causal · r2`

Quantile difference-in-differences at deciles with 95% intervals from 1,000 student-level bootstrap resamples, reported in the distributional results and Fig. 2b. Only the 10th-percentile estimate is bounded away from zero.

> "The gain is 11.0 marks at the 10th percentile (95% interval 5.0 to 13.0) and 5.0 marks at the 20th (−1.0 to 10.0), and estimates from the 30th percentile upward are close to zero."

### Dang 2026 (2)

Dang, C. T., & Nguyen, A. (2026). Verified, not generated: expert-verified AI study materials and the distribution of learning gains in a university course. https://arxiv.org/abs/2610.07097. [doi:10.48550/arxiv.2610.07097](https://doi.org/10.48550/arxiv.2610.07097)

`q2 · i?` · `causal · r2`

Quintile decomposition of the average effect in the same distributional analysis, supporting hypothesis H2 that gains concentrate in the lower tail and attenuate toward the upper tail.

> "Decomposing the average by quintile of each cohort’s distribution attributes roughly three-quarters of the 2.34 marks to the bottom quintile, whose difference-in-differences is 8.9 marks, and almost none to the top three."

## Discussion


## Related Claims
- [The average effect of verified AI materials attenuates when the lowest pre-intervention marks are removed, while the threshold effect at the upper-second boundary is robust](average-effect-fragile-threshold-robust.md) — related
- [Access to expert-verified AI study materials is associated with a 2.34-mark difference-in-differences advantage on a 50-mark examination component, reflecting protection from a decline rather than a rise](did-2-34-mark-advantage-verified-ai-materials.md) — a broader claim this one bears on
- [Chatbot treatment effects on final grades were concentrated between the 35th and 75th quantiles of the course grade distribution](chatbot-quantile-effects-middle-distribution.md) — related
- [School-based intelligent environment support shows an inverted U-shaped quantile pattern, stronger at lower-to-middle competence levels](intelligent-environment-support-inverted-u-quantile.md) — related

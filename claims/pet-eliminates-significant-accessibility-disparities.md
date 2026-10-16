---
type: claim
title: After PET normalization, no statistically significant performance differences remain between user cohorts
description: After PET normalization, no statistically significant performance differences remain between user cohorts
id: pet-eliminates-significant-accessibility-disparities
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: lier-jin-2026
    resource: "https://doi.org/10.48550/arxiv.2608.08942"
    title: "Lier Jin, Lan Hu, Binqi Shen, Hanyu Cai, and Yuting Xin. (2026). Same Question, Different Answer? Measuring and Mitigating Prompt Privilege for Equitable AI Access. https://arxiv.org/abs/2608.08942 [doi:10.48550/arxiv.2608.08942](https://doi.org/10.48550/arxiv.2608.08942)"
    author: Lier Jin, Lan Hu, Binqi Shen, Hanyu Cai, and Yuting Xin
    q: 2
    i: "?"
    kind: causal
    rigour: 1
  - id: lier-jin-2026-2
    resource: "https://arxiv.org/abs/2608.08942"
    title: "Lier Jin, Lan Hu, Binqi Shen, Hanyu Cai, and Yuting Xin. (2026). Same Question, Different Answer? Measuring and Mitigating Prompt Privilege for Equitable AI Access. https://arxiv.org/abs/2608.08942"
    author: Lier Jin, Lan Hu, Binqi Shen, Hanyu Cai, and Yuting Xin
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# After PET normalization, no statistically significant performance differences remain between user cohorts

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 causal `r1` · `q2`

## Subclaims
`q2 i?` The statistically significant baseline disparity between Low Literacy and Prompt Engineer cohorts is reduced by half after PET, and no pairwise comparison remains statistically significant. [→ Lier Jin 2026](#lier-jin-2026)
`q2 i?` Every post-PET confidence interval overlaps zero, indicating performance differences between cohorts are no longer distinguishable from sampling variability. [→ Lier Jin 2026 (2)](#lier-jin-2026-2)

## Evidence

### Lier Jin 2026

Lier Jin, Lan Hu, Binqi Shen, Hanyu Cai, and Yuting Xin. (2026). Same Question, Different Answer? Measuring and Mitigating Prompt Privilege for Equitable AI Access. https://arxiv.org/abs/2608.08942 [doi:10.48550/arxiv.2608.08942](https://doi.org/10.48550/arxiv.2608.08942)

`q2 · i?` · `causal · r1`

Post-normalization pairwise comparison of GPT-5.4-mini accuracy across cohorts on MedQA. Prior to normalization the Low Literacy and Prompt Engineer cohorts exhibited a statistically significant difference; after applying PET, this disparity is reduced by half, and no pairwise comparison remains statistically significant.

> "After applying PET, this disparity is reduced by half, and no pairwise comparison remains statistically significant."

### Lier Jin 2026 (2)

Lier Jin, Lan Hu, Binqi Shen, Hanyu Cai, and Yuting Xin. (2026). Same Question, Different Answer? Measuring and Mitigating Prompt Privilege for Equitable AI Access. https://arxiv.org/abs/2608.08942

`q2 · i?` · `causal · r1`

Pairwise accuracy differences with 95% bootstrap confidence intervals after PET normalization. Every post-PET confidence interval overlaps zero, indicating that performance differences between user cohorts are no longer distinguishable from sampling variability; equivalence beyond non-significance was not tested.

> "As shown in Table IV, every post-PET confidence interval overlaps zero, indicating that performance differences between user cohorts are no longer distinguishable from sampling variability."

## Discussion


## Related Claims
- [LLM accuracy increases monotonically with prompt sophistication across semantically equivalent medical questions, with Low Literacy users scoring significantly below Prompt Engineer users](prompt-privilege-monotonic-accuracy-gap-medqa.md) — related
- [Applying PET raises accuracy for every user cohort, with the largest gain for the Low Literacy cohort](pet-raises-accuracy-all-cohorts-largest-low-literacy-gain.md) — related

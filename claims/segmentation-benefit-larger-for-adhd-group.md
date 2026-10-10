---
type: claim
title: Segmentation yields a larger performance benefit for participants with ADHD than for those without, though the interaction term was not statistically significant
description: Segmentation yields a larger performance benefit for participants with ADHD than for those without, though the interaction term was not statistically significant
id: segmentation-benefit-larger-for-adhd-group
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: mixed
sources:
  - id: veronica-pimenova-2026
    resource: "https://arxiv.org/abs/2607.24612"
    title: "Veronica Pimenova, Chris Lee, Baramee Bhakdibhumi, Simon Chu, and Andrew Begel. (2026). Leveling the Playing Field: Temporal Video Segmentation for Individuals with ADHD in Computing Education. https://arxiv.org/abs/2607.24612"
    author: Veronica Pimenova, Chris Lee, Baramee Bhakdibhumi, Simon Chu, and Andrew Begel
    q: 3
    i: 3
    kind: causal
    rigour: 1
  - id: veronica-pimenova-2026-2
    resource: "https://arxiv.org/abs/2607.24612"
    title: "Veronica Pimenova, Chris Lee, Baramee Bhakdibhumi, Simon Chu, and Andrew Begel. (2026). Leveling the Playing Field: Temporal Video Segmentation for Individuals with ADHD in Computing Education. https://arxiv.org/abs/2607.24612"
    author: Veronica Pimenova, Chris Lee, Baramee Bhakdibhumi, Simon Chu, and Andrew Begel
    q: 3
    i: 3
    kind: causal
    rigour: 2
---

# Segmentation yields a larger performance benefit for participants with ADHD than for those without, though the interaction term was not statistically significant

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1`–`r2` · `q3` · `i3` large

## Subclaims
`q3 i3` The error reduction under segmentation was large for the ADHD group (d=0.85) and medium for the control group (d=0.66), while the Seg×ADHD interaction was not significant (p=.232). [→ Veronica Pimenova 2026](#veronica-pimenova-2026)
`q3 i3` The hesitation reduction under segmentation was large for the ADHD group (d=1.14) and medium for the control group (d=0.72), while the Seg×ADHD interaction was not significant (p=.242). [→ Veronica Pimenova 2026 (2)](#veronica-pimenova-2026-2)

## Evidence

### Veronica Pimenova 2026

Veronica Pimenova, Chris Lee, Baramee Bhakdibhumi, Simon Chu, and Andrew Begel. (2026). Leveling the Playing Field: Temporal Video Segmentation for Individuals with ADHD in Computing Education. https://arxiv.org/abs/2607.24612

`q3 · i3` · `causal · r1`

GLMM simple-effects analysis on Medium and Hard tasks (N=104 observations). The article reports a "large effect (𝑑> 0.8)" for participants with ADHD at d=0.85 and a smaller control-group effect at d=0.66, describing the standardized benefit as nearly 30% stronger.

> "Analysis of simple effects indicated that the reduction in errors for the ADHD group was characterized by a large magnitude (Ratio = 7.75,𝑑= 0.85,𝑝<. 001), whereas the effect for the control group was notably smaller (Ratio = 3.33,𝑑= 0.66,𝑝=. 009)."

### Veronica Pimenova 2026 (2)

Veronica Pimenova, Chris Lee, Baramee Bhakdibhumi, Simon Chu, and Andrew Begel. (2026). Leveling the Playing Field: Temporal Video Segmentation for Individuals with ADHD in Computing Education. https://arxiv.org/abs/2607.24612

`q3 · i3` · `causal · r2`

Simple-effects table (Table 8) of segmentation benefit by group on hesitations: the ADHD group's rate ratio was 4.70 with d=1.14 (Large); the control group's was 2.71 with d=0.72 (Medium).

> "HesitationsControl (Non-ADHD) 2.71 .010* 0.72 Medium ADHD Group 4.70 <.001*** 1.14 Large"

## Discussion


## Learner Variables
- [Attention](../learner-variables/attention.md) — moderator: an instructional effect differs with it

## Related Claims
- [ADHD medication status shows no significant interaction with segmentation, though medicated participants made fewer hesitations](medication-status-segmentation-interaction-null.md) — related
- [Segmented videos reduce hesitations for participants with ADHD by approximately 79% compared to non-segmented videos](segmentation-reduces-hesitations-adhd-participants.md) — related

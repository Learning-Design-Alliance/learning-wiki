---
type: claim
title: "Segmented videos reduce hesitations for participants with ADHD by approximately 79% compared to non-segmented videos"
description: "Segmented videos reduce hesitations for participants with ADHD by approximately 79% compared to non-segmented videos"
id: segmentation-reduces-hesitations-adhd-participants
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: veronica-pimenova-2026
    resource: "https://doi.org/10.48550/arxiv.2607.24612"
    title: "Veronica Pimenova, Chris Lee, Baramee Bhakdibhumi, Simon Chu, and Andrew Begel. (2026). Leveling the Playing Field: Temporal Video Segmentation for Individuals with ADHD in Computing Education. https://arxiv.org/abs/2607.24612 [doi:10.48550/arxiv.2607.24612](https://doi.org/10.48550/arxiv.2607.24612)"
    author: Veronica Pimenova, Chris Lee, Baramee Bhakdibhumi, Simon Chu, and Andrew Begel
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# Segmented videos reduce hesitations for participants with ADHD by approximately 79% compared to non-segmented videos

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q3`

## Subclaims
`q3 i?` Participants with ADHD exhibited approximately 79% fewer hesitations in the segmented condition than in the non-segmented condition. [→ Veronica Pimenova 2026](#veronica-pimenova-2026)

## Evidence

### Veronica Pimenova 2026

Veronica Pimenova, Chris Lee, Baramee Bhakdibhumi, Simon Chu, and Andrew Begel. (2026). Leveling the Playing Field: Temporal Video Segmentation for Individuals with ADHD in Computing Education. https://arxiv.org/abs/2607.24612 [doi:10.48550/arxiv.2607.24612](https://doi.org/10.48550/arxiv.2607.24612)

`q3 · i?` · `causal · r2`

Negative Binomial GLMM of hesitation counts for the ADHD subgroup (n=68 observations, 17 participants). The article reports a highly significant negative effect (β=-1.54, SE=0.29, z=-5.37, p<.001) with an Incident Rate Ratio of 0.214, indicating "approximately 79% fewer hesitations". No standardized effect size is printed for this model, so no magnitude is coded. The article's separate simple-effects table on Medium and Hard tasks (Table 8) prints d = 1.14 for the ADHD group's hesitation reduction; that is a different analysis, recorded on [the ADHD-interaction claim](segmentation-benefit-larger-for-adhd-group.md).

> "By exponentiating the coefficient, we calculated an Incident Rate Ratio (IRR) of0 .214, indicating that participants in the segmented condition exhibited approximately 79% fewer hesitations than those in the non-segmented condition."

## Discussion

## Learner Variables
- [Attention](../learner-variables/attention.md) — outcome: instruction changes it

## Related Claims

- [Segmenting Improves Multimedia Learning](segmenting-improves-multimedia-learning.md) — the general claim this finding bears on, with the studies behind it
- [ADHD medication status shows no significant interaction with segmentation, though medicated participants made fewer hesitations](medication-status-segmentation-interaction-null.md) — related
- [Segmentation reduces errors and hesitations for participants with and without ADHD, with larger point estimates for the ADHD group but no significant segmentation-by-ADHD interaction](segmentation-benefit-larger-for-adhd-group.md) — related
- [Task difficulty increases hesitations, with significantly more hesitations on Medium and Hard tasks than Easy tasks](task-difficulty-increases-hesitations-scratch-videos.md) — related

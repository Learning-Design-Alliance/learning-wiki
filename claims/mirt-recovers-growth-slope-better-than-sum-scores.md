---
type: claim
title: In a three-timepoint simulation, MIRT-based scores recover true linear growth slope parameters better than sum scores and unidimensional IRT approaches, which understate the slope
description: In a three-timepoint simulation, MIRT-based scores recover true linear growth slope parameters better than sum scores and unidimensional IRT approaches, which understate the slope
id: mirt-recovers-growth-slope-better-than-sum-scores
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: moderate
sources:
  - id: kuhfeld-2020
    resource: "https://www.edworkingpapers.com/ai20-193"
    title: "Kuhfeld, Megan, and James Soland. (2020). Estimating Student Growth on Psychological and Social-emotional Constructs: A Comparison of Multiple Scoring Approaches. EdWorkingPaper No. 20-193. https://www.edworkingpapers.com/ai20-193"
    author: Kuhfeld, Megan, and James Soland
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# In a three-timepoint simulation, MIRT-based scores recover true linear growth slope parameters better than sum scores and unidimensional IRT approaches, which understate the slope

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` In simulated three-timepoint Likert data, non-MIRT scoring (sum scores and unidimensional IRT) understates the true linear slope, in some cases by almost half the magnitude, while MIRT estimates overstate it only slightly. [→ Kuhfeld 2020](#kuhfeld-2020)

## Evidence

### Kuhfeld 2020

Kuhfeld, Megan, and James Soland. (2020). Estimating Student Growth on Psychological and Social-emotional Constructs: A Comparison of Multiple Scoring Approaches. EdWorkingPaper No. 20-193. https://www.edworkingpapers.com/ai20-193

`q2 · i?` · `design · r2`

Simulation Study 1 (100 replications per condition, 36 conditions varying items, N, growth, and difficulty) compared growth model parameter estimates across scoring approaches in flexMIRT and lavaan. The article reports that non-MIRT estimates "tend to understate the slope significantly, in some cases by almost half the magnitude of the slope."

> "Whereas the MIRT model estimates tend to overstate the slope slightly, the non-MIRT estimates tend to understate the slope significantly, in some cases by almost half the magnitude of the slope (e.g., true slope = .5 based on observed scores)."

## Discussion


## Related Claims
- [In the empirical growth mindset study, MIRT scoring yields substantively higher intercept and slope means and variances, including an intercept-slope covariance of .13 that is indistinguishable from zero under other approaches](empirical-mindset-mirt-higher-means-variances-covariance.md) — related
- [In a four-timepoint quadratic-growth simulation, the MIRT model marginally outperforms sum score and cross-sectional models for slope and quadratic means and much better recovers intercept and slope variances](mirt-better-quadratic-growth-recovery-four-timepoints.md) — related
- [Multidimensional IRT scores that account for latent variable covariances over time produce better recovery of growth parameters in longitudinal growth models than sum scores and other IRT approaches](multidimensional-irt-covariance-scores-better-growth-recovery.md) — a broader claim this one bears on
- [Standardized sum scores greatly compress individual differences in simulated growth trajectories, while only MIRT scores capture the wide variation in true trajectories](sum-scores-compress-growth-trajectory-variability.md) — related
- [Correlations between estimated and true scores diminish over time mainly with easy items, especially with a true slope of .5 and only four items, likely due to ceiling effects](score-true-correlations-diminish-easy-items-ceiling.md) — related

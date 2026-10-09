---
type: claim
title: MAB assignment overestimates effect sizes for normally distributed rewards, with greater overestimation for smaller true effects
description: MAB assignment overestimates effect sizes for normally distributed rewards, with greater overestimation for smaller true effects
id: mab-overestimates-effect-sizes
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: moderate
sources:
  - id: rafferty-2019
    resource: "https://jedm.educationaldatamining.org/index.php/JEDM/article/view/357"
    title: "Rafferty, A. N., Ying, H., & Williams, J. J. (2019). Statistical Consequences of using Multi-armed Bandits to Conduct Adaptive Educational Experiments. Journal of Educational Data Mining, Volume 11, No 1. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/357"
    author: "Rafferty, A. N., Ying, H., & Williams, J. J."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# MAB assignment overestimates effect sizes for normally distributed rewards, with greater overestimation for smaller true effects

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` With a true effect size of 0.2, prior-between simulations measured an average effect size of 0.30 at sample size m; a true effect of 0.8 was measured as 0.93. [→ Rafferty 2019](#rafferty-2019)

## Evidence

### Rafferty 2019

Rafferty, A. N., Ying, H., & Williams, J. J. (2019). Statistical Consequences of using Multi-armed Bandits to Conduct Adaptive Educational Experiments. Journal of Educational Data Mining, Volume 11, No 1. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/357

`q2 · i?` · `causal · r2`

Simulation measurement of effect sizes from MAB-collected data for normally distributed rewards. The article reports "an average effect size of 0.30" for a true 0.2 and 0.93 for a true 0.8, attributing overestimation to measurement errors in condition means from adaptive assignment rather than filtering of nonsignificant runs.

> "for small actual effect size of0.2, prior-between simula- tions found an average effect size of 0.30 with sample size m, while simulations with the large effect size of0.8 found average effect size0.93."

## Discussion


## Related Claims
- [MAB assignment yields higher average rewards (student outcomes) than uniform random assignment during experiments](mab-assignment-higher-average-student-rewards.md) — related
- [MAB (Thompson sampling) assignment reduces statistical power relative to uniform random assignment, requiring roughly doubled sample sizes](mab-assignment-reduces-experimental-power.md) — related
- [Over long horizons, MAB assignment places fewer total students in the less effective condition than a shorter uniform experiment followed by committing to one condition](mab-fewer-students-in-worse-condition-long-horizon.md) — related
- [An optimistic prior distribution partially mitigates MAB power loss without substantially reducing student benefits](optimistic-prior-mitigates-mab-power-loss.md) — related
- [MAB assignment increases the Type I (false positive) error rate above the nominal alpha level](mab-assignment-increases-type-i-error-rate.md) — related
- [Type S errors (significant findings in the wrong direction) are rare under both MAB and uniform assignment](mab-type-s-errors-rare.md) — related

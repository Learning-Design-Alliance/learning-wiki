---
type: claim
title: MAB assignment increases the Type I (false positive) error rate above the nominal alpha level
description: MAB assignment increases the Type I (false positive) error rate above the nominal alpha level
id: mab-assignment-increases-type-i-error-rate
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

# MAB assignment increases the Type I (false positive) error rate above the nominal alpha level

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` When conditions were equally effective, 9.4% of MAB-assigned simulations found a significant difference versus 5.0% under uniform assignment, both tested at alpha = 0.05. [→ Rafferty 2019](#rafferty-2019)

## Evidence

### Rafferty 2019

Rafferty, A. N., Ying, H., & Williams, J. J. (2019). Statistical Consequences of using Multi-armed Bandits to Conduct Adaptive Educational Experiments. Journal of Educational Data Mining, Volume 11, No 1. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/357

`q2 · i?` · `causal · r2`

Simulations with zero true effect size, aggregated across prior types, tested with standard tests at alpha = 0.05. The article reports "9.4% of simulations using MAB assignment found a difference" versus 5.0% under uniform assignment, so researchers using standard tests will underestimate their false positive rate.

> "5.0% of simulations using uniform assignment found a signiﬁcant differ- ence between conditions, while 9.4% of simulations using MAB assignment found a difference."

## Discussion


## Related Claims
- [MAB assignment yields higher average rewards (student outcomes) than uniform random assignment during experiments](mab-assignment-higher-average-student-rewards.md) — related
- [Over long horizons, MAB assignment places fewer total students in the less effective condition than a shorter uniform experiment followed by committing to one condition](mab-fewer-students-in-worse-condition-long-horizon.md) — related
- [MAB (Thompson sampling) assignment reduces statistical power relative to uniform random assignment, requiring roughly doubled sample sizes](mab-assignment-reduces-experimental-power.md) — related
- [MAB assignment overestimates effect sizes for normally distributed rewards, with greater overestimation for smaller true effects](mab-overestimates-effect-sizes.md) — related
- [Type S errors (significant findings in the wrong direction) are rare under both MAB and uniform assignment](mab-type-s-errors-rare.md) — related

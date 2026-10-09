---
type: claim
title: MAB assignment yields higher average rewards (student outcomes) than uniform random assignment during experiments
description: MAB assignment yields higher average rewards (student outcomes) than uniform random assignment during experiments
id: mab-assignment-higher-average-student-rewards
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
    kind: theoretical
    rigour: 3
---

# MAB assignment yields higher average rewards (student outcomes) than uniform random assignment during experiments

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q2`

## Subclaims
`q2 i?` Expected reward per student under MAB assignment approaches the success rate or mean of the more effective condition, exceeding uniform assignment. [→ Rafferty 2019](#rafferty-2019)

## Evidence

### Rafferty 2019

Rafferty, A. N., Ying, H., & Williams, J. J. (2019). Statistical Consequences of using Multi-armed Bandits to Conduct Adaptive Educational Experiments. Journal of Educational Data Mining, Volume 11, No 1. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/357

`q2 · i?` · `theoretical · r3`

Simulation results shown in Figure 4 comparing average reward per step for MAB versus uniform assignment across small, moderate, and large effect sizes for binary and normally distributed rewards. The article reports MAB "obtain[s] greater rewards than uniform", with reward increasing over time as the experiment runs.

> "MAB assignment does obtain greater rewards than uniform: the expected reward for a sin- gle student is close to the success rate of the more effective condition for binary rewards and approaches the mean of the better condition for normally distributed rewards a bit more slowly (Figure 4)."

## Discussion


## Related Claims
- [MAB (Thompson sampling) assignment reduces statistical power relative to uniform random assignment, requiring roughly doubled sample sizes](mab-assignment-reduces-experimental-power.md) — related
- [Over long horizons, MAB assignment places fewer total students in the less effective condition than a shorter uniform experiment followed by committing to one condition](mab-fewer-students-in-worse-condition-long-horizon.md) — related
- [MAB assignment overestimates effect sizes for normally distributed rewards, with greater overestimation for smaller true effects](mab-overestimates-effect-sizes.md) — related
- [MAB assignment increases the Type I (false positive) error rate above the nominal alpha level](mab-assignment-increases-type-i-error-rate.md) — related
- [Type S errors (significant findings in the wrong direction) are rare under both MAB and uniform assignment](mab-type-s-errors-rare.md) — related
- [An optimistic prior distribution partially mitigates MAB power loss without substantially reducing student benefits](optimistic-prior-mitigates-mab-power-loss.md) — related

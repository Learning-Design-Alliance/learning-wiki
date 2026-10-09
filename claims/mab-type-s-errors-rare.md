---
type: claim
title: Type S errors (significant findings in the wrong direction) are rare under both MAB and uniform assignment
description: Type S errors (significant findings in the wrong direction) are rare under both MAB and uniform assignment
id: mab-type-s-errors-rare
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

# Type S errors (significant findings in the wrong direction) are rare under both MAB and uniform assignment

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q2`

## Subclaims
`q2 i?` Overall, Type S errors occurred in fewer than 0.15% of simulations, with 0.13% for MAB and 0.00% for uniform assignment. [→ Rafferty 2019](#rafferty-2019)

## Evidence

### Rafferty 2019

Rafferty, A. N., Ying, H., & Williams, J. J. (2019). Statistical Consequences of using Multi-armed Bandits to Conduct Adaptive Educational Experiments. Journal of Educational Data Mining, Volume 11, No 1. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/357

`q2 · i?` · `theoretical · r3`

Simulation analysis of Type S errors, defined as significant findings in the direction opposite the true effect, across MAB and uniform assignment conditions. The article reports "Type S errors were rare (< 0.15%)" with no detected difference by assignment type.

> "Overall, Type S errors were rare (< 0.15%), and no difference by assignment type was detected: 0.13% of MAB simulations had a Type S error, and0.00% of uniform simulations had a Type S error."

## Discussion


## Related Claims
- [MAB assignment yields higher average rewards (student outcomes) than uniform random assignment during experiments](mab-assignment-higher-average-student-rewards.md) — related
- [MAB assignment increases the Type I (false positive) error rate above the nominal alpha level](mab-assignment-increases-type-i-error-rate.md) — related
- [MAB (Thompson sampling) assignment reduces statistical power relative to uniform random assignment, requiring roughly doubled sample sizes](mab-assignment-reduces-experimental-power.md) — related
- [MAB assignment overestimates effect sizes for normally distributed rewards, with greater overestimation for smaller true effects](mab-overestimates-effect-sizes.md) — related

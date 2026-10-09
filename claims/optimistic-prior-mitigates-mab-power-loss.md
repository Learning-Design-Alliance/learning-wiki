---
type: claim
title: An optimistic prior distribution partially mitigates MAB power loss without substantially reducing student benefits
description: An optimistic prior distribution partially mitigates MAB power loss without substantially reducing student benefits
id: optimistic-prior-mitigates-mab-power-loss
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

# An optimistic prior distribution partially mitigates MAB power loss without substantially reducing student benefits

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Prior above found a significant effect in 68% of simulations versus 62% for prior between and 53% for prior below, with only modest decreases in average reward. [→ Rafferty 2019](#rafferty-2019)

## Evidence

### Rafferty 2019

Rafferty, A. N., Ying, H., & Williams, J. J. (2019). Statistical Consequences of using Multi-armed Bandits to Conduct Adaptive Educational Experiments. Journal of Educational Data Mining, Volume 11, No 1. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/357

`q2 · i?` · `causal · r2`

Simulation comparison of three prior placements (above, between, below both condition means) with equal prior strength. The article reports "prior above found a significant effect in 68% of simulations", and attributes this to more equal early sampling because initial samples fall below the optimistic prior mean.

> "An optimistic prior ( prior above) led to higher power and more accurate eﬀect sizes than the other two priors: prior above found a signiﬁcant eﬀect in 68% of simulations, compared to 62% for prior between, and 53% for prior below."

## Discussion


## Related Claims
- [MAB assignment yields higher average rewards (student outcomes) than uniform random assignment during experiments](mab-assignment-higher-average-student-rewards.md) — related
- [MAB (Thompson sampling) assignment reduces statistical power relative to uniform random assignment, requiring roughly doubled sample sizes](mab-assignment-reduces-experimental-power.md) — related
- [MAB assignment overestimates effect sizes for normally distributed rewards, with greater overestimation for smaller true effects](mab-overestimates-effect-sizes.md) — related

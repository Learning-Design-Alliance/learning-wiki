---
type: claim
title: MAB (Thompson sampling) assignment reduces statistical power relative to uniform random assignment, requiring roughly doubled sample sizes
description: MAB (Thompson sampling) assignment reduces statistical power relative to uniform random assignment, requiring roughly doubled sample sizes
id: mab-assignment-reduces-experimental-power
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

# MAB (Thompson sampling) assignment reduces statistical power relative to uniform random assignment, requiring roughly doubled sample sizes

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` With a prior-between Thompson sampling MAB, power fell from an expected 0.80 to 0.57 for binary rewards and 0.49 for normally distributed rewards; doubling the sample size raised power to 0.79 and 0.69. [→ Rafferty 2019](#rafferty-2019)

## Evidence

### Rafferty 2019

Rafferty, A. N., Ying, H., & Williams, J. J. (2019). Statistical Consequences of using Multi-armed Bandits to Conduct Adaptive Educational Experiments. Journal of Educational Data Mining, Volume 11, No 1. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/357

`q2 · i?` · `causal · r2`

Simulation study of 500 repetitions per parameter set comparing Thompson sampling MAB versus uniform assignment, analyzed with t-tests and chi-squared tests at alpha = 0.05. The article reports power "decreased power from an expected 0.80 to 0.57" for binary and 0.49 for normal rewards, rising to 0.79 and 0.69 at doubled sample size.

> "MAB assignment without an optimistic or pessimistic prior ( prior between) decreased power from an expected 0.80 to 0.57 for binary rewards (Figure 1a) and0.49 for normally-distributed rewards (Figure 1c). Doubling the sample size raised power closer to the desired 0.80 (0.79 and 0.69 respectively)."

## Discussion


## Related Claims
- [MAB assignment yields higher average rewards (student outcomes) than uniform random assignment during experiments](mab-assignment-higher-average-student-rewards.md) — related
- [MAB assignment increases the Type I (false positive) error rate above the nominal alpha level](mab-assignment-increases-type-i-error-rate.md) — related
- [An optimistic prior distribution partially mitigates MAB power loss without substantially reducing student benefits](optimistic-prior-mitigates-mab-power-loss.md) — related
- [MAB assignment overestimates effect sizes for normally distributed rewards, with greater overestimation for smaller true effects](mab-overestimates-effect-sizes.md) — related
- [Over long horizons, MAB assignment places fewer total students in the less effective condition than a shorter uniform experiment followed by committing to one condition](mab-fewer-students-in-worse-condition-long-horizon.md) — related
- [Type S errors (significant findings in the wrong direction) are rare under both MAB and uniform assignment](mab-type-s-errors-rare.md) — related
- [A multi-armed bandit controller achieves scoring accuracy comparable to exhaustive grid search while reducing LLM calls by 78.4% and token consumption by 72.8%](mab-prompt-selection-reduces-aes-costs.md) — related

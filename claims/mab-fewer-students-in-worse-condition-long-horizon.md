---
type: claim
title: Over long horizons, MAB assignment places fewer total students in the less effective condition than a shorter uniform experiment followed by committing to one condition
description: Over long horizons, MAB assignment places fewer total students in the less effective condition than a shorter uniform experiment followed by committing to one condition
id: mab-fewer-students-in-worse-condition-long-horizon
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
    rigour: 3
---

# Over long horizons, MAB assignment places fewer total students in the less effective condition than a shorter uniform experiment followed by committing to one condition

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r3` · `q2`

## Subclaims
`q2 i?` For normally distributed rewards at 2m students, MAB assigned an average of 19 of 256 students (7.5%) to the worse condition, versus 64 (25%) for revise-always and 77 (30%) for revise-if-different. [→ Rafferty 2019](#rafferty-2019)

## Evidence

### Rafferty 2019

Rafferty, A. N., Ying, H., & Williams, J. J. (2019). Statistical Consequences of using Multi-armed Bandits to Conduct Adaptive Educational Experiments. Journal of Educational Data Mining, Volume 11, No 1. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/357

`q2 · i?` · `causal · r3`

Large-sample simulations (2m, 6m, 11m students, moderate effect size) comparing Thompson sampling MAB throughout against uniform assignment for the first m students then committing to a condition. The article reports MAB "assigned an average of 19 out of 256 students" to the worse condition, and MAB also had the highest average reward per student.

> "for normally distributed rewards, an average of 19 out of 256 students were assigned to the worse condition by MAB assignment ( 7.5% of all simulated stu- dents), while revise always assigned an average of 64 students (25%) to this condition andrevise if diﬀerent assigned an average of 77 students (30%) to this condition."

## Discussion


## Related Claims
- [MAB assignment yields higher average rewards (student outcomes) than uniform random assignment during experiments](mab-assignment-higher-average-student-rewards.md) — related
- [MAB assignment increases the Type I (false positive) error rate above the nominal alpha level](mab-assignment-increases-type-i-error-rate.md) — related
- [MAB (Thompson sampling) assignment reduces statistical power relative to uniform random assignment, requiring roughly doubled sample sizes](mab-assignment-reduces-experimental-power.md) — related
- [MAB assignment overestimates effect sizes for normally distributed rewards, with greater overestimation for smaller true effects](mab-overestimates-effect-sizes.md) — related
- [A multi-armed bandit controller achieves scoring accuracy comparable to exhaustive grid search while reducing LLM calls by 78.4% and token consumption by 72.8%](mab-prompt-selection-reduces-aes-costs.md) — related

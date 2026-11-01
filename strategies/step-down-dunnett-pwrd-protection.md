---
type: strategy
id: step-down-dunnett-pwrd-protection
title: Combine PWRD aggregation with a standard analysis method via the step-down Dunnett procedure to protect against power loss if the theory of change fails
description: The article recommends implementing PWRD aggregation simultaneously with a standard method such as flat weighting or exit observation analysis using the step-down Dunnett procedure.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-01
sources:
  - id: timothy-lycurgus-2022
    resource: "https://doi.org/10.1080/19345747.2022.2142178"
    title: "Timothy Lycurgus, Ben B. Hansen, and Mark White. (2022). Conjuring Power from a Theory of Change: The PWRD Method for Trials with Anticipated Variation in Effects. Journal of Research on Educational Effectiveness. https://doi.org/10.1080/19345747.2022.2142178"
    author: Timothy Lycurgus, Ben B. Hansen, and Mark White
---

# Combine PWRD aggregation with a standard analysis method via the step-down Dunnett procedure to protect against power loss if the theory of change fails

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 theoretical), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The article recommends implementing PWRD aggregation simultaneously with a standard method such as flat weighting or exit observation analysis using the step-down Dunnett procedure. As the article states, "Given the theory of the intervention holds, PWRD aggregation yields substantially more power than extant alternatives; if instead effects accumulate in a manner different than that hypothesized by the theory of the intervention, the standard method protects against a large loss of power." The procedure maintains valid Type I error rates while requiring only a consistent estimate of the statistics' covariance, and provides power close to either correlated statistic. A third test statistic using a different working model may also be included.

## Design Implications

### Context
#### Requirements
- A consistent estimate of the test statistics' covariance
#### Constraints
- Offers less power than PWRD aggregation alone when the theory of change holds

### Target Learners
- Researchers analyzing education RCTs with longitudinal outcomes

### Target Learning Goals
- Hypothesis testing robust to misspecification of the intervention's theory of change

### Affordances
- [Pwrd Aggregation Method](../research-methods/pwrd-aggregation-power-maximizing-weighting-for-repeated-measurements-with-delayed-effects.md)

## Claims

- [Under within-cluster interference (a negative spillover effect on non-eligible treatment students), PWRD aggregation's power advantage over traditional methods grows, roughly doubling power for large effect sizes](../claims/pwrd-advantage-under-spillover.md) [+W]
- [In simulations where the theory of change holds, PWRD aggregation outperforms standard analysis methods, with a 35-50% power increase for medium effect sizes](../claims/pwrd-increases-power-when-theory-holds.md) [+W]
- [When the theory of change entirely fails (effects neither stacked nor persistent), standard methods outperform PWRD aggregation but the improvement never exceeds 3%](../claims/pwrd-small-loss-when-theory-fails.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Timothy Lycurgus, Ben B. Hansen, and Mark White. (2022). Conjuring Power from a Theory of Change: The PWRD Method for Trials with Anticipated Variation in Effects. Journal of Research on Educational Effectiveness. https://doi.org/10.1080/19345747.2022.2142178

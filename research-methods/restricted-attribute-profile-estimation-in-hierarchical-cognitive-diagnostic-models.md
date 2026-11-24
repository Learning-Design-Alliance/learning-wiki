---
type: research-method
id: restricted-attribute-profile-estimation-in-hierarchical-cognitive-diagnostic-models
title: Restricted attribute-profile estimation in hierarchical cognitive diagnostic models
description: When a diagnostic assessment uses a restricted Q-matrix design and a latent class-based CDM is appropriate, attribute profile estimation should be confined to profiles that can exist under the assumed hierarchy.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-24
---

# Restricted attribute-profile estimation in hierarchical cognitive diagnostic models

> **Research Method** · [All research methods](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
When a diagnostic assessment uses a restricted Q-matrix design and a latent class-based CDM is appropriate, attribute profile estimation should be confined to profiles that can exist under the assumed hierarchy. The article concludes: "the attribute profile estimation should be restricted in the set which contains all permissible attribute profiles under the specified hierarchical structure, no matter using the frequentist estimation procedure or Bayesian estimation procedure." With the EM algorithm this can be achieved by setting the population probability of impermissible profiles to zero or dropping them, which also reduces latent classes, improves fit and item parameter estimation, and decreases required sample size and computing time.

## Accounts
<!-- How each source describes or uses the method -->
- **Restrict attribute profile estimation to the permissible profile set when a restricted Q-matrix design and attribute hierarchy are in place**: When a diagnostic assessment uses a restricted Q-matrix design and a latent class-based CDM is appropriate, attribute profile estimation should be confined to profiles that can exist under the assumed hierarchy. The article concludes: "the attribute profile estimation should be restricted in the set which contains all permissible attribute profiles under the specified hierarchical structure, no matter using the frequentist estimation procedure or Bayesian estimation procedure." With the EM algorithm this can be achieved by setting the population probability of impermissible profiles to zero or dropping them, which also reduces latent classes, improves fit and item parameter estimation, and decreases required sample size and computing time. (Tu et al. (2019))

### Claims
- [In simulations with a restricted Q-matrix design, restricted estimation yields higher pattern-wise classification agreement than unrestricted estimation across four CDMs and four attribute hierarchy structures](../claims/restricted-estimation-higher-par-simulation.md) [+M]
- [In the real data analysis, restricted estimation improves BIC for every model, while AIC shows a mixed pattern, and HDCM-H fits better than LCDM-H](../claims/real-data-bic-improvement-restricted.md) [+M]
- [Restricted estimation improves model fit and item parameter recovery in simulation, with the largest item-parameter gains for the saturated GDINA model](../claims/restricted-estimation-fit-rmse-simulation.md) [+M]

## Related Research Methods
-

## Key Sources
- Tu, D., Wang, S., Cai, Y., Douglas, J., & Chang, H.-H. (2019). Cognitive Diagnostic Models With Attribute Hierarchies: Model Estimation With a Restricted Q-Matrix Design. Applied Psychological Measurement, 43(4), 255-271. https://doi.org/10.1177/0146621618765721

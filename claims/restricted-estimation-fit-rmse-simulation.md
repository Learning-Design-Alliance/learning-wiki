---
type: claim
title: Restricted estimation improves model fit and item parameter recovery in simulation, with the largest item-parameter gains for the saturated GDINA model
description: Restricted estimation improves model fit and item parameter recovery in simulation, with the largest item-parameter gains for the saturated GDINA model
id: restricted-estimation-fit-rmse-simulation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-24
evidence_strength: moderate
newest_evidence: 2019
recheck_by: 2022
sources:
  - id: tu-2019
    resource: "https://doi.org/10.1177/0146621618765721"
    title: "Tu, D., Wang, S., Cai, Y., Douglas, J., & Chang, H.-H. (2019). Cognitive Diagnostic Models With Attribute Hierarchies: Model Estimation With a Restricted Q-Matrix Design. Applied Psychological Measurement, 43(4), 255-271. https://doi.org/10.1177/0146621618765721"
    author: "Tu, D., Wang, S., Cai, Y., Douglas, J., & Chang, H.-H."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: tu-2019-2
    resource: "https://doi.org/10.1177/0146621618765721"
    title: "Tu, D., Wang, S., Cai, Y., Douglas, J., & Chang, H.-H. (2019). Cognitive Diagnostic Models With Attribute Hierarchies: Model Estimation With a Restricted Q-Matrix Design. Applied Psychological Measurement, 43(4), 255-271. https://doi.org/10.1177/0146621618765721"
    author: "Tu, D., Wang, S., Cai, Y., Douglas, J., & Chang, H.-H."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Restricted estimation improves model fit and item parameter recovery in simulation, with the largest item-parameter gains for the saturated GDINA model

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2019 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2022**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Model fit improves under restricted estimation in every simulation condition evaluated by AIC and BIC. [→ Tu 2019](#tu-2019)
`q2 i?` Item parameter RMSE is similar for DINA under both procedures, slightly better for rRUM and ACDM under restriction, and much better for GDINA under restriction. [→ Tu 2019 (2)](#tu-2019-2)

## Evidence

### Tu 2019

Tu, D., Wang, S., Cai, Y., Douglas, J., & Chang, H.-H. (2019). Cognitive Diagnostic Models With Attribute Hierarchies: Model Estimation With a Restricted Q-Matrix Design. Applied Psychological Measurement, 43(4), 255-271. https://doi.org/10.1177/0146621618765721

`q2 · i?` · `causal · r2`

Simulation study comparing mean AIC and BIC over 100 replications for restricted versus unrestricted MMLE estimation of four CDMs under four attribute hierarchies. The article reports the directional finding; no effect size is printed.

> "An improvement of model fit can be observed by using the restricted estimation in each simulation condition."

### Tu 2019 (2)

Tu, D., Wang, S., Cai, Y., Douglas, J., & Chang, H.-H. (2019). Cognitive Diagnostic Models With Attribute Hierarchies: Model Estimation With a Restricted Q-Matrix Design. Applied Psychological Measurement, 43(4), 255-271. https://doi.org/10.1177/0146621618765721

`q2 · i?` · `causal · r2`

Simulation study of item parameter recovery via RMSE of correct response probabilities across items and replications, shown in Figure 3. The article attributes the model differences to complexity: GDINA produces 2^Kj possible estimates when unrestricted, which may contaminate estimates within permissible profiles.

> "For the DINA model, the two estimation methods both have good recovery of item parameters. The restricted method produces a slightly better result for the rRUM and the ACDM, and improved a lot for the GDINA, compared with the unrestricted estimation method."

## Discussion


## Related Claims
- [Under restricted estimation, even parsimonious models such as DINA produce reasonable classification results under attribute hierarchy, as shown in the real data analysis](dina-restricted-reasonable-classification.md) — related
- [In the real data analysis, restricted estimation improves BIC for every model, while AIC shows a mixed pattern, and HDCM-H fits better than LCDM-H](real-data-bic-improvement-restricted.md) — related
- [In simulations with a restricted Q-matrix design, restricted estimation yields higher pattern-wise classification agreement than unrestricted estimation across four CDMs and four attribute hierarchy structures](restricted-estimation-higher-par-simulation.md) — related

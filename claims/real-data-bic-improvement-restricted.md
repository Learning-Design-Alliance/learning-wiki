---
type: claim
title: In the real data analysis, restricted estimation improves BIC for every model, while AIC shows a mixed pattern, and HDCM-H fits better than LCDM-H
description: In the real data analysis, restricted estimation improves BIC for every model, while AIC shows a mixed pattern, and HDCM-H fits better than LCDM-H
id: real-data-bic-improvement-restricted
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

# In the real data analysis, restricted estimation improves BIC for every model, while AIC shows a mixed pattern, and HDCM-H fits better than LCDM-H

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2019 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2022**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` BIC improves under restricted estimation for each model, especially the more general models, but AIC shows a mixed effect across models. [→ Tu 2019](#tu-2019)
`q2 i?` HDCM with restricted estimation fits better than LCDM with restricted estimation. [→ Tu 2019 (2)](#tu-2019-2)

## Evidence

### Tu 2019

Tu, D., Wang, S., Cai, Y., Douglas, J., & Chang, H.-H. (2019). Cognitive Diagnostic Models With Attribute Hierarchies: Model Estimation With a Restricted Q-Matrix Design. Applied Psychological Measurement, 43(4), 255-271. https://doi.org/10.1177/0146621618765721

`q2 · i?` · `causal · r2`

Real data analysis comparing AIC and BIC for six CDMs under restricted versus unrestricted estimation on the 769-respondent syllogistic reasoning data (Table 2). The article attributes the BIC gain to the reduction in attribute profiles and corresponding item parameters; no effect size is printed.

> "Based on the BIC index, the model fit is improved when using the restriction estimation procedure for each of the models, especially for the more general model, while based on the AIC index there is a mixed effect across different models."

### Tu 2019 (2)

Tu, D., Wang, S., Cai, Y., Douglas, J., & Chang, H.-H. (2019). Cognitive Diagnostic Models With Attribute Hierarchies: Model Estimation With a Restricted Q-Matrix Design. Applied Psychological Measurement, 43(4), 255-271. https://doi.org/10.1177/0146621618765721

`q2 · i?` · `causal · r2`

Real data analysis comparing HDCM-H and LCDM-H fit indices on the syllogistic reasoning data. The article attributes the difference to the restricted kernel reducing item parameters, consistent with Templin and Bradshaw (2014).

> "The HDCM-H has a better fit than the LCDM-H, which is consistent with the finding from Templin and Bradshaw (2014), as it further reduces the number of item parameters due to the restricted kernel form."

## Discussion


## Related Claims
- [Under restricted estimation, even parsimonious models such as DINA produce reasonable classification results under attribute hierarchy, as shown in the real data analysis](dina-restricted-reasonable-classification.md) — related
- [In a real syllogistic reasoning analysis, unrestricted estimation assigns 40.7% to 89.5% of examinees to impermissible attribute profiles depending on the CDM](real-data-impermissible-rates.md) — related
- [Restricted estimation improves model fit and item parameter recovery in simulation, with the largest item-parameter gains for the saturated GDINA model](restricted-estimation-fit-rmse-simulation.md) — related

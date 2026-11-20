---
type: claim
title: A deep learning model predicted the economic achievement gap with strong fit (R2 0.860), and higher Directly Certified Percentage was associated with a smaller economic gap
description: A deep learning model predicted the economic achievement gap with strong fit (R2 0.860), and higher Directly Certified Percentage was associated with a smaller economic gap
id: georgia-economic-achievement-gap-model-findings
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: yichen-ma-2024
    resource: "https://doi.org/10.48550/arXiv.2402.01710"
    title: "Yichen Ma, Dima Nazzal. (2024). Exploring Educational Equity: A Machine Learning Approach to Unravel Achievement Disparities in Georgia. Originally published 2023. [doi:10.48550/arXiv.2402.01710](https://doi.org/10.48550/arXiv.2402.01710)"
    author: Yichen Ma, Dima Nazzal
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: yichen-ma-2024-2
    resource: "https://doi.org/10.48550/arXiv.2402.01710"
    title: "Yichen Ma, Dima Nazzal. (2024). Exploring Educational Equity: A Machine Learning Approach to Unravel Achievement Disparities in Georgia. Originally published 2023. [doi:10.48550/arXiv.2402.01710](https://doi.org/10.48550/arXiv.2402.01710)"
    author: Yichen Ma, Dima Nazzal
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# A deep learning model predicted the economic achievement gap with strong fit (R2 0.860), and higher Directly Certified Percentage was associated with a smaller economic gap

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The economic achievement gap model achieved an average R2 of 0.860 (SD 0.019) under 10-fold validation, with Directly Certified Percentage the most influential feature. [→ Yichen Ma 2024](#yichen-ma-2024)
`q2 i?` ICE plots showed the economic achievement gap shrinks as Directly Certified Percentage rises, with PPE Federal and instruction expenditure also negatively correlated with the gap. [→ Yichen Ma 2024 (2)](#yichen-ma-2024-2)

## Evidence

### Yichen Ma 2024

Yichen Ma, Dima Nazzal. (2024). Exploring Educational Equity: A Machine Learning Approach to Unravel Achievement Disparities in Georgia. Originally published 2023. [doi:10.48550/arXiv.2402.01710](https://doi.org/10.48550/arXiv.2402.01710)

`q2 · i?` · `associational · r2`

10-fold cross-validated deep learning model predicting the economic achievement gap (Table 9): MSE 114.518 (Sd 15.910), RMSE 10.676 (Sd 0.737), MAE 7.507 (Sd 0.593). The quote reports "The average 𝑅2 across the folds was 0.860 with an Sd of 0.019"; Directly Certified Percentage was the most influential feature, followed by PPE Federal.

> "The average 𝑅2 across the folds was 0.860 with an Sd of 0.019."

### Yichen Ma 2024 (2)

Yichen Ma, Dima Nazzal. (2024). Exploring Educational Equity: A Machine Learning Approach to Unravel Achievement Disparities in Georgia. Originally published 2023. [doi:10.48550/arXiv.2402.01710](https://doi.org/10.48550/arXiv.2402.01710)

`q2 · i?` · `associational · r2`

ICE plot analysis of feature effects on the economic gap (Figure 27). The quote states "with a higher Directly Certified Percentage, the economic achievement gap shrinks"; PPE Federal and instruction expenditure also showed negative correlations with flatter slopes.

> "The ICE plots for the economic achievement gap reveals that with a higher Directly Certified Percentage, the economic achievement gap shrinks."

## Discussion


## Related Claims
- [Directly Certified Percentage (free-lunch eligibility) was by far the most influential feature predicting achievement rates in all three deep learning models](directly-certified-percentage-most-influential-feature.md) — related
- [A deep learning model predicted the White-Black racial achievement gap with moderate fit (R2 0.574), and higher student achievement scores were associated with a larger achievement gap](georgia-racial-achievement-gap-model-findings.md) — related
- [Random Forest and Stacking Regressor explained about 69% of variability in Georgia math achievement rates, with deep learning models reaching R2 of 0.796](georgia-ml-models-predict-achievement-rates.md) — related

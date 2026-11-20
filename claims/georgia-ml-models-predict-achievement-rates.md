---
type: claim
title: "Random Forest and Stacking Regressor explained about 69% of variability in Georgia math achievement rates, with deep learning models reaching R2 of 0.796"
description: "Random Forest and Stacking Regressor explained about 69% of variability in Georgia math achievement rates, with deep learning models reaching R2 of 0.796"
id: georgia-ml-models-predict-achievement-rates
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

# Random Forest and Stacking Regressor explained about 69% of variability in Georgia math achievement rates, with deep learning models reaching R2 of 0.796

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Among general models, Random Forest achieved the highest R2 (0.693) and the Stacking Regressor 0.695 for predicting achievement rates. [→ Yichen Ma 2024](#yichen-ma-2024)
`q2 i?` Deep learning Model #2 slightly outperformed Models #1 and #3, with an R2 of 0.796 under 10-fold validation. [→ Yichen Ma 2024 (2)](#yichen-ma-2024-2)

## Evidence

### Yichen Ma 2024

Yichen Ma, Dima Nazzal. (2024). Exploring Educational Equity: A Machine Learning Approach to Unravel Achievement Disparities in Georgia. Originally published 2023. [doi:10.48550/arXiv.2402.01710](https://doi.org/10.48550/arXiv.2402.01710)

`q2 · i?` · `associational · r2`

Model comparison on Georgia school-level data (Table 4): Random Forest R2 0.693, Stacking Regressor R2 0.695, Decision Tree only 0.354. The quote names the winner: "the Random Forest model notably stood out, explaining approximately 69.3% of the variability".

> "Evaluating the performance metrics, the Random Forest model notably stood out, explaining approximately 69.3% of the variability in the dataset."

### Yichen Ma 2024 (2)

Yichen Ma, Dima Nazzal. (2024). Exploring Educational Equity: A Machine Learning Approach to Unravel Achievement Disparities in Georgia. Originally published 2023. [doi:10.48550/arXiv.2402.01710](https://doi.org/10.48550/arXiv.2402.01710)

`q2 · i?` · `associational · r2`

Deep learning models evaluated with 10-fold cross-validation (Table 5). The quote names the winner and its statistics: "surpassed Model #1 slightly"; Model #3 echoed Model #1's metrics (R2 0.793). The printed R2 SD for Model #2 is 0.024.

> "Model #2, however, surpassed Model #1 slightly, registering an MSE of 112.101 and an improved 𝑅2 of 0.796"

## Discussion


## Related Claims
- [A deep learning model predicted the economic achievement gap with strong fit (R2 0.860), and higher Directly Certified Percentage was associated with a smaller economic gap](georgia-economic-achievement-gap-model-findings.md) — related
- [Feature-based models (LLM-extracted features plus metadata in random forest and gradient boosting) outperform direct LLM estimation, dummy regressor, TF-IDF, and metadata-only benchmarks, with correlations up to r = .87](feature-based-llm-models-outperform-direct-estimation-and-benchmarks.md) — related

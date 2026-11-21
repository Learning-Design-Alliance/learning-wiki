---
type: claim
title: "The LOOP estimator provides an unbiased ATE estimate with greater precision than the Student's t-test when covariate imputation improves on mean imputation"
description: "The LOOP estimator provides an unbiased ATE estimate with greater precision than the Student's t-test when covariate imputation improves on mean imputation"
id: loop-estimator-unbiased-precise
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: siedahmed-2025
    resource: "https://doi.org/10.48550/arXiv.2502.10545"
    title: "Siedahmed, A., Pei, Y., Sales, A., Heffernan, N. T., Gagnon-Bartsch, J. A., Zhang, D., Schuetze, B. A., & Zengilowski, A. (2025). E-TRIALS: Empowering Data-Driven Decisions to Enhance Computer-Based Learning Platforms. arXiv. [doi:10.48550/arXiv.2502.10545](https://doi.org/10.48550/arXiv.2502.10545)"
    author: "Siedahmed, A., Pei, Y., Sales, A., Heffernan, N. T., Gagnon-Bartsch, J. A., Zhang, D., Schuetze, B. A., & Zengilowski, A."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: siedahmed-2025-2
    resource: "https://doi.org/10.48550/arXiv.2502.10545"
    title: "Siedahmed, A., Pei, Y., Sales, A., Heffernan, N. T., Gagnon-Bartsch, J. A., Zhang, D., Schuetze, B. A., & Zengilowski, A. (2025). E-TRIALS: Empowering Data-Driven Decisions to Enhance Computer-Based Learning Platforms. arXiv. [doi:10.48550/arXiv.2502.10545](https://doi.org/10.48550/arXiv.2502.10545)"
    author: "Siedahmed, A., Pei, Y., Sales, A., Heffernan, N. T., Gagnon-Bartsch, J. A., Zhang, D., Schuetze, B. A., & Zengilowski, A."
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: siedahmed-2025-3
    resource: "https://doi.org/10.48550/arXiv.2502.10545"
    title: "Siedahmed, A., Pei, Y., Sales, A., Heffernan, N. T., Gagnon-Bartsch, J. A., Zhang, D., Schuetze, B. A., & Zengilowski, A. (2025). E-TRIALS: Empowering Data-Driven Decisions to Enhance Computer-Based Learning Platforms. arXiv. [doi:10.48550/arXiv.2502.10545](https://doi.org/10.48550/arXiv.2502.10545)"
    author: "Siedahmed, A., Pei, Y., Sales, A., Heffernan, N. T., Gagnon-Bartsch, J. A., Zhang, D., Schuetze, B. A., & Zengilowski, A."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# The LOOP estimator provides an unbiased ATE estimate with greater precision than the Student's t-test when covariate imputation improves on mean imputation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In the two E-TRIALS experiments, both Regression and LOOP gave more precise estimates than the t-test, and only LOOP was unbiased. [→ Siedahmed 2025](#siedahmed-2025)
`q2 i?` Analytically, LOOP is unbiased regardless of the imputation algorithm, and outperforms the t-test whenever imputation improves beyond baseline mean imputation. [→ Siedahmed 2025 (2)](#siedahmed-2025-2)
`q2 i?` A classification permutation test found no strong evidence of treatment-control imbalance but residual covariate differences suggesting covariate adjustment remains necessary. [→ Siedahmed 2025 (3)](#siedahmed-2025-3)

## Evidence

### Siedahmed 2025

Siedahmed, A., Pei, Y., Sales, A., Heffernan, N. T., Gagnon-Bartsch, J. A., Zhang, D., Schuetze, B. A., & Zengilowski, A. (2025). E-TRIALS: Empowering Data-Driven Decisions to Enhance Computer-Based Learning Platforms. arXiv. [doi:10.48550/arXiv.2502.10545](https://doi.org/10.48550/arXiv.2502.10545)

`q2 · i?` · `causal · r2`

Reanalysis of the two E-TRIALS support-comparison experiments comparing three ATE estimators. The article reports "only LOOP offers an unbiased estimate"; e.g., Experiment 1 proximal SEs: t-test 0.0333, Regression 0.0290, LOOP 0.0316.

> "These findings confirm that while both Regression and LOOP provide more precise estimators compared to the student's t-test, only LOOP offers an unbiased estimate based on equation 10."

### Siedahmed 2025 (2)

Siedahmed, A., Pei, Y., Sales, A., Heffernan, N. T., Gagnon-Bartsch, J. A., Zhang, D., Schuetze, B. A., & Zengilowski, A. (2025). E-TRIALS: Empowering Data-Driven Decisions to Enhance Computer-Based Learning Platforms. arXiv. [doi:10.48550/arXiv.2502.10545](https://doi.org/10.48550/arXiv.2502.10545)

`q2 · i?` · `design · r2`

Mathematical derivation in the Methods section showing the leave-one-out potential outcomes estimator is unbiased (equation 10) and has reduced variance when the imputed m-i approximates m-i well; Random Forest is recommended for imputation.

> "the LOOP estimator outperformsˆτt-test as long as the imputation of potential outcomes improves beyond the baseline mean imputation approach."

### Siedahmed 2025 (3)

Siedahmed, A., Pei, Y., Sales, A., Heffernan, N. T., Gagnon-Bartsch, J. A., Zhang, D., Schuetze, B. A., & Zengilowski, A. (2025). E-TRIALS: Empowering Data-Driven Decisions to Enhance Computer-Based Learning Platforms. arXiv. [doi:10.48550/arXiv.2502.10545](https://doi.org/10.48550/arXiv.2502.10545)

`q2 · i?` · `causal · r2`

Classification permutation test of baseline covariate balance in the two experiments (p-values 0.196 and 0.124). The article reports "some degree of covariate difference remains," motivating covariate adjustment in the ATE estimation.

> "Table 3 shows that while there is no strong evidence of imbalance between the treatment and control groups, some degree of covariate difference remains, suggesting that covariate adjustment is still necessary."

## Discussion


## Related Claims
- [Fitting an imputation model with all covariates using only the small trial sample reduces precision relative to pretest-only adjustment](rct-only-all-covariates-hurt-precision.md) — related
- [Random forest imputation of missing predictor values did not meaningfully improve auxiliary model performance over simple mean imputation](mean-imputation-sufficient-auxiliary-model.md) — related
- [In auxiliary Texas school data, a random forest with all predictors predicts math TAKS passing rates better than OLS with the pretest alone](rf-all-predictors-beats-pretest-auxiliary.md) — related

---
type: claim
title: Random forest models consistently outperform neural networks for predicting math TAKS passing rates in the auxiliary data
description: Random forest models consistently outperform neural networks for predicting math TAKS passing rates in the auxiliary data
id: random-forests-outperform-neural-nets-auxiliary
aliases: [random-forest-outperforms-neural-nets-auxiliary-prediction]
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-01
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: c-z-mann-2024
    resource: "https://doi.org/10.5281/zenodo.12729874"
    title: "C. Z. Mann, J. Wang, A. Sales, and J. A. Gagnon-Bartsch. (2024). Using publicly available auxiliary data to improve precision of treatment effect estimation in a randomized efficacy trial. Proceedings of the 17th International Conference on Educational Data Mining. [doi:10.5281/zenodo.12729874](https://doi.org/10.5281/zenodo.12729874)"
    author: C. Z. Mann, J. Wang, A. Sales, and J. A. Gagnon-Bartsch
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Random forest models consistently outperform neural networks for predicting math TAKS passing rates in the auxiliary data

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims

`q2 i?` Across model specifications and predictor sets, random forests out-performed neural nets on MSE and R2 for predicting 2008 passing rates. [→ C. Z. Mann 2024](#c-z-mann-2024)

`q2 i?` Based on MSE and R2 of predictions, random forests out-performed neural nets across model specifications and predictor sets. [→ C. Z. Mann 2024](#c-z-mann-2024)

## Evidence

### C. Z. Mann 2024

C. Z. Mann, J. Wang, A. Sales, and J. A. Gagnon-Bartsch. (2024). Using publicly available auxiliary data to improve precision of treatment effect estimation in a randomized efficacy trial. Proceedings of the 17th International Conference on Educational Data Mining. [doi:10.5281/zenodo.12729874](https://doi.org/10.5281/zenodo.12729874)

`q2 · i?` · `causal · r2`

Algorithm comparison during auxiliary model development on the auxiliary Texas schools, evaluating random forests against neural networks by cross-validated MSE and R2. The article adds that default randomForest package parameters performed essentially as well as further tuning.

> "Based on the MSE and R2 of the resulting predictions, we find that the random forest models consistently out-perform the neural nets, for different model specifications and sets of predictors."

<!-- merged 2026-11-23 from random-forest-outperforms-neural-nets-auxiliary-prediction: that page's entry for this study, which differed from the one above, kept verbatim.
### C. Z. Mann 2024

C. Z. Mann, J. Wang, A. Sales, and J. A. Gagnon-Bartsch. (2024). Using publicly available auxiliary data to improve precision of treatment effect estimation in a randomized efficacy trial. Proceedings of the 17th International Conference on Educational Data Mining. [doi:10.5281/zenodo.12729874](https://doi.org/10.5281/zenodo.12729874)

`q2 · i?`

Algorithm comparison during auxiliary model development on Texas AEIS schools (Section 4.2), evaluating random forests versus neural nets by cross-validated MSE and R2. The article reports random forests "consistently out-perform the neural nets" and that default randomForest parameters performed essentially as well as tuning.

> "Based on the MSE and R2 of the resulting predictions, we find that the random forest models consistently out-perform the neural nets, for different model specifications and sets of predictors."
-->

## Discussion



## Related Claims

- [Variable importance from the auxiliary model indicates the student cohort matters most for predicting middle school math passing rates, while demographics matter for high schools](cohort-importance-middle-school-auxiliary-model.md) — related
- [Random forest imputation of missing predictor values did not meaningfully improve auxiliary model performance over simple mean imputation](mean-imputation-sufficient-auxiliary-model.md) — related
- [In auxiliary Texas school data, a random forest with all predictors predicts math TAKS passing rates better than OLS with the pretest alone](rf-all-predictors-beats-pretest-auxiliary.md) — related
- [Fitting an imputation model with all covariates using only the small trial sample reduces precision relative to pretest-only adjustment](rct-only-all-covariates-hurt-precision.md) — related

---
type: claim
title: After Benjamini-Hochberg false-discovery-rate adjustment, covariate-adjusted estimators detect more significant effects than t-tests (LOOP 11, ReLOOP+ 10, ReLOOP 8, T-Test 3 of 227 contrasts)
description: After Benjamini-Hochberg false-discovery-rate adjustment, covariate-adjusted estimators detect more significant effects than t-tests (LOOP 11, ReLOOP+ 10, ReLOOP 8, T-Test 3 of 227 contrasts)
id: bh-adjusted-discoveries-by-estimator
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: weak
sources:
  - id: adam-c-sales-2023
    resource: "https://osf.io/k8ph9/"
    title: "Adam C. Sales, Ethan B. Prihar, Johann A. Gagnon-Bartsch, Neil T. Heffernan. (2023). Using Auxiliary Data to Boost Precision in the Analysis of A/B Tests on an Online Educational Platform: New Data and New Results. Journal of Educational Data Mining, Volume 15, No 2. https://osf.io/k8ph9/"
    author: Adam C. Sales, Ethan B. Prihar, Johann A. Gagnon-Bartsch, Neil T. Heffernan
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# After Benjamini-Hochberg false-discovery-rate adjustment, covariate-adjusted estimators detect more significant effects than t-tests (LOOP 11, ReLOOP+ 10, ReLOOP 8, T-Test 3 of 227 contrasts)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Counting p-values below 0.05 across 227 contrasts after Benjamini-Hochberg adjustment, T-Tests yielded 3 discoveries, LOOP 11, ReLOOP 8, and ReLOOP+ 10. [→ Adam C. Sales 2023](#adam-c-sales-2023)

## Evidence

### Adam C. Sales 2023

Adam C. Sales, Ethan B. Prihar, Johann A. Gagnon-Bartsch, Neil T. Heffernan. (2023). Using Auxiliary Data to Boost Precision in the Analysis of A/B Tests on an Online Educational Platform: New Data and New Results. Journal of Educational Data Mining, Volume 15, No 2. https://osf.io/k8ph9/

`q2 · i?` · `causal · r2`

Count of significant p-values (Table 3) from applying the four estimators to the same 227 randomized contrasts, unadjusted and adjusted with Benjamini-Hochberg and Benjamini-Yekutieli procedures. Under the conservative Benjamini-Yekutieli adjustment all four estimators rejected 2 null hypotheses.

> "After Benjamini-Hochberg adjustment, a researcher using T-Tests would only discover 3 effects, while researchers using LOOP would discover 11, those using ReLOOP would discover 8, and those combining within-sample and remnant-based adjustments with ReLOOP + would lead to two additional discoveries or 10 total."

## Discussion


## Related Claims
- [Remnant-based adjustment still adds precision beyond within-sample-only machine-learning adjustment (LOOP), equivalent to roughly a 10–20% sample-size increase in about half of cases](reloop-gains-beyond-within-sample-loop.md) — related
- [Remnant-based covariate adjustment (ReLOOP/ReLOOP+) reduces estimated sampling variance in A/B effect estimates relative to t-tests, equivalent to roughly a 20% average sample-size increase](reloop-remnant-imputation-variance-reduction-vs-ttest.md) — related
- [OLS regression-adjusted standard errors and significance levels for average treatment effect estimators are similar to Neyman-model estimates when baseline covariates are included in experimental designs](ols-neyman-similar-standard-errors-with-covariates.md) — related

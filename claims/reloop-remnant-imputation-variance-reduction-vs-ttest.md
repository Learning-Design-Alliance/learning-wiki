---
type: claim
title: "Remnant-based covariate adjustment (ReLOOP/ReLOOP+) reduces estimated sampling variance in A/B effect estimates relative to t-tests, equivalent to roughly a 20% average sample-size increase"
description: "Remnant-based covariate adjustment (ReLOOP/ReLOOP+) reduces estimated sampling variance in A/B effect estimates relative to t-tests, equivalent to roughly a 20% average sample-size increase"
id: reloop-remnant-imputation-variance-reduction-vs-ttest
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: moderate
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

# Remnant-based covariate adjustment (ReLOOP/ReLOOP+) reduces estimated sampling variance in A/B effect estimates relative to t-tests, equivalent to roughly a 20% average sample-size increase

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Across 227 randomized contrasts, ReLOOP+ adjustment for remnant-based imputations plus within-sample covariates had a median variance improvement equivalent to increasing the sample size by about 20%, up to 80% in the best case, versus the unadjusted t-test estimator. [→ Adam C. Sales 2023](#adam-c-sales-2023)

## Evidence

### Adam C. Sales 2023

Adam C. Sales, Ethan B. Prihar, Johann A. Gagnon-Bartsch, Neil T. Heffernan. (2023). Using Auxiliary Data to Boost Precision in the Analysis of A/B Tests on an Online Educational Platform: New Data and New Results. Journal of Educational Data Mining, Volume 15, No 2. https://osf.io/k8ph9/

`q2 · i?` · `causal · r2`

Numerical comparison of estimated sampling-variance ratios across 227 randomized contrasts from 68 ASSISTments A/B tests, shown in Figure 3 boxplots. The ReLOOP+ estimator's median improvement was "equivalent to increasing the sample size by about 20%" versus the t-test; no effect size is printed.

> "Here the results are slightly more impressive than those of the left panel—the median improvement is equivalent to increasing the sample size by about 20%, and in the best case the improvement is equivalent to an 80% increase in sample size."

## Discussion


## Related Claims
- [After Benjamini-Hochberg false-discovery-rate adjustment, covariate-adjusted estimators detect more significant effects than t-tests (LOOP 11, ReLOOP+ 10, ReLOOP 8, T-Test 3 of 227 contrasts)](bh-adjusted-discoveries-by-estimator.md) — related
- [Remnant-based adjustment still adds precision beyond within-sample-only machine-learning adjustment (LOOP), equivalent to roughly a 10–20% sample-size increase in about half of cases](reloop-gains-beyond-within-sample-loop.md) — related
- [Among remnant data types, the combined ensemble model reduced sampling variance most, the action-level model least, and the assignment-level model performed nearly as well as the combined model](remnant-data-type-contribution-variance.md) — related

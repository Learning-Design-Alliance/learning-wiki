---
type: claim
title: "Remnant-based adjustment still adds precision beyond within-sample-only machine-learning adjustment (LOOP), equivalent to roughly a 10–20% sample-size increase in about half of cases"
description: "Remnant-based adjustment still adds precision beyond within-sample-only machine-learning adjustment (LOOP), equivalent to roughly a 10–20% sample-size increase in about half of cases"
id: reloop-gains-beyond-within-sample-loop
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

# Remnant-based adjustment still adds precision beyond within-sample-only machine-learning adjustment (LOOP), equivalent to roughly a 10–20% sample-size increase in about half of cases

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Comparing LOOP (within-sample covariate adjustment, no remnant) to ReLOOP+ in 227 contrasts, adding remnant data was equivalent to increasing the sample size by about 10–20% in roughly half of cases, and closer to 30% in a handful. [→ Adam C. Sales 2023](#adam-c-sales-2023)

## Evidence

### Adam C. Sales 2023

Adam C. Sales, Ethan B. Prihar, Johann A. Gagnon-Bartsch, Neil T. Heffernan. (2023). Using Auxiliary Data to Boost Precision in the Analysis of A/B Tests on an Online Educational Platform: New Data and New Results. Journal of Educational Data Mining, Volume 15, No 2. https://osf.io/k8ph9/

`q2 · i?` · `causal · r2`

Numerical comparison of estimated sampling-variance ratios between the LOOP estimator (random-forest within-sample adjustment) and ReLOOP+ in the rightmost panel of Figure 3, over 227 randomized contrasts. Gains are described as "more modest relative gains"; no effect size is printed.

> "Nevertheless, the contribution of the remnant is still significant—in roughly half of cases, including data from the remnant was equivalent to increasing the sample size by about 10–20%, and in a handful of cases the improvement was closer to 30%."

## Discussion


## Related Claims
- [After Benjamini-Hochberg false-discovery-rate adjustment, covariate-adjusted estimators detect more significant effects than t-tests (LOOP 11, ReLOOP+ 10, ReLOOP 8, T-Test 3 of 227 contrasts)](bh-adjusted-discoveries-by-estimator.md) — related
- [Remnant-based covariate adjustment (ReLOOP/ReLOOP+) reduces estimated sampling variance in A/B effect estimates relative to t-tests, equivalent to roughly a 20% average sample-size increase](reloop-remnant-imputation-variance-reduction-vs-ttest.md) — related
- [Among remnant data types, the combined ensemble model reduced sampling variance most, the action-level model least, and the assignment-level model performed nearly as well as the combined model](remnant-data-type-contribution-variance.md) — related

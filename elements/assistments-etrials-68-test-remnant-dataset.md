---
type: element
id: assistments-etrials-68-test-remnant-dataset
title: ASSISTments E-Trials A/B test dataset with remnant log data (68 tests, 227 contrasts, 38,035 experimental students, 193,218 remnant students)
description: "A dataset assembled for testing remnant-based estimators, drawn from the ASSISTments online tutor's E-Trials experimentation platform."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
sources:
  - id: adam-c-sales-2023
    resource: "https://osf.io/k8ph9/"
    title: "Adam C. Sales, Ethan B. Prihar, Johann A. Gagnon-Bartsch, Neil T. Heffernan. (2023). Using Auxiliary Data to Boost Precision in the Analysis of A/B Tests on an Online Educational Platform: New Data and New Results. Journal of Educational Data Mining, Volume 15, No 2. https://osf.io/k8ph9/"
    author: Adam C. Sales, Ethan B. Prihar, Johann A. Gagnon-Bartsch, Neil T. Heffernan
---

# ASSISTments E-Trials A/B test dataset with remnant log data (68 tests, 227 contrasts, 38,035 experimental students, 193,218 remnant students)

> **Element** · [All elements](index.md)
> **Evidence** · 5 claims (5 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 5 claims rest on one study

## Description
A dataset assembled for testing remnant-based estimators, drawn from the ASSISTments online tutor's E-Trials experimentation platform. It comprises, in the article's words, "a collection of 68 multi-armed A/B tests run on the ASSISTments TestBed (Ostrow et al., 2016, now called "E-Trials"), which together include 227 different two-way comparisons and 38,035 students." Alongside it, log data were collected for 193,218 remnant students who worked on similar skill builders but participated in no experiment, with no overlap in students or skill builders between the two sets. The outcome analyzed was binary assignment completion, with nine student-level aggregated predictors used for within-RCT adjustment.

## Design Implications

### Context
#### Requirements
- Bernoulli randomization with p = 1/2; contrasts with outcome variance zero, p ≠ 1/2 indications, or very small samples were excluded
#### Constraints
- Analyses focus on estimated standard errors rather than treatment effects, since the interest is methodological

### Target Learners
- middle- and high-school students using ASSISTments

### Target Learning Goals
- estimating causal effects of educational conditions on assignment completion

### Affordances
- [Reloop Remnant Based Design Based Estimators](../theories/reloop-remnant-based-design-based-estimators.md)

## Claims

- [After Benjamini-Hochberg false-discovery-rate adjustment, covariate-adjusted estimators detect more significant effects than t-tests (LOOP 11, ReLOOP+ 10, ReLOOP 8, T-Test 3 of 227 contrasts)](../claims/bh-adjusted-discoveries-by-estimator.md) [+W]
- [Prior assignment statistics were the most predictive remnant data type for assignment performance, followed by prior student statistics, with daily action history least predictive; combining datasets improved predictions over any single dataset](../claims/prior-assignment-statistics-most-predictive.md) [+W]
- [Remnant-based adjustment still adds precision beyond within-sample-only machine-learning adjustment (LOOP), equivalent to roughly a 10–20% sample-size increase in about half of cases](../claims/reloop-gains-beyond-within-sample-loop.md) [+W]
- [Remnant-based covariate adjustment (ReLOOP/ReLOOP+) reduces estimated sampling variance in A/B effect estimates relative to t-tests, equivalent to roughly a 20% average sample-size increase](../claims/reloop-remnant-imputation-variance-reduction-vs-ttest.md) [+W]
- [Among remnant data types, the combined ensemble model reduced sampling variance most, the action-level model least, and the assignment-level model performed nearly as well as the combined model](../claims/remnant-data-type-contribution-variance.md) [+W]

## Related Elements

- [Four remnant-trained deep-learning imputation models (prior student statistics, prior assignments, prior daily actions, and a combined ensemble)](four-remnant-deep-learning-imputation-models.md)
- [ASSISTments/E-TRIALS: free A/B testing platform integrated with a K-12 math practice platform](assistments-e-trials-platform.md)

## Examples
-

## Key Sources
- Adam C. Sales, Ethan B. Prihar, Johann A. Gagnon-Bartsch, Neil T. Heffernan. (2023). Using Auxiliary Data to Boost Precision in the Analysis of A/B Tests on an Online Educational Platform: New Data and New Results. Journal of Educational Data Mining, Volume 15, No 2. https://osf.io/k8ph9/

---
type: research-method
id: remnant-based-covariate-adjustment-reloop
title: Remnant-based covariate adjustment (ReLOOP+)
description: "This principle directs platform researchers analyzing randomized experiments to train outcome-prediction models on log data from non-experimental ('remnant') users and incorporate those predictions, together with within-sample covariates, into design-based covariate-adjusted estimators such as ReLOO"
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-09
---

# Remnant-based covariate adjustment (ReLOOP+)

> **Research Method** · [All research methods](index.md)

## Description
This principle directs platform researchers analyzing randomized experiments to train outcome-prediction models on log data from non-experimental ('remnant') users and incorporate those predictions, together with within-sample covariates, into design-based covariate-adjusted estimators such as ReLOOP+. The article's summary of its findings: "covariate adjustment can lead to substantial gains in precision, with the greatest improvement resulting from adjustment using both within-sample aggregated covariates and remnant-based imputations." Because adjustment is design-based, estimates remain unbiased and inference valid even if the imputation model is poor.

## Accounts
<!-- How each source describes or uses the method -->
- **When analyzing A/B tests on online learning platforms, use remnant-trained imputation models for covariate adjustment alongside within-sample covariates to gain precision without sacrificing unbiasedness**: This principle directs platform researchers analyzing randomized experiments to train outcome-prediction models on log data from non-experimental ('remnant') users and incorporate those predictions, together with within-sample covariates, into design-based covariate-adjusted estimators such as ReLOOP+. The article's summary of its findings: "covariate adjustment can lead to substantial gains in precision, with the greatest improvement resulting from adjustment using both within-sample aggregated covariates and remnant-based imputations." Because adjustment is design-based, estimates remain unbiased and inference valid even if the imputation model is poor. (Adam C. Sales et al. (2023))

### Claims
- [Remnant-based covariate adjustment (ReLOOP/ReLOOP+) reduces estimated sampling variance in A/B effect estimates relative to t-tests, equivalent to roughly a 20% average sample-size increase](../claims/reloop-remnant-imputation-variance-reduction-vs-ttest.md) [+M]
- [Remnant-based adjustment still adds precision beyond within-sample-only machine-learning adjustment (LOOP), equivalent to roughly a 10–20% sample-size increase in about half of cases](../claims/reloop-gains-beyond-within-sample-loop.md) [+M]

## Related Research Methods
-

## Key Sources
- Adam C. Sales, Ethan B. Prihar, Johann A. Gagnon-Bartsch, Neil T. Heffernan. (2023). Using Auxiliary Data to Boost Precision in the Analysis of A/B Tests on an Online Educational Platform: New Data and New Results. Journal of Educational Data Mining, Volume 15, No 2. https://osf.io/k8ph9/

---
type: strategy
id: combine-cng-accuracy-with-ng-individual-analysis
title: Combine the unbiased case-average estimator with the individual-level usability of ngain in learning-rate analyses
description: "The article recommends exploiting both estimators' complementary strengths when analyzing learning data."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: jairo-navarrete-2024
    resource: "https://arxiv.org/abs/2407.07730"
    title: "Jairo Navarrete, Valentina Giaconi, Gonzalo Contador, Mariano Vazquez. (2024). Another reason why normalized gain should continue to be used to analyze concept inventories (and estimate learning rates). arXiv. https://arxiv.org/abs/2407.07730"
    author: Jairo Navarrete, Valentina Giaconi, Gonzalo Contador, Mariano Vazquez
---

# Combine the unbiased case-average estimator with the individual-level usability of ngain in learning-rate analyses

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (2 for, 1 mixed) · 1 study (1 theoretical), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The article recommends exploiting both estimators' complementary strengths when analyzing learning data. The case-average estimator cng is asymptotically unbiased and precise for a group's learning rate, but it "cannot integrate individual information into data analysis" — for example it cannot be the output variable of an ANCOVA with individual predictors. Although ng underestimates the learning rate, it can input individual information such as cognitive abilities, SES or teaching methods. The proposed approach: "The best of both worlds would be to use ng as the output variable of an analysis (e.g., ANCOV A) but then force the computations to center the mean of the output on the more accurate estimate cng."

## Design Implications

### Context
#### Requirements
- Requires developing computational methods to correct ngain estimations using the measurement-error-induced pretest-ngain correlation, which the authors say needs further research
#### Constraints
- The combined approach is proposed as future work; the article states developing it requires further research
- Measurement errors are unavoidable in practice, so only the measurement-error case is analyzed

### Target Learners
- researchers and analysts estimating learning rates from pretest-posttest concept-inventory data

### Target Learning Goals
- unbiased estimation of knowledge change controlling for prior knowledge

## Claims

- [Without measurement errors, both learning-rate estimators (average ngain and ngain of the average learner) are unbiased, and any difference between them is random](../claims/errorless-case-both-ngain-estimators-unbiased.md) [+W]
- [Further simulations suggest the mean-of-cases estimator may be reliable in low-pretest-mean settings, and bias shrinks when score variance is reduced](../claims/appendix-simulations-low-pretest-reliable-mean-of-cases.md) [+W]
- [Measurement errors in pretest and posttest scores induce a spurious negative pretest-ngain correlation even when prior knowledge and learning rate are independent](../claims/measurement-errors-induce-spurious-pretest-ngain-correlation.md) [~W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Jairo Navarrete, Valentina Giaconi, Gonzalo Contador, Mariano Vazquez. (2024). Another reason why normalized gain should continue to be used to analyze concept inventories (and estimate learning rates). arXiv. https://arxiv.org/abs/2407.07730

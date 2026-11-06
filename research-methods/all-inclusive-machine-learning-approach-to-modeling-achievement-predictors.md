---
type: research-method
id: all-inclusive-machine-learning-approach-to-modeling-achievement-predictors
title: All-inclusive machine learning approach to modeling achievement predictors
description: "The article coins an \"all-inclusive approach\": modeling the entire set of potential predictors, including their nonlinear and complex interactions, at once, rather than testing a small subset of predictors."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-25
---

# All-inclusive machine learning approach to modeling achievement predictors

> **Research Method** · [All research methods](index.md)
> **Evidence** · 3 claims (3 for) · 2 studies (2 associational), `q2` · 0 of 2 report an effect size · 3 claims rest on one study

## Description
The article coins an "all-inclusive approach": modeling the entire set of potential predictors, including their nonlinear and complex interactions, at once, rather than testing a small subset of predictors. Machine learning makes this feasible because regularization and out-of-sample evaluation protect against overfitting and multicollinearity that destabilize traditional regression with many predictors. The approach is applied to the PALMA longitudinal data with Elastic Net and Random Forest models, using a pipeline of training/test splitting, five-fold cross-validation, and SHAP-based variable importance for interpretation.

## Accounts
<!-- How each source describes or uses the method -->
- **All-inclusive machine learning approach to modeling achievement predictors**: The article coins an "all-inclusive approach": modeling the entire set of potential predictors, including their nonlinear and complex interactions, at once, rather than testing a small subset of predictors. Machine learning makes this feasible because regularization and out-of-sample evaluation protect against overfitting and multicollinearity that destabilize traditional regression with many predictors. The approach is applied to the PALMA longitudinal data with Elastic Net and Random Forest models, using a pipeline of training/test splitting, five-fold cross-validation, and SHAP-based variable importance for interpretation. (Lavelle-Hill et al. (2024))
- **Random Forest Algorithm with Boruta feature selection as a method for identifying important predictors of educational outcomes**: The article employs the Random Forest Algorithm (RFA) via the Boruta package in R as its analytical framework. Boruta is described as "a wrapping method based on Random Forest and calculates the significance levels of the variables using Z-scores", creating a shadow copy of each variable and retaining only variables with unique information value. The authors argue RFA suits educational data because it handles high-dimensional categorical data, minimises multicollinearity, and captures nonlinear interactions and interactions that classical statistical models miss. Its role in the study is both prediction and evidence-based prioritisation of influential variables for policy makers. (Alkan Bilal Baris et al. (2025))

### Claims
- [A machine learning model using 105 predictors predicts next-year standardized math achievement with out-of-sample prediction R-squared of .70–.78](../claims/ml-model-predicts-next-year-math-achievement-r2-70-78.md) [+M]
- [Beyond prior achievement, predictor groups (IQ, grades, motivation and emotion, cognitive strategies, classroom/home environments, demographics) show smaller yet consistent contributions to predicting math achievement over time](../claims/predictor-groups-smaller-consistent-contributions-math.md) [+M]
- [Nine variables were flagged as important overall in the Random Forest analysis, with five shared across reading, mathematics and science](../claims/pisa-nine-important-variables-five-shared.md) [+M]

## Related Research Methods
-

## Key Sources
- Lavelle-Hill, R., Frenzel, A. C., Goetz, T., Lichtenfeld, S., Marsh, H. W., Pekrun, R., Sakaki, M., Smith, G., & Murayama, K. (2024). How the Predictors of Math Achievement Change Over Time: A Longitudinal Machine Learning Approach. Journal of Educational Psychology, 116(8), 1383–1403. https://doi.org/10.1037/edu0000863
- Alkan Bilal Baris, Kuzucuk Serafettin, Odabasi Şevki Yetkin, Karakuş Leyla. (2025). Educational improvement through machine learning: Strategic models for better PISA scores. PLOS One 20(7): e0326121. https://doi.org/10.1371/journal.pone.0326121

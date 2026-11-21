---
type: research-method
id: out-of-sample-predictive-model-evaluation-and-model-comparison
title: Out-of-sample predictive model evaluation and model comparison
description: The article recommends that predictive claims in PER rest on model performance on data the model has not seen, rather than on in-sample statistical significance.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
---

# Out-of-sample predictive model evaluation and model comparison

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article recommends that predictive claims in PER rest on model performance on data the model has not seen, rather than on in-sample statistical significance. It states "A model’s predictive ability should be evaluated by its ability to predict new data that the model has not seen before" and that several constants should hold for any predictive study: "Statistical model evaluation should use out-of-sample data to evaluate model performance. Multiple types of statistical models should be compared and evaluated before presenting results from the model." This places model reliability in its ability to represent the natural world rather than in-sample significance.

## Accounts
<!-- How each source describes or uses the method -->
- **Evaluate predictive statistical models on out-of-sample data and compare multiple model types before presenting results**: The article recommends that predictive claims in PER rest on model performance on data the model has not seen, rather than on in-sample statistical significance. It states "A model’s predictive ability should be evaluated by its ability to predict new data that the model has not seen before" and that several constants should hold for any predictive study: "Statistical model evaluation should use out-of-sample data to evaluate model performance. Multiple types of statistical models should be compared and evaluated before presenting results from the model." This places model reliability in its ability to represent the natural world rather than in-sample significance. (John M. Aiken et al. (2021))
- **Validate remote learner-state detection models with user-independent splits holding out whole clients**: The article recommends evaluating remote learner-state detection models with user-independent splits that hold out entire clients rather than samples, because such validation has "superior validity in handling unseen data" and "makes it a more suitable representation for real-world applications". The authors note this makes modeling more demanding but better reflects deployment on unseen learners. (Bodonhelyi et al. (2026))

### Claims
- [Gradient boosted models achieve lower out-of-sample mean absolute and mean squared error than OLS and mixed-effects models when predicting LASSO concept-inventory post-test scores](../claims/gradient-boosted-lower-error-lasso-posttest.md) [+M]
- [Gradient boosted logistic regression outperforms fixed-effects and mixed-effects logistic regression in classifying introductory vs beyond-first-year E-CLASS students, though all models fall below excellent discrimination](../claims/eclass-boosted-logistic-best-auc.md) [+M]

## Related Research Methods
-

## Key Sources
- John M. Aiken, Riccardo De Bin, H. J. Lewandowski, and Marcos D. Caballero. (2021). A Framework for Evaluating Statistical Models in Physics Education Research. https://arxiv.org/abs/2106.11038
- Bodonhelyi, A., Wang, M., Bozkir, E., Bühler, B., Kasneci, E. (2026). Safeguarding Privacy: Privacy-Preserving Detection of Mind Wandering and Disengagement Using Federated Learning in Online Education. https://arxiv.org/abs/2602.09904

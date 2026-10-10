---
type: research-method
id: remnant-trained-deep-learning-models-for-assignment-completion-and-mastery-prediction
title: Remnant-trained deep-learning models for assignment-completion and mastery prediction
description: "The article trained four neural networks on remnant data to predict assignment completion and problems to mastery: a feed-forward network on prior student statistics, LSTM networks on the last 20 started assignments and the last 60 days of tutor actions, and an ensemble."
status: draft
generated:
  by: "process:sweep-kinds"
  at: 2026-10-10
sources:
  - id: adam-c-sales-2023
    resource: "https://osf.io/k8ph9/"
    title: "Adam C. Sales, Ethan B. Prihar, Johann A. Gagnon-Bartsch, Neil T. Heffernan. (2023). Using Auxiliary Data to Boost Precision in the Analysis of A/B Tests on an Online Educational Platform: New Data and New Results. Journal of Educational Data Mining, Volume 15, No 2. https://osf.io/k8ph9/"
    author: Adam C. Sales, Ethan B. Prihar, Johann A. Gagnon-Bartsch, Neil T. Heffernan
---

# Remnant-trained deep-learning models for assignment-completion and mastery prediction

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article trained four neural networks on remnant data to predict assignment completion and problems to mastery: a feed-forward network on prior student statistics, LSTM networks on the last 20 started assignments and the last 60 days of tutor actions, and an ensemble. The combined model "takes the three models above and couples their predictions such that the prediction is a function of all three models' weights and the loss is backpropagated through each model during training." Hyperparameters (dropout frequency, layer depth, node counts) were chosen by grid search on a held-out subset, with 5-fold cross-validation used to measure model quality.

## Accounts
<!-- How each source describes or uses the method -->
- **Four remnant-trained deep-learning imputation models (prior student statistics, prior assignments, prior daily actions, and a combined ensemble)**: The article trained four neural networks on remnant data to predict assignment completion and problems to mastery: a feed-forward network on prior student statistics, LSTM networks on the last 20 started assignments and the last 60 days of tutor actions, and an ensemble. The combined model "takes the three models above and couples their predictions such that the prediction is a function of all three models' weights and the loss is backpropagated through each model during training." Hyperparameters (dropout frequency, layer depth, node counts) were chosen by grid search on a held-out subset, with 5-fold cross-validation used to measure model quality. (Adam C. Sales et al. (2023))

### Claims
- [Prior assignment statistics were the most predictive remnant data type for assignment performance, followed by prior student statistics, with daily action history least predictive; combining datasets improved predictions over any single dataset](../claims/prior-assignment-statistics-most-predictive.md) [+W]
- [Among remnant data types, the combined ensemble model reduced sampling variance most, the action-level model least, and the assignment-level model performed nearly as well as the combined model](../claims/remnant-data-type-contribution-variance.md) [+W]

## Related Research Methods
-

## Key Sources
- Adam C. Sales, Ethan B. Prihar, Johann A. Gagnon-Bartsch, Neil T. Heffernan. (2023). Using Auxiliary Data to Boost Precision in the Analysis of A/B Tests on an Online Educational Platform: New Data and New Results. Journal of Educational Data Mining, Volume 15, No 2. https://osf.io/k8ph9/

<!-- merged 2026-10-10 from elements/four-remnant-deep-learning-imputation-models ("Four remnant-trained deep-learning imputation models (prior student statistics, prior assignments, prior daily actions, and a combined ensemble)"), misfiled as a element and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Four remnant-trained deep-learning imputation models (prior student statistics, prior assignments, prior daily actions, and a combined ensemble)

> **Element** · [All elements](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article trained four neural networks on remnant data to predict assignment completion and problems to mastery: a feed-forward network on prior student statistics, LSTM networks on the last 20 started assignments and the last 60 days of tutor actions, and an ensemble. The combined model "takes the three models above and couples their predictions such that the prediction is a function of all three models' weights and the loss is backpropagated through each model during training." Hyperparameters (dropout frequency, layer depth, node counts) were chosen by grid search on a held-out subset, with 5-fold cross-validation used to measure model quality.

## Design Implications

### Context
#### Requirements
- Training used the ADAM optimizer with binary cross-entropy loss for completion, mean squared error for problems to mastery, and a grid-searched gain of 16 on the cross-entropy loss
#### Constraints
- Dropout was used for regularization but not in validation, testing, or prediction

### Target Learners
- students using ASSISTments

### Target Learning Goals
- predicting student assignment completion and problems to mastery from prior platform log data

### Affordances
- [Reloop Remnant Based Design Based Estimators](../theories/reloop-remnant-based-design-based-estimators.md)

## Claims

- [Prior assignment statistics were the most predictive remnant data type for assignment performance, followed by prior student statistics, with daily action history least predictive; combining datasets improved predictions over any single dataset](../claims/prior-assignment-statistics-most-predictive.md) [+W]
- [Among remnant data types, the combined ensemble model reduced sampling variance most, the action-level model least, and the assignment-level model performed nearly as well as the combined model](../claims/remnant-data-type-contribution-variance.md) [+W]

## Related Elements

- [ASSISTments E-Trials A/B test dataset with remnant log data (68 tests, 227 contrasts, 38,035 experimental students, 193,218 remnant students)](../products/assistments.md)

## Examples
-

## Key Sources
- Adam C. Sales, Ethan B. Prihar, Johann A. Gagnon-Bartsch, Neil T. Heffernan. (2023). Using Auxiliary Data to Boost Precision in the Analysis of A/B Tests on an Online Educational Platform: New Data and New Results. Journal of Educational Data Mining, Volume 15, No 2. https://osf.io/k8ph9/
-->

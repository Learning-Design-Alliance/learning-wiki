---
type: element
id: bootstrapping-adjustment-ba-method
title: Bootstrapping adjustment (BA) method for item parameter bias reduction
description: BA is one of two item parameter adjustment methods proposed in the article, reducing biases in both item difficulty and item discrimination parameters using statistical bootstrapping.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
sources:
  - id: xue-2020
    resource: "https://educationaldatamining.org/EDM2020/"
    title: "Xue, K., Huggins-Manley, A. C., & Leite, W. (2020). Semi-supervised Learning Method for Adjusting Biased Item Difficulty Estimates Caused by Nonignorable Missingness under 2PL-IRT Model. Proceedings of The 13th International Conference on Educational Data Mining (EDM 2020), pp. 715-719. https://educationaldatamining.org/EDM2020/"
    author: "Xue, K., Huggins-Manley, A. C., & Leite, W"
---

# Bootstrapping adjustment (BA) method for item parameter bias reduction

> **Element** · [All elements](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
BA is one of two item parameter adjustment methods proposed in the article, reducing biases in both item difficulty and item discrimination parameters using statistical bootstrapping. In four steps it repeatedly samples anchor students based on the unbiased ability estimates to form standard-normal-distributed samples of the same size, applies 2PL-IRT to each sample, and averages the resulting difficulty and discrimination estimates over K repetitions. The article states "The BA method relies on less constraint and could reduce the biases contained in both item discrimination and diﬃculty estimates", and that it "has the potential for applying on more complicated IRT models, such as 3PL-IRT".

## Design Implications

### Context
#### Requirements
- Requires unbiased ability estimates from the semi-supervised deep learning architecture as the basis for sampling
- Requires repeated sampling K times to average difficulty and discrimination estimates
#### Constraints
- Its reduced-bias performance was evaluated in simulation under the 2PL-IRT model; applicability to 3PL-IRT is stated only as potential

### Target Learners
- K-12 students using a statewide virtual learning environment for Algebra I

### Target Learning Goals
- Unbiased item difficulty and discrimination estimation for operational ability measurement in VLEs

### Affordances
- [Semi Supervised Deep Learning Irt Bias Adjustment Framework](../theories/semi-supervised-deep-learning-irt-bias-adjustment-framework.md)

## Claims

- [Both proposed adjustment methods (IEA and BA) reduce RMSE of item difficulty estimates from direct 2PL-IRT fitting, with BA yielding more consistent (lower-variance) estimates in simulation](../claims/iea-ba-reduce-difficulty-estimate-bias.md) [+W]
- [A semi-supervised deep learning architecture recovers the ability distribution of anchor students more accurately than direct 2PL-IRT fitting under simulated nonignorable missingness](../claims/semi-supervised-deep-learning-unbiased-ability-estimates.md) [+W]

## Related Elements
- 

## Examples
-

## Key Sources
- Xue, K., Huggins-Manley, A. C., & Leite, W. (2020). Semi-supervised Learning Method for Adjusting Biased Item Difficulty Estimates Caused by Nonignorable Missingness under 2PL-IRT Model. Proceedings of The 13th International Conference on Educational Data Mining (EDM 2020), pp. 715-719. https://educationaldatamining.org/EDM2020/

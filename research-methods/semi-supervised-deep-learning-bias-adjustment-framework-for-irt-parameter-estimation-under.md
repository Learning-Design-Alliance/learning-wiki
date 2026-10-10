---
type: research-method
id: semi-supervised-deep-learning-bias-adjustment-framework-for-irt-parameter-estimation-under
title: Semi-supervised deep learning bias-adjustment framework for IRT parameter estimation under nonignorable missingness
description: The article introduces a framework combining semi-supervised learning with deep learning to adjust biased 2PL-IRT parameter estimates caused by nonignorable missingness in VLE data.
status: draft
generated:
  by: "process:sweep-kinds"
  at: 2026-10-10
sources:
  - id: xue-2020
    resource: "https://educationaldatamining.org/EDM2020/"
    title: "Xue, K., Huggins-Manley, A. C., & Leite, W. (2020). Semi-supervised Learning Method for Adjusting Biased Item Difficulty Estimates Caused by Nonignorable Missingness under 2PL-IRT Model. Proceedings of The 13th International Conference on Educational Data Mining (EDM 2020), pp. 715-719. https://educationaldatamining.org/EDM2020/"
    author: "Xue, K., Huggins-Manley, A. C., & Leite, W"
---

# Semi-supervised deep learning bias-adjustment framework for IRT parameter estimation under nonignorable missingness

> **Research Method** · [All research methods](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 associational), `q1` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The article introduces a framework combining semi-supervised learning with deep learning to adjust biased 2PL-IRT parameter estimates caused by nonignorable missingness in VLE data. A deep feedforward network with 3 hidden layers and ReLU activation converts observed response patterns of anchor students into unbiased ability estimates, trained by minimizing a weighted cost function combining MSE against biased 2PL-IRT ability estimates and cross-entropy against observed response patterns. The authors state that "the idea of semi-supervised learning was ﬁrst time used in IRT area to improve the robustness of latent trait estimation", with hyperparameters determined by the elbow method in vali

## Accounts
<!-- How each source describes or uses the method -->
- **Semi-supervised deep learning bias-adjustment framework for IRT parameter estimation under nonignorable missingness**: The article introduces a framework combining semi-supervised learning with deep learning to adjust biased 2PL-IRT parameter estimates caused by nonignorable missingness in VLE data. A deep feedforward network with 3 hidden layers and ReLU activation converts observed response patterns of anchor students into unbiased ability estimates, trained by minimizing a weighted cost function combining MSE against biased 2PL-IRT ability estimates and cross-entropy against observed response patterns. The authors state that "the idea of semi-supervised learning was ﬁrst time used in IRT area to improve the robustness of latent trait estimation", with hyperparameters determined by the elbow method in vali (Xue et al. (2020))

### Claims
- [A semi-supervised deep learning architecture recovers the ability distribution of anchor students more accurately than direct 2PL-IRT fitting under simulated nonignorable missingness](../claims/semi-supervised-deep-learning-unbiased-ability-estimates.md) [+W]
- [Both proposed adjustment methods (IEA and BA) reduce RMSE of item difficulty estimates from direct 2PL-IRT fitting, with BA yielding more consistent (lower-variance) estimates in simulation](../claims/iea-ba-reduce-difficulty-estimate-bias.md) [+W]
- [In a statewide VLE algebra dataset, item missingness is nonignorable: skipping is related to student ability and item difficulty as measured in 2PL-IRT](../claims/vle-item-skipping-nonignorable-missingness.md) [+W]

## Related Research Methods
-

## Key Sources
- Xue, K., Huggins-Manley, A. C., & Leite, W. (2020). Semi-supervised Learning Method for Adjusting Biased Item Difficulty Estimates Caused by Nonignorable Missingness under 2PL-IRT Model. Proceedings of The 13th International Conference on Educational Data Mining (EDM 2020), pp. 715-719. https://educationaldatamining.org/EDM2020/

<!-- merged 2026-10-10 from theories/semi-supervised-deep-learning-irt-bias-adjustment-framework ("Semi-supervised deep learning bias-adjustment framework for IRT parameter estimation under nonignorable missingness"), misfiled as a theorie and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Semi-supervised deep learning bias-adjustment framework for IRT parameter estimation under nonignorable missingness

> **Theory** · [All theories](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 associational), `q1` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The article introduces a framework combining semi-supervised learning with deep learning to adjust biased 2PL-IRT parameter estimates caused by nonignorable missingness in VLE data. A deep feedforward network with 3 hidden layers and ReLU activation converts observed response patterns of anchor students into unbiased ability estimates, trained by minimizing a weighted cost function combining MSE against biased 2PL-IRT ability estimates and cross-entropy against observed response patterns. The authors state that "the idea of semi-supervised learning was ﬁrst time used in IRT area to improve the robustness of latent trait estimation", with hyperparameters determined by the elbow method in validation testing.

## Design Implications

### Context
#### Requirements
- Requires a sub-population of anchor students who completed all items in a domain, whose biased ability estimates and response patterns serve as the two training targets
- Requires two assumptions: biased estimation is a function of the unbiased latent trait, and the unbiased latent trait maximizes the likelihood function relating latent trait to response pattern
#### Constraints
- The two item adjustment methods were tested only under the 2PL-IRT model in simulation
- Hidden-layer count was set based on prior deep learning research for cognitive diagnostic models, not independently optimized

### Target Learners
- K-12 students using a statewide virtual learning environment for Algebra I

### Target Learning Objectives
- Ongoing measurement of student ability in algebra domains via unbiased IRT item parameters

### Claims

- [Semi Supervised Deep Learning Unbiased Ability Estimates](../claims/semi-supervised-deep-learning-unbiased-ability-estimates.md) [+M]
- [Iea Ba Reduce Difficulty Estimate Bias](../claims/iea-ba-reduce-difficulty-estimate-bias.md) [+M]
- [In a statewide VLE algebra dataset, item missingness is nonignorable: skipping is related to student ability and item difficulty as measured in 2PL-IRT](../claims/vle-item-skipping-nonignorable-missingness.md) [+W]

## Related Theories
- 

## Examples
-

## Key Sources
- Xue, K., Huggins-Manley, A. C., & Leite, W. (2020). Semi-supervised Learning Method for Adjusting Biased Item Difficulty Estimates Caused by Nonignorable Missingness under 2PL-IRT Model. Proceedings of The 13th International Conference on Educational Data Mining (EDM 2020), pp. 715-719. https://educationaldatamining.org/EDM2020/
-->

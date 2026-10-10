---
type: research-method
id: loss-function-decision-rule-for-late-pretest-use-in-education-rcts
title: Loss-function decision rule for late pretest use in education RCTs
description: Education RCTs often use pretest-posttest designs because including pretests improves the precision of estimated treatment effects.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-09
sources:
  - id: peter-z-schochet-2010
    resource: "https://www.mathematica.org/publications/journal-article-the-late-pretest-problem-in-randomized-control-trials-of-education-interventions"
    title: "Peter Z. Schochet. (2010). The Late Pretest Problem in Randomized Control Trials of Education Interventions. Journal of Educational and Behavioral Statistics, vol. 35, no. 4. https://www.mathematica.org/publications/journal-article-the-late-pretest-problem-in-randomized-control-trials-of-education-interventions"
    author: Peter Z. Schochet
  - id: peter-z-schochet-2008
    resource: "https://ies.ed.gov/ncee"
    title: "Peter Z. Schochet. (2008). The Late Pretest Problem in Randomized Control Trials of Education Interventions. Washington, DC: National Center for Education Evaluation and Regional Assistance, Institute of Education Sciences, U.S. Department of Education. https://ies.ed.gov/ncee"
    author: Peter Z. Schochet
---

# Loss-function decision rule for late pretest use in education RCTs

> **Research Method** · [All research methods](index.md)
> **Evidence** · 6 claims (6 for) · 2 studies (2 theoretical), `q2` · 0 of 2 report an effect size · 6 claims rest on one study

## Description
Education RCTs often use pretest-posttest designs because including pretests improves the precision of estimated treatment effects. However, when pretests are collected after random assignment, analysts should not automatically include them: the decision "involves a variance-bias trade-off" that should be evaluated using a loss function approach before late pretest data are used in impact estimation.

## Accounts
<!-- How each source describes or uses the method -->
- **Use pretest-posttest designs in education RCTs to improve precision of estimated treatment effects, but weigh the bias risk of late pretests**: Education RCTs often use pretest-posttest designs because including pretests improves the precision of estimated treatment effects. However, when pretests are collected after random assignment, analysts should not automatically include them: the decision "involves a variance-bias trade-off" that should be evaluated using a loss function approach before late pretest data are used in impact estimation. (Peter Z. Schochet (2010))
- **A loss function approach grounded in the causal inference literature for evaluating late pretest use in RCTs**: The article proposes evaluating the late pretest decision using a loss function approach grounded in the causal inference literature. This framework balances the precision gains from including pretest covariates against the bias risk when pretests are measured after random assignment. The article states it addresses the issue "using a loss function approach grounded in the causal inference literature," applying it to several commonly used impact estimators. (Peter Z. Schochet (2010))
- **Variance-bias tradeoff framework for deciding whether to use late pretest data in education RCTs**: The paper organizes the late pretest decision as a tradeoff: including late pretest data improves the precision of estimated treatment effects but risks bias because the pretest may be treatment-contaminated. The author "addresses this issue both theoretically and empirically for several commonly used impact estimators, using a loss function approach grounded in the causal inference literature." The framework thus weighs precision gains against bias risk when choosing an impact estimator. (Peter Z. Schochet (2008))

### Claims
- [Including late pretest data in RCT analyses can bias post-test impact estimates because pretests are collected after random assignment](../claims/late-pretest-inclusion-can-bias-posttest-estimates.md) [+M]
- [Deciding whether to collect and use late pretest data in RCTs involves a variance-bias trade-off](../claims/late-pretest-variance-bias-tradeoff.md) [+M]
- [The variance-bias trade-off for late pretests is addressed both theoretically and empirically for several commonly used impact estimators](../claims/late-pretest-analyzed-for-several-estimators.md) [+W]
- [Including late pretest data in RCT analyses can bias post-test impact estimates because pretests are collected after random assignment](../claims/late-pretest-inclusion-can-bias-posttest-estimates.md) [+W]
- [In RCTs of interventions to improve student test scores, estimators including late pretests will typically be preferred to estimators excluding them or using other baseline data](../claims/late-pretest-estimators-typically-preferred.md) [+W]
- [Including late pretest data in RCT analysis could bias post-test impact estimates when pretests are collected after random assignment](../claims/late-pretest-inclusion-can-bias-impact-estimates.md) [+W]
- [The late-pretest estimator preference holds as long as test score impacts do not grow very quickly early in the school year](../claims/late-pretest-preference-conditional-on-slow-early-impact-growth.md) [+W]
- [Including late pretest data in RCT analysis could bias post-test impact estimates when pretests are collected after random assignment](../claims/late-pretest-inclusion-can-bias-impact-estimates.md) [+M]
- [The late-pretest estimator preference holds as long as test score impacts do not grow very quickly early in the school year](../claims/late-pretest-preference-conditional-on-slow-early-impact-growth.md) [~W]
- [Deciding whether to collect and use late pretest data in RCTs involves a variance-bias trade-off](../claims/late-pretest-variance-bias-tradeoff.md) [+W]

## Related Research Methods
-

## Key Sources
- Peter Z. Schochet. (2010). The Late Pretest Problem in Randomized Control Trials of Education Interventions. Journal of Educational and Behavioral Statistics, vol. 35, no. 4. https://www.mathematica.org
- Peter Z. Schochet. (2010). The Late Pretest Problem in Randomized Control Trials of Education Interventions. Journal of Educational and Behavioral Statistics, vol. 35, no. 4. https://www.mathematica.org/publications/journal-article-the-late-pretest-problem-in-randomized-control-trials-of-education-interventions
- Peter Z. Schochet. (2008). The Late Pretest Problem in Randomized Control Trials of Education Interventions. Washington, DC: National Center for Education Evaluation and Regional Assistance, Institute of Education Sciences, U.S. Department of Education. https://ies.ed.gov/ncee

<!-- merged 2026-10-10 from theories/loss-function-approach-late-pretests ("A loss function approach grounded in the causal inference literature for evaluating late pretest use in RCTs"), misfiled as a theorie and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.
- Peter Z. Schochet. (2008). The Late Pretest Problem in Randomized Control Trials of Education Interventions. Washington, DC: National Center for Education Evaluation and Regional Assistance, Institute of Education Sciences, U.S. Department of Education. https://ies.ed.gov/ncee

# A loss function approach grounded in the causal inference literature for evaluating late pretest use in RCTs

> **Theory** · [All theories](index.md)
> **Evidence** · 6 claims (6 for) · 2 studies (2 theoretical), `q2` · 0 of 2 report an effect size · 6 claims rest on one study

## Description
The article proposes evaluating the late pretest decision using a loss function approach grounded in the causal inference literature. This framework balances the precision gains from including pretest covariates against the bias risk when pretests are measured after random assignment. The article states it addresses the issue "using a loss function approach grounded in the causal inference literature," applying it to several commonly used impact estimators.

## Design Implications

### Context
#### Requirements
- Applicable to RCTs where pretest data may be collected after random assignment
#### Constraints
- Developed for education randomized control trials and commonly used impact estimators

### Target Learners
- Education researchers and evaluators designing randomized control trials

### Target Learning Objectives
- Improved precision and unbiasedness of estimated treatment effects in education RCTs

### Claims

- [Late Pretest Variance Bias Tradeoff](../claims/late-pretest-variance-bias-tradeoff.md) [+M]
- [The variance-bias trade-off for late pretests is addressed both theoretically and empirically for several commonly used impact estimators](../claims/late-pretest-analyzed-for-several-estimators.md) [+W]
- [Including late pretest data in RCT analyses can bias post-test impact estimates because pretests are collected after random assignment](../claims/late-pretest-inclusion-can-bias-posttest-estimates.md) [+W]
- [In RCTs of interventions to improve student test scores, estimators including late pretests will typically be preferred to estimators excluding them or using other baseline data](../claims/late-pretest-estimators-typically-preferred.md) [+W]
- [Including late pretest data in RCT analysis could bias post-test impact estimates when pretests are collected after random assignment](../claims/late-pretest-inclusion-can-bias-impact-estimates.md) [+W]
- [The late-pretest estimator preference holds as long as test score impacts do not grow very quickly early in the school year](../claims/late-pretest-preference-conditional-on-slow-early-impact-growth.md) [+W]

## Related Theories

- [Variance-bias tradeoff framework for deciding whether to use late pretest data in education RCTs](loss-function-decision-rule-for-late-pretest-use-in-education-rcts.md)
- [Neyman causal inference framework distinguishing finite-population and super-population models for clustered education RCTs](../theories/neyman-framework-clustered-rct-causal-models.md)
- [Suitability and feasibility framework for deciding whether to use state tests in education experiments](suitability-and-feasibility-framework-for-deciding-whether-to-use-state-tests-in-education.md)

## Examples
-

## Key Sources
- Peter Z. Schochet. (2010). The Late Pretest Problem in Randomized Control Trials of Education Interventions. Journal of Educational and Behavioral Statistics, vol. 35, no. 4. https://www.mathematica.org/publications/journal-article-the-late-pretest-problem-in-randomized-control-trials-of-education-interventions
-->

<!-- merged 2026-10-10 from theories/variance-bias-tradeoff-late-pretests ("Variance-bias tradeoff framework for deciding whether to use late pretest data in education RCTs"), misfiled as a theorie and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Variance-bias tradeoff framework for deciding whether to use late pretest data in education RCTs

> **Theory** · [All theories](index.md)
> **Evidence** · 6 claims (5 for, 1 mixed) · 2 studies (2 theoretical), `q2` · 0 of 2 report an effect size · 6 claims rest on one study

## Description
The paper organizes the late pretest decision as a tradeoff: including late pretest data improves the precision of estimated treatment effects but risks bias because the pretest may be treatment-contaminated. The author "addresses this issue both theoretically and empirically for several commonly used impact estimators, using a loss function approach grounded in the causal inference literature." The framework thus weighs precision gains against bias risk when choosing an impact estimator.

## Design Implications

### Context
#### Requirements
- A choice among "several commonly used impact estimators" for an RCT analysis, with information on pretest timing relative to random assignment
#### Constraints
- The tradeoff applies specifically to pretest data collected after random assignment, not to pretests collected before randomization

### Target Learners
- Education researchers and evaluators designing randomized control trials of education interventions

### Target Learning Objectives
- Accurate and precise estimation of education intervention effects on student test scores

### Claims

- [Late Pretest Inclusion Can Bias Impact Estimates](../claims/late-pretest-inclusion-can-bias-impact-estimates.md) [+M]
- [In RCTs of interventions to improve student test scores, estimators including late pretests will typically be preferred to estimators excluding them or using other baseline data](../claims/late-pretest-estimators-typically-preferred.md) [+W]
- [The late-pretest estimator preference holds as long as test score impacts do not grow very quickly early in the school year](../claims/late-pretest-preference-conditional-on-slow-early-impact-growth.md) [~W]
- [Deciding whether to collect and use late pretest data in RCTs involves a variance-bias trade-off](../claims/late-pretest-variance-bias-tradeoff.md) [+W]
- [The variance-bias trade-off for late pretests is addressed both theoretically and empirically for several commonly used impact estimators](../claims/late-pretest-analyzed-for-several-estimators.md) [+W]
- [Including late pretest data in RCT analyses can bias post-test impact estimates because pretests are collected after random assignment](../claims/late-pretest-inclusion-can-bias-posttest-estimates.md) [+W]

## Related Theories

- [A loss function approach grounded in the causal inference literature for evaluating late pretest use in RCTs](../research-methods/loss-function-decision-rule-for-late-pretest-use-in-education-rcts.md)
- [Suitability and feasibility framework for deciding whether to use state tests in education experiments](../research-methods/suitability-and-feasibility-framework-for-deciding-whether-to-use-state-tests-in-education.md)

## Examples
-

## Key Sources
- Peter Z. Schochet. (2008). The Late Pretest Problem in Randomized Control Trials of Education Interventions. Washington, DC: National Center for Education Evaluation and Regional Assistance, Institute of Education Sciences, U.S. Department of Education. https://ies.ed.gov/ncee
-->

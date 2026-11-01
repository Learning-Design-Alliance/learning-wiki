---
type: research-method
id: tame-detecting-treatment-effects-by-training-a-model-across-multiple-experiments-and-testi
title: TAME (detecting treatment effects by training a model across multiple experiments and testing residuals)
description: TAME is a statistical method for detecting treatment effects in randomized controlled experiments run inside online tutoring systems.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-01
---

# TAME (detecting treatment effects by training a model across multiple experiments and testing residuals)

> **Research Method** · [All research methods](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q2` · 1 of 1 report an effect size · 3 claims rest on one study

## Description
TAME is a statistical method for detecting treatment effects in randomized controlled experiments run inside online tutoring systems. It borrows the idea of meta-analysis: it first models the outcome measure in the absence of condition assignment, training on all experiments in a group except the test experiment, then computes residuals (actual minus modeled outcome) for the test experiment and runs a two-tailed unpaired T-test on residuals of control versus treatment groups. The sign of the residual matters: positive residuals indicate students overperformed the model, possibly due to helpful interventions, while negative residuals indicate underperformance, possibly caused by harmful interventions.

## Accounts
<!-- How each source describes or uses the method -->
- **TAME: detecting treatment effects by training a model across multiple experiments and testing residuals**: TAME is a statistical method for detecting treatment effects in randomized controlled experiments run inside online tutoring systems. It borrows the idea of meta-analysis: it first models the outcome measure in the absence of condition assignment, training on all experiments in a group except the test experiment, then computes residuals (actual minus modeled outcome) for the test experiment and runs a two-tailed unpaired T-test on residuals of control versus treatment groups. The sign of the residual matters: positive residuals indicate students overperformed the model, possibly due to helpful interventions, while negative residuals indicate underperformance, possibly caused by harmful interventions. (Thanaporn Patikorn et al. (2016))

### Claims

- [In resampled real data from the experiment with the strongest treatment effect, TAME detects the effect better than ANOVA especially when sample size is 40 or below](../claims/tame-resampling-experiment3-small-samples.md) [+W]
- [On real ASSISTments data, TAME and ANOVA agree on which experiments show significant treatment effects](../claims/tame-anova-agreement-real-assistments-data.md) [+W]
- [As the number of factors increases, TAME's power decreases less than ANOVA's, with a significant method-by-factors interaction](../claims/tame-power-degrades-less-with-more-factors.md) [+W]

## Related Research Methods

- [Multi-armed randomized trial analysis](multi-armed-randomized-trial-analysis.md)

## Key Sources
- Thanaporn Patikorn, Douglas Selent, Neil T. Heffernan, Joseph E. Beck, Jian Zou. (2016). Using a Single Model Trained across Multiple Experiments to Improve the Detection of Treatment Effects. Proceedings of the 10th International Conference on Educational Data Mining. https://sites.google.com/site/tamemethod/

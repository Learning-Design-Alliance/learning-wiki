---
type: research-method
id: probabilistic-peer-grading-models-pg1-pg2-pg3
title: Probabilistic peer grading models (PG1, PG2, PG3)
description: "The article introduces a family of Bayesian models in which each submission has a latent true score, each grader a bias (tendency to \"inﬂate or deﬂate her assessment\") and a reliability (precision of assessments after bias correction)."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-16
---

# Probabilistic peer grading models (PG1, PG2, PG3)

> **Research Method** · [All research methods](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The article introduces a family of Bayesian models in which each submission has a latent true score, each grader a bias (tendency to "inﬂate or deﬂate her assessment") and a reliability (precision of assessments after bias correction). PG1 places priors over these latents; PG2 adds temporal coherence of bias across assignments (consecutive-assignment bias correlation of 0.33); PG3 couples a grader's reliability to her own grade. Inference uses Gibbs sampling or EM, producing posterior belief distributions over grades rather than single scores.

## Accounts
<!-- How each source describes or uses the method -->
- **Probabilistic peer grading models (PG1, PG2, PG3) representing grader bias, reliability, temporal coherence, and coupled score-reliability**: The article introduces a family of Bayesian models in which each submission has a latent true score, each grader a bias (tendency to "inﬂate or deﬂate her assessment") and a reliability (precision of assessments after bias correction). PG1 places priors over these latents; PG2 adds temporal coherence of bias across assignments (consecutive-assignment bias correlation of 0.33); PG3 couples a grader's reliability to her own grade. Inference uses Gibbs sampling or EM, producing posterior belief distributions over grades rather than single scores. (Chris Piech et al. (2013))

### Claims
- [Probabilistic peer grading models that estimate grader bias and reliability reduce RMSE against ground-truth grades by 33% and 31% on two HCI course offerings](../claims/probabilistic-peer-grading-reduces-rmse-over-30-percent.md) [+M]
- [Estimating each grader's bias alone accounts for 95% of the RMSE reduction, while modeling grader reliability contributes little with only four grades per student](../claims/grader-bias-estimation-dominates-accuracy-gains.md) [+M]
- [The model's posterior confidence estimates are conservative: over 95% of predictions the model claims 90–95% confidence in are correct](../claims/peer-grading-confidence-estimates-conservative.md) [+M]

## Related Research Methods
-

## Key Sources
- Chris Piech, Jonathan Huang, Zhenghao Chen, Chuong Do, Andrew Ng, Daphne Koller. (2013). Tuned Models of Peer Assessment in MOOCs. arXiv. https://arxiv.org/abs/1307.2579

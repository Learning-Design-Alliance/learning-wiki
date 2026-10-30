---
type: claim
title: The two-fold training process suffers from overfitting due to the small labeled training set relative to feature dimensionality.
description: The two-fold training process suffers from overfitting due to the small labeled training set relative to feature dimensionality.
id: overfitting-from-small-labeled-set-and-high-dimensionality
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2018
recheck_by: 2021
sources:
  - id: yeung-2018
    resource: "https://arxiv.org/abs/1806.03256"
    title: "Yeung, C.-K., Lin, Z., Yang, K., & Yeung, D.-Y. (2018). Incorporating Features Learned by an Enhanced Deep Knowledge Tracing Model for STEM/Non-STEM Job Prediction. arXiv preprint arXiv:1806.03256. https://arxiv.org/abs/1806.03256"
    author: "Yeung, C.-K., Lin, Z., Yang, K., & Yeung, D.-Y."
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# The two-fold training process suffers from overfitting due to the small labeled training set relative to feature dimensionality.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`
> **Currency** · newest study 2018 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2021**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Training and test results differ significantly for the majority of models, demonstrating an overfitting issue the authors attribute to 467 training samples with up to 112 features and only around 374 students actually used per training fold. [→ Yeung 2018](#yeung-2018)

## Evidence

### Yeung 2018

Yeung, C.-K., Lin, Z., Yang, K., & Yeung, D.-Y. (2018). Incorporating Features Learned by an Enhanced Deep Knowledge Tracing Model for STEM/Non-STEM Job Prediction. arXiv preprint arXiv:1806.03256. https://arxiv.org/abs/1806.03256

`q2 · i?` · `associational · r1`

Observation from the ADM 2017 experiment results (Section 4.3, Table 2). The authors state "the training set consists of only 467 samples while the number of features used is up to 112", and that with 5-fold cross-validation "only around 374 students are actually used for training".

> "The overﬁtting issue may be attributed to the curse of dimension-ality, because the training set consists of only 467 samples while the number of features used is up to 112. Even worse, only around 374 students are actually used for training ow-ing to 5-fold cross-validation, leading to an inevitable bottle-neck for the performance of classiﬁer."

## Discussion


## Related Claims
- [Recursive feature elimination mitigates overfitting and improves STEM/non-STEM prediction performance, with LR-DKT&SP performing best after RFE.](rfe-mitigates-overfitting-in-stem-job-prediction.md) — related
- [The single-head base model (Model 1) outperformed the more complex Model 2, suggesting overfitting in the larger architecture](model1-outperforms-complex-model2.md) — related
- [Fold-local top-20 feature selection had mixed effects across model families, supporting the complete 166-dimensional representation as the primary analysis](feature-selection-effects-mixed-across-families.md) — related
- [Cross-validation-selected hyperparameters generalized to the test set only for Situation and Clarity, with the other four dimensions showing CV–test misalignment](cv-test-misalignment-small-imbalanced-data.md) — related

---
type: theory
title: Semi-supervised ANN framework combining ANNs with DINA and DINO diagnostic classification models
description: The article proposes a framework that combines artificial neural networks with two typical theoretical diagnostic classification models, the DINA model and the DINO model, within a semi-supervised learning framework.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
sources:
  - id: kang-xue-2021
    resource: "https://www.frontiersin.org/journals/psychology"
    title: "Kang Xue, Laine Bradshaw. (2021). A semi-supervised learning-based diagnostic classification method using artificial neural networks. Frontiers in Psychology, 11, 3992. https://www.frontiersin.org/journals/psychology"
    author: Kang Xue, Laine Bradshaw
---

# Semi-supervised ANN framework combining ANNs with DINA and DINO diagnostic classification models

> **Theory** · [All theories](index.md)
> **Evidence** · 3 claims (1 for, 2 mixed) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The article proposes a framework that combines artificial neural networks with two typical theoretical diagnostic classification models, the DINA model and the DINO model, within a semi-supervised learning framework. Its purpose is to convert a pattern of item responses into a diagnostic classification robustly and accurately, addressing instability the authors attribute to earlier ANN approaches. The authors state this is "the first time of applying the thinking of semi-supervised learning into CDM".

## Design Implications

### Context
#### Requirements
- Requires combining the ANN with a theoretical diagnostic classification model (DINA or DINO) within a semi-supervised learning framework
#### Constraints
- Earlier ANN methods, per the authors, produced very unstable and unappreciated estimation unless a great deal of care was taken, motivating the framework's care in parameter selection

### Target Learners
- students assessed with diagnostic classification assessments

### Target Learning Objectives
- classification of students' latent attribute profiles from diagnostic assessment responses

### Claims

- [Semi Supervised Ann Cdm Robust Classification](../claims/semi-supervised-ann-cdm-robust-classification.md) [+M]
- [Prior ANN approaches to diagnostic classification produced unstable and unappreciated estimation unless great care was taken](../claims/prior-ann-cdm-unstable-estimation.md) [~W]
- [Misspecification of theoretical diagnostic classification models and inaccurate Q-matrices impact classification accuracy](../claims/tdcm-qmatrix-misspecification-hurts-classification.md) [~W]

## Related Theories
- 

## Examples

- [Choose ANN parameters with a validating test instead of typical statistical criteria such as AIC or BIC](../strategies/validating-test-ann-parameter-selection.md)

## Key Sources
- Kang Xue, Laine Bradshaw. (2021). A semi-supervised learning-based diagnostic classification method using artificial neural networks. Frontiers in Psychology, 11, 3992. https://www.frontiersin.org/journals/psychology

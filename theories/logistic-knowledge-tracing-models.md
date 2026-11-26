---
type: theory
id: logistic-knowledge-tracing-models
title: Logistic Knowledge Tracing Models (LFA, PFA, KTM)
description: "The survey's logistic branch covers Learning Factor Analysis, Performance Factor Analysis and Knowledge Tracing Machines."
canonical: true
status: review
generated:
  by: claude/unspecified
  at: 2026-09-24
sources:
  - id: shuanghong-shen-2021
    resource: "https://arxiv.org/abs/2105.15106"
    title: "Shuanghong Shen, Qi Liu, Zhenya Huang, Yonghe Zheng, Minghao Yin, Minjuan Wang, and Enhong Chen. (2021). A Survey of Knowledge Tracing: Models, Variants, and Applications. https://arxiv.org/abs/2105.15106"
    author: Shuanghong Shen, Qi Liu, Zhenya Huang, Yonghe Zheng, Minghao Yin, Minjuan Wang, and Enhong Chen
---

# Logistic Knowledge Tracing Models (LFA, PFA, KTM)

> **Theory** · [All theories](index.md)
> **Evidence** · 5 claims (4 for, 1 mixed) · 3 studies (2 associational, 1 design), `q2` · 0 of 3 report an effect size · 5 claims rest on one study

## Description
The survey's logistic branch covers Learning Factor Analysis, Performance Factor Analysis and Knowledge Tracing Machines. "Logistic models represent the probability of students cor- rectly answering exercises as a logistic function of the student and KC parameters." LFA uses initial knowledge, KC easiness and KC learning rate; PFA uses prior failures, prior successes and KC easiness; KTM uses factorization machines to encode side information about exercises or students.

## Design Implications

### Context
#### Requirements
- Factors estimated from students' learning interactions (e.g., prior successes and failures on a KC, KC easiness) combined through a logistic (sigmoid) function
#### Constraints
- The survey notes the original PFA model ignores the order of answers and the time between learning interactions, making it difficult to incorporate time information directly

### Target Learners
- Students whose exercise-answering interactions are recorded by online learning systems such as ASSISTments, Junyi Academy, Eedi and EdNet's Santa tutor

### Target Learning Objectives
- Monitoring students' evolving knowledge states on knowledge concepts and predicting performance on future exercises

### Claims

- [EPFA estimates fewer trials to mastery for above-average students and more trials for below-average students relative to standard PFA](../claims/epfa-mastery-trials-by-student-level.md) [~W]
- [LFA finds alternative cognitive models with better statistical fit than the original Geometry Area Unit model](../claims/lfa-improves-cognitive-model-fit.md) [+W] — attached 2026-11-23 from Hao Cen et al. (2005), which proposed "Learning Factors Analysis: a semi-automated method combining a statistical model, difficulty factors, and A* search for cognitive model improvement".
- [LFA detects hidden knowledge components as learning-curve blips without visual inspection, as in the Compose-by-multiplication split](../claims/lfa-detects-hidden-blip-cm-split.md) [+W] — attached 2026-11-23 from Hao Cen et al. (2005), which proposed "Learning Factors Analysis: a semi-automated method combining a statistical model, difficulty factors, and A* search for cognitive model improvement".
- [KT predicts much worse performance after a failure than PFA, with observed data falling between the two but much closer to PFA](../claims/kt-overestimates-failure-impact.md) [+W] — attached 2026-11-26 from Pavlik Jr. et al. (2009), which proposed "Performance Factors Analysis (PFA): a logistic model using prior successes and failures per KC to create an adaptive model overlay"; tests this page's relationship.
- [Across four tutor datasets, the PFA model achieves better LL, BIC, r and A' than two knowledge tracing variants, though the differences are not large](../claims/pfa-outperforms-kt-fit-four-datasets.md) [+W] — attached 2026-11-26 from Pavlik Jr. et al. (2009), which proposed "Performance Factors Analysis (PFA): a logistic model using prior successes and failures per KC to create an adaptive model overlay"; tests this page's relationship.

## Related Theories
- [Knowledge Tracing Model Taxonomy](knowledge-tracing-model-taxonomy.md)

## Examples
-

## Key Sources
- Shuanghong Shen, Qi Liu, Zhenya Huang, Yonghe Zheng, Minghao Yin, Minjuan Wang, and Enhong Chen. (2021). A Survey of Knowledge Tracing: Models, Variants, and Applications. https://arxiv.org/abs/2105.15106

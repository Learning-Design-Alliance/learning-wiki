---
type: theory
title: Logistic Knowledge Tracing Models (LFA, PFA, KTM)
description: "The survey's logistic branch covers Learning Factor Analysis, Performance Factor Analysis and Knowledge Tracing Machines."
status: draft
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
- 

## Related Theories
- [Knowledge Tracing Model Taxonomy](knowledge-tracing-model-taxonomy.md)

## Examples
-

## Key Sources
- Shuanghong Shen, Qi Liu, Zhenya Huang, Yonghe Zheng, Minghao Yin, Minjuan Wang, and Enhong Chen. (2021). A Survey of Knowledge Tracing: Models, Variants, and Applications. https://arxiv.org/abs/2105.15106

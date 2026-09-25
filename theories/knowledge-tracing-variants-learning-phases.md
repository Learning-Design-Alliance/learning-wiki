---
type: theory
title: Four-Phase Taxonomy of Knowledge Tracing Variants
description: "The survey's second organizing axis groups extensions of the fundamental models by the learning phase they add: \"we classify and review current variants of fundamental KT models into four categories\" — individualizati..."
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

# Four-Phase Taxonomy of Knowledge Tracing Variants

> **Theory** · [All theories](index.md)

## Description
The survey's second organizing axis groups extensions of the fundamental models by the learning phase they add: "we classify and review current variants of fundamental KT models into four categories" — individualization before learning, engagement during learning, forgetting after learning, and side information across learning. Examples include student-node BKT and DKT-DSC clustering, KAT and EEG-BKT, BKT-Forget and DKT-forget, and FAST and EKT.

## Design Implications

### Context
#### Requirements
- Data beyond exercises and responses: student-specific parameters or clusters, engagement signals (EEG or behavioral indicators such as quick guess and bottom-out hints), time gaps and trial counts, or side information such as response time, tutor intervention, exercise text and code submissions
#### Constraints
- The survey motivates the variants by stating the fundamental KT models, while straightforward, may have reduced performance in real-world learning scenarios

### Target Learners
- Students whose exercise-answering interactions are recorded by online learning systems such as ASSISTments, Junyi Academy, Eedi and EdNet's Santa tutor

### Target Learning Objectives
- Monitoring students' evolving knowledge states on knowledge concepts and predicting performance on future exercises

### Claims
- [Individualized Bkt Reduces Questions Needed For Mastery](../claims/individualized-bkt-reduces-questions-needed-for-mastery.md) [+W]
- [Engagement Covariates Improve Deep Knowledge Tracing](../claims/engagement-covariates-improve-deep-knowledge-tracing.md) [+W]
- [Bkt Overestimates Accuracy After A Day Elapses](../claims/bkt-overestimates-accuracy-after-a-day-elapses.md) [+W]
- [Language Proficiency Side Information Improves Kt Models](../claims/language-proficiency-side-information-improves-kt-models.md) [+W]

## Related Theories
- [Knowledge Tracing Model Taxonomy](knowledge-tracing-model-taxonomy.md)
- [Engagement](../principles/engagement.md)

## Examples
-

## Key Sources
- Shuanghong Shen, Qi Liu, Zhenya Huang, Yonghe Zheng, Minghao Yin, Minjuan Wang, and Enhong Chen. (2021). A Survey of Knowledge Tracing: Models, Variants, and Applications. https://arxiv.org/abs/2105.15106

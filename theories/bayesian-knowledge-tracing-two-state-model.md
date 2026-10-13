---
type: theory
title: Bayesian Knowledge Tracing (Two-State Hidden Markov Model)
description: The survey describes Bayesian Knowledge Tracing (BKT), introduced by Corbett and Anderson, as a special case of the Hidden Markov Model with learning parameters (transition, forgetting) and performance parameters (gue...
canonical: true
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

# Bayesian Knowledge Tracing (Two-State Hidden Markov Model)

> **Theory** · [All theories](index.md)
> **Evidence** · 5 claims (2 for, 2 mixed, 1 against) · 3 studies (1 causal, 1 review, 1 design), `q2` · 0 of 3 report an effect size · 5 claims rest on one study

## Description
The survey describes Bayesian Knowledge Tracing (BKT), introduced by Corbett and Anderson, as a special case of the Hidden Markov Model with learning parameters (transition, forgetting) and performance parameters (guess, slip) plus an initial mastery probability. "BKT operates within a two-state student modeling framework: knowledge is either learned or unlearned, and there is no forgetting once a student has mastered the knowledge." Dynamic Bayesian knowledge tracing extends it to model hierarchies and relationships among knowledge concepts jointly.

## Design Implications

### Context
#### Requirements
- Per-knowledge-concept parameters: initial probability of mastery, transition probability, guessing probability and slipping probability
- Observed correct/incorrect answers used to update the posterior probability of mastery
#### Constraints
- Standard BKT models the parameters of each knowledge concept independently, although the survey notes knowledge concepts are hierarchical and closely related
- Fundamental models such as BKT often overlook forgetting

### Target Learners
- Students whose exercise-answering interactions are recorded by online learning systems such as ASSISTments, Junyi Academy, Eedi and EdNet's Santa tutor

### Target Learning Objectives
- Monitoring students' evolving knowledge states on knowledge concepts and predicting performance on future exercises

### Claims

- [Bkt Overestimates Accuracy After A Day Elapses](../claims/bkt-overestimates-accuracy-after-a-day-elapses.md) [-W]
- [Individualized Bkt Reduces Questions Needed For Mastery](../claims/individualized-bkt-reduces-questions-needed-for-mastery.md) [+W]
- [The survey reports, citing Desmarais and Baker, that students using the BKT-sequence recommendation algorithm solved more difficult exercises, obtained higher performance and spent more time in the system than students using the traditional approach.](../claims/bkt-sequence-recommendation-students-solved-harder-exercises.md) [+W]
- [No credible spacing or color cue effects on the BKT learning rate were observed in the perceptual-cue reanalysis](../claims/no-credible-cue-effects-learning-rate.md) [~W]
- [In simulated online mastery learning, BKT gave the fewest problems, Streak the second fewest, Random the most, and DKT gave almost as many as Random in one problem type and the least in the other two](../claims/problem-counts-by-knowledge-tracing-condition.md) [~W]

## Related Theories

- [Knowledge Tracing Model Taxonomy](knowledge-tracing-model-taxonomy.md)
- Mastery Learning
- [Bayesian Knowledge Tracing: a four-parameter student-learning model in two forms (HMM and Knowledge Tracing Algorithm)](bkt-four-parameter-two-form-model.md)
- [Bayesian Knowledge Tracing: a two-state Hidden Markov Model inferring skill mastery from response histories](bkt-two-state-hmm-student-model.md)
- [Two hypotheses for the meaning of Spectral BKT's intermediate states: a stages-of-mastery account and a mastery-by-metacognition interaction account](spectral-bkt-intermediate-state-hypotheses.md)
- [BKT+IRT: Bayesian Knowledge Tracing augmented with multidimensional generalizable student abilities and problem effects](bkt-irt-multidimensional-generalizable-model.md)
- [Bayesian Knowledge Tracing as a model of changing skill mastery during game-based assessment](bkt-mastery-updating-model.md)
- [Intervention-BKT: a BKT extension that models the effect of instructional interventions on student knowledge states](intervention-bkt-model.md)

## Examples

- [BKT RNN: a fast, flexible PyTorch recurrent neural network implementation of Bayesian Knowledge Tracing](../research-methods/bkt-rnn.md)

## Key Sources
- Shuanghong Shen, Qi Liu, Zhenya Huang, Yonghe Zheng, Minghao Yin, Minjuan Wang, and Enhong Chen. (2021). A Survey of Knowledge Tracing: Models, Variants, and Applications. https://arxiv.org/abs/2105.15106

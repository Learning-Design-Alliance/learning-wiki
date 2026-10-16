---
type: theory
title: Bayesian Knowledge Tracing (Two-State Hidden Markov Model)
description: The survey describes Bayesian Knowledge Tracing (BKT), introduced by Corbett and Anderson, as a special case of the Hidden Markov Model with learning parameters (transition, forgetting) and performance parameters (gue...
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
  - id: martori-2015
    resource: "https://www.educationaldatamining.org/EDM2015/proceedings/short364-367.pdf"
    title: "Martori, F., Cuadros, J., & González-Sabaté, L. (2015). Direct estimation of the minimum RSS value for training Bayesian Knowledge Tracing parameters. Proceedings of the 8th International Conference on Educational Data Mining. https://www.educationaldatamining.org/EDM2015/proceedings/short364-367.pdf"
    author: "Martori, F., Cuadros, J., & González-Sabaté, L"
---

# Bayesian Knowledge Tracing (Two-State Hidden Markov Model)

> **Theory** · [All theories](index.md)
> **Evidence** · 8 claims (4 for, 2 mixed, 2 against) · 6 studies (2 causal, 2 design, 1 review, 1 theoretical), `q1`–`q3` · 0 of 6 report an effect size · 8 claims rest on one study

## Description
The survey describes Bayesian Knowledge Tracing (BKT), introduced by Corbett and Anderson, as a special case of the Hidden Markov Model with learning parameters (transition, forgetting) and performance parameters (guess, slip) plus an initial mastery probability. "BKT operates within a two-state student modeling framework: knowledge is either learned or unlearned, and there is no forgetting once a student has mastered the knowledge." Dynamic Bayesian knowledge tracing extends it to model hierarchies and relationships among knowledge concepts jointly.

## Design Implications

### Context
#### Requirements
- Per-knowledge-concept parameters: initial probability of mastery, transition probability, guessing probability and slipping probability
- Observed correct/incorrect answers used to update the posterior probability of mastery
- Response data tagged with the skills the instructor wants students to learn
- A history of student responses to problems (typically first attempts only)
- Values for the four probabilities L0, T, G, and S
#### Constraints
- Standard BKT models the parameters of each knowledge concept independently, although the survey notes knowledge concepts are hierarchical and closely related
- Fundamental models such as BKT often overlook forgetting
- The knowledge state is absorbent: the model assumes the student will not forget the skill once learned
- Usually a separate BKT model is fit for each skill

### Target Learners
- Students whose exercise-answering interactions are recorded by online learning systems such as ASSISTments, Junyi Academy, Eedi and EdNet's Santa tutor
- students in online/cognitive-tutor courses (e.g., MOOC students)

### Target Learning Objectives
- Monitoring students' evolving knowledge states on knowledge concepts and predicting performance on future exercises
- inferring mastery of instructor-tagged skills
- predicting future student performance

### Claims

- [Bkt Overestimates Accuracy After A Day Elapses](../claims/bkt-overestimates-accuracy-after-a-day-elapses.md) [-W]
- [Individualized Bkt Reduces Questions Needed For Mastery](../claims/individualized-bkt-reduces-questions-needed-for-mastery.md) [+W]
- [The survey reports, citing Desmarais and Baker, that students using the BKT-sequence recommendation algorithm solved more difficult exercises, obtained higher performance and spent more time in the system than students using the traditional approach.](../claims/bkt-sequence-recommendation-students-solved-harder-exercises.md) [+W]
- [No credible spacing or color cue effects on the BKT learning rate were observed in the perceptual-cue reanalysis](../claims/no-credible-cue-effects-learning-rate.md) [~W]
- [In simulated online mastery learning, BKT gave the fewest problems, Streak the second fewest, Random the most, and DKT gave almost as many as Random in one problem type and the least in the other two](../claims/problem-counts-by-knowledge-tracing-condition.md) [~W]
- [Adaptive scaffolding policies (BKT and DRL) significantly improve posttest performance over a non-adaptive control in a logic ITS](../claims/adaptive-icap-scaffolding-improves-posttest-logic-tutor.md) [+W]
- [Individualizing the initial knowledge parameter reliably improves prediction of real-world data](../claims/individualizing-initial-knowledge-improves-prediction.md) [+W] — attached 2026-10-14 from Pardos et al. (2010), which proposed "Individualized Bayesian knowledge tracing framework".
- [The exponential functional form of the BKT HMM calls into question the popular practice of fitting that model form to student data](../claims/bkt-hmm-exponential-form-questions-fitting-practice.md) [-W]

## The evidence by question
- *Does choosing practice or scaffolding by BKT's mastery estimate improve learning or reduce the practice needed, compared with fixed or random sequencing, and for whom?* [Adaptive scaffolding policies (BKT and DRL) significantly improve posttest performance over a non-adaptive control in a logic ITS](../claims/adaptive-icap-scaffolding-improves-posttest-logic-tutor.md) [+M]
- *How accurately does BKT predict a learner's next answers, compared with other knowledge-tracing models, and do its assumptions and fitted parameters hold up?* [The survey states that deep learning knowledge tracing models exhibit superior performance to Bayesian and logistic models but have significant room for improvement in interpretability.](../claims/deep-learning-knowledge-tracing-outperforms-but-lacks-interpretability.md) [~M]

## Related Theories

- [Knowledge Tracing Model Taxonomy](knowledge-tracing-model-taxonomy.md)
- Mastery Learning
- [Bayesian Knowledge Tracing: a four-parameter student-learning model in two forms (HMM and Knowledge Tracing Algorithm)](bkt-four-parameter-two-form-model.md)
- [Two hypotheses for the meaning of Spectral BKT's intermediate states: a stages-of-mastery account and a mastery-by-metacognition interaction account](spectral-bkt-intermediate-state-hypotheses.md)
- [BKT+IRT: Bayesian Knowledge Tracing augmented with multidimensional generalizable student abilities and problem effects](bkt-irt-multidimensional-generalizable-model.md)
- [Bayesian Knowledge Tracing as a model of changing skill mastery during game-based assessment](bkt-mastery-updating-model.md)
- [Intervention-BKT: a BKT extension that models the effect of instructional interventions on student knowledge states](intervention-bkt-model.md)
- [BKT Brute Force (BKT-BF): grid-search parameter estimation minimizing Residual Sum of Squares](bkt-brute-force-grid-search-estimation.md)
- [Spectral BKT: a BKT variant combining feature compensation (3-gram observations) with model compensation (four latent states)](spectral-bkt-model.md)
- [BKTransformer: transformer-based generation of temporally-evolving BKT parameters](bktransformer-temporal-bkt-parameters.md)

## Examples

- [BKT RNN: a fast, flexible PyTorch recurrent neural network implementation of Bayesian Knowledge Tracing](../research-methods/bkt-rnn.md)
- [Fit the combined parameter A and fix P(G) or P(L0) externally as an alternative to Dirichlet priors when fitting the BKT HMM](../strategies/fit-a-fix-one-parameter-alternative-to-dirichlet-priors.md)

## Key Sources
- Shuanghong Shen, Qi Liu, Zhenya Huang, Yonghe Zheng, Minghao Yin, Minjuan Wang, and Enhong Chen. (2021). A Survey of Knowledge Tracing: Models, Variants, and Applications. https://arxiv.org/abs/2105.15106
- Martori, F., Cuadros, J., & González-Sabaté, L. (2015). Direct estimation of the minimum RSS value for training Bayesian Knowledge Tracing parameters. Proceedings of the 8th International Conference on Educational Data Mining. https://www.educationaldatamining.org/EDM2015/proceedings/short364-367.pdf

<!-- merged 2026-10-15 from theories/bkt-two-state-hmm-student-model ("Bayesian Knowledge Tracing: a two-state Hidden Markov Model inferring skill mastery from response histories"), a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Bayesian Knowledge Tracing: a two-state Hidden Markov Model inferring skill mastery from response histories

> **Theory** · [All theories](index.md)
> **Evidence** · 1 claim (1 against) · 1 study (1 theoretical), `q1` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
Bayesian Knowledge Tracing (BKT) is a student model used to infer a student's knowledge from their history of responses to skill-tagged problems and to predict future performance. It is "a two state Hidden Markov Model", with states for knowing and not knowing a skill, and an absorbent knowledge state implying no forgetting. It requires four probabilities: L0 (prior knowledge), T (transition/learning probability per practice opportunity), G (guess rate), and S (slip rate). Knowledge affects performance mediated by guess and slip rates, and knowledge at one time step affects knowledge at the next. Usually a separate BKT model is fit per skill using only first attempts.

## Design Implications

### Context
#### Requirements
- Response data tagged with the skills the instructor wants students to learn
- A history of student responses to problems (typically first attempts only)
- Values for the four probabilities L0, T, G, and S
#### Constraints
- The knowledge state is absorbent: the model assumes the student will not forget the skill once learned
- Usually a separate BKT model is fit for each skill

### Target Learners
- students in online/cognitive-tutor courses (e.g., MOOC students)

### Target Learning Objectives
- inferring mastery of instructor-tagged skills
- predicting future student performance

### Claims

- [The exponential functional form of the BKT HMM calls into question the popular practice of fitting that model form to student data](../claims/bkt-hmm-exponential-form-questions-fitting-practice.md) [-W]

## Related Theories

- [Bayesian Knowledge Tracing: a four-parameter student-learning model in two forms (HMM and Knowledge Tracing Algorithm)](bkt-four-parameter-two-form-model.md)
- [Bayesian Knowledge Tracing (Two-State Hidden Markov Model)](bayesian-knowledge-tracing-two-state-model.md)
- [BKT Brute Force (BKT-BF): grid-search parameter estimation minimizing Residual Sum of Squares](bkt-brute-force-grid-search-estimation.md)
- [Spectral BKT: a BKT variant combining feature compensation (3-gram observations) with model compensation (four latent states)](spectral-bkt-model.md)
- [BKTransformer: transformer-based generation of temporally-evolving BKT parameters](bktransformer-temporal-bkt-parameters.md)
- [BKT+IRT: Bayesian Knowledge Tracing augmented with multidimensional generalizable student abilities and problem effects](bkt-irt-multidimensional-generalizable-model.md)
- [Bayesian Knowledge Tracing as a model of changing skill mastery during game-based assessment](bkt-mastery-updating-model.md)
- [Intervention-BKT: a BKT extension that models the effect of instructional interventions on student knowledge states](intervention-bkt-model.md)

## Examples

- [Fit the combined parameter A and fix P(G) or P(L0) externally as an alternative to Dirichlet priors when fitting the BKT HMM](../strategies/fit-a-fix-one-parameter-alternative-to-dirichlet-priors.md)
- [BKT RNN: a fast, flexible PyTorch recurrent neural network implementation of Bayesian Knowledge Tracing](../research-methods/bkt-rnn.md)

## Key Sources
- Martori, F., Cuadros, J., & González-Sabaté, L. (2015). Direct estimation of the minimum RSS value for training Bayesian Knowledge Tracing parameters. Proceedings of the 8th International Conference on Educational Data Mining. https://www.educationaldatamining.org/EDM2015/proceedings/short364-367.pdf
-->

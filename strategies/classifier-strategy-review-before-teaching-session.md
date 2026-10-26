---
type: strategy
id: classifier-strategy-review-before-teaching-session
title: Use the trained classifier to review recommended teacher communication strategies for specific interaction scenarios before a teaching session.
description: The article proposes that teachers, in advance of a lesson, input scenario variables (student attributes, teaching type, context, emotional state, past response) into the trained GP classifier and review its ranked pr...
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-26
sources:
  - id: vasileios-lampos-2021
    resource: "https://doi.org/10.1038/s41539-021-00102-x"
    title: "Vasileios Lampos, Joseph Mintz and Xiao Qu (2021). An artificial intelligence approach for selecting effective teacher communication strategies in autism education. npj Science of Learning 6:25. https://doi.org/10.1038/s41539-021-00102-x"
    author: Vasileios Lampos, Joseph Mintz and Xiao Qu
---

# Use the trained classifier to review recommended teacher communication strategies for specific interaction scenarios before a teaching session.

> **Strategy** · [All strategies](index.md)
> **Evidence** · 6 claims (6 for) · 1 study (1 associational), `q2` · 1 of 1 report an effect size · 6 claims rest on one study

## Description
The article proposes that teachers, in advance of a lesson, input scenario variables (student attributes, teaching type, context, emotional state, past response) into the trained GP classifier and review its ranked probabilities of full student response for each communication strategy or pair. As the authors put it, "teachers, in advance of a teaching session, to input specific variables, as in Fig. 2, relating to real-world scenarios in the classroom" and "then review the recommendations of the model for specific teacher communications". The model outputs relative rankings of communication options conditioned on the scenario, illustrated with a simulated out-of-sample scenario in Fig. 2.

## Design Implications

### Context
#### Requirements
- The classifier must be trained on coded in-vivo observation data of teacher-student interactions including student attributes and past responses.
- Teachers must be able to specify the scenario variables for a specific child with specific attributes and conditions.
#### Constraints
- The study is exploratory, based on a cohort of seven students, and claims of generalisation need caution.
- The conditional probabilities produced by the classifier may have biased face values; the approach relies on their relative ranking.
- Student attribute data are educational indicators, not standardised clinical metrics.

### Target Learners
- primary-school students with autism spectrum condition

### Target Learning Goals
- improving student responsiveness to classroom instruction
- supporting teacher decisions about communication strategy selection for effective inclusion

## Claims

- [Adding student attributes and autoregression improves prediction accuracy, with GP-α (τ = 1) reaching 0.711 accuracy and 0.757 F1.](../claims/attributes-autoregression-improve-response-prediction.md) [+W]
- [Omitting the teacher's communication strategy causes the greatest drop in classifier accuracy, marking communication choice as the most impactful feature category.](../claims/communication-strategy-most-impactful-ablation.md) [+W]
- [In the classifier's expanded sample of over 2.6 million observations, negative student emotional state (r = −0.431) and physical prompt communication (r = 0.341) show the strongest correlations with full student response.](../claims/expanded-sample-correlations-emotion-physical-prompt.md) [+M]
- [Machine-learning classifiers predict full student response to teacher communication in autism classrooms above random and major-class baselines.](../claims/ml-predicts-student-response-autism-communication.md) [+W]
- [Teachers' prompt-hierarchy hypothesis is not supported: after unsuccessful communication, physical prompts are not the most common subsequent choice (probability 0.310).](../claims/prompt-hierarchy-hypothesis-not-supported.md) [+W]
- [Performing two teacher communications rather than one is more effective in producing full student responses (60.01% vs 50.58%).](../claims/two-communications-more-effective-than-one.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Vasileios Lampos, Joseph Mintz and Xiao Qu (2021). An artificial intelligence approach for selecting effective teacher communication strategies in autism education. npj Science of Learning 6:25. https://doi.org/10.1038/s41539-021-00102-x

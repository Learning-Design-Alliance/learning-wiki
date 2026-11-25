---
type: strategy
id: pj-spikes-refine-mastery-assessment
title: Use P(J) learning spikes to refine mastery assessment in ASSISTments so that students stop receiving over-practice after mastery is reached
description: The authors propose that the moment-of-learning signal can improve intelligent tutoring system mastery methodology.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-25
sources:
  - id: baker-2011
    resource: "https://doi.org/10.3233/JAI-2011-015"
    title: "Baker, Ryan S.J.d., Goldstein, Adam B., Heffernan, Neil T. (2011). Detecting Learning Moment-by-Moment. International Journal of Artificial Intelligence in Education. In Press. https://doi.org/10.3233/JAI-2011-015"
    author: Baker, Ryan S.J.d., Goldstein, Adam B., Heffernan, Neil T
---

# Use P(J) learning spikes to refine mastery assessment in ASSISTments so that students stop receiving over-practice after mastery is reached

> **Strategy** · [All strategies](index.md)
> **Evidence** · 6 claims (6 for) · 1 study (1 associational), `q2` · 1 of 1 report an effect size · 6 claims rest on one study

## Description
The authors propose that the moment-of-learning signal can improve intelligent tutoring system mastery methodology. In their data, a student kept receiving practice after reaching mastery by Bayesian Knowledge Tracing; the P(J) spike occurred several actions before P(Ln) reached mastery level. Their hypothesis is that P(J) can refine Bayesian Knowledge Tracing "so that the estimate of mastery goes up more, when spikes occur, than simply what would be indicated by the model's skill-level estimate of P(T)".

## Design Implications

### Context
#### Requirements
- Addition of Bayesian Knowledge Tracing into ASSISTments
- Well-fit Bayesian Knowledge Tracing parameter values
#### Constraints
- Using P(J) overly aggressively risks under-practice: a spike does not imply learning is complete, since a student may need more practice to maintain long-term memory.
- P(J) does not drop to 0 immediately after a spike; more work is needed to determine how much additional practice is needed after a spike for learning to be maintained.

### Target Learners
- Middle school and high school mathematics students using ASSISTments

### Target Learning Goals
- Accurate mastery assessment and appropriate amounts of practice on mathematics knowledge components

### Affordances
- [Pj Moment Of Learning Model](../theories/bayesian-knowledge-tracing-two-state-model.md)

## Claims

- [Incorrect answers show a positive association with momentary learning in both systems, and past errors predict more current learning than past help requests in the Cognitive Tutor.](../claims/errors-positively-associated-with-momentary-learning.md) [+W]
- [An expanded 67-feature model of P(J) gave only a minor correlation improvement over the original feature set in ASSISTments.](../claims/expanded-feature-set-minor-improvement.md) [+W]
- [Spikiness varies more between knowledge components than between students, and some high spikiness in the Cognitive Tutor comes from very easy KCs.](../claims/kc-spikiness-varies-more-than-student-spikiness.md) [+W]
- [Machine-learned P(J) models predict moment-of-learning training labels with cross-validated correlations around 0.40-0.45 in two intelligent tutoring systems.](../claims/pj-model-predicts-moment-of-learning-labels.md) [+W]
- [The P(J) models predict learning rather than merely current non-knowledge: excluding Ln and Ln-1 yields significantly lower cross-validated correlations.](../claims/pj-models-not-just-predicting-non-knowledge.md) [+W]
- [A student's spikiness of momentary learning predicts their final knowledge in both tutoring systems.](../claims/spikiness-predicts-final-knowledge.md) [+M]

## Related Strategies
- 

## Examples
-

## Key Sources
- Baker, Ryan S.J.d., Goldstein, Adam B., Heffernan, Neil T. (2011). Detecting Learning Moment-by-Moment. International Journal of Artificial Intelligence in Education. In Press. https://doi.org/10.3233/JAI-2011-015

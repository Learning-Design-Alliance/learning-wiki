---
type: design
id: ace-dbn-student-model-gaze-time-predictors
title: "ACE's Dynamic Bayesian Network student model with gaze-shift and time nodes as independent predictors of implicit self-explanation"
description: "ACE's student model is a Dynamic Bayesian Network that assesses exploratory behavior at multiple levels of granularity (exploration cases, exercises, units, and categories) together with knowledge nodes."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-16
sources:
  - id: christina-merten-and-cristina-conati-2005
    resource: "https://www.cs.ubc.ca"
    title: "Christina Merten and Cristina Conati. (2005). Eye-Tracking to Model and Adapt to User Meta-cognition in Intelligent Learning Environments. https://www.cs.ubc.ca"
    author: Christina Merten and Cristina Conati
---

# ACE's Dynamic Bayesian Network student model with gaze-shift and time nodes as independent predictors of implicit self-explanation

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
ACE's student model is a Dynamic Bayesian Network that assesses exploratory behavior at multiple levels of granularity (exploration cases, exercises, units, and categories) together with knowledge nodes. The revised model separates the causes of implicit self-explanation from its effects, encoding gaze shifts and time on action "as independent predictors as in a naïve Bayesian classifier". This structure is highly modular, allowing the gaze shift and time nodes to be used or ignored as needed, and facilitates learning the conditional probability tables from data.

## Design Implications

### Context
#### Requirements
- Conditional probability tables for the time and gaze shift nodes derived from user-study data frequencies
- A threshold over implicitSE node probabilities, set via ROC analysis over training data
#### Constraints
- The structure assumes independence between time and the presence of gaze shifts, which the data suggests is not strictly true (a small positive correlation)
- The model does not currently include the coach's hint-to-self-explain nodes because no hint data was available from the user study

### Target Learners
- University students learning mathematical functions through exploration

### Learning Goals
- Effective exploratory learning of mathematical functions
- Self-explanation of instructional material

### Claims
- [Eye Tracking Improves Implicit Se Assessment](../claims/eye-tracking-improves-implicit-se-assessment.md) [+M]
- [Se Assessment Improves Exploration Assessment](../claims/se-assessment-improves-exploration-assessment.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Christina Merten and Cristina Conati. (2005). Eye-Tracking to Model and Adapt to User Meta-cognition in Intelligent Learning Environments. https://www.cs.ubc.ca

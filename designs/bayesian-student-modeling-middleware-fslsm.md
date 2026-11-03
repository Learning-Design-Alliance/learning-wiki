---
type: design
id: bayesian-student-modeling-middleware-fslsm
title: Bayesian student modeling middleware based on FSLSM with dynamic threshold updating
description: "A machine-learning student modeling middleware that records \"the learning scene itself, the usage of mouse and keyboard, and the period of time that the learning scene is active\" as three evidence nodes and processes..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-03
sources:
  - id: burak-galip-aslan-2014
    resource: "https://doi.org/10.12738/estp.2014.3.1587"
    title: "Burak Galip Aslan, Özlem Öztürk, Mustafa Murat İnceoğlu. (2014). Effect of Bayesian Student Modeling on Academic Achievement in Foreign Language Teaching (University Level English Preparatory School Example). Educational Sciences: Theory & Practice, 14(3). https://doi.org/10.12738/estp.2014.3.1587"
    author: Burak Galip Aslan, Özlem Öztürk, Mustafa Murat İnceoğlu
---

# Bayesian student modeling middleware based on FSLSM with dynamic threshold updating

> **Design** · [All designs](index.md)
> **Evidence** · 3 claims (3 for) · 2 studies (1 causal, 1 theoretical), `q2` · 0 of 2 report an effect size · 3 claims rest on one study

## Description
A machine-learning student modeling middleware that records "the learning scene itself, the usage of mouse and keyboard, and the period of time that the learning scene is active" as three evidence nodes and processes them with combined predictive and diagnostic reasoning in a Bayesian network. Conditional probability table values were assigned manually in parallel to simulation results with virtual students. Threshold labels for mouse–keyboard use and playtimes were initialized with four students and then dynamically updated with every student processed, addressing concept drift.

## Design Implications

### Context
#### Requirements
- Conditional probability table values assigned (manually, informed by simulation); threshold values for evidence-node labeling initialized and dynamically updated
#### Constraints
- Only two of the four FSLSM dimensions (visual/verbal, active/reflective) were modeled, because the number of learning scenes grows exponentially with more dimensions

### Target Learners
- undergraduate and graduate EFL students at university preparatory level

### Learning Goals
- diagnosing individual learning styles to adapt EFL grammar content presentation

### Claims

- [Bayesian Diagnosis 41 54 Percent](../claims/bayesian-diagnosis-41-54-percent.md) [+M]
- [Verbal Active Learner Diagnosis Rates](../claims/verbal-active-learner-diagnosis-rates.md) [+M]
- [Dynamic belief networks provide a theoretically-sound way to update the student model](../claims/dynamic-belief-networks-update-student-model.md) [+W]

## Related Designs

- [Browser-shell e-learning software with learning-style-based IF-Clauses content](browser-shell-adaptive-efl-software.md)
- [ACE's Dynamic Bayesian Network student model with gaze-shift and time nodes as independent predictors of implicit self-explanation](ace-dbn-student-model-gaze-time-predictors.md)

## Examples
-

## Key Sources
- Burak Galip Aslan, Özlem Öztürk, Mustafa Murat İnceoğlu. (2014). Effect of Bayesian Student Modeling on Academic Achievement in Foreign Language Teaching (University Level English Preparatory School Example). Educational Sciences: Theory & Practice, 14(3). https://doi.org/10.12738/estp.2014.3.1587

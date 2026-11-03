---
type: strategy
id: dynamic-threshold-updating-concept-drift
title: Dynamically update student model thresholds during learning to counter concept drift
description: "The article suggests a \"dynamic student modeling system that can update itself against concept drift and adapt itself according to the changes in learning styles during the learning process\"."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-03
sources:
  - id: burak-galip-aslan-2014
    resource: "https://doi.org/10.12738/estp.2014.3.1587"
    title: "Burak Galip Aslan, Özlem Öztürk, Mustafa Murat İnceoğlu. (2014). Effect of Bayesian Student Modeling on Academic Achievement in Foreign Language Teaching (University Level English Preparatory School Example). Educational Sciences: Theory & Practice, 14(3). https://doi.org/10.12738/estp.2014.3.1587"
    author: Burak Galip Aslan, Özlem Öztürk, Mustafa Murat İnceoğlu
---

# Dynamically update student model thresholds during learning to counter concept drift

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article suggests a "dynamic student modeling system that can update itself against concept drift and adapt itself according to the changes in learning styles during the learning process". Threshold values for labeling evidence-node data were initialized with a small startup group and then updated with every student processed, so the model tracks changes in learning styles over time rather than relying on static parameters.

## Design Implications

### Context
#### Requirements
- A startup phase to initialize threshold values, and continued logging of mouse, keyboard and scene-time data for ongoing updates
#### Constraints
- 

### Target Learners
- e-learning students whose learning styles or behaviors may change during a course

### Target Learning Goals
- maintaining accurate student models for adaptive content selection

## Claims

- [The Festschrift introduction reports that Rimac versions with student models outperformed versions without or with weaker student models, with dynamic updating helping both high and low prior knowledge students](../claims/rimac-student-model-outperformed-no-model.md) [+W]

## Related Strategies

- [Use dynamic user models to recognize non-optimal learning behaviors and redirect students toward more effective behaviors](dynamic-user-models-redirect-non-optimal-behaviors.md)

## Examples
-

## Key Sources
- Burak Galip Aslan, Özlem Öztürk, Mustafa Murat İnceoğlu. (2014). Effect of Bayesian Student Modeling on Academic Achievement in Foreign Language Teaching (University Level English Preparatory School Example). Educational Sciences: Theory & Practice, 14(3). https://doi.org/10.12738/estp.2014.3.1587

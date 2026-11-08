---
type: design
id: e-gal-system-design
title: "e-GAL: a five-module system design for e-learning platforms supporting gesture-aided learning"
description: e-GAL is a system design for e-learning platforms with gesture-aided learning (GAL) support, built around decoupling learning content from gestures so recorded gestures can be shared and reused.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-08
sources:
  - id: kremser-wolfgang-2021
    resource: "https://doi.org/10.3390/s21238042"
    title: "Kremser Wolfgang, Kranzinger Stefan, Bernhart Severin. (2021). Design and Implementation of a Gesture-Aided E-Learning Platform. Sensors. https://doi.org/10.3390/s21238042"
    author: Kremser Wolfgang, Kranzinger Stefan, Bernhart Severin
---

# e-GAL: a five-module system design for e-learning platforms supporting gesture-aided learning

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
e-GAL is a system design for e-learning platforms with gesture-aided learning (GAL) support, built around decoupling learning content from gestures so recorded gestures can be shared and reused. It comprises five modules: a content catalog, a gesture catalog, a lesson configurator for instructors, a web-based lesson player with an animated humanoid avatar, and a monitoring module that records learner motion data for instructor review. The article states: "This section proposes the e-GAL design, a system design for e-learning platforms with GAL support." A lesson is an ordered list of gesture-enhanced content items (GECs).

## Design Implications

### Context
#### Requirements
- Gesture data must be sufficient to animate a humanoid avatar; ideally recorded with a high-quality motion-capture system
- The monitoring module requires a motion sensor (e.g., accelerometer, video) chosen according to the gesture's range of motion
#### Constraints
- The design is open regarding the type of learning content but was developed specifically for this study
- The article states the study does not say anything about the influence of this mode of learning on learning outcomes

### Target Learners
- Remote e-learning learners, demonstrated with adult participants learning German vocabulary

### Learning Goals
- Vocabulary/word learning via gesture-aided rehearsal; extendable to other learning content types

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Kremser Wolfgang, Kranzinger Stefan, Bernhart Severin. (2021). Design and Implementation of a Gesture-Aided E-Learning Platform. Sensors. https://doi.org/10.3390/s21238042

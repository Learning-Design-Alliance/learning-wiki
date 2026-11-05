---
type: design
id: three-phase-robot-patient-case-design
title: "Three-phase design pattern for building a robot-simulated patient case: theoretical case design, technical implementation, study implementation"
description: "The article describes a reusable three-phase procedure for creating a robot-simulated patient case: \"(1) theoretical design of the patient case, (2) technical implementation, and (3) study implementation\"."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-05
sources:
  - id: schwarz-p-2025
    resource: "https://doi.org/10.2196/70363"
    title: "Schwarz P, Hellmers S, Spanknebel S, Immel D, Hurlemann R, Hein A. (2025). Comparing Patient Simulation With a Humanoid Robot or a Human Actor in Terms of Training Success and Acceptance: Pilot Questionnaire Study. JMIR Formative Research. https://doi.org/10.2196/70363"
    author: Schwarz P, Hellmers S, Spanknebel S, Immel D, Hurlemann R, Hein A
---

# Three-phase design pattern for building a robot-simulated patient case: theoretical case design, technical implementation, study implementation

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article describes a reusable three-phase procedure for creating a robot-simulated patient case: "(1) theoretical design of the patient case, (2) technical implementation, and (3) study implementation". Videos of actor patients are used as a "reproducible and precise basis" for the robot simulation; audio (mood, thoughts, feelings) and movement sequences are transferred through a graphical user interface to the robot management system, producing symptom sequences that can be recombined and evaluated with learners. This pattern enabled direct comparison between robot and video simulations by participants.

## Design Implications

### Context
#### Requirements
- Existing actor-patient video recordings of the target clinical behaviors
- Collaboration with domain experts to select and validate symptoms
- A robot management system with a graphical user interface for transferring audio and movement data
#### Constraints
- Developed and evaluated for one specific humanoid robot (Ameca) and one clinical picture (schizophrenia) in a pilot study

### Target Learners
- medical students
- nursing students

### Learning Goals
- psychopathological assessment and diagnostic skills

### Claims
- [Robot Noninferior 20 Percent Deviation Criterion](../claims/robot-noninferior-20-percent-deviation-criterion.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Schwarz P, Hellmers S, Spanknebel S, Immel D, Hurlemann R, Hein A. (2025). Comparing Patient Simulation With a Humanoid Robot or a Human Actor in Terms of Training Success and Acceptance: Pilot Questionnaire Study. JMIR Formative Research. https://doi.org/10.2196/70363

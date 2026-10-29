---
type: design
id: poed-strategy-framework
title: "POED strategy: extending POEE with a two-tier diagnostic test phase that diagnoses misconceptions and guides knowledge reconstruction"
description: The POED strategy extends the Predict-Observe-Explain-Evaluate (POEE) strategy by replacing the evaluation phase with a two-tier test-based diagnosis phase.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-29
sources:
  - id: kuanfu-chen-2025
    resource: "https://doi.org/10.1007/s11423-025-10527-5"
    title: "Kuan‑Fu Chen, Gwo‑Jen Hwang, Mei‑Rong Alice Chen. (2025). Precision diagnosis in virtual learning contexts: a predict‑observe‑explain‑diagnose‑based approach to scientific inquiry. Education Tech Research Dev. https://doi.org/10.1007/s11423-025-10527-5"
    author: Kuan‑Fu Chen, Gwo‑Jen Hwang, Mei‑Rong Alice Chen
---

# POED strategy: extending POEE with a two-tier diagnostic test phase that diagnoses misconceptions and guides knowledge reconstruction

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q2` · 1 of 1 report an effect size · 2 claims rest on one study

## Description
The POED strategy extends the Predict-Observe-Explain-Evaluate (POEE) strategy by replacing the evaluation phase with a two-tier test-based diagnosis phase. The article states that "a two-tier test-based learning diagnosis strategy was adopted to replace the evaluation in POEE to diagnose learners' misconceptions and guide them to construct correct knowledge and concepts". In the implemented VR system, students progress through prediction, observation, explanation, and evaluation scenes, then take a two-tier test whose first tier verifies factual knowledge and second tier requires conceptual justification; incorrect answers prompt a choice between retrying or reading supplementary learning materials, and progression is contingent on passing both tiers.

## Design Implications

### Context
#### Requirements
- A two-tier test database with teacher-designed diagnostic questions and supplementary learning materials, plus a learning process database recording student behavior
#### Constraints
- The article notes the two-tier test questions were limited to multiple-choice questions only, which it says cannot diagnose some misconceptions

### Target Learners
- eighth-grade junior high school natural science students

### Learning Goals
- conceptual understanding of factors affecting chemical reaction rate
- diagnosis and correction of science misconceptions

### Claims
- [Poed Vr Better Chemistry Achievement Than Poee](../claims/poed-vr-better-chemistry-achievement-than-poee.md) [+M]
- [Poed Diagnostic Feedback Drives Supplementary Material Use](../claims/poed-diagnostic-feedback-drives-supplementary-material-use.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Kuan‑Fu Chen, Gwo‑Jen Hwang, Mei‑Rong Alice Chen. (2025). Precision diagnosis in virtual learning contexts: a predict‑observe‑explain‑diagnose‑based approach to scientific inquiry. Education Tech Research Dev. https://doi.org/10.1007/s11423-025-10527-5

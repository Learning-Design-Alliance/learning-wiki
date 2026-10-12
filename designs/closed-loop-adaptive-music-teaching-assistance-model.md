---
type: design
id: closed-loop-adaptive-music-teaching-assistance-model
title: Closed-loop adaptive teaching assistance model integrating perception, evaluation, generation and feedback for music education
description: "The article proposes an adaptive teaching assistance model for music education organized as a closed-loop path of \"perception evaluation generation feedback\"."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-12
sources:
  - id: zhu-z-2026
    resource: "https://doi.org/10.3389/fpsyg.2026.1844703"
    title: "Zhu Z, Luo C and Li L (2026) Adaptive teaching assistance model combining generative AI and big data analytics. Front. Psychol. 17:1844703. https://doi.org/10.3389/fpsyg.2026.1844703"
    author: Zhu Z, Luo C and Li L
---

# Closed-loop adaptive teaching assistance model integrating perception, evaluation, generation and feedback for music education

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The article proposes an adaptive teaching assistance model for music education organized as a closed-loop path of "perception evaluation generation feedback". Student performance audio and multidimensional behavioral data build a big data repository; a multimodal contrastive learning transformer aligns audio features with symbolic music knowledge via cosine similarity loss; analysis results are mapped into a reward space; and the PPO algorithm fine-tunes generation parameters in real time so that output scores and accompaniments adapt to learner progress. The design forms "a reverse drive from evaluation to generation", establishing "an automated closed loop from monitoring to generation to intervention".

## Design Implications

### Context
#### Requirements
- Performance audio capture and standard digital score input must be available so the CMT can align heterogeneous modalities in a shared high-dimensional space
- The big data analysis module must quantify performance into reward signals and capability defect matrices to constrain the PPO generation policy
#### Constraints
- The article states educational statements should be interpreted within the scope of testing conditions and technical proxy indicators reported
- The system was validated as a technical framework with the educational comparison serving as an auxiliary demonstration

### Target Learners
- undergraduate music majors

### Learning Goals
- instrumental performance skills in pitch, rhythm and dynamic control
- personalized practice content matched to learner skill level

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Zhu Z, Luo C and Li L (2026) Adaptive teaching assistance model combining generative AI and big data analytics. Front. Psychol. 17:1844703. https://doi.org/10.3389/fpsyg.2026.1844703

---
type: design
id: logic-aware-segmented-video-intervention
title: Logic-aware segmented video intervention with fixed 4-second system-defined pauses
description: "A post-hoc video processing intervention for instructional programming videos: after recording, content is cut at logical action boundaries and a fixed pause is injected after each step."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: veronica-pimenova-2026
    resource: "https://arxiv.org/abs/2607.24612"
    title: "Veronica Pimenova, Chris Lee, Baramee Bhakdibhumi, Simon Chu, and Andrew Begel. (2026). Leveling the Playing Field: Temporal Video Segmentation for Individuals with ADHD in Computing Education. https://arxiv.org/abs/2607.24612"
    author: Veronica Pimenova, Chris Lee, Baramee Bhakdibhumi, Simon Chu, and Andrew Begel
---

# Logic-aware segmented video intervention with fixed 4-second system-defined pauses

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
A post-hoc video processing intervention for instructional programming videos: after recording, content is cut at logical action boundaries and a fixed pause is injected after each step. The article explains that "a pause was manually inserted immediately after the completion of a logical action (e.g., snapping a block into place), but before the explanation of the subsequent step." Pausing is system-defined rather than student-initiated, chosen because student-initiated pausing often has negligible learning effects. Pause duration was set to 4 seconds after piloting 2-, 4-, and 6-second intervals with 13 participants.

## Design Implications

### Context
#### Requirements
- Pre-recorded instructional videos whose content can be divided into discrete logical steps, with segment cuts agreed upon by multiple authors
#### Constraints
- The 4-second pause duration is fixed; the article acknowledges a one-size-fits-all pause duration may not be optimal for every learner
- Evaluated with adult novices with no programming experience in the Scratch environment, which the authors note may limit generalizability

### Target Learners
- adult novice programmers
- individuals with ADHD in computing education

### Learning Goals
- following instructional video steps to build a Scratch game
- reducing errors and hesitations during programming tasks

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Veronica Pimenova, Chris Lee, Baramee Bhakdibhumi, Simon Chu, and Andrew Begel. (2026). Leveling the Playing Field: Temporal Video Segmentation for Individuals with ADHD in Computing Education. https://arxiv.org/abs/2607.24612

---
type: design
id: genai-video-tracking-fitting-workflow
title: "Four-phase generative-AI physics workflow: video generation, Tracker tracking, Excel Solver curve fitting, parameter validation"
description: A replicable instructional workflow combining generative-AI video platforms (PixVerse.ai, Grok Imagine, Pippit), the open-source Tracker video analysis tool, and the Microsoft Excel Solver GRG Nonlinear algorithm.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: laura-b-alvarado-cruz-2026
    resource: "https://arxiv.org/abs/2609.19400"
    title: "Laura B. Alvarado-Cruz, Josep Ll. Suñer, Pedro Yuste, Juan C. Castro-Palacio, Juan A. Monsoriu, and Francisco M. Muñoz-Pérez. (2026). From Prompts to Physical Laws: A Generative AI Workflow for Engineering Physics Education. https://arxiv.org/abs/2609.19400"
    author: Laura B. Alvarado-Cruz, Josep Ll. Suñer, Pedro Yuste, Juan C. Castro-Palacio, Juan A. Monsoriu, and Francisco M. Muñoz-Pérez
---

# Four-phase generative-AI physics workflow: video generation, Tracker tracking, Excel Solver curve fitting, parameter validation

> **Design** · [All designs](index.md)
> **Evidence** · 7 claims (7 for) · 2 studies (2 design), `q2` · 0 of 2 report an effect size · 7 claims rest on one study

## Description
A replicable instructional workflow combining generative-AI video platforms (PixVerse.ai, Grok Imagine, Pippit), the open-source Tracker video analysis tool, and the Microsoft Excel Solver GRG Nonlinear algorithm. As the article states, "The proposed workflow is organized into four sequential phases: (i) generation of synthetic videos using generative AI, (ii) extraction of kinematic data throug video analysis with software Tracker, (iii) estimation of model parameters by means of non-linear curve fitting, and (iv) identification and validation of the recovered physical parameters." It functions as a virtual laboratory mirroring experimental practice from model construction to quantitative validation.

## Design Implications

### Context
#### Requirements
- Access to generative-AI video platforms, the Tracker open-source video analysis tool, and the Excel Solver add-in with the GRG Nonlinear algorithm
#### Constraints
- The agreement achieved is approximate rather than exact, since videos are generated from natural-language descriptions rather than explicit physical equations

### Target Learners
- introductory engineering physics students

### Learning Goals
- experimental design
- data acquisition
- parameter estimation
- model evaluation
- modelling of physical systems

### Claims

- [Ai Generated Video Trajectories Fit Resistive Force Models](../claims/ai-generated-video-trajectories-fit-resistive-force-models.md) [+M]
- [Using video analysis data to set model parameters yields a more precise model than trial-and-error model building](../claims/data-driven-modeling-more-precise-than-trial-and-error.md) [+W]
- [The authors observe that more specific physical descriptions in generation prompts tend to produce more physically coherent AI-generated motion](../claims/prompt-specificity-shapes-physical-coherence.md) [+W]
- [Students can derive an accurate gravitational acceleration value from Tracker's parabola fit of a falling-ball video](../claims/tracker-parabola-fit-derives-gravitational-acceleration.md) [+W]
- [The linear-drag AI video yields a fitted glycerin viscosity (≈ 0.234 Pa·s) consistent with an aqueous glycerin solution of about 85% by weight](../claims/ai-video-linear-drag-recovers-plausible-viscosity.md) [+W]
- [The quadratic-drag AI video yields a fitted drag coefficient (CD ≈ 3.18) within the literature range reported for skydivers](../claims/ai-video-quadratic-drag-recovers-plausible-drag-coefficient.md) [+W]
- [The constant-friction AI video yields a fitted friction coefficient (µ ≈ 0.169) consistent with literature values for wood on smooth or waxed surfaces](../claims/ai-video-constant-friction-recovers-plausible-mu.md) [+W]

## Related Designs
- 

## Examples
-

## Key Sources
- Laura B. Alvarado-Cruz, Josep Ll. Suñer, Pedro Yuste, Juan C. Castro-Palacio, Juan A. Monsoriu, and Francisco M. Muñoz-Pérez. (2026). From Prompts to Physical Laws: A Generative AI Workflow for Engineering Physics Education. https://arxiv.org/abs/2609.19400

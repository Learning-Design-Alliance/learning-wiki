---
type: strategy
id: webgl-browser-deployment-strategy
title: Deploy gamified onboarding simulations via WebGL in a standard web browser rather than VR or installed software
description: "The authors deliberately avoided VR deployment so that \"any future employee [can] use it with a simple web browser.\" WebGL deployment runs directly in the browser, independent of hardware and operating system, with ce..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
sources:
  - id: gobron-stephane-2025
    resource: "https://doi.org/10.2196/72202"
    title: "Gobron Stephane, Lestrade Antoine, Sadiku Artan, Bentvelzen Alexandre, Ait Kaci Leila, Carrier Jean-Michel, Guyot Emmanuelle, Carron Pierre-Nicolas. (2025). Gamified Simulation for Onboarding Health Care Teams in Emergency Care: Development and Preliminary Feasibility Study. JMIR Formative Research. https://doi.org/10.2196/72202"
    author: Gobron Stephane, Lestrade Antoine, Sadiku Artan, Bentvelzen Alexandre, Ait Kaci Leila, Carrier Jean-Michel, Guyot Emmanuelle, Carron Pierre-Nicolas
---

# Deploy gamified onboarding simulations via WebGL in a standard web browser rather than VR or installed software

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The authors deliberately avoided VR deployment so that "any future employee [can] use it with a simple web browser." WebGL deployment runs directly in the browser, independent of hardware and operating system, with centralized updates eliminating manual installations. They applied mesh simplification, texture compression, static batching, and light baking to reach acceptable size, speed, and visual quality.

## Design Implications

### Context
#### Requirements
- Optimization procedures to reduce application size and maintain frame rate for online use
#### Constraints
- The app was not tested on low hardware configurations; hardware limits remain unstudied

### Target Learners
- Newly arriving hospital staff using PCs, tablets, or smartphones

### Target Learning Goals
- Accessible self-paced onboarding from any location

## Claims

- [Most ED staff testers found the 3D gamified simulation helpful for understanding department topology and useful for new employees](../claims/ed-staff-rate-3d-onboarding-simulation-helpful.md) [+W]
- [Personal anecdotes and gamified tasks were viewed as engaging and motivating by testers](../claims/anecdotes-gamified-tasks-engaging.md) [+W]
- [Permanent staff rated the quest management application positively, with 91% praising autonomous content modification without technical staff](../claims/quest-editor-autonomous-content-update-accepted.md) [+W]

## Related Strategies

- [Platform Agnostic Design](platform_agnostic_design.md)
- [Deploy Amira as a browser-based program integrated with district systems through Single Sign-On and automated rostering](amira-browser-deployment-sso-rostering.md)

## Examples
-

## Key Sources
- Gobron Stephane, Lestrade Antoine, Sadiku Artan, Bentvelzen Alexandre, Ait Kaci Leila, Carrier Jean-Michel, Guyot Emmanuelle, Carron Pierre-Nicolas. (2025). Gamified Simulation for Onboarding Health Care Teams in Emergency Care: Development and Preliminary Feasibility Study. JMIR Formative Research. https://doi.org/10.2196/72202

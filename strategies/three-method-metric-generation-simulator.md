---
type: strategy
id: three-method-metric-generation-simulator
title: Three-method metric generation for simulator-based skill assessment
description: "The framework's metric-generation step uses three methods: consulting domain experts to create metrics representative of current expertise measures, reusing metrics from previous simulation studies, and developing nov..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-08
sources:
  - id: mirchi-n-2020
    resource: "https://doi.org/10.1371/journal.pone.0229596"
    title: "Mirchi N, Bissonnette V, Yilmaz R, Ledwos N, Winkler-Schwartz A, Del Maestro RF. (2020). The Virtual Operative Assistant: An explainable artificial intelligence tool for simulation-based training in surgery and medicine. PLoS ONE. https://doi.org/10.1371/journal.pone.0229596"
    author: Mirchi N, Bissonnette V, Yilmaz R, Ledwos N, Winkler-Schwartz A, Del Maestro RF
---

# Three-method metric generation for simulator-based skill assessment

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (4 for) · 2 studies (1 review, 1 design), `q2` · 0 of 2 report an effect size · 4 claims rest on one study

## Description
The framework's metric-generation step uses three methods: consulting domain experts to create metrics representative of current expertise measures, reusing metrics from previous simulation studies, and developing novel metrics. The article highlights force application as a construct "difficult to assess by surgeon instructors" that computer platforms can quantify positionally and qualitatively, and recommends that "Efforts should be made to generate as many different metrics as possible, to try and capture the multiple facets of a given technical skill".

## Design Implications

### Context
#### Requirements
- Access to simulator-recorded raw data (tool position, rotation, forces, volumes removed) and expert or literature input for metric design
#### Constraints
- 

### Target Learners
- Trainees on medical and surgical simulators

### Target Learning Goals
- Quantifying multiple facets of technical and psychomotor expertise, including force application

### Affordances
- [Transparency Framework Explainable Ai Simulation Training](../designs/transparency-framework-explainable-ai-simulation-training.md)

## Claims

- [Four of 270 simulator-derived performance metrics, all with negative weights, were selected by an iterative loop algorithm to drive the classification model](../claims/four-metrics-selected-from-270-negative-weights.md) [+W]
- [A linear support vector machine using 4 performance metrics classified skilled versus novice participants in a virtual reality brain tumor resection task with 92% accuracy, 100% sensitivity and 82% specificity](../claims/svm-classifies-skilled-novice-vr-neurosurgery-92-accuracy.md) [+W]
- [Kinematic-based metrics such as reduced path length and lower instrument vibration correlate with higher rubric scores and distinguish experts from novices](../claims/kinematic-metrics-correlate-rubric-performance.md) [+W]
- [Metric weights reveal each metric's relative importance and expose compensation between metrics, allowing trainees to see how strong performance on one metric offsets weakness in another](../claims/metric-weights-reveal-importance-and-compensation.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Mirchi N, Bissonnette V, Yilmaz R, Ledwos N, Winkler-Schwartz A, Del Maestro RF. (2020). The Virtual Operative Assistant: An explainable artificial intelligence tool for simulation-based training in surgery and medicine. PLoS ONE. https://doi.org/10.1371/journal.pone.0229596

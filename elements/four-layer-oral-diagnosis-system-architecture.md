---
type: element
id: four-layer-oral-diagnosis-system-architecture
title: Four-layer system architecture for intelligent oral diagnosis and adaptive training
description: "The proposed system is organized as a hierarchical four-layer architecture: Data Acquisition, Feature Extraction, Intelligent Diagnosis, and Adaptive Training."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-25
sources:
  - id: chai-rui-2026
    resource: "https://doi.org/10.1038/s41598-026-51608-6"
    title: "Chai Rui. (2026). Deep learning-based intelligent diagnosis and adaptive training system for university english oral proficiency. Scientific Reports. https://doi.org/10.1038/s41598-026-51608-6"
    author: Chai Rui
---

# Four-layer system architecture for intelligent oral diagnosis and adaptive training

> **Element** · [All elements](index.md)

## Description
The proposed system is organized as a hierarchical four-layer architecture: Data Acquisition, Feature Extraction, Intelligent Diagnosis, and Adaptive Training. "the Data Acquisition Layer acts as the system’s sensory interface: it handles audio capture, runs noise-reduction preprocessing, and applies voice activity detection to break continuous recordings into analysable speech segments." Layers communicate through standardized interfaces, with time-critical recognition and feedback running synchronously and computationally intensive diagnostic analysis and learner-model updates running asynchronously.

## Design Implications

### Context
#### Requirements
- Standardized interfaces between layers so heterogeneous feature vectors converge at the diagnosis layer before dimension-specific scoring
#### Constraints
- The design was chosen for modularity, maintainability, and differing compute demands of components, per the authors' practical rationale

### Target Learners
- University students practicing spoken English

### Target Learning Goals
- Oral proficiency diagnosis and personalized practice recommendation

## Related Elements
- 

## Examples
-

## Key Sources
- Chai Rui. (2026). Deep learning-based intelligent diagnosis and adaptive training system for university english oral proficiency. Scientific Reports. https://doi.org/10.1038/s41598-026-51608-6

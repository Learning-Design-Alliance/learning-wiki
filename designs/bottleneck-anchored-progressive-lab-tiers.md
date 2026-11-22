---
type: design
id: bottleneck-anchored-progressive-lab-tiers
title: Four progressive tiers plus an engineering layer, each anchored to an open technical bottleneck, with deliberate vertical dependency
description: "The curriculum spine is a sequence of four tiers (representation learning, fusion and reasoning, knowledge evolution, robustness) plus a Tier V engineering layer, each mapped to a bottleneck with \"candidate solutions..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: dongjing-shan-2026
    title: "Dongjing Shan, Yamei Luo, Jin Li, Yong Luo. (2026). From Research Frontier to Laboratory Bench: Design of a Four-Tier Experimental Teaching System for Multimodal Medical Image Intelligent Diagnosis."
    author: Dongjing Shan, Yamei Luo, Jin Li, Yong Luo
---

# Four progressive tiers plus an engineering layer, each anchored to an open technical bottleneck, with deliberate vertical dependency

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The curriculum spine is a sequence of four tiers (representation learning, fusion and reasoning, knowledge evolution, robustness) plus a Tier V engineering layer, each mapped to a bottleneck with "candidate solutions but no consensus". The dependency is cumulative: "the graph representation built in Tier I is the object that Tier II fuses, that Tier III must preserve across tasks, and that Tier IV must keep stable under shift". Anchoring tiers to open bottlenecks makes genuinely open-ended laboratory work possible.

## Design Implications

### Context
#### Requirements
- Prerequisite coursework distributed across second and third undergraduate years; tiers cannot form a single course
- A joint representation must be constructed in Tier I and fused in Tier II before modality laziness is encountered in Tier III
#### Constraints
- Because prerequisites are distributed across the second and third undergraduate years, the tiers are delivered as laboratory strands embedded in named courses, with Tier V offered as a capstone

### Target Learners
- undergraduate intelligent medical engineering students

### Learning Goals
- multimodal fusion and reasoning
- catastrophic forgetting mitigation
- out-of-distribution detection and abstention

### Claims
- [Three Structural Gaps Medical Ai Lab Teaching](../claims/three-structural-gaps-medical-ai-lab-teaching.md) [+M]

## Related Designs

- [The Quantum Learning Pyramid: a four-tier framework for quantum computing education](quantum-learning-pyramid-framework.md)

## Examples
-

## Key Sources
- Dongjing Shan, Yamei Luo, Jin Li, Yong Luo. (2026). From Research Frontier to Laboratory Bench: Design of a Four-Tier Experimental Teaching System for Multimodal Medical Image Intelligent Diagnosis.

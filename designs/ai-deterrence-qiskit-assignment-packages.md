---
type: design
id: ai-deterrence-qiskit-assignment-packages
title: Three AI-deterrence-modified autogradable Qiskit assignment packages (HW1–HW3) with layered personalization and grading
description: "Three complete take-home homework packages for an undergraduate quantum software course: HW1 (seeded basis-state circuits with bit flips and customized measurement mappings), HW2 (QFT followed by inverse-transform rec..."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: alexei-kaltchenko-and-gurnivaj-tiwana-2026
    resource: "https://arxiv.org/abs/2608.19707"
    title: "Alexei Kaltchenko and Gurnivaj Tiwana. (2026). ChatGPT Solves All Tested Qiskit Homework Assignments. arXiv. https://arxiv.org/abs/2608.19707"
    author: Alexei Kaltchenko and Gurnivaj Tiwana
---

# Three AI-deterrence-modified autogradable Qiskit assignment packages (HW1–HW3) with layered personalization and grading

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (1 for, 1 against) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
Three complete take-home homework packages for an undergraduate quantum software course: HW1 (seeded basis-state circuits with bit flips and customized measurement mappings), HW2 (QFT followed by inverse-transform recovery with circuit metrics and an optional hardware extension), and HW3 (seeded Deutsch–Jozsa with customized oracle masks). Each used a deterministic student identifier so an instructor-side reference could regenerate the configuration, and layers included exact JSON submissions, hidden deterministic references, circuit metrics, reflections, and optional IBM Quantum execution.

## Design Implications

### Context
#### Requirements
- An instructor-side reference that regenerates each student's seeded configuration and expected output so personalization works without a separate answer key per student
#### Constraints
- In the tested designs, these deterrence layers did not prevent direct ChatGPT completion

### Target Learners
- undergraduate quantum software development students

### Learning Goals
- count-key ordering in Qiskit
- QFT and inverse-QFT recovery
- Deutsch–Jozsa oracle construction and classification

### Claims
- [Chatgpt Completes All 150 Qiskit Homework Sessions](../claims/chatgpt-completes-all-150-qiskit-homework-sessions.md) [-M]
- [Why Qiskit Deterrence Layers Failed](../claims/why-qiskit-deterrence-layers-failed.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Alexei Kaltchenko and Gurnivaj Tiwana. (2026). ChatGPT Solves All Tested Qiskit Homework Assignments. arXiv. https://arxiv.org/abs/2608.19707

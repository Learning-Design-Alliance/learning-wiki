---
type: design
id: four-module-ai-imaging-teaching-platform
title: Four-module AI teaching platform for medical imaging
description: "A closed-loop AI teaching system comprising four modules: (1) cognitive diagnosis using BKT (pyBKT) and DKT (custom LSTM in TensorFlow) for real-time mastery updates and misjudgment modeling; (2) case generation & sel..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-05
sources:
  - id: an-jie-2026
    resource: "https://doi.org/10.1186/s12909-026-09002-3"
    title: "An Jie, Leng Xi, Liu Yujie, Zhou Jie, Liang Yi, Chen Yuna, Qiu Shijun (2026). Rebuilding ability acquisition in medical imaging teaching: a multi-level AI-driven teaching paradigm based on cognitive-information theory. BMC Medical Education. https://doi.org/10.1186/s12909-026-09002-3"
    author: An Jie, Leng Xi, Liu Yujie, Zhou Jie, Liang Yi, Chen Yuna, Qiu Shijun
---

# Four-module AI teaching platform for medical imaging

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
A closed-loop AI teaching system comprising four modules: (1) cognitive diagnosis using BKT (pyBKT) and DKT (custom LSTM in TensorFlow) for real-time mastery updates and misjudgment modeling; (2) case generation & selection from public image datasets with synthetic perturbations creating difficulty gradients and confusion pairs; (3) explainable guidance using Grad-CAM saliency maps and LLM-generated three-level cues; (4) adaptive scheduling via custom-coded PPO in PyTorch with a 15-feature state space and custom reward function.

## Design Implications

### Context
#### Requirements
- Public image datasets with expert annotations for case generation
- Pilot data for calibrating BKT parameters (forgetting rate and guessing probability)
- Historical interaction sequences for DKT training (20 pilot learners)
#### Constraints
- DKT trained on historical interaction sequences from only 20 pilot learners

### Target Learners
- Postgraduate medical imaging students

### Learning Goals
- Fine-grained knowledge point mastery
- Diagnostic accuracy
- Reduction of systematic misjudgment errors

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- An Jie, Leng Xi, Liu Yujie, Zhou Jie, Liang Yi, Chen Yuna, Qiu Shijun (2026). Rebuilding ability acquisition in medical imaging teaching: a multi-level AI-driven teaching paradigm based on cognitive-information theory. BMC Medical Education. https://doi.org/10.1186/s12909-026-09002-3

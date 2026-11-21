---
type: strategy
id: safety-interlocks-ai-alerts-virtual-hv-training
title: Use C++ safety interlocks with AI-assistant alerts to enforce HV safety protocols in virtual labs
description: "VLab-HV enforces safety procedurally: \"Safety interlocks, implemented in C++, prevent unsafe operations, such as applying voltage with open test chamber doors or handling electrodes with residual charge, aligning with..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: pliuhin-2024
    resource: "https://arxiv.org/abs/2511.20919"
    title: "Pliuhin, V., Tsegelnyk, Y., Sukhonos, M., Biletskyi, I., Plankovskyy, S., and Sakhoshko, T. (2024). Virtual High Voltage Lab: Gamified Learning in a Safe 3D Environment. O.M. Beketov National University of Urban Economy in Kharkiv. https://arxiv.org/abs/2511.20919"
    author: Pliuhin, V., Tsegelnyk, Y., Sukhonos, M., Biletskyi, I., Plankovskyy, S., and Sakhoshko, T
---

# Use C++ safety interlocks with AI-assistant alerts to enforce HV safety protocols in virtual labs

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 review), `q3` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
VLab-HV enforces safety procedurally: "Safety interlocks, implemented in C++, prevent unsafe operations, such as applying voltage with open test chamber doors or handling electrodes with residual charge, aligning with international standards (IEC 60060-1, 2010)." When a learner attempts an unsafe action, the AI assistant issues a warning displayed as a red alert on the virtual monitor, reinforcing safety awareness. This makes safety compliance an active, practiced part of the training rather than a written rule.

## Design Implications

### Context
#### Requirements
- Safety rules must be encoded as interlocks in the simulation logic and paired with an assistant or feedback channel that alerts the learner
#### Constraints
- The article ties the interlocks to IEC 60060-1 (2010); no measured safety-training outcome is printed in the supplied text

### Target Learners
- undergraduate HV students
- electricians and utility professionals in training

### Target Learning Goals
- HV safety protocol adherence, safe laboratory operation, emergency response to transformer faults

## Claims

- [Virtual lab simulations improved blood typing knowledge and motivation but faced technical and language barriers](../claims/virtual-labs-improve-blood-typing-knowledge-motivation.md) [+W]

## Related Strategies

- [Iteratively refine virtual laboratory teaching using student feedback: add group discussions, advance reading materials, and clearer in-experiment guidance](feedback-driven-vlab-refinement-strategy.md)

## Examples
-

## Key Sources
- Pliuhin, V., Tsegelnyk, Y., Sukhonos, M., Biletskyi, I., Plankovskyy, S., and Sakhoshko, T. (2024). Virtual High Voltage Lab: Gamified Learning in a Safe 3D Environment. O.M. Beketov National University of Urban Economy in Kharkiv. https://arxiv.org/abs/2511.20919

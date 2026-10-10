---
type: design
id: contingency-dimension-load-versus-demand
title: "The contingency dimension: separating the load a system carries from the demand it places on the learner"
description: "The paper defines a design axis on which tutor designs sit: \"We call the line those positions lie on thecontingency dimension, and contingent tutoring is movement along it during a task.\" Structuring changes how much..."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: hou-2026
    resource: "https://arxiv.org/abs/2609.22993"
    title: "Hou, X., Weng, Y., Yeh, C. H., Lee, D. L., Zheng, L., Li, F., Wang, W., & Liu, Y. (2026). Adaptive Scaffolding Needs Contingency: An AI Tutor That Escalates and Fades on What the Learner Does. arXiv preprint. https://arxiv.org/abs/2609.22993"
    author: "Hou, X., Weng, Y., Yeh, C. H., Lee, D. L., Zheng, L., Li, F., Wang, W., & Liu, Y"
---

# The contingency dimension: separating the load a system carries from the demand it places on the learner

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q3` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The paper defines a design axis on which tutor designs sit: "We call the line those positions lie on thecontingency dimension, and contingent tutoring is movement along it during a task." Structuring changes how much load the system carries; problematizing changes how much demand the learner faces. Existing LLM tutors fix one position at design time; contingent tutoring moves along the dimension during a task, escalating after failure and fading after success. The theory has three parts: direction (the contingent shift rule), unit (decision points), and warrant (what justifies fading).

## Design Implications

### Context
#### Requirements
- A signal the tutor can read from the learner's writing to decide when support rises and falls
#### Constraints
- Positions of prior systems on the dimension are illustrative; the warrant part was tested only on a text-channel tutor with authored decision points

### Target Learners
- adult novice programmers using AI tutors

### Learning Goals
- regulatory work such as deciding, articulating and judging before help arrives

### Claims
- [Aim Warrant For Fading Ai Tutor](../claims/aim-warrant-for-fading-ai-tutor.md) [+M]
- [Contingent Tutor Delegation Held Delivery Rose](../claims/contingent-tutor-delegation-held-delivery-rose.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Hou, X., Weng, Y., Yeh, C. H., Lee, D. L., Zheng, L., Li, F., Wang, W., & Liu, Y. (2026). Adaptive Scaffolding Needs Contingency: An AI Tutor That Escalates and Fades on What the Learner Does. arXiv preprint. https://arxiv.org/abs/2609.22993

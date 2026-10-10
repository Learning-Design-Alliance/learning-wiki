---
type: design
id: comet-contingent-ai-tutor-environment
title: "CoMeT: a browser-based contingent AI programming tutor with a support ladder over authored decision points"
description: "CoMeT is \"a browser-based environment in which a learner works through a short programming task beside a chat tutor\", with a sketchpad and code editor."
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

# CoMeT: a browser-based contingent AI programming tutor with a support ladder over authored decision points

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q3` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
CoMeT is "a browser-based environment in which a learner works through a short programming task beside a chat tutor", with a sketchpad and code editor. Tasks run three gated phases (Planning with the editor locked, Monitoring, Evaluating), and correctness is decided by authored test cases, never by the model. Tutor C escalates one rung at a time through three asks (Socratic question, specific hint, contrasting case), concedes a point after R = 3 rounds, and returns to the first rung on take-up; coverage is decided by authored patterns rather than holistic model judgement.

## Design Implications

### Context
#### Requirements
- Decision points must be authored per task and phase, with coverage patterns and scaffold wording, so the difference between tutors is auditable
#### Constraints
- All three tutors ran on the same model backbone (Claude Haiku 4.5); take-up where patterns do not settle it falls to a one-word model judgement and a length threshold that errs on the learner's side

### Target Learners
- adult learners with no prior programming threshold through over five years of Python experience

### Learning Goals
- settling the decisions a program turns on before code is written
- monitoring and evaluating one's own solution

### Claims
- Preserved Metacognitive Demand Principle [+M]
- [Contingent Scaffolding Surrenders Full Answer Least](../claims/contingent-scaffolding-surrenders-full-answer-least.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Hou, X., Weng, Y., Yeh, C. H., Lee, D. L., Zheng, L., Li, F., Wang, W., & Liu, Y. (2026). Adaptive Scaffolding Needs Contingency: An AI Tutor That Escalates and Fades on What the Learner Does. arXiv preprint. https://arxiv.org/abs/2609.22993

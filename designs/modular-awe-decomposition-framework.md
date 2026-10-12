---
type: design
id: modular-awe-decomposition-framework
title: Modular decomposition of AWE into scoring, surface-level feedback, and deep-level feedback
description: "The article organizes automated writing evaluation as a modular architecture that divides AWE tasks into three modules: scoring, surface-level feedback, and deep-level feedback."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-12
sources:
  - id: adnan-labib-2026
    resource: "https://arxiv.org/abs/2607.14524"
    title: "Adnan Labib, Yixuan Huang, Jiahui Wu, John Maurice Gayed, Zheng Yuan, Qiao Wang. (2026). WrAFT: a Modularized Automated Writing Evaluation System for Argumentative Essays. arXiv preprint. https://arxiv.org/abs/2607.14524"
    author: Adnan Labib, Yixuan Huang, Jiahui Wu, John Maurice Gayed, Zheng Yuan, Qiao Wang
---

# Modular decomposition of AWE into scoring, surface-level feedback, and deep-level feedback

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article organizes automated writing evaluation as a modular architecture that divides AWE tasks into three modules: scoring, surface-level feedback, and deep-level feedback. The abstract states that "WrAFT adopts a modular design by dividing the automated writing evaluation (AWE) tasks into scoring, surface-level feedback and deep-level feedback." Deep-level feedback is further split into macro feedback (paragraphing, text length, structure) and micro feedback (context-dependent grammar, clarity, coherence, argumentation, formality), each handled by a separate pipeline. The authors report this decomposition builds on Li and Ng (2024)'s layered proposal for AWE systems and supports specialized models per aspect.

## Design Implications

### Context
#### Requirements
- Separate LLMs or pipelines tailored to each module, with validation schemes appropriate to each (benchmark scores for scoring, human raters for feedback)
#### Constraints
- The article notes specialized models handling different aspects can produce better assessments than unified approaches, but the system was developed and tested only on argumentative essays with writing prompts

### Target Learners
- students writing argumentative essays
- second language writers

### Learning Goals
- essay scoring accuracy
- surface-level error correction
- higher-order writing qualities including organization, coherence and argumentation

### Claims
- [Sft Less Effective Than Prompting For Feedback Generation](../claims/sft-less-effective-than-prompting-for-feedback-generation.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Adnan Labib, Yixuan Huang, Jiahui Wu, John Maurice Gayed, Zheng Yuan, Qiao Wang. (2026). WrAFT: a Modularized Automated Writing Evaluation System for Argumentative Essays. arXiv preprint. https://arxiv.org/abs/2607.14524

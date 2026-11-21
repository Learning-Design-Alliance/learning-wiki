---
type: strategy
id: cogapp-three-move-selection-principles
title: "Select LLM mentor moves using three CogApp principles: global before local skills, increasing complexity, and increasing diversity"
description: "Tutorly's prompt engineering selects an appropriate mentor move by following three principles from the CogApp framework."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: wengxi-li-2024
    resource: "https://arxiv.org/abs/2405.12946"
    title: "Wengxi Li, Roy Pea, Nick Haber, and Hari Subramonyam. (2024). Tutorly: Turning Programming Videos Into Apprenticeship Learning Environments with LLMs. https://arxiv.org/abs/2405.12946"
    author: Wengxi Li, Roy Pea, Nick Haber, and Hari Subramonyam
---

# Select LLM mentor moves using three CogApp principles: global before local skills, increasing complexity, and increasing diversity

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (4 for) · 2 studies (1 qualitative, 1 design), `q2` · 0 of 2 report an effect size · 4 claims rest on one study

## Description
Tutorly's prompt engineering selects an appropriate mentor move by following three principles from the CogApp framework. "Global before local skills" has learners build a conceptual map first, so Modeling or Coaching opens each segment. "Increasing complexity" gradually raises task difficulty via prompt engineering and student modeling. "Increasing diversity" varies teaching methods across segments sharing the same learning goal to maintain interest and cater to different learning styles.

## Design Implications

### Context
#### Requirements
- A student model must be available so complexity and prior method use can inform move selection
#### Constraints
- Rigidly mapping specific teaching methods to particular knowledge can constrain adaptability to unforeseen content, and monotony may lead to disengagement

### Target Learners
- novice programmers working through video-based learning goals

### Target Learning Goals
- progressive mastery of programming skills
- sustained engagement across repeated practice

## Claims

- [Expert evaluators assessed Tutorly's prompt-pipeline controllability by annotating 277 dialogue messages against a hierarchical intent label scheme across three video topics](../claims/tutorly-controllability-277-messages.md) [+W]
- [Tutorly's video segmentation by learning goal achieved 73.7% overall accuracy within a five-second margin, with accuracy decreasing for longer videos](../claims/tutorly-segmentation-accuracy-73-7.md) [+W]
- [In a within-subject study, Tutorly improved post-test performance from 61.9% to 76.6% for learners studying exploratory data analysis from a streamcast](../claims/tutorly-within-subject-post-test-gain.md) [+W]
- [The emergent LLM coding pipeline reaches substantial agreement with expert human coding (Cohen's κ = 0.78, raw agreement 84%) on a stratified 10% sample](../claims/llm-discourse-coding-kappa-078-expert-agreement.md) [+W]

## Related Strategies

- [Provide diverse, representative examples in prompts to unlock latent LLM performance on discourse classification](example-driven-prompting-unlock-llm-performance.md)

## Examples
-

## Key Sources
- Wengxi Li, Roy Pea, Nick Haber, and Hari Subramonyam. (2024). Tutorly: Turning Programming Videos Into Apprenticeship Learning Environments with LLMs. https://arxiv.org/abs/2405.12946

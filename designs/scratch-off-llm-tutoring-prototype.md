---
type: design
id: scratch-off-llm-tutoring-prototype
title: Interactive LLM tutoring prototype with scratch-off scaffolding reveal
description: An LLM-based tutoring prototype built as a design probe for studying interactive scaffolding.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: zixin-chen-2026
    resource: "https://doi.org/10.1145/3772363.3798931"
    title: "Zixin Chen, Haotian Li, Zhe Liu, Huamin Qu, and Xing Xie. 2026. From Passive Consumption to Active Interaction: Exploring Interactive LLM Scaffolding to Support Learning Engagement. In Extended Abstracts of the 2026 CHI Conference on Human Factors in Computing Systems (CHI EA '26). https://doi.org/10.1145/3772363.3798931"
    author: Zixin Chen, Haotian Li, Zhe Liu, Huamin Qu, and Xing Xie
---

# Interactive LLM tutoring prototype with scratch-off scaffolding reveal

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
An LLM-based tutoring prototype built as a design probe for studying interactive scaffolding. It has a Learning Material Zone for viewing the target proof and selecting the scaffolding condition, and a Chatbot Tutor Zone for question-driven interaction. "Under the interactive condition, scaffolded content within the responses (e.g., definitions or explanatory guidance) is initially masked and must be actively revealed through a mouse-based scratch-off interaction," while the non-interactive condition presents the same content as plain text. It uses the GPT-5.2 model with prompts encouraging hints, explanations, and step-by-step guidance, and switches to a quiz interface after the learning phase.

## Design Implications

### Context
#### Requirements
- The LLM must explicitly mark scaffolded content segments in its responses, which a client-side script detects to enable scratch-off interaction
#### Constraints
- Evaluated only in a controlled laboratory setting with eight computer science PhD students on two number theory proofs

### Target Learners
- college-level learners with undergraduate mathematics backgrounds

### Learning Goals
- comprehension of mathematical proofs
- engagement with scaffolded explanations

### Claims
- [Interactive Llm Scaffolding Quiz Score Trend](../claims/interactive-llm-scaffolding-quiz-score-trend.md) [+W]
- [Interactive Scaffolding No Workload Increase](../claims/interactive-scaffolding-no-workload-increase.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Zixin Chen, Haotian Li, Zhe Liu, Huamin Qu, and Xing Xie. 2026. From Passive Consumption to Active Interaction: Exploring Interactive LLM Scaffolding to Support Learning Engagement. In Extended Abstracts of the 2026 CHI Conference on Human Factors in Computing Systems (CHI EA '26). https://doi.org/10.1145/3772363.3798931

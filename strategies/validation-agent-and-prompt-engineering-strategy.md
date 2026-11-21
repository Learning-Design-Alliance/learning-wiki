---
type: strategy
id: validation-agent-and-prompt-engineering-strategy
title: Extend the validation-agent approach and refine prompt engineering and multi-agent design to further improve automatic feedback quality
description: The article recommends continuing to develop the multi-agent design pattern in which a second agent detects and revises problematic feedback.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: guo-2024
    resource: "https://arxiv.org/abs/2411.07407"
    title: "Guo, S., Latif, E., Zhou, Y., Huang, X., & Zhai, X. (2024). Using Generative AI and Multi-Agents to Provide Automatic Feedback. https://arxiv.org/abs/2411.07407"
    author: "Guo, S., Latif, E., Zhou, Y., Huang, X., & Zhai, X"
---

# Extend the validation-agent approach and refine prompt engineering and multi-agent design to further improve automatic feedback quality

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (2 for, 1 mixed) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The article recommends continuing to develop the multi-agent design pattern in which a second agent detects and revises problematic feedback. It notes that "as Agent 2 serves the function of detecting and revising feedback, similar strategies could be employed to address other common issues found in automatic feedback", and that future research should explore advanced prompt engineering and multi-agent design, expand the range of assessment items, and investigate real-world impact on student learning in authentic settings.

## Design Implications

### Context
#### Requirements
- A generation agent producing feedback plus a validation agent prompted with the possible problems to detect, using the WRVRT iterative prompt-development approach with expert review and pilot responses until saturation
#### Constraints
- The study provided ChatGPT with responses to only one item, so with limited information it is hard to generate truly personalized learning strategies

### Target Learners
- middle school science students

### Target Learning Goals
- improving the accuracy and quality of automated formative feedback on constructed science responses

## Claims

- [The AutoFeedback multi-agent system significantly outperforms a single GenAI agent by reducing over-praise and over-inference in generated feedback](../claims/autofeedback-multi-agent-reduces-over-praise-over-inference.md) [+M]
- [Even with the multi-agent system, some feedback still contains over-praise and over-inference, and Agent 2's detection and revision are not fully accurate](../claims/residual-feedback-issues-multi-agent.md) [~W]
- [A single GenAI agent generating feedback on science constructed responses produces over-praise in 15.42% of feedback and over-inference in 27.20%, with 9.58% exhibiting both](../claims/single-agent-genai-feedback-over-praise-over-inference-rates.md) [+M]

## Related Strategies

- [Match the refinement coordination strategy to the quality criterion: decentralized refinement for localized criteria, centralized planning for holistic ones](match-refinement-strategy-to-quality-criterion.md)
- [Incorporate pre-delivery LLM-based evaluation approaches into GenAI-powered personalised SRL scaffolding systems to mitigate hallucinations](pre-delivery-llm-evaluation-mitigate-hallucinations.md)

## Examples
-

## Key Sources
- Guo, S., Latif, E., Zhou, Y., Huang, X., & Zhai, X. (2024). Using Generative AI and Multi-Agents to Provide Automatic Feedback. https://arxiv.org/abs/2411.07407. [doi:10.48550/arxiv.2411.07407](https://doi.org/10.48550/arxiv.2411.07407)

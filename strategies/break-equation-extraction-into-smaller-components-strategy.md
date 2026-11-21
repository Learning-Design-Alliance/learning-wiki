---
type: strategy
id: break-equation-extraction-into-smaller-components-strategy
title: Break the equation-extraction task into smaller components, processing one line of the student response per model call
description: Facing the accuracy shortfall of LLM equation extraction, the authors recommend decomposing the task before parsing.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: lachlan-mcginness-and-peter-baumgartner-2025
    resource: "https://arxiv.org/abs/2505.10966"
    title: "Lachlan McGinness and Peter Baumgartner. (2025). Can Large Language Models Correctly Interpret Equations with Errors? https://arxiv.org/abs/2505.10966"
    author: Lachlan McGinness and Peter Baumgartner
---

# Break the equation-extraction task into smaller components, processing one line of the student response per model call

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (4 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
Facing the accuracy shortfall of LLM equation extraction, the authors recommend decomposing the task before parsing. They note that "One strategy which has been shown to work is to break the task into smaller components", which they propose implementing "by including only one line of the student response per model call instead of the entire response". This is offered as future work to raise accuracy toward the 96.5% threshold required for reliable marking.

## Design Implications

### Context
#### Requirements
- Requires additional model calls per response, which increases computational cost and runtime
#### Constraints
- 

### Target Learners
- 16-18 year-old physics exam participants

### Target Learning Goals
- improving accuracy of automated extraction of student equations for grading

## Claims

- [LLM accuracy on physics equation extraction increases with model size but plateaus at approximately 85% around 70B parameters for thinking models](../claims/llm-accuracy-plateaus-70b-physics-equation-extraction.md) [+W]
- [Frontier open-source LLMs translated complex typed student physics responses at about 88% accuracy, 8.5% below the 96.5% human-grader agreement threshold](../claims/llm-equation-extraction-88-percent-below-human-threshold.md) [+W]
- [Neuro-symbolic feedback frameworks improved LLM translation accuracy only when the model received specific feedback on how to fix its responses; SymPy-based feedback barely improved performance](../claims/llm-modulo-specific-feedback-improves-equation-translation.md) [+W]
- [Smaller LLMs more often used undefined symbols, missed equations, and hallucinated equations; a 14B parameter model (Phi4) achieved only about 70% accuracy on the task](../claims/small-llms-undefined-symbols-phi4-70-percent.md) [+W]

## Related Strategies

- [Break synthesis clicker questions into separate sub-questions before combining them into one question](break-synthesis-clickers-into-sub-problems.md)
- [Break complex tasks into smaller sub-tasks when completing programming work with AI assistance](decompose-tasks-into-subtasks-for-ai-assistance.md)

## Examples
-

## Key Sources
- Lachlan McGinness and Peter Baumgartner. (2025). Can Large Language Models Correctly Interpret Equations with Errors? https://arxiv.org/abs/2505.10966

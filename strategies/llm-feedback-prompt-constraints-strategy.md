---
type: strategy
id: llm-feedback-prompt-constraints-strategy
title: Constrain LLM feedback prompts to physics content with a rubric and ideal-answer example
description: "The article's prompting approach instructs the LLM: \"You are an educator."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: winter-allen-2025
    resource: "https://arxiv.org/abs/2508.14759"
    title: "Winter Allen, Anand Shanker, N. Sanjay Rebello. (2025). Students' Perceptions to a Large Language Model's Generated Feedback and Scores of Argumentation Essays. arXiv preprint. https://arxiv.org/abs/2508.14759"
    author: Winter Allen, Anand Shanker, N. Sanjay Rebello
---

# Constrain LLM feedback prompts to physics content with a rubric and ideal-answer example

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 mixed) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article's prompting approach instructs the LLM: "You are an educator. Your goal is to provide useful feedback on the physics aspect of the essay. Your feedback should be no more than 100 words long." The prompt further forbids salutations, grammar commentary, and complements or critiques, and the API is fed the problem, an ideal answer example, and a rubric. The authors state that different methods of prompting can be explored, including prompting with specific guidelines based on prior feedback research.

## Design Implications

### Context
#### Requirements
- Access to the LLM via API, a scoring rubric out of 5 points, and an example of an ideal answer to feed the model.
#### Constraints
- The authors acknowledge that different methods of prompting can be explored and that comparing LLM scores to a human grader's scores remains future work.

### Target Learners
- students in large-enrollment introductory physics courses

### Target Learning Goals
- receiving individualized feedback on physics ideas in written arguments

## Claims

- [Rubric-grounded prompting alone provides limited proficiency control, aligning far better on content-oriented traits than on form-oriented traits](../claims/prompting-limited-uneven-proficiency-control-writing-simulation.md) [~W]

## Related Strategies

- [Design GPT feedback prompts with few-shot examples covering each response category and documented student preconceptions as context](few-shot-prompt-with-preconceptions-for-feedback-generation.md)
- [Craft educational LLM prompts using iterative refinement, role-playing, and constraints with suitable context](three-pillar-educational-prompting-strategy.md)

## Examples
-

## Key Sources
- Winter Allen, Anand Shanker, N. Sanjay Rebello. (2025). Students' Perceptions to a Large Language Model's Generated Feedback and Scores of Argumentation Essays. arXiv preprint. https://arxiv.org/abs/2508.14759

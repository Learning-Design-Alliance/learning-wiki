---
type: strategy
id: few-shot-exemplar-prompting-strategy-educators
title: Educators can improve AI classification of math tasks by few-shot prompting with curricular exemplars rather than waiting for model updates
description: This strategy has teachers supply a small set of expert-classified exemplar tasks (two per cognitive-demand category, eight total) drawn from curricular materials they already have, presented with the Task Analysis Gu...
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: fox-2026
    resource: "https://arxiv.org/abs/2605.30151"
    title: "Fox, D. S., Robles, B. L., DiPietro Brovey, E., & Schunn, C. D. (2026). Temporal Stability and Few-Shot Prompting in Math Task Assessment. https://arxiv.org/abs/2605.30151"
    author: "Fox, D. S., Robles, B. L., DiPietro Brovey, E., & Schunn, C. D"
---

# Educators can improve AI classification of math tasks by few-shot prompting with curricular exemplars rather than waiting for model updates

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (4 for, 1 mixed) · 3 studies (3 causal), `q2` · 0 of 3 report an effect size · 5 claims rest on one study

## Description
This strategy has teachers supply a small set of expert-classified exemplar tasks (two per cognitive-demand category, eight total) drawn from curricular materials they already have, presented with the Task Analysis Guide in LaTeX format in low-to-high demand order. The article frames few-shot prompting as "an accessible middle ground for teachers to improve their AI model's output," and its results show it raised both tools' accuracy, with Coteach recovering fully to baseline.

## Design Implications

### Context
#### Requirements
- Exemplars must be pre-classified by human experts and chosen for semantic similarity to the test tasks rather than identical wording.
#### Constraints
- Gains were not uniform across categories: Doing Mathematics tasks remained low even with few-shot prompting, and increased API token usage may raise cost, which the study did not evaluate.

### Target Learners
- K-12 mathematics teachers
- teacher educators

### Target Learning Goals
- accurate identification of the cognitive demand level of mathematics tasks during lesson planning

## Claims

- [Few-shot prompting with two exemplars per cognitive-demand category improved both AI tools' classification accuracy (Gemini 58% to 67%; Coteach 50% to 75%)](../claims/few-shot-prompting-improves-math-task-classification.md) [+W]
- [Few-shot prompting produced larger accuracy gains than model updates alone for both AI tools](../claims/few-shot-gains-exceed-model-update-gains.md) [+W]
- [Doing Mathematics task accuracy remained low from pre-test to post-test in one single-group pre-post study with no comparison group involving few-shot prompting; the authors discussed central-tendency bias and shortcut learning](../claims/few-shot-fails-doing-mathematics-tasks.md) [~W]
- [In-context examples improve LLM Bloom classification: three-shot and ten-shot prompting score at or above zero-shot on every dataset tested, and above it in most comparisons](../claims/in-context-examples-improve-bloom-classification.md) [+W]
- [Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance](../claims/curricular-cot-improves-accuracy-larger-models.md) [+W]

## Related Strategies

- [Use GPT-4 few-shot rephrasing of incorrect trainee responses to deliver corrective explanatory feedback at scale](gpt4-rephrase-incorrect-responses-feedback-strategy.md)

## Examples
-

## Key Sources
- Fox, D. S., Robles, B. L., DiPietro Brovey, E., & Schunn, C. D. (2026). Temporal Stability and Few-Shot Prompting in Math Task Assessment. https://arxiv.org/abs/2605.30151. [doi:10.48550/arxiv.2605.30151](https://doi.org/10.48550/arxiv.2605.30151)

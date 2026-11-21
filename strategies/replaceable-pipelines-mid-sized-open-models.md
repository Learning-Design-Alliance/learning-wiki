---
type: strategy
id: replaceable-pipelines-mid-sized-open-models
title: Build replaceable pipelines around robust APIs or mid-sized open models instead of training bespoke foundation models
description: The report advises researchers to take a pragmatic stance toward capability building and avoid competing with frontier model labs.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: marcus-kubsch-2025
    resource: "https://arxiv.org/abs/2511.14318"
    title: "Marcus Kubsch, Marit Kastaun, Peter Wulff, Nicole Graulich. (2025). Report on the Scoping Workshop on AI in Science Education Research. https://arxiv.org/abs/2511.14318"
    author: Marcus Kubsch, Marit Kastaun, Peter Wulff, Nicole Graulich
---

# Build replaceable pipelines around robust APIs or mid-sized open models instead of training bespoke foundation models

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The report advises researchers to take a pragmatic stance toward capability building and avoid competing with frontier model labs. Instead of investing scarce time in training bespoke foundation models, it recommends building replaceable pipelines around robust APIs or mid-sized open models such as Mistral that can be hosted locally, with evaluation harnesses allowing rapid swap-in of newer back-ends. It adds that for specialized tasks like short-answer scoring aligned to rubrics, smaller or similarity-based models may outperform generic LLMs given appropriate data and evaluation.

## Design Implications

### Context
#### Requirements
- Evaluation harnesses that allow rapid swap-in of newer back-ends
- Appropriate data and evaluation when using smaller or similarity-based models
#### Constraints
- Specialized performance needs are where smaller models may outperform generic LLMs

### Target Learners
- science education researchers
- graduate students

### Target Learning Goals
- AI-augmented research methods
- automated short-answer scoring

## Related Strategies

- [Standards-by-design: embed compliance checklists and audit hooks into data and MLOps pipelines](standards-by-design-ai-pipelines.md)
- [Reserve LLM grading for short, well-structured tasks with explicit rubrics or exemplar answers, newer models, and stable API pipelines](reserve-llm-grading-for-structured-rubric-tasks.md)
- [Use LLM in-context student synthesis with expert-data fine-tuning rather than building complex student-modeling pipelines](llm-incontext-student-synthesis-strategy.md)

## Examples
-

## Key Sources
- Marcus Kubsch, Marit Kastaun, Peter Wulff, Nicole Graulich. (2025). Report on the Scoping Workshop on AI in Science Education Research. https://arxiv.org/abs/2511.14318

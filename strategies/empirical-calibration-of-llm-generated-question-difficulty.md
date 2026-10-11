---
type: strategy
id: empirical-calibration-of-llm-generated-question-difficulty
title: Calibrate LLM-generated question difficulty empirically from student response data rather than trusting model-assigned labels
description: The article recommends treating LLM-assigned difficulty labels as uncalibrated and evaluating question difficulty using student response data, starting with Classical Test Theory difficulty indices and moving to Item...
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: yuan-an-2026
    resource: "https://arxiv.org/abs/2609.27063"
    title: "Yuan An, Lei Wang. (2026). Student Use of LLMs and the Limits of AI-Generated Question Difficulty in Data Science Courses. https://arxiv.org/abs/2609.27063"
    author: Yuan An, Lei Wang
---

# Calibrate LLM-generated question difficulty empirically from student response data rather than trusting model-assigned labels

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article recommends treating LLM-assigned difficulty labels as uncalibrated and evaluating question difficulty using student response data, starting with Classical Test Theory difficulty indices and moving to Item Response Theory as response volume grows. It concludes that "assigned difficulty labels require empirical calibration based on student performance." Future systems could select, retire, or update questions to match target difficulty levels, potentially using knowledge-graph-structured lecture materials for generation.

## Design Implications

### Context
#### Requirements
- Sufficient student response data per item to estimate difficulty (and eventually discrimination) values, using CTT initially and Item Response Theory as response volume grows
#### Constraints
- The study did not evaluate knowledge-graph conditioning directly; it is proposed as future work
- High overall accuracy in the studied corpus restricted score variance for item statistics

### Target Learners
- undergraduate and graduate data science students

### Target Learning Goals
- in-lecture retrieval practice for long-term retention of course content

## Related Strategies

- [Evaluate quantisation choices empirically on the target task and hardware rather than inheriting them from other studies](evaluate-quantisation-on-target-task.md)

## Examples
-

## Key Sources
- Yuan An, Lei Wang. (2026). Student Use of LLMs and the Limits of AI-Generated Question Difficulty in Data Science Courses. https://arxiv.org/abs/2609.27063

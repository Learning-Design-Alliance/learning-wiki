---
type: strategy
id: limited-distillation-for-scarce-evaluation-labels
title: Use knowledge distillation with deliberately limited synthetic data to expand scarce labeled evaluation datasets
description: When labeled data for a specialized evaluation task is scarce, the authors generate synthetic student-tutor conversations with a frontier LLM, prompting it to produce nine tutor responses per conversation (three high-...
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: tahmid-al-hannan-2026
    resource: "https://arxiv.org/abs/2607.10647"
    title: "Tahmid Al Hannan, Diego Garcia, Alex Njoroge, Suha Al Juboori, Tarek Sakakini. (2026). Knowledge Distillation for Automated AI Tutor Evaluation. https://arxiv.org/abs/2607.10647"
    author: Tahmid Al Hannan, Diego Garcia, Alex Njoroge, Suha Al Juboori, Tarek Sakakini
---

# Use knowledge distillation with deliberately limited synthetic data to expand scarce labeled evaluation datasets

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
When labeled data for a specialized evaluation task is scarce, the authors generate synthetic student-tutor conversations with a frontier LLM, prompting it to produce nine tutor responses per conversation (three high-quality, three average, three poor) to rebalance class distributions. Citing Stanton et al. (2021), they note that "excessively large distillation datasets can hinder optimization" and therefore deliberately limited the synthetic data. This produced 1,350 conversations and 12,150 labeled tutor responses.

## Design Implications

### Context
#### Requirements
- Access to a frontier LLM to generate synthetic conversations and labeled responses
- An existing annotated seed dataset whose label distribution can be analyzed for class imbalance
#### Constraints
- The article, citing Stanton et al. (2021), states that excessively large distillation datasets can hinder optimization, so synthetic data volume must be limited

### Target Learners
- K-12 and higher education students interacting with AI tutors

### Target Learning Goals
- Building reliable automated evaluators of AI tutor pedagogical quality when expert-labeled data is limited

## Related Strategies

- [Generate synthetic negative explanations with a small language model to balance imbalanced educational scoring datasets](synthetic-negative-examples-llm-dataset-balancing.md)
- [Use synthetic LLM-generated error datasets for AI tutors, teachable agents, and teacher professional development](synthetic-error-datasets-for-tutors-teachable-agents-teacher-pd.md)

## Examples
-

## Key Sources
- Tahmid Al Hannan, Diego Garcia, Alex Njoroge, Suha Al Juboori, Tarek Sakakini. (2026). Knowledge Distillation for Automated AI Tutor Evaluation. https://arxiv.org/abs/2607.10647

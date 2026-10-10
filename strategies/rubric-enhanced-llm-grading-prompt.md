---
type: strategy
id: rubric-enhanced-llm-grading-prompt
title: Provide LLM graders with the full human rubric, accepted solutions, and common-mistake penalties in the prompt (rubric-enhanced prompting)
description: "This strategy supplies the automated grader with the same structured guidance human evaluators use: general criteria plus question-specific scoring rules."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
sources:
  - id: alonso-carracedo-2026
    resource: "https://arxiv.org/abs/2607.02432"
    title: "Alonso-Carracedo, M., Fernandez-Boullon, R., Celard, P., Rodríguez-Martínez, F. J., Otero-Cerdeira, L. (2026). Automated grading of Linux/bash examinations using large language models: a four-level cognitive taxonomy approach. https://arxiv.org/abs/2607.02432"
    author: Alonso-Carracedo, M., Fernandez-Boullon, R., Celard, P., Rodríguez-Martínez, F. J., Otero-Cerdeira, L
---

# Provide LLM graders with the full human rubric, accepted solutions, and common-mistake penalties in the prompt (rubric-enhanced prompting)

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
This strategy supplies the automated grader with the same structured guidance human evaluators use: general criteria plus question-specific scoring rules. As the article states, "The rubric implemented in this variant provides general evaluation considerations such as completeness, command syntax, and correct path definition, while also incorporating question-specific aspects such as alternative valid solutions and common mistake penalties." It is implemented as a prompt variant (Variant 2) contrasted against a minimal no-rubric baseline to isolate the effect of criterial structure on grading.

## Design Implications

### Context
#### Requirements
- A developed and refined rubric documenting acceptable correct solutions and common student errors with point deductions
- Explicit prompt instructions for evaluating alternative solutions, since many bash commands have multiple valid implementations
#### Constraints
- The article frames the rubric's benefit as a hypothesis tested by comparing Variant 1 and Variant 2, and the reported score gains vary by model and taxonomy level

### Target Learners
- second-year undergraduate Computer Engineering students in an Operating Systems course

### Target Learning Goals
- accurate automated grading of short bash command-line exam responses with partial credit

## Related Strategies
- 

## Examples
-

## Key Sources
- Alonso-Carracedo, M., Fernandez-Boullon, R., Celard, P., Rodríguez-Martínez, F. J., Otero-Cerdeira, L. (2026). Automated grading of Linux/bash examinations using large language models: a four-level cognitive taxonomy approach. https://arxiv.org/abs/2607.02432

---
type: strategy
id: freetext-question-criteria-refinement-strategy
title: Iteratively refine question text against grading criteria by simulating a naive student
description: "FreeText can use assessment criteria to improve question text: one LLM instantiation answers the question while oblivious to the criteria, and a second instantiation evaluates that answer against the criteria to detec..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: matelsky-2023
    resource: "https://arxiv.org/abs/2308.02439"
    title: "Matelsky, J. K., Parodi, F., Liu, T., Lange, R. D., & Kording, K. P. (2023). A large language model-assisted education tool to provide feedback on open-ended responses. arXiv preprint. https://arxiv.org/abs/2308.02439"
    author: "Matelsky, J. K., Parodi, F., Liu, T., Lange, R. D., & Kording, K. P"
---

# Iteratively refine question text against grading criteria by simulating a naive student

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 2 studies (2 design), `q1`–`q3` · 0 of 2 report an effect size · 2 claims rest on one study

## Description
FreeText can use assessment criteria to improve question text: one LLM instantiation answers the question while oblivious to the criteria, and a second instantiation evaluates that answer against the criteria to detect whether students would be unfairly penalized by unclear question wording. The paper explains that "the question is updated to better encompass the requirements of the grading criteria." Updates should nudge toward the right material without giving new information.

## Design Implications

### Context
#### Requirements
- Instructor-provided grading criteria and original question text; two LLM instantiations (simulated student and evaluator)
#### Constraints
- A bad update explicitly asks about the criteria content, giving the student more information than the instructor intended

### Target Learners
- instructors designing open-ended questions

### Target Learning Goals
- fair and clear assessment question design

## Claims

- [GPT-4 achieved almost perfect inter-rater reliability with faculty after three iterations of rubric engineering on three of four medical school OEQ questions](../claims/gpt4-almost-perfect-irr-after-rubric-engineering.md) [+W]
- [Iterative persona refinement against reference answers achieved over 90% VSP response accuracy](../claims/vsp-persona-response-accuracy-over-90.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Matelsky, J. K., Parodi, F., Liu, T., Lange, R. D., & Kording, K. P. (2023). A large language model-assisted education tool to provide feedback on open-ended responses. arXiv preprint. https://arxiv.org/abs/2308.02439

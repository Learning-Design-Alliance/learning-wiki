---
type: strategy
id: predict-test-case-invalidity-before-delivery
title: Develop models that predict test case invalidity before delivery so invalid AI feedback can be filtered or repaired in real time
description: "The article proposes developing models that predict test case invalidity before delivery, \"enabling real-time filtering or repair\" of AI-generated failing test cases."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: hasnain-heickal-and-andrew-lan-2026
    resource: "https://arxiv.org/abs/2606.08807"
    title: "Hasnain Heickal and Andrew Lan. (2026). A Classroom Study of LLM-Generated Feedback Intervention in Introductory Programming. https://arxiv.org/abs/2606.08807"
    author: Hasnain Heickal and Andrew Lan
---

# Develop models that predict test case invalidity before delivery so invalid AI feedback can be filtered or repaired in real time

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article proposes developing models that predict test case invalidity before delivery, "enabling real-time filtering or repair" of AI-generated failing test cases. This strategy responds directly to the finding that only 66% of generated test cases were valid while 24% were false positives, which the authors link to heterogeneous effects of test case feedback on student performance. It is offered as a future-work direction for improving the reliability of test case feedback in classroom deployments.

## Design Implications

### Context
#### Requirements
- A model capable of predicting whether an AI-generated test case is invalid before it is delivered to the student.
#### Constraints
- The article presents this as future work, not as an implemented or tested intervention.

### Target Learners
- first-year introductory programming students

### Target Learning Goals
- debugging with AI-generated failing test case feedback

## Related Strategies

- [Combine data-driven and expert-driven approaches, and add a filter network, to mitigate non-factual output in automated feedback](combine-data-driven-expert-driven-feedback-generation.md)

## Examples
-

## Key Sources
- Hasnain Heickal and Andrew Lan. (2026). A Classroom Study of LLM-Generated Feedback Intervention in Introductory Programming. https://arxiv.org/abs/2606.08807

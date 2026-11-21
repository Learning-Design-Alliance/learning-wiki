---
type: strategy
id: instructor-steerable-refinement-policies-strategy
title: Develop adaptive, instructor-steerable refinement policies that decide which rubric dimensions to iterate
description: "The article's future-work recommendation is that systems move beyond fixed refinement settings toward policies that choose which feedback components to regenerate based on student needs and instructional intent, and e..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: fares-fawzi-2026
    resource: "https://arxiv.org/abs/2603.29142"
    title: "Fares Fawzi, Seyed Parsa Neshaei, Marta Knezevic, Tanya Nazaretsky, and Tanja Käser. (2026). REFINE: Real-world Exploration of Interactive Feedback and Student Behaviour. arXiv. https://arxiv.org/abs/2603.29142"
    author: Fares Fawzi, Seyed Parsa Neshaei, Marta Knezevic, Tanya Nazaretsky, and Tanja Käser
---

# Develop adaptive, instructor-steerable refinement policies that decide which rubric dimensions to iterate

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q2` · 1 of 1 report an effect size · 2 claims rest on one study

## Description
The article's future-work recommendation is that systems move beyond fixed refinement settings toward policies that choose which feedback components to regenerate based on student needs and instructional intent, and extend deployment to more courses and domains with richer tools and content. The authors write that "futuresystemsshouldexplore adaptive, instructor-steerable refinement policies that decide which rubric dimensionstoiteratebasedonstudentneedsandinstructionalintent". This addresses the deployment constraint that latency limited refinement to a subset of criteria.

## Design Implications

### Context
#### Requirements
- A rubric-based judge that can evaluate components selectively
- Latency budget allowing additional refinement iterations when needed
#### Constraints
- Current deployments targeted only current-state and task-level correctness to meet real-time latency constraints

### Target Learners
- undergraduate students in large STEM courses

### Target Learning Goals
- timely, pedagogically aligned formative feedback at scale

## Claims

- [Feedback quality rubric criteria showed significant pre-test-to-post-test gains across models after a single judge-guided regeneration step, with self-regulated next steps showing the largest gain, in one single-group pre-post study.](../claims/judge-guided-regeneration-improves-feedback-quality.md) [+W]
- [Feedback content steers student inquiry: highlighted rubric components are far more likely to be discussed in follow-up questions](../claims/highlighted-feedback-steers-student-inquiry.md) [+W]

## Related Strategies

- [Move beyond static skill-targeted rewriting toward interaction-aware adaptive error explanations](interaction-aware-adaptive-error-explanations.md)
- [Integrate GPT models into LA-supported feedback systems with an iterative instructor-student validation loop to improve reliability](iterative-validation-loop-gpt-feedback-systems.md)

## Examples
-

## Key Sources
- Fares Fawzi, Seyed Parsa Neshaei, Marta Knezevic, Tanya Nazaretsky, and Tanja Käser. (2026). REFINE: Real-world Exploration of Interactive Feedback and Student Behaviour. arXiv. https://arxiv.org/abs/2603.29142

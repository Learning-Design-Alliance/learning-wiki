---
type: strategy
id: adaptive-selective-self-explanation-prompting
title: Provide student-adaptive self-explanation prompts that target only example parts the student may not fully understand, rather than prompting at every step
description: "The SE-Coach's key innovative point was that prompts should be \"tailored to student individual differences both at the cognitive level (e.g., existing knowledge) and meta-cognitive level (e.g., tendency to self-explai..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
sources:
  - id: conati-2016
    resource: "https://doi.org/10.1007/s40593-015-0074-8"
    title: "Conati, C. (2016). Commentary on: “Toward Computer-Based Support of MetaCognitive Skills: a Computational Framework to Coach Self Explanation”. International Journal of Artificial Intelligence in Education, 26. https://doi.org/10.1007/s40593-015-0074-8"
    author: Conati, C
---

# Provide student-adaptive self-explanation prompts that target only example parts the student may not fully understand, rather than prompting at every step

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 review), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The SE-Coach's key innovative point was that prompts should be "tailored to student individual differences both at the cognitive level (e.g., existing knowledge) and meta-cognitive level (e.g., tendency to self-explain)". Based on its ongoing assessment, the SE-Coach "guides the student to more carefully explain only parts of the example that may not be fully understood", in contrast to prompting every step regardless of whether students already understand it.

## Design Implications

### Context
#### Requirements
- A student model that tracks reading patterns, chosen self-explanations, and their correctness to assess which example lines may benefit from further self-explanation
#### Constraints
- In the evaluation, students further along in the curriculum tended to ignore the more elaborated adaptive guidance, for which the control's milder scaffolding was sufficient

### Target Learners
- students studying worked-out examples in introductory physics

### Target Learning Goals
- domain knowledge acquisition from example studying
- self-explanation skill

### Affordances
- [Se Coach Framework](../products/se-coach.md)

## Claims

- [Eye-tracker attention patterns significantly improved a student model's ability to capture self-explanation versus a time-based predictor](../claims/eye-tracking-improves-self-explanation-modeling.md) [+W]
- [Adaptive SE-Coach scaffolding improved problem-solving performance for students in the early stage of learning Newton's Laws, at p<0.05](../claims/se-coach-adaptive-scaffolding-early-stage-learning-gains.md) [+W]
- [Explicit tutorial interventions successfully stimulated self-explanation in the SE-Coach evaluation](../claims/se-coach-interventions-stimulate-self-explanation.md) [+W]

## Related Strategies

- [Conduct systematic ablation studies comparing levels of interface scaffolding and tailoring to identify when scaffolding approaches are effective](ablation-studies-scaffolding-levels-and-tailoring.md)
- [Adaptive systems should deliver prior-knowledge-tailored discrepancy prompts and regular self-assessment calibration prompts](pk-tailored-discrepancy-prompts.md)
- [Metacognitive Reflection Prompts](metacognitive_reflection_prompts.md)
- [Faded Guidance](faded-guidance.md)

## Examples
-

## Key Sources
- Conati, C. (2016). Commentary on: “Toward Computer-Based Support of MetaCognitive Skills: a Computational Framework to Coach Self Explanation”. International Journal of Artificial Intelligence in Education, 26. https://doi.org/10.1007/s40593-015-0074-8

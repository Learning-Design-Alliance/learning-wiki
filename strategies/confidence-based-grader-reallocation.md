---
type: strategy
id: confidence-based-grader-reallocation
title: Reallocate graders to gradees based on model confidence so low-confidence submissions receive more or better graders
description: "Because the probabilistic model produces a belief distribution over each submission's grade, it can quantify how confident it is in each prediction."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-16
sources:
  - id: chris-piech-2013
    resource: "https://arxiv.org/abs/1307.2579"
    title: "Chris Piech, Jonathan Huang, Zhenghao Chen, Chuong Do, Andrew Ng, Daphne Koller. (2013). Tuned Models of Peer Assessment in MOOCs. arXiv. https://arxiv.org/abs/1307.2579"
    author: Chris Piech, Jonathan Huang, Zhenghao Chen, Chuong Do, Andrew Ng, Daphne Koller
---

# Reallocate graders to gradees based on model confidence so low-confidence submissions receive more or better graders

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
Because the probabilistic model produces a belief distribution over each submission's grade, it can quantify how confident it is in each prediction. The article proposes that midway through grading, submissions with low-confidence scores be given "to more and/or better graders", ensuring each student fair access to quality feedback. Its round-by-round simulation showed 54% of students remained below high confidence after all rounds, demonstrating the need for such reallocation.

## Design Implications

### Context
#### Requirements
- A probabilistic model producing calibrated posterior confidence estimates (validated as conservative in the article's experiments)
#### Constraints
- The article leaves open which specific grader is best for a particular submission, noting it could depend on writing styles and cultural or linguistic backgrounds

### Target Learners
- MOOC students in large-scale peer assessment courses

### Target Learning Goals
- Fair and accurate grading of open-ended assignments

### Affordances
- [Probabilistic Peer Grading Models Pg1 Pg2 Pg3](../research-methods/probabilistic-peer-grading-models-pg1-pg2-pg3.md)

## Claims

- [The model's posterior confidence estimates are conservative: over 95% of predictions the model claims 90–95% confidence in are correct](../claims/peer-grading-confidence-estimates-conservative.md) [+W]

## Related Strategies

- [Peer and Self-Assessment](peer_and_self-assessment.md)

## Examples
-

## Key Sources
- Chris Piech, Jonathan Huang, Zhenghao Chen, Chuong Do, Andrew Ng, Daphne Koller. (2013). Tuned Models of Peer Assessment in MOOCs. arXiv. https://arxiv.org/abs/1307.2579

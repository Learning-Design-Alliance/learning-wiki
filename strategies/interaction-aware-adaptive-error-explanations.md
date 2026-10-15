---
type: strategy
id: interaction-aware-adaptive-error-explanations
title: Move beyond static skill-targeted rewriting toward interaction-aware adaptive error explanations
description: "The authors recommend that future programming-support systems adapt explanations dynamically to the user's interaction state rather than assigning a fixed style."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: alexandru-radu-moraru-2026
    resource: "https://arxiv.org/abs/2608.20896"
    title: "Alexandru-Radu Moraru, Shreyan Biswas, Ujwal Gadiraju. (2026). Beyond the Traceback: Using LLMs for Adaptive Explanations of Programming Errors. https://arxiv.org/abs/2608.20896"
    author: Alexandru-Radu Moraru, Shreyan Biswas, Ujwal Gadiraju
---

# Move beyond static skill-targeted rewriting toward interaction-aware adaptive error explanations

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The authors recommend that future programming-support systems adapt explanations dynamically to the user's interaction state rather than assigning a fixed style. As they state, "Future systems should move beyond static skill-targeted rewriting toward interaction-aware support", with systems that "progressively disclose more detail when users struggle, offer concise summaries when users move quickly, or adapt explanations based on repeated failures and repair behavior". This strategy follows from their finding that static skill categories are likely too coarse for robust personalization.

## Design Implications

### Context
#### Requirements
- Systems must capture interaction signals such as repeated failed attempts, time spent before editing, edit location, error recurrence, or requests for additional detail
#### Constraints
- The article did not evaluate such adaptive systems; the recommendation is forward-looking, and the authors note such systems should also be evaluated for risks including over-reliance, false confidence, and fluent but incorrect explanations reinforcing misconceptions

### Target Learners
- novice and more experienced Python programmers using AI programming-support tools

### Target Learning Goals
- interpreting programming error messages and repairing buggy code

## Related Strategies

- [Use dynamic user models to recognize non-optimal learning behaviors and redirect students toward more effective behaviors](dynamic-user-models-redirect-non-optimal-behaviors.md)
- [Deliver AI-generated visual explanations adaptively based on learner engagement profiles rather than uniformly](adaptive-delivery-gats-by-engagement-profile.md)
- [Evaluate LLM-supported learning beyond binary access by measuring enacted interaction and preserving no-help assessments](evaluate-llm-learning-beyond-access.md)
- [Design AI tutors for complementarity across role paradigms and move beyond static prompting toward dynamic learner modeling](design-for-complementarity-and-dynamic-learner-modeling.md)

## Examples
-

## Key Sources
- Alexandru-Radu Moraru, Shreyan Biswas, Ujwal Gadiraju. (2026). Beyond the Traceback: Using LLMs for Adaptive Explanations of Programming Errors. https://arxiv.org/abs/2608.20896

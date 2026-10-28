---
type: strategy
id: delay-penalty-metacognitive-feedback
title: Metacognitive feedback with delay penalties proportional to value-of-computation differences
description: "A feedback mechanism in which the tutor responds to suboptimal planning choices by identifying the correct action and imposing \"a delay penalty, a short period of time in which the participant has to wait and can't in..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
sources:
  - id: heindrich-2025
    resource: "https://doi.org/10.1007/s40593-025-00493-7"
    title: "Heindrich, L., Consul, S., & Lieder, F. (2025). An Intelligent Tutor for Planning in Large Partially Observable Environments. International Journal of Artificial Intelligence in Education, 35, 3095–3127. https://doi.org/10.1007/s40593-025-00493-7"
    author: "Heindrich, L., Consul, S., & Lieder, F"
---

# Metacognitive feedback with delay penalties proportional to value-of-computation differences

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q3` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
A feedback mechanism in which the tutor responds to suboptimal planning choices by identifying the correct action and imposing "a delay penalty, a short period of time in which the participant has to wait and can't interact with the learning environment." "The duration of the delay penalty depends on the difference in VOC between the chosen planning action and the optimal planning, with larger mistakes resulting in longer delays." In the partially observable extension, all operations with negative VOC or VOC differing by more than 0.05 from the best receive the same penalty, and premature termination triggers a penalty proportional to estimated remaining planning value.

## Design Implications

### Context
#### Requirements
- An algorithm (MGPO) that can compute VOC values online for the current belief state
- A defined threshold for treating operations as equivalent
#### Constraints
- Penalty durations are fixed approximations (3 seconds base, 4 seconds maximum) rather than exactly proportional to Q-value differences

### Target Learners
- adult learners
- students in intelligent tutoring systems

### Target Learning Goals
- optimal planning strategy selection
- metacognitive awareness of information value

### Affordances
- Meta Level Mdp Partially Observable Planning

## Claims

- [A preregistered experiment with 330 participants demonstrated the intelligent tutor is highly effective at improving planning in partially observable environments](../claims/tutor-improves-human-planning-partially-observable.md) [+W]

## Related Strategies

- [Give Prompt Feedback](give_prompt_feedback.md)

## Examples
-

## Key Sources
- Heindrich, L., Consul, S., & Lieder, F. (2025). An Intelligent Tutor for Planning in Large Partially Observable Environments. International Journal of Artificial Intelligence in Education, 35, 3095–3127. https://doi.org/10.1007/s40593-025-00493-7

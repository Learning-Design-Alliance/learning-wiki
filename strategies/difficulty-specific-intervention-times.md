---
type: strategy
id: difficulty-specific-intervention-times
title: Set difficulty-specific intervention times based on when prediction quality exceeds a fixed threshold
description: The article proposes choosing an intervention time for each student difficulty by setting a limit for desired predictive quality and determining the specific time accordingly.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
sources:
  - id: kennel-2025
    resource: "https://doi.org/10.1007/s40593-024-00447-5"
    title: "Kennel, K., Ishimaru, S., Küchemann, S., Steinert, S., Kuhn, J., & Ruzika, S. (2025). Gaze-Based Prediction of Students' Math Difficulties - A Time Dynamic Machine Learning Approach to Enable Early Individual Assistance. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00447-5"
    author: "Kennel, K., Ishimaru, S., Küchemann, S., Steinert, S., Kuhn, J., & Ruzika, S"
---

# Set difficulty-specific intervention times based on when prediction quality exceeds a fixed threshold

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article proposes choosing an intervention time for each student difficulty by setting a limit for desired predictive quality and determining the specific time accordingly. For the discussed item with a bound of MCC = 0.7, "slope-height assistance after 15 s, block-slope assistance after 30 s, inverted-slope assistance after around 60 s." This enables early individual assistance during the solution process.

## Design Implications

### Context
#### Requirements
- Eye tracking data must be analyzed in real time during task solution
#### Constraints
- If the time is chosen too early, there is a risk that the algorithm will assign many learners to the wrong class

### Target Learners
- upper-secondary students solving calculus tasks

### Target Learning Goals
- graphical differentiation
- concept of the derivative

## Claims

- [On one graphical differentiation item, eye tracking data predicted students' specific difficulties as a multiclass classification problem](../claims/gaze-prediction-specific-math-difficulties-multiclass.md) [+W]

## Related Strategies

- [Tune the mind wandering detection threshold to the deployment setting, and choose thresholds by use case (recall for research, precision for interventions)](threshold-tuning-per-use-case-strategy.md)

## Examples
-

## Key Sources
- Kennel, K., Ishimaru, S., Küchemann, S., Steinert, S., Kuhn, J., & Ruzika, S. (2025). Gaze-Based Prediction of Students' Math Difficulties - A Time Dynamic Machine Learning Approach to Enable Early Individual Assistance. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00447-5

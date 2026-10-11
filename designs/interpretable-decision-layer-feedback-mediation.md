---
type: design
id: interpretable-decision-layer-feedback-mediation
title: Interpretable decision layer for outcome-independent coordination of teacher and student feedback
description: A transparent mechanism that combines teacher and student feedback to rank course topics needing attention without grades or outcome labels.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: junsoo-park-2026
    resource: "https://github.com/park-jsdev/classroom-feedback-mediator"
    title: "Junsoo Park, Youssef Medhat, Htet Phyo Wai, Ploy Thajchayapong and Ashok K. Goel. (2026). Surfacing Isolated Learners with Outcome-Independent Mediation of Feedback between Teachers and Students Using AI. HAI-Agency Workshop, AIED 2026. https://github.com/park-jsdev/classroom-feedback-mediator"
    author: Junsoo Park, Youssef Medhat, Htet Phyo Wai, Ploy Thajchayapong and Ashok K. Goel
---

# Interpretable decision layer for outcome-independent coordination of teacher and student feedback

> **Design** · [All designs](index.md)
> **Evidence** · 4 claims (4 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
A transparent mechanism that combines teacher and student feedback to rank course topics needing attention without grades or outcome labels. It integrates three signals — gap prevalence, survey disagreement, and teacher friction — into a topic priority score with a per-topic decision record explaining each ranking. The article states it "organizes teacher, student, and researcher roles around this shared decision process," positioning the layer as supporting human–AI co-agency rather than replacing instructor judgment.

## Design Implications

### Context
#### Requirements
- Teacher signals from coded instructor interviews, student signals from interaction traces and surveys, and researcher-defined weights must be available for the same course topics
#### Constraints
- Weights are specified rather than learned in the current implementation; the study reflects one graduate-level course offering and findings are preliminary and exploratory

### Target Learners
- graduate CS students in an AI-augmented classroom

### Learning Goals
- timely identification of course topics requiring instructional attention before graded outcomes are available

### Claims
- [Mediation Layer Priorities Align Instructor Concerns](../claims/mediation-layer-priorities-align-instructor-concerns.md) [+M]
- [Topic Priority Aligns Self Reported Difficulty](../claims/topic-priority-aligns-self-reported-difficulty.md) [+M]
- [Multi Signal Integration Surfaces Isolated Learners](../claims/multi-signal-integration-surfaces-isolated-learners.md) [+M]
- [Topic Priorities Stable Across Weights](../claims/topic-priorities-stable-across-weights.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Junsoo Park, Youssef Medhat, Htet Phyo Wai, Ploy Thajchayapong and Ashok K. Goel. (2026). Surfacing Isolated Learners with Outcome-Independent Mediation of Feedback between Teachers and Students Using AI. HAI-Agency Workshop, AIED 2026. https://github.com/park-jsdev/classroom-feedback-mediator

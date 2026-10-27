---
type: strategy
id: gaze-based-teacher-dashboards-feedback
title: Use gaze-based automated strategy identification for teacher dashboards and personalized feedback in online statistics learning
description: The article proposes that automated gaze-based strategy identification can enable teacher dashboards reporting which students use what strategy, and immediate personalized feedback during online learning.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
sources:
  - id: boels-2024
    resource: "https://doi.org/10.1007/s40593-023-00368-9"
    title: "Boels, L., Garcia Moreno-Esteva, E., Bakker, A., & Drijvers, P. (2024). Automated Gaze-Based Identification of Students' Strategies in Histogram Tasks through an Interpretable Mathematical Model and a Machine Learning Algorithm. International Journal of Artificial Intelligence in Education, 34, 931-973. https://doi.org/10.1007/s40593-023-00368-9"
    author: "Boels, L., Garcia Moreno-Esteva, E., Bakker, A., & Drijvers, P"
---

# Use gaze-based automated strategy identification for teacher dashboards and personalized feedback in online statistics learning

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (4 for, 1 mixed) · 3 studies (1 review, 1 design, 1 theoretical), `q2` · 0 of 3 report an effect size · 5 claims rest on one study

## Description
The article proposes that automated gaze-based strategy identification can enable teacher dashboards reporting which students use what strategy, and immediate personalized feedback during online learning. The authors state the results "allow for the future design of teacher dashboards that report which students use what strategy, or for immediate, personalized feedback during online learning, homework, or massive open online courses (MOOCs) through measuring eye movements, for example, with a webcam." This positions gaze data as a source for intelligent tutoring systems in statistics education.

## Design Implications

### Context
#### Requirements
- Eye-tracking technology accessible enough for large-scale use (e.g., webcam-based low-accuracy eye tracking expected to become standard)
- Automated strategy identification models (IMM or MLA) that perform well enough for real-time classification
#### Constraints
- This is described as a first step; a gaze-based ITS for statistics education does not yet exist
- Feedback on strategies can be provided earlier during problem-solving than feedback on answers alone, but the current study does not implement or test the feedback itself

### Target Learners
- Secondary and post-secondary students learning statistics online

### Target Learning Goals
- Correct interpretation of histograms
- Awareness of strategy correctness during problem-solving

## Claims

- [Students' horizontal or vertical gaze patterns on the graph area of single histograms are indicative of their task-specific strategies for estimating the mean](../claims/gaze-patterns-indicate-histogram-strategies.md) [+W]
- [An interpretable mathematical model based on saccade lengths and angles performs well, is transparent, and is theoretically meaningful for identifying students' histogram strategies](../claims/imm-transparent-performs-well.md) [+W]
- [The machine learning algorithm and the interpretable mathematical model identified the same task-solving strategies from students' gaze data](../claims/mla-imm-identify-same-strategies.md) [+W]
- [Mirroring dashboards improved teacher situational awareness while alerting-and-guiding dashboards reduced teacher workload and frustration](../claims/mirroring-alerting-dashboards-teacher-withitness.md) [+W]
- [Real-time AI alerts can expand teachers' situational awareness but in some cases overload teachers' attention or draw focus away from their own observation flow](../claims/ai-alerts-can-overload-teacher-attention.md) [~W]

## Related Strategies

- [Instructor Feedback Loops](instructor-feedback-loops.md)
- [Translate coupling indices into intuitive dashboards for teachers' reflective evaluation](coupling-dashboard-reflective-evaluation-strategy.md)

## Examples
-

## Key Sources
- Boels, L., Garcia Moreno-Esteva, E., Bakker, A., & Drijvers, P. (2024). Automated Gaze-Based Identification of Students' Strategies in Histogram Tasks through an Interpretable Mathematical Model and a Machine Learning Algorithm. International Journal of Artificial Intelligence in Education, 34, 931-973. https://doi.org/10.1007/s40593-023-00368-9

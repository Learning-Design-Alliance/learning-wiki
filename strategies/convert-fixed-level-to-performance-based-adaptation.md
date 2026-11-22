---
type: strategy
id: convert-fixed-level-to-performance-based-adaptation
title: Convert fixed-level training systems to performance-based difficulty adaptation
description: "The article recommends a concrete recipe for turning a trainer with instructor-selected difficulty levels into an adaptive one: \"Instead of selecting among a few discrete difficulty levels, RAFT maintains a continuous..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: amit-dutta-2026
    resource: "https://arxiv.org/abs/2608.20751"
    title: "Amit Dutta, Sushil J. Louis. (2026). Adaptive Training for Nautical Rules of the Road. https://arxiv.org/abs/2608.20751"
    author: Amit Dutta, Sushil J. Louis
---

# Convert fixed-level training systems to performance-based difficulty adaptation

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (4 for) · 1 study (1 causal), `q3` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
The article recommends a concrete recipe for turning a trainer with instructor-selected difficulty levels into an adaptive one: "Instead of selecting among a few discrete difficulty levels, RAFT maintains a continuous difficulty value, updates that value from student performance, and maps it to variables that control the next scenario." This allows the trainer to increase scenario difficulty gradually as a student progresses, while keeping content and interface constant. The study's results support that this configuration improved learning outcomes and engagement.

## Design Implications

### Context
#### Requirements
- A measurable student performance score per exercise
- Scenario variables that can be parameterized by a difficulty value
#### Constraints
- The reported adaptation rule only increases difficulty; the authors plan methods that can both increase and decrease difficulty

### Target Learners
- individual trainees in simulation-based skills training

### Target Learning Goals
- improving learning outcomes and engagement in simulation-based training

### Affordances
- [Raft Performance Based Difficulty Model](../products/raft-performance-based-difficulty-adaptation-model.md)

## Claims

- [Students who received adaptive RAFT training achieved significantly higher post-test scores than students who received non-adaptive RoR training](../claims/adaptive-raft-higher-posttest-scores-ror.md) [+W]
- [Difficulty values for all 15 students in the RAFT condition rose from the novice range to the intermediate range during training, measured within that group from start to end](../claims/raft-difficulty-trajectories-novice-to-intermediate.md) [+W]
- [After experiencing both trainers, most students judged RAFT more effective and rated it higher on engagement and feedback](../claims/student-preferences-favor-raft.md) [+W]
- [Within-condition learning gains appeared only in the adaptive condition: RAFT scores rose significantly pre- to post-test while RoR showed no significant improvement](../claims/within-condition-gains-only-raft.md) [+W]

## Related Strategies

- [Adaptive Learning](adaptive-learning.md)
- [Adaptive speed-of-processing training protocol with tailored durations, feedback, and progressive difficulty](adaptive-speed-of-processing-training-protocol.md)
- [Adaptively time feedback to moments of declining attention or rising workload rather than delivering at fixed intervals](adaptive-timing-over-fixed-interval-feedback.md)
- [Deconstruct procedures into basic skills, build dedicated exercises for each subskill, evaluate learners against them, and select activities to match the evaluation.](deconstruct-procedures-into-basic-skills.md)

## Examples
-

## Key Sources
- Amit Dutta, Sushil J. Louis. (2026). Adaptive Training for Nautical Rules of the Road. https://arxiv.org/abs/2608.20751

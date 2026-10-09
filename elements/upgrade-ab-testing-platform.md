---
type: element
id: upgrade-ab-testing-platform
title: UpGrade open-source A/B testing platform for classroom-embedded field experiments
description: UpGrade, developed by Carnegie Learning in 2020, is an open-source platform for conducting field trials in educational software.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
sources:
  - id: murphy-a-2026-july-classroom-based
    resource: "https://doi.org/10.51388/20.500.12265/306"
    title: "Murphy, A. (2026, July). Classroom-Based experimentation in a digital learning platform. Digital Promise. https://doi.org/10.51388/20.500.12265/306"
---

# UpGrade open-source A/B testing platform for classroom-embedded field experiments

> **Element** · [All elements](index.md)
> **Evidence** · 3 claims (3 for) · 3 studies (2 causal, 1 qualitative), `q2` · 0 of 3 report an effect size · 3 claims rest on one study

## Description
UpGrade, developed by Carnegie Learning in 2020, is an open-source platform for conducting field trials in educational software. It acts as a middle layer between a client application and the experimenter, managing "scheduling, randomization, and parameterization of all experiments (and feature flags)" via three key API calls and decision points. It supports individual and group random assignment and lets experiments enroll students as they encounter target content in adaptive curricula. To date it has been used in over 73 field experiments impacting hundreds of thousands of students.

## Design Implications

### Context
#### Requirements
- Integration with a client app requires adding three key API calls that initialize UpGrade and check for active experiments.
#### Constraints
- Created specifically to address challenges with running large-scale field tests in real classrooms; most useful when students use adaptive digital materials.

### Target Learners
- K-12 students using educational software such as MATHia

### Target Learning Goals
- Evaluating the effectiveness of digital learning platform interventions through randomized experiments

## Claims

- [Localizing word-problem character names improved MATHia performance only for specific subgroup-majority schools, with no improvement in sense of belonging overall](../claims/localized-names-personalization-subgroup-performance.md) [+W]
- [Rewriting MATHia word problems for struggling readers, by human experts or LLMs, sped completion by 30% and improved mastery rate](../claims/rewritten-word-problems-faster-completion-mastery.md) [+W]
- [Carnegie Learning attributes positive practitioner feedback to connecting research to participants' needs, lowering effort barriers, and compensating participation](../claims/carnegie-learning-practitioner-engagement-tactics.md) [+W]

## Related Elements

- [MATHia intelligent tutoring system with adaptive mastery-based instruction](mathia-intelligent-tutoring-system.md)
- [MATHia/UpGrade: open-source field-trial platform integrated with Carnegie Learning's adaptive math tutoring system](mathia-upgrade-field-trial-platform.md)
- [ASSISTments/E-TRIALS: free A/B testing platform integrated with a K-12 math practice platform](assistments-e-trials-platform.md)
- [MATHia tutoring software](mathia-tutoring-software.md)
- [SEERNet: a network of five digital learning platforms operating as research infrastructure](seernet-dlp-research-infrastructure.md)
- [SEERNet network connecting platforms, researchers, and educators](seernet-network-element.md)

## Examples

- [Design classroom-embedded experiments as small, focused, theory-driven manipulations](../strategies/focused-theory-driven-embedded-manipulations.md)
- [Prioritize process-data instrumentation, open collaboration, and dissemination in learning platforms](../strategies/platform-instrumentation-open-research-recommendations.md)

## Key Sources
- Murphy, A. (2026, July). Classroom-Based experimentation in a digital learning platform. Digital Promise. https://doi.org/10.51388/20.500.12265/306

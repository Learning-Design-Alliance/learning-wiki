---
type: design
id: closed-loop-three-layer-interpretable-its-architecture
title: Closed-loop three-layer interpretable ITS architecture linking multimodal scoring, expressive diagnostics, and conversational coaching
description: The article proposes an ITS architecture that treats assessment not as an endpoint but as part of a closed loop of practice, feedback, and behavioral adjustment.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: hung-yue-suen-and-kuo-en-hung-2026
    resource: "https://doi.org/10.1109/TLT.2026.3693864"
    title: "Hung-Yue Suen and Kuo-En Hung. (2026). An Interpretable Closed-Loop Intelligent Tutoring System for Multimodal Affective Feedback in Asynchronous Presentation Training. IEEE Transactions on Learning Technologies. https://doi.org/10.1109/TLT.2026.3693864"
    author: Hung-Yue Suen and Kuo-En Hung
---

# Closed-loop three-layer interpretable ITS architecture linking multimodal scoring, expressive diagnostics, and conversational coaching

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 associational), `q3` · 1 of 1 report an effect size · 2 claims rest on one study

## Description
The article proposes an ITS architecture that treats assessment not as an endpoint but as part of a closed loop of practice, feedback, and behavioral adjustment. It is "structured as a closed-loop feedback system with three distinct layers": a performance layer presenting Overall Rating and six BARS dimension scores, an emotion-aware expressive diagnosis layer treating audience-facing cues as behavioral signals, and a Conversational AI Tutor that resolves learner queries using retrieved analytic evidence. The design aims to move learners from performance awareness to interpretation to actionable change.

## Design Implications

### Context
#### Requirements
- Rubric-aligned (BARS) annotated training data so scores trace to observable performance cues
- A retrieval layer restricting tutor generation to the learner's own multimodal records
#### Constraints
- Asynchronous, upload-based design; no real-time feedback during live performance
- Multimodal signals are summarized rather than modeled temporally
- Adapting to a new rubric or domain requires re-annotation and retraining (cold-start dependency)

### Target Learners
- adult learners and working professionals practicing on-camera oral presentation

### Learning Goals
- on-camera oral presentation delivery and content skills

### Claims
- [Its Prepost Gains All Seven Bars Dimensions](../claims/its-prepost-gains-all-seven-bars-dimensions.md) [+M]
- [Practice Frequency Predicts Posttest Performance](../claims/practice-frequency-predicts-posttest-performance.md) [+M]

## Related Designs

- [cc-self-train adaptive learning system: a three-layer hook-based engagement observation and scaffolding adjustment mechanism](cc-self-train-adaptive-learning-system.md)
- [Closed-loop adaptive teaching assistance model integrating perception, evaluation, generation and feedback for music education](closed-loop-adaptive-music-teaching-assistance-model.md)
- [Intelligent tutoring systems as three-model architectures operationalizing formative assessment](its-three-core-components-architecture.md)
- [AI Expert Feedback Ecology: a closed-loop cognition framework linking AI Twins, AI Tutors, dashboards, and learners](ai-expert-feedback-ecology.md)

## Examples
-

## Key Sources
- Hung-Yue Suen and Kuo-En Hung. (2026). An Interpretable Closed-Loop Intelligent Tutoring System for Multimodal Affective Feedback in Asynchronous Presentation Training. IEEE Transactions on Learning Technologies. https://doi.org/10.1109/TLT.2026.3693864

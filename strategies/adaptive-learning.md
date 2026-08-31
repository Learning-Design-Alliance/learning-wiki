---
type: strategy
title: Adaptive Learning
description: A strategy in which instruction, task difficulty, or pacing adjusts dynamically to individual learner performance, typically via algorithmic or rule-based systems.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Adaptive Learning

> **Strategy** · [All strategies](index.md)

## Description
Adaptive learning adjusts instructional content, task difficulty, pacing, or feedback in response to ongoing evidence of each learner's performance, rather than delivering a fixed sequence to all learners. Adaptation may be rule-based (e.g., mastery thresholds) or algorithmic (e.g., Bayesian knowledge tracing, item-response-theory-driven selection), implemented by a system or by a teacher using formative data.

## Design Implications

Adaptive systems work by keeping each learner operating at the edge of their current competence — challenging enough to induce learning, easy enough to avoid overload or discouragement [Adaptive learning improves learning outcomes relative to non-adaptive instruction.](../claims/adaptive-learning-improves-outcomes.md) [+M]. The mechanism is largely indirect: adaptation is valuable insofar as it enforces mastery, manages [Cognitive Load](../principles/cognitive-load-management.md), and delivers timely feedback — not because personalization is inherently powerful. Poorly calibrated adaptation (e.g., advancing on weak evidence of mastery) can be worse than fixed sequencing.

### Context
#### Requirements
- A valid, sensitive measure of learner state (accuracy alone is weak; latency and confidence add signal)
- An explicit adaptation rule: what triggers remediation, advancement, or [Fading](../elements/fading.md) of support
- A sufficiently large pool of tasks at graded difficulty levels, aligned to the target [Learning Goals](../elements/learning-goals.md)
- Mastery thresholds set high enough that "passed" means durable learning, not momentary luck

#### Constraints
- Adaptation based on noisy or sparse performance data misroutes learners; early errors in the learner model compound over a sequence [-M]
- Over-adaptation can narrow exposure — learners never see content the algorithm predicts they will fail, blocking productive struggle [~M]
- Effects shrink or reverse for advanced learners, who are often better served by less guidance and more challenge (the expertise-reversal pattern) [~M]
- Adaptive difficulty tuned to maintain a fixed high success rate (~90%+) can reduce effortful retrieval compared with desirable difficulties [~S]

#### Implementation Variability
- **Macro-adaptation:** routing between whole units or tracks based on pre-assessment
- **Micro-adaptation:** selecting the next item or hint level within a task ([Adaptive Difficulty](../elements/adaptive-difficulty.md))
- **Mastery-based adaptation:** requiring criterion performance before advancement ([Adaptive Mastery Learning](../elements/adaptive-mastery-learning.md))
- **Teacher-mediated adaptation:** instructors adjust instruction using dashboard data rather than automating decisions

### Target Learners
- Novices and lower-prior-knowledge learners, who benefit most from calibrated task difficulty and immediate remediation [Adaptive learning improves learning outcomes relative to non-adaptive instruction.](../claims/adaptive-learning-improves-outcomes.md) [+M]
- Learners in large heterogeneous groups where a single fixed pace fits few students
- Less beneficial for experts or fast learners, for whom adaptation often adds redundancy and slows progress [~M]

### Target Learning Goals
- Procedural fluency and automaticity in well-structured domains (mathematics, language learning, coding)
- Mastery of hierarchical prerequisite knowledge
- Less suited to ill-structured goals — argumentation, design, collaboration — where "correct performance" is hard to model

### Instructions
1. Define the knowledge/skill model: decompose the domain into prerequisites and map task difficulty levels.
2. Establish a baseline through diagnostic assessment or embedded early items.
3. Set adaptation rules: mastery thresholds for advancement, remediation triggers, and support-fading conditions ([Adaptive Mastery Learning](../elements/adaptive-mastery-learning.md)).
4. Deliver tasks with immediate, actionable [Feedback](../elements/feedback.md); adapt difficulty to keep learners in a productive challenge band ([Adaptive Difficulty](../elements/adaptive-difficulty.md)).
5. Review system decisions periodically — audit for learners stuck in remediation loops or advancing without mastery — and override the algorithm where the model is wrong.

## Related Strategies
- [Mastery Learning](mastery-learning.md) — the instructional logic most adaptive systems automate; adaptation without a mastery criterion is mere pacing variation
- [Spaced Retrieval](spaced-retrieval.md) — adaptive scheduling of review items (e.g., expanding intervals) is a common and well-supported adaptation dimension
- [Formative Assessment](formative-assessment.md) — supplies the performance evidence on which any adaptation depends

## Examples
- **[ASSISTments](https://www.assistments.org)** — free math platform that adapts problem selection and scaffolding based on student responses; evaluated in randomized controlled trials in Maine middle schools.
- **[Khan Academy](https://www.khanacademy.org)** — mastery-based progression where exercises unlock as learners demonstrate proficiency, with hints and remedial tasks triggered by errors.
- **[Duolingo](https://www.duolingo.com)** — adaptive item scheduling and difficulty adjustment using learner error and response-latency data.
- **[ALEKS](https://www.aleks.com)** — knowledge-space-theory system that maps what a learner is ready to learn and restricts topic choice accordingly.

## Key Sources
- Kulik, C.-L. C., Kulik, J. A., & Bangert-Drowns, R. L. (1990). Effectiveness of mastery learning programs: A meta-analysis. *Review of Educational Research, 60*(2), 265–299. [doi:10.3102/00346543060002265](https://doi.org/10.3102/00346543060002265)
- VanLehn, K. (2011). The relative effectiveness of human tutoring, intelligent tutoring systems, and other tutoring systems. *Educational Psychologist, 46*(4), 197–221. [doi:10.1080/00461520.2011.611369](https://doi.org/10.1080/00461520.2011.611369)
- Pane, J. F., Steiner, E. D., Baird, M. D., Hamilton, L. S., & Pane, J. D. (2017). Informing progress: Insights on personalized learning and adaptive educational technology. *RAND Corporation.* [doi:10.7249/RR2042](https://doi.org/10.7249/RR2042)
- Corbett, A. T., & Anderson, J. R. (1994). Knowledge tracing: Modeling the acquisition of procedural knowledge. *User Modeling and User-Adapted Interaction, 4*(4), 253–278. [doi:10.1007/BF01099821](https://doi.org/10.1007/BF01099821)
---
type: strategy
title: Provide Feedback
description: Delivering specific, actionable information to learners about their performance relative to a goal, timed so it can still be used to improve subsequent attempts.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Provide Feedback

## Description
Providing feedback means giving learners information about the correctness, quality, or appropriateness of their performance, together with guidance on how to close the gap between current and desired performance. It is carried out through instructor comments, automated system responses, peer review, rubric-based evaluation, or self-assessment against criteria — ideally while the learner is still working toward the goal, not after it has passed.

## Design Implications

Feedback is among the most powerful influences on learning, but its effects are highly variable: it works when learners act on it and fails when it merely grades or praises [~S]. Effective feedback answers three questions — *Where am I going? How am I going? Where to next?* — and is specific to the task rather than to the person [Hattie & Timperley's feedback model frames feedback at task, process, and self-regulation levels.](https://doi.org/10.3102/003465430750010081) [+S]. Feedback should follow [Practice](../elements/practice.md) closely and be actionable: the learner must be able to do something different on the next attempt.

### Context
#### Requirements
- A clear performance goal or criterion the feedback references (rubrics, exemplars, or worked models)
- Opportunities for the learner to *use* the feedback — revision, retry, or a subsequent task ([Practice](../elements/practice.md), [Revision](../elements/revision.md))
- Feedback focused on the task and process, not on the learner's global ability or worth
- Timing that keeps the feedback usable — immediate for procedural skills, delayed slightly for complex tasks to avoid interrupting effortful processing

#### Constraints
- Feedback on the self ("You're so smart") can reduce persistence and performance [Person-praise undermines motivation and persistence compared with process-praise.](https://doi.org/10.1126/science.1064991) [-S]
- When learners are still struggling to understand the task itself, detailed corrective feedback can overload working memory [~M] — brief, goal-directed feedback works better early on
- Feedback without an opportunity to revise produces little durable learning; grades alone frequently have near-zero or negative effects [~S]
- Automated feedback that flags errors without explaining why encourages trial-and-error rather than understanding [-M]

#### Implementation Variability
- **Immediate vs. delayed:** immediate feedback supports procedural skill acquisition; delayed feedback can benefit complex conceptual tasks by allowing self-correction first [~M]
- **Automated:** intelligent tutoring systems deliver step-level feedback at scale (e.g., ASSISTments, Khan Academy hints)
- **Peer feedback:** structured protocols (e.g., critique with rubrics) make peer comments usable; unstructured peer comments often mirror the quality problems of instructor comments
- **Feed-forward:** replacing or supplementing grades with "next-step" comments shifts attention from outcome to improvement

### Target Learners
- Novices, who lack the knowledge to detect and diagnose their own errors [~S]
- Struggling learners, for whom specific corrective information prevents error consolidation
- High-achieving learners may benefit more from process- and self-regulation-level feedback than from task-level confirmation [~M]

### Target Learning Goals
- Procedural accuracy: correcting errors before they become entrenched
- Conceptual understanding: surfacing and addressing misconceptions
- Self-regulation: building learners' capacity to monitor and adjust their own work

### Instructions
1. Establish the goal and criteria before the task, using [Rubrics](../elements/rubrics.md) or [Advance Organizers](../elements/advance-organizers.md) so feedback has a reference point.
2. Have learners attempt the task through [Practice](../elements/practice.md).
3. Deliver feedback that is specific, task-focused, and actionable — identify what was correct, what was not, and the next step.
4. Require learners to act on the feedback through revision or a subsequent attempt ([Assessment for Learning](../principles/assessment-for-learning.md)).
5. Gradually shift toward learner-generated self-assessment against criteria to build independence.

## Related Strategies
- [Action-Oriented Feedback](action-oriented-feedback.md) — a specific formulation of feedback that mandates a next action
- [Formative Assessment](../principles/assessment-for-learning.md) — the assessment cycle that generates feedback opportunities
- [Peer Review](../elements/peer-review.md) — distributes feedback generation to learners

## Examples
- **ASSISTments** ([https://www.assistments.org](https://www.assistments.org)) — math homework platform delivering immediate, step-level feedback to students and error reports to teachers.
- **Writing revision cycles** in process-writing curricula — drafts receive criterion-referenced comments and must be revised, converting feedback into observable improvement.
- **Khan Academy** ([https://www.khanacademy.org](https://www.khanacademy.org)) — practice exercises provide instant correctness feedback with hint ladders that scaffold toward the solution.

## Key Sources
- Hattie, J., & Timperley, H. (2007). The power of feedback. *Review of Educational Research, 77*(1), 81–112. [doi:10.3102/003465430298487](https://doi.org/10.3102/003465430298487)
- Black, P., & Wiliam, D. (1998). Assessment and classroom learning. *Assessment in Education: Principles, Policy & Practice, 5*(1), 7–74. [doi:10.1080/0969595980050102](https://doi.org/10.1080/0969595980050102)
- Mueller, C. M., & Dweck, C. S. (1998). Praise for intelligence can undermine children's motivation and performance. *Journal of Personality and Social Psychology, 75*(1), 33–52. [doi:10.1037/0022-3514.75.1.33](https://doi.org/10.1037/0022-3514.75.1.33)
- Shute, V. J. (2008). Focus on formative feedback. *Review of Educational Research, 78*(1), 153–189. [doi:10.3102/0034654307313795](https://doi.org/10.3102/0034654307313795)
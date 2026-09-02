---
type: strategy
id: instructor-feedback
title: Instructor Feedback
description: Instructor-provided information about a learner's performance that closes the gap between current and desired performance.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Instructor Feedback

> **Strategy** · [All strategies](index.md)

## Description
Instructor feedback is information provided by a teacher, tutor, or system acting in an instructional role about a learner's performance, intended to reduce the gap between what the learner did and what the task required. It ranges from simple correctness confirmation to detailed explanations of errors, hints toward better strategies, and guidance on self-regulation. Its effectiveness depends less on how much is given than on whether the learner can act on it.

## Design Implications

Feedback is one of the most powerful influences on learning, but also one of the most variable — it can improve or degrade achievement depending on its focus and timing [The power and variability of feedback is well established.](https://doi.org/10.1037/0033-2909.120.2.254) [~S]. Feedback that directs attention to the task and the process outperforms feedback directed at the person ("You're so smart") or at vague self-perceptions [Feedback should answer where am I going, how am I doing, and where to next.](https://doi.org/10.1080/00405840709554545) [+S]. Feedback embedded in [Assessment for Learning](../principles/assessment-for-learning.md) practices — with opportunities to act on it — improves achievement [Formative assessment with actionable feedback raises achievement.](../claims/assessment-for-learning-improves-achievement.md) [+S].

### Context
#### Requirements
- A clear performance criterion or rubric so feedback can reference a shared standard
- Timing that lets learners revise while the task is still active ([Check-In](../elements/check-in.md) points during work, not only after submission)
- Specific, actionable statements: what was done, why it works or fails, and what to do next
- An opportunity for the learner to respond — revise, retry, or explain — so feedback becomes input to [Practice](../elements/assess-performance.md) rather than a verdict

#### Constraints
- Feedback without opportunity to act is largely wasted effort; learners often ignore comments when no revision follows
- Praise and person-focused feedback can reduce performance, especially after failure [Feedback can decrease performance when it directs attention to the self.](https://doi.org/10.1037/0033-2909.120.2.254) [-S]
- Overly detailed feedback can overwhelm working memory for novices [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) [-M] — limit to two or three priority points
- Checklists and rubric scores alone, without explanatory comments, show weak effects online [Checklist evaluation is ineffective online.](../claims/checklist-evaluation-ineffective-online.md) [-W]

#### Implementation Variability
- **Immediate vs. delayed:** immediate feedback suits procedural skills and early learning; delayed feedback can benefit complex tasks by allowing initial self-correction [~M]
- **Written, oral, or dialogic:** dialogue (e.g., [5-Minute Writing Conferences](5-minute_writing_conferences.md)) lets the instructor diagnose the learner's reasoning, not just the artifact
- **Peer vs. instructor:** peer feedback builds evaluative judgment but needs training and calibration against instructor standards
- **Automated:** adaptive systems deliver item-level feedback at scale but struggle with higher-order goals

### Target Learners
- Novices benefit most from task-level, directive feedback that corrects errors before they consolidate
- Struggling learners need process-level feedback ("try this strategy") rather than outcome-level scores
- Advanced learners benefit more from metacognitive prompts to self-evaluate than from directive correction [~M]

### Target Learning Goals
- Skill refinement: closing specific gaps between performance and criteria
- Conceptual understanding: diagnosing and repairing misconceptions
- Self-regulation: building learners' capacity to evaluate and adjust their own work [Formative assessment with actionable feedback raises achievement.](../claims/assessment-for-learning-improves-achievement.md) [+S]

### Instructions
1. Establish criteria before the task using [Advance Organizers](../elements/advance-organizers.md) or a rubric, so feedback references a shared standard.
2. Build in an early [Check-In](../elements/check-in.md) to catch errors while correction is cheap.
3. Deliver feedback focused on the task and process: name what was done, explain the gap against criteria, and give one concrete next step.
4. Require a response — revision, retry, or [Articulation](../elements/articulation.md) of what changed — so feedback is acted on, not filed.
5. Fade over time: shift from directive correction toward prompts for self-assessment as competence grows.

## Related Strategies
- [Action-Oriented Feedback](action-oriented-feedback.md) — the specific framing of feedback as a next action rather than a judgment
- [5-Minute Writing Conferences](5-minute_writing_conferences.md) — brief dialogic feedback during the writing process

## Examples
- **Writing instruction with revision cycles:** instructors comment on drafts against a rubric, students revise before grading — the structure used in portfolio-based composition programs such as [Calibrated Peer Review](https://cpr.molsci.ucla.edu/).
- **Khan Academy** ([khanacademy.org](https://www.khanacademy.org)) — immediate correctness feedback and hint ladders on practice items, exemplifying task-level immediate feedback at scale.
- **Formative assessment in UK classrooms:** Black & Wiliam's review documented large gains from comment-only feedback (no grades) with revision opportunities.

## Key Sources
- Hattie, J., & Timperley, H. (2007). The power of feedback. *Review of Educational Research, 77*(1), 81–112. [doi:10.3102/003465430298487](https://doi.org/10.3102/003465430298487)
- Shute, V. J. (2008). Focus on formative feedback. *Review of Educational Research, 78*(1), 153–189. [doi:10.3102/0034654307313795](https://doi.org/10.3102/0034654307313795)
- Kluger, A. N., & DeNisi, A. (1996). The effects of feedback interventions on performance: A historical review, a meta-analysis, and a preliminary feedback intervention theory. *Psychological Bulletin, 119*(2), 254–284. [doi:10.1037/0033-2909.119.2.254](https://doi.org/10.1037/0033-2909.119.2.254)
- Black, P., & Wiliam, D. (1998). Assessment and classroom learning. *Assessment in Education: Principles, Policy & Practice, 5*(1), 7–74. [doi:10.1080/0969595980050102](https://doi.org/10.1080/0969595980050102)
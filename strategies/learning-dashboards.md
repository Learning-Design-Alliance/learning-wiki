---
type: strategy
title: Learning Dashboards
description: Visual displays of learner activity and performance data intended to support self-regulated learning and instructional decision-making.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Learning Dashboards

> **Strategy** · [All strategies](index.md)

## Description
Learning dashboards aggregate data about learner behavior (time on task, progress, quiz scores, peer comparison) and present it visually to learners, instructors, or both. They are carried out by embedding analytics visualizations in a learning environment — course homepages, LMS widgets, or standalone tools — with the intent that seeing the data prompts reflection, goal-setting, or corrective action.

## Design Implications

Dashboards are only as effective as the self-regulatory behavior they trigger; displaying data does not by itself change learning [~M]. Their value depends on whether the displayed metrics are actionable (tied to specific next steps rather than raw activity counts) and whether they support rather than undermine motivation. Comparative displays are the most consequential design choice: normative comparisons (rankings, class averages) can motivate or demotivate depending on the learner's standing and goal orientation [~M].

### Context
#### Requirements
- Valid, timely data — metrics must actually relate to learning outcomes, not just engagement proxies
- Actionable framing: each display should suggest what to do next ([Assessment](../elements/assessment.md) feedback loops, recommended resources)
- Learner support in interpreting the data — dashboards without guidance on how to respond rarely change behavior [~M]
- Alignment with [Assessment for Learning](../principles/assessment-for-learning.md) — the dashboard should function as formative feedback, not surveillance

#### Constraints
- Raw activity metrics (logins, minutes spent) correlate weakly with achievement and can encourage gaming or shallow "time-on-task" behavior [-M]
- Normative peer comparisons depress motivation and engagement for lower-performing learners [~M] — self-referenced (progress over time) displays avoid this
- Information overload: too many indicators degrades use; [Chunking](../principles/chunking.md) and progressive disclosure of detail are necessary
- Dashboards can create a false sense of mastery when completion or activity is displayed as if it were competence [-M]

#### Implementation Variability
- **Learner-facing** (self-regulation support): progress bars, goal-setting, self-referenced trends
- **Instructor-facing** (teaching analytics): at-risk identification, cohort patterns, triggering [Check-ins](../elements/check-in.md) or outreach
- **Comparative vs. self-referenced**: rankings vs. personal growth trajectories
- **Static vs. adaptive**: dashboards coupled to [Adaptive Learning](../principles/adaptive-learning.md) recommendations close the loop from data to action

### Target Learners
- Self-regulated learners benefit most; learners with weak metacognitive skills may misinterpret or ignore dashboard data [~M] — pairing with [Self-Regulated Learning](../theories/self-regulated-learning.md) instruction improves outcomes
- At-risk learners in large enrollment courses, when instructors use analytics for early outreach [~M]
- Lower-performing learners are harmed by ranking-style displays [~M]

### Target Learning Goals
- Metacognitive monitoring: accurate self-assessment of progress and gaps
- Study behavior regulation: planning, time allocation, help-seeking
- Not well suited to conceptual learning goals directly — dashboards support the *regulation* of learning, not the learning itself

### Instructions
1. Define which metrics are validly linked to learning in your course (e.g., practice quiz performance, not logins).
2. Choose self-referenced displays (progress toward goals, change over time) over normative rankings.
3. Pair each visualization with an actionable prompt or recommended next step ([Assessment](../elements/assessment.md) results linked to targeted resources).
4. Teach learners how to interpret and act on the data — a brief orientation or [Check-in](../elements/check-in.md) routine.
5. Review instructor-facing views on a schedule and intervene early with struggling learners; the dashboard triggers, the human conversation delivers, the intervention.

## Related Strategies
- [Assessment for Learning](../principles/assessment-for-learning.md) — dashboards are a delivery mechanism for formative feedback data
- Early-alert analytics — instructor-facing variant focused on retention

## Examples
- **[Open University, UK — "Student Progress Dashboard"](https://www.open.ac.uk)** — self-referenced progress indicators shown to distance learners; evaluated studies found effects depended on students' prior attainment.
- **[Khan Academy](https://www.khanacademy.org)** — learner dashboard showing skill mastery levels, recommended next activities, and activity history; couples display directly to actionable recommendations.
- **[Canvas / Blackboard LMS analytics](https://www.instructure.com/canvas)** — instructor-facing course analytics for at-risk identification; widely deployed but frequently showing activity metrics of questionable validity.
- **LAK research prototypes (e.g., ViTAL, OnTrack)** — research dashboards studied for effects on self-regulated learning behavior.

## Key Sources
- Verbert, K., Duval, E., Klerkx, J., Govaerts, S., & Santos, J. L. (2013). Learning analytics dashboard applications. *IEEE Transactions on Learning Technologies, 6*(3), 150–158. [doi:10.1177/0002764213479363](https://doi.org/10.1177/0002764213479363)
- Bodily, R., & Verbert, K. (2017). Review of research on student-facing learning analytics dashboards and educational recommender systems. *IEEE Transactions on Learning Technologies, 10*(4), 405–418. [doi:10.1109/tlt.2017.2740172](https://doi.org/10.1109/tlt.2017.2740172)
- Jivet, I., Scheffel, M., Drachsler, H., & Specht, M. (2018). License to evaluate: Preparing learners for educational recommender systems and learning analytics dashboards. *Proceedings of the 8th International Conference on Learning Analytics and Knowledge (LAK '18)*, 41–50. [doi:10.1145/3170431.3174343](https://doi.org/10.1145/3170431.3174343)
- Corrin, L., & de Barba, P. (2015). How do students interpret feedback delivered via dashboards? *Proceedings of the 5th International Conference on Learning Analytics and Knowledge (LAK '15)*, 430–431. [doi:10.1145/2723576.2723662](https://doi.org/10.1145/2723576.2723662)
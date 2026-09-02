---
type: strategy
id: jigsaw-cooperative-learning
title: Jigsaw Cooperative Learning
description: An interdependent group structure in which each member masters a unique piece of material and teaches it to peers, making every learner both student and teacher.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Jigsaw Cooperative Learning

> **Strategy** · [All strategies](index.md)

## Description
Jigsaw divides a body of material into segments and assigns each segment to one member of a small "home" group. Learners first meet in temporary "expert" groups with peers from other home groups who share the same segment, then return to teach their segment to their home group. Because no one else in the home group has that piece, each learner becomes the sole source of critical information, creating genuine positive interdependence [Cooperative learning](../patterns/cooperative-learning.md).

## Design Implications

Jigsaw converts the accountability problem of group work into a structural feature: each member's contribution is indispensable, which suppresses free-riding and raises individual engagement [Active learning improves exam performance.](../claims/active-learning-improves-exam-performance.md) [+S]. The teaching role is the engine of the method — preparing to explain, and explaining, forces elaboration and organization of the material beyond what passive reading produces. The expert-group phase provides a rehearsal space that lowers the risk of teaching peers inaccurate content.

### Context
#### Requirements
- Material that decomposes naturally into interdependent segments of roughly equal difficulty
- Sufficient time for two phases (expert meeting, then home-group teaching) — typically a full class period or more
- Explicit norms for the teaching exchange: each member must check that others understood before moving on
- Instructor circulation to monitor accuracy and intervene when explanations go wrong

#### Constraints
- Weak or inaccurate peer teaching propagates errors; without instructor monitoring, learners may leave with misconceptions [-M]
- Unequal segment difficulty or unequal learner ability undermines the interdependence — stronger learners dominate, weaker learners disengage [~M]
- Poor fit for material that is tightly sequential or hierarchical, where segments cannot be understood in isolation
- Requires social confidence; anxious or low-status learners may struggle in the teaching role without scaffolding [~W]
- Time-intensive relative to direct instruction; the payoff depends on the material warranting deep processing [-M]

#### Implementation Variability
- **Jigsaw II** (Slavin): all learners first read common base material, then specialize in a subtopic — reduces the risk of missing the whole-picture frame
- **Reverse jigsaw**: expert groups reconvene after teaching to compare how their home groups understood the segment
- **Jigsaw in discussion formats**: segments are stakeholder perspectives rather than content units, feeding into [debate](../patterns/debate.md) or [case-based learning](../patterns/case-based-learning.md)

### Target Learners
- Adolescents and adults with sufficient reading fluency to master a segment independently
- Mixed-ability groups: the structure gives lower-status learners a legitimate expert role, which can improve participation and belonging [Belonging interventions improve outcomes.](../claims/belonging-interventions-improve-outcomes.md) [+M]
- Less suitable for complete novices who cannot yet self-explain a segment without support [~M]

### Target Learning Goals
- Comprehension and retention of segmented factual/conceptual material
- Oral explanation and communication skills
- Interdependence and perspective-taking; originally designed to reduce intergroup hostility in desegregated classrooms

### Instructions
1. Segment the material and assign one segment per group member, ensuring balanced difficulty.
2. Form expert groups of learners sharing the same segment; provide guiding questions and time to master the material ([Articulation](../elements/articulation.md) — rehearse the explanation aloud).
3. Return learners to home groups; each member teaches their segment while others question and take notes ([Assigned positions](../elements/assigned-positions.md) — rotate roles such as timekeeper and clarifier to enforce participation).
4. Assess individual mastery of the *whole* material so that listening is as consequential as teaching.
5. Debrief on both content gaps and group process.

## Related Strategies
- [Think-Pair-Share](../patterns/think-pair-share.md) — a lighter-weight interdependence structure for shorter exchanges
- [Reciprocal Teaching](../elements/reciprocal-teaching.md) — shares the learner-as-explainer role but rotates fixed comprehension strategies rather than content segments
- [Peer Instruction](peer-instruction.md) — similar peer-teaching mechanism, driven by conceptual questions rather than segmented content

## Examples
- **The Jigsaw Classroom** ([jigsaw.org](https://www.jigsaw.org)) — Elliot Aronson's original implementation in Austin, TX elementary classrooms, where each child owned one biography segment of a history unit.
- **Medical education case-based curricula** — jigsaw variants used in problem-based medical programs, with students specializing in diagnostic, pharmacological, or psychosocial aspects of a case before teaching their team.
- **Flipped-classroom jigsaw** — learners study their segment as pre-class homework, reserving class time entirely for expert and home-group teaching.

## Key Sources
- Aronson, E., Blaney, N., Stephan, C., Sikes, J., & Snapp, M. (1978). *The jigsaw classroom*. Sage.
- Slavin, R. E. (1995). *Cooperative learning: Theory, research, and practice* (2nd ed.). Allyn & Bacon.
- Souvignier, E., & Kronenberger, J. (2007). Cooperative learning with third and fourth graders: Effects of jigsaw on achievement and motivation. *Learning and Instruction, 17*(4), 423–439.
- Johnson, D. W., & Johnson, R. T. (2009). An educational psychology success story: Social interdependence theory and cooperative learning. *Educational Researcher, 38*(5), 365–379. [doi:10.3102/0013189X09339057](https://doi.org/10.3102/0013189X09339057)
---
type: strategy
id: desmos-classroom-activities
title: Desmos Classroom Activities
description: A strategy using Desmos Classroom's interactive, teacher-paced digital activities to make mathematical thinking visible, collect real-time student responses, and structure whole-class discussion.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Desmos Classroom Activities

> **Strategy** · [All strategies](index.md)

## Description
Desmos Classroom Activities ([teacher.desmos.com](https://teacher.desmos.com)) are browser-based mathematics lessons built from interactive screens — graphing tasks, card sorts, marbleslides, and response prompts — that students work through while the teacher orchestrates pacing and monitors anonymized student work on a dashboard. The teacher can pause the class, showcase individual student responses, and sequence discussion around the work students actually produce, making the activity a vehicle for [formative assessment](../patterns/formative-assessment.md) rather than self-paced drill.

## Design Implications

The strategy's core mechanism is making student thinking collectively visible: because every response streams to the teacher dashboard, instruction can respond to actual student conceptions rather than anticipated ones, which is the defining move of responsive, [active learning](../principles/active-learning.md) [active-learning-improves-exam-performance](../claims/active-learning-improves-exam-performance.md) [+S]. Interactive graphing manipulatives offload the mechanics of plotting and computation, letting working memory attend to structure and relationships [chunking-reduces-working-memory-load](../claims/chunking-reduces-working-memory-load.md) [+M]. The teacher's pause-and-discuss moves are essential: activities left to run as unguided exploration produce weaker learning than the same screens embedded in teacher-led discussion and [practice](../elements/practice.md) cycles.

### Context
#### Requirements
- A device per student (laptop, tablet, or phone) and reliable internet access
- A teacher dashboard session with the activity pre-loaded and pacing planned in advance
- Deliberate facilitation: pausing at designed moments, anonymizing and sequencing student work for discussion, and following screens with verbal consolidation
- A short debrief that connects the activity's informal reasoning to formal mathematical notation

#### Constraints
- Unguided screen-by-screen exploration without teacher orchestration yields shallow engagement; the dashboard is a formative-assessment tool, not a self-teaching system [-M]
- Card sorts and multiple-choice screens can be completed by pattern-matching or guessing without conceptual understanding if responses are never discussed [-M]
- Device and connectivity requirements create access barriers; activities need low-tech fallbacks for equity
- Overuse of gamified screens (e.g., marbleslides) can shift attention toward puzzle-solving satisfaction rather than the underlying mathematics [~W]

#### Implementation Variability
- **Full lesson replacement**: a complete Desmos activity (e.g., "Polygraph: Parabolas") as the core of a class period, with teacher-paced discussion between screens
- **Warm-up or exit ticket**: a 2–3 screen activity used to surface prior conceptions or check retention [spaced-repetition-improves-retention](../claims/spaced-repetition-improves-retention.md) [+S]
- **Card sorts for discrimination**: students sort examples and non-examples, then the teacher displays mismatch patterns to drive discussion [multiple-contrasting-cases-support-abstraction](../claims/multiple-contrasting-cases-support-abstraction.md) [+M]
- **Asynchronous/flipped use**: screens assigned before class to gather data that shapes the in-person lesson, as in a [flipped classroom](../patterns/flipped-classroom.md)

### Target Learners
- Middle and secondary mathematics students, where dynamic graphing most directly supports conceptual development
- Reluctant participants: anonymized dashboard display lowers the social cost of contributing, broadening participation in [class discussion](../elements/class-discussion.md) [+W]
- Less effective for learners who already have strong procedural fluency, for whom the scaffolding embedded in screens adds little [expertise-reversal-effect](../claims/expertise-reversal-effect.md) [~M]

### Target Learning Goals
- Conceptual understanding of functions, graphs, and transformations
- Mathematical discourse: justifying and critiquing reasoning with peers
- Formative assessment data on student conceptions for the teacher

### Instructions
1. Select or author an activity aligned to the lesson goal; preview every screen and plan which responses will anchor discussion.
2. Launch with a low-floor opening screen that activates prior knowledge [activation](../elements/activation.md).
3. Monitor the dashboard while students work; identify two or three contrasting responses to sequence for discussion.
4. Pause the class at designed moments and display anonymized student work, asking students to compare and justify approaches [self-explanation-improves-conceptual-understanding](../claims/self-explanation-improves-conceptual-understanding.md) [+S].
5. Consolidate: connect the activity's informal language to formal notation, and follow with independent [practice](../elements/practice.md) or an [assessment](../elements/assessment.md) screen to check transfer.

## Related Strategies
- [Think-Pair-Share](../patterns/think-pair-share.md) — the pause-and-discuss moments within an activity enact the same structure
- [Peer Instruction](peer-instruction.md) — dashboard-revealed response distributions serve the same function as clicker votes
- [Worked Examples](worked-examples.md) — some Desmos screens present annotated solutions before student attempts

## Examples
- **[Polygraph: Parabolas](https://teacher.desmos.com/polygraph)** — a paired guessing game where students ask questions to identify a graph, forcing precise vocabulary use; the teacher dashboard reveals which vocabulary gaps block progress.
- **[Marbleslides](https://teacher.desmos.com/marbleslides)** — students transform function equations to guide marbles through stars, receiving immediate visual feedback at the task level [feedback-most-effective-at-task-and-process-levels](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S].
- **Card sorts** (e.g., "Card Sort: Linear Functions") — students match representations; the teacher displays class mismatch data to target re-teaching.

## Key Sources
- Roschelle, J., Penuel, W. R., & Shechtman, N. (2006). Co-design and the implementation of wireless response technology. *Journal of Science Education and Technology, 15*(5–6), 501–512.
- Drijvers, P., Kieran, C., & Mariotti, M. A. (2010). Integrating technology into mathematics education: Theoretical perspectives. In C. Hoyles & J.-B. Lagrange (Eds.), *Mathematics education and technology-rethinking the terrain* (pp. 89–132). Springer.
- Hattie, J., & Timperley, H. (2007). The power of feedback. *Review of Educational Research, 77*(1), 81–112. [doi:10.3102/003465430298487](https://doi.org/10.3102/003465430298487)
- Freeman, S., et al. (2014). Active learning increases student performance in science, engineering, and mathematics. *PNAS, 111*(23), 8410–8415. [doi:10.1073/pnas.1319030111](https://doi.org/10.1073/pnas.1319030111)

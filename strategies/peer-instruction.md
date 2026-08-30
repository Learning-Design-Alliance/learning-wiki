---
type: strategy
title: Peer Instruction
description: Students answer a conceptually challenging question individually, then discuss their reasoning with peers before revoting, with the instructor facilitating a whole-class debrief.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Peer Instruction

## Description
Peer Instruction, developed by Eric Mazur at Harvard, structures class time around a repeating cycle: the instructor poses a conceptually demanding multiple-choice or true/false question ([ConcepTest](../elements/conceptest.md)); students commit to an individual answer, often via clicker or show of hands; they then attempt to convince a neighbor with a different answer; finally they revote and the instructor debriefs based on the vote distribution. The strategy converts lecture time into episodes of [active learning](../principles/active-learning.md) driven by cognitive conflict and peer explanation.

## Design Implications

Peer Instruction operationalizes the finding that interactive engagement outperforms passive lecture on conceptual measures [Interactive engagement methods outperform traditional lecture on conceptual understanding.](../claims/active-learning-improves-exam-performance.md) [+S]. Its engine is the discrepancy between a student's initial answer and a peer's reasoning: articulating an explanation and confronting contradiction forces retrieval and elaboration that listening alone does not produce. Questions must target conceptual understanding rather than calculation — students should be able to argue about them without paper-and-pencil work.

### Context
#### Requirements
- Conceptually focused questions with plausible distractors that expose common misconceptions
- A mechanism for individual commitment before discussion (clickers, cards, or online polling) to prevent anchoring on a confident peer's answer
- Sufficient class time for the full cycle (typically 5–10 minutes per question)
- Instructor willingness to adapt the debrief to the actual vote distribution rather than a planned script

#### Constraints
- Fails when questions are procedural or rote — there is nothing substantive to argue about [~M]
- Students with low confidence may defer to peers without genuine evaluation, propagating misconceptions when few students hold the correct answer [~M]
- Requires a critical mass of students who have done preparatory work; in an unflipped course, students meet the question cold and discussion quality drops
- Large vote majorities (>90% correct) make discussion pointless; small majorities (<35%) may leave no student able to articulate the correct reasoning

#### Implementation Variability
- [Flipped Classroom](../patterns/flipped-classroom.md) variant: content delivery moves to pre-class reading with [Just-in-Time Teaching](../strategies/just-in-time-teaching.md) quizzes, freeing class time entirely for Peer Instruction cycles
- Two-stage or two-round exams: the same discussion mechanism applied to assessment, where students first answer individually then discuss and re-answer
- Online adaptation: asynchronous discussion boards or breakout rooms in video conferencing replace shoulder-to-neighbor talk, at some cost to immediacy

### Target Learners
- Undergraduate and advanced secondary students in conceptually dense domains (physics, chemistry, economics, biology) [Interactive engagement methods outperform traditional lecture on conceptual understanding.](../claims/active-learning-improves-exam-performance.md) [+S]
- Students holding entrenched misconceptions, which surface and become arguable through the voting cycle
- Less effective for complete novices who lack enough prior knowledge to generate or evaluate any explanation — pair with [Activation](../principles/activation.md) of prerequisite knowledge first

### Target Learning Goals
- Conceptual understanding and misconception repair, rather than procedural fluency
- Argumentation and explanation skills: justifying reasoning and critiquing others'
- Metacognitive awareness of one's own understanding, exposed by the gap between confidence and correctness

### Instructions
1. Assign preparatory material and optionally a pre-class quiz so students arrive with baseline exposure ([Flipped Classroom](../patterns/flipped-classroom.md)).
2. Pose a [ConcepTest](../elements/conceptest.md) targeting a known misconception; students vote individually without discussion.
3. Display the vote distribution. If answers are split (roughly 35–90% correct), have students discuss with a neighbor holding a *different* answer.
4. Students revote. If the majority now answers correctly, briefly confirm and consolidate; if not, reteach or run a second round ([Class Discussion](../elements/class-discussion.md)).
5. Repeat with 2–4 questions per class session, keeping each cycle under ten minutes.

## Related Strategies
- [Think-Pair-Share](../patterns/think-pair-share.md) — the same individual-then-discuss structure without the voting and revote mechanism
- [Just-in-Time Teaching](../strategies/just-in-time-teaching.md) — supplies the pre-class preparation and question targeting that Peer Instruction depends on
- [Clicker Questions](../strategies/clicker-questions.md) — the polling infrastructure that enforces individual commitment before discussion

## Examples
- **[Peer Instruction Network / Mazur Group resources](https://blog.peerinstruction.net)** — Eric Mazur's original implementation in Harvard Physics 1, replacing most lecture with ConcepTests; documented in *Peer Instruction: A User's Manual* (1997).
- **[Carl Wieman Science Education Initiative](https://www.cwsei.ubc.ca)** — Clicker resource guides and question banks from UBC and CU Boulder, where large-enrollment science courses adopted Peer Instruction at scale.
- **[Perusall](https://www.perusall.com)** — extends the peer-discussion mechanism to pre-class reading, with students annotating and responding to each other before the vote cycle begins.

## Key Sources
- Mazur, E. (1997). *Peer instruction: A user's manual*. Prentice Hall.
- Crouch, C. H., & Mazur, E. (2001). Peer instruction: Ten years of experience and results. *American Journal of Physics, 69*(9), 970–977. [doi:10.1119/1.1374249](https://doi.org/10.1119/1.1374249)
- Freeman, S., Eddy, S. L., McDonough, M., Smith, M. K., Okoroafor, N., Jordt, H., & Wenderoth, M. P. (2014). Active learning increases student performance in science, engineering, and mathematics. *PNAS, 111*(23), 8410–8415. [doi:10.1073/pnas.1319030111](https://doi.org/10.1073/pnas.1319030111)
- Smith, M. K., Wood, W. B., Adams, W. K., Wieman, C., Knight, J. K., Guild, N., & Su, T. T. (2009). Why peer discussion improves student performance on in-class concept questions. *Science, 323*(5910), 122–124. [doi:10.1126/science.1165919](https://doi.org/10.1126/science.1165919)
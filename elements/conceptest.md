---
type: element
title: ConcepTest
description: A multiple-choice question targeting a single conceptual difficulty, used with student voting and peer discussion to expose and confront misconceptions.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# ConcepTest

> **Element** · [All elements](index.md)

## Description
A ConcepTest is a short multiple-choice (or short-answer) question focused on a single concept — typically one where learners hold predictable misconceptions — posed to the whole class. Learners commit to an answer individually (often via clicker or show of hands), discuss with neighbors, revote, and then the instructor resolves the result. Developed by Eric Mazur in Harvard's physics course, it is the question engine of [Peer Instruction](../patterns/peer-instruction.md).

## Design Implications

ConcepTests convert lecture time into [active learning](../principles/active-learning.md) by forcing every student to commit to an answer before hearing an explanation, which surfaces misconceptions that passive listening conceals [Active learning improves exam performance relative to lecture alone.](../claims/active-learning-improves-exam-performance.md) [+S]. The individual vote creates cognitive engagement; the peer discussion creates [cognitive disequilibrium](../principles/cognitive-disequilibrium.md) when answers diverge, motivating conceptual change [Cognitive disequilibrium motivates conceptual change.](../claims/cognitive-disequilibrium-motivates-conceptual-change.md) [+M]. Peer discussion alone improves performance even when no student initially knows the correct answer, because reasoning aloud forces retrieval and elaboration [Smith et al. found peer discussion improves understanding even when no one in the group initially answers correctly.](https://doi.org/10.1126/science.1198704) [+S].

### Context
#### Requirements
- Questions targeting a *single* conceptual difficulty, with distractors that map onto known misconceptions — not multi-step calculation
- An individual commitment step (vote) before discussion; discussion without prior commitment produces conformity rather than reasoning
- Instructor willingness to adapt in real time: high correct rates (~90%+) mean move on; low rates (<35%) mean re-teach; middle rates mean discussion will be productive
- A response mechanism visible to the instructor (clickers, cards, poll) so results drive the next move ([Assessment](assessment.md) as feedback, not grading)

#### Constraints
- Poorly designed questions — recall items, ambiguous wording, or distractors that don't correspond to real misconceptions — produce discussion without conceptual payoff [Question design quality determines the value of the resulting discussion.](https://doi.org/10.1119/1.1807315) [~M]
- Rewards conceptual understanding at the expense of procedural fluency; ConcepTests alone do not build computational skill and must be paired with problem-solving practice
- Discussion can propagate wrong answers when the correct rate is very low and no student in a group has a defensible reason — instructor follow-up explanation is still required
- Grading votes for accuracy suppresses honest commitment and destroys the diagnostic function; stakes must be minimal

### Target Learners
- Large-enrollment introductory courses where individual questioning of every student is impossible
- Learners with entrenched misconceptions in concept-dense domains (physics, chemistry, biology, economics) — the distractor structure is what makes misconceptions visible
- Less effective for advanced learners who already share the expert conception, since discussion adds little beyond confirmation

### Target Learning Goals
- Conceptual understanding and misconception repair, rather than procedural skill
- Formative diagnosis: the vote distribution tells the instructor what the class actually believes ([Assessment for Learning](../principles/assessment-for-learning.md))
- Argumentation and justification: articulating reasoning to a peer strengthens it [Active learning improves exam performance relative to lecture alone.](../claims/active-learning-improves-exam-performance.md) [+S]

### Affordances
- [Active Learning](../principles/active-learning.md) — ConcepTests are a low-overhead way to make every student in a large lecture respond, commit, and reason, rather than a handful of volunteers
- [Cognitive Disequilibrium](../principles/cognitive-disequilibrium.md) — the revote after peer discussion, when answers change, is a designed moment of surprise that motivates re-examination of prior beliefs
- [Assessment for Learning](../principles/assessment-for-learning.md) — the anonymous vote distribution is real-time formative data that lets the instructor decide whether to move on, discuss, or re-teach
- [Cognitive Load Management](../principles/cognitive-load-management.md) — restricting each question to one concept keeps the discussion focused on a single schema rather than a multi-step problem that overloads working memory

## Related Elements
- [Class Discussion](class-discussion.md) — the peer discussion phase is a tightly structured, whole-class-simultaneous variant
- [Assessment](assessment.md) — ConcepTests function as ungraded formative assessment embedded in instruction
- [Activation](activation.md) — the initial vote activates prior conceptions, including misconceptions, before instruction addresses them

## Patterns That Use This Element
- [Peer Instruction](../patterns/peer-instruction.md) — the defining pattern: vote → discuss → revote → explain
- [Direct Instruction](../patterns/direct-instruction.md) — ConcepTests can serve as the checks-for-understanding between explanation segments, though their peer-discussion phase departs from the pattern's pure form

## Examples

**[Peer Instruction (Mazur, Harvard Physics)](https://www.per-central.org)** — The original implementation: ConcepTests on mechanics and E&M concepts, with clicker voting and neighbor discussion replacing roughly a third of lecture time.

**[Peer Instruction for Computer Science](https://www.peerinstruction4cs.org)** — Daniel Zingaro and Cynthia Taylor's collection of ConcepTests for CS1/CS2, demonstrating the format transfers beyond physics.

**[Project Galileo / ConcepTest collections](https://galileo.seas.harvard.edu)** — Harvard's curated question banks across physics, chemistry, and biology, with documented misconception-based distractors.

## Key Sources
- Mazur, E. (1997). *Peer instruction: A user's manual.* Prentice Hall.
- Crouch, C. H., & Mazur, E. (2001). Peer instruction: Ten years of experience and results. *American Journal of Physics, 69*(9), 970–977. [doi:10.1119/1.1374249](https://doi.org/10.1119/1.1374249)
- Beatty, I. D., Gerace, W. J., Leonard, W. J., & Dufresne, R. J. (2006). Designing effective questions for classroom response systems. *American Journal of Physics, 74*(1), 31–39. [doi:10.1119/1.2121753](https://doi.org/10.1119/1.2121753)
- Smith, M. K., Wood, W. B., Adams, W. K., Wieman, C., Knight, J. K., Guild, N., & Su, T. T. (2009). Why peer discussion improves student performance on in-class concept questions. *Science, 323*(5910), 122–124. [doi:10.1126/science.1165919](https://doi.org/10.1126/science.1165919)
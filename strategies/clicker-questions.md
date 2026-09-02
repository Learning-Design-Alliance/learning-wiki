---
type: strategy
id: clicker-questions
title: Clicker Questions
description: Structured in-class questions answered by all students via response systems (clickers or equivalents), typically followed by peer discussion and revoting.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Clicker Questions

> **Strategy** · [All strategies](index.md)

## Description
Clicker questions are multiple-choice or conceptual questions posed to an entire class, with every student answering simultaneously through a personal response system (dedicated clickers, phone apps, or flashcards). The canonical cycle — question, individual vote, peer discussion, revote, instructor explanation — is [Peer Instruction](../patterns/peer-instruction.md), developed by Eric Mazur at Harvard. The simultaneous public commitment of an answer makes every student's thinking active and visible, rather than leaving participation to volunteers.

## Design Implications

Clicker questions are a core implementation of [Active Learning](../principles/active-learning.md); meta-analytic evidence shows active-learning formats improve exam performance and reduce failure rates relative to lecture alone [Active learning improves exam performance.](../claims/active-learning-improves-exam-performance.md) [+S]. Their power comes less from the technology than from the sequence: committing to an answer individually before discussion prevents social loafing, and the vote distribution gives the instructor real-time formative data to decide whether to reteach or move on [Assessment for learning improves achievement.](../claims/assessment-for-learning-improves-achievement.md) [+M]. Questions should target conceptual understanding and common misconceptions rather than factual recall, so that peer discussion involves genuine argumentation [Argumentation improves reasoning.](../claims/argumentation-improves-reasoning.md) [+M].

### Context
#### Requirements
- Conceptually demanding questions with plausible distractors drawn from known misconceptions
- An individual-answer phase before any discussion, so students commit privately
- Instructor willingness to adjust the lesson in response to vote results
- Low- or no-stakes grading policy so wrong answers are safe

#### Constraints
- Recall-level questions produce no productive discussion and add overhead without benefit [-M]
- If revoting is allowed without genuine discussion, students copy neighbors and the peer-instruction benefit collapses [~S]
- Overuse (more than roughly 3–5 per hour) turns the technique into quiz fatigue and erodes engagement [-W]
- Technology failures and setup friction can consume class time; low-tech alternatives (A/B cards) preserve most of the benefit [~W]

#### Implementation Variability
- **Peer Instruction (Mazur cycle):** vote → discuss with a neighbor → revote → instructor debrief
- **Formative check:** vote → instructor explains immediately, no peer phase
- **Graded response:** answers count modestly toward grades (participation or correctness), trading some safety for accountability [~M]
- **Low-tech equivalent:** colored cards or raised fingers achieve the same simultaneous commitment without hardware

### Target Learners
- Large-enrollment classes where individual questioning of every student is impossible
- Students holding entrenched misconceptions, which the vote exposes and peer discussion confronts [~S]
- Less effective for advanced learners who already agree on the answer — discussion becomes trivial [~M]

### Target Learning Goals
- Conceptual understanding and misconception repair in domains like physics, chemistry, biology, and statistics
- Formative assessment: giving instructors and students real-time evidence of understanding [Assessment for learning improves achievement.](../claims/assessment-for-learning-improves-achievement.md) [+M]
- Argumentation and explanation skills through structured peer discussion

### Instructions
1. Pose a conceptual multiple-choice question with distractors based on documented misconceptions; display a countdown for individual voting.
2. Show the vote distribution without revealing the correct answer.
3. Have students convince a neighbor, using [Class Discussion](../elements/class-discussion.md) in pairs — require both students to explain their reasoning.
4. Run the revote and compare distributions; large shifts indicate productive peer learning.
5. Debrief: have a student explain the reasoning, then confirm or correct with a brief instructor explanation.
6. Adjust subsequent instruction based on the final distribution — high error rates signal the need for reteaching rather than moving on.

## Related Strategies
- [Think-Pair-Share](../patterns/think-pair-share.md) — the same discuss-then-commit structure without the response technology
- [Two-Stage Exams](two-stage-exams.md) — extends the individual-then-group logic to assessment itself
- [Retrieval Practice](retrieval-practice.md) — each clicker vote is a low-stakes retrieval event

## Examples
- **[Peer Instruction](https://www.peerinstruction.net)** — Eric Mazur's method, originated in Harvard physics (ConcepTests), now used across STEM disciplines; question banks are published through the [Peer Instruction Network](https://blog.peerinstruction.net).
- **[iClicker](https://www.iclicker.com)** and **[Poll Everywhere](https://www.polleverywhere.com)** — commercial response systems supporting the vote–discuss–revote cycle in large lectures.
- **Carl Wieman's Science Education Initiative** — documented large-scale adoption of clicker questions in UBC and University of Colorado physics courses, with published question banks.

## Key Sources
- Freeman, S., Eddy, S. L., McDonough, M., Smith, M. K., Okoroafor, N., Jordt, H., & Wenderoth, M. P. (2014). Active learning increases student performance in science, engineering, and mathematics. *Proceedings of the National Academy of Sciences, 111*(23), 8410–8415. [doi:10.1073/pnas.1319030111](https://doi.org/10.1073/pnas.1319030111)
- Mazur, E. (1997). *Peer instruction: A user's manual.* Prentice Hall.
- Smith, M. K., Wood, W. B., Adams, W. K., Wieman, C., Knight, J. K., Guild, N., & Su, T. T. (2009). Why peer discussion improves student performance on in-class concept questions. *Science, 323*(5910), 122–124. [doi:10.1126/science.1165919](https://doi.org/10.1126/science.1165919)
- Caldwell, J. E. (2007). Clickers in the large classroom: Current research and best-practice tips. *CBE—Life Sciences Education, 6*(1), 9–20. [doi:10.1187/cbe.06-12-0205](https://doi.org/10.1187/cbe.06-12-0205)
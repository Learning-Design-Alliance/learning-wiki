---
type: strategy
title: Response Devices
description: Response devices allow learners to anonymously share answers with the whole class, enabling whole-group participation and rapid formative assessment.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Response Devices

## Description
Response devices allow learners to anonymously share answers with the whole class. They range from low-tech whiteboards and colored cards to commercial clicker systems and web-based polling tools (e.g., [Poll Everywhere](https://www.polleverywhere.com), [Socrative](https://www.socrative.com), [Kahoot!](https://kahoot.com), [Mentimeter](https://www.mentimeter.com)). The typical cycle: the instructor poses a question, learners commit to an answer individually, responses are aggregated and displayed, and the distribution drives discussion or instructional adjustment.

## Design Implications

Response devices convert passive audiences into active respondents and give instructors real-time formative data on whole-class understanding [Active learning improves exam performance relative to lecture alone.](../claims/active-learning-improves-exam-performance.md) [+S]. Their learning benefit depends less on the device than on the question design and what happens after the vote: displaying a response distribution and requiring peer discussion or instructor explanation produces substantially deeper learning than polling alone [Feedback is most effective at the task and process levels.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S]. Anonymity lowers the social cost of wrong answers, surfacing misconceptions that hand-raising conceals.

### Context
#### Requirements
- A reliable response mechanism (clickers, mobile app, or whiteboards) accessible to every learner
- Well-designed questions targeting known misconceptions, not just factual recall ([Questioning](questioning.md))
- Time for individual commitment *before* any group response — committing first is what drives engagement
- A follow-up routine: display the distribution, discuss, and re-vote or explain ([Class Discussion](../elements/class-discussion.md), [Provide Feedback](../elements/provide-feedback.md))

#### Constraints
- Devices used for attendance, trivia, or low-level recall add logistics without learning benefit [~M]
- If the instructor moves on without addressing a wrong-answer distribution, learners' misconceptions are confirmed rather than corrected [-M]
- Technical failures and device-access inequities can exclude learners; low-tech fallbacks (whiteboards, cards) mitigate this
- Perceived as superficial by learners if polling is not visibly connected to subsequent instruction

#### Implementation Variability
- **Peer instruction**: individual vote → peer discussion → re-vote → instructor explanation; the strongest-evidenced variant [~S]
- **Low-tech**: mini whiteboards or A/B/C/D cards achieve the same commit-and-reveal cycle with no infrastructure
- **Gamified quizzing**: Kahoot-style competition increases engagement and motivation, but speed pressure can favor fast retrieval over reasoning [~W]
- **Open-response polling**: word clouds and free-text collection for brainstorming or prior-knowledge checks

### Target Learners
- Large-enrollment classes where individual learners rarely speak; anonymity enables participation at scale
- Anxious or low-confidence learners who avoid public error — anonymous response creates a safe space to be wrong
- All age levels, K–12 through professional development; question sophistication, not the device, is the age-dependent variable

### Target Learning Goals
- Formative assessment: diagnosing whole-class misconceptions in real time
- Conceptual understanding: conceptual-confrontation questions that expose and resolve misconceptions
- Engagement and attention: sustained on-task participation during direct instruction
- Self-assessment: learners calibrate their understanding against the class distribution

### Instructions
1. Design a question with plausible distractors based on known misconceptions ([Questioning](questioning.md))
2. Give adequate time for individual work and commitment to an answer ([Practice](../elements/practice.md))
3. Collect anonymous responses and display the distribution
4. If answers diverge, have learners discuss with neighbors and re-vote ([Peer Discussion](../elements/peer-discussion.md), [Class Discussion](../elements/class-discussion.md))
5. Address the remaining confusion explicitly and adjust instruction ([Provide Feedback](../elements/provide-feedback.md), [Assess Performance](../elements/assess-performance.md))

## Related Strategies
- [Peer Instruction](peer-instruction.md) — the canonical response-device pedagogy: vote, discuss, re-vote
- [Think-Pair-Share](../patterns/think-pair-share.md) — a low-tech variant with the same commit-discuss-share structure
- [Formative Assessment](formative-assessment.md) — response devices are one instrument for enacting it

## Related Elements
- [Practice](../elements/practice.md) — each question is a retrieval practice opportunity
- [Provide Feedback](../elements/provide-feedback.md) — the post-vote discussion is where feedback operates
- [Assess Performance](../elements/assess-performance.md) — aggregated responses give whole-class performance data
- [Class Discussion](../elements/class-discussion.md) — the response distribution is a discussion prompt

## Tools
- [Poll Everywhere](https://www.polleverywhere.com) — web/mobile polling with live word clouds and multiple choice
- [Socrative](https://www.socrative.com) — quizzes, space race, and exit tickets with teacher dashboards
- [Kahoot!](https://kahoot.com) — gamified multiple-choice quizzes
- [Mentimeter](https://www.mentimeter.com) — polling, open response, and visualization
- Mini whiteboards — zero-infrastructure anonymous response

## Examples
- A physics instructor uses [Peer Instruction](peer-instruction.md) with clickers: a conceptual question on Newton's third law yields a split vote, students argue with neighbors, and the re-vote shows majority convergence before the instructor resolves the remainder (Mazur's method at Harvard).
- A kindergarten teacher uses mini whiteboards for whole-group math: every child writes an answer, all boards go up simultaneously, and the teacher scans for error patterns before reteaching.
- A large lecture course uses [Socrative](https://www.socrative.com) exit tickets; the instructor reviews the response report before the next session and opens class by addressing the two most common wrong answers.

## Key Sources
- Freeman, S., Eddy, S. L., McDonough, M., Smith, M. K., Okoroafor, N., Jordt, H., & Wenderoth, M. P. (2014). Active learning increases student performance in science, engineering, and mathematics. *PNAS, 111*(23), 8410–8415. [doi:10.1073/pnas.1319030111](https://doi.org/10.1073/pnas.1319030111)
- Caldwell, J. E. (2007). Clickers in the large classroom: Current research and best-practice tips. *CBE—Life Sciences Education, 6*(1), 9–20. [doi:10.1187/cbe.06-12-0205](https://doi.org/10.1187/cbe.06-12-0205)
- Beatty, I. D., Gerace, W. J., Leonard, W. J., & Dufresne, R. J. (2006). Designing effective questions for classroom response system teaching. *American Journal of Physics, 74*(1), 31–39. [doi:10.1119/1.2121753](https://doi.org/10.1119/1.2121753)
- Mazur, E. (1997). *Peer instruction: A user's manual.* Prentice Hall.
- Black, P., & Wiliam, D. (1998). Assessment and classroom learning. *Assessment in Education: Principles, Policy & Practice, 5*(1), 7–74. [doi:10.1080/0969595980050102](https://doi.org/10.1080/0969595980050102)
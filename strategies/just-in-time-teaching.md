---
type: strategy
title: Just In Time Teaching
description: A strategy where learners complete pre-class web assignments whose responses the instructor reviews just before class, using them to tailor in-class activities to actual student difficulties.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Just In Time Teaching

> **Strategy** · [All strategies](index.md)

## Description
Just-in-Time Teaching (JiTT) is a cycle in which learners complete short, conceptually focused web-based "warm-up" assignments before class, and the instructor reviews those responses immediately beforehand to adapt the upcoming session. Class time is then devoted to addressing the specific misconceptions and gaps revealed, typically through interactive activities rather than lecture. Developed by Novak, Patterson, Gavrin, and Christian at IUPUI for introductory physics, JiTT makes formative assessment the hinge between out-of-class preparation and in-class instruction.

## Design Implications

JiTT operationalizes formative assessment: pre-class responses give the instructor evidence of current understanding in time to act on it, and give learners feedback on their own thinking before misconceptions consolidate [Feedback is most effective when it targets the task and the learner's processes.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S]. The warm-up questions must target known conceptual difficulties — not reading comprehension — so that responses expose reasoning rather than recall. Because class time is restructured around student responses, JiTT shifts contact hours toward interactive methods, which independently improves exam performance [Active learning improves exam performance relative to lecture.](../claims/active-learning-improves-exam-performance.md) [+S].

### Context
#### Requirements
- Short, low-stakes pre-class assignments due a few hours before class, with a strict deadline so responses are genuinely "just in time"
- Questions designed to elicit reasoning and misconceptions, often drawn from research on documented student difficulties (e.g., Force Concept Inventory-style items in physics)
- Instructor commitment to actually reading responses and visibly adapting the lesson; learners disengage quickly if warm-ups never influence class
- A classroom structure that supports interactive work on the revealed difficulties

#### Constraints
- Fails when warm-up responses are ignored in class — completion rates and preparation collapse once learners perceive the assignments as disconnected busywork [~S]
- Requires reliable technology and timely instructor turnaround; in very large sections without grading support, the feedback loop can break down
- Less effective when learners can copy answers or when questions are answerable by keyword search, which produces plausible but unreflective responses [-M]
- The adaptation burden falls on the instructor mid-cycle; instructors who default to prepared slides regardless of responses forfeit the strategy's core benefit [~M]

#### Implementation Variability
- Warm-up + mini-lecture hybrid: brief targeted lecture segment responding to common errors, then activities
- Peer instruction variant: warm-up results seed clicker questions and peer discussion in class
- Fully flipped variant: JiTT warm-ups replace the video-watching of a standard [Flipped Classroom](../patterns/flipped-classroom.md), with responses rather than content delivery driving class design
- Disciplinary adaptations: code snippets to critique in CS, clinical vignettes in health sciences, data plots to interpret in statistics

### Target Learners
- Undergraduates in large introductory STEM courses, the original and best-documented population [+M]
- Learners who under-prepare for class; the deadline and visible use of responses create accountability for preparation [~M]
- Less suited to learners needing heavy procedural skill-building in class time, since JiTT consumes contact hours for conceptual remediation

### Target Learning Goals
- Conceptual understanding and misconception repair, especially where intuitive beliefs conflict with instruction
- Preparation and engagement: learners arrive having committed to answers they must defend
- Instructor learning goals as well — the response data builds the instructor's model of the class's actual state

### Instructions
1. Write 2–4 conceptual warm-up questions targeting known difficulties with the upcoming topic; keep them short and reasoning-focused.
2. Post the assignment online with a deadline a few hours before class; make it low-stakes but required ([Assessment](../elements/assessment.md) for learning, not of learning).
3. Read responses immediately before class and sort them into common correct ideas, partial understandings, and misconceptions.
4. Open class by anonymously displaying representative student answers and having learners discuss which is best and why ([Class Discussion](../elements/class-discussion.md)).
5. Run in-class activities ([Application of Knowledge](../elements/application-of-knowledge.md), peer instruction, or [Case Studies](../elements/case-studies.md)) built directly on the revealed difficulties.
6. Close the loop: explicitly tell learners how their responses shaped the session, sustaining the preparation norm.

## Related Strategies
- Peer Instruction — a natural in-class companion; warm-up responses seed clicker questions and peer debate
- Flipped Classroom — shares the pre-class/in-class split, but JiTT's distinguishing feature is instructor adaptation to response content rather than fixed pre-class content delivery
- Formative feedback loops — JiTT is essentially a scheduled, whole-class formative assessment cycle

## Examples
- **IUPUI introductory physics (Novak et al.)** — the original implementation: web-based warm-ups due at 6 a.m., with the 9:30 a.m. lecture rebuilt around student answers; materials published in *Just-in-Time Teaching: Blending Active Learning with Web Technology* (1999).
- **Physics education research adaptations** — JiTT warm-ups paired with [Peer Instruction](../patterns/flipped-classroom.md) at institutions such as the U.S. Air Force Academy, showing gains on the Force Concept Inventory beyond lecture-only sections [+M].
- **Large-enrollment biology courses** — warm-up essays on common misconceptions (e.g., natural selection misconceptions) reviewed before class, with misconceptions addressed via small-group argumentation.

## Key Sources
- Novak, G. M., Patterson, E. T., Gavrin, A. D., & Christian, W. (1999). *Just-in-Time Teaching: Blending Active Learning with Web Technology*. Prentice Hall.
- Novak, G. M., Wedekind, C., Patterson, E. T., Gavrin, A., & Christian, W. (1999). Just-in-time teaching: Active learner pedagogy with WWW. *Journal of Excellence in College Teaching, 10*(2), 87–104.
- Freeman, S., Eddy, S. L., McDonough, M., Smith, M. K., Okoroafor, N., Jordt, H., & Wenderoth, M. P. (2014). Active learning increases student performance in science, engineering, and mathematics. *Proceedings of the National Academy of Sciences, 111*(23), 8410–8415. [doi:10.1073/pnas.1319030111](https://doi.org/10.1073/pnas.1319030111)
- Hattie, J., & Timperley, H. (2007). The power of feedback. *Review of Educational Research, 77*(1), 81–112. [doi:10.3102/003465430298487](https://doi.org/10.3102/003465430298487)
- Simkins, S. P., & Maier, M. H. (Eds.). (2010). *Just-in-Time Teaching: Across the Disciplines, Across the Academy*. Stylus Publishing.
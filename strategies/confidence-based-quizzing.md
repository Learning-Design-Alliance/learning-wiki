---
type: strategy
id: confidence-based-quizzing
title: Confidence Based Quizzing
description: Learners answer quiz items and simultaneously rate their confidence, with scoring or feedback adjusted to reward accurate self-assessment as well as correct answers.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Confidence Based Quizzing

> **Strategy** · [All strategies](index.md)

## Description
Confidence Based Quizzing (CBQ) asks learners to answer each quiz item and also indicate how confident they are in that answer (e.g., a 1–3 scale). Scoring schemes such as confidence-weighted marking award more points for correct answers marked high-confidence and penalize high-confidence errors, so learners are assessed on calibration — the match between confidence and accuracy — as well as on content knowledge.

## Design Implications

CBQ converts a routine quiz into a metacognitive monitoring exercise: the confidence rating is a judgment of learning made at the moment of retrieval, and the scoring makes the cost of miscalibration visible. This targets the well-documented gap between feeling of knowing and actual performance, and helps learners decide what to restudy. Because the confidence judgment adds a step to each item, it should be quick (a single click) to avoid displacing retrieval effort from the question itself.

### Context
#### Requirements
- A quiz delivery mechanism that captures a confidence rating per item alongside the answer (LMS quiz plugins, clickers, or paper answer sheets with a confidence column)
- A transparent scoring rule — e.g., correct + high confidence = full marks; correct + low confidence = partial; wrong + high confidence = penalty — so learners understand the incentive
- Feedback that reports both accuracy and calibration, not just a total score
- Enough items per quiz for calibration patterns to be meaningful

#### Constraints
- Confidence ratings add response time and cognitive overhead; on tightly timed or high-load assessments they can interfere with retrieval itself [~M]
- Learners can game the scheme by systematically under-reporting confidence, which trains underconfidence rather than calibration [~M]
- Penalties for high-confidence errors can raise anxiety and discourage risk-taking for anxious learners, shifting attention from the task to the stakes [~M]
- Calibration feedback improves monitoring accuracy but does not automatically improve study behavior; it must be paired with guidance on what to do about identified gaps [~M]

#### Implementation Variability
- **Confidence-weighted scoring** (Gardner-Medford style): points scaled by confidence, with penalties for confident errors — strongest incentive for calibration
- **Confidence as feedback only**: ratings collected but not scored; used to trigger targeted feedback ("You were confident but wrong here — restudy this")
- **Team/peer variant**: groups commit to answers with a confidence level before discussion, surfacing disagreement for productive peer argument
- **Low-stakes retrieval format**: confidence ratings embedded in daily retrieval-practice quizzes rather than graded assessments

### Target Learners
- Learners prone to illusions of competence — those who feel they know material they cannot retrieve — benefit most from explicit calibration feedback [~M]
- Intermediate learners preparing for high-stakes exams, where knowing *what you don't know* guides efficient restudy
- Novices may lack the knowledge base for meaningful confidence judgments; their ratings are often uninformative noise until basic familiarity develops [~W]

### Target Learning Goals
- Metacognitive accuracy: calibrating confidence to actual performance
- Self-regulated study decisions: using calibration data to allocate restudy effort
- Content retention: the underlying retrieval practice still drives learning, with feedback most effective when it addresses the task and process levels [Feedback most effective at task and process levels.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S]

### Instructions
1. Design a short low-stakes quiz of retrieval-practice items on recently taught material.
2. Add a one-click confidence rating (e.g., "sure / fairly sure / guessing") to each item; keep it fast so retrieval remains the main cognitive work.
3. Apply a transparent scoring rule that rewards correct answers more when confidence is warranted and penalizes confident errors.
4. Return item-level feedback showing accuracy *and* calibration, highlighting confident errors as priority restudy targets.
5. Have learners record their miscalibrated items and plan restudy accordingly, closing the loop between monitoring and control.
6. Repeat across sessions and show learners their calibration trend over time.

## Related Strategies
- [Retrieval Practice](retrieval-practice.md) — CBQ is a metacognitive layer on top of quizzing; the retrieval itself is what builds memory
- [Self-Assessment](../elements/self-assessment.md) — confidence ratings are a micro-form of self-assessment done at item level
- [Error Analysis](../principles/error-analysis.md) — confident errors surfaced by CBQ are the highest-value material for error analysis
- [Spaced Repetition](../elements/spaced-repetition.md) — calibration data can drive scheduling of what to review

## Examples
- **Confidence-Based Marking in UK medical exams** — Gardner-Medford and Sparrow's confidence-weighted scoring scheme, used in medical school assessments to reward well-calibrated knowledge and discourage guessing.
- **Peer Instruction with clickers** — Eric Mazur's ConcepTests ask students to commit to an answer (often with confidence) before peer discussion; confident wrong answers predictably shift after discussion ([Peer Instruction](https://mazur.harvard.edu/research/peerinstruction)).
- **Anki-style flashcard self-rating** — learners grade their own recall (again/hard/good/easy), an implicit confidence judgment that drives spaced scheduling ([Anki](https://apps.ankiweb.net)).

## Key Sources
- Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques. *Psychological Science in the Public Interest, 14*(1), 4–58. [doi:10.1177/1529100612453266](https://doi.org/10.1177/1529100612453266)
- Roediger, H. L., & Butler, A. C. (2011). The critical role of retrieval practice in long-term retention. *Trends in Cognitive Sciences, 15*(1), 20–27. [doi:10.1016/j.tics.2010.09.003](https://doi.org/10.1016/j.tics.2010.09.003)
- Gardner-Medford, A. R., & Sparrow, N. R. (2010). Answer confidently: On the metacognitive feedback of confidence-based marking. *Journal of Educational Psychology* (confidence-weighted marking scheme).
- Bjork, R. A., & Bjork, E. L. (2011). Making things hard on yourself, but in a good way: Creating desirable difficulties to enhance learning. In M. A. Gernsbacher et al. (Eds.), *Psychology and the Real World*. Worth Publishers.
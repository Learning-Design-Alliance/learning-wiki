---
type: strategy
id: formative-assessment-cycles
aliases: [formative-assessment]
title: Formative Assessment Cycles
description: Running instruction as a repeating loop — elicit evidence of learning, interpret it, adjust teaching, then re-elicit — so that what happens next is decided by what students actually understood.
status: review
generated:
  by: claude/unspecified
  at: 2026-08-30
sources:
  - id: black-wiliam-1998
    resource: "https://doi.org/10.1080/0969595980050102"
    title: "Black, P., & Wiliam, D. (1998). Assessment and classroom learning. *Assessment in Education: Principles, Policy & Practice, 5*(1), 7–74"
    author: "Black, P., & Wiliam, D"
  - id: wiliam-2011
    resource: "https://doi.org/10.1016/j.stueduc.2011.03.001"
    title: "Wiliam, D. (2011). What is assessment for learning? *Studies in Educational Evaluation, 37*(1), 3–14"
    author: "Wiliam, D"
  - id: hattie-timperley-2007
    resource: "https://doi.org/10.3102/003465430298487"
    title: "Hattie, J., & Timperley, H. (2007). The power of feedback. *Review of Educational Research, 77*(1), 81–112"
    author: "Hattie, J., & Timperley, H"
---

# Formative Assessment Cycles

> **Strategy** · [All strategies](index.md)
> **Evidence** · 9 claims (4 for, 2 mixed, 3 against) · 18 studies (9 quant-synthesis, 6 causal, 2 review, 1 associational), `q2`–`q4` · 9 of 18 report an effect size · 1 claim rests on one study

## Description
A formative assessment cycle is a short instructional loop with four moves: elicit evidence of what students currently understand, interpret that evidence against where they need to get to, adjust the next stretch of teaching in response, and elicit again to check whether the adjustment worked. The cycle can run in ninety seconds, with a show-of-hands question mid-explanation, or across a fortnight, with a diagnostic task driving a re-teaching plan. What makes it a cycle rather than a check is the third move: if the evidence never changes what happens next, the assessment was monitoring, not formative.

## Design Implications

The evidence for assessment for learning is strong in aggregate but heterogeneous in the way that always signals an implementation-dependent effect [Assessment for learning improves achievement](../claims/assessment-for-learning-improves-achievement.md) [+S]. Wiliam's framing explains why: formative assessment is not an instrument but a set of practices, and the classroom gains come from the *responsiveness* — the teacher and the learner both doing something different because of what the evidence showed. Programmes that install the instruments (exit tickets, mini-whiteboards, traffic lights) without changing what follows them produce little.

Two design consequences follow. The eliciting move has to be diagnostic rather than merely performance-revealing: a question that most students get right tells you nothing you can act on, and a question whose wrong answers all look alike tells you nothing about *why* [Eliciting Student Thinking](../elements/eliciting-student-thinking.md). And the adjustment has to be feasible in the time available, which means the cycle's length must match the size of the adjustment it can support — a mid-lesson check can support a re-explanation, not a re-planned unit.

### Context
#### Requirements
- A clear learning target for the cycle, since "interpret the evidence" requires something to interpret it against ([Learning Goals](../elements/learning-goals.md))
- Eliciting tasks designed so that wrong answers are informative — distractors tied to specific misconceptions, or responses that require reasoning ([Eliciting Student Thinking](../elements/eliciting-student-thinking.md))
- Evidence from all students, not the ones who volunteer; a cycle driven by the four raised hands is a cycle driven by a biased sample
- A planned repertoire of adjustments — the re-explanation, the worked example, the extra practice set — prepared in advance, because they cannot be invented mid-lesson
- Willingness to abandon the plan when the evidence says the class is not ready
- Clear, shared learning targets — learners cannot close a gap they cannot see ([Constructive Alignment](../patterns/constructive-alignment.md))
- Low-stakes elicitation tasks that surface *thinking*, not just answers ([Check-In](../elements/check-in.md), [3-2-1 Reflection](../strategies/3-2-1_reflection.md))
- A decision rule: the instructor must know in advance what they will do with each likely result (reteach, regroup, advance)
- Feedback that specifies the gap between current and target performance and gives actionable next steps

#### Constraints
- Cycles that elicit but do not adjust produce no learning gain while consuming instructional time — the most common failure mode by a wide margin [-S]
- Whole-class summary displays (traffic lights, thumbs) reflect confidence, and confidence is a poor proxy for understanding [Fluent Illusions Mislead Self Assessment](../claims/fluent-illusions-mislead-self-assessment.md) [-M]
- Self-reported understanding is unreliable without training in the criteria [Self Assessment Accuracy Is Low Without Training](../claims/self-assessment-accuracy-is-low-without-training.md) [-M]
- Frequent low-stakes checks become high-stakes if results are recorded and graded, at which point students optimize for the display rather than reveal what they do not know [-M]
- Overhead is real: cycles cost instructional minutes, and short cycles run constantly can crowd out the sustained work they were meant to protect [~M]
- Interpreting evidence in real time is a genuine expertise; novice teachers reliably see that students are struggling but not what they are struggling with [~M]
- Feedback that is only evaluative (grades, praise) yields near-zero gains and can reduce performance [Feedback improves learning when it addresses the task, not the self.](../claims/feedback-most-effective-at-task-and-process-levels.md) [-M]
- Frequent low-stakes quizzing without instructional response adds workload and anxiety without benefit [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) [~M]
- Public elicitation can expose struggling learners; anonymous response systems mitigate this
- Over-reliance on self-assessment without training produces inaccurate self-ratings, especially in novices [~M]

#### Implementation Variability
- **Micro-cycle (within a lesson)** — a diagnostic question mid-explanation, with an immediate branch: re-explain, work an example, or move on ([Formative Assessment Routines](formative-assessment-routines.md))
- **Lesson-boundary cycle** — an exit ticket read between lessons, with the next lesson's opening adjusted accordingly ([Exit Ticket](exit-ticket.md))
- **Draft cycle** — the loop runs over a piece of work rather than a concept, with feedback between drafts ([Drafting and Feedback Cycles](drafting-and-feedback-cycles.md))
- **Unit pre-assessment** — a diagnostic before teaching, used to skip what is already secure and pre-empt known misconceptions
- **Student-run cycle** — learners self-assess against criteria and choose their own next task [Self Assessment Improves Self Regulated Learning](../claims/self-assessment-improves-self-regulated-learning.md) [+M]
- **Elicitation format:** exit tickets, hinge-point multiple-choice questions, whiteboards, clickers, think-pair-share
- **Response locus:** teacher-adjusted (reteaching), learner-adjusted (revision, self-regulation), or peer-adjusted (structured peer feedback)
- **Technology-mediated:** adaptive platforms that adjust item difficulty from response data ([Adaptive Learning](../principles/adaptive-learning.md))

### Target Learners
- Whole classes with heterogeneous prior knowledge, where the teacher's model of "where the class is" is otherwise guesswork
- Learners in cumulative subjects — mathematics, languages, programming — where an unnoticed gap compounds across subsequent lessons
- Novices, who cannot yet detect their own misunderstanding and therefore will not raise it [Prior Knowledge Needed For Accurate Self Assessment](../claims/prior-knowledge-needed-for-accurate-self-assessment.md) [~M]
- Learners who have been taught to hide confusion; the cycle only works if not-knowing is safe to display, which is a climate question before it is a technique question
- Learners developing self-regulation, who need external monitoring cues before internalizing them
- Less effective when learners lack the prerequisite knowledge to interpret feedback meaningfully [~M]

### Target Learning Goals
- Accurate mastery of specific content, by catching and repairing gaps before they compound
- Correction of misconceptions, particularly the confident ones that never surface unprompted [High-confidence errors lead to better retention after correction than low-confidence errors.](../claims/high-confidence-errors-improve-retention.md) [+M]
- Self-regulation, when learners are brought inside the loop rather than being its subject
- Retention, since well-designed eliciting tasks are themselves retrieval events [Feedback Enhances Retrieval Practice](../claims/feedback-enhances-retrieval-practice.md) [+M]
- Conceptual understanding: diagnosing and correcting misconceptions mid-instruction
- Skill development: identifying which step of a procedure breaks down
- Self-regulated learning: building learners' capacity to judge their own work against criteria

### Instructions
1. **State the target for this cycle.** One thing students should be able to do by the end of it, specific enough to write a diagnostic question about.
2. **Design the eliciting task to be diagnostic.** Build it so that each wrong answer implicates a particular misunderstanding, and so that guessing right is unlikely ([Formative Assessment](../elements/formative-assessment.md)).
3. **Collect from everyone at once.** Mini-whiteboards, all-student response, or written responses — anything that samples the whole class rather than the volunteers.
4. **Interpret against the target, not the average.** Ask what the wrong answers have in common; the pattern, not the percentage, is what tells you what to do.
5. **Decide and act before moving on.** Choose from a prepared set — re-explain differently, run a worked example, pair students, move on with a note to revisit ([Demonstration](../elements/demonstration.md), [Scaffolding](../elements/scaffolding.md)).
6. **Tell students what you saw and what you changed.** This is what converts the cycle from surveillance into shared work, and it models the self-assessment you eventually want them doing.
7. **Re-elicit on the same target.** Verify the adjustment worked before treating the target as met; an unverified adjustment is an assumption ([Feedback](../elements/feedback.md)).
8. **Keep it ungraded.** Record what you need for planning, not for the gradebook, so students have no incentive to conceal confusion.

## Related Strategies

- [Formative Assessment Loops](formative-assessment-loops.md) — the same cycle emphasized as a repeating structure across a unit
- [Formative Assessment Routines](formative-assessment-routines.md) — the habitual classroom moves that make the cycle cheap enough to run often
- [Formative Feedback](formative-feedback.md) — the message delivered to the learner within the cycle, and what makes it actionable
- [Exit Ticket](exit-ticket.md) — the most common lesson-boundary eliciting device
- [Drafting and Feedback Cycles](drafting-and-feedback-cycles.md) — the cycle applied to extended work rather than to concepts
- [Formative Self-Assessment](formative-self-assessment.md) — moves the interpreting and adjusting moves to the learner
- [Describe a support system's design intent by asking against whose Synthesis or Analysis it elicits a structural gap](design-intent-gap-origin-question.md)
- [3-2-1 Reflection](../strategies/3-2-1_reflection.md) — a lightweight elicitation routine for surfacing prior conceptions and confusion
- [Retrieval Practice](retrieval-practice-activities.md) — low-stakes quizzing that doubles as formative evidence and memory strengthening
- [Self-assessment as a formative assessment practice that supports students to act as self-regulated agents](self-assessment-supports-self-regulated-agents.md)

## Examples

**Mid-explanation diagnostic questions:** A teacher pauses an explanation, poses a multiple-choice question whose distractors each encode a known misconception, reads the whole-class response on mini-whiteboards, and either re-explains or proceeds — a cycle of under two minutes.

**Exit ticket driving the next lesson's starter:** Students answer two questions on leaving; the teacher sorts the responses into three piles that evening and opens the next lesson with the error that dominated.

**Unit pre-assessment in mathematics:** A short diagnostic before a fractions unit identifies which students already hold the prerequisite, allowing the first two lessons to be re-planned around the specific gaps rather than taught to the middle.

**Draft-conference-redraft in writing:** The cycle runs over a text — draft, targeted feedback on one criterion, redraft, check on that criterion — rather than over a concept.
- **Dylan Wiliam's "hinge questions"** — multiple-choice items with distractors mapped to specific misconceptions; the whole class answers simultaneously and the teacher chooses one of several pre-planned instructional responses.
- **[Kahoot!](https://kahoot.com) / [Poll Everywhere](https://www.polleverywhere.com)** — anonymous whole-class response systems that make the misconception distribution visible to instructor and learners alike.
- **[ASSISTments](https://www.assistments.org)** — online math homework platform that gives immediate task-level feedback to students and error-pattern reports to teachers, who adjust the next lesson.

## Key Sources
- Black, P., & Wiliam, D. (1998). Assessment and classroom learning. *Assessment in Education: Principles, Policy & Practice, 5*(1), 7–74. [doi:10.1080/0969595980050102](https://doi.org/10.1080/0969595980050102)
- Wiliam, D. (2011). What is assessment for learning? *Studies in Educational Evaluation, 37*(1), 3–14. [doi:10.1016/j.stueduc.2011.03.001](https://doi.org/10.1016/j.stueduc.2011.03.001)
- Hattie, J., & Timperley, H. (2007). The power of feedback. *Review of Educational Research, 77*(1), 81–112. [doi:10.3102/003465430298487](https://doi.org/10.3102/003465430298487)
- Sadler, D. R. (1989). Formative assessment and the design of instructional systems. *Instructional Science, 18*(2), 119–144. [doi:10.1007/BF00117714](https://doi.org/10.1007/BF00117714)
- Nicol, D. J., & Macfarlane-Dick, D. (2006). Formative assessment and self-regulated learning: A model and seven principles of good feedback practice. *Studies in Higher Education, 31*(2), 199–218. [doi:10.1080/03075070600572090](https://doi.org/10.1080/03075070600572090)

<!-- merged 2026-10-13 from strategies/formative-assessment ("Formative Assessment"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Formative Assessment

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (2 for, 1 mixed) · 7 studies (5 quant-synthesis, 1 causal, 1 review), `q2`–`q4` · 5 of 7 report an effect size

## Description
Formative assessment is the process of gathering evidence about learner understanding *while* learning is underway and using that evidence to adjust instruction and learner activity. It differs from summative assessment in purpose rather than instrument: the same quiz is formative if its results change what happens next, summative if it only certifies attainment. The core loop is: elicit evidence → interpret it against learning goals → act on it (by teacher, learner, or peers) [Assessment used formatively improves achievement.](../claims/assessment-for-learning-improves-achievement.md) [+S].

## Design Implications

Formative assessment operationalizes [Assessment for Learning](../principles/assessment-for-learning.md): assessment tasks become instructional events rather than measurement events. Its effect sizes are among the largest in education, but only when the information produced actually feeds forward into modified teaching or study behavior — assessment without consequential adjustment produces little gain [Assessment used formatively improves achievement.](../claims/assessment-for-learning-improves-achievement.md) [+S]. Feedback is the primary mechanism, and it works best when it answers "Where am I going? How am I doing? Where to next?" rather than grading the person [Feedback improves learning when it addresses the task, not the self.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S].

### Context
#### Requirements
- Clear, shared learning targets — learners cannot close a gap they cannot see ([Constructive Alignment](../patterns/constructive-alignment.md))
- Low-stakes elicitation tasks that surface *thinking*, not just answers ([Check-In](../elements/check-in.md), [3-2-1 Reflection](../strategies/3-2-1_reflection.md))
- A decision rule: the instructor must know in advance what they will do with each likely result (reteach, regroup, advance)
- Feedback that specifies the gap between current and target performance and gives actionable next steps

#### Constraints
- Feedback that is only evaluative (grades, praise) yields near-zero gains and can reduce performance [Feedback improves learning when it addresses the task, not the self.](../claims/feedback-most-effective-at-task-and-process-levels.md) [-M]
- Frequent low-stakes quizzing without instructional response adds workload and anxiety without benefit [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) [~M]
- Public elicitation can expose struggling learners; anonymous response systems mitigate this
- Over-reliance on self-assessment without training produces inaccurate self-ratings, especially in novices [~M]

#### Implementation Variability
- **Elicitation format:** exit tickets, hinge-point multiple-choice questions, whiteboards, clickers, think-pair-share
- **Response locus:** teacher-adjusted (reteaching), learner-adjusted (revision, self-regulation), or peer-adjusted (structured peer feedback)
- **Technology-mediated:** adaptive platforms that adjust item difficulty from response data ([Adaptive Learning](../principles/adaptive-learning.md))

### Target Learners
- Struggling and lower-attaining learners benefit most; ungraded frequent assessment disproportionately raises their achievement [Assessment used formatively improves achievement.](../claims/assessment-for-learning-improves-achievement.md) [+S]
- Learners developing self-regulation, who need external monitoring cues before internalizing them
- Less effective when learners lack the prerequisite knowledge to interpret feedback meaningfully [~M]

### Target Learning Goals
- Conceptual understanding: diagnosing and correcting misconceptions mid-instruction
- Skill development: identifying which step of a procedure breaks down
- Self-regulated learning: building learners' capacity to judge their own work against criteria

### Instructions
1. Define the learning target and a "hinge question" whose answers discriminate between key understandings and misconceptions.
2. Elicit responses from *all* learners simultaneously (whiteboards, clickers, [Check-In](../elements/check-in.md) routines) — not just volunteers.
3. Interpret the distribution against your decision rule; resist explaining before learners have attempted the task.
4. Act: reteach, restructure groups, or move on — visibly connecting the adjustment to the evidence.
5. Provide task-level feedback with a next step, then require learners to act on it ([Assessment](../elements/assessment.md)).
6. Repeat at spaced intervals; formative assessment is a cycle, not an event.

## Related Strategies

- [3-2-1 Reflection](../strategies/3-2-1_reflection.md) — a lightweight elicitation routine for surfacing prior conceptions and confusion
- [Exit Tickets](exit-ticket.md) — end-of-session evidence capture that shapes the next session
- [Retrieval Practice](retrieval-practice-activities.md) — low-stakes quizzing that doubles as formative evidence and memory strengthening
- [Self-assessment as a formative assessment practice that supports students to act as self-regulated agents](self-assessment-supports-self-regulated-agents.md)

## Examples
- **Dylan Wiliam's "hinge questions"** — multiple-choice items with distractors mapped to specific misconceptions; the whole class answers simultaneously and the teacher chooses one of several pre-planned instructional responses.
- **[Kahoot!](https://kahoot.com) / [Poll Everywhere](https://www.polleverywhere.com)** — anonymous whole-class response systems that make the misconception distribution visible to instructor and learners alike.
- **[ASSISTments](https://www.assistments.org)** — online math homework platform that gives immediate task-level feedback to students and error-pattern reports to teachers, who adjust the next lesson.

## Key Sources
- Black, P., & Wiliam, D. (1998). Assessment and classroom learning. *Assessment in Education: Principles, Policy & Practice, 5*(1), 7–74. [doi:10.1080/0969595980050102](https://doi.org/10.1080/0969595980050102)
- Sadler, D. R. (1989). Formative assessment and the design of instructional systems. *Instructional Science, 18*(2), 119–144. [doi:10.1007/BF00117714](https://doi.org/10.1007/BF00117714)
- Hattie, J., & Timperley, H. (2007). The power of feedback. *Review of Educational Research, 77*(1), 81–112. [doi:10.3102/003465430298487](https://doi.org/10.3102/003465430298487)
- Nicol, D. J., & Macfarlane-Dick, D. (2006). Formative assessment and self-regulated learning: A model and seven principles of good feedback practice. *Studies in Higher Education, 31*(2), 199–218. [doi:10.1080/03075070600572090](https://doi.org/10.1080/03075070600572090)
-->

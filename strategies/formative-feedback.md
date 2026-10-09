---
type: strategy
id: formative-feedback
aliases: [formative_feedback]
title: Formative Feedback
description: Giving learners information about their work that tells them where they are going, how they are doing, and what to do next — while there is still time and opportunity to act on it.
status: review
generated:
  by: claude/unspecified
  at: 2026-08-30
sources:
  - id: hattie-timperley-2007
    resource: "https://doi.org/10.3102/003465430298487"
    title: "Hattie, J., & Timperley, H. (2007). The power of feedback. *Review of Educational Research, 77*(1), 81–112"
    author: "Hattie, J., & Timperley, H"
  - id: shute-2008
    resource: "https://doi.org/10.3102/0034654307313795"
    title: "Shute, V. J. (2008). Focus on formative feedback. *Review of Educational Research, 78*(1), 153–189"
    author: "Shute, V. J"
  - id: kluger-denisi-1996
    resource: "https://doi.org/10.1037/0033-2909.119.2.254"
    title: "Kluger, A. N., & DeNisi, A. (1996). The effects of feedback interventions on performance: A historical review, a meta-analysis, and a preliminary feedback intervention theory. *Psychological Bulletin, 119*(2), 254–284"
    author: "Kluger, A. N., & DeNisi, A"
  - id: black-wiliam-1998
    resource: "https://doi.org/10.1080/0969595980050102"
    title: "Black, P., & Wiliam, D. (1998). Assessment and classroom learning. *Assessment in Education: Principles, Policy & Practice, 5*(1), 7–74"
    author: "Black, P., & Wiliam, D"
---

# Formative Feedback

> **Strategy** · [All strategies](index.md)
> **Evidence** · 10 claims (6 for, 2 mixed, 2 against) · 16 studies (6 quant-synthesis, 4 associational, 3 causal, 3 review), `q2`–`q4` · 6 of 16 report an effect size · 2 claims rest on one study

## Description
Formative feedback is information given to a learner about their work, at a point where they can still change the work or their approach to the next one. What makes it formative is not its timing alone but its content and its consequence: it addresses the task or the process rather than the person, it names a specific next action, and it is followed by an opportunity to act. A comment on a returned final paper that no one will revise is summative regardless of how detailed it is.

## Design Implications

Feedback is among the highest-variance interventions in education — large average effects concealing a substantial minority of studies where feedback made performance *worse* [Feedback improves learning by a medium amount on average, but its effect varies widely with the information it carries, and more than a third of feedback interventions reduce performance](../claims/feedback-improves-learning.md) [+S]. Kluger and DeNisi's meta-analysis located the mechanism: feedback that draws attention to the self rather than the task diverts effort into managing self-image instead of improving work, and this is where negative effects concentrate [Praise for intelligence, rather than for effort, after success undermines children's motivation and performance after a later failure](../claims/feedback-praise-reduces-learning.md) [-M]. Person-directed praise and bare grades both do this.

The usable design rule comes from Hattie and Timperley: effective feedback answers three questions — where am I going, how am I doing, and where to next — and operates at the task, process, or self-regulation level rather than the self level [Feedback that answers three questions (Where am I going? How am I doing? Where to next?) improves learning.](../claims/feedback-answers-three-questions-improves-learning.md) [+S] [Feedback Most Effective At Task And Process Levels](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S]. The second rule is that feedback only works if it is used: information the learner reads and files changes nothing [Feedback improves learning, with a medium average effect that varies widely by feedback type](../claims/feedback-improves-learning.md) [+M]. Most of the design work in practice is engineering the uptake, not improving the wording.

### Context
#### Requirements
- Criteria the learner already understands, so "where am I going" has a referent ([Criteria Development](../elements/criteria-development.md), [Learning Goals](../elements/learning-goals.md))
- A subsequent opportunity to act — a revision, a re-attempt, or a closely related next task. Without it the feedback cannot be formative
- Time protected for learners to read, interpret, and respond, treated as classwork rather than homework
- Feedback specific enough to act on: naming what to change and how, not only that something is wrong
- Separation from grades, since a mark attached to a comment reliably captures the learner's attention and suppresses engagement with the comment [Praise for intelligence, rather than for effort, after success undermines children's motivation and performance after a later failure](../claims/feedback-praise-reduces-learning.md) [-M]
- Clear success criteria shared with learners before work begins, so feedback has a reference point
- Timing that lets learners revise or retry — feedback delivered after the opportunity to act is wasted
- A climate of psychological safety; learners must see feedback as information, not judgment
- Follow-up structures: revision cycles, [Practice](../elements/practice.md), or [Coaching](../elements/coaching.md) that convert feedback into action

#### Constraints
- Feedback directed at the person — praise, ability attributions, discouragement — moves attention to the self and can depress subsequent performance [Praise for intelligence, rather than for effort, after success undermines children's motivation and performance after a later failure](../claims/feedback-praise-reduces-learning.md) [-S]
- Excessive feedback overwhelms: marking every error on a piece of work produces a document the learner cannot act on and often does not read [Cognitive Overload Degrades Learning](../claims/cognitive-overload-degrades-learning.md) [-M]
- Feedback at the self-regulation level presumes learners who can act on it; novices given "think about your strategy" without a concrete task-level correction have nothing to do [~M]
- Learners without sufficient prior knowledge cannot judge whether feedback applies to their work, and may implement it mechanically or not at all [Prior Knowledge Needed For Accurate Self Assessment](../claims/prior-knowledge-needed-for-accurate-self-assessment.md) [~M]
- Delayed feedback on a task the learner has moved on from produces no revision and little learning [-M]
- Peer-generated feedback varies in accuracy with the peer's own expertise, so it needs criteria and moderation [Peer feedback accuracy depends on expertise.](../claims/peer-feedback-accuracy-depends-on-expertise.md) [~M]
- Overly detailed feedback can overwhelm novices; too little leaves experts unmoved — the [expertise-reversal effect](../theories/expertise-reversal-effect.md) applies to feedback granularity [~M]
- In high-stakes evaluative climates, learners may optimize for the grade rather than the improvement the feedback describes [~M]

#### Implementation Variability
- **Comment-only marking** — grades withheld until after revision, so the comment is the only available signal ([Effective Feedback](effective_feedback.md))
- **Whole-class feedback** — the teacher reads a set, identifies the three common issues, and teaches into them rather than writing individual comments
- **Audio or video feedback** — spoken commentary conveys more nuance per minute and reads as less punitive ([Audio Feedback](audio-feedback.md))
- **Feed-forward on the next task** — feedback framed entirely as instructions for the upcoming piece, which guarantees an opportunity to act
- **Peer feedback against criteria** — distributes the load and benefits the giver as much as the receiver ([Peer Feedback](peer_feedback.md))
- **Drafting cycles** — feedback embedded in a required draft-revise sequence ([Drafting and Feedback Cycles](drafting-and-feedback-cycles.md))
- Teacher-to-learner feedback: the default mode; strongest when tied to explicit criteria
- Peer feedback: builds evaluative judgment; requires training and structured protocols (e.g., two-stars-and-a-wish, rubric-guided critique)
- Self-assessment: develops self-regulation as learners internalize the criteria [Self-monitoring improves self-regulation.](../claims/self-monitoring-improves-self-regulation.md) [+M]
- Automated feedback: scalable and immediate, but limited to well-specified task domains
- The same formative logic applies to teacher professional growth: performance management framed as developmental rather than evaluative, with the teacher participating in setting goals, yields feedback that is more meaningful and applicable to daily practice

### Target Learners
- Learners working on anything revisable — writing, design, code, performance, problem sets with re-attempts
- Novices, who benefit most from task-level correctives and least from abstract process commentary
- Learners who currently receive grades without commentary, for whom almost any actionable specific is an improvement
- Weaker fit where the work is genuinely final and no related task follows; there the honest description is summative assessment
- Requires care with learners for whom critique carries high social or emotional cost, where framing and privacy matter as much as content
- High-achieving learners often need less corrective feedback and more challenge; excessive guidance can reduce their engagement [~M]
- Learners with low self-efficacy need early, achievable success feedback to sustain persistence [Self-efficacy predicts academic persistence.](../claims/self-efficacy-predicts-academic-persistence.md) [+M]

### Target Learning Goals
- Improved performance on the specific task and on structurally similar later ones
- Understanding of quality criteria — what "good" consists of in this domain [Self Assessment Against Criteria Supports Self Regulated Learning](../claims/self-assessment-improves-self-regulated-learning.md) [+M]
- Self-regulation: internalizing the feedback question set so learners eventually ask it of their own work
- Correction of specific misconceptions, particularly confidently held ones [High-confidence errors lead to better retention after correction than low-confidence errors.](../claims/high-confidence-errors-improve-retention.md) [+M]
- Skill refinement: closing specific gaps between current and target performance
- Self-regulated learning: building learners' capacity to judge and adjust their own work
- Conceptual understanding: feedback that surfaces misconceptions for revision [Erroneous examples build conceptual knowledge.](../claims/erroneous-examples-build-conceptual-knowledge.md) [+M]

### Instructions
1. **Make the target visible first.** Share criteria or exemplars before the work begins, so feedback has something to point at ([Criteria Development](../elements/criteria-development.md)).
2. **Limit yourself to two or three points.** Choose the ones that would most improve the next attempt, and leave the rest unmarked ([Cognitive Load Management](../principles/cognitive-load-management.md)).
3. **Write at the task or process level.** Describe what the work does and what to change; avoid comment on the learner's ability, effort, or character.
4. **Answer "where to next" concretely.** End each point with a specific action — a sentence to rewrite, a step to redo, a check to run.
5. **Withhold the grade until revision is done.** If a mark must be recorded, record it privately and release it after the learner has responded.
6. **Schedule the response in class.** Give protected time for learners to read the feedback, mark what they will change, and make the change ([Feedback](../elements/feedback.md)).
7. **Require evidence of uptake.** Ask learners to indicate where they acted on each point, which makes non-use visible to both of you [Feedback improves learning, with a medium average effect that varies widely by feedback type](../claims/feedback-improves-learning.md) [+M].
8. **Check whether it landed.** Look at whether the named issue actually changed; if it did not, the problem is usually clarity or opportunity, not motivation.

## Related Strategies
- [Formative Assessment Cycles](formative-assessment-cycles.md) — the surrounding loop that generates the evidence this feedback responds to
- [Effective Feedback](effective_feedback.md) — the general characteristics of feedback that works, across formative and other uses
- [Drafting and Feedback Cycles](drafting-and-feedback-cycles.md) — the structural guarantee that feedback has something to act on
- [Peer Feedback](peer_feedback.md) — distributes the giving, and benefits the giver [The quality of feedback students give peers predicts gains in their own work, but no recorded study isolates a causal benefit of the assessor role](../claims/peer-assessment-benefits-assessor.md) [+M]
- [Audio Feedback](audio-feedback.md) — a delivery variation that raises nuance per minute of teacher time
- [Exemplar-Based Feedback](exemplar-based-feedback.md) — using annotated examples to communicate the standard rather than describing it
- [Assessment for Learning](../principles/assessment-for-learning.md) — the assessment system that generates formative feedback
- [Activating Prior Knowledge](activating-prior-knowledge.md) — knowing the starting point makes the feedback gap meaningful
- [Self-Monitoring](self-monitoring.md) — the internalized endpoint of formative feedback

## Examples

**Comment-only marking in secondary science:** Work is returned with two specific comments and no mark; learners spend the first ten minutes of the next lesson responding in a different colour, and grades are released only afterwards.

**Whole-class feedback sheets:** Rather than annotating thirty scripts, the teacher records the three most common errors, two strong examples, and one whole-class next step, then teaches directly into those before returning the work.

**Code review as formative feedback:** Reviewers comment on the code and the approach, never on the developer; each comment names a concrete change, and the pull request cannot merge until the author has responded to every one — uptake is structurally enforced.

**Writing conferences:** A three-minute one-to-one on a draft, ending with the learner stating the single change they will make next — the "where to next" question answered by the learner rather than the teacher.
- **MyWritingLab / Turnitin Feedback Studio** — inline instructor and automated comments on drafts before final submission, making revision the point of the feedback cycle.
- **Khan Academy** — immediate correctness feedback and hint scaffolds on every practice item, so learners act on feedback within seconds.
- **Peer observation programs in schools** — teachers observe colleagues using a structured framework and exchange developmental (non-evaluative) feedback, applying the same formative logic to educator growth; this works best when teachers help set the observation goals and feedback is decoupled from formal evaluation.
- **Dylan Wiliam's "embedded formative assessment"** — engineering classroom discussions, hinge questions, and comment-only marking (no grades) so students must read and use the feedback.

## Key Sources
- Hattie, J., & Timperley, H. (2007). The power of feedback. *Review of Educational Research, 77*(1), 81–112. [doi:10.3102/003465430298487](https://doi.org/10.3102/003465430298487)
- Shute, V. J. (2008). Focus on formative feedback. *Review of Educational Research, 78*(1), 153–189. [doi:10.3102/0034654307313795](https://doi.org/10.3102/0034654307313795)
- Kluger, A. N., & DeNisi, A. (1996). The effects of feedback interventions on performance: A historical review, a meta-analysis, and a preliminary feedback intervention theory. *Psychological Bulletin, 119*(2), 254–284. [doi:10.1037/0033-2909.119.2.254](https://doi.org/10.1037/0033-2909.119.2.254)
- Black, P., & Wiliam, D. (1998). Assessment and classroom learning. *Assessment in Education: Principles, Policy & Practice, 5*(1), 7–74. [doi:10.1080/0969595980050102](https://doi.org/10.1080/0969595980050102)

<!-- merged 2026-10-09 from strategies/formative_feedback ("Formative Feedback"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Formative Feedback

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (4 for) · 8 studies (3 quant-synthesis, 3 review, 1 causal, 1 theoretical), `q2`–`q4` · 2 of 8 report an effect size

## Description
Formative feedback is information provided to learners *while* learning is underway, describing the gap between current and desired performance and pointing to concrete next steps. It is carried out through timely, specific, task- and process-focused comments, self- and peer-assessment routines, and iterative revision cycles — in contrast to summative evaluation, which renders a judgment after learning concludes.

## Design Implications

Feedback is among the most powerful influences on achievement, but its effects are highly variable: it improves learning when it answers "Where am I going? How am I doing? Where to next?" and can depress learning when it directs attention to the self rather than the task [Feedback is most effective at task and process levels.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S]. Feedback should therefore be specific, actionable, and timed so learners can act on it while effort still matters.

### Context
#### Requirements
- Clear success criteria shared with learners before work begins, so feedback has a reference point
- Timing that lets learners revise or retry — feedback delivered after the opportunity to act is wasted
- A climate of psychological safety; learners must see feedback as information, not judgment
- Follow-up structures: revision cycles, [Practice](../elements/practice.md), or [Coaching](../elements/coaching.md) that convert feedback into action

#### Constraints
- Feedback on personal traits ("you're so smart") can undermine persistence and encourage entity beliefs; praise for process and strategy works better [Feedback is most effective at task and process levels.](../claims/feedback-most-effective-at-task-and-process-levels.md) [-M]
- Feedback given without opportunity to apply it produces negligible gains [Feedback is most effective at task and process levels.](../claims/feedback-most-effective-at-task-and-process-levels.md) [-S]
- Overly detailed feedback can overwhelm novices; too little leaves experts unmoved — the [expertise-reversal effect](../theories/expertise-reversal-effect.md) applies to feedback granularity [~M]
- In high-stakes evaluative climates, learners may optimize for the grade rather than the improvement the feedback describes [~M]

#### Implementation Variability
- Teacher-to-learner feedback: the default mode; strongest when tied to explicit criteria
- Peer feedback: builds evaluative judgment; requires training and structured protocols (e.g., two-stars-and-a-wish, rubric-guided critique)
- Self-assessment: develops self-regulation as learners internalize the criteria [Self-monitoring improves self-regulation.](../claims/self-monitoring-improves-self-regulation.md) [+M]
- Automated feedback: scalable and immediate, but limited to well-specified task domains
- The same formative logic applies to teacher professional growth: performance management framed as developmental rather than evaluative, with the teacher participating in setting goals, yields feedback that is more meaningful and applicable to daily practice

### Target Learners
- Struggling learners benefit most from process-level guidance about strategies [Feedback is most effective at task and process levels.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S]
- High-achieving learners often need less corrective feedback and more challenge; excessive guidance can reduce their engagement [~M]
- Learners with low self-efficacy need early, achievable success feedback to sustain persistence [Self-efficacy predicts academic persistence.](../claims/self-efficacy-predicts-academic-persistence.md) [+M]

### Target Learning Goals
- Skill refinement: closing specific gaps between current and target performance
- Self-regulated learning: building learners' capacity to judge and adjust their own work
- Conceptual understanding: feedback that surfaces misconceptions for revision [Erroneous examples build conceptual knowledge.](../claims/erroneous-examples-build-conceptual-knowledge.md) [+M]

### Instructions
1. Establish success criteria and exemplars before the task ([Advance Organizers](../elements/advance-organizers.md), [Assessment](../elements/assessment.md) for learning)
2. Collect evidence of current performance during learning ([Check-ins](../principles/check-ins.md), [Assess Performance](../elements/assess-performance.md))
3. Deliver feedback focused on the task and process, not the person — specific, actionable, and timed for use [Feedback is most effective at task and process levels.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S]
4. Require learners to act on the feedback through revision or retry ([Practice](../elements/practice.md))
5. Gradually transfer evaluative judgment to learners ([Fading](../elements/fading.md)), moving from teacher feedback to peer and self-assessment

## Related Strategies
- [Assessment for Learning](../principles/assessment-for-learning.md) — the assessment system that generates formative feedback
- [Activating Prior Knowledge](activating-prior-knowledge.md) — knowing the starting point makes the feedback gap meaningful
- [Self-Monitoring](self-monitoring.md) — the internalized endpoint of formative feedback

## Related Elements
- [Provide Feedback](../elements/provide-feedback.md) — the core element this strategy operationalizes
- [Coaching](../elements/coaching.md) — delivers feedback in a continuous, relational form
- [Fading](../elements/fading.md) — progressively hands evaluative responsibility to the learner

## Examples
- **MyWritingLab / Turnitin Feedback Studio** — inline instructor and automated comments on drafts before final submission, making revision the point of the feedback cycle.
- **Khan Academy** — immediate correctness feedback and hint scaffolds on every practice item, so learners act on feedback within seconds.
- **Peer observation programs in schools** — teachers observe colleagues using a structured framework and exchange developmental (non-evaluative) feedback, applying the same formative logic to educator growth; this works best when teachers help set the observation goals and feedback is decoupled from formal evaluation.
- **Dylan Wiliam's "embedded formative assessment"** — engineering classroom discussions, hinge questions, and comment-only marking (no grades) so students must read and use the feedback.

## Key Sources
- Hattie, J., & Timperley, H. (2007). The power of feedback. *Review of Educational Research, 77*(1), 81–112. [doi:10.3102/003465430298487](https://doi.org/10.3102/003465430298487)
- Black, P., & Wiliam, D. (1998). Assessment and classroom learning. *Assessment in Education: Principles, Policy & Practice, 5*(1), 7–74. [doi:10.1080/0969595980050102](https://doi.org/10.1080/0969595980050102)
- Shute, V. J. (2008). Focus on formative feedback. *Review of Educational Research, 78*(1), 153–189. [doi:10.3102/0034654307313795](https://doi.org/10.3102/0034654307313795)
- Kluger, A. N., & DeNisi, A. (1996). The effects of feedback interventions on performance: A historical review, a meta-analysis, and a preliminary feedback intervention theory. *Psychological Bulletin, 119*(2), 254–284. [doi:10.1037/0033-2909.119.2.254](https://doi.org/10.1037/0033-2909.119.2.254)
-->

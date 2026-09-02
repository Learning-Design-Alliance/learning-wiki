---
type: strategy
id: model_and_example_feedback
title: Model and Example Feedback
description: Communicating assessment expectations to learners by showing annotated models of strong and weak work, so feedback criteria become concrete rather than abstract.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Model and Example Feedback

> **Strategy** · [All strategies](index.md)

## Description
Model and example feedback communicates the purpose and criteria of an assessment by showing learners concrete exemplars — a strong ("A-level") model, a weak ("C-level") contrast, and ideally intermediate cases — with annotation explaining *why* each exemplar earns its quality level. Rather than describing standards in the abstract, the instructor makes quality visible, turning evaluation criteria into observable features learners can compare against their own work.

## Design Implications

Exemplars work because they convert abstract rubric language into perceptual, comparable instances; contrasting multiple cases supports abstraction of the underlying criteria [Comparing multiple contrasting cases supports abstraction of deep features.](../claims/multiple-contrasting-cases-support-abstraction.md) [+M]. The annotation matters as much as the examples: models without explanation of *why* they succeed invite surface imitation, so pair each model with commentary linking features to criteria, and prompt learners to [Self-Explanation](../elements/self-explanation.md) the gap between their draft and the model [Self-explanation improves conceptual understanding.](../claims/self-explanation-improves-conceptual-understanding.md) [+S]. Weak examples are not filler — studying flawed work with guided analysis builds conceptual understanding of the criteria [Erroneous examples build conceptual knowledge.](../claims/erroneous-examples-build-conceptual-knowledge.md) [+M].

### Context
#### Requirements
- Authentic, high-quality models of the target performance, ideally from prior students or real contexts
- A deliberate quality contrast (strong vs. weak, or a quality gradient) rather than a single exemplar
- Annotation or commentary that maps exemplar features to assessment criteria ([Demonstration](../elements/demonstration.md), [Non-Examples](../elements/non-examples.md))
- A mechanism for learners to apply the criteria to their own or peers' work ([Provide Feedback](../elements/provide-feedback.md), [Rubrics](../elements/rubrics.md))

#### Constraints
- A single model anchors learners to one "correct" version and suppresses legitimate variation in approach [~M] — use multiple contrasting models to avoid this
- Learners may copy surface features of the model rather than the underlying qualities, especially when annotation is thin [-M]
- If models are far above learners' current level, they can demotivate rather than inform; the exemplar should be attainably excellent [~W]
- Passive exposure to exemplars without an application or comparison task produces shallow encoding [-S]

#### Implementation Variability
- **Full-to-faded models**: show a complete exemplar, then progressively incomplete ones learners must finish
- **Live critique**: instructor evaluates an anonymous draft against criteria in front of the class, modeling the evaluation process itself
- **Peer calibration**: learners score samples, compare their judgments with the instructor's, and discuss discrepancies — used extensively in [Calibrated Peer Review](https://calibratedpeerreview.org)
- **Exemplar banks**: curated collections of past student work at multiple quality levels, searchable by assignment

### Target Learners
- Novices who cannot yet infer quality criteria from abstract rubric language [Comparing multiple contrasting cases supports abstraction of deep features.](../claims/multiple-contrasting-cases-support-abstraction.md) [+M]
- Advanced learners especially benefit from weak-example analysis, which sharpens discrimination beyond what positive models alone teach [Erroneous examples build conceptual knowledge.](../claims/erroneous-examples-build-conceptual-knowledge.md) [+M]
- Less beneficial for expert learners, who already possess internalized standards and may find exemplars redundant [~W]

### Target Learning Goals
- Clarifying performance expectations and assessment criteria
- Developing evaluative judgment — the capacity to judge quality in one's own and others' work
- Guiding revision and improvement of drafts ([Assessment for Learning](../principles/assessment-for-learning.md))

### Instructions
1. Select or create a strong model and a contrasting weaker example of the target task ([Demonstration](../elements/demonstration.md))
2. Annotate both, explicitly linking features to the assessment criteria; keep commentary criterion-referenced, not taste-referenced
3. Have learners compare the models and articulate the differences ([Comparing Cases](../elements/comparing-cases.md)), prompting [Self-Explanation](../elements/self-explanation.md)
4. Have learners apply the criteria to a sample draft or their own work before submitting ([Provide Feedback](../elements/provide-feedback.md))
5. Repeat with new exemplars as task complexity grows, fading annotation over time

## Related Strategies
- [Use Worked Examples](../strategies/use_worked_examples.md) — the problem-solving analogue: models of solutions rather than models of finished products
- [Think-Aloud Modeling](../strategies/think-aloud-modeling.md) — makes the *evaluation* reasoning visible, not just the product
- [Action-Oriented Feedback](../strategies/action-oriented_feedback.md) — exemplars show the target; actionable feedback tells learners how to close the gap

## Examples
- **Calibrated Peer Review (https://calibratedpeerreview.org)** — students first rate sample essays and receive feedback on the accuracy of their judgments before reviewing peers, operationalizing exemplar-based calibration.
- **Writing-across-the-curriculum practice** — instructors distribute an annotated A paper and a C paper side by side; students list the differences before drafting, then self-assess their draft against the A model.
- **Video-based coaching** — a coach shows footage of expert technique alongside a novice's attempt, pausing to contrast specific movement features before practice.

## Key Sources
- Sadler, D. R. (1989). Formative assessment and the design of instructional systems. *Instructional Science, 18*(2), 119–144. [doi:10.1007/BF00117714](https://doi.org/10.1007/BF00117714)
- Hattie, J., & Timperley, H. (2007). The power of feedback. *Review of Educational Research, 77*(1), 81–112. [doi:10.3102/003465430298487](https://doi.org/10.3102/003465430298487)
- Große, C. S., & Renkl, A. (2007). Finding and fixing errors in worked examples: Can this foster learning outcomes? *Learning and Instruction, 17*(3), 312–322. [doi:10.1016/j.learninstruc.2007.02.005](https://doi.org/10.1016/j.learninstruc.2007.02.005)
- Nicol, D. J., & Macfarlane-Dick, D. (2006). Formative assessment and self-regulated learning: A model and seven principles of good feedback practice. *Studies in Higher Education, 31*(2), 199–218. [doi:10.1080/03075070600572090](https://doi.org/10.1080/03075070600572090)

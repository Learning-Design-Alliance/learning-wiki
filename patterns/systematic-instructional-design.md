---
type: pattern
id: systematic-instructional-design
title: Systematic Instructional Design
description: The objective-first design process — ADDIE and the Dick & Carey systems approach — in which instructional goals are analysed into subordinate skills, assessments are written from the objectives, instruction is built to serve them, and formative evaluation feeds revision before the design is released.
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-02
author: Robert Gagné, Walter Dick and Lou Carey lineage
grain_size: course
---

# Systematic Instructional Design

> **Pattern** · [All patterns](index.md)

## Description
Systematic instructional design treats a course as a system whose parts must be derived from a stated goal and checked against it. The lineage runs from Gagné's analysis of learning conditions through the military and industrial training models of the 1970s to ADDIE — Analysis, Design, Development, Implementation, Evaluation — and to Dick & Carey's *systematic design of instruction*, which is the fullest published expression of it.

Its defining commitment is **derivation**: nothing enters the course that cannot be traced to an objective, and no objective survives that cannot be assessed. Instructional analysis decomposes the goal into the subordinate skills a learner must already have; assessment items are written from the objectives *before* the instruction is built, so that alignment is a construction step rather than a later audit; formative evaluation with real learners drives revision before release.

**This is not Gagné's nine events.** The nine events are a lesson-level method — what happens inside one instructional episode — and are described at [Gagné's 9 Events of Instruction](gagnes-9-events-of-instruction.md). This page is the course-level process that decides which lessons should exist at all. Gagné contributed to both, which is why they are routinely conflated.

## Implications

### Context
#### Requirements
- **A goal that can be stated as performance** — what a learner will be able to do, in what conditions, to what criterion. The process has little purchase on goals that resist that statement
- **Time up front.** Analysis and objective-writing consume budget before anything visible exists, which is the process's main political cost
- **Access to learners or performers for the analysis and for formative evaluation** — the two steps most often cut, and the two that carry most of the method's value
- **Stable content.** The derivation chain is expensive to rebuild, so it assumes the target is not moving underneath it

#### Constraints
- **Waterfall failure mode.** Run linearly with one evaluation at the end, ADDIE discovers a wrong analysis after the whole course is built — the criticism [Successive Approximation](successive-approximation-model.md) was formulated against
- **Objectives crowd out what cannot be operationalised.** Dispositions, judgement and taste are hard to write as performance objectives and so tend to be dropped rather than taught
- **Analysis paralysis.** A full hierarchical task analysis of a large domain can outlast the need it was commissioned for
- **Weak on ill-defined problems.** Where nobody yet knows what the course should achieve, the process has nothing to derive from; [Design Thinking](design-thinking.md) starts there instead
- **Over-decomposition risks losing the whole task.** Splitting a complex skill into separately-taught subskills can leave learners able to do each part and unable to do the job — the argument [Whole-task performance improves transfer of complex skills to real-world settings.](../claims/whole-task-performance-improves-transfer.md) [-M] makes against fragmenting practice

#### Grain Size
- Course
- Programme
- Training curriculum

### Target Goals
- Well-defined performance goals — procedures, regulated practice, certification, anything with a defensible criterion
- Designs that must demonstrate alignment to an auditor, an accreditor or a client
- Instruction that will be delivered by people other than its designer, where the derivation chain is the handover document

### Target Learners
- Audiences whose entry skills can be established in advance, which is what the subordinate-skills analysis assumes
- Large or repeat cohorts, where the up-front analysis cost is amortised over many deliveries

### Theory
#### Supporting
- [Information Processing Theory](../theories/information-processing-theory.md) — the account of prerequisite skills that instructional analysis rests on
- [Behaviorism](../theories/behaviorism.md) — the performance-objective form, and criterion-referenced assessment, come from this tradition

#### Contradicting / Qualifying
- [Constructivism](../theories/constructivism.md) — objects to goals fixed before learners are met, and to decomposition that removes the meaningful whole
- [Situated Learning](../theories/situated-learning.md) — subordinate skills taught out of context transfer poorly to the setting that motivated them

### Claims
#### Supporting
- [Goal setting improves performance.](../claims/goal-setting-improves-performance.md) [+M] — the case for stating the target before designing toward it
- [Feedback is most effective when directed at the task and process rather than the self.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S] — what makes formative evaluation a revision instrument
- [Prior knowledge determines new learning.](../claims/prior-knowledge-determines-new-learning.md) [+S] — the premise of entry-behaviour analysis

#### Contradicting
- [Whole-task performance improves transfer of complex skills to real-world settings.](../claims/whole-task-performance-improves-transfer.md) [-M] — a constraint on part-task decomposition, not on the process as a whole

## Design

### Sequence
1. **Identify the instructional goal** — what performance the instruction exists to produce
2. **Conduct an instructional analysis** — decompose the goal into subordinate skills and their prerequisite relations. [Task Analysis](../strategies/task-analysis.md), [Learning Hierarchy Task Analysis](../strategies/learning-hierarchy-task-analysis.md) and, where the demands are judgemental rather than procedural, [Cognitive Task Analysis](../strategies/cognitive-task-analysis.md)
3. **Analyse learners and context** — entry behaviours, characteristics, and the setting of both instruction and performance. [Learner and Context Analysis](../strategies/learner-and-context-analysis.md), [Needs Analysis](../strategies/needs-analysis.md)
4. **Write performance objectives** — conditions, behaviour, criterion. [Learning Objectives](../elements/learning-objectives.md)
5. **Develop criterion-referenced assessments** — written from the objectives, before the instruction
6. **Develop the instructional strategy** — sequence, grouping, events, media
7. **Develop and select materials**
8. **Design and conduct formative evaluation** — one-to-one, small group, field trial. [Formative Evaluation](../strategies/formative-evaluation.md)
9. **Revise the instruction** against what the evaluation found
10. **Design and conduct summative evaluation** — a judgement of the released course, conducted independently of its designer

Steps 1–3 are ADDIE's *Analysis*; 4–6 its *Design*; 7 its *Development*; the field trial and release its *Implementation*; 8–10 its *Evaluation*.

### Elements Used
- [Learning Objectives](../elements/learning-objectives.md)
- [Audience Analysis](../elements/audience-analysis.md)
- [Assessment](../elements/assessment.md)
- [Summative Assessment](../elements/summative-assessment.md)

### Affordances
- [Formative Assessment](../principles/formative-assessment.md)

### Personalization
- **Iterative ADDIE.** Running the phases as a loop rather than a line — evaluating after each phase instead of at the end — recovers most of what [Successive Approximation](successive-approximation-model.md) was built to fix, without abandoning the derivation chain
- **Where the goal is externally set**, steps 1–2 are partly done for you: a [standards crosswalk](../strategies/standards-crosswalk.md) supplies the goal tree and its codes, and the analysis begins at the subordinate-skill level
- **Small designs** can collapse steps 6–7 and run a single one-to-one formative round; skipping formative evaluation entirely is what turns this into a waterfall

## Related Patterns
- [Gagné's 9 Events of Instruction](gagnes-9-events-of-instruction.md) — the lesson-level method inside step 6, explicitly not this process
- [Successive Approximation Model](successive-approximation-model.md) — the iterative reply to this process's waterfall failure mode
- [Understanding by Design](understanding-by-design.md) — shares the objective-and-assessment-first commitment at unit grain; see [Backward Design](../strategies/backward-design.md)
- [4C/ID (Four-Component Instructional Design)](4cid-four-component-instructional-design.md) — a systematic process that deliberately keeps the whole task intact
- [Design Thinking](design-thinking.md) — the contrasting process where the goal is not yet known

## Examples
- **Military and industrial training design** — the setting the systems approach was developed in and where the full ten steps are still routinely run
- **Certification and licensure courses** — where a defensible chain from objective to assessment item is the deliverable, not a by-product

## Key Sources
- Curry, Johnson, & Peacock. Ch. 23 in *Design for Learning*. EdTech Books. [https://edtechbooks.org/id/robert_gagn_and_systematic_design](https://edtechbooks.org/id/robert_gagn_and_systematic_design)
- Dick, W., Carey, L., & Carey, J. O. (2015). *The systematic design of instruction* (8th ed.). Pearson.
- Gagne, R. M. (1985). *The conditions of learning* (4th ed.). Holt, Rinehart and Winston.

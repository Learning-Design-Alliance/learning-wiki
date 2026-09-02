---
type: strategy
id: standards-crosswalk
title: Standards Crosswalk
description: Deriving a course's goal tree from an external framework — a standards set, competency model or certification blueprint — and carrying the framework's own codes through objectives, activities and assessment items so that coverage and provenance stay traceable in both directions.
status: review
generated:
  by: claude/unspecified
  at: 2026-09-02
---

# Standards Crosswalk

> **Strategy** · [All strategies](index.md)

## Description
Many designs do not get to choose their goals. A state standards set, a professional competency framework, an accreditation outcome list or a certification blueprint arrives already written, and the design's job is to satisfy it and to be able to show that it does. A **crosswalk** is the artifact that makes that possible: a table mapping each statement in the external framework onto the course's own goals, and each course goal back onto the statements it serves.

Two properties make it more than paperwork.

**It runs in both directions, and the two directions catch different faults.** Framework → course answers *coverage*: which requirements nothing in this course addresses. Course → framework answers *provenance*: which parts of this course exist for a reason nobody can name. The second is the one teams skip and the one that surfaces inherited content — a fortnight on a topic that is in the course because it was in the course.

**It carries the framework's codes, not just its wording.** A goal tagged `2.b.iii` can be re-checked when the framework is revised, aggregated across a programme, and defended to an auditor. A goal that merely paraphrases `2.b.iii` cannot be any of those things: the moment someone rewords it, the link is gone. Carrying codes down through objectives, activities and individual assessment items is what turns a one-off compliance exercise into a structure the design can be maintained against.

The crosswalk is normally the *first* analysis step where it applies, because it settles what a [needs analysis](needs-analysis.md) would otherwise have to establish, and hands [backward design](backward-design.md) a goal tree to work from.

## Design Implications

### Context
#### Requirements
- **A stable, published framework with identifiers.** A framework whose statements have no codes has to be given local ones, and those must then be versioned by hand
- **The framework's version recorded explicitly.** Frameworks are revised; a crosswalk with no version is a claim about an unspecified document
- **Authority to decide granularity** — whether one framework statement becomes one objective, several, or part of one. This is a judgement, and it must be made once and applied consistently
- **A place to store the codes** that survives content editing: frontmatter, a mapping table, an item bank field. Codes kept only in a planning spreadsheet are gone within a year

#### Constraints
- **Coverage checklisting.** The characteristic failure: every statement is mapped to something, the table is complete and green, and nothing is taught to depth. A crosswalk certifies that a topic was addressed, never that it was learned — [Mastery Learning Improves Outcomes](../claims/mastery-learning-improves-outcomes.md) [~M] is the standard the table cannot speak to
- **Breadth pressure.** A large framework mapped exhaustively onto a fixed number of weeks produces a course that touches everything briefly, which is a reliable route to [Cognitive Overload Degrades Learning](../claims/cognitive-overload-degrades-learning.md) [-M]
- **Double counting.** One activity mapped against six codes looks like six-fold coverage and is one activity; count evidence, not mappings
- **Granularity mismatch is the norm, not the exception.** Framework statements are written at wildly different grains — one is a semester, its neighbour is a definition. Forcing one-to-one correspondence distorts the design
- **Frameworks encode their authors' commitments.** Adopting one wholesale imports a view of the subject; where that view is contested, the crosswalk should record the disagreement rather than silently resolve it
- **Mapping is not alignment.** A code beside an objective asserts intent. Whether the assessment actually elicits that performance is a separate question, and the crosswalk will not ask it

#### Implementation Variability
- **Full vs. partial.** Regulated and certification work maps every statement; a course that merely reports to a programme outcome map might crosswalk only its assessed outcomes
- **Depth of propagation.** Codes on course goals only; or down to objectives; or down to individual assessment items — the last is what makes item-level reporting and gap analysis possible, and costs the most
- **Multiple frameworks at once** — a state standard and a professional competency set — mapped through a single course goal tree rather than by maintaining two parallel tables
- **Coverage grading.** Distinguishing *introduced* / *developed* / *assessed* per statement rather than a binary tick, which is what makes a programme-level map readable

### Target Learners
- Designers serving learners in credentialed, regulated or articulated programmes, where the goals are set by someone the learner will later have to satisfy
- Learners transferring between institutions or progressing through a sequence, for whom the crosswalk is what makes the prior course's claim legible to the next one
- Of little use where goals are genuinely open — there, [Design Thinking](../patterns/design-thinking.md) derives the goals rather than inheriting them

### Target Learning Goals
- The full goal tree the course owes, stated in the course's own language and traceable to its source
- Defensible coverage claims, for accreditation, articulation or a client
- A maintenance surface: when the framework is revised, the affected goals are the ones that can be listed rather than rediscovered

### Instructions
1. **Fix the source.** Name the framework, its version and its date. Copy the statements and their codes verbatim into the working table; do not paraphrase at this stage
2. **Decide granularity once** — what a single row is, and how a statement spanning a whole unit is handled — and write the rule down before mapping, so a later reader can tell a decision from an inconsistency
3. **Map framework → course.** For each statement, record the course goal that serves it, or record explicitly that nothing does. An empty cell is a finding
4. **Map course → framework.** For each existing goal, record which statements it serves. Goals serving none are inherited content, and are either justified in a sentence or cut
5. **Write the course's goals in the course's own language**, each carrying its source codes. The wording is for learners and instructors; the codes are for maintenance. [Learning Objectives](../elements/learning-objectives.md)
6. **Propagate the codes downward** onto objectives, activities and assessment items, as far as the maintenance budget supports
7. **Grade the coverage** — introduced, developed, assessed — rather than ticking, and read the result for statements that are only ever *introduced*
8. **Hand off to [backward design](backward-design.md)**: the goal tree is now the input, and the next question is what evidence each goal requires
9. **Re-run on framework revision**, comparing versions by code. This is the step the codes existed for

## Related Strategies
- [Backward Design](backward-design.md) — the immediate consumer of the goal tree this produces
- [Needs Analysis](needs-analysis.md) — what you do instead when no framework sets the goals, and alongside it when the framework is silent on local need
- [Task Analysis](task-analysis.md) — decomposes a mapped goal into the skills beneath it
- [Learning Hierarchy Task Analysis](learning-hierarchy-task-analysis.md) — orders those skills by prerequisite
- [Standards-Based Grading](standards-based-grading.md) — the reporting practice the same codes make possible
- [Cognitive Task Analysis](cognitive-task-analysis.md) — for the mapped statements that turn out to be judgement rather than procedure

## Examples
- **Accreditation self-study** — a programme outcome map crosswalking every course's assessed outcomes to the accreditor's criteria, graded introduced / developed / assessed
- **Certification preparation** — a course built directly from an exam blueprint, with every item in the bank carrying its blueprint code so coverage gaps are queryable
- **Curriculum adoption** — crosswalking a purchased curriculum against local standards to find what it does not cover before it is bought

## Key Sources
- Martin, & Ritzhaupt. Ch. 21 in *Design for Learning*. EdTech Books.

<!-- Chapter title, editors and year were not established: this sandbox cannot
     reach edtechbooks.org, and the commissioning brief named the authors and
     chapter number only. An absent field says "not established". -->

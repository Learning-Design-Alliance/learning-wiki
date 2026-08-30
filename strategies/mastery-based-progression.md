---
type: strategy
title: Mastery Based Progression
description: Learners advance to new content only after demonstrating a defined standard of proficiency on current content, with time varying and mastery held constant.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Mastery Based Progression

## Description
Mastery based progression holds the learning standard constant and lets time vary: learners move to new material only after demonstrating a defined proficiency level on prerequisite material, typically via criterion-referenced assessment. Instruction is organized into units with explicit mastery thresholds (e.g., 80–90% on parallel assessment forms), and learners who fall short receive corrective instruction and reassessment rather than moving on with gaps.

## Design Implications

Mastery learning rests on the assumption that most learners can reach high standards given enough time and appropriate correction; meta-analytic evidence shows positive but variable effects on achievement, strongest when mastery thresholds are paired with high-quality corrective feedback [Kulik et al. meta-analysis of mastery learning programs.](../claims/adaptive-learning-improves-outcomes.md) [+M]. The strategy depends on valid, aligned assessments — if the mastery check is weak, progression decisions are meaningless [Assessment that feeds forward into instruction improves achievement.](../claims/assessment-for-learning-improves-achievement.md) [+M]. Because prerequisites compound, mastery progression works best for hierarchically structured domains (mathematics, language mechanics, programming) where later skills genuinely depend on earlier ones.

### Context
#### Requirements
- A decomposition of the domain into sequenced units with clear prerequisite relationships
- Explicit, criterion-referenced mastery thresholds set before instruction begins
- Multiple parallel assessment forms so reassessment measures learning, not memory of the test
- Corrective instruction pathways — alternative explanations, targeted [Practice](../elements/practice.md), tutoring — distinct from the original presentation
- A system for tracking individual progress when learners move at different rates

#### Constraints
- Time costs are real: in fixed-duration courses, slower learners may cover less total content, and gains on covered material can come at the expense of breadth [-M]
- Poorly chosen thresholds create problems in both directions — too low certifies shallow learning; too high produces frustration, repeated failure experiences, and motivational damage for struggling learners [-M]
- Assessment-driven progression invites gaming: learners may optimize for passing the check rather than durable learning, especially when the same items are reused [-M]
- In ill-structured or non-hierarchical domains (open-ended writing, discussion-based inquiry), strict gating adds friction without clear benefit [~W]
- Group-based instruction becomes harder to schedule when learners diverge widely; implementations that ignore this drift often quietly revert to lockstep pacing [-W]

#### Implementation Variability
- **Unit-level gating** (classic Bloom mastery learning): whole units must be mastered before the next begins
- **Objective-level gating**: finer-grained, per-skill progression — the model used by adaptive platforms
- **Group-based mastery**: the class progresses together but individuals receive corrective instruction until reaching the standard before the unit test counts
- **Soft mastery**: progression is recommended but not enforced, with prerequisite gaps surfaced as warnings — common in self-paced online courses

### Target Learners
- Struggling and average learners benefit most; high achievers often show minimal gains because they already meet thresholds on first attempt [Mastery learning effects are largest for lower-performing students.](../claims/adaptive-learning-improves-outcomes.md) [+M]
- Learners in cumulative domains where unmastered prerequisites silently sabotage later units
- Less suitable as-is for learners who need exposure to breadth over depth within a fixed term, or who are demotivated by repeated reassessment

### Target Learning Goals
- Procedural and conceptual foundations in hierarchical domains (mathematics, science, language, programming)
- Automaticity on prerequisite skills that later tasks depend on
- Less well suited to goals emphasizing divergent production, creativity, or integrative judgment, where "mastery" is hard to criterion-reference

### Instructions
1. Decompose the domain into units and specify the prerequisite graph; identify which skills genuinely gate later work.
2. Set an explicit mastery criterion per unit (commonly 80–90%) and build at least two parallel assessment forms ([Assessment](../elements/assessment.md)).
3. Teach the unit, then assess. Learners below criterion receive **corrective instruction** — a different route than the original teaching, not a repeat ([Adaptive Mastery Learning](../elements/adaptive-mastery-learning.md)).
4. Reassess with a parallel form; only mastery-level performance counts toward progression.
5. Enrich learners who master content early with extension or peer-tutoring activities rather than idle time.
6. Periodically review thresholds and item quality against actual downstream performance in later units.

## Related Strategies
- [Competency-Based Assessment](../principles/competency-based-assessment.md) — the assessment philosophy that supplies valid mastery checks
- [Spaced Retrieval](spaced-retrieval.md) — counters the risk that mastery is demonstrated once and then forgotten; schedule re-checks of previously mastered units
- [Formative Feedback](formative-feedback.md) — corrective instruction depends on diagnosis, not just a score
- [Self-Paced Learning](../elements/self-paced-learning.md) — the pacing model mastery progression typically requires

## Patterns That Use This Strategy
- [Competency-Based Learning](../patterns/competency-based-learning.md) — mastery progression is the advancement mechanism
- [Adaptive Learning](../patterns/adaptive-learning.md) — platforms such as ALEKS and Khan Academy implement objective-level mastery gating algorithmically
- [Direct Instruction](../patterns/direct-instruction.md) — scripted programs gate passage through tracks on mastery of prerequisite skills

## Examples
- **Khan Academy** ([khanacademy.org](https://www.khanacademy.org)) — exercises tagged by skill; learners must reach "mastery" levels on prerequisite skills before the system recommends dependent skills.
- **ALEKS** (McGraw Hill) — knowledge-space model that gates new topics on demonstrated readiness, an objective-level variant of mastery progression.
- **Bloom's "Learning for Mastery"** (University of Chicago, 1968) — the original group-based formulation: unit tests, corrective activities, and parallel forms for reassessment.

## Key Sources
- Bloom, B. S. (1968). Learning for mastery. *Evaluation Comment, 1*(2), 1–12. UCLA Center for the Study of Evaluation.
- Kulik, C.-L. C., Kulik, J. A., & Bangert-Drowns, R. L. (1990). Effectiveness of mastery learning programs: A meta-analysis. *Review of Educational Research, 60*(2), 265–299. [doi:10.3102/00346543060002265](https://doi.org/10.3102/00346543060002265)
- Guskey, T. R. (2007). Closing achievement gaps: Revisiting Benjamin S. Bloom's "Learning for Mastery." *Journal of Advanced Academics, 19*(1), 8–31. [doi:10.4219/jaa-2007-704](https://doi.org/10.4219/jaa-2007-704)
- Anderson, L. W. (2000). *Increasing teacher effectiveness* (2nd ed.). UNESCO International Institute for Educational Planning.
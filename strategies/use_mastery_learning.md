---
type: strategy
title: Use Mastery Learning
description: Organize instruction so learners must demonstrate criterion-level mastery of each unit before advancing, with time varying and achievement held constant.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Use Mastery Learning

## Description
Mastery learning restructures the traditional instructional contract: instead of holding instructional time constant and letting achievement vary, it holds achievement constant at a criterion level and lets time and support vary. Learners study a unit, take a [formative assessment](../elements/assessment.md), and receive corrective instruction targeted at their specific gaps; they advance only after demonstrating the criterion, typically 80–90% correct.

## Design Implications

Mastery learning works because it prevents prerequisite gaps from compounding — later units in hierarchical subjects like mathematics depend on fluent mastery of earlier ones, and unmastered prerequisites create cascading failure [Mastery learning produces meaningful achievement gains, largest for lower-performing students.](https://doi.org/10.3102/00346543060003279) [+S]. The corrective-feedback cycle, not the gating alone, drives most of the effect: assessment must be followed by specific, actionable remediation rather than simple retesting [Assessment functions as learning only when feedback is actionable.](../claims/assessment-for-learning-improves-achievement.md) [+S].

### Context
#### Requirements
- Units sequenced by prerequisite structure, so mastery of unit *n* genuinely enables unit *n+1*
- A criterion-referenced assessment per unit, aligned to explicit objectives
- Parallel corrective activities (alternative explanations, [practice](../elements/practice.md) sets, peer tutoring) — not merely "study it again"
- A system for tracking individual progress across units ([Adaptive Mastery Learning](../elements/adaptive-mastery-learning.md) automates this)

#### Constraints
- Time requirements diverge sharply; without flexible scheduling, slower learners are either rushed or stigmatized [-M]
- Gating on mastery can demotivate learners who repeatedly fail the criterion if corrective instruction is weak or the retake feels punitive [~M]
- Poorly suited to content without strong prerequisite hierarchies (e.g., open-ended discussion, creative work), where "mastery" is hard to define and gating adds friction without benefit [~W]
- Advanced learners held at group pace lose challenge; enrichment or acceleration tracks are needed to avoid disengagement [-M]

#### Implementation Variability
- **Group-based (Bloom's original)**: whole class moves through units together; non-masters attend corrective sessions, then retake a parallel form
- **Individually paced**: learners progress through a linear unit sequence at their own rate (Keller's Personalized System of Instruction)
- **Technology-mediated**: platforms adapt item difficulty and progression rules algorithmically ([Adaptive Mastery Learning](../elements/adaptive-mastery-learning.md)), often using continuous estimation of mastery rather than discrete unit tests
- **Hybrid**: mastery gates on core prerequisites, with flexible pacing on enrichment content

### Target Learners
- Struggling and lower-achieving learners benefit most; the approach narrows achievement gaps by guaranteeing prerequisites before advancement [Mastery learning gains are largest for lower third of achievers.](https://doi.org/10.3102/00346543060003279) [+S]
- Learners in hierarchical domains (mathematics, science, language grammar, programming) where gaps compound
- Less beneficial for high-aptitude learners under uniform pacing, who complete criteria quickly and need acceleration or enrichment [~M]

### Target Learning Goals
- Foundational knowledge and skills that later learning depends on
- Procedural fluency to a reliable criterion ([automaticity](../elements/automaticity.md))
- Competency certification where a defensible standard of "ready" is required ([competency-based assessment](../principles/competency-based-assessment.md))

### Instructions
1. Decompose the domain into a prerequisite-ordered sequence of small units with explicit, observable objectives.
2. Write a criterion assessment for each unit (typically 80–90% mastery threshold) plus a parallel alternate form for retakes.
3. Teach the unit, then administer the [assessment](../elements/assessment.md) diagnostically.
4. For non-masters, assign targeted corrective instruction matched to specific error patterns — alternative [analogies](../elements/analogies.md), re-teaching, peer study, or additional [practice](../elements/practice.md) — not a repeat of the original presentation.
5. Retest with the parallel form; on mastery, advance. Schedule enrichment for learners who master early.
6. Where scale demands it, delegate pacing and gating logic to an [adaptive learning](../principles/adaptive-learning.md) system.

## Related Strategies
- **Use spaced practice** — mastery criteria should be re-checked over time; passing once does not guarantee retention
- **Use formative assessment cycles** — mastery learning is essentially formative assessment with a gating rule attached

## Examples
- **Bloom's "Learning for Mastery" (1968)** — the original group-based model: teach, assess, correct, retest per unit.
- **Keller Plan / Personalized System of Instruction** — self-paced university courses with unit tests and proctors; widely used in physics and psychology in the 1970s.
- **[Khan Academy](https://www.khanacademy.org)** — course progress is gated by "mastery" levels per skill; learners must pass checks at each level before advancing, with hints and videos serving as corrective instruction.
- **[ALEKS](https://www.aleks.com)** — knowledge-space model that gates new topics on demonstrated mastery of prerequisites, used widely in developmental mathematics.
- **City Charter schools' math programs** — blended rotation models combining teacher-led instruction with software-managed mastery progression.

## Key Sources
- Bloom, B. S. (1968). Learning for mastery. *Evaluation Comment, 1*(2), 1–12.
- Kulik, C.-L. C., Kulik, J. A., & Bangert-Drowns, R. L. (1990). Effectiveness of mastery learning programs: A meta-analysis. *Review of Educational Research, 60*(2), 265–299. [doi:10.3102/00346543060002265](https://doi.org/10.3102/00346543060002265)
- Guskey, T. R. (2007). Closing achievement gaps: Revisiting Benjamin S. Bloom's "Learning for Mastery." *Journal of Advanced Academics, 19*(1), 8–31. [doi:10.4219/jaa-2007-704](https://doi.org/10.4219/jaa-2007-704)
- Keller, F. S. (1968). Good-bye, teacher…. *Journal of Applied Behavior Analysis, 1*(1), 79–89. [doi:10.1901/jaba.1968.1-79](https://doi.org/10.1901/jaba.1968.1-79)
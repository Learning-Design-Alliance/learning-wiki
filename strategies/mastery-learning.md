---
type: strategy
id: mastery-learning
aliases: [use_mastery_learning]
title: Mastery Learning
description: Learners must demonstrate a defined level of competence on each unit before progressing, with time varying and achievement held constant.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Mastery Learning

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (2 for, 1 mixed) · 7 studies (3 review, 2 quant-synthesis, 1 causal, 1 theoretical), `q1`–`q4` · 2 of 7 report an effect size

## Description
Mastery learning restructures pacing so that achievement is held constant and time is allowed to vary: learners study a unit, take a formative assessment, receive corrective instruction on what they missed, and only advance once they reach a preset criterion (typically 80–90% correct). The cycle of instruction → assessment → corrective feedback → reassessment repeats until mastery is demonstrated.

## Design Implications

Mastery learning operationalizes the assumption that most learners can master most objectives given sufficient time and appropriate correction; meta-analytic evidence shows positive effects on achievement, strongest when mastery criteria are paired with well-designed corrective instruction [~M]. Its power comes from closing the loop: assessment is not terminal but diagnostic, and [Feedback](../elements/feedback.md) targeted at specific gaps drives the corrective cycle [Feedback is most effective at task and process levels.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S]. Because success experiences accumulate, mastery approaches also build confidence and persistence [Self-efficacy predicts academic persistence.](../claims/self-efficacy-predicts-academic-persistence.md) [+M].

### Context
#### Requirements
- Objectives broken into small, hierarchically ordered units with explicit mastery criteria
- Parallel or repeated [Formative Assessment](../elements/formative-assessment.md) instruments so reassessment measures the same objectives without simple memorization of items
- Corrective instruction that is genuinely *alternative* — different representations, [Practice](../elements/practice.md) formats, or peer tutoring — not merely repeating the same explanation
- A system for tracking individual progress when learners move at different rates
- Units sequenced by prerequisite structure, so mastery of unit *n* genuinely enables unit *n+1*
- A criterion-referenced assessment per unit, aligned to explicit objectives
- A system for tracking individual progress across units ([Adaptive Mastery Learning](../elements/adaptive-mastery-learning.md) automates this)

#### Constraints
- Time costs are real: covering material to mastery reduces the amount of content covered, which can hurt performance on breadth-oriented assessments [~M]
- Requiring mastery of *every* objective imposes heavy time demands and can produce diminishing returns for peripheral content; the criterion level and unit granularity must be chosen carefully [~M]
- Repeated failure to reach criterion without effective corrective instruction demoralizes learners rather than motivating them [-M]
- For learners with high prior knowledge, uniform mastery requirements on known material create redundancy and boredom [The expertise-reversal effect: guidance that helps novices can hinder more knowledgeable learners.](../claims/expertise-reversal-effect.md) [~M]
- Time requirements diverge sharply; without flexible scheduling, slower learners are either rushed or stigmatized [-M]
- Gating on mastery can demotivate learners who repeatedly fail the criterion if corrective instruction is weak or the retake feels punitive [~M]
- Poorly suited to content without strong prerequisite hierarchies (e.g., open-ended discussion, creative work), where "mastery" is hard to define and gating adds friction without benefit [~W]
- Advanced learners held at group pace lose challenge; enrichment or acceleration tracks are needed to avoid disengagement [-M]

#### Implementation Variability
- **Group-based (Bloom)**: whole class progresses through units together; non-masters receive corrective activities in small groups or peer sessions, then retake an alternate assessment
- **Individually paced (Keller's PSI)**: self-paced written materials with proctored mastery tests and proctors; maximal individualization, high setup cost
- **Technology-mediated**: adaptive platforms (e.g., Khan Academy mastery tracking, ALEKS) automate assessment, prescription, and reassessment loops
- **Threshold models**: mastery required only for foundational, prerequisite objectives, with later units graded conventionally — a pragmatic compromise
- **Group-based (Bloom's original)**: whole class moves through units together; non-masters attend corrective sessions, then retake a parallel form
- **Individually paced**: learners progress through a linear unit sequence at their own rate (Keller's Personalized System of Instruction)
- **Technology-mediated**: platforms adapt item difficulty and progression rules algorithmically ([Adaptive Mastery Learning](../elements/adaptive-mastery-learning.md)), often using continuous estimation of mastery rather than discrete unit tests
- **Hybrid**: mastery gates on core prerequisites, with flexible pacing on enrichment content

### Target Learners
- Struggling learners and those with gaps in prerequisite knowledge, who benefit most from time-to-maturity rather than fixed pacing [+M]
- Learners in cumulative domains (mathematics, language mechanics, procedural skills) where early gaps compound
- High-achievers may stagnate waiting for peers in group-based implementations; pair with enrichment or [Adaptive Difficulty](../elements/adaptive-difficulty.md) [~M]
- Struggling and lower-achieving learners benefit most; the approach narrows achievement gaps by guaranteeing prerequisites before advancement [Mastery learning gains are largest for lower third of achievers.](https://doi.org/10.3102/00346543060003279) [+S]
- Learners in hierarchical domains (mathematics, science, language grammar, programming) where gaps compound
- Less beneficial for high-aptitude learners under uniform pacing, who complete criteria quickly and need acceleration or enrichment [~M]

### Target Learning Goals
- Foundational knowledge and skills that later learning depends on (prerequisite hierarchies)
- Procedural fluency and accuracy-based objectives with clear correctness criteria
- Less suited to divergent, creative, or ill-structured goals where "mastery" cannot be operationalized as a criterion score
- Procedural fluency to a reliable criterion ([automaticity](../elements/automaticity.md))
- Competency certification where a defensible standard of "ready" is required ([competency-based assessment](../principles/competency-based-assessment.md))

### Instructions
1. Decompose the course into small units ordered by prerequisite structure; define an explicit mastery criterion for each ([Clear Structure](../principles/clear-structure.md)).
2. Teach the unit, then administer a formative assessment aligned to the objectives ([Assess Performance](../elements/assess-performance.md)).
3. For non-masters, provide corrective instruction that differs in form from the original teaching — alternative examples, peer tutoring, targeted [Practice](../elements/practice.md) — rather than repetition ([Feedback](../elements/feedback.md)).
4. Reassess with a parallel instrument; learners who reach criterion move on, others cycle again.
5. Use mastery data to trigger [Adaptive Mastery Learning](../elements/adaptive-mastery-learning.md) pathways where platform support exists.

## Related Strategies

- [Competency-Based Learning](competency-based-learning.md) — the broader institutional model; mastery learning is its instructional engine
- [Direct Instruction](direct-instruction.md) — often combined, since tightly scripted lessons pair well with criterion-referenced checks
- [Flipped Classroom](flipped-classroom.md) — frees class time for the corrective-practice cycle that mastery requires
- [Advance register-graded sequencing, distributed repetition and adaptive pacing as hypotheses for classroom testing](register-graded-distributed-repetition-hypotheses.md)
- [Exit students from tutoring once they consistently read at the average level for their grade](exit-tutoring-at-grade-level-consistency.md)
- **Use spaced practice** — mastery criteria should be re-checked over time; passing once does not guarantee retention
- **Use formative assessment cycles** — mastery learning is essentially formative assessment with a gating rule attached

## Examples
- **Bloom's "Learning for Mastery" (LFM)** — the classic group-based implementation: teach, check, correct in small groups, reassess with alternate forms.
- **Keller's Personalized System of Instruction (PSI)** — used widely in university psychology courses in the 1970s; self-pacing with mastery tests and proctors.
- **[Khan Academy](https://www.khanacademy.org)** — course-level mastery system where exercises, quizzes, and unit tests feed a per-skill mastery status that gates course completion.
- **[ALEKS](https://www.aleks.com)** — knowledge-space model that assesses what a learner is ready to master next and requires demonstrated mastery before unlocking new topics.
- **Bloom's "Learning for Mastery" (1968)** — the original group-based model: teach, assess, correct, retest per unit.
- **Keller Plan / Personalized System of Instruction** — self-paced university courses with unit tests and proctors; widely used in physics and psychology in the 1970s.
- **[Khan Academy](https://www.khanacademy.org)** — course progress is gated by "mastery" levels per skill; learners must pass checks at each level before advancing, with hints and videos serving as corrective instruction.
- **[ALEKS](https://www.aleks.com)** — knowledge-space model that gates new topics on demonstrated mastery of prerequisites, used widely in developmental mathematics.
- **City Charter schools' math programs** — blended rotation models combining teacher-led instruction with software-managed mastery progression.

## Key Sources
- Bloom, B. S. (1968). Learning for mastery. *Evaluation Comment, 1*(2), 1–12.
- Kulik, C.-L. C., Kulik, J. A., & Bangert-Drowns, R. L. (1990). Effectiveness of mastery learning programs: A meta-analysis. *Review of Educational Research, 60*(2), 265–299. [doi:10.3102/00346543060002265](https://doi.org/10.3102/00346543060002265)
- Guskey, T. R. (2007). Closing achievement gaps: Revisiting Benjamin S. Bloom's "Learning for Mastery." *Journal of Advanced Academics, 19*(1), 8–31. [doi:10.4219/jaa-2007-704](https://doi.org/10.4219/jaa-2007-704)
- Kulik, J. A., Kulik, C.-L. C., & Cohen, P. A. (1979). A meta-analysis of outcome studies of Keller's Personalized System of Instruction. *American Psychologist, 34*(4), 307–318. [doi:10.1037/0003-066X.34.4.307](https://doi.org/10.1037/0003-066X.34.4.307)
- Keller, F. S. (1968). Good-bye, teacher…. *Journal of Applied Behavior Analysis, 1*(1), 79–89. [doi:10.1901/jaba.1968.1-79](https://doi.org/10.1901/jaba.1968.1-79)

<!-- merged 2026-10-13 from strategies/use_mastery_learning ("Use Mastery Learning"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Use Mastery Learning

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 3 studies (2 quant-synthesis, 1 review), `q2`–`q3` · 2 of 3 report an effect size

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
-->

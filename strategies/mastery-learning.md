---
type: strategy
title: Mastery Learning
description: Learners must demonstrate a defined level of competence on each unit before progressing, with time varying and achievement held constant.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Mastery Learning

> **Strategy** · [All strategies](index.md)

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

#### Constraints
- Time costs are real: covering material to mastery reduces the amount of content covered, which can hurt performance on breadth-oriented assessments [~M]
- Requiring mastery of *every* objective imposes heavy time demands and can produce diminishing returns for peripheral content; the criterion level and unit granularity must be chosen carefully [~M]
- Repeated failure to reach criterion without effective corrective instruction demoralizes learners rather than motivating them [-M]
- For learners with high prior knowledge, uniform mastery requirements on known material create redundancy and boredom [The expertise-reversal effect: guidance that helps novices can hinder more knowledgeable learners.](../claims/expertise-reversal-effect.md) [~M]

#### Implementation Variability
- **Group-based (Bloom)**: whole class progresses through units together; non-masters receive corrective activities in small groups or peer sessions, then retake an alternate assessment
- **Individually paced (Keller's PSI)**: self-paced written materials with proctored mastery tests and proctors; maximal individualization, high setup cost
- **Technology-mediated**: adaptive platforms (e.g., Khan Academy mastery tracking, ALEKS) automate assessment, prescription, and reassessment loops
- **Threshold models**: mastery required only for foundational, prerequisite objectives, with later units graded conventionally — a pragmatic compromise

### Target Learners
- Struggling learners and those with gaps in prerequisite knowledge, who benefit most from time-to-maturity rather than fixed pacing [+M]
- Learners in cumulative domains (mathematics, language mechanics, procedural skills) where early gaps compound
- High-achievers may stagnate waiting for peers in group-based implementations; pair with enrichment or [Adaptive Difficulty](../elements/adaptive-difficulty.md) [~M]

### Target Learning Goals
- Foundational knowledge and skills that later learning depends on (prerequisite hierarchies)
- Procedural fluency and accuracy-based objectives with clear correctness criteria
- Less suited to divergent, creative, or ill-structured goals where "mastery" cannot be operationalized as a criterion score

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

## Examples
- **Bloom's "Learning for Mastery" (LFM)** — the classic group-based implementation: teach, check, correct in small groups, reassess with alternate forms.
- **Keller's Personalized System of Instruction (PSI)** — used widely in university psychology courses in the 1970s; self-pacing with mastery tests and proctors.
- **[Khan Academy](https://www.khanacademy.org)** — course-level mastery system where exercises, quizzes, and unit tests feed a per-skill mastery status that gates course completion.
- **[ALEKS](https://www.aleks.com)** — knowledge-space model that assesses what a learner is ready to master next and requires demonstrated mastery before unlocking new topics.

## Key Sources
- Bloom, B. S. (1968). Learning for mastery. *Evaluation Comment, 1*(2), 1–12.
- Kulik, C.-L. C., Kulik, J. A., & Bangert-Drowns, R. L. (1990). Effectiveness of mastery learning programs: A meta-analysis. *Review of Educational Research, 60*(2), 265–299. [doi:10.3102/00346543060002265](https://doi.org/10.3102/00346543060002265)
- Guskey, T. R. (2007). Closing achievement gaps: Revisiting Benjamin S. Bloom's "Learning for Mastery." *Journal of Advanced Academics, 19*(1), 8–31. [doi:10.4219/jaa-2007-704](https://doi.org/10.4219/jaa-2007-704)
- Kulik, J. A., Kulik, C.-L. C., & Cohen, P. A. (1979). A meta-analysis of outcome studies of Keller's Personalized System of Instruction. *American Psychologist, 34*(4), 307–318. [doi:10.1037/0003-066X.34.4.307](https://doi.org/10.1037/0003-066X.34.4.307)

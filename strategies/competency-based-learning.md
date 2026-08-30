---
type: strategy
title: Competency Based Learning
description: Learners advance by demonstrating mastery of defined competencies rather than by accumulating seat time, with assessment and pacing tied to evidence of proficiency.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Competency Based Learning

## Description
Competency based learning (CBL) organizes instruction around explicit, measurable competencies — statements of what learners must know and be able to do — and allows progression only when learners demonstrate mastery of each one. Time becomes the variable and learning the constant: students receive differentiated support and multiple assessment opportunities until they reach the proficiency standard, rather than moving on with the cohort regardless of attainment.

## Design Implications

CBL operationalizes [mastery learning](../theories/behaviorism.md) logic: holding achievement standards constant while varying time and support produces substantially better outcomes than holding time constant and letting achievement vary [Bloom's mastery learning model shows strong effects when corrective instruction follows formative assessment.](../claims/assessment-for-learning-improves-achievement.md) [+S]. The design burden shifts to defining competencies precisely and building rich formative assessment — without high-quality evidence of current proficiency, "mastery" decisions collapse into teacher judgment or re-testing of trivial recall.

### Context
#### Requirements
- A competency framework: decomposed, observable, assessable statements of proficiency, ideally with rubrics describing performance levels
- Multiple, varied assessment opportunities per competency ([Assessment](../elements/assessment.md)), including performance-based tasks, not just tests
- Formative feedback loops that tell learners *what to do next*, not just a score [Feedback most effective at task and process levels.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S]
- Flexible pacing structures and re-learning pathways (tutoring, alternative materials, [Practice](../elements/practice.md)) for learners who have not yet demonstrated mastery
- Data systems that track per-competency status across courses, since a single grade cannot represent partial mastery

#### Constraints
- Poorly specified competencies (vague, unobservable, or too granular) fragment learning into checklist behavior and lose coherence [-M]
- Fully self-paced models can reduce motivation for learners who lack self-regulation skills; cohort structures and deadlines provide needed external structure [~M]
- Assessment capacity is the bottleneck: without enough assessment occasions, learners queue behind grading and pacing benefits disappear [-M]
- Overly narrow competency decomposition can strip away integrative abilities (synthesis, judgment) that resist itemized assessment [-W]

#### Implementation Variability
- **Fully asynchronous mastery models** (e.g., Western Governors University): learners test out of competencies at any time
- **Classroom hybrid models** (e.g., Lindsay Unified School District): shared cohort with per-competency progression and flexible grouping
- **Credit-by-examination / prior learning assessment**: CBL applied only at entry points for adult learners
- **Professional education variants** (e.g., competency-based medical education): time-fixed programs with competency gates at transition points, trading pure pacing flexibility for safety-critical assurance

### Target Learners
- Adult and working learners who bring prior experience and benefit from credit for existing proficiency [+M]
- Learners who have historically been failed by time-based pacing — those who need more time, or who are held back after already mastering content [+M]
- Less suitable as pure self-pacing for young or novice learners with weak self-regulation; these learners need embedded structure and check-ins [~M]

### Target Learning Goals
- Well-defined procedural and knowledge outcomes that can be stated as observable performance
- Progressive skill building where prerequisites genuinely gate later learning (e.g., mathematics, technical training)
- Less well suited to emergent, discursive, or disposition-oriented goals where "mastery" is contested or developmental [~W]

### Instructions
1. Define competencies by unpacking terminal outcomes into assessable components, checking that each is observable and criterion-referenced ([Clear Structure](../principles/clear-structure.md))
2. Build or select a [Competency-Based Assessment](../principles/competency-based-assessment.md) system: rubrics, performance tasks, and cut scores defining mastery
3. Sequence learning tasks so each targets one or few competencies, with [Scaffolding](../principles/scaffolding.md) faded as proficiency grows [Fading support promotes transfer of responsibility.](../claims/fading-support-promotes-transfer-of-responsibility.md) [+M]
4. Run frequent formative checks; route non-mastery learners to targeted corrective activities before re-assessment ([Assessment for Learning](../principles/assessment-for-learning.md))
5. Certify mastery and advance the learner; record per-competency status in a dashboard visible to learner and instructor
6. Periodically audit the competency framework for gaps in integrative or higher-order outcomes

## Related Strategies
- [Mastery Learning](../patterns/competency-based-learning.md) — the pattern-level treatment; CBL is its institutionalized, credential-bearing form
- [Adaptive Mastery Learning](../elements/adaptive-mastery-learning.md) — technology-delivered variant where the system routes learners based on assessment results
- [Direct Instruction](../patterns/direct-instruction.md) — a common instructional engine inside CBL corrective loops
- [Flipped Classroom](../patterns/flipped-classroom.md) — frees contact time for the differentiated practice CBL requires

## Examples
- **[Western Governors University](https://www.wgu.edu)** — fully competency-based online degrees; students progress by passing objective and performance assessments at their own pace.
- **[Lindsay Unified School District](https://www.lindsay.k12.ca.us)** — a K-12 performance-based system where learners advance on demonstrated performance levels rather than grade levels.
- **Competency-based medical education (CBME)** — residency programs using Entrustable Professional Activities and milestone frameworks (ACGME) to gate progression on demonstrated competence.

## Key Sources
- Bloom, B. S. (1968). Learning for mastery. *Evaluation Comment, 1*(2), 1–12. UCLA Center for the Study of Evaluation.
- Guskey, T. R. (2007). Closing achievement gaps: Revisiting Benjamin S. Bloom's "Learning for Mastery." *Journal of Advanced Academics, 19*(1), 8–31. [doi:10.4219/jaa-2007-704](https://doi.org/10.4219/jaa-2007-704)
- Spady, W. G. (1994). *Outcome-Based Education: Critical Issues and Answers.* American Association of School Administrators.
- Klein-Collins, R. (2012). *Competency-Based Degree Programs in the U.S.* Council for Adult and Experiential Learning. [https://www.cael.org](https://www.cael.org)
- Frank, J. R., et al. (2010). Competency-based medical education: Theory to practice. *Medical Teacher, 32*(8), 638–645. [doi:10.3109/0142159X.2010.501190](https://doi.org/10.3109/0142159X.2010.501190)
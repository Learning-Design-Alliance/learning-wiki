---
type: strategy
title: Standards-Based Grading
description: Shift from arbitrary points and percentages to evaluating students on mastery of specific learning standards, making expectations clear and grades meaningful.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Standards-Based Grading

## Description
Standards-based grading (SBG) replaces point-accumulation and percentage systems with evaluation against explicitly defined learning standards. Each grade reports what a student knows and can do relative to a standard — often on a proficiency scale — rather than averaging behavior, effort, homework compliance, and early failures into a single number. Reassessment is typically permitted, so the grade reflects eventual mastery rather than the pace at which it was reached.

## Design Implications

SBG aligns grading with [Assessment for Learning](../principles/assessment-for-learning.md): grades become information about mastery rather than rewards and sanctions, which shifts student attention from point-chasing to learning [~M]. Because grades map to specific standards, they generate actionable [feedback](../elements/assessment.md) at the task and process level — the feedback conditions most strongly associated with achievement gains [Feedback is most effective at the task and process levels.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S]. SBG is closely related to [Competency-Based Assessment](../principles/competency-based-assessment.md) and functions as the reporting layer for [Competency-Based Learning](../patterns/competency-based-learning.md).

### Context
#### Requirements
- Clearly defined, learner-facing standards or learning targets, ideally in student-friendly language
- Rubrics or proficiency scales that describe performance levels for each standard
- Assessments that genuinely align to the standards (validity of the mapping is the whole game)
- A reassessment policy and a reporting system capable of communicating per-standard proficiency
- Significant teacher training and calibration — common rubrics and moderation across sections [Requires significant training to implement consistently]

#### Constraints
- Grades become less comparable across schools and less familiar to parents and admissions offices accustomed to traditional GPA conventions [~M]
- Without teacher calibration, proficiency judgments drift toward subjective inconsistency, undermining the accuracy the system is meant to provide [-M]
- Per-standard reporting multiplies the grading workload; teachers who adopt SBG without reducing the number of standards tracked tend to revert [-W]
- Reducing D/F rates does not by itself indicate learning gains — in reported implementations, D's and F's fell but so did A's, suggesting grade compression rather than clear mastery signals [~W]
- Poorly designed reassessment policies can produce gaming (students retaking without remediation) or grade inflation in later reporting periods [-W]

#### Implementation Variability
- Full conversion (per-standard report cards, no single letter grade) vs. hybrid (SBG inside a traditional gradebook)
- Proficiency scales: 4-point mastery scales, binary proficient/not-yet, or rubric-based narrative reporting
- Standards-referenced (grades report standards but a summary grade is still required) vs. standards-based (grades report standards only)
- Retake policies: unlimited with full credit, capped with remediation required, or averaging attempts

### Target Learners
- Middle and high school students, where traditional point systems most strongly conflate compliance with achievement [~M]
- Students who learn at uneven paces — reassessment lets late mastery count, supporting mastery orientation rather than punishing early failure [+W]
- High-achieving students accustomed to earning A's through compliance may initially experience grade deflation and motivational friction [~W]

### Target Learning Goals
- Mastery of well-defined knowledge and skill standards (procedural and conceptual targets)
- Accurate self-assessment: per-standard reporting helps students see *which* competencies need work, supporting self-regulated monitoring
- Less suited to goals that resist decomposition into discrete standards (integrated performance, creativity, disposition)

### Instructions
1. **[State objectives](../elements/assessment.md)** — Define a small set of priority standards per course; write each as an observable learning target with a proficiency scale.
2. **Design aligned assessments** — Build assessments that map items to standards so each score reports mastery of one target, not a blended average.
3. **[Assess performance](../elements/assess-performance.md)** — Score against the scale, not against points; separate academic achievement from behavior, effort, and attendance in reporting.
4. **Provide feedback** — Pair each proficiency score with task- and process-level feedback [Feedback is most effective at the task and process levels.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S]; use [Formative Assessment](../patterns/formative-assessment.md) cycles between scored assessments.
5. **Allow reassessment** — Permit retakes after remediation so the final grade reflects eventual mastery; cap or structure retakes to prevent gaming.
6. **Report per standard** — Communicate proficiency by standard to students and families; calibrate scoring with colleagues through moderation of student work.

## Related Strategies
- [Mastery Learning](mastery-learning.md) — SBG is the grading counterpart of mastery-based pacing; both hold time variable and achievement constant
- [Formative Assessment](formative-assessment.md) — supplies the low-stakes evidence and feedback loop between scored assessments
- [Ungrading](ungrading.md) — a more radical variant that removes grades entirely in favor of reflective self-assessment

## Examples
- **High school physics SBG conversion** — A widely cited implementation replaced percentage grades with standards scores (e.g., "Graphs motion — 3/4"); D/F rates declined, but A rates also declined, showing grade redistribution rather than uniform inflation.
- **[Marzano Academies / Marzano proficiency scales](https://www.marzanocenter.com)** — Published proficiency-scale frameworks and report card templates used at scale in standards-based districts.
- **[ActiveGrade / JumpRope](https://www.jumpro.pe)** — Standards-based gradebooks that track per-standard mastery and support reassessment workflows.

## Key Sources
- Guskey, T. R., & Swan, G. M. (2011). *Developing standards-based report cards.* Corwin Press.
- Brookhart, S. M. (2013). *How to create and use rubrics for formative assessment and grading.* ASCD.
- Hattie, J., & Timperley, H. (2007). The power of feedback. *Review of Educational Research, 77*(1), 81–112. [doi:10.3102/003465430298487](https://doi.org/10.3102/003465430298487)
- Black, P., & Wiliam, D. (1998). Assessment and classroom learning. *Assessment in Education: Principles, Policy & Practice, 5*(1), 7–74. [doi:10.1080/0969595980050102](https://doi.org/10.1080/0969595980050102)
- Guskey, T. R. (2011). Five obstacles to grading reform. *Educational Leadership, 69*(3), 16–21.
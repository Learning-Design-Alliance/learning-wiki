---
type: pattern
id: mastery-learning
aliases: [mastery-learning-formative-corrective-cycle]
title: Mastery Learning
description: "A reusable gate-correct-recheck policy for cumulative units: elicit a criterion-referenced response, interpret a shortfall, give responsive correction and recheck on a parallel task before advancing, with time, attempts and the outcome horizon stated."
canonical: true
status: review
generated:
  by: claude/unspecified
  at: 2026-10-01
sources:
  - id: kulik-1990
    resource: "https://doi.org/10.3102/00346543060002265"
    title: "Kulik, C. L. C., Kulik, J. A., & Bangert-Drowns, R. L. (1990). Effectiveness of mastery learning programs: A meta-analysis. *Review of Educational Research, 60*(2), 265-299"
    author: "Kulik, C. L. C., Kulik, J. A., & Bangert-Drowns, R. L"
  - id: bonczar-1983
    resource: "https://eric.ed.gov/?id=ED238505"
    title: "Bonczar, Thomas P., & Easton, John Q. (1983). The Effect of Mastery Learning on Student Achievement. https://eric.ed.gov/?id=ED238505"
    author: "Bonczar, Thomas P., & Easton, John Q"
  - id: guskey-1982
    resource: "https://eric.ed.gov/?id=ED213702"
    title: "Guskey, Thomas R., et al. (1982). The Effectiveness of Mastery Learning Strategies in Undergraduate Education Courses. Paper presented at the Annual Meeting of the American Educational Research Association, New York. https://eric.ed.gov/?id=ED213702"
    author: Guskey, Thomas R., et al
author: Bloom / mastery learning tradition
grain_size: unit
---

# Mastery Learning

> **Pattern** · [All patterns](index.md)
> **Evidence** · 9 claims (4 for, 5 mixed) · 16 studies (6 quant-synthesis, 3 causal, 3 review, 2 theoretical, 1 associational, 1 qualitative), `q1`–`q4` · 4 of 16 report an effect size · 5 claims rest on one study

## Description and scope

A reusable policy for organising cumulative units around a stated criterion: each unit ends in a check, a response below the criterion leads to corrective work and a further, comparable check, and advancement depends on that response rather than on the calendar alone. It instantiates the [conditional principle](../principles/mastery-learning.md). The programme configurations in the studies below are evidence; the response-dependent policy on this page is an **untested design proposal**. Use it to collect better evidence about learners' responses, not to certify that a learner "has mastered" a unit.

## Inputs: establish the design brief

| Field | Record or elicit |
|---|---|
| Learner and starting observation | Responses on the first unit check and on any prerequisite probe; attempt history; errors and their kind. Use `expertise`, `age` and `population_band` values where known, and record unknowns as unknown. |
| Context and activities | Setting (`classroom`, `online-self-paced`, `online-instructor-led`, `workplace-clinical`), unit length, who delivers correction (teacher, peer, software), time available for reattempts, aids permitted on checks, and what learners who pass do meanwhile. |
| Learner-valued goal | Ask what the learner wants from the course and on what timescale. Record divergence from the unit criterion, and the learner's tolerance for extra time, as observations. |
| Designer objective | The capability each unit's check stands for, its knowledge type (`procedure`, `principle`, `complex-skill`, ...), which later units depend on it, and the cut score with its justification. |
| Outcome | Unit-check performance, the course or programme examination (`general-achievement`), delayed retention or transfer if targeted, completion (`persistence`) and time to criterion (`learning-time`), each with its instrument and horizon. |

A request to "make sure students master the material" does not specify these. Ask for them before prescribing a cut score, a number of attempts or an expected gain. Check that the unit check samples the capability the next unit needs and that a parallel form exists before relying on a recheck.

## Sequence and conditional policy

1. **State the criterion and the check.** Name the capability, the representative task, the cut score, permitted aids, and a parallel form for rechecks. Tell learners what the criterion is.
2. **Teach and practise the unit.** Record what instruction and practice each learner actually received.
3. **Elicit a unit-check response.** Score it against the criterion and record the reasoning or error, not only the score.
4. **Interpret a shortfall provisionally.** Use the table below to choose a probe that separates explanations; record which remain.
5. **Correct responsively.** Change the form of instruction to address what the response showed, rather than replaying the unit. Record the correction delivered and its time.
6. **Recheck on a parallel task.** Change surface features and at least one relevant condition. Record the attempt number.
7. **Decide on advancement, with the time limit explicit.** Advance on criterion, or by the agreed rule when the attempt or time limit is reached, recording any unresolved gap so the next unit's first task can re-probe it.
8. **Reobserve later.** Check the earlier capability at the start of the dependent unit or at the stated delayed horizon.

| Observation | Discriminating probe | Proposed action, with its uncertainty |
|---|---|---|
| Below criterion on the first check | A short prerequisite probe set apart from the unit task; one item on the same relation in another representation; ask the learner to explain one wrong step. | If the prerequisite fails, correct it first; if only the unit relation fails, correct that with a different explanation or example; if only one representation fails, address access or representation. None of these is a validated diagnosis. |
| Passes only on a recheck that repeats items | Give a parallel form with a changed relevant condition. | Treat item recognition as a live explanation until the parallel form is passed; do not count a repeated-item pass as meeting the criterion. |
| Passes the gate, then fails the next unit's first task | Compare the failed step with what the previous check sampled; re-probe the earlier capability. | Widen the previous check or add a bridging task; a narrow check, forgetting and a genuinely new demand each lead to a different action, and one observation does not separate them. |
| Repeated failures after correction | Change the correction's form and observe; probe an earlier prerequisite; ask about purpose and barriers. | Offer a different route (one-to-one or small-group help, a worked example, a smaller step) or revisit the cut score with evidence from other learners; do not keep cycling the same material. |
| Falling participation or time running out | Record time and attempts per unit; ask what the learner wants from the course. | Negotiate the limit and the advancement rule in the open; a capped number of attempts with a recorded gap may serve the learner's goal better than an unbounded gate. |

## Choosing configurations from evidence

- **Whether to gate at all.** [Mastery learning programmes, 108 controlled evaluations](../claims/mastery-learning-improves-outcomes.md) [+M] report positive effects on examination performance against conventionally paced instruction at college, high-school and upper-elementary levels, apparently stronger for weaker students and varying with the mastery procedure, design and content. The same synthesis reports possibly more time on instructional tasks and, for self-paced college programmes, often reduced completion. Abstract only; no pooled size recorded. It supports a gate-and-correct configuration as a candidate, and puts time and completion in the brief as outcomes to watch, not side issues.
- **What the correction should be.** [Contingent versus fixed support](../claims/contingent-scaffolding-improves-learning.md) [+M]: in one-to-one long-division tutoring with fourth and fifth graders (n = 8 per condition), support adjusted to each response beat fixed or no support at immediate and one-month tests; a dynamic-assessment synthesis ranks explicit strategy training above contingent scaffolding. Choose correction that responds to the response, and consider explicit strategy instruction as an alternative; the one-to-one evidence does not show this works in a whole class. Not settled against its sources.
- **How the check feeds action.** [Formative assessment syntheses](../claims/assessment-for-learning-improves-achievement.md) [+M] report small positive overall effects in K-12 (d = .29; .20 in another synthesis), with larger estimates where self-assessment was supported. These are configuration comparisons across studies with no common horizon; they do not predict an effect for a new course.
- **Software-delivered pacing.** [Intelligent tutoring meta-analyses](../claims/adaptive-learning-improves-outcomes.md) [~M] associate tutoring systems with higher achievement than teacher-led large-group instruction, other computer-based instruction and textbooks, but report no advantage over individual human tutoring or small-group instruction, and gains that depend on whether tests were locally developed or standardised. If a system delivers the gate, compare it with human small-group correction, not only with whole-class pacing, and measure on an instrument independent of the system. The claim page words one entry causally ("produced") where its own description says "associated with"; read it as an association.
- **Section-level comparisons.** [Earned credit in mastery and non-mastery sections](../claims/mastery-learning-higher-earned-credit-rates.md) [~W]: one college system's records favoured mastery sections in eight of nine comparisons, but students taking one mastery class earned less credit than those taking none, attributed to course selection. Retrospective and uncontrolled; do not use a local section comparison as evidence of the gate's effect without accounting for who enrolled.
- **Whether the check means what the criterion says.** [Criterion-referenced tests need construct validation](../claims/criterion-referenced-tests-need-construct-validation.md) [~W] is a theoretical argument (checked by the judge on full text) that a criterion-referenced test's tasks must be shown empirically to reflect the competence of interest. The gate is only as good as that evidence.

Do not combine these into one strength, rank the syntheses by effect labels while their comparators differ, or read "positive effects" as a size. A precise abstention names the missing comparison, instrument or horizon and how to obtain it.

## Further evidence, not yet read against this model
<!-- Restored 2026-10-01 (maintainer's decision): claims this page cited before the 2026-10-01 rewrite, which kept only claims whose sources it had re-read. Each marker keeps its old direction, capped by the claim's recorded evidence (strength_cap); each label says how far the claim's own entries have been checked against their sources by check_load_bearing.py. None has been re-read for the conditional model above, so treat them as candidates for it, not as part of it. -->
Claims this page cited before it was rewritten as a conditional model. They are evidence about the relationship, but none has yet been re-read against the model above; each says how far its own sources have been checked.

- [Self-monitoring improves self-regulation and supports better learning decisions.](../claims/self-monitoring-improves-self-regulation.md) [+M] — not settled: the text available could not confirm the entries (abstract)
- [Mastery and control groups show no significant differences in entry knowledge, academic self-concept, or affect toward education](../claims/mastery-control-no-entry-differences.md) [~W]
- [Female students show stronger academic self-confidence, more positive attitudes, higher achievement, and fewer absences, but this advantage diminishes almost completely under mastery learning](../claims/sex-advantage-diminishes-under-mastery-learning.md) [~W]

## Illustrative design instance and observation record

*Illustration, invented for this page; not a tested course.* An introductory statistics course for part-time adult learners (`adult`, `postsecondary`, `online-instructor-led`) has six cumulative units. A learner says they want to finish within the term because their employer funds one term only; the designer's objective is criterion performance on each unit. They agree a cut score for each unit check, two rechecks on parallel forms, and a rule that a learner still below criterion after the second recheck advances with the gap recorded and a short re-probe at the start of the next unit. On unit 2 (sampling distributions) the learner scores below criterion; a prerequisite probe on unit 1 (variability) is passed, and the learner explains the wrong step by confusing the spread of a sample with the spread of sample means. The tutor corrects with a simulation-based demonstration rather than replaying the unit's video; the learner passes the parallel recheck, and the start-of-unit-3 re-probe is recorded.

Record: **unit, criterion and check form → instruction and practice received → response and reasoning → candidate interpretations and the probe chosen → correction delivered and its time → recheck form, attempt number and response → advancement decision and rule applied → re-probe at the next unit or stated horizon**, alongside the learner's stated goal and any change in it. An agent may summarise this record but must not invent missing inputs or assign a probability that the learner has "mastered" the unit without a calibrated model.

## Elements and limits

[Formative assessment](../elements/formative-assessment.md), [feedback](../elements/feedback.md), [reassessment](../elements/reassessment.md), [adaptive mastery learning](../elements/adaptive-mastery-learning.md), [rubric](../elements/rubrics.md) and [practice](../elements/practice.md).

This pattern is scoped to cumulative units with a definable check. Performances that develop continuously without a single threshold, open-ended projects, and programme-level competency certification need other configurations and evidence. The evidence above concerns programmes and averages; whether this page's diagnostic branches improve decisions for individual learners, and what cut score or attempt limit serves a given goal, remain to be tested with learners.

## Related Patterns
- [Game-Based Mastery Learning (e.g., Duolingo Pattern)](game-based-mastery-learning-eg-duolingo-pattern.md)

## Examples
- A unit where learners receive targeted reteaching and then reassess until they meet the rubric threshold.
- [Increase the use of feedback and correctives through mastery learning procedures](../strategies/formative-tests-with-corrective-feedback.md)
- [Mastery Learning](../strategies/mastery-learning.md)
- [Use Mastery Learning](../strategies/use_mastery_learning.md)

## Key Sources
- Bloom, B. S. (1971). Mastery learning. In J. H. Block (Ed.), *Mastery learning: Theory and practice*. Holt, Rinehart and Winston.
- Kulik, C. L. C., Kulik, J. A., & Bangert-Drowns, R. L. (1990). Effectiveness of mastery learning programs: A meta-analysis. *Review of Educational Research, 60*(2), 265-299. [https://doi.org/10.3102/00346543060002265](https://doi.org/10.3102/00346543060002265)
- Bonczar, Thomas P., & Easton, John Q. (1983). The Effect of Mastery Learning on Student Achievement. https://eric.ed.gov/?id=ED238505
- Guskey, Thomas R., et al. (1982). The Effectiveness of Mastery Learning Strategies in Undergraduate Education Courses. Paper presented at the Annual Meeting of the American Educational Research Association, New York. https://eric.ed.gov/?id=ED213702

<!-- deprecated 2026-10-01: superseded by the conditional model above. The page's earlier body, kept verbatim:

## Description
Mastery Learning is a pattern in which instruction is organized around clear criteria, formative checks, corrective support, and reassessment before progression. Unlike one-pass instruction, the pattern assumes some learners will need additional explanation, feedback, or time before moving on.

## Implications

### Context
#### Requirements
- **Clear mastery thresholds**
- **Frequent formative checks**
- **Corrective instruction and reassessment**
#### Constraints
- **Scheduling and workload pressures**
- **Risk of reducing mastery to narrow test performance**
#### Grain Size
- Lesson
- Unit

### Target Goals
- Reliable competence before advancement.
- Reduced accumulation of unresolved misunderstandings.

### Target Learners
- Learners building cumulative skills and prerequisite knowledge.

### Theory
#### Supporting
- Bloom's mastery learning tradition.
- [Self-Regulated Learning](../theories/self-regulated-learning.md)
#### Contradicting / Qualifying
- Not all complex performances can be reduced to a single mastery threshold.

### Claims
- [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [+M]
- [Self-monitoring improves self-regulation and supports better learning decisions.](../claims/self-monitoring-improves-self-regulation.md) [+M]

## Design

### Sequence
1. Define mastery criteria.
2. Teach and model the target performance.
3. Check understanding formatively.
4. Provide corrective support for non-mastery.
5. Reassess before advancing.

### Elements Used
- [Formative Assessment](../elements/formative-assessment.md)
- [Feedback](../elements/feedback.md)
- [Reassessment](../elements/reassessment.md)

### Affordances
- [Mastery Learning](../principles/mastery-learning.md)
- [Formative Assessment](../principles/formative-assessment.md)
- [Competency-Based Learning & Assessment](../principles/competency-based-assessment.md)
-->

<!-- merged 2026-10-07 from patterns/mastery-learning-formative-corrective-cycle ("Mastery learning cycle of formative tests, correctives, and relearning"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Mastery learning cycle of formative tests, correctives, and relearning

> **Pattern** · [All patterns](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
A lesson-level instructional pattern in which "Students take frequent \"formative tests\" to measure their learning progress" and these are "followed by correc-"tions and opportunities to relearn material not yet understood before new content is introduced. The City Colleges of Chicago implemented this pattern system-wide for over a decade: "What began as an experimental project on one campus developed into an" institution-wide approach. The pattern pairs assessment with corrective action rather than using tests only for grading.

## Design Implications

### Context
#### Requirements
- Frequent formative tests that measure learning progress
- Corrective activities and opportunities for students to relearn ideas and concepts they have not understood
#### Constraints
- 

### Target Learners
- full-time community college students at the City Colleges of Chicago

### Target Goals
- course achievement as measured by earned credit rates

### Claims
- [Mastery Learning Higher Earned Credit Rates](../claims/mastery-learning-higher-earned-credit-rates.md) [+M]

## Related Patterns

- [Game-Based Mastery Learning (e.g., Duolingo Pattern)](game-based-mastery-learning-eg-duolingo-pattern.md)

## Examples

- [Increase the use of feedback and correctives through mastery learning procedures](../strategies/formative-tests-with-corrective-feedback.md)

## Key Sources
- Bonczar, Thomas P., & Easton, John Q. (1983). The Effect of Mastery Learning on Student Achievement. https://eric.ed.gov/?id=ED238505
-->

<!-- merged 2026-10-07 from principles/superimpose-mastery-learning-on-lecture-courses ("Superimpose group-based mastery learning on traditional lecture-format courses with formative tests and corrective activities"), misfiled as a principle and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Superimpose group-based mastery learning on traditional lecture-format courses with formative tests and corrective activities

> **Principle** · [All principles](index.md)
> **Evidence** · 2 claims (2 mixed) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article recommends the teacher-paced, group-based mastery model for postsecondary instruction because it can be added to existing lecture courses with minimal restructuring: "The teacher -paced,rgroug-based model canbe easily superimposed on thetraditional lecture4rimatactually affording little or no changein the way a course is taught." Instructors state objectives clearly, administer short formative tests with feedback after each unit, and require corrective work for students below the mastery criterion, while keeping content, topic sequence, and group-based instruction identical across sections.

## Design Implications

### Context
#### Requirements
- A series of formative tests with accompanying feedback and corrective activities administered following instruction on each unit
- A detailed set of common course objectives shared with students, on which the final examination is based
#### Constraints
- The article notes mastery learning is not a panacea, though it may be a step toward demonstrating competencies in teacher preparation

### Target Learners
- undergraduate education majors
- preservice teachers

### Target Learning Objectives
- increased learning and achievement in coursework
- more enthusiasm toward learning

### Claims

- Mastery Learning Higher Achievement Grades Attendance Undergraduate [+M]
- [Mastery and control groups show no significant differences in entry knowledge, academic self-concept, or affect toward education](../claims/mastery-control-no-entry-differences.md) [~W]
- [Female students show stronger academic self-confidence, more positive attitudes, higher achievement, and fewer absences, but this advantage diminishes almost completely under mastery learning](../claims/sex-advantage-diminishes-under-mastery-learning.md) [~W]

## Related Principles
- 

## Examples

- [Mastery Learning](../strategies/mastery-learning.md)
- [Mastery Learning](../patterns/mastery-learning.md)
- [Use Mastery Learning](../strategies/use_mastery_learning.md)

## Key Sources
- Guskey, Thomas R., et al. (1982). The Effectiveness of Mastery Learning Strategies in Undergraduate Education Courses. Paper presented at the Annual Meeting of the American Educational Research Association, New York. https://eric.ed.gov/?id=ED213702
-->

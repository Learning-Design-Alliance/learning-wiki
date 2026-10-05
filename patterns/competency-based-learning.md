---
type: pattern
id: competency-based-learning
title: Competency-Based Learning
description: "A reusable course-level policy that maps a course to stated competencies, places each learner by a criterion-referenced response, lets pace vary and advances on demonstrated competence, with the validity of the evidence, the support offered, time and completion stated as conditions."
status: review
generated:
  by: claude/unspecified
  at: 2026-10-02
author: competency-based education tradition
grain_size: course
---

# Competency-Based Learning

> **Pattern** · [All patterns](index.md)
> **Evidence** · 7 claims (2 for, 5 mixed) · 13 studies (5 causal, 3 quant-synthesis, 2 review, 2 theoretical, 1 qualitative), `q1`–`q4` · 3 of 13 report an effect size · 4 claims rest on one study

## Description and scope

A reusable policy for organising a course around a map of stated competencies rather than a fixed calendar: each learner's starting response on each competency is elicited, instruction and support are directed at the competencies not yet shown, pace varies between learners, and a learner advances on a competency when a criterion-referenced performance shows it. It instantiates the [Competency-Based Learning & Assessment](../principles/competency-based-assessment.md) principle; [competency-based assessment](../principles/competency-based-assessment.md) concerns how the evidence of competence is gathered and judged.

This page owns the **more general, course-level relationship**: a map of several competencies, placement, flexible pace across them and progression on evidence. [Mastery learning](mastery-learning.md) (and its [principle](../principles/mastery-learning.md)) is a narrower configuration that sits inside it: a gate-correct-recheck loop on one cumulative unit at a time, usually with a group schedule. Use the mastery-learning pages for the loop at each competency's check; use this page for how the competencies are mapped, how learners are placed, how far pace may vary and what progression and completion rules apply. Programme governance (credit unbundled from seat time, assessment on demand, a competency transcript) is a further, programme-level object that this page does not describe.

The study configurations below are evidence; **the wiki has no claim that tests a competency-based course as a whole against a time-based one.** The closest is a quasi-experiment on personalized-learning schools in which competency-based progression was one bundled component among several. The response-dependent policy on this page is therefore an **untested design proposal**. Use it to collect better evidence about learners' responses, not to certify that a learner "is competent".

## Inputs: establish the design brief

| Field | Record or elicit |
|---|---|
| Learner and starting observation | A criterion-referenced response on each competency in the map (or a placement probe), prior experience the learner reports, earlier credentials, errors and their kind. Use `expertise` (`novice`, `intermediate`, `advanced`, `mixed`), `age` and `population_band` values where known; record unknowns as unknown, not as novice. |
| Context and activities | Setting (`classroom`, `online-self-paced`, `online-instructor-led`, `workplace-clinical`), duration (`days-weeks`, `term-plus`), who teaches and who judges evidence, what support is available between attempts (teacher, peer, software, worked examples), aids permitted during assessment, how far pace may vary within the term and what the administrative calendar requires. |
| Learner-valued goal | Ask what the learner wants from the course and by when: a credential, a job task, finishing within funded time, skipping what they already know. Record divergence from the competency map, and the learner's tolerance for extra time, as observations. |
| Designer objective | The competency map: each competency, its knowledge type (`procedure`, `principle`, `complex-skill`, `metacognitive-strategy`, ...), which competencies depend on which, the representative performance that would show each, the criterion and its justification, and which competencies must be shown together in an integrated task rather than one at a time. |
| Outcome | Competency-check performance, an independent course or programme examination (`general-achievement`), integrated or whole-task performance (`skill-performance`), delayed retention or transfer if targeted, completion (`persistence`) and time to criterion (`learning-time`), each with its instrument and horizon. |

A request to "move to competency-based learning" or "let students go at their own pace" does not specify these. Ask for them before prescribing a placement test, a criterion, an attempt limit, a degree of self-pacing or an expected gain. Check that each competency's performance samples what the competency names, that a parallel form exists for reassessment, and that some task requires competencies to be integrated.

## Sequence and conditional policy

1. **Map the competencies.** Name each competency, its representative performance, criterion, permitted aids and dependencies. Include at least one integrated task that requires several competencies together. Tell learners the map and the criteria.
2. **Elicit a starting response.** Place each learner by a criterion-referenced response on the competencies, not by self-report alone. Record what the learner already shows and what remains unknown.
3. **Set the pacing and progression rules openly.** Decide how far pace may vary, whether learners move as a group with individual correction or individually, what checkpoints or deadlines apply, and what happens when time runs out. Agree these with the learner where the course allows.
4. **Teach and support the competencies not yet shown.** Direct instruction, practice and support at those competencies. Record what each learner actually received, including how much was self-directed.
5. **Gather performance evidence.** Score responses against the criterion and record the reasoning or error, not only the score. Use the [mastery-learning loop](mastery-learning.md) where a competency check falls short: interpret, correct responsively, recheck on a parallel form.
6. **Advance on demonstrated competence, with the limit explicit.** Advance on criterion, or by the agreed rule when the attempt or time limit is reached, recording any unresolved gap.
7. **Check integration and retention.** Re-observe competencies in the integrated task and at a stated delayed horizon; a sequence of single-competency passes is not yet evidence of integrated performance.

| Observation | Discriminating probe | Proposed action, with its uncertainty |
|---|---|---|
| Learner shows a competency on placement | Give a parallel task with a changed relevant condition; compare with the learner's account of where they learned it. | If the parallel task is also met, credit it and move on; if only the familiar form is met, treat recognition or narrow practice as live explanations and give a shorter targeted route rather than full instruction. One placement response does not establish competence. |
| Falling behind under self-paced progress | Record time and attempts per competency; compare progress on a scheduled checkpoint with progress without one; ask about purpose, barriers and time available. | Add checkpoints, group sessions or a tutor contact, or negotiate the time limit; self-pacing that the learner cannot sustain may cost completion. Neither procrastination nor a missing prerequisite is established by the delay alone. |
| Passes each competency check, struggles on the integrated task | Compare which competency the failed step draws on with what its check sampled; give a smaller task combining two competencies. | Add integration practice or widen the earlier checks; a narrow check, forgetting and a genuinely new demand of integration each lead to a different action, and one observation does not separate them. |
| Repeated attempts on one competency without reaching criterion | Change the form of support and observe; probe an earlier competency in the map; check how other learners fare on the same item set. | Offer a different route (explicit strategy instruction, a worked example, one-to-one or small-group help) or revisit the criterion with evidence from other learners; do not keep cycling the same material. |
| Course-level results no better than the time-based version | Record which components were actually delivered: placement, targeted support, varied pace, reassessment; compare sections or terms that delivered more of them. | Read a null result as possibly a partial implementation before reading it as a failure of the pattern; equally, do not read larger gains where implementation was fuller as proof, since who implements fully is not random. |

## Choosing configurations from evidence

- **The bundle as a whole.** [Personalized-learning effects and implementation](../claims/personalized-learning-effects-vary-with-fidelity.md) [~M]: a quasi-experiment (`controlled-nonrandom`, matched virtual comparison groups built from national norm-referenced tests; `pre-k-12`; about 40 schools, 5,539 students in mathematics and 5,474 in reading, 2014–15) of schools implementing personalized-learning practices that included competency-based progression, flexible pacing, adaptive software and data-driven grouping. One-year effects were small: +0.09 SD in mathematics (significant), +0.07 SD in reading (not significant). Schools reporting fuller implementation and schools in their second year showed larger effects, which the authors call suggestive, not confirmed, since implementation was self-reported and the district subsample small. It cannot separate competency-based progression from the other components, and it does not predict an effect for one course. Not yet checked against its source. Treat the pattern as a bundle whose components need to be delivered and recorded, and expect small average effects rather than large ones.
- **Gating each competency on a criterion.** [Mastery learning programmes, 108 controlled evaluations](../claims/mastery-learning-improves-outcomes.md) [+M] report positive effects on examination performance against conventionally paced instruction at college, high-school and upper-elementary levels, apparently stronger for weaker students and varying with the mastery procedure, design and content; possibly more time on instructional tasks; and, for **self-paced** college programmes, often reduced completion. Abstract only, judged to pass on it; no pooled size recorded. It supports criterion-based progression as a candidate and makes the degree of self-pacing a decision to take with completion in view.
- **Group-paced versus self-paced progression.** [Group-based mastery learning and attrition](../claims/mastery-improves-engagement-attrition.md) [~M]: a 1985 conference synthesis reports, from five observational studies, more time-on-task in mastery classes (average effect size .68), and, from one community-college evaluation of over 7,000 students in 77 sections, lower attrition in mastery-taught classes in seven of eight disciplines (average .85), contrasted with findings for personalised self-paced systems. The attrition result rests on one evaluation and the time-on-task result on observation, not assignment; not yet checked against its source. Together with the synthesis above, it is a reason to consider group checkpoints with individual correction rather than unbounded self-pacing, not proof that either is better.
- **Letting learners set the pace.** [Learner pacing and learner control](../claims/learner-paced-beats-system-paced-complex-material.md) [~M]: in one experiment with primary-school students learning the causes of day and night from an animation, learner-paced versions beat a system-paced one on difficult, high-element-interactivity questions only; a meta-analysis of 18 studies (29 effects) of learner control in educational technology found an overall effect near zero (g = 0.05). Both entries pass the judge on abstracts. Pace control within a lesson is not the same as pace across a course, so this does not test the pattern's flexible progression; it does mean "learners control their pace" should not be expected to help by itself.
- **Support between attempts.** [Contingent versus fixed support](../claims/contingent-scaffolding-improves-learning.md) [~M]: in one-to-one long-division tutoring with fourth and fifth graders (n = 8 per condition), fully contingent support beat fixed, moderate, partly contingent and no support at immediate and one-month tests; a dynamic-assessment synthesis ranks explicit strategy training above contingent scaffolding; most evidence is one-to-one, and classroom contingency is largely undemonstrated. Not settled against its sources. Make the support between attempts respond to what the response showed, and keep explicit strategy instruction as an alternative.
- **Whether the evidence of competence means what the map says.** [Criterion-referenced tests need construct validation](../claims/criterion-referenced-tests-need-construct-validation.md) [~W] is a theoretical argument (checked by the judge on full text) that the tasks of a criterion-referenced test must be shown empirically to reflect the competence of interest; it reports no validation study. Progression is only as sound as that evidence, so the competency checks should be checked against an independent outcome before the map is trusted.

The earlier page's requirements (defined competencies, valid evidence, flexible pacing or modular progression, feedback and reassessment) and constraints (design complexity, atomising learning into isolated skills, administrative systems built on seat time) are carried into the inputs and sequence above. None of them is tested as a requirement by a claim here; they are proposals from the earlier page. Do not combine these findings into one strength, rank unlike comparators by effect labels, or read "positive effects" as a size. A precise abstention names the missing comparison, instrument or horizon and how to obtain it.

## Further evidence, not yet read against this model
<!-- Restored 2026-10-02: claims this page cited before the 2026-10-02 rewrite and did not use in the model above. Each marker keeps its old direction, capped by the claim's recorded evidence (strength_cap); each label says how far the claim's own entries have been checked against their sources by check_load_bearing.py. None has been re-read for the conditional model above, so treat them as candidates for it, not as part of it. -->
Claims this page cited before it was rewritten as a conditional model. They are evidence about the relationship, but none has yet been re-read against the model above; each says how far its own sources have been checked.

- [Self-monitoring improves self-regulation and supports better learning decisions.](../claims/self-monitoring-improves-self-regulation.md) [+M] — not settled: the text available could not confirm the entries (abstract)

## Illustrative design instance and observation record

*Illustration, invented for this page; not a tested course.* A term-long workplace course in electrical maintenance for adult apprentices (`adult`, `adult-workplace`, `workplace-clinical`, `term-plus`) is mapped to eight competencies, from reading schematics to fault-finding on a live panel, with a final integrated fault-finding task. One apprentice, who has worked as an electrician's helper, wants to qualify before a site placement in ten weeks; the designer's objective is criterion performance on all eight competencies and the integrated task. On placement the apprentice meets the criterion on three competencies; on a parallel task with a different panel layout, two of the three hold and one (isolating a circuit) does not, so that one is kept in the route. The group meets weekly for a checkpoint, with individual work between. In week 6 the apprentice passes every single-competency check but misses a step on the integrated task that draws on schematic reading under time pressure; a smaller two-competency task is added and the integrated task is reattempted in week 8, with the result recorded.

Record: **competency, criterion and check form → placement response and parallel-form response → route agreed and pacing rule → instruction and support received, and how much was self-directed → response and reasoning → candidate interpretations and the probe chosen → recheck form, attempt number and response → advancement decision and rule applied → integrated task and delayed re-observation**, alongside the learner's stated goal and any change in it. An agent may summarise this record but must not invent missing inputs or assign a probability that the learner "is competent" without a calibrated model.

## Elements and limits

[Assessment](../elements/assessment.md), [formative assessment](../elements/formative-assessment.md), [feedback](../elements/feedback.md), [reassessment](../elements/reassessment.md), [adaptive mastery learning](../elements/adaptive-mastery-learning.md), [learning objectives](../elements/learning-objectives.md), [rubric](../elements/rubric.md), [self-assessment](../elements/self-assessment.md), [portfolio](../elements/portfolio.md) and [practice](../elements/practice.md).

This pattern is scoped to a course organised around a competency map with criterion-referenced evidence. It does not establish that a competency-based course outperforms a time-based one, an optimal degree of self-pacing, a criterion, a number of attempts or a unit size, or a forecast for an individual learner. The risk named by the earlier page, that a competency map atomises a complex performance into isolated skills, is why the sequence includes an integrated task; whether that guards against it remains to be tested. Programme-level competency certification and credit policy need their own configuration and evidence.

## Related Patterns
- [Mastery Learning](mastery-learning.md)

## Examples
- A competency map that lets learners reassess specific standards until they show proficiency.
- Modular technical training where prior experience allows early demonstration and faster progression.

## Key Sources
- Le, C., Wolfe, R. E., & Steinberg, A. (2014). *The past and the promise: Today's competency education movement*. Jobs for the Future.
- Sturgis, C., & Casey, K. (2018). *Designing for equity: Leveraging competency-based education to ensure all students succeed*. CompetencyWorks.

<!-- deprecated 2026-10-02: superseded by the conditional model above. The page's earlier body, kept verbatim:

## Description
Competency-Based Learning is a pattern that organizes progression around demonstrated competence on defined outcomes rather than uniform pacing. It typically combines explicit competencies, flexible progress, reassessment, and evidence of performance across time.

## Implications

### Context
#### Requirements
- **Defined competencies**
- **Valid evidence of mastery**
- **Flexible pacing or modular progression**
- **Feedback and reassessment pathways**
#### Constraints
- **High design complexity**
- **Risk of atomizing learning into isolated skills**
- **Administrative systems may assume seat-time progression**
#### Grain Size
- Unit
- Course

### Target Goals
- Make expectations transparent.
- Support progression when competence is demonstrated.
- Personalize pace without abandoning standards.

### Target Learners
- Learners with variable readiness, prior experience, or pacing needs.

### Theory
#### Supporting
- Mastery learning and criterion-referenced assessment traditions.
- [Self-Regulated Learning](../theories/self-regulated-learning.md)
#### Contradicting / Qualifying
- Competency frameworks can become reductive if complex performance is broken into isolated fragments.

### Claims
- [Self-monitoring improves self-regulation and supports better learning decisions.](../claims/self-monitoring-improves-self-regulation.md) [+M]
- [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [~M]

## Design

### Sequence
1. Define competencies and performance criteria.
2. Assess current level.
3. Provide targeted instruction and support.
4. Gather performance evidence.
5. Reassess and advance on demonstrated competence.

### Elements Used
- [Assessment](../elements/assessment.md)
- [Feedback](../elements/feedback.md)
- [Reassessment](../elements/reassessment.md)

### Affordances
- [Competency-Based Learning & Assessment](../principles/competency-based-assessment.md)
- [Mastery Learning](../principles/mastery-learning.md)
- [Formative Assessment](../principles/formative-assessment.md)
-->

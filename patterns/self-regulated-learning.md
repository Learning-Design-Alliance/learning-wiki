---
type: pattern
id: self-regulated-learning
title: Self-Regulated Learning
description: "A reusable plan–monitor–act policy that makes regulation explicit with task-specific prompts, modelled self-assessment and a usable next action, then reads the response before handing regulation to the learner."
status: review
generated:
  by: claude/unspecified
  at: 2026-10-01
sources:
  - id: zimmerman-2002
    resource: "https://doi.org/10.1207/s15430421tip4102_2"
    title: "Zimmerman, B. J. (2002). Becoming a self-regulated learner: An overview. *Theory Into Practice, 41*(2), 64-70"
    author: Zimmerman, B. J
author: self-regulated learning tradition
grain_size: unit
---

# Self-Regulated Learning

> **Pattern** · [All patterns](index.md)
> **Evidence** · 7 claims (3 for, 4 mixed) · 9 studies (4 quant-synthesis, 2 causal, 2 review, 1 theoretical), `q3`–`q4` · 4 of 9 report an effect size · 3 claims rest on one study

## Description and scope

A reusable policy for making planning, monitoring against a criterion and choosing a next action explicit within subject-matter work, then reading each response before reducing support. It instantiates the [conditional principle](../principles/self-regulated-learning.md). The study configurations below (prompts in computer-based environments, school training programmes, web-based training with a diary and peer feedback, modelled self-assessment) are evidence; the response-dependent policy is an **untested design proposal**. Use it to gather better evidence about a learner's regulation, not to certify a trait called "self-regulated".

## Inputs: establish the design brief

| Field | Record or elicit |
|---|---|
| Learner and starting observation | Task-specific prior knowledge (a short content probe); a prediction or self-rating set beside a scored result; whether the learner already plans or reviews unprompted; age band and setting. Preserve unknowns. |
| Context and activities | Subject task the regulation is attached to; `classroom`, `online-self-paced` or other setting; time available across the unit; who delivers any training; prompts, diary, rubric, peer groups and feedback actually available; what the learner can choose (chapters, order, pace, help). |
| Learner-valued goal | Ask what the learner wants from this unit and why. Record disagreement with the designer objective; negotiate rather than assume agreement. |
| Designer objective | Which capability matters: subject performance, accurate self-assessment, a planning habit, or independent regulation without prompts. Say which supports are permitted at the target. |
| Outcome | Instrument for each objective (subject test aligned with what was regulated; calibration of self-ratings against scores; behaviour traces such as logged time or revisions; questionnaire, labelled as self-report), the local criterion, and the horizon (`immediate`, end of unit, `delayed`). |

A request to "make learners more independent" does not specify these inputs. Ask for them before prescribing a prompt schedule, a diary or a fading point. Check that the criterion learners monitor against is itself correct and understandable; monitoring against an unclear rubric produces confident error.

## Sequence and conditional policy

1. **Elicit briefly.** Before support, ask for a short plan for the coming task and a prediction of performance; then score the task. Record the gap between prediction and score, and whether a plan was written at all. These probes are also learning events; record them.
2. **Model the regulation on this task.** Show a worked example of someone setting a goal, checking work against the criterion, rating it and choosing a next action, in the subject the learner is studying rather than as a separate study-skills session.
3. **Prompt at natural pauses.** Use short, task-specific planning, monitoring and evaluation prompts before, between and after task segments, paired with feedback on the task where possible. Offer a named set of next actions (review, try a different method, ask for help, move on) so that monitoring has something to act on.
4. **Choose the next activity provisionally.** Use the table below. Repeat matched observations where feasible; prior knowledge, task difficulty and the prompts themselves confound a single reading.
5. **Reobserve, then reduce support.** Score a new representative task with fewer prompts at the agreed horizon, and compare self-ratings with the score again. Reduce prompts only after the learner's choices and calibration hold without them; keep unresolved explanations on the record.

| Observation | Discriminating probe | Proposed action, with its uncertainty |
|---|---|---|
| Large overestimate of own score | Ask for a prediction after a retrieval attempt rather than after rereading; have the learner score a worked exemplar with the rubric; run a short content probe. | If calibration improves after retrieval or exemplar scoring, keep that step before every self-rating. If the content probe is weak, treat it as a knowledge gap first and do not rely on self-assessment yet. Neither branch is a validated diagnosis. |
| Accurate rating, next choice does not change | Present a fixed menu of next actions and ask why the learner chose one; ask what they are aiming for. | If no option seems usable, teach one control strategy explicitly. If the goal is not valued, negotiate the task before adding prompts. More monitoring prompts alone are unlikely to help. |
| Prompts and diary completed, subject scores flat | Compare entries with traces (time, revisions, chapters chosen); score the chapters the learner chose to focus on separately from the overall test. | If focus-area scores rise and the overall score does not, the outcome may be misaligned, not the regulation. If traces do not change either, replace generic prompts with task-specific ones or add feedback on the plan. |
| Uses supports only when present | Remove one prompt type on a matched task and observe whether planning or checking still occurs. | Fade one prompt at a time and reobserve. Keep the prompt if removal costs performance at the target and permanent prompting is acceptable to the objective. |
| Little participation or abandons plans | Ask about purpose, time and barriers; supply the plan and see whether execution follows. | If execution follows a supplied plan, provide plans and teach planning later. If not, the barrier may be content, load or motivation rather than planning skill. |

## Choosing configurations from evidence

- For learning in a computer-based environment, [task-specific metacognitive prompts](../claims/metacognitive-prompts-improve-learning.md) [+M] are a candidate configuration: a meta-analysis against no-prompt controls reported g = 0.40 on learning outcomes, varying with feedback pairing, task specificity and adaptivity. It does not set a schedule, and it does not show effects outlast the prompts; one reviewed study found lower-prior-knowledge learners needed training before prompts helped.
- For school learners, [SRL training programmes](../claims/self-regulated-learning-improves-achievement.md) [+M] have a pooled average of 0.69 across 84 studies, but over performance, strategy use and motivation together, and larger when researchers delivered them. Do not forecast a teacher-delivered unit's achievement gain from it; in online settings support helped only when it was used.
- Before relying on self-ratings, [modelling self-assessment](../claims/self-assessment-accuracy-is-low-without-training.md) [~M] is a candidate step: in a randomized experiment with 80 pre-university students on genetics problems, modelling examples improved self-assessment accuracy (ηp² = .10). It shows calibration can be trained; it does not show the trained learners then learned more.
- A [diary alone](../claims/learning-diary-alone-no-significant-srl-gains-online-math-prep-course.md) [~M] showed no detected pre–post gain on any measured outcome in a randomized four-group online mathematics preparation trial; equivalence was not tested, so this is no detected gain, not no effect. Not yet checked against its sources.
- In the same trial, [training plus a diary](../claims/web-based-srl-training-with-diary-raises-srl-knowledge-and-self-efficacy-not-math.md) [~M] raised SRL knowledge, self-reported planning and metacognition, and self-efficacy, but not mathematics scores (checked by the judge: all 2 entries pass, full text); across groups the [overall mathematics score missed significance while a score on self-chosen chapters did not](../claims/srl-interventions-math-overall-score-marginal-focus-score-significant-online-prep-course.md) [~M] (checked by the judge: all 2 entries pass, full text). Choose the outcome instrument before choosing the configuration: a broad test may not register what learners chose to regulate.

Do not rank these configurations by their effect labels: the comparators, learners, outcomes and horizons differ, and the 0.69 and 0.40 figures are not on one outcome.

## Further evidence, not yet read against this model
<!-- Restored 2026-10-01 (maintainer's decision): claims this page cited before the 2026-10-01 rewrite, which kept only claims whose sources it had re-read. Each marker keeps its old direction, capped by the claim's recorded evidence (strength_cap); each label says how far the claim's own entries have been checked against their sources by check_load_bearing.py. None has been re-read for the conditional model above, so treat them as candidates for it, not as part of it. -->
Claims this page cited before it was rewritten as a conditional model. They are evidence about the relationship, but none has yet been re-read against the model above; each says how far its own sources have been checked.

- [Self-monitoring improves self-regulation and supports better learning decisions.](../claims/self-monitoring-improves-self-regulation.md) [+M] — not settled: the text available could not confirm the entries (abstract)

## Illustrative design instance and observation record

*Illustration, invented, not a tested design.* An adult learner in a four-week self-paced statistics refresher says she wants to stop "freezing" on hypothesis-test questions; the designer's objective is a pass on the end-of-course test and a weekly planning habit. Agree that both count and record them separately. Week 1: a short plan and a prediction before a mixed problem set; she predicts 80% and scores 45%, with errors concentrated in test selection. A content probe shows she cannot yet say which test fits which design, so self-rating is not yet relied on; a modelled self-check of a worked solution against a three-point rubric is added before each later self-rating, with planning prompts at the start of each session and a menu of next actions. Week 3: prediction and score are within ten points on test-selection items; one prompt type is removed on a matched set. The end-of-course test and a score on the chapters she chose are reported separately.

Record: **task and criterion → supports present (prompts, model, rubric, feedback) → plan and prediction → scored result → candidate interpretations and their basis → discriminating probe → chosen next activity and why → next observation at the stated horizon**. Preserve the learner's stated purpose and any change in it. An agent may summarize this record, but must not fabricate missing inputs or assign numerical state probabilities without a calibrated model.

## Elements and limits

[Goal setting](../elements/goal-setting.md), [self-monitoring](../elements/self-monitoring.md), [prompts](../elements/prompts.md), [metacognitive strategies](../elements/metacognitive-strategies.md), [self-assessment](../elements/self-assessment.md), [rubric](../elements/rubric.md), [feedback](../elements/feedback.md), [peer feedback](../elements/peer-feedback.md), [reflection](../elements/reflection.md), [daily before-and-after SRL learning diary](../elements/daily-before-and-after-srl-learning-diary.md) and [fading scaffolding](../elements/fading-scaffolding.md).

This pattern is scoped to regulation attached to subject-matter tasks over a unit. Standalone study-skills courses, motivational interventions, behavioural self-monitoring for on-task conduct and adaptive systems that take regulation decisions for the learner are distinct configurations with their own evidence. The present policy supports observation and design reasoning; its branches, fading rule and the role of the learner's valued goal remain to be tested with actual learners.

## Key Sources
- Zimmerman, B. J. (2002). Becoming a self-regulated learner: An overview. *Theory Into Practice, 41*(2), 64-70. [https://doi.org/10.1207/s15430421tip4102_2](https://doi.org/10.1207/s15430421tip4102_2)

<!-- deprecated 2026-10-01: superseded by the conditional model above. The original body follows verbatim.

## Description
Self-Regulated Learning is the pattern-level target for designs that explicitly cycle planning, monitoring, feedback, and revision so learners can manage their own learning more effectively.

## Implications

### Context
#### Requirements
- **Clear goals**
- **Feedback or evidence**
- **Routines for monitoring and adjustment**
#### Constraints
- **Learners may need modeling and scaffolds to regulate effectively**
#### Grain Size
- Lesson
- Unit

### Target Goals
- Strengthen planning, monitoring, and adaptive revision.

### Target Learners
- Learners developing independence and strategic control over learning.

### Theory
#### Supporting
- [Self-Regulated Learning](../principles/self-regulated-learning.md)

### Claims
- [Self-monitoring improves self-regulation and supports better learning decisions.](../claims/self-monitoring-improves-self-regulation.md) [+M]

## Design

### Elements Used
- [Metacognitive Strategies](../elements/metacognitive-strategies.md)
- [Self-Assessment](../elements/self-assessment.md)
- [Reflection](../elements/reflection.md)
-->

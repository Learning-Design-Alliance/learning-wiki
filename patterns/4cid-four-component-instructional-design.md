---
type: pattern
id: 4cid-four-component-instructional-design
aliases: [4cid]
title: 4C/ID (Four-Component Instructional Design)
description: "A reusable whole-task policy for complex skills: learning tasks in simple-to-complex task classes with fading support, supportive and just-in-time procedural information, and selective part-task practice, whose response-dependent branches are untested proposals."
status: review
generated:
  by: claude/unspecified
  at: 2026-10-01
sources:
  - id: van-merrienboer-2006
    resource: "https://doi.org/10.1002/acp.1250"
    title: "van Merrienboer, J. J. G., Kester, L., & Paas, F. (2006). Teaching complex rather than simple tasks: Balancing intrinsic and germane load to enhance transfer of learning. *Applied Cognitive Psychology, 20*(3), 343-352"
    author: "van Merrienboer, J. J. G., Kester, L., & Paas, F"
author: Jeroen J. G. van Merrienboer
grain_size: unit
---

# 4C/ID (Four-Component Instructional Design)

> **Pattern** · [All patterns](index.md)
> **Evidence** · 5 claims (4 for, 1 mixed) · 10 studies (4 causal, 2 review, 2 theoretical, 1 quant-synthesis, 1 qualitative), `q2`–`q4` · 0 of 10 report an effect size · 2 claims rest on one study

## Description and scope

A reusable whole-task policy for **complex skills** (performance that integrates several kinds of knowledge and routine). It instantiates the [cognitive load principle](../principles/cognitive-load-theory.md): learners work on whole, authentic learning tasks grouped into task classes from simpler to more complex; support within each class starts high and fades; supportive information (how the domain is organised, how to approach the task) is available before and around the tasks; procedural information (how to carry out routine steps) is given just in time; and part-task practice is added only for routines that must become automatic. The study configurations below are evidence about parts of this policy; **no study recorded in this wiki tests the four components together**, and the response-dependent policy is an untested design proposal. It is a pattern for any complex skill; a particular clinical, technical or professional programme built with it is a design instance.

## Inputs: establish the design brief

| Field | Record or elicit |
|---|---|
| Learner and starting observation | Task-specific experience for each task class; an attempt at a simple whole task with reasoning, errors, help needed and time; which routines are already fluent. Preserve unknowns; "novice" is per task class. |
| Context and activities | Setting, time available, whether real or simulated tasks are possible, which supports (examples, completion tasks, coaching, job aids) can be supplied and faded, and who judges performance. |
| Learner-valued goal | Ask what performance the learner wants and why. Record divergence from the designer's objective and negotiate task content rather than assume agreement. |
| Designer objective | The whole-task performance intended, its knowledge type (usually complex-skill), the range of situations it must transfer to, and which routines must be automatic versus looked up. |
| Outcome | A representative whole task scored by an agreed rubric; immediate, delayed and near/far-transfer horizons as separate outcomes; any safety outcome. Learning-phase effort or efficiency is a separate measure. |

A request to "use 4C/ID" or to "teach the skill" does not supply these inputs. Ask for them before fixing the number of task classes, a fading schedule or a part-task dose.

## Sequence and conditional policy

1. **Analyse the whole task.** Identify the integrated performance, its non-routine (reasoning) and routine (procedural) parts, and the dimensions that make a version simpler or more complex. These are design judgements; record their basis.
2. **Elicit on a simple whole task.** Before instruction, ask for an attempt at the simplest representative version, with reasoning and every help given. This places the learner in a task class; it is not a measure of a latent schema.
3. **Work through a task class with fading support.** Begin with high support (worked or modelled tasks, then completion tasks) and reduce it across varied tasks of the class; give supportive information before or alongside, and procedural information at the step where it is needed, then withdraw it.
4. **Add part-task practice selectively.** Only for a routine that whole-task practice does not make fluent enough and whose slowness is plausibly blocking whole-task performance.
5. **Reobserve before moving on.** Use an unsupported, varied task of the current class under the agreed rubric. Move to a more complex class, stay, or adjust support provisionally; recheck at the stated delay.

| Observation | Discriminating probe | Proposed action, with its uncertainty |
|---|---|---|
| Cannot start even the simplest whole task | Present the same task with mutually referring information integrated and one interacting element pre-taught; ask for the first decision and why. | If performance returns with integration or pre-teaching, keep the whole task and add that support or a simpler version. If not, consider brief isolated-element practice before the whole task. Neither branch is validated. |
| Succeeds with full examples or completion tasks, fails without | Give one unsupported varied task of the same class; ask which relation licenses each step. | Stay in the class and fade more gradually (removing the last worked steps first is one tested option). One failure does not show that support must stay. |
| Correct whole-task reasoning but slow or error-prone on one routine | Time the routine on its own and inside the whole task; vary whether a job aid is available. | Add short part-task practice or a just-in-time aid for that routine, provisionally; drill is not warranted for routines the objective allows to be looked up. |
| Fluent, unsupported success across varied tasks of the class | Present a task from the next class and a changed condition within the current one. | Move to the more complex class with high support again, and remove support the learner no longer needs, since redundant guidance may cost the learner. The exact point is not established. |
| Low participation or reliance on hints regardless of difficulty | Ask about purpose, stakes and barriers; compare a task closer to the learner's valued goal. | Negotiate task content or conditions; hint use and effort alone do not establish the learner's state. |

## Choosing configurations from evidence

- **Whole tasks as the organising unit.** [Whole-task practice for transfer of complex skills](../claims/whole-task-performance-improves-transfer.md) [+W] rests on one design argument, not an experiment: it holds that the load-reducing methods suited to retention (low variability, full guidance) hinder transfer, and proposes high variability and limited guidance, with intrinsic load lowered early for novices. Use it as the pattern's rationale, not as evidence of an effect; judge-checked against its abstract.
- **Isolating interacting elements first.** For novices on high-element-interactivity tasks, [isolated parts before the integrated whole](../claims/part-task-practice-reduces-load-for-novices.md) [+M] improved performance in one experiment (sample, outcome and horizon not reported on the claim page; not yet checked against its sources). It supports pre-teaching or part-task practice as an entry step; it does not test part-task practice for automating routines inside a whole-task sequence, which is 4C/ID's use.
- **Fading within a task class.** [Fading from complete to incomplete examples to problems](../claims/fading-support-promotes-transfer-of-responsibility.md) [+M] favoured near transfer over static example–problem arrangements in three experiments (20 ninth graders; 54 and 45 college students), and removing the last steps first was more favourable. It does not establish a fading rate or far transfer; not settled against its sources.
- **Adjusting support to the response.** [Contingent scaffolding](../claims/contingent-scaffolding-improves-learning.md) [+M]: one-to-one long-division tutoring for fourth and fifth graders (N=8 per condition) found fully contingent support ahead of fixed, moderate or no support at immediate and one-month tests; contingent tutoring matched non-interactive tutoring immediately but improved transfer in a second study (11 pairs); a meta-analysis ranked scaffolding above coaching but below explicit strategy training. Small samples, mostly one-to-one; not settled against its sources.
- **Removing support as expertise grows.** [Worked-example guidance becomes less effective as expertise increases](../claims/worked-examples-less-effective-with-expertise.md) [~M]: two reviews, abstract only and not settled, argue that full guidance becomes redundant and should be faded toward independent problem solving. It qualifies keeping high support across task classes; it gives no threshold.

Do not combine these into a predicted effect for the whole pattern. They differ in learners (children, secondary and college students, trainees), task, comparator and outcome, and none measured delayed whole-task performance in a workplace.

## Further evidence, not yet read against this model
<!-- Restored 2026-10-01 (maintainer's decision): claims this page cited before the 2026-10-01 rewrite, which kept only claims whose sources it had re-read. Each marker keeps its old direction, capped by the claim's recorded evidence (strength_cap); each label says how far the claim's own entries have been checked against their sources by check_load_bearing.py. None has been re-read for the conditional model above, so treat them as candidates for it, not as part of it. -->
Every claim this page cited before the rewrite has been read against the model and appears above, so none is listed here.

## Illustrative design instance and observation record

*Illustration only, invented, not a tested programme.* A new technician wants to fix faults on the machines in their own plant; the training lead's objective is passing a standard fault-finding assessment. Agree a representative whole task (diagnosing a simulated fault on a familiar machine), task classes from a single obvious fault to intermittent multiple faults, a reasoning-and-outcome rubric, permitted aids (the wiring diagram, not the fault table), and a one-month delayed task on a less familiar machine as the transfer outcome. Meter use, a routine, gets part-task practice only if it is slow inside the whole task.

Record: **task and class → support given and removed → response and reasoning → candidate interpretations and confidence basis → distinguishing probe → chosen next task and justification → next observation at the stated horizon**. Preserve the learner's stated purpose and any change in it. An agent may summarise this record, but must not invent missing inputs or assign numerical state probabilities without a calibrated model.

## Elements and limits

[Whole-task performance](../elements/whole-task-performance.md), [supportive information](../elements/supportive-information.md), [procedural information](../elements/procedural-information.md), [just-in-time information](../elements/just-in-time-information.md), [part-task practice](../elements/part-task-practice.md), [fading](../elements/fading.md), [scaffolding](../elements/scaffolding.md), [worked examples](../elements/worked-examples.md), [problem presentation](../elements/problem-presentation.md) and [assessment](../elements/assessment.md). The pattern also applies [guided practice](../principles/guided-practice.md), [problem-based learning](../principles/problem-based-learning.md), [competency-based learning and assessment](../principles/competency-based-learning-assessment.md) and [worked examples](../principles/worked-examples.md); the [worked-examples pattern](worked-examples.md) is the lesson-level policy for the support inside a task class.

This pattern is scoped to complex skills where whole-task transfer is the objective; it is excessive for single facts or one-step procedures, and its analysis and sequencing cost design time. The evidence above tests components in other configurations, not the pattern as a whole, and the conditional branches remain to be tested with learners.

## Related Patterns
- [Problem-Based Learning (PBL)](problem-based-learning.md)
- [Cognitive Load Reduction (CLT Scaffolding Approach)](cognitive-load-reduction-clt-scaffolding-approach.md)

## Examples
- Clinical training programs that move from simpler to more complex patient cases while fading support.
- Technical workforce training where learners perform increasingly realistic troubleshooting tasks.
- Professional education sequences that combine authentic tasks, coaching, and targeted subskill drills.

## Key Sources
- van Merrienboer, J. J. G. (1997). *Training complex cognitive skills*. Educational Technology Publications.
- van Merrienboer, J. J. G., Kester, L., & Paas, F. (2006). Teaching complex rather than simple tasks: Balancing intrinsic and germane load to enhance transfer of learning. *Applied Cognitive Psychology, 20*(3), 343-352. [https://doi.org/10.1002/acp.1250](https://doi.org/10.1002/acp.1250)
- van Merrienboer, J. J. G., & Kirschner, P. A. (2018). *Ten steps to complex learning* (3rd ed.). Routledge.

<!-- deprecated 2026-10-01: superseded by the conditional model above; the pattern body as it stood before the rewrite, kept verbatim.

## Description
4C/ID is a design pattern for teaching complex skills by organizing instruction around four coordinated components: whole learning tasks, supportive information, procedural information, and part-task practice. The pattern is designed for skills that require learners to integrate knowledge, strategy, and procedure rather than master isolated facts. Its central move is to keep the whole task visible while still managing difficulty through sequencing, scaffolding, and selective automation of subskills.

The pattern is strongest when learners need transfer to authentic performance. It is not mainly a content-delivery model. It is a design approach for building sequences in which learners perform meaningful tasks, receive just enough support, and gradually work with more variability and complexity over time.
## Implications

### Context
#### Requirements
- **Complex performance goals**: Best used when the target involves coordination of multiple skills in realistic tasks.
- **A sequence of whole tasks**: Tasks should progress from simpler to more complex while preserving meaningful structure.
- **Supportive and procedural information**: Learners need conceptual guidance before or around the task and just-in-time directions during performance.
- **Selective part-task practice**: Routine elements can be isolated when automation is necessary and the whole task would overload absolute novices.
#### Constraints
- **Design intensity**: 4C/ID requires careful sequencing, task-class design, and support planning.
- **Weak fit for simple recall**: It is excessive for instruction focused mainly on memorization or single-step procedures.
- **Scaffolding quality matters**: Poorly timed support can either overload learners or over-support them.
- **Whole-task complexity can swamp novices**: Designers still need to manage intrinsic load deliberately.
#### Grain Size
- Unit
- Course
- Training sequence

### Target Goals
- **Complex skill acquisition**: Building integrated performance rather than detached subskills.
- **Transfer**: Preparing learners for real or realistic practice conditions.
- **Strategic and procedural coordination**: Combining conceptual understanding with fluent execution.

### Target Learners
- **Adult and professional learners**: Strong fit for workforce, technical, medical, and higher education contexts.
- **Learners preparing for authentic performance**: Best when the outcome is application in practice, not only classroom recall.
- **Novices in complex domains**: Particularly useful when complexity must be managed without losing sight of the whole task.

### Theory
#### Supporting
- Cognitive load theory — complex performance should be sequenced so intrinsic load is manageable and extraneous load stays low.
- Whole-task instructional design traditions — authentic coordinated performance supports transfer better than isolated training alone.
- Scaffolding and fading perspectives — supports should be gradually withdrawn as learners gain control.
#### Contradicting / Qualifying
- Not all skills require full 4C/ID treatment; some can be learned more efficiently through simpler explicit instruction sequences.
- Part-task work is a support inside the pattern, not the organizing center.

### Claims
#### Supporting
- [Whole-task performance improves transfer of complex skills to real-world settings.](../claims/whole-task-performance-improves-transfer.md) [+M]
- [Part-task practice reduces cognitive load for absolute novices during initial skill acquisition.](../claims/part-task-practice-reduces-load-for-novices.md) [+M]
- [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [+M]
#### Contradicting
- [Worked examples can become redundant or counterproductive for advanced learners.](../claims/worked-examples-less-effective-with-expertise.md) [~M]
## Design

### Sequence
1. Present a whole task at an entry level learners can attempt.
2. Provide supportive information that helps learners understand the task class and relevant strategies.
3. Deliver procedural information just in time during task performance.
4. Add part-task practice for routine subskills that need automation.
5. Increase task variability and complexity while fading supports.

### Elements Used
- [Whole-task Performance](../elements/whole-task-performance.md)
- [Part-task Practice](../elements/part-task-practice.md)
- [Problem Presentation](../elements/problem-presentation.md)
- [Assessment](../elements/assessment.md)

### Affordances
- [Guided Practice](../principles/guided-practice.md)
- [Problem-based Learning](../principles/problem-based-learning.md)
- [Competency-Based Learning & Assessment](../principles/competency-based-learning-assessment.md)
- [Worked Examples](../principles/worked-examples.md)

### Personalization
- Task complexity can be adjusted by changing constraints, support, and variability.
- Procedural supports can be faded at different rates for different learners.
- Part-task practice can be targeted only to the subskills a learner has not yet automated.
## Impact
- Strong fit for complex-skill domains where transfer matters more than short-term task ease.
- Helps preserve authentic performance demands while still protecting novices from overload.
-->

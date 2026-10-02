---
type: pattern
id: problem-based-learning
title: Problem-Based Learning
description: "A reusable policy for a problem-centred unit: elicit each learner's framing, set guidance by task-specific starting knowledge, facilitate contingently, consolidate the target content explicitly, and reobserve individually."
status: review
generated:
  by: claude/unspecified
  at: 2026-10-01
sources:
  - id: hmelo-silver-2004
    resource: "https://doi.org/10.1023/B:EDPR.0000034022.16470.f3"
    title: "Hmelo-Silver, C. E. (2004). Problem-based learning: What and how do students learn? *Educational Psychology Review, 16*(3), 235-266"
    author: Hmelo-Silver, C. E
author: PBL tradition
grain_size: unit
---

# Problem-Based Learning

> **Pattern** · [All patterns](index.md)
> **Evidence** · 5 claims (2 for, 2 mixed, 1 against) · 13 studies (5 causal, 3 review, 2 quant-synthesis, 1 qualitative, 1 design, 1 theoretical), `q2`–`q4` · 2 of 13 report an effect size · 1 claim rests on one study

## Description and scope

A reusable policy for organizing a unit around a problem that learners must investigate, deciding how much guidance to give and when, and reading what learners do with the problem. It instantiates the [conditional principle](../principles/problem-based-learning.md). The study configurations below are evidence; the response-dependent policy is an **untested design proposal**. Use it to gather better evidence about a learner group, not to certify that a learner is "ready for open problems".

The pattern is general across domains. A course for a particular setting (a medical curriculum, a primary science unit) is a design that may use it; see [Problem-Based Learning (PBL)](problem-based-learning-pbl.md) for the longer description of the tradition.

## Inputs: establish the design brief

| Field | Record or elicit |
|---|---|
| Learner and starting observation | Age band and task-specific starting knowledge (`novice`, `intermediate`, `advanced`, or `?`); a brief independent attempt at framing the problem or a comparable one; what the learner says they would need to know. Preserve unknowns. |
| Context and activities | Setting (`classroom`, `online-instructor-led`, `workplace-clinical`, ...), duration, group size and roles, available resources, who facilitates, and exactly what guidance, instruction and feedback are planned and when. |
| Learner-valued goal | Ask what the learner wants from working on this problem and why. Record disagreement with the designer objective; negotiate rather than assume agreement. |
| Designer objective | The concept, principle or complex skill the problem is meant to carry (`principle`, `complex-skill`, ...), and whether a correct solution to the problem as posed actually requires it. |
| Outcome | Separate instruments for conceptual understanding, transfer, procedural fluency and product quality; individual as well as group measures; immediate and delayed horizons. |

A request for "more engaging, real-world learning" does not specify these inputs. Ask for them before choosing a problem, a guidance level or a predicted gain. Check first that the problem, the resources and any model solution are correct and that the target concept is needed to solve it.

## Sequence and conditional policy

1. **Elicit briefly.** Present the problem and ask each learner (not only the group) for a first framing: what is the question, what do they already know, what do they need to learn. Keep this short; record it as a learning exposure.
2. **Choose the guidance level provisionally.** If learners are task-specific novices and the target content cannot be reached from what they know, plan explicit guidance (resources that carry the content, prompts, worked or modelled steps) rather than leaving the content to be discovered. If learners can generate several partial solutions, a bounded problem-first phase followed by consolidating instruction is a candidate.
3. **Run the problem phase with contingent facilitation.** Increase support when a learner or group is stuck, reduce it when they progress; record each intervention. Ask learners to make their solutions visible, including flawed ones.
4. **Consolidate.** Teach the canonical idea explicitly, building on and contrasting with the solutions learners produced. Do not treat the consolidation as optional: the problem-first evidence concerns problem solving *followed by* instruction.
5. **Reobserve individually.** Use a new problem or a changed condition, scored separately for concept, transfer and procedure, at the agreed horizon. If the response disagrees with the expectation, revise the interpretation or the configuration.

| Observation | Discriminating probe | Proposed action, with its uncertainty |
|---|---|---|
| Learners cannot frame the problem or list learning issues | Re-present the problem in a familiar representation or with a model of a finished product; ask for a first decision only. | If a familiar framing releases a start, the barrier may be access or representation: adjust the problem. If not, supply the missing content explicitly before continuing. Neither branch is a validated diagnosis. |
| Group is active, but solutions do not use the target concept | Ask what idea the solution depends on; check whether the problem as written requires the concept. | If the concept is not required, revise the problem. If it is required and absent, move consolidation earlier or add a targeted resource. Activity alone does not show learning. |
| Several varied, partly wrong solutions generated | Ask learners to compare two of their solutions and say what each assumes. | Proceed to consolidating instruction that contrasts these solutions with the canonical one. The claim page places the effect mostly in well-structured domains such as mathematics, and its synthesis reports a reversal for second to fifth graders. |
| Strong group product, weak individual explanation | Individual explanation or changed-condition task, matched in demand. | Add individual accountability and individual practice; record who contributed what. Do not read the group score as each member's. |
| Conceptual probe passed, routine procedure failed | Score procedure separately under the same conditions. | Add targeted procedural practice; the problem-first evidence records no procedural advantage, so this is expected rather than a failure of the policy. |

## Choosing configurations from evidence

- **Order of problem and instruction.** For conceptual and transfer outcomes, [a problem-first phase followed by instruction](../claims/productive-failure-improves-conceptual-learning.md) [~S] has meta-analytic support over the same instruction taught first, with no procedural difference and a reversal for second to fifth graders and for domain-general skills. Choose it only with a consolidation phase, for learners old enough, and judge it on conceptual and transfer measures. The claim page reports no delayed-horizon breakdown.
- **Amount of guidance.** For novices, [unassisted discovery underperforms explicit instruction, while enhanced discovery outperforms other instruction](../claims/minimal-guidance-less-effective-for-novices.md) [-S]. This rules out a configuration in which essential content is left for novices to find unsupported; it does not rule out guided problem work. The meta-analysis is not broken down by prior knowledge on the claim page.
- **Facilitation.** [Contingent scaffolding](../claims/contingent-scaffolding-improves-learning.md) [+M] (support raised after failure, lowered after success) outperformed fixed or absent support in small one-to-one tutoring studies, with better transfer in one. It is a candidate rule for a facilitator, not a tested result in PBL groups.
- **Case-based formats.** [Case-based learning](../claims/case-based-learning-improves-exam-performance.md) [~M] raised exam scores in one non-randomized biology cohort, while a systematic review in health professional education found the evidence on learning inconclusive and noted that gains may come from group work. Do not expect a case or problem format alone to carry the effect.

Do not rank these results against one another: their comparators (instruction-first, explicit instruction, fixed support, lecture and reading) and outcomes differ. A precise abstention names the missing comparison, outcome or observation and the next way to resolve it.

## Further evidence, not yet read against this model
<!-- Restored 2026-10-01 (maintainer's decision): claims this page cited before the 2026-10-01 rewrite, which kept only claims whose sources it had re-read. Each marker keeps its old direction, capped by the claim's recorded evidence (strength_cap); each label says how far the claim's own entries have been checked against their sources by check_load_bearing.py. None has been re-read for the conditional model above, so treat them as candidates for it, not as part of it. -->
Claims this page cited before it was rewritten as a conditional model. They are evidence about the relationship, but none has yet been re-read against the model above; each says how far its own sources have been checked.

- [Whole-task performance improves transfer of complex skills to real-world settings.](../claims/whole-task-performance-improves-transfer.md) [+M] — checked by the judge: all 1 entries pass (abstract)

## Illustrative design instance and observation record

*Illustration only, invented, not a tested lesson.* An adult evening class in community health is given a problem: a neighbourhood's clinic reports rising missed appointments. The designer's objective is that learners can explain and apply a model of barriers to access; one learner says she wants to be able to argue for a change at her own workplace. Agree that both an individual explanation of the model and a defensible proposal matter. Ask each learner for a first framing; note that most list causes from experience but none names a structural barrier. Give a short resource on the model, let groups generate competing explanations, then teach the model explicitly against their explanations. Assess individually with a changed case a week later, separately for explanation and proposal.

Record: **problem and its framing → each learner's first response → resources, guidance and facilitation actually given, with timing → solutions generated → candidate interpretations and confidence basis → distinguishing probe → consolidation delivered → individual next observation at the stated horizon**. Preserve the learner's stated purpose and any change in it. An agent may summarize this record but must not fabricate missing inputs or assign numerical state probabilities without a calibrated model.

## Elements and limits

[Problem-based learning](../elements/problem-based-learning.md), [problem scenario](../elements/problem-scenario.md), [solution development](../elements/solution-development.md), [invention](../elements/invention.md), [scaffolding](../elements/scaffolding.md), [case-based learning](../elements/case-based-learning.md), [group roles](../elements/group-roles.md), [feedback](../elements/feedback.md) and [reflection](../elements/reflection.md).

This pattern is scoped to problem-centred units in which an explicit consolidation of target content is planned. Fully self-directed inquiry with no consolidation, assessment of whole PBL curricula, and learner groups below the ages in the evidence need distinct configurations and evidence. The wiki records no direct comparison of whole PBL curricula with conventional instruction, and the diagnostic branches above remain to be tested with actual learners.

## Related Patterns
- [Problem-Based Learning (PBL)](problem-based-learning-pbl.md)

## Examples
- A unit organized around diagnosing and responding to a realistic problem case.

## Key Sources
- Hmelo-Silver, C. E. (2004). Problem-based learning: What and how do students learn? *Educational Psychology Review, 16*(3), 235-266. [https://doi.org/10.1023/B:EDPR.0000034022.16470.f3](https://doi.org/10.1023/B:EDPR.0000034022.16470.f3)

<!-- deprecated 2026-10-01: superseded by the conditional model above. Old body kept verbatim.

## Description
Problem-Based Learning uses an authentic or ill-structured problem to drive inquiry, knowledge building, and solution development. This page serves as the canonical short-form target for links that refer to PBL without the explicit acronym.

## Implications

### Context
#### Requirements
- **A meaningful problem**
- **Learner investigation and solution development**
- **Facilitation and feedback**
#### Constraints
- **Novices may require more guidance**
- **Problems must be authentic enough to sustain inquiry**
#### Grain Size
- Unit
- Course

### Target Goals
- Drive learning through inquiry, explanation, and application.

### Target Learners
- Learners building applied reasoning and collaborative problem solving.

### Theory
#### Supporting
- [Problem-based Learning](../principles/problem-based-learning.md)
- [Constructivism](../principles/constructivism.md)

### Claims
- [Whole-task performance improves transfer of complex skills to real-world settings.](../claims/whole-task-performance-improves-transfer.md) [+S]

## Design

### Sequence
1. Present an authentic problem.
2. Identify what needs to be known.
3. Investigate and develop possible solutions.
4. Test, justify, and refine a response.

### Elements Used
- [Problem-Based Learning](../elements/problem-based-learning.md)
- [Problem Scenario](../elements/problem-scenario.md)
- [Solution Development](../elements/solution-development.md)

### Affordances
- [Problem-based Learning](../principles/problem-based-learning.md)
- [Active Learning](../principles/active-learning.md)
-->

---
type: pattern
id: problem-based-learning
aliases: [problem-based-learning-pbl]
title: Problem-Based Learning
description: "A reusable policy for problem-centred units: establish what learners already know of the target content, guide novices explicitly, use a problem-first phase only where learners can generate partial solutions and instruction follows, and judge the unit on individual outcomes."
status: review
generated:
  by: claude/unspecified
  at: 2026-10-01
sources:
  - id: hmelo-silver-2004
    resource: "https://doi.org/10.1023/B:EDPR.0000034022.16470.f3"
    title: "Hmelo-Silver, C. E. (2004). Problem-based learning: What and how do students learn? *Educational Psychology Review, 16*(3), 235-266"
    author: Hmelo-Silver, C. E
  - id: savery-2006
    resource: "https://doi.org/10.7771/1541-5015.1002"
    title: "Savery, J. R. (2006). Overview of problem-based learning: Definitions and distinctions. *Interdisciplinary Journal of Problem-Based Learning, 1*(1), 9-20"
    author: Savery, J. R
author: PBL tradition
grain_size: unit
---

# Problem-Based Learning

> **Pattern** · [All patterns](index.md)
> **Evidence** · 12 claims (3 for, 8 mixed, 1 against) · 18 studies (7 causal, 4 quant-synthesis, 3 review, 2 qualitative, 2 theoretical), `q2`–`q4` · 2 of 18 report an effect size · 7 claims rest on one study

## Description and scope

A reusable policy for organizing a unit around a problem that learners must investigate, deciding how much guidance to give and when, and reading what learners do with the problem. It instantiates the [conditional principle](../principles/problem-based-learning.md). The study configurations below are evidence; the response-dependent policy is an **untested design proposal**. Use it to gather better evidence about a learner group, not to certify that a learner is "ready for open problems".

The pattern is general across domains. A course for a particular setting (a medical curriculum, a primary science unit) is a design that may use it; the longer description of the tradition, from the former `problem-based-learning-pbl` page, is kept in the merged block at the end of this page.

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
2. **Choose the guidance level provisionally.** Default for task-specific novices on the target content: make the content explicit (a short explanation, a worked or modelled example, resources that carry it) before or alongside the problem, and use the problem to apply and connect it. A problem-first phase is a narrower candidate, for learners who can generate several partial solutions from what they already know, always followed by consolidating instruction. Do not adopt PBL on its label: the average curriculum-level effect is small and varies widely, so the configuration decides.
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

- **Whether to expect anything from the PBL label.** [The overall effect in a 353-outcome re-analysis is modest (g = 0.27)](../claims/pbl-overall-effect-modest-large-heterogeneity.md) [~M], [ranges from g = −1.26 to 1.91](../claims/massive-range-pbl-outcome-effect-sizes.md) [~M] and [may be inflated by publication bias (g = 0.103 after trim-and-fill)](../claims/publication-bias-pbl-tutor-meta-analysis.md) [~M]. Plan and evaluate the specific configuration; do not promise a gain from the format.
- **Who facilitates.** [Tutor background did not predict learning](../claims/tutor-background-meta-regression-not-predictive.md) [~M] in the same data. Prepare facilitators in the guidance and consolidation moves below rather than relying on content expertise or its absence; whether facilitation training itself changes outcomes is not recorded in the wiki.
- **Amount of guidance.** For novices, [unassisted discovery underperforms explicit instruction, while enhanced discovery outperforms other instruction](../claims/minimal-guidance-less-effective-for-novices.md) [-S]. This rules out a configuration in which essential content is left for novices to find unsupported; it does not rule out guided problem work. The meta-analysis is not broken down by prior knowledge on the claim page.
- **Order of problem and instruction.** For conceptual and transfer outcomes, [a problem-first phase followed by instruction](../claims/productive-failure-improves-conceptual-learning.md) [~S] has meta-analytic support over the same instruction taught first, with no procedural difference and a reversal for second to fifth graders and for domain-general skills. Choose it only with a consolidation phase, for learners old enough, and judge it on conceptual and transfer measures. The claim page reports no delayed-horizon breakdown.
- **Facilitation.** [Contingent scaffolding](../claims/contingent-scaffolding-improves-learning.md) [+M] (support raised after failure, lowered after success) outperformed fixed or absent support in small one-to-one tutoring studies, with better transfer in one. It is a candidate rule for a facilitator, not a tested result in PBL groups.
- **Case-based formats.** [Case-based learning](../claims/case-based-learning-improves-exam-performance.md) [~M] raised exam scores in one non-randomized biology cohort, while a systematic review in health professional education found the evidence on learning inconclusive and noted that gains may come from group work. Do not expect a case or problem format alone to carry the effect.

Do not rank these results against one another: their comparators (instruction-first, explicit instruction, fixed support, lecture and reading) and outcomes differ. A precise abstention names the missing comparison, outcome or observation and the next way to resolve it.

## Further evidence, not yet read against this model
<!-- Restored 2026-10-01 (maintainer's decision): claims this page cited before the 2026-10-01 rewrite, which kept only claims whose sources it had re-read. Each marker keeps its old direction, capped by the claim's recorded evidence (strength_cap); each label says how far the claim's own entries have been checked against their sources by check_load_bearing.py. None has been re-read for the conditional model above, so treat them as candidates for it, not as part of it. -->
Claims this page cited before it was rewritten as a conditional model. They are evidence about the relationship, but none has yet been re-read against the model above; each says how far its own sources have been checked.

- [A training-design argument, not tested by any study recorded here, holds that practising whole complex tasks improves transfer of complex skills](../claims/whole-task-performance-improves-transfer.md) [+M] — checked by the judge: all 1 entries pass (abstract)
- [Process goals lead to better skill acquisition for novices than outcome goals.](../claims/process-goals-outperform-outcome-goals-for-novices.md) [~M] — not settled: the text available could not confirm the entries (abstract)
- [Spontaneous responsiveness to real-world events in PBL can deepen student-directed inquiry beyond what designed curriculum achieves](../claims/spontaneous-authenticity-in-pbl-deepens-student-directed-inquiry.md) [+W] — a single case study found that a teacher's in-the-moment departure from the written PBL sequence, to respond to an unplanned real-world event tied to the driving question, produced deeper student-initiated inquiry than the pre-designed ("contrived") authentic scenario; not yet checked against its sources
- [Part-task practice reduces cognitive load for absolute novices during initial skill acquisition.](../claims/part-task-practice-reduces-load-for-novices.md) [~M] — not yet checked against its sources

## Illustrative design instance and observation record

*Illustration only, invented, not a tested lesson.* An adult evening class in community health is given a problem: a neighbourhood's clinic reports rising missed appointments. The designer's objective is that learners can explain and apply a model of barriers to access; one learner says she wants to be able to argue for a change at her own workplace. Agree that both an individual explanation of the model and a defensible proposal matter. Ask each learner for a first framing; note that most list causes from experience but none names a structural barrier. Give a short resource on the model, let groups generate competing explanations, then teach the model explicitly against their explanations. Assess individually with a changed case a week later, separately for explanation and proposal.

Record: **problem and its framing → each learner's first response → resources, guidance and facilitation actually given, with timing → solutions generated → candidate interpretations and confidence basis → distinguishing probe → consolidation delivered → individual next observation at the stated horizon**. Preserve the learner's stated purpose and any change in it. An agent may summarize this record but must not fabricate missing inputs or assign numerical state probabilities without a calibrated model.

## Elements and limits

[Problem-based learning](../elements/problem-based-learning.md), [problem scenario](../elements/problem-scenario.md), [solution development](../elements/solution-development.md), [invention](../elements/invention.md), [scaffolding](../elements/scaffolding.md), [case-based learning](../elements/case-based-learning.md), [group roles](../elements/group-roles.md), [feedback](../elements/feedback.md) and [reflection](../elements/reflection.md).

This pattern is scoped to problem-centred units in which an explicit consolidation of target content is planned. Fully self-directed inquiry with no consolidation, assessment of whole PBL curricula, and learner groups below the ages in the evidence need distinct configurations and evidence. The wiki records no direct comparison of whole PBL curricula with conventional instruction, and the diagnostic branches above remain to be tested with actual learners.

## Related Patterns
- [Anchored Instruction](anchored-instruction.md)
- [Case-Based Learning (Harvard Method)](case-based-learning-harvard-method.md)
- [Interdisciplinary Societal Dilemma Units](../designs/interdisciplinary-societal-dilemma-units.md) — a variant specific to civic/societal dilemmas spanning named disciplines
- [Organization Simulation for Interdisciplinary Learning](../designs/organization-simulation-for-interdisciplinary-learning.md) — adds a competitive external evaluator and organizational role structure to the authentic-problem, facilitated-inquiry core
- [Interdisciplinary Course-Based Research Experience](interdisciplinary-course-based-research-experience.md) — organizes inquiry around a recurring shared object rather than a single driving problem
- [Bioart Boundary-Crossing Making](../designs/bioart-boundary-crossing-making.md) — organizes inquiry around progressive institutional access and material engagement
- [Learning by Producing (multimedia production as learning)](learning-by-producing-pattern.md)

## Examples
- A unit organized around diagnosing and responding to a realistic problem case.
- Medical learners diagnosing and responding to a patient scenario.
- Business learners working through a complex organizational case.
- Engineering or civic learners designing responses to a local real-world problem.

## Key Sources
- Hmelo-Silver, C. E. (2004). Problem-based learning: What and how do students learn? *Educational Psychology Review, 16*(3), 235-266. [https://doi.org/10.1023/B:EDPR.0000034022.16470.f3](https://doi.org/10.1023/B:EDPR.0000034022.16470.f3)
- Barrows, H. S., & Tamblyn, R. M. (1980). *Problem-based learning: An approach to medical education*. Springer.
- Savery, J. R. (2006). Overview of problem-based learning: Definitions and distinctions. *Interdisciplinary Journal of Problem-Based Learning, 1*(1), 9-20. [https://doi.org/10.7771/1541-5015.1002](https://doi.org/10.7771/1541-5015.1002)

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

<!-- deprecated 2026-10-02: superseded after the brief test, which found answers following the previous version into problem-first designs for novices.

2. **Choose the guidance level provisionally.** If learners are task-specific novices and the target content cannot be reached from what they know, plan explicit guidance (resources that carry the content, prompts, worked or modelled steps) rather than leaving the content to be discovered. If learners can generate several partial solutions, a bounded problem-first phase followed by consolidating instruction is a candidate.
-->

<!-- merged 2026-10-02 from patterns/problem-based-learning-pbl ("Problem-Based Learning (PBL)"), a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Problem-Based Learning (PBL)

> **Pattern** · [All patterns](index.md)
> **Evidence** · 5 claims (3 for, 2 mixed) · 10 studies (4 causal, 2 qualitative, 2 theoretical, 1 quant-synthesis, 1 review), `q2`–`q4` · 0 of 10 report an effect size · 3 claims rest on one study

## Description
Problem-Based Learning is a pattern that organizes a course, unit, or module around a complex problem that learners must investigate and respond to. Instead of teaching all required content first, the pattern uses the problem to generate the need for inquiry, evidence gathering, collaboration, and explanation. Learners identify what they need to know, research relevant information, test ideas, and refine proposed responses.

The pattern is strongest when the problem is authentic enough to matter and the facilitation is strong enough to keep the inquiry rigorous. It is not equivalent to minimal guidance. Good PBL is structured, coached, and accountable.

## Implications

### Context
#### Requirements
- **A meaningful ill-structured problem**: The problem should require interpretation, inquiry, and judgment.
- **Access to evidence and resources**: Learners need materials, data, cases, or sources they can investigate.
- **Facilitated inquiry**: Instructors need to scaffold process and evidence use without taking over the problem.
- **A decision, proposal, or product**: Learners should arrive at some defended response to the problem.
#### Constraints
- **Novice overload**: Learners with limited background may need more direct support or preteaching.
- **Busy-work risk**: Inquiry can become shallow if evidence use and synthesis expectations are weak.
- **Time intensity**: PBL usually takes longer than direct explanation-first instruction.
- **Coordination demands**: Group work can mask uneven understanding unless roles and accountability are designed clearly.
#### Grain Size
- Unit
- Course

### Target Goals
- **Problem solving and reasoning**: Applying knowledge to ambiguous situations.
- **Evidence-based inquiry**: Identifying what must be learned and using sources purposefully.
- **Transfer**: Learning in ways that resemble authentic future use.

### Target Learners
- **Higher education, adult, and professional learners**: Strong fit where authenticity and application matter.
- **Learners developing self-directed inquiry habits**: PBL builds planning, monitoring, and revision.
- **Collaborative groups**: The pattern benefits from distributed reasoning and shared investigation.

### Theory
#### Supporting
- Constructivist perspectives — learners build understanding through engagement with a meaningful problem.
- Situated and experiential learning traditions — realistic contexts improve relevance and application.
- Self-regulated learning perspectives — extended problem work requires planning, monitoring, and adaptation.
#### Contradicting / Qualifying
- Some foundational objectives are learned more efficiently through explicit instruction before or during PBL.
- The pattern depends on facilitation; unguided open-ended work is not the same thing.
- Written PBL curricula design authenticity in advance ("contrived" authenticity), but the strongest engagement in one case study came from a teacher's spontaneous departure from the script to respond to a real event — suggesting curriculum flexibility and teacher autonomy matter as much as the designed scenario itself.

### Claims
#### Supporting
- [Whole-task performance improves transfer of complex skills to real-world settings.](../claims/whole-task-performance-improves-transfer.md) [+S]
- [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [+M]
- [Process goals lead to better skill acquisition for novices than outcome goals.](../claims/process-goals-outperform-outcome-goals-for-novices.md) [~M]
- [Spontaneous responsiveness to real-world events in PBL can deepen student-directed inquiry beyond what designed curriculum achieves](../claims/spontaneous-authenticity-in-pbl-deepens-student-directed-inquiry.md) [+W] — a single case study found that a teacher's in-the-moment departure from the written PBL sequence, to respond to an unplanned real-world event tied to the driving question, produced deeper student-initiated inquiry than the pre-designed ("contrived") authentic scenario
#### Contradicting
- [Part-task practice reduces cognitive load for absolute novices during initial skill acquisition.](../claims/part-task-practice-reduces-load-for-novices.md) [~M]

## Design

### Sequence
1. Introduce a complex authentic problem.
2. Have learners identify what they know, what they need to know, and how they will investigate.
3. Support inquiry, evidence gathering, and collaborative reasoning.
4. Ask learners to propose and justify a response, solution, or recommendation.
5. Debrief what was learned about both the problem and the inquiry process.

### Elements Used
- [Problem Presentation](../elements/problem-presentation.md)
- [Inquiry and Research](../elements/inquiry-and-research.md)
- [Problem-Solving Tasks](../elements/problem-solving-tasks.md)
- [Reflection](../elements/reflection.md)

### Affordances
- [Problem-based Learning](../principles/problem-based-learning.md)
- [Inquiry-based Learning](../principles/inquiry-based-learning.md)
- [Authentic Audiences & Purposes](../principles/authentic-audiences-purposes.md)
- [Guided Practice](../principles/guided-practice.md)

### Personalization
- Problems can be selected or adapted for learner context and domain.
- Inquiry supports can be heavier for novices and lighter for more experienced learners.
- Products can vary, including presentations, proposals, designs, or cases.

## Related Patterns

- [Anchored Instruction](anchored-instruction.md)
- [Case-Based Learning (Harvard Method)](case-based-learning-harvard-method.md)
- [Interdisciplinary Societal Dilemma Units](../designs/interdisciplinary-societal-dilemma-units.md) — a variant specific to civic/societal dilemmas spanning named disciplines
- [Organization Simulation for Interdisciplinary Learning](../designs/organization-simulation-for-interdisciplinary-learning.md) — adds a competitive external evaluator and organizational role structure to the authentic-problem, facilitated-inquiry core
- [Interdisciplinary Course-Based Research Experience](interdisciplinary-course-based-research-experience.md) — organizes inquiry around a recurring shared object rather than a single driving problem
- [Bioart Boundary-Crossing Making](../designs/bioart-boundary-crossing-making.md) — organizes inquiry around progressive institutional access and material engagement
- [Learning by Producing (multimedia production as learning)](learning-by-producing-pattern.md)

## Examples
- Medical learners diagnosing and responding to a patient scenario.
- Business learners working through a complex organizational case.
- Engineering or civic learners designing responses to a local real-world problem.

## Impact
- Strong pattern for integrating inquiry, collaboration, and authentic transfer.
- Most effective when the problem is real enough to matter and the facilitation is strong enough to prevent drift.

## Key Sources
- Barrows, H. S., & Tamblyn, R. M. (1980). *Problem-based learning: An approach to medical education*. Springer.
- Hmelo-Silver, C. E. (2004). Problem-based learning: What and how do students learn? *Educational Psychology Review, 16*(3), 235-266. [https://doi.org/10.1023/B:EDPR.0000034022.16470.f3](https://doi.org/10.1023/B:EDPR.0000034022.16470.f3)
- Savery, J. R. (2006). Overview of problem-based learning: Definitions and distinctions. *Interdisciplinary Journal of Problem-Based Learning, 1*(1), 9-20. [https://doi.org/10.7771/1541-5015.1002](https://doi.org/10.7771/1541-5015.1002)
-->

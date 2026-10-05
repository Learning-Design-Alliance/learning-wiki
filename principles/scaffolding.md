---
type: principle
id: scaffolding
title: Scaffolding
description: "Temporary support given while a learner attempts a task they cannot yet complete alone may improve later cognitive outcomes compared with unsupported attempts, qualified by the learner's task-specific starting response, the kind of support, the setting and whether the outcome is measured without the support."
status: review
generated:
  by: claude/unspecified
  at: 2026-10-02
sources:
  - id: wood-1976
    resource: "https://doi.org/10.1111/j.1469-7610.1976.tb00381.x"
    title: "Wood, D., Bruner, J. S., & Ross, G. (1976). The role of tutoring in problem solving. *Journal of Child Psychology and Psychiatry, 17*(2), 89-100"
    author: "Wood, D., Bruner, J. S., & Ross, G"
---

# Scaffolding

> **Principle** · [All principles](index.md)
> **Evidence** · 6 claims (3 for, 2 mixed, 1 against) · 12 studies (4 causal, 3 quant-synthesis, 3 review, 1 qualitative, 1 theoretical), `q1`–`q4` · 2 of 12 report an effect size · 1 claim rests on one study

## Conditional relationship

A learner who cannot yet complete a task alone may learn more from attempting it **with support** than from attempting it unsupported. Support here means hints, prompts, models, partial structures or tutor questions given during the attempt. The expected change is in later cognitive outcomes on the target task (`immediate-performance`, `near-transfer`, `conceptual-understanding`), not in how well the learner does while the support is present. The relationship is bounded by the learner's starting response on *this* task (`novice` for the task, not for the domain), by the kind of support and what it leaves the learner to do, by the setting (most evidence is one-to-one tutoring or computer-based support in STEM problem solving; little is `classroom`), and by whether the outcome is measured with the support removed.

This page owns the general relationship: support versus none. The [Scaffolding and Fading](scaffolding-and-fading.md) principle holds a narrower model inside it, in which support is **contingent** (raised after failure, lowered after success) and then **withdrawn**, and the outcome is unassisted performance. Whether support must be contingent and must fade to help is a question that page treats; the evidence below does not settle it, and one synthesis found no difference by fading. The [cognitive apprenticeship pattern](../patterns/cognitive-apprenticeship.md) is a reusable policy built on that narrower model.

## Observation, state and explanation

What can be observed is a response under stated conditions: what the learner attempted, which support was available or given (record its kind and how much of the task it did), whether the learner used it, and what they produced. "Cannot yet do it alone" and "can do it with help" are inferred states, and each depends on the task and on the support offered. A support can make a task easier by doing part of it for the learner; success then shows what the learner and the support did together, not what the learner has learned.

| Response | Plausible explanations | Observation that could change the interpretation |
|---|---|---|
| Fails the task unsupported, succeeds with a prompt | The prompt cued knowledge the learner already had; the prompt supplied the missing step; the unsupported attempt failed for a reason unrelated to the step (instructions, access, time) | Give a matched task with a weaker cue (a question, not the step) and record which level is enough; check the unsupported attempt's instructions and response mode. |
| Fails even with support | The task is too far beyond the learner's current knowledge for this support to bridge; the support is the wrong kind (structuring when the gap is a concept); the learner did not read or use it | Ask the learner to say what the support tells them to do; try a different kind of support on a simpler component of the same task. |
| Succeeds with support but cannot explain the result | The support did the reasoning and the learner followed it; the learner has the procedure without its rationale; a language or expression barrier | Ask for an explanation in an accessible mode, and pose a changed case the followed steps would not solve. |
| Does as well without the support as with it, or worse with it | The support is redundant for this learner (expertise reversal); the support adds reading or split attention; the learner ignored it | Offer the task with support optional; record whether it is used and whether accuracy or time changes. |
| Takes every support offered | The learner needs it; the learner values finishing over independence; using support carries no cost while trying alone does | Ask privately what the learner is aiming for; vary whether support is on request or automatic on a matched task. |

These rows are proposals for interpreting a response; none has been tested with learners as a diagnostic. A probe is itself practice and can change the state it measures, so record each one. Keep the explanations that remain open rather than choosing the one whose name fits.

## Evidence and qualifications

- [Scaffolding improves learning](../claims/scaffolding-improves-learning.md) [+M]. A random-effects meta-analysis of 144 experimental studies (333 outcomes) of computer-based scaffolding for STEM learners from primary school through adult education, working in ill-structured, problem-centred curricula, reports a positive effect on cognitive outcomes (ĝ = 0.46). The effect did not differ by context-specificity or by whether or how scaffolding was faded, and was greatest at the level of principles and among adult learners. A systematic review of teacher–student scaffolding (1998–2009) found 8 controlled effectiveness studies, mostly small one-to-one tutoring experiments on simple, well-structured tasks, favouring scaffolded or contingent conditions over no or less-contingent support, with no pooled effect and thin classroom evidence. This is the most direct support for the support-versus-none relationship. A pooled program-level effect forecasts no individual learner's response, and the comparison conditions are not described on the claim page. Not yet checked against its sources. The claim's opening sentence says the benefit holds "provided the support is faded", which its own meta-analysis entry does not show.
- [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [+M]. In one-to-one long-division tutoring (fourth and fifth graders, 8 per condition, coded as a quasi-experiment), fully contingent support beat moderate, high, partly contingent and no support at an immediate and a one-month test. With 11 tutor–student pairs (grade 8, the circulatory system), more interactive tutoring gave similar immediate learning but better transfer. A meta-analysis of dynamic assessment ranked explicit strategy training above scaffolding and scaffolding above coaching. Not settled: the abstracts could not confirm the entries. It supports support over none in tutoring; it does not show a classroom-scale effect, and it does not show that scaffolding beats explicit strategy instruction.
- [Human tutoring has a medium effect over no tutoring, and in one small study students learned as well when tutors only prompted them as when tutors also explained and gave feedback](../claims/tutoring-effectiveness-comes-from-scaffolding-and-feedback.md) [~M]. In one-to-one tutoring of 8th graders on the circulatory system (11 dyads per study), students whose tutors withheld explanations and feedback and only prompted learned as well as students in ordinary tutoring. A review of tutoring experiments reports human tutoring at d = 0.79 against no tutoring, close to intelligent tutoring systems at d = 0.76. The claim page itself says its evidence supports prompting-type scaffolding more than feedback as the active part, so its title overstates. It bears on which kind of support matters, not on support versus none in groups. Not settled: the abstracts could not confirm the entries.
- [Instructional guidance that helps novices can become redundant or counterproductive as expertise grows.](../claims/expertise-reversal-effect.md) [~M]. A synthesis of cognitive-load studies: integrated explanations, worked examples and step-by-step guidance help novices by reducing unnecessary search, and can become redundant for more knowledgeable learners, who may learn more efficiently from leaner tasks. This limits the relationship to learners for whom the task is new; it gives no criterion for when an individual has crossed over. Not settled: the abstract could not confirm the entry.
- [Teacher repetition and translation as unplanned scaffolding can hinder rather than facilitate learning](../claims/repetition-translation-scaffolding-hinders-learning.md) [-W]. A forum piece reports a study of teacher–student exchanges in Cypriot after-school language programmes in which teachers' repetition and translation, used as unplanned support, hindered learning. It is a second-hand report with no design details or outcome measure on the claim page, so it shows only that something called scaffolding can fail; it does not show when. Not yet checked against its sources.

The wiki has no claim that compares kinds of support (structuring the task versus simplifying it, procedural versus metacognitive prompts) on a common outcome, and none that tests scaffolding in whole classes against unsupported practice at a delayed horizon. Before transporting these observations, record the learners, setting (one-to-one, small group, computer-based), the support actually given and what it left to the learner, the comparator, outcome alignment and horizon. These studies do not rank one another; their comparisons differ.

## Further evidence, not yet read against this model
<!-- Restored 2026-10-02 (maintainer's decision): claims this page cited before the 2026-10-02 rewrite, which kept only claims whose sources it had re-read. Each marker keeps its old direction, capped by the claim's recorded evidence (strength_cap); each label says how far the claim's own entries have been checked against their sources by check_load_bearing.py. None has been re-read for the conditional model above, so treat them as candidates for it, not as part of it. -->
Claims this page cited before it was rewritten as a conditional model. They are evidence about the relationship, but none has yet been re-read against the model above; each says how far its own sources have been checked.

- [Fading support promotes the transfer of responsibility from instructor to learner.](../claims/fading-support-promotes-transfer-of-responsibility.md) [+S] — not settled: the text available could not confirm the entries (abstract)

## Objective and learner-valued goal

The designer's objective is usually a capability the learner shows without the support, on a representative task, at a stated horizon and with stated aids. The learner may value something else: getting this task done, not looking stuck, or the real-world result the task stands for. Ask what they want and why, and record it apart from the objective. A learner who values finishing may use every support; one who values independence may refuse support they still need. In both cases how support is used reflects the goal as well as competence.

For example, an adult returning to study may want to submit a correct statistics assignment this week, while the designer wants them to choose and justify an analysis alone in next term's project. A step-by-step prompt sheet serves the first aim and may hide whether the second has been met. Agree which aim the support is for, and check the second with an unsupported task later, not with the prompted one.

## What would revise this model?

The expectation should weaken if supported attempts fail to beat unsupported ones on aligned outcomes measured without the support, for comparable learners, outside one-to-one tutoring and computer-based STEM problem solving. It should also weaken if explicit strategy instruction matches or exceeds the gain at lower cost, as the dynamic-assessment synthesis suggests. If the benefit appears only while the support is present, the page is describing assisted performance, not learning, and should say so. If one kind of support (for example, support that does part of the task) consistently fails where another succeeds, the relationship belongs to that kind, not to support in general. Do not protect the model by relabelling every failure as "the wrong support" or "outside the zone of proximal development" after the outcome is seen.

Assisted performance, unassisted immediate performance, delayed retention, transfer and use in the learner's own setting are separate claims. The evidence above establishes no best kind or amount of support, no individual readiness criterion and no classroom-scale effect.

## Related Principles
- [Scaffolding and Fading](scaffolding-and-fading.md)

## Examples
- Hints, worked examples, modeling, and coaching that are reduced as competence grows.

## Key Sources
- Wood, D., Bruner, J. S., & Ross, G. (1976). The role of tutoring in problem solving. *Journal of Child Psychology and Psychiatry, 17*(2), 89-100. [https://doi.org/10.1111/j.1469-7610.1976.tb00381.x](https://doi.org/10.1111/j.1469-7610.1976.tb00381.x)

<!-- deprecated 2026-10-02: superseded by the conditional model above. The former body, kept verbatim:

## Description
Scaffolding is the principle of providing temporary support that helps learners perform beyond what they could do independently. This page serves as the canonical short-form target for links that refer to scaffolding without explicitly naming fading or transfer of responsibility.

## Implications
Scaffolding is useful when learners can succeed with support but not yet on their own. Well-calibrated prompts, hints, models, or partial structures can improve learning when they respond to the learner’s actual bottleneck [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [+M]. The design consequence is that scaffolding should be temporary: support that never fades can reduce independence, while support withdrawn too early can overload the learner [Fading support promotes the transfer of responsibility from instructor to learner.](../claims/fading-support-promotes-transfer-of-responsibility.md) [+S].

### Context
#### Requirements
- **A task slightly beyond independent reach**
- **Support calibrated to the learner's current need**
- **A plan to reduce support over time**
#### Constraints
- **Over-scaffolding can create dependence**
- **Premature withdrawal can trigger overload**

### Target Learners
- Learners building new concepts, procedures, or complex performances.

### Target Learning Objectives
- Support successful performance while developing independence.

### Theory
#### Supporting
- Sociocultural and apprenticeship traditions.
- [Cognitive Load Theory](../theories/cognitive-load-theory.md)

### Claims
- [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [+M] — support helps most when it is matched to the learner’s current difficulty
- [Fading support promotes the transfer of responsibility from instructor to learner.](../claims/fading-support-promotes-transfer-of-responsibility.md) [+S] — effective scaffolds are designed to hand more of the task back to the learner over time
-->

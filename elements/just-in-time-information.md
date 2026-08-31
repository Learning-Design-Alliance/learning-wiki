---
type: element
title: Just-in-Time Information
description: Instruction is provided at the point of need rather than upfront.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Just-in-Time Information

> **Element** · [All elements](index.md)

## Description
Just-in-time information presents explanatory content — procedures, concepts, feedback — at the moment the learner needs it to perform the current task step, rather than as a block of upfront instruction. The task comes first; information is delivered on demand or automatically triggered when the learner reaches a point where it is required.

## Design Implications

Delivering information at the point of need reduces the burden of holding unapplied content in working memory and improves the relevance and retrievability of what is learned [Presenting prerequisite information just before it is needed improves learning efficiency compared with presenting it upfront.](../claims/example-problem-sequences-reduce-cognitive-load.md) [+M]. In whole-task designs, supportive information is offered before the task while procedural information is embedded within it, appearing precisely at the step where it applies [Whole-task sequencing improves transfer compared with part-task sequencing.](../claims/whole-task-performance-improves-transfer.md) [+M]. The design decision is *when* to present: information given too early is forgotten or ignored; information given too late forces unproductive trial-and-error search.

### Context
#### Requirements
- A well-analyzed task sequence so the system or instructor knows *which* information is needed at *which* step
- On-demand access mechanisms: embedded hints, tooltips, help panels, or instructor circulation ([Coaching](coaching.md))
- Information formatted for quick uptake — concise, step-local, and action-oriented ([Procedural Information](procedural-information.md))
- A task complex enough that upfront instruction would overload learners; trivial tasks do not need it

#### Constraints
- Constant interruption with information fragments can fragment the learner's developing schema and disrupt understanding of the whole task [~M] — just-in-time presentation suits *procedural* information better than material requiring integrated conceptual understanding
- Learners who never request help miss critical information; on-demand systems depend on help-seeking behavior, which weaker learners often underuse [-M]
- Less effective when learners lack the prior knowledge to recognize *when* they need information — novices may not know what to ask for [~M]
- In self-paced e-learning, poorly timed pop-ups can split attention between the information and the task itself [~M]

### Target Learners
- Novices in complex, multi-step domains (STEM, software, statistics) where upfront instruction would exceed working memory capacity [Presenting prerequisite information just before it is needed improves learning efficiency compared with presenting it upfront.](../claims/example-problem-sequences-reduce-cognitive-load.md) [+M]
- Self-paced learners who can control when they request support
- Less beneficial for advanced learners, who can integrate upfront material efficiently and may find step-by-step prompting redundant [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M]

### Target Learning Goals
- Procedural skill acquisition: knowing how to execute each step as it arises
- Complex task performance in domains with high element interactivity
- Just-in-time scaffolding toward independent performance, with support fading over time

### Affordances
- [Cognitive Load Management](../principles/cognitive-load-management.md) — by deferring information until the task creates a slot for it, just-in-time presentation avoids forcing learners to hold unapplied content in working memory, directly enacting load-reduction principles
- [Cognitive Load Theory](../principles/cognitive-load-theory.md) — the timing distinction between supportive information (before the task) and procedural information (during the task) is a core CLT-based design prescription
- [Scaffolding](../principles/scaffolding.md) — just-in-time information is scaffolding in its most literal form: temporary, task-contingent support that should fade as competence grows ([Fading](fading.md))
- [Worked Examples](../principles/worked-examples.md) — worked examples with embedded completion steps deliver explanatory information exactly where the learner's own attempt begins [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+M]

## Related Elements
- [Scaffolding](scaffolding.md) — just-in-time information is the informational form of scaffolding; both require fading
- [Procedural Information](procedural-information.md) — the content type most suited to just-in-time delivery
- [Coaching](coaching.md) — the human-delivered mechanism for supplying information at the point of need
- [Demonstration](demonstration.md) — demonstrations can be triggered just-in-time when a learner reaches an unfamiliar step
- [Fading](fading.md) — the mechanism for withdrawing just-in-time support as expertise develops

## Patterns That Use This Element
- [Cognitive Apprenticeship](../patterns/cognitive-apprenticeship.md) — the coaching phase delivers hints and information as the learner works
- [4C/ID (Four-Component Instructional Design)](../patterns/4cid-four-component-instructional-design.md) — procedural information is explicitly designed to be presented just-in-time during learning tasks
- [Cognitive Load Reduction (CLT Scaffolding Approach)](../patterns/cognitive-load-reduction-clt-scaffolding-approach.md) — timing of information presentation is a primary load-management lever

## Examples
- **[Use Worked Examples](../strategies/use_worked_examples.md)** — completion problems embed explanatory information at the exact step where the learner takes over from the model.
- **[Khan Academy](https://www.khanacademy.org)** — hints in practice exercises reveal step-by-step information only when the learner requests it, delivering support at the point of need.
- **Codecademy ([https://www.codecademy.com](https://www.codecademy.com))** — contextual hints and documentation panels appear inline as learners write code, triggered by the current exercise step.
- **Duolingo ([https://www.duolingo.com](https://www.duolingo.com))** — grammar tips surface at the point in a lesson where the new structure is first encountered, rather than as upfront grammar lectures.

## Key Sources
- Kester, L., Kirschner, P. A., & van Merriënboer, J. J. G. (2004). Timing of information presentation in learning statistics. *Instructional Science, 32*(1–2), 1–29. [doi:10.1023/b:truc.0000024191.27560.e3](https://doi.org/10.1023/b:truc.0000024191.27560.e3)
- van Merriënboer, J. J. G., & Kirschner, P. A. (2018). *Ten steps to complex learning* (3rd ed.). Routledge.
- Mayer, R. E. (2009). *Multimedia learning* (2nd ed.). Cambridge University Press. [doi:10.1017/CBO9780511811678](https://doi.org/10.1017/CBO9780511811678)
- Renkl, A., & Atkinson, R. K. (2003). Structuring the transition from example study to problem solving in cognitive skill acquisition: A cognitive load perspective. *Educational Psychologist, 38*(1), 15–22. [doi:10.1207/S15326985EP3801_3](https://doi.org/10.1207/S15326985EP3801_3)
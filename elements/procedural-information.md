---
type: element
title: Procedural Information
description: Step-by-step instructions and just-in-time guidance to assist learners in acquiring procedural fluency.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
sources:
  - id: van-merrienboer-2002
    resource: "https://doi.org/10.1023/A:1015353406100"
    title: "van Merriënboer, J. J. G., Clark, R. E., & de Croock, M. B. M. (2002). Blueprints for complex learning: The 4C/ID-model. *Educational Psychology Review, 14*(1), 57–71"
    author: "van Merriënboer, J. J. G., Clark, R. E., & de Croock, M. B. M"
  - id: sweller-1985
    resource: "https://doi.org/10.1207/s1532690xci0201_3"
    title: "Sweller, J., & Cooper, G. A. (1985). The use of worked examples as a substitute for problem solving in learning algebra. *Cognition and Instruction, 2*(1), 59–89"
    author: "Sweller, J., & Cooper, G. A"
  - id: kester-2004
    resource: "https://doi.org/10.1023/A:1021814310356"
    title: "Kester, L., Kirschner, P. A., & van Merriënboer, J. J. G. (2004). Timing of information presentation in learning statistics. *Instructional Science, 32*(1), 31–52"
    author: "Kester, L., Kirschner, P. A., & van Merriënboer, J. J. G"
---

# Procedural Information

> **Element** · [All elements](index.md)

## Description
Procedural information provides step-by-step instructions — "how-to" guidance — that supports learners in performing the recurrent, algorithmic components of a task. In [Four-Component Instructional Design](../patterns/4cid-four-component-instructional-design.md) it is one of two forms of supportive information, presented *just in time* during task performance rather than up front, so that learners can act while consulting the steps rather than memorizing them first.

## Design Implications

Procedural information reduces the working-memory burden of executing routine task steps, freeing capacity for the non-recurrent reasoning that constitutes real learning [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+S]. It is most effective when delivered at the moment of need — embedded in the task interface or available on demand — rather than as a pre-task lecture, which forces learners to hold steps in memory before they can apply them [Pairing worked examples with practice or fading supports transfer better than examples alone.](../claims/worked-examples-with-practice-improve-transfer.md) [+M]. Presenting steps as small, ordered units with clear conditions for each action supports encoding into automated schemas [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+M].

### Context
#### Requirements
- A task analysis identifying the recurrent, rule-based components of the task (the "how" steps distinct from the "why" of [Mental Models](mental-models.md))
- Just-in-time delivery: steps available at the point of action, ideally in the task environment ([Performance Support](performance-support.md))
- Opportunities to apply the steps immediately, so guidance converts into fluency through [Practice](practice.md) and [Part-Task Practice](part-task-practice.md)
- A plan for fading: as steps become automated, the information should be withdrawn [Fading support promotes transfer of responsibility.](../claims/fading-support-promotes-transfer-of-responsibility.md) [+M]

#### Constraints
- Presenting all procedural detail before practice overloads novices and produces inert knowledge; just-in-time presentation outperforms just-in-case presentation [Timing of information presentation affects learning outcomes.](../claims/example-problem-sequences-reduce-cognitive-load.md) [~M]
- Over-reliance on step-by-step guidance can produce dependency: learners follow rules without understanding when they apply, harming transfer to variant tasks [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M]
- Poorly suited to non-recurrent, heuristic task aspects, where rigid steps mislead; those require [Mental Models](mental-models.md) and [Cognitive Strategies](cognitive-strategies.md) instead

### Target Learners
- Novices who lack automated procedures and would otherwise flounder in unguided search [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+M]
- Learners in vocational and technical training where correct execution of standard procedures is safety- or performance-critical
- Less beneficial for experienced learners, who find explicit step guidance redundant and may perform worse with it [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M]

### Target Learning Goals
- Procedural fluency: accurate, efficient execution of routine task steps
- Automation: converting deliberate steps into effortless routines through repeated guided practice [Part-task practice reduces load for novices.](../claims/part-task-practice-reduces-load-for-novices.md) [+M]
- Error reduction in rule-based task components

### Affordances
- [Cognitive Load Management](../principles/cognitive-load-management.md) — by externalizing routine steps, procedural information keeps learners from holding instructions in working memory while simultaneously performing the task, reserving capacity for schema construction
- [Scaffolding](../principles/scaffolding.md) — procedural information is a scaffold by design: it supports performance the learner cannot yet sustain alone and must be faded as steps automate
- [Worked Examples](../principles/worked-examples.md) — a worked example embeds procedural information in a demonstration; the annotated steps of the example *are* the procedure made visible [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+M]
- [Chunking](../principles/chunking.md) — effective procedural information groups steps into meaningful, ordered chunks matching the learner's processing capacity [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+S]

## Related Elements
- [Worked Examples](worked-examples.md) — procedural information instantiated in a fully worked demonstration
- [Practice](practice.md) — the application context in which guided steps become fluent, automated routines
- [Fading](fading.md) — the mechanism for withdrawing procedural support as expertise grows
- [Demonstration](demonstration.md) — the observed counterpart; procedural information is the same guidance in text or diagram form
- [Part-Task Practice](part-task-practice.md) — repetitive practice of recurrent task components to automation

## Patterns That Use This Element
- [Four-Component Instructional Design](../patterns/4cid-four-component-instructional-design.md) — procedural information is one of the four components, supporting recurrent task aspects
- [Cognitive Load Theory](../patterns/cognitive-load-theory.md) — just-in-time guidance manages intrinsic load during task performance
- [Gagné's 9 Events](../patterns/gagnés-9-events-of-instruction.md) — "provide learning guidance" and "eliciting performance" events

## Examples

**[4C/ID in statistics instruction](https://www.4cid.org)** — Kester, Kirschner, and van Merriënboer's experiments presented procedural "how-to" information just before learners performed each recurrent step of statistical analyses, improving performance over presenting the same information as a pre-task block.

**[Duolingo](https://www.duolingo.com)** — Grammar tips and inline hints deliver procedural rules at the moment a pattern first appears in an exercise, then withdraw them as items are mastered.

**[Microsoft Office contextual help / Clippy-style task guidance](https://support.microsoft.com)** — Step-by-step task instructions surfaced within the application at the point of need, a classic performance-support implementation of just-in-time procedural information.

## Key Sources
- van Merriënboer, J. J. G., Clark, R. E., & de Croock, M. B. M. (2002). Blueprints for complex learning: The 4C/ID-model. *Educational Psychology Review, 14*(1), 57–71. [doi:10.1023/A:1015353406100](https://doi.org/10.1023/A:1015353406100)
- Kester, L., Kirschner, P. A., & van Merriënboer, J. J. G. (2004). Timing of information presentation in learning statistics. *Instructional Science, 32*(1), 31–52. [doi:10.1023/b:truc.0000024191.27560.e3](https://doi.org/10.1023/b:truc.0000024191.27560.e3)
- Sweller, J., & Cooper, G. A. (1985). The use of worked examples as a substitute for problem solving in learning algebra. *Cognition and Instruction, 2*(1), 59–89. [doi:10.1207/s1532690xci0201_3](https://doi.org/10.1207/s1532690xci0201_3)
- van Merriënboer, J. J. G., & Kirschner, P. A. (2018). *Ten steps to complex learning* (3rd ed.). Routledge.
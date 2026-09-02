---
type: element
id: demonstration
title: Demonstration
description: A demonstration presents a complete or partial model of a skill, process, or solution so learners can observe expert performance before attempting it themselves.
status: review
generated:
  by: claude/unspecified
  at: 2026-04-06
sources:
  - id: sweller-1985
    resource: "https://doi.org/10.1207/s1532690xci0201_3"
    title: "Sweller, J., & Cooper, G. A. (1985). The use of worked examples as a substitute for problem solving in learning algebra. *Cognition and Instruction, 2*(1), 59–89"
    author: "Sweller, J., & Cooper, G. A"
  - id: clark-2016
    resource: "https://doi.org/10.1002/9781119239086"
    title: "Clark, R. C., & Mayer, R. E. (2016). *E-Learning and the Science of Instruction* (4th ed.). Wiley"
    author: "Clark, R. C., & Mayer, R. E"
  - id: van-gog-2010
    resource: "https://doi.org/10.1007/s10648-010-9134-7"
    title: "van Gog, T., & Rummel, N. (2010). Example-based learning: Integrating cognitive and social-cognitive research perspectives. *Educational Psychology Review, 22*(2), 155–174"
    author: "van Gog, T., & Rummel, N"
---

# Demonstration

> **Element** · [All elements](index.md)

## Description
A demonstration presents a complete or partial model of a skill, process, or solution so learners can observe expert performance before attempting it themselves. The instructor or system makes thinking visible — articulating what is being done and why — rather than simply showing the end result.

## Design Implications

Demonstrations reduce the cognitive burden of initial skill acquisition by giving learners a reference model to study and imitate [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+M]. Their value depends heavily on how thinking is made visible: narrated or annotated demonstrations that explain reasoning produce better learning than silent ones. Demonstrations should be followed by practice opportunities, since passive observation without application leads to shallow encoding [Pairing worked examples with practice or fading supports transfer better than examples alone.](../claims/worked-examples-with-practice-improve-transfer.md) [+S].

### Context
#### Requirements
- A clear, accurate model of the target performance
- Narration or annotation that makes reasoning explicit, not just actions ([Think-Aloud](think-aloud.md) or written commentary)
- A follow-on activity that requires learners to apply what they observed ([Practice](practice.md))

#### Constraints
- Passive observation without prompts or practice creates illusions of understanding [Pairing worked examples with practice or fading supports transfer better than examples alone.](../claims/worked-examples-with-practice-improve-transfer.md) [-S] — learners often overestimate how much they have learned from watching alone
- Less effective for open-ended or creative tasks where there is no single correct approach
- Can anchor learners to a single solution method; pairing with [Non-Examples](non-examples.md) or [Comparing Cases](comparing-cases.md) reduces this risk

### Target Learners
- Novices encountering a skill or process for the first time [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+M]
- Learners with limited prior knowledge who would otherwise spend effort on unguided search
- Less beneficial for learners with strong prior knowledge, who may find explicit modeling redundant [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M]

### Target Learning Goals
- Procedural skill acquisition: understanding the steps of a process
- Schema formation: building a mental model of task structure
- Metacognitive modeling: learning what expert monitoring and decision-making looks like

### Affordances
- [Worked Examples](../principles/worked-examples.md) — a demonstration applied to a problem-solving context enacts this principle by giving learners a complete solution to study before attempting their own; the worked example *is* the demonstration with added reasoning annotation
- [Explicit Instruction](../principles/explicit-instruction.md) — demonstration enacts this principle by having the expert narrate decisions aloud ("I'm choosing this approach because…"), converting tacit knowledge into observable, learnable steps rather than leaving learners to infer intent from outcomes
- [Cognitive Load Management](../principles/cognitive-load-management.md) — by externalizing each step of a task, demonstration lets learners attend to *understanding* the structure rather than holding intermediate states in working memory while simultaneously figuring out what to do next
- [Scaffolding](../principles/scaffolding.md) — a demonstration functions as temporary external structure; the key design decision is when and how to fade it — moving from full worked examples to partial examples to problem-only as competence grows

## Related Elements
- [Practice](practice.md) — the necessary follow-on; demonstration without practice rarely transfers
- [Think-Aloud](think-aloud.md) — the narration method that makes demonstration effective
- [Fading](fading.md) — progressively reduces the completeness of demonstrations as expertise grows
- [Non-Examples](non-examples.md) — contrasting a correct demonstration with a flawed one sharpens discrimination
- [Procedural Information](procedural-information.md) — text or diagram form of the same function

## Patterns That Use This Element
- [Cognitive Apprenticeship](../patterns/cognitive-apprenticeship.md) — modeling phase
- [Four-Component Instructional Design](../patterns/4cid-four-component-instructional-design.md) — worked examples as the demonstration component of learning tasks
- [Gagné's 9 Events](../patterns/gagnes-9-events-of-instruction.md) — "present the content" event

## Examples

**[Use Worked Examples](../strategies/use_worked_examples.md)** — Presents a fully solved problem with step-by-step reasoning, then asks learners to solve a similar problem. The worked example is the demonstration component.

**[Think-Aloud Modeling](../strategies/think-aloud-modeling.md)** — Instructor verbalizes their reasoning while solving a problem or reading a text, making metacognitive moves visible (monitoring confusion, checking work, revising approach).

**[Khan Academy](https://www.khanacademy.org)** — Video demonstrations with narrated step-by-step problem solving, followed by [practice exercises](practice.md) with hints. The hint system itself delivers sub-demonstrations on demand.

**[Codecademy](https://www.codecademy.com)** — Annotated code demonstrations inline with [coding exercises](practice.md); learners see a working example before writing their own version.

## Key Sources
- Sweller, J., & Cooper, G. A. (1985). The use of worked examples as a substitute for problem solving in learning algebra. *Cognition and Instruction, 2*(1), 59–89. [doi:10.1207/s1532690xci0201_3](https://doi.org/10.1207/s1532690xci0201_3)
- Clark, R. C., & Mayer, R. E. (2016). *E-Learning and the Science of Instruction* (4th ed.). Wiley. [doi:10.1002/9781119239086](https://doi.org/10.1002/9781119239086)
- Bandura, A. (1977). Social learning theory. *Englewood Cliffs, NJ: Prentice Hall.*
- van Gog, T., & Rummel, N. (2010). Example-based learning: Integrating cognitive and social-cognitive research perspectives. *Educational Psychology Review, 22*(2), 155–174. [doi:10.1007/s10648-010-9134-7](https://doi.org/10.1007/s10648-010-9134-7)


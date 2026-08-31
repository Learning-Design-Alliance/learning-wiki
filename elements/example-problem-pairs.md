---
type: element
title: Example Problem Pairs
description: An example problem pair presents a fully worked solution followed immediately by a similar problem for the learner to solve, alternating study of an example with practice on an isomorphic task.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Example Problem Pairs

> **Element** · [All elements](index.md)

## Description
An example problem pair pairs a fully worked example with a structurally identical (isomorphic) problem that the learner must solve immediately afterward. The learner studies the expert solution, then applies the same procedure to a near-transfer task, alternating example study and problem solving across a sequence.

## Design Implications

Example problem pairs reduce unguided search during early skill acquisition while guaranteeing that every example is followed by active application [Example–problem pairs lower cognitive load compared with solving all problems independently.](../claims/example-problem-sequences-reduce-cognitive-load.md) [+S]. The pairing is the critical design feature: examples alone produce passive study and illusions of competence, while problems alone impose search costs on novices; the alternation captures the benefit of both [Pairing worked examples with practice or fading supports transfer better than examples alone.](../claims/worked-examples-with-practice-improve-transfer.md) [+S]. Pairs should be structurally similar but superficially varied so learners abstract the underlying procedure rather than surface features.

### Context
#### Requirements
- A fully worked example with clear step-by-step reasoning ([Worked Examples](worked-examples.md))
- An isomorphic follow-up problem matched in solution structure
- Successive pairs that vary surface features while holding solution structure constant, to support schema abstraction
- Learner accountability for studying the example (e.g., self-explanation prompts or completion problems), since unexamined copying defeats the design

#### Constraints
- For learners with substantial prior knowledge, studying a full example is redundant and slows them relative to plain problem solving [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M] — the [expertise reversal effect](../theories/expertise-reversal-effect.md) applies directly to pair sequences
- If the follow-up problem is too dissimilar, learners cannot map the example onto it and revert to guessing
- Long uninterrupted example sequences without problems reduce engagement and processing depth [Pairing worked examples with practice or fading supports transfer better than examples alone.](../claims/worked-examples-with-practice-improve-transfer.md) [-S]
- Less suited to ill-structured domains where no single solution procedure transfers across problems

### Target Learners
- Novices in a structured domain (algebra, physics, programming, statistics) who lack schemas for the task type [Example–problem pairs lower cognitive load compared with solving all problems independently.](../claims/example-problem-sequences-reduce-cognitive-load.md) [+S]
- Learners prone to ineffective trial-and-error strategies under conventional problem sets
- Less beneficial for advanced learners, who should receive faded or problem-only sequences [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M]

### Target Learning Goals
- Procedural fluency: acquiring and automating a solution procedure
- Schema construction: recognizing which problem type a new problem belongs to
- Near transfer: applying a learned procedure to structurally identical problems

### Affordances
- [Worked Examples](../principles/worked-examples.md) — the example half of the pair *is* a worked example; the pair format is the canonical way of embedding worked examples in a practice sequence
- [Cognitive Load Management](../principles/cognitive-load-management.md) — the example eliminates means-ends search on the first task, freeing working memory for schema construction; the paired problem then consolidates it under moderate load
- [Scaffolding](../principles/scaffolding.md) — pairs are a starting point for a fading sequence: full example + problem → completion problem + problem → problem + problem as expertise grows ([Fading](fading.md))
- [Cognitive Apprenticeship](../principles/cognitive-apprenticeship.md) — the worked example functions as a model of expert solution behavior that learners immediately imitate in the paired task

## Related Elements
- [Worked Examples](worked-examples.md) — the example component of the pair
- [Fading](fading.md) — the natural next step once pairs have built initial competence
- [Practice](practice.md) — the problem component; pairs guarantee practice follows every example
- [Non-Examples](non-examples.md) — can replace the example in a pair to sharpen conceptual discrimination
- [Erroneous Examples](erroneous-examples.md) — a variant where the example contains an error for learners to diagnose

## Patterns That Use This Element
- [Cognitive Load Theory](../patterns/cognitive-load-theory.md) — the canonical example-based instruction sequence
- [Four-Component Instructional Design](../patterns/4cid-four-component-instructional-design.md) — supportive information and task classes built from example–task alternation
- [Direct Instruction](../patterns/direct-instruction.md) — model–guide–test structure mirrors example → pair → independent problems

## Examples

**[Use Worked Examples](../strategies/use_worked_examples.md)** — The general strategy of alternating fully solved problems with isomorphic practice problems; example problem pairs are its core unit.

**[Sweller & Cooper's algebra studies](https://doi.org/10.1207/s1532690xci0201_3)** — The original experimental paradigm: students studied a worked algebra example then solved a matched problem, outperforming problem-only peers on subsequent tests.

**[Khan Academy](https://www.khanacademy.org)** — Narrated example videos followed immediately by practice exercises of the same type, with on-demand hints that decompose the problem into completion steps.

**[Codecademy](https://www.codecademy.com)** — Annotated example code shown alongside an exercise where learners write structurally similar code, an example problem pair in a programming context.

## Key Sources
- Sweller, J., & Cooper, G. A. (1985). The use of worked examples as a substitute for problem solving in learning algebra. *Cognition and Instruction, 2*(1), 59–89. [doi:10.1207/s1532690xci0201_3](https://doi.org/10.1207/s1532690xci0201_3)
- Cooper, G., & Sweller, J. (1987). Effects of schema acquisition and rule automation on mathematical problem-solving transfer. *Journal of Educational Psychology, 79*(4), 347–362. [doi:10.1037/0022-0663.79.4.347](https://doi.org/10.1037/0022-0663.79.4.347)
- van Gog, T., & Rummel, N. (2010). Example-based learning: Integrating cognitive and social-cognitive research perspectives. *Educational Psychology Review, 22*(2), 155–174. [doi:10.1007/s10648-010-9134-7](https://doi.org/10.1007/s10648-010-9134-7)
- Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J. (2003). The expertise reversal effect. *Educational Psychologist, 38*(1), 23–31. [doi:10.1207/S15326985EP3801_4](https://doi.org/10.1207/S15326985EP3801_4)
- Renkl, A. (2014). Toward an instructionally oriented theory of example-based learning. *Cognitive Science, 38*(1), 1–37. [doi:10.1111/cogs.12086](https://doi.org/10.1111/cogs.12086)
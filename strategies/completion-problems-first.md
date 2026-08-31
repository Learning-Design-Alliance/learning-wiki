---
type: strategy
title: Completion Problems First
description: Learners begin with partially completed problems (completion problems) before moving to full problem solving, bridging worked examples and independent practice.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Completion Problems First

> **Strategy** · [All strategies](index.md)

## Description
Completion problems first is a sequencing strategy in which learners' earliest practice tasks are partially completed — some steps or solution states are given, and learners fill in the remainder. It operationalizes the *completion strategy* (van Merriënboer) as a bridge between studying full [worked examples](../principles/worked-examples.md) and solving problems unaided, implementing a smooth [fading](../elements/fading.md) of guidance rather than an abrupt transition.

## Design Implications

Completion problems reduce the unguided search that makes early problem solving inefficient for novices, while requiring more generative processing than passive example study [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+M]. Because learners must actively complete steps, the strategy avoids the shallow encoding and illusion of understanding that full-example study alone can produce [Pairing worked examples with practice or fading supports transfer better than examples alone.](../claims/worked-examples-with-practice-improve-transfer.md) [+S]. The design task is choosing *which* steps to omit: omit steps that isolate the goal-rule or decision being taught, and fade progressively as performance improves.

### Context
#### Requirements
- A set of high-quality worked examples establishing the full solution procedure first
- A task sequence that fades support: full example → completion problem (most steps given) → completion problem (few steps given) → full problem ([Fading](../elements/fading.md))
- Deliberate selection of which steps to blank — typically the steps carrying the learning goal, not arbitrary gaps
- Feedback or a correct model answer so learners can check their completions

#### Constraints
- If too many steps are omitted too early, learners revert to inefficient search strategies and cognitive overload [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) [-M]
- Blank steps that are trivial (e.g., routine arithmetic) add workload without promoting schema construction [~M]
- For learners with substantial prior knowledge, completion scaffolds become redundant and slow performance [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M]
- Without a model answer to compare against, learners may consolidate incorrect completions [-M]

#### Implementation Variability
- **Backward fading:** remove the last steps first (learners finish solutions), then earlier steps — common in mathematics tutoring
- **Forward fading:** remove early steps first, forcing learners to plan before executing
- **Completion within worked-example pairs:** alternate example study with an isomorphic completion problem (example–problem pairs)
- **Programmatic fading:** in adaptive systems such as [ASSISTments](https://www.assistments.org) or [Squirrel AI](https://www.squirrelai.com), the number of given steps adjusts to learner performance

### Target Learners
- Novices who lack the schemas to benefit from unguided problem solving [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+M]
- Learners who have studied worked examples but are not yet ready for independent problems
- Less appropriate for advanced learners, who perform better solving problems directly [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M]

### Target Learning Goals
- Procedural skill acquisition in well-structured domains (algebra, programming, statistics)
- Schema construction for recurring problem types
- Bridging toward transfer: faded completion supports application to novel variants [Pairing worked examples with practice or fading supports transfer better than examples alone.](../claims/worked-examples-with-practice-improve-transfer.md) [+S]

### Instructions
1. Present a fully worked example with reasoning made visible ([Think-Aloud](../elements/think-aloud.md) or annotated steps).
2. Assign a completion problem on an isomorphic task with the goal-critical steps blanked; provide the completed example alongside for reference ([Worked Examples](../principles/worked-examples.md)).
3. Fade: progressively blank more steps across successive tasks ([Fading](../elements/fading.md)), monitoring accuracy ([Check-In](../elements/check-in.md)).
4. Transition to full problem solving once completion accuracy is high, with feedback on each attempt ([Practice](../elements/practice.md), [Assessment](../elements/assessment.md)).

## Related Strategies
- [Worked examples first](worked_examples_first.md) — the preceding phase; completion problems assume example study has occurred
- [Faded guidance](faded-guidance.md) — the general principle this strategy instantiates in problem sequences
- [Example-problem pairs](../elements/example-problem-pairs.md) — an alternating variant with similar rationale

## Examples
- **van Merriënboer's 4C/ID task sequences** — complex-skill curricula (e.g., technical training) begin each task class with completion tasks and fade to conventional tasks ([Four-Component Instructional Design](../patterns/4cid-four-component-instructional-design.md))
- **[Khan Academy](https://www.khanacademy.org)** — hint sequences effectively function as on-demand completion problems, revealing solution steps one at a time
- **Renkl & Atkinson's fading studies** — algebra tutoring sequences that faded worked examples into completion problems and then full problems, improving near transfer

## Key Sources
- van Merriënboer, J. J. G. (1990). Strategies for programming instruction in high school: Program completion vs. program generation. *Journal of Educational Computing Research, 6*(3), 265–285. [doi:10.2190/NW2X-L8GK-M8PP-1L7N](https://doi.org/10.2190/NW2X-L8GK-M8PP-1L7N)
- Renkl, A., Atkinson, R. K., & Große, C. S. (2004). How fading worked solution steps works — a cognitive load perspective. *Instructional Science, 32*(1–2), 59–82. [doi:10.1023/b:truc.0000021815.74806.f6](https://doi.org/10.1023/b:truc.0000021815.74806.f6)
- van Merriënboer, J. J. G., & Kirschner, P. A. (2018). *Ten steps to complex learning* (3rd ed.). Routledge.
- Sweller, J., van Merriënboer, J. J. G., & Paas, F. (2019). Cognitive architecture and instructional design: 20 years later. *Educational Psychology Review, 31*(2), 261–292. [doi:10.1007/s10648-019-09465-5](https://doi.org/10.1007/s10648-019-09465-5)
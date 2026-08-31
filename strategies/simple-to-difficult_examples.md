---
type: strategy
title: Simple-to-Difficult Examples
description: Start with simple examples when introducing a concept, then progress to more complex ones later.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Simple-to-Difficult Examples

> **Strategy** · [All strategies](index.md)

## Description
Simple-to-difficult sequencing presents learners with easy, prototypical instances of a concept or task first, then progressively introduces more complex, ambiguous, or atypical instances. If learners only ever see simple instances, they under-generalize — forming a concept representation too narrow to classify the harder cases they will eventually meet. Sequencing manages this by letting the concept schema form on clear cases before it must accommodate noisy ones.

## Design Implications

Sequencing examples from simple to complex manages intrinsic load during schema formation: learners build an initial representation from prototypical cases without the added burden of irrelevant complexity [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) [+S]. The sequence must actually reach the difficult cases — stopping at simple examples produces under-generalization, and the difficulty ramp should be faded as expertise grows, since overly guided sequencing becomes redundant for advanced learners [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M].

### Context
#### Requirements
- An analysis of the concept's dimensions of variability — which features make an instance simple (prototypical, few irrelevant features) versus difficult (atypical, ambiguous, many irrelevant features)
- A deliberate sequence that ends with the difficult cases, not just begins with the easy ones
- [Demonstration](../elements/demonstration.md) or worked examples for early cases, with [Fading](../elements/fading.md) of support as instances grow harder
- Classification or application tasks that require learners to handle both simple and complex instances

#### Constraints
- Sequencing that never reaches difficult instances causes under-generalization — learners classify only prototypical cases correctly [-S]
- For learners with substantial prior knowledge, a strict simple-to-difficult ramp wastes time and can impair learning (expertise reversal) [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [-M]
- Overly long ramps can bore learners or create an illusion of mastery from easy wins; early difficulty spikes cause overload [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) [-S]
- Requires significant front-end analysis to define complexity levels; poorly calibrated sequences undermine the whole design

#### Implementation Variability
- **Whole-task with simplified versions**: present the full task class early but in simplified form (as in [4C/ID](../patterns/4cid-four-component-instructional-design.md)), rather than withholding complexity entirely
- **Learner-controlled sequencing**: let learners choose when to move to harder examples, supported by [Adaptive Difficulty](../elements/adaptive-difficulty.md)
- **Interleaved difficulty**: once the ramp is complete, mix simple and difficult cases so learners practice discrimination, not just progression

### Target Learners
- Novices encountering a new concept, who need prototypical cases to form an initial schema [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+M]
- Learners in complex domains where instances vary widely in typicality (medical diagnosis, fault diagnosis, classification tasks)
- Less appropriate for advanced learners, who benefit from starting with complex or varied cases [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M]

### Target Learning Goals
- Concept acquisition and classification: correctly identifying instances across the full range of typicality
- Schema formation: building generalizable mental models rather than narrow prototypes
- Discrimination learning: distinguishing relevant from irrelevant features as noise increases

### Instructions
1. Analyze the concept to identify what makes an instance simple (prototypical, low feature variability) versus difficult (atypical, ambiguous, high variability)
2. Select or author 2–3 simple exemplars and present them with explicit [Demonstration](../elements/demonstration.md) or worked-example support
3. Progress through intermediate cases, gradually removing support ([Fading](../elements/fading.md)) and adding irrelevant features
4. Finish with difficult, atypical, or ambiguous cases; use [Non-Examples](../elements/non-examples.md) and [Comparing Cases](../elements/comparing-cases.md) to sharpen boundaries
5. Assess classification of both simple and complex instances; recycle difficult cases via [Practice](../elements/practice.md) until learners classify them reliably

## Related Strategies
- [Use Worked Examples](use_worked_examples.md) — the example format most commonly sequenced from simple to difficult
- [Think-Aloud Modeling](think-aloud-modeling.md) — narration that makes the reasoning on each example visible

## Related Elements
- [Demonstration](../elements/demonstration.md) — how early simple examples are typically presented
- [Fading](../elements/fading.md) — support decreases as example difficulty increases
- [Non-Examples](../elements/non-examples.md) — contrast cases that prevent over-generalization at each difficulty level
- [Comparing Cases](../elements/comparing-cases.md) — side-by-side simple/difficult pairs make the critical features salient

## Patterns That Use This Strategy
- [4C/ID](../patterns/4cid-four-component-instructional-design.md) — learning tasks are sequenced from simple whole tasks toward complex ones with decreasing support
- [Elaboration Theory](../patterns/elaboration-theory.md) — epitome-first, progressively-elaborated sequencing of content complexity
- [Concept Attainment](../patterns/concept-attainment.md) — exemplar sequences drive hypothesis formation about concept boundaries

## Examples
- **Radiology training**: trainees learn to identify bone fractures starting with obvious cases where fragments are fully separated, progressing to hairline fractures with partially joined fragments — the canonical under-generalization risk if training stops at easy films.
- **Khan Academy** (https://www.khanacademy.org) — practice sets order problems from basic to multi-step, with mastery-based gating that holds learners at a level until they succeed.
- **Duolingo** (https://www.duolingo.com) — introduces grammar with simple, high-frequency sentences before irregular and ambiguous constructions.

## Key Sources
- Elio, R., & Anderson, J. R. (1981). The effects of information order and learning mode on schema abstraction. *Memory & Cognition, 9*(6), 569–579. [doi:10.3758/bf03196994](https://doi.org/10.3758/bf03196994)
- Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J. (2003). The expertise reversal effect. *Educational Psychologist, 38*(1), 23–31. [doi:10.1207/S15326985EP3801_4](https://doi.org/10.1207/S15326985EP3801_4)
- Renkl, A. (2014). Toward an instructionally oriented theory of example-based learning. *Cognitive Science, 38*(1), 1–37. [doi:10.1111/cogs.12086](https://doi.org/10.1111/cogs.12086)
- Sweller, J., & Cooper, G. A. (1985). The use of worked examples as a substitute for problem solving in learning algebra. *Cognition and Instruction, 2*(1), 59–89. [doi:10.1207/s1532690xci0201_3](https://doi.org/10.1207/s1532690xci0201_3)
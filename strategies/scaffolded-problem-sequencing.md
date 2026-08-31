---
type: strategy
title: Scaffolded Problem Sequencing
description: Ordering practice problems from simple to complex with graduated support, so each task is slightly beyond current competence but within reach with available scaffolds.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Scaffolded Problem Sequencing

> **Strategy** · [All strategies](index.md)

## Description
Scaffolded problem sequencing arranges a set of practice tasks along a deliberate difficulty gradient, pairing each step of increasing complexity with an appropriate level of support — from worked examples, to completion problems, to independent problem solving. The sequence is designed so that learners are neither overwhelmed by premature complexity nor bored by redundant practice, with supports [faded](../elements/fading.md) as competence grows.

## Design Implications

Sequencing works because it keeps each task within working memory limits while still requiring new learning; uncontrolled difficulty spikes are a primary cause of [cognitive overload degrading learning](../claims/cognitive-overload-degrades-learning.md) [+S]. The optimal sequence depends on learner expertise: too much support for advanced learners wastes time and can even depress performance, an instance of the expertise-reversal pattern [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M]. Sequences should therefore be treated as adjustable, not fixed.

### Context
#### Requirements
- A task class broken into features that drive difficulty (number of steps, unfamiliarity, number of interacting concepts)
- A bank of problems ordered on those features, with support levels attached ([worked examples](../elements/worked-examples.md), completion problems, hints, bare problems)
- A fading rule: criteria for when to withdraw support (e.g., accuracy thresholds, or a fixed example-to-problem ratio)
- Diagnostic checks between stages to confirm readiness to advance ([Assessment](../elements/assessment.md))

#### Constraints
- Sequences calibrated for novices misfire for learners with prior knowledge, who perform worse with high support than with independent practice [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [-M]
- Overly gradual sequences can promote passive pattern-matching on worked examples rather than genuine problem solving [Pairing worked examples with practice or fading supports transfer better than examples alone.](../claims/worked-examples-with-practice-improve-transfer.md) [-S] — learners may imitate surface procedures without forming schemas
- Fixed linear sequences ignore between-learner variance; without diagnosis or [adaptive difficulty](../elements/adaptive-difficulty.md), a large fraction of the class is mis-placed at any given step [~M]
- Sequencing by surface difficulty (problem "size") rather than by conceptual feature can leave core misconceptions untouched until late in the sequence

#### Implementation Variability
- **Completion problems**: each task omits part of the solution, so support fades within the task itself rather than across tasks
- **Alternation**: worked example → isomorphic problem pairs, rather than blocks of examples then blocks of problems [Pairing worked examples with practice or fading supports transfer better than examples alone.](../claims/worked-examples-with-practice-improve-transfer.md) [+S]
- **Backwards fading**: begin with full examples and remove the last step first, then earlier steps
- **Learner-controlled**: learners choose when to see a worked example (e.g., on-demand hints in Khan Academy), trading calibration demands for autonomy
- **Multiple-case sequences**: varying surface features across isomorphic problems to support abstraction [Comparing contrasting cases improves learning.](../claims/comparing-contrasting-cases-improves-learning.md) [+M]

### Target Learners
- Novices in a structured domain (mathematics, programming, physics, chemistry), who lack schemas for managing problem complexity [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+M]
- Learners with low prior knowledge, for whom unsequenced problem sets produce unproductive search and frustration
- Less beneficial for advanced learners, who profit more from problem solving with minimal support [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M]

### Target Learning Goals
- Procedural fluency: building reliable execution of multi-step methods
- Schema construction: learning which problem features call for which solution approaches
- Transfer to variant problems: sequences that vary surface features while preserving deep structure [Comparing contrasting cases improves learning.](../claims/comparing-contrasting-cases-improves-learning.md) [+M]

### Instructions
1. Decompose the target skill into difficulty-driving features and order them from fewest to most interacting elements ([Chunking](../principles/chunking.md))
2. Open the sequence with fully worked examples with reasoning made visible ([Think-Aloud](../elements/think-aloud.md))
3. Move to completion problems in which learners supply progressively larger portions of the solution ([Fading](../elements/fading.md))
4. Alternate examples with isomorphic practice problems rather than batching them ([Practice](../elements/practice.md))
5. Diagnose readiness before advancing; allow fast learners to skip ahead and struggling learners to repeat with fresh isomorphic problems ([Adaptive Difficulty](../elements/adaptive-difficulty.md))
6. Close the sequence with problems that vary surface features so learners must select, not just execute, a method

## Related Strategies
- [Use Worked Examples](use_worked_examples.md) — the support mechanism most commonly faded across a sequence
- [Interleaving](interleaving.md) — contrasts with blocked sequencing; once basic fluency is established, mixing problem types improves discrimination
- [Completion Problems](completion-problems.md) — the within-task form of fading

## Examples
- **[4C/ID](../patterns/4cid-four-component-instructional-design.md)** — van Merriënboer's model organizes whole learning tasks into task classes of increasing complexity, with decreasing learner support within each class; the canonical implementation of scaffolded sequencing.
- **[Khan Academy](https://www.khanacademy.org)** — exercise sets ordered by difficulty within a skill, with on-demand hints that function as partial worked examples.
- **[Codecademy](https://www.codecademy.com)** — sequences from guided, scaffolded code completion toward free-form projects.
- **Cognitive Tutor (Carnegie Learning)** — adaptive algebra sequences that adjust problem selection and hint availability based on real-time skill estimates ([Cognitive Apprenticeship](../patterns/cognitive-apprenticeship.md) lineage).

## Key Sources
- Sweller, J., & Cooper, G. A. (1985). The use of worked examples as a substitute for problem solving in learning algebra. *Cognition and Instruction, 2*(1), 59–89. [doi:10.1207/s1532690xci0201_3](https://doi.org/10.1207/s1532690xci0201_3)
- Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J. (2003). The expertise reversal effect. *Educational Psychologist, 38*(1), 23–31. [doi:10.1207/S15326985EP3801_4](https://doi.org/10.1207/S15326985EP3801_4)
- Renkl, A., & Atkinson, R. K. (2003). Structuring the transition from example study to problem solving in cognitive skill acquisition: A cognitive load perspective. *Educational Psychologist, 38*(1), 15–22. [doi:10.1207/S15326985EP3801_3](https://doi.org/10.1207/S15326985EP3801_3)
- van Merriënboer, J. J. G. (1997). *Training complex cognitive skills: A four-component instructional design model for technical training.* Educational Technology Publications.
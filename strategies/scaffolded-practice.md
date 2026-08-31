---
type: strategy
title: Scaffolded Practice
description: Practice arranged as a graded sequence of tasks with temporary supports that are progressively removed as learner competence grows.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Scaffolded Practice

> **Strategy** · [All strategies](index.md)

## Description
Scaffolded practice structures repeated application of a skill so that support is high at first and fades as learners gain competence. Rather than moving from full instruction directly to independent problems, the designer builds a gradient — worked examples, then completion problems, then faded or simplified tasks, then independent practice with feedback. The supports (prompts, hints, partially completed solutions, reduced task complexity) are temporary and deliberately withdrawn.

## Design Implications

Scaffolded practice operationalizes the expertise-reversal logic: guidance that helps novices hinders experts, so support must track current competence rather than stay fixed [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M]. The evidence base is strongest for example-based gradients: pairing worked examples with practice and fading them over time produces better transfer than either examples alone or unsupported problem solving from the start [Pairing worked examples with practice or fading supports transfer better than examples alone.](../claims/worked-examples-with-practice-improve-transfer.md) [+S]. Task sequencing also manages working memory load — early tasks should be simplified or chunked so intrinsic load stays within capacity [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+M]; unmanaged complexity degrades learning [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) [+S].

### Context
#### Requirements
- A task analysis identifying which sub-skills need support and in what order
- A graded task sequence: full models → [Worked Examples](../principles/worked-examples.md) → completion problems → independent problems
- A fading plan specifying when and how supports are withdrawn ([Fading](../elements/fading.md))
- Feedback at each stage so errors are corrected before they consolidate ([Practice](../elements/practice.md), [Assessment](../elements/assessment.md))

#### Constraints
- Fading too early leaves learners in unguided search, which is inefficient for novices [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [-M]
- Fading too late or never produces over-reliance; learners who always see the model struggle on independent tasks [Pairing worked examples with practice or fading supports transfer better than examples alone.](../claims/worked-examples-with-practice-improve-transfer.md) [-S]
- A fixed scaffold for all learners misfires in both directions — too much for some, too little for others; adaptive sequencing mitigates this [Adaptive learning improves outcomes.](../claims/adaptive-learning-improves-outcomes.md) [~M]
- Scaffolds that reduce task complexity but also reduce the *quality* of engagement (e.g., multiple-choice substitutes for constructed responses) can undercut the practice effect

#### Implementation Variability
- **Static gradient**: all learners move through the same example→completion→independent sequence
- **Adaptive gradient**: support level adjusts to performance data ([Adaptive Difficulty](../elements/adaptive-difficulty.md))
- **On-demand scaffolds**: hints and sub-demonstrations available when learners request them rather than imposed
- **Within-task fading**: a single task starts with prompts embedded and removes them across successive items

### Target Learners
- Novices, who benefit most from high initial support and suffer most from unguided practice [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+M]
- Learners with low prior knowledge or high working memory demands in the domain [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) [+M]
- Advanced learners, for whom heavy scaffolding becomes redundant and can *reduce* performance [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M] — support should be minimal or absent

### Target Learning Goals
- Procedural fluency: building accurate, automatic execution of multi-step skills
- Schema construction: forming organized mental models of problem types
- Transfer: applying learned procedures to novel variants [Pairing worked examples with practice or fading supports transfer better than examples alone.](../claims/worked-examples-with-practice-improve-transfer.md) [+S]

### Instructions
1. Analyze the skill into sub-skills and order tasks from simple to complex ([Cognitive Load Management](../principles/cognitive-load-management.md))
2. Begin with full models and worked examples with reasoning made explicit ([Think-Aloud](../elements/think-aloud.md))
3. Insert completion problems — partially worked solutions learners finish — as the first practice step
4. Fade supports across successive tasks ([Fading](../elements/fading.md)), moving to independent problems
5. Provide feedback at every stage and adjust the gradient to observed performance ([Adaptive Difficulty](../elements/adaptive-difficulty.md))
6. End with independent practice under realistic conditions to consolidate ([Practice](../elements/practice.md))

## Related Strategies
- [Use Worked Examples](use_worked_examples.md) — the high-support end of the scaffolded gradient
- [Think-Aloud Modeling](think-aloud-modeling.md) — how the initial models make expert reasoning visible
- [Fading](../elements/fading.md) — the mechanism by which support is withdrawn

## Examples
- **[Khan Academy](https://www.khanacademy.org)** — each exercise set moves from video demonstration to problems with tiered hints; hints function as on-demand scaffolds that fade as learners succeed.
- **Cognitive Tutor (Carnegie Learning)** — adaptive algebra practice that provides step-level hints and reduces them as student mastery estimates rise, a direct implementation of adaptive scaffolded practice.
- **[Codecademy](https://www.codecademy.com)** — lessons sequence annotated examples, fill-in-the-blank completion exercises, then free-form projects, enacting the example→completion→independent gradient.
- **Reciprocal teaching (Palincsar & Brown)** — reading comprehension practice where teacher modeling of predicting, questioning, clarifying, and summarizing fades to student-led group practice.

## Key Sources
- Sweller, J., & Cooper, G. A. (1985). The use of worked examples as a substitute for problem solving in learning algebra. *Cognition and Instruction, 2*(1), 59–89. [doi:10.1207/s1532690xci0201_3](https://doi.org/10.1207/s1532690xci0201_3)
- Renkl, A., & Atkinson, R. K. (2003). Structuring the transition from example study to problem solving in cognitive skill acquisition: A cognitive load perspective. *Educational Psychologist, 38*(1), 15–22. [doi:10.1207/S15326985EP3801_3](https://doi.org/10.1207/S15326985EP3801_3)
- Palincsar, A. S., & Brown, A. L. (1984). Reciprocal teaching of comprehension-fostering and comprehension-monitoring activities. *Cognition and Instruction, 1*(2), 117–175. [doi:10.1207/s1532690xci0102_1](https://doi.org/10.1207/s1532690xci0102_1)
- Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J. (2003). The expertise reversal effect. *Educational Psychologist, 38*(1), 23–31. [doi:10.1207/S15326985EP3801_4](https://doi.org/10.1207/S15326985EP3801_4)
- van Gog, T., & Rummel, N. (2010). Example-based learning: Integrating cognitive and social-cognitive research perspectives. *Educational Psychology Review, 22*(2), 155–174. [doi:10.1007/s10648-010-9134-7](https://doi.org/10.1007/s10648-010-9134-7)
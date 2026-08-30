---
type: element
title: Provide guidance
description: Offers scaffolding, modeling, or examples to support learning.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Provide guidance

## Description
Providing guidance means supplying learners with scaffolding, models, worked examples, or coaching support while they acquire new knowledge or skills. The instructor or system structures the task enough to prevent unproductive search and error, then progressively withdraws support as competence develops.

## Design Implications

Guidance reduces the working-memory burden of early learning by narrowing the space of possible actions and giving learners a reference model to study [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+M]. Its effectiveness depends on matching the amount of support to learner expertise: too little guidance leaves novices floundering, while too much produces redundancy for more knowledgeable learners [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M]. Guidance should be adaptive and faded over time, shifting responsibility to the learner as performance improves [Fading support promotes transfer of responsibility.](../claims/fading-support-promotes-transfer-of-responsibility.md) [+M].

### Context
#### Requirements
- A task analysis identifying where learners are likely to struggle, so support targets actual difficulty points
- Support that is contingent on learner performance, adjusted in response to evidence of understanding [Contingent scaffolding improves learning.](../claims/contingent-scaffolding-improves-learning.md) [+M]
- A plan for fading: moving from full models to partial examples to independent performance ([Fading](fading.md))
- Opportunities for learners to apply guidance actively rather than passively receive it ([Practice](practice.md))

#### Constraints
- Unguided or minimally guided discovery is less effective for novices than explicit guidance, particularly for complex content [~S] — inquiry works best *after* foundational guidance, not instead of it
- Over-guidance for learners with prior knowledge wastes capacity and can depress performance [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M]
- Static, one-size-fits-all guidance ignores the expertise-reversal effect; support calibrated for the middle of a group helps no one at the extremes
- Guidance that does the cognitive work for the learner (e.g., fully completed solutions with no [Self-Explanation](self-explanation.md) prompts) yields shallow encoding [Pairing worked examples with practice or fading supports transfer better than examples alone.](../claims/worked-examples-with-practice-improve-transfer.md) [-S]

### Target Learners
- Novices acquiring complex concepts or procedural knowledge, who lack schemas to organize unguided search [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+M]
- Learners in the middle of an expertise trajectory, for whom faded and contingent support accelerates growth [Contingent scaffolding improves learning.](../claims/contingent-scaffolding-improves-learning.md) [+M]
- Less beneficial for experts, who perform better with problem-solving opportunities than with redundant guidance [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M]

### Target Learning Goals
- Procedural knowledge: learning how to execute multi-step tasks correctly
- Conceptual understanding: using examples and explanations to build accurate mental models [Self-explanation improves conceptual understanding.](../claims/self-explanation-improves-conceptual-understanding.md) [+M]
- Transfer: faded guidance that hands responsibility to learners supports application beyond the original context [Fading support promotes transfer of responsibility.](../claims/fading-support-promotes-transfer-of-responsibility.md) [+M]

### Affordances
- [Scaffolding](../principles/scaffolding.md) — providing guidance *is* the enactment of scaffolding: temporary, contingent support that is withdrawn as competence grows
- [Cognitive Load Management](../principles/cognitive-load-management.md) — worked examples and models externalize intermediate steps so novices attend to task structure rather than means-ends search [Example-problem sequences reduce cognitive load.](../claims/example-problem-sequences-reduce-cognitive-load.md) [+M]
- [Metacognition](../principles/metacognition.md) — guidance can model self-monitoring (via [Think-Aloud](think-aloud.md)) and prompt learners to explain and evaluate their own reasoning
- [Inquiry-Based Learning](../principles/inquiry-based-learning.md) — guidance makes inquiry productive: prompts, hints, and [Coaching](coaching.md) keep exploration oriented without eliminating the learner's own reasoning work

## Related Elements
- [Worked Examples](worked-examples.md) — the most heavily researched form of guidance; complete solution models for study
- [Guided Discovery](guided-discovery.md) — inquiry with built-in prompts and hints, balancing exploration and support
- [Immediate Feedback](immediate-feedback.md) — corrective guidance delivered at the moment of error, before misconceptions consolidate
- [Demonstration](demonstration.md) — modeling expert performance as a form of guidance
- [Fading](fading.md) — the mechanism for withdrawing guidance as expertise develops
- [Coaching](coaching.md) — interactive, performance-contingent guidance during practice

## Patterns That Use This Element
- [Gagné's 9 Events](../patterns/gagnés-9-events-of-instruction.md) — "provide learning guidance" is the fifth event
- [4C/ID](../patterns/4cid-four-component-instructional-design.md) — supportive information and procedural information are the guidance components surrounding learning tasks
- [Cognitive Apprenticeship](../patterns/cognitive-apprenticeship.md) — modeling and coaching phases deliver guidance before fading
- [Direct Instruction](../patterns/direct-instruction.md) — high-guidance enactment with scripted models and prompted practice

## Examples

**[Use Worked Examples](../strategies/use_worked_examples.md)** — Presents a fully solved problem with step-by-step reasoning, then alternates with problems for the learner to solve; the canonical example-problem pairing.

**[Think-Aloud Modeling](../strategies/think-aloud-modeling.md)** — Instructor verbalizes reasoning and self-monitoring while performing a task, making expert decision-making available for imitation.

**[Khan Academy](https://www.khanacademy.org)** — Narrated video demonstrations paired with practice exercises and a graduated hint system that delivers progressively more explicit guidance on demand.

**[Cognitive Tutor](https://www.carnegielearning.com)** (Carnegie Learning) — Adaptive tutoring software that provides just-in-time hints and feedback calibrated to each learner's current step in a problem, enacting contingent guidance at scale.

## Key Sources
- Sweller, J., & Cooper, G. A. (1985). The use of worked examples as a substitute for problem solving in learning algebra. *Cognition and Instruction, 2*(1), 59–89. [doi:10.1207/s1532690xci0201_3](https://doi.org/10.1207/s1532690xci0201_3)
- Kirschner, P. A., Sweller, J., & Clark, R. E. (2006). Why minimal guidance during instruction does not work: An analysis of the failure of constructivist, discovery, problem-based, experiential, and inquiry-based teaching. *Educational Psychologist, 41*(2), 75–86. [doi:10.1207/s15326985ep4102_1](https://doi.org/10.1207/s15326985ep4102_1)
- van Merriënboer, J. J. G., & Kirschner, P. A. (2018). *Ten steps to complex learning* (3rd ed.). Routledge.
- Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J. (2003). The expertise reversal effect. *Educational Psychologist, 38*(1), 23–31. [doi:10.1207/S15326985EP3801_4](https://doi.org/10.1207/S15326985EP3801_4)
- van Gog, T., & Rummel, N. (2010). Example-based learning: Integrating cognitive and social-cognitive research perspectives. *Educational Psychology Review, 22*(2), 155–174. [doi:10.1007/s10648-010-9134-7](https://doi.org/10.1007/s10648-010-9134-7)
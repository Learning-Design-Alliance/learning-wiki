---
type: strategy
title: Modeling
description: The instructor or a peer demonstrates a skill, process, or way of thinking so learners can observe expert performance before attempting it themselves.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Modeling

## Description
Modeling is the act of demonstrating a skill, strategy, or reasoning process while learners observe, so that expert performance becomes visible and imitable before learners attempt the task themselves. Effective modeling goes beyond showing the final product: the modeler narrates decisions, monitors their own understanding, and makes tacit expert knowledge explicit. It is the foundational move in [Cognitive Apprenticeship](../theories/cognitive-apprenticeship.md) and derives its theoretical grounding from [Social Learning Theory](../theories/social-learning-theory.md), in which observational learning is a primary mechanism of skill acquisition.

## Design Implications

Modeling reduces the unguided search that overwhelms novices by supplying a reference model they can study and imitate, easing working-memory demands during initial acquisition [Cognitive overload degrades learning when learners must construct procedures without support.](../claims/cognitive-overload-degrades-learning.md) [+M]. Its value depends on making thinking visible: models who verbalize their reasoning and self-monitoring produce stronger learning than silent demonstrations, and models similar to the learners (e.g., a fellow student) can be at least as effective as expert models [~M]. Modeling must be followed by guided practice, since observation alone yields shallow encoding and illusions of competence [-S].

### Context
#### Requirements
- A clear, accurate model of the target performance, ideally including imperfect or in-progress work so learners see how experts recover from errors
- Narration that makes reasoning explicit — [Articulation](../elements/articulation.md) of decisions, not just actions
- A planned transition to learner activity ([Coaching](../elements/coaching.md), [Practice](../elements/practice.md)) so observation converts into performance
- Attention to model-learner similarity when peer models are used

#### Constraints
- Observation without subsequent practice creates illusions of understanding; learners systematically overestimate what they learned from watching [-S]
- Expert models can be less effective than near-peer models for novices, because expert performance is too fluent to parse [~M]
- As expertise grows, continued modeling becomes redundant and can interfere with learning (the expertise-reversal pattern documented in [Expertise Reversal Effect](../theories/expertise-reversal-effect.md)) [~M]
- Modeling a single canonical solution can anchor learners and reduce flexibility on open-ended tasks; contrasting multiple models mitigates this [~W]

#### Implementation Variability
- **Expert modeling** — instructor demonstrates full expertise; best for establishing a target standard
- **Near-peer modeling** — a comparable student works through the task; errors and repair are visible, which supports self-efficacy
- **Contrast modeling** — two models (strong/weak, or two valid approaches) are compared, sharpening discrimination between good and poor strategy use
- **Silent vs. narrated** — narrated modeling with [Think-Aloud](../elements/think-aloud.md) commentary is generally superior for strategy learning [~M]

### Target Learners
- Novices encountering a skill or strategy for the first time, who lack the schemas to guide unaided performance [Cognitive overload degrades learning when learners must construct procedures without support.](../claims/cognitive-overload-degrades-learning.md) [+M]
- Struggling learners who benefit from seeing the process, including false starts and self-correction, rather than only polished outcomes
- Less beneficial for learners with strong prior knowledge, who learn more from solving problems themselves than from observing [~M]

### Target Learning Goals
- Procedural skill acquisition: seeing the steps of a process executed
- Strategic and metacognitive learning: what expert monitoring, revision, and decision-making look like
- Self-efficacy: observing a similar peer succeed ("coping model") builds belief that the task is attainable

### Instructions
1. Identify the target skill and the expert decisions within it that are normally invisible.
2. Demonstrate the task while verbalizing reasoning — use [Think-Aloud](../elements/think-aloud.md) to expose monitoring and self-correction, and [Articulation](../elements/articulation.md) to name why each move is made.
3. Where useful, show a second model or a flawed attempt and compare ([Case Studies](../elements/case-studies.md) work well for contrast).
4. Transition immediately to guided practice with [Coaching](../elements/coaching.md), fading support as competence grows.
5. Have learners articulate their own reasoning back ([Articulation](../elements/articulation.md)) to confirm the modeled strategies transferred.

## Related Strategies
- [Activating Prior Knowledge](activating-prior-knowledge.md) — prepares learners to extract the right features from a model before they observe it
- [Action-Oriented Feedback](action-oriented-feedback.md) — the natural follow-on to modeling; feedback references the modeled criteria

## Examples
- **[Cognitive Apprenticeship](../patterns/cognitive-apprenticeship.md)** — modeling is the first phase of the modeling–coaching–fading sequence described by Collins, Brown, and Newman.
- **Writing instruction with model texts** — Braaksma et al. had students observe peers composing and evaluating texts; observational learning improved writing performance relative to direct practice alone.
- **[Khan Academy](https://www.khanacademy.org)** — narrated, step-by-step video modeling of problem solving, followed by practice exercises with on-demand hints that function as partial re-models.
- **Reading strategy instruction (e.g., reciprocal teaching)** — the teacher models predicting, questioning, clarifying, and summarizing before students take turns leading.

## Key Sources
- Bandura, A. (1977). *Social learning theory*. Prentice Hall.
- Collins, A., Brown, J. S., & Newman, S. E. (1989). Cognitive apprenticeship: Teaching the crafts of reading, writing, and mathematics. In L. B. Resnick (Ed.), *Knowing, learning, and instruction: Essays in honor of Robert Glaser* (pp. 453–494). Lawrence Erlbaum. [doi:10.4324/9781315044408-14](https://doi.org/10.4324/9781315044408-14)
- Braaksma, M. A. H., Rijlaarsdam, G., & van den Bergh, H. (2002). Observational learning and the effects of model-observer similarity. *Journal of Educational Psychology, 94*(3), 405–415. [doi:10.1037/0022-0663.94.2.405](https://doi.org/10.1037/0022-0663.94.2.405)
- van Gog, T., & Rummel, N. (2010). Example-based learning: Integrating cognitive and social-cognitive research perspectives. *Educational Psychology Review, 22*(2), 155–174. [doi:10.1007/s10648-010-9134-7](https://doi.org/10.1007/s10648-010-9134-7)
- Sweller, J., & Cooper, G. A. (1985). The use of worked examples as a substitute for problem solving in learning algebra. *Cognition and Instruction, 2*(1), 59–89. [doi:10.1207/s1532690xci0201_3](https://doi.org/10.1207/s1532690xci0201_3)
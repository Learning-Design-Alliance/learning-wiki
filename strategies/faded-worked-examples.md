---
type: strategy
id: faded-worked-examples
title: Faded Worked Examples
description: A sequence that begins with fully worked examples and progressively removes solution steps, transferring responsibility from the model to the learner.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Faded Worked Examples

> **Strategy** · [All strategies](index.md)

## Description
Faded worked examples present a series of problems in which the expert's solution is initially complete, then progressively incomplete — first the final steps are omitted (backward fading), later earlier steps (forward fading), until the learner solves entire problems independently. The technique operationalizes [Scaffolding](../principles/scaffolding.md) within example-based learning: support is withdrawn in step-sized increments matched to growing competence.

## Design Implications

Fading combines the working-memory benefits of [Worked Examples](../principles/worked-examples.md) for novices with the practice benefits of problem solving, avoiding the pitfalls of either alone [Pairing worked examples with practice or fading supports transfer better than examples alone.](../claims/worked-examples-with-practice-improve-transfer.md) [+S]. Completion problems — where learners fill in the missing steps — force active processing of the faded portion rather than passive reading [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+M]. Fading should be calibrated to expertise: fading too slowly wastes time for fast learners, too quickly reintroduces unguided search [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M].

### Context
#### Requirements
- A problem domain with structured, step-based solutions (algebra, physics, programming, argument construction)
- A sequence of isomorphic or near-isomorphic problems so faded steps build on the same schema
- Completion prompts at each faded step, ideally with self-explanation prompts asking *why* the step works
- A diagnostic or adaptive mechanism (or instructor judgment) for deciding when to fade further

#### Constraints
- Ineffective when learners lack the knowledge to complete faded steps — premature fading produces guessing and error encoding [-S]
- Poor fit for ill-structured domains with no canonical solution steps; use [Case Studies](../elements/case-studies.md) or [Comparing Cases](../elements/comparing-cases.md) instead
- Static fading schedules ignore individual differences; fixed sequences can bore advanced learners and overwhelm novices [~M] — adaptive fading mitigates this
- Learners who skip the example and jump to the problem lose the benefit; design must make studying the worked portion necessary

#### Implementation Variability
- **Backward fading** (omit final steps first) is generally easier and slightly more effective than forward fading, especially for low-knowledge learners [+W]
- **Adaptive fading** — fading triggered by learner performance on completion steps rather than a fixed schedule (Renkl & Atkinson's approach)
- **Alternating example–problem pairs** — each worked example immediately followed by an isomorphic problem, a simpler variant of fading
- **Self-explanation prompts** appended to worked steps to deepen processing without changing the fade schedule

### Target Learners
- Novices in a structured domain, who benefit from full guidance before independent problem solving [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+M]
- Low-prior-knowledge learners, for whom premature problem solving imposes extraneous load [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) [+M]
- Less beneficial for advanced learners, who learn more from problem solving than from studying examples [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M] — the [expertise reversal effect](../theories/expertise-reversal-effect.md) applies to the fade schedule itself

### Target Learning Goals
- Procedural fluency in well-structured domains (mathematics, science, programming)
- Schema acquisition: recognizing which solution method applies to which problem
- Transfer to near problems with changed surface features [Pairing worked examples with practice or fading supports transfer better than examples alone.](../claims/worked-examples-with-practice-improve-transfer.md) [+S]

### Instructions
1. Select a problem sequence of increasing complexity within one solution schema.
2. Present the first problem as a fully worked example with reasoning annotations ([Think-Aloud](../elements/think-aloud.md) or written rationale).
3. Present the second problem with the final one or two steps omitted; learners complete them ([Practice](../elements/practice.md)).
4. Fade earlier steps across subsequent problems until learners solve full problems unaided.
5. Add self-explanation prompts ("Why is this step valid?") at worked steps to prevent passive copying.
6. Monitor completion accuracy; slow the fade if error rates spike, accelerate it for learners solving completions quickly ([Adaptive Difficulty](../elements/adaptive-difficulty.md)).

## Related Strategies
- [Use Worked Examples](use_worked_examples.md) — the non-faded parent strategy; fading is its dynamic extension
- [Self-Explanation Prompting](self-explanation-prompting.md) — the standard companion, converting example study into generative processing
- [Interleaving](interleaving.md) — faded sequences can be interleaved across problem types to build discrimination

## Examples
- **Atkinson, Renkl & Merrill's adaptive algebra tutor** — computer-based faded worked examples in probability and algebra where fading was contingent on completion-step performance (see Renkl & Atkinson, 2003, below).
- **[Khan Academy](https://www.khanacademy.org)** — hint systems function as on-demand fading: each successive hint reveals one more solution step, letting learners complete the remainder themselves.
- **[Codecademy](https://www.codecademy.com)** — early lessons provide full code to run, then partially completed code with TODO markers, then blank scaffolds — a fade from example to independent coding.

## Key Sources
- Renkl, A., & Atkinson, R. K. (2003). Structuring the transition from example study to problem solving in cognitive skill acquisition: A cognitive load perspective. *Educational Psychologist, 38*(1), 15–22. [doi:10.1207/S15326985EP3801_3](https://doi.org/10.1207/S15326985EP3801_3)
- Renkl, A., Atkinson, R. K., & Große, C. S. (2004). How fading worked solution steps works — a cognitive load perspective. *Instructional Science, 32*(1–2), 59–82. [doi:10.1023/b:truc.0000021815.74806.f6](https://doi.org/10.1023/b:truc.0000021815.74806.f6)
- Sweller, J., & Cooper, G. A. (1985). The use of worked examples as a substitute for problem solving in learning algebra. *Cognition and Instruction, 2*(1), 59–89. [doi:10.1207/s1532690xci0201_3](https://doi.org/10.1207/s1532690xci0201_3)
- van Gog, T., & Rummel, N. (2010). Example-based learning: Integrating cognitive and social-cognitive research perspectives. *Educational Psychology Review, 22*(2), 155–174. [doi:10.1007/s10648-010-9134-7](https://doi.org/10.1007/s10648-010-9134-7)
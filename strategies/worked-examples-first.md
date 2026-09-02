---
type: strategy
id: worked-examples-first
title: Worked Examples First
description: Presenting fully worked solutions before asking learners to solve problems independently, so novices study expert performance instead of searching for it.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
sources:
  - id: sweller-1985
    resource: "https://doi.org/10.1207/s1532690xci0201_3"
    title: "Sweller, J., & Cooper, G. A. (1985). The use of worked examples as a substitute for problem solving in learning algebra. *Cognition and Instruction, 2*(1), 59–89"
    author: "Sweller, J., & Cooper, G. A"
  - id: renkl-2002
    resource: "https://doi.org/10.1037/0022-0663.94.2.392"
    title: "Renkl, A. (2002). Learning from worked-out examples: Instructional explanations supplement self-explanations. *Journal of Educational Psychology, 94*(2), 392–400"
    author: "Renkl, A"
  - id: van-gog-2010
    resource: "https://doi.org/10.1007/s10648-010-9134-7"
    title: "van Gog, T., & Rummel, N. (2010). Example-based learning: Integrating cognitive and social-cognitive research perspectives. *Educational Psychology Review, 22*(2), 155–174"
    author: "van Gog, T., & Rummel, N"
---

# Worked Examples First

> **Strategy** · [All strategies](index.md)

## Description
Worked Examples First is a sequencing strategy: before learners attempt problems on their own, they study one or more fully solved, step-annotated examples of the same problem type. The example substitutes for early problem solving, showing both the procedure and the reasoning behind each step, and is typically followed by a similar problem the learner solves independently.

## Design Implications

For novices, unguided problem solving forces working memory to be spent on search — trying solution paths, backtracking, and holding partial results — rather than on building a schema for the problem type [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+S]. Studying a worked example externalizes those intermediate states, letting learners attend to *why* each step follows from the last. The strategy works best when learners actively self-explain the steps rather than passively read them [Self-explanation prompts improve learning from worked examples.](../claims/self-explanation-improves-learning.md) [+S], and when each example is immediately paired with a problem to solve [Pairing worked examples with practice or fading supports transfer better than examples alone.](../claims/worked-examples-with-practice-improve-transfer.md) [+S].

### Context
#### Requirements
- Examples that are isomorphic or near-isomorphic to the target problems, so the studied schema transfers directly
- Step-level annotation or explanation of reasoning, not just the final solution ([Think-Aloud](../elements/think-aloud.md) narration or written rationale)
- An immediate follow-on problem for the learner to solve ([Practice](../elements/practice.md))
- A plan for fading: alternating example–problem pairs, then completion problems, then full problems ([Fading](../elements/fading.md))

#### Constraints
- Examples alone, without paired practice, produce strong illusions of competence and poor transfer [Pairing worked examples with practice or fading supports transfer better than examples alone.](../claims/worked-examples-with-practice-improve-transfer.md) [-S]
- For learners with substantial prior knowledge, worked examples are redundant and can *impair* learning relative to problem solving [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~S] — the expertise reversal effect
- Splitting an example across a diagram and separate text forces split attention and degrades learning [Split-attention from separated sources degrades worked-example learning.](../claims/split-attention-effect-degrades-learning.md) [+S] — integrate steps with the diagram
- A single example can anchor learners to one solution method; multiple contrasting examples reduce this [Comparing contrasting cases improves learning.](../claims/comparing-contrasting-cases-improves-learning.md) [+M]

#### Implementation Variability
- **Alternating pairs:** example, then isomorphic problem, repeated across a sequence — the classic Sweller–Cooper format
- **Completion problems:** give the setup and partial solution; learners fill in missing steps as a bridge between studying and solving
- **Multiple contrasting examples:** two examples differing on one feature, studied side by side to highlight the condition that matters
- **Erroneous examples:** learners find and fix a flawed worked solution, sharpening discrimination ([Non-Examples](../elements/non-examples.md))

### Target Learners
- Novices encountering a new problem type, who otherwise waste capacity on means-ends search [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+S]
- Learners with low prior knowledge in the domain; benefit shrinks and can reverse as expertise grows [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~S]
- Less suitable for advanced learners, who learn more from solving problems directly

### Target Learning Goals
- Procedural fluency: acquiring standard solution procedures efficiently
- Schema construction: recognizing problem types and mapping them to solution methods
- Conditional knowledge: knowing *when* a method applies (best served by contrasting examples)

### Instructions
1. Select or write a fully solved example isomorphic to the target problem type, with each step annotated with its rationale.
2. Present the example first, integrated with any diagram, and prompt learners to self-explain key steps [Self-explanation prompts improve learning from worked examples.](../claims/self-explanation-improves-learning.md) [+S].
3. Immediately follow with an isomorphic problem the learner solves alone [Pairing worked examples with practice or fading supports transfer better than examples alone.](../claims/worked-examples-with-practice-improve-transfer.md) [+S].
4. Fade support across the sequence: full example → completion problem → full problem ([Fading](../elements/fading.md)).
5. As expertise grows, drop examples and shift to unsupported problem solving [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~S].

## Related Strategies
- [Completion Problems First](completion-problems-first.md) — the intermediate rung between studying full examples and solving alone
- [Self-Explanation Prompting](self-explanation-prompting.md) — the mechanism that converts example study into schema construction
- [Contrasting Cases](contrasting-cases.md) — multiple examples that highlight when a method applies

## Examples
- **[Use Worked Examples](../strategies/use_worked_examples.md)** — the canonical implementation: a solved problem with step-by-step reasoning followed by a similar problem.
- **Sweller & Cooper's algebra sequence (1985)** — alternating worked-example/problem pairs replaced conventional problem solving in algebra instruction, halving time-to-criterion while improving test accuracy.
- **[Khan Academy](https://www.khanacademy.org)** — narrated step-by-step solution videos precede practice sets; on-demand hints function as partial worked examples during problem solving.
- **[Codecademy](https://www.codecademy.com)** — annotated working code shown before each exercise; learners modify a demonstrated solution before writing their own.

## Key Sources
- Sweller, J., & Cooper, G. A. (1985). The use of worked examples as a substitute for problem solving in learning algebra. *Cognition and Instruction, 2*(1), 59–89. [doi:10.1207/s1532690xci0201_3](https://doi.org/10.1207/s1532690xci0201_3)
- Renkl, A. (2002). Learning from worked-out examples: Instructional explanations supplement self-explanations. *Journal of Educational Psychology, 94*(2), 392–400. [doi:10.1016/s0959-4752(01)00030-5](https://doi.org/10.1016/s0959-4752(01)00030-5)
- van Gog, T., & Rummel, N. (2010). Example-based learning: Integrating cognitive and social-cognitive research perspectives. *Educational Psychology Review, 22*(2), 155–174. [doi:10.1007/s10648-010-9134-7](https://doi.org/10.1007/s10648-010-9134-7)
- Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J. (2003). The expertise reversal effect. *Educational Psychologist, 38*(1), 23–31. [doi:10.1207/S15326985EP3801_4](https://doi.org/10.1207/S15326985EP3801_4)
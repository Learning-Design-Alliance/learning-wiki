---
type: strategy
id: worked-examples-first
aliases: [worked_examples_first]
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
  - id: renkl-2014
    resource: "https://doi.org/10.1080/00461520.2014.885893"
    title: "Renkl, A. (2014). Toward an instructionally oriented theory of example-based learning. *Cognitive Science, 38*(1), 1–37"
    author: "Renkl, A"
  - id: kalyuga-2003
    resource: "https://doi.org/10.1037/0278-7393.29.2.233"
    title: "Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J. (2003). The expertise reversal effect. *Educational Psychologist, 38*(1), 23–31"
    author: "Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J"
---

# Worked Examples First

> **Strategy** · [All strategies](index.md)
> **Evidence** · 6 claims (5 for, 1 mixed) · 12 studies (5 causal, 4 quant-synthesis, 1 review, 1 associational, 1 theoretical), `q2`–`q4` · 3 of 12 report an effect size · 2 claims rest on one study

## Description
Worked Examples First is a sequencing strategy: before learners attempt problems on their own, they study one or more fully solved, step-annotated examples of the same problem type. The example substitutes for early problem solving, showing both the procedure and the reasoning behind each step, and is typically followed by a similar problem the learner solves independently.

## Design Implications

For novices, unguided problem solving forces working memory to be spent on search — trying solution paths, backtracking, and holding partial results — rather than on building a schema for the problem type [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+S]. Studying a worked example externalizes those intermediate states, letting learners attend to *why* each step follows from the last. The strategy works best when learners actively self-explain the steps rather than passively read them [Self-explanation prompts improve learning from worked examples.](../claims/self-explanation-improves-conceptual-understanding.md) [+S], and when each example is immediately paired with a problem to solve [Example-based sequences outperform problem-only practice for novices, and fading support is argued to aid transfer](../claims/worked-examples-with-practice-improve-transfer.md) [+S].

### Context
#### Requirements
- Examples that are isomorphic or near-isomorphic to the target problems, so the studied schema transfers directly
- Step-level annotation or explanation of reasoning, not just the final solution ([Think-Aloud](../elements/think-aloud.md) narration or written rationale)
- An immediate follow-on problem for the learner to solve ([Practice](../elements/practice.md))
- A plan for fading: alternating example–problem pairs, then completion problems, then full problems ([Fading](../elements/fading.md))
- Well-structured tasks with a correct, generalizable solution method
- A fading plan: full examples → completion problems (partially worked) → unsolved problems

#### Constraints
- Examples alone, without paired practice, produce strong illusions of competence and poor transfer [Example-based sequences outperform problem-only practice for novices, and fading support is argued to aid transfer](../claims/worked-examples-with-practice-improve-transfer.md) [-S]
- For learners with substantial prior knowledge, worked examples are redundant and can *impair* learning relative to problem solving [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~S] — the expertise reversal effect
- Splitting an example across a diagram and separate text forces split attention and degrades learning [Split-attention from separated sources degrades worked-example learning.](../claims/split-attention-effect-degrades-learning.md) [+S] — integrate steps with the diagram
- A single example can anchor learners to one solution method; multiple contrasting examples reduce this [Comparing contrasting cases improves learning.](../claims/comparing-contrasting-cases-improves-learning.md) [+M]
- For learners with substantial prior knowledge, worked examples impose redundancy and slow learning relative to problem solving [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [-S] — the [expertise reversal effect](../theories/expertise-reversal-effect.md)
- Ill-structured or open-ended tasks (design, argumentation) lack a single canonical solution, limiting the strategy's applicability [~M]
- Splitting attention between a problem statement, diagram, and solution steps degrades the benefit; integrate text and visuals physically ([Cognitive Load Management](../principles/cognitive-load-management.md))

#### Implementation Variability
- **Alternating pairs:** example, then isomorphic problem, repeated across a sequence — the classic Sweller–Cooper format
- **Completion problems:** give the setup and partial solution; learners fill in missing steps as a bridge between studying and solving
- **Multiple contrasting examples:** two examples differing on one feature, studied side by side to highlight the condition that matters
- **Erroneous examples:** learners find and fix a flawed worked solution, sharpening discrimination ([Non-Examples](../elements/non-examples.md))
- **Example–problem pairs**: alternate one worked example with one isomorphic practice problem — the most robustly supported format [+S]
- **Completion problems**: present a partially worked solution the learner must finish, bridging observation and independent performance
- **Faded worked examples**: a sequence of examples with progressively more steps omitted
- **Erroneous examples**: present a flawed solution for learners to diagnose, sharpening discrimination of common misconceptions

### Target Learners
- Novices encountering a new problem type, who otherwise waste capacity on means-ends search [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+S]
- Learners with low prior knowledge in the domain; benefit shrinks and can reverse as expertise grows [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~S]
- Less suitable for advanced learners, who learn more from solving problems directly
- Learners prone to math or code anxiety, for whom a safe model to study lowers the cost of early failure

### Target Learning Goals
- Procedural fluency: acquiring standard solution procedures efficiently
- Schema construction: recognizing problem types and mapping them to solution methods
- Conditional knowledge: knowing *when* a method applies (best served by contrasting examples)
- Procedural fluency: algorithms, transformations, syntax, and multi-step methods
- Schema construction: recognizing which solution method applies to which problem structure
- Conditional knowledge: via annotated examples, learning *when* and *why* to apply a procedure

### Instructions
1. Select or write a fully solved example isomorphic to the target problem type, with each step annotated with its rationale.
2. Present the example first, integrated with any diagram, and prompt learners to self-explain key steps [Self-explanation prompts improve learning from worked examples.](../claims/self-explanation-improves-conceptual-understanding.md) [+S].
3. Immediately follow with an isomorphic problem the learner solves alone [Example-based sequences outperform problem-only practice for novices, and fading support is argued to aid transfer](../claims/worked-examples-with-practice-improve-transfer.md) [+S].
4. Fade support across the sequence: full example → completion problem → full problem ([Fading](../elements/fading.md)).
5. As expertise grows, drop examples and shift to unsupported problem solving [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~S].

## Related Strategies
- [Completion Problems First](completion-problems-first.md) — the intermediate rung between studying full examples and solving alone
- [Self-Explanation Prompting](self-explanation-prompting.md) — the mechanism that converts example study into schema construction
- [Contrasting Cases](contrasting-cases.md) — multiple examples that highlight when a method applies
- [Use Worked Examples](use_worked_examples.md) — the core tactic this sequencing strategy organizes
- [Think-Aloud Modeling](think-aloud-modeling.md) — narration method that makes worked steps pedagogically meaningful
- [I Do, We Do, You Do](i_do_we_do_you_do.md) — a live, interactive variant of the same gradual-release logic

## Examples
- **[Use Worked Examples](../strategies/use_worked_examples.md)** — the canonical implementation: a solved problem with step-by-step reasoning followed by a similar problem.
- **Sweller & Cooper's algebra sequence (1985)** — alternating worked-example/problem pairs replaced conventional problem solving in algebra instruction, halving time-to-criterion while improving test accuracy.
- **[Khan Academy](https://www.khanacademy.org)** — narrated step-by-step solution videos precede practice sets; on-demand hints function as partial worked examples during problem solving.
- **[Codecademy](https://www.codecademy.com)** — annotated working code shown before each exercise; learners modify a demonstrated solution before writing their own.
- **Sweller & Cooper's algebra studies** — learners studying worked example–problem pairs outperformed those solving the same problems unaided, with far less time on task ([doi:10.1207/s1532690xci0201_3](https://doi.org/10.1207/s1532690xci0201_3)).
- **[Khan Academy](https://www.khanacademy.org)** — narrated worked examples precede practice sets; on-demand hints function as progressive fading within each exercise.
- **[Codecademy](https://www.codecademy.com)** — annotated reference code is shown before each coding exercise, enacting the example–problem pair.
- **[Brilliant.org](https://brilliant.org)** — sequences solved examples with step-by-step explanations before escalating to independent problems.

## Key Sources
- Sweller, J., & Cooper, G. A. (1985). The use of worked examples as a substitute for problem solving in learning algebra. *Cognition and Instruction, 2*(1), 59–89. [doi:10.1207/s1532690xci0201_3](https://doi.org/10.1207/s1532690xci0201_3)
- Renkl, A. (2002). Learning from worked-out examples: Instructional explanations supplement self-explanations. *Journal of Educational Psychology, 94*(2), 392–400. [doi:10.1016/s0959-4752(01)00030-5](https://doi.org/10.1016/s0959-4752(01)00030-5)
- van Gog, T., & Rummel, N. (2010). Example-based learning: Integrating cognitive and social-cognitive research perspectives. *Educational Psychology Review, 22*(2), 155–174. [doi:10.1007/s10648-010-9134-7](https://doi.org/10.1007/s10648-010-9134-7)
- Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J. (2003). The expertise reversal effect. *Educational Psychologist, 38*(1), 23–31. [doi:10.1207/S15326985EP3801_4](https://doi.org/10.1207/S15326985EP3801_4)
- Renkl, A. (2014). Toward an instructionally oriented theory of example-based learning. *Cognitive Science, 38*(1), 1–37. [doi:10.1111/cogs.12086](https://doi.org/10.1111/cogs.12086)

<!-- merged 2026-10-09 from strategies/worked_examples_first ("Worked_Examples_First"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Worked_Examples_First

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (3 for, 1 mixed) · 7 studies (4 causal, 1 quant-synthesis, 1 review, 1 theoretical), `q3`–`q4` · 1 of 7 report an effect size · 1 claim rests on one study

## Description
Worked_Examples_First sequences instruction so that learners encounter one or more fully worked solutions — with reasoning made explicit — *before* attempting problems on their own. The strategy replaces early unguided problem solving, where novices flounder in means-ends search, with careful study of expert solutions, followed by paired practice and progressive fading of support.

## Design Implications

Studying worked examples reduces the extraneous cognitive load of unguided search, freeing working memory for schema construction [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+S]. The strategy works only when learners actually process examples deeply — self-explanation prompts, [Fading](../elements/fading.md) to completion problems, and alternating example–problem pairs all substantially improve outcomes over examples alone [Example-based sequences outperform problem-only practice for novices, and fading support is argued to aid transfer](../claims/worked-examples-with-practice-improve-transfer.md) [+S]. As expertise grows, the same support becomes redundant and can actively impair learning [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~S].

### Context
#### Requirements
- Well-structured tasks with a correct, generalizable solution method
- Step annotations or [Think-Aloud](../elements/think-aloud.md) commentary explaining *why* each step is taken, not just *what* is done
- An example–problem pairing: each worked example immediately followed by an isomorphic problem for the learner to solve ([Practice](../elements/practice.md))
- A fading plan: full examples → completion problems (partially worked) → unsolved problems

#### Constraints
- For learners with substantial prior knowledge, worked examples impose redundancy and slow learning relative to problem solving [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [-S] — the [expertise reversal effect](../theories/expertise-reversal-effect.md)
- Passive reading of examples produces an illusion of competence; without self-explanation prompts or paired problems, learners recognize solutions they cannot generate [Example-based sequences outperform problem-only practice for novices, and fading support is argued to aid transfer](../claims/worked-examples-with-practice-improve-transfer.md) [-S]
- Ill-structured or open-ended tasks (design, argumentation) lack a single canonical solution, limiting the strategy's applicability [~M]
- Splitting attention between a problem statement, diagram, and solution steps degrades the benefit; integrate text and visuals physically ([Cognitive Load Management](../principles/cognitive-load-management.md))

#### Implementation Variability
- **Example–problem pairs**: alternate one worked example with one isomorphic practice problem — the most robustly supported format [+S]
- **Completion problems**: present a partially worked solution the learner must finish, bridging observation and independent performance
- **Faded worked examples**: a sequence of examples with progressively more steps omitted
- **Erroneous examples**: present a flawed solution for learners to diagnose, sharpening discrimination of common misconceptions
- **Comparing cases**: present two worked examples side by side for learners to contrast solution methods [Comparing contrasting cases improves learning.](../claims/comparing-contrasting-cases-improves-learning.md) [+M]

### Target Learners
- Novices encountering a new problem type, who otherwise waste effort on unguided search [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+S]
- Learners with low prior knowledge in the domain; benefit diminishes and reverses as expertise develops [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~S]
- Learners prone to math or code anxiety, for whom a safe model to study lowers the cost of early failure

### Target Learning Goals
- Procedural fluency: algorithms, transformations, syntax, and multi-step methods
- Schema construction: recognizing which solution method applies to which problem structure
- Conditional knowledge: via annotated examples, learning *when* and *why* to apply a procedure

### Instructions
1. Select or author a canonical worked solution for the target task type, with steps annotated for reasoning.
2. Present the worked example with self-explanation prompts ("Why is this step valid here?") to force deep processing.
3. Immediately follow with an isomorphic problem the learner solves alone ([Practice](../elements/practice.md)).
4. Fade support across the sequence: full example → [Fading](../elements/fading.md) via completion problems → independent problems.
5. Monitor for the expertise reversal point; once learners solve problems fluently, drop examples and increase problem solving.
6. Use [Non-Examples](../elements/non-examples.md) or [Comparing Cases](../elements/comparing-cases.md) to prevent anchoring to a single method.

## Related Strategies
- [Use Worked Examples](use_worked_examples.md) — the core tactic this sequencing strategy organizes
- [Think-Aloud Modeling](think-aloud-modeling.md) — narration method that makes worked steps pedagogically meaningful
- [I Do, We Do, You Do](i_do_we_do_you_do.md) — a live, interactive variant of the same gradual-release logic

## Examples
- **Sweller & Cooper's algebra studies** — learners studying worked example–problem pairs outperformed those solving the same problems unaided, with far less time on task ([doi:10.1207/s1532690xci0201_3](https://doi.org/10.1207/s1532690xci0201_3)).
- **[Khan Academy](https://www.khanacademy.org)** — narrated worked examples precede practice sets; on-demand hints function as progressive fading within each exercise.
- **[Codecademy](https://www.codecademy.com)** — annotated reference code is shown before each coding exercise, enacting the example–problem pair.
- **[Brilliant.org](https://brilliant.org)** — sequences solved examples with step-by-step explanations before escalating to independent problems.

## Key Sources
- Sweller, J., & Cooper, G. A. (1985). The use of worked examples as a substitute for problem solving in learning algebra. *Cognition and Instruction, 2*(1), 59–89. [doi:10.1207/s1532690xci0201_3](https://doi.org/10.1207/s1532690xci0201_3)
- Renkl, A. (2014). Toward an instructionally oriented theory of example-based learning. *Cognitive Science, 38*(1), 1–37. [doi:10.1111/cogs.12086](https://doi.org/10.1111/cogs.12086)
- Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J. (2003). The expertise reversal effect. *Educational Psychologist, 38*(1), 23–31. [doi:10.1207/s15326985ep3801_4](https://doi.org/10.1207/s15326985ep3801_4)
- van Gog, T., & Rummel, N. (2010). Example-based learning: Integrating cognitive and social-cognitive research perspectives. *Educational Psychology Review, 22*(2), 155–174. [doi:10.1007/s10648-010-9134-7](https://doi.org/10.1007/s10648-010-9134-7)
-->

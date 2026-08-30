---
type: strategy
title: Worked_Examples_First
description: Sequence instruction so learners study fully worked solutions before attempting problems themselves, then fade support as expertise grows.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
sources:
  - id: sweller-1985
    resource: "https://doi.org/10.1207/s1532690xci0201_3"
    title: "Sweller, J., & Cooper, G. A. (1985). The use of worked examples as a substitute for problem solving in learning algebra. *Cognition and Instruction, 2*(1), 59–89"
    author: "Sweller, J., & Cooper, G. A"
  - id: renkl-2014
    resource: "https://doi.org/10.1080/00461520.2014.885893"
    title: "Renkl, A. (2014). Toward an instructionally oriented theory of example-based learning. *Cognitive Science, 38*(1), 1–37"
    author: "Renkl, A"
  - id: kalyuga-2003
    resource: "https://doi.org/10.1037/0278-7393.29.2.233"
    title: "Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J. (2003). The expertise reversal effect. *Educational Psychologist, 38*(1), 23–31"
    author: "Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J"
---

# Worked_Examples_First

## Description
Worked_Examples_First sequences instruction so that learners encounter one or more fully worked solutions — with reasoning made explicit — *before* attempting problems on their own. The strategy replaces early unguided problem solving, where novices flounder in means-ends search, with careful study of expert solutions, followed by paired practice and progressive fading of support.

## Design Implications

Studying worked examples reduces the extraneous cognitive load of unguided search, freeing working memory for schema construction [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+S]. The strategy works only when learners actually process examples deeply — self-explanation prompts, [Fading](../elements/fading.md) to completion problems, and alternating example–problem pairs all substantially improve outcomes over examples alone [Pairing worked examples with practice or fading supports transfer better than examples alone.](../claims/worked-examples-with-practice-improve-transfer.md) [+S]. As expertise grows, the same support becomes redundant and can actively impair learning [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~S].

### Context
#### Requirements
- Well-structured tasks with a correct, generalizable solution method
- Step annotations or [Think-Aloud](../elements/think-aloud.md) commentary explaining *why* each step is taken, not just *what* is done
- An example–problem pairing: each worked example immediately followed by an isomorphic problem for the learner to solve ([Practice](../elements/practice.md))
- A fading plan: full examples → completion problems (partially worked) → unsolved problems

#### Constraints
- For learners with substantial prior knowledge, worked examples impose redundancy and slow learning relative to problem solving [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [-S] — the [expertise reversal effect](../theories/expertise-reversal-effect.md)
- Passive reading of examples produces an illusion of competence; without self-explanation prompts or paired problems, learners recognize solutions they cannot generate [Pairing worked examples with practice or fading supports transfer better than examples alone.](../claims/worked-examples-with-practice-improve-transfer.md) [-S]
- Ill-structured or open-ended tasks (design, argumentation) lack a single canonical solution, limiting the strategy's applicability [~M]
- Splitting attention between a problem statement, diagram, and solution steps degrades the benefit; integrate text and visuals physically ([Cognitive Load Management](../principles/cognitive-load-management.md))

#### Implementation Variability
- **Example–problem pairs**: alternate one worked example with one isomorphic practice problem — the most robustly supported format [+S]
- **Completion problems**: present a partially worked solution the learner must finish, bridging observation and independent performance
- **Faded worked examples**: a sequence of examples with progressively more steps omitted
- **Erroneous examples**: present a flawed solution for learners to diagnose, sharpening discrimination of common misconceptions
- **Comparing cases**: present two worked examples side by side for learners to contrast solution methods [Comparing contrasting cases improves learning.](../claims/comparing-contrasting-cases-improve-learning.md) [+M]

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
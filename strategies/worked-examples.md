---
type: strategy
title: Worked Examples
description: Presenting fully solved problems with step-by-step reasoning for learners to study before attempting similar problems themselves.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Worked Examples

> **Strategy** · [All strategies](index.md)

## Description
A worked example presents a complete solution to a problem, with each step shown and often annotated with the reasoning behind it. Learners study the example before solving a similar problem themselves, substituting example study for unguided problem search during early skill acquisition. The strategy is the canonical application of [Cognitive Load Theory](../theories/cognitive-load-theory.md): novices studying worked examples avoid the means-ends search that consumes working memory without contributing to schema construction [Worked examples reduce unnecessary search for novices.](../claims/example-problem-sequences-reduce-cognitive-load.md) [+S].

## Design Implications

Worked examples are most effective when paired with isomorphic practice problems in an alternating example–problem sequence, and when support is faded as expertise develops [Pairing worked examples with practice or fading supports transfer better than examples alone.](../claims/example-problem-sequences-reduce-cognitive-load.md) [+S]. Steps should be integrated with the problem (not split across a diagram and a legend) to avoid split-attention, and extraneous prose should be cut to avoid redundancy [Clark, R. C., & Mayer, R. E. (2016)](https://doi.org/10.1002/9781119239086) [+S]. Self-explanation prompts ("Why is this step taken?") increase processing depth without adding much load [~S].

### Context
#### Requirements
- Problems with a well-structured, convergent solution path
- Steps presented in integrated, physically contiguous format with reasoning made explicit ([Think-Aloud](../elements/think-aloud.md) or written annotations)
- Isomorphic practice problems for learners to attempt immediately after studying each example ([Practice](../elements/practice.md))
- A fading plan: full examples → completion problems ([Fading](../elements/fading.md)) → unsolved problems

#### Constraints
- For learners with substantial prior knowledge, worked examples become redundant and can *impair* learning relative to problem solving [Worked-example guidance becomes less effective as learner expertise increases.](../claims/expertise-reversal-effect.md) [-S] — the expertise reversal effect
- Example study alone, without paired practice, produces overconfidence and poor transfer [Pairing worked examples with practice or fading supports transfer better than examples alone.](../claims/example-problem-sequences-reduce-cognitive-load.md) [-S]
- Ill-suited to ill-structured domains (open design, negotiation) where no single canonical solution exists
- Learners often skim examples superficially; without self-explanation prompts or completion tasks, study time collapses and learning gains vanish [~M]

#### Implementation Variability
- **Example–problem pairs**: alternate one worked example with one isomorphic problem — the most robustly supported format [Renkl, A. (2014)](https://doi.org/10.1080/00461520.2014.885653) [+S]
- **Completion problems**: present a partially worked solution the learner finishes, bridging example and independent solving [Fading](../elements/fading.md)
- **Erroneous examples**: present a flawed solution for learners to find and fix, which builds conceptual understanding and error discrimination [Erroneous examples help learners identify and correct misconceptions.](../claims/erroneous-examples-build-conceptual-knowledge.md) [+M]
- **Faded worked examples**: progressively remove later steps across a sequence as competence grows [Fading support promotes transfer of responsibility.](../claims/fading-support-promotes-transfer-of-responsibility.md) [+M]

### Target Learners
- Novices in a domain, who lack schemas to guide search and benefit most from studying complete solutions [Worked examples reduce unnecessary search for novices.](../claims/example-problem-sequences-reduce-cognitive-load.md) [+S]
- Learners with low prior knowledge in mathematics, science, programming, and other structured problem domains
- Not recommended for advanced learners, who learn more from solving problems directly [Worked-example guidance becomes less effective as learner expertise increases.](../claims/expertise-reversal-effect.md) [-M]

### Target Learning Goals
- Procedural fluency: acquiring standard solution procedures
- Schema construction: recognizing which solution method applies to which problem type
- Conceptual discrimination: via erroneous examples and [Non-Examples](../elements/non-examples.md)

### Instructions
1. Select a problem with a clear, canonical solution path and solve it fully, annotating each step with its rationale ([Think-Aloud](../elements/think-aloud.md)).
2. Present the example in integrated format — steps adjacent to the relevant part of the problem, no split sources ([Chunking](../principles/chunking.md) and [Cognitive Load Management](../principles/cognitive-load-management.md)).
3. Add a self-explanation prompt ("Why does this step follow?") to force active processing.
4. Immediately follow with an isomorphic problem the learner solves alone ([Practice](../elements/practice.md)); repeat in alternating pairs.
5. Fade support across the sequence: replace later examples with completion problems, then full problems ([Fading](../elements/fading.md)).
6. Monitor for expertise; once learners solve problems accurately and quickly, discontinue examples to avoid the reversal effect [Worked-example guidance becomes less effective as learner expertise increases.](../claims/expertise-reversal-effect.md) [-M].

## Related Strategies
- [Completion Problems](../strategies/completion-problems.md) — the intermediate fading step between full examples and independent solving
- [Erroneous Examples](../elements/erroneous-examples.md) — flawed worked examples that build error-detection skill
- [Self-Explanation Prompts](../strategies/self-explanation-prompts.md) — the processing mechanism that makes example study active
- [Modeling with Think-Alouds](../strategies/think-aloud-modeling.md) — the live, narrated counterpart to the static worked example

## Examples
- **[Use Worked Examples](../strategies/use_worked_examples.md)** — the canonical implementation: one solved problem with reasoning annotations, followed by an isomorphic problem.
- **Sweller & Cooper's algebra studies (1985)** — students studying worked examples solved subsequent algebra problems faster and with fewer errors than students practicing equivalent problems throughout [Sweller, J., & Cooper, G. A. (1985)](https://doi.org/10.1207/s1532690xci0201_3).
- **[Khan Academy](https://www.khanacademy.org)** — narrated step-by-step solution videos paired with practice exercises and on-demand hints, which function as progressive sub-fading.
- **[Codecademy](https://www.codecademy.com)** — annotated code examples shown inline before learners write their own version in the same exercise.

## Key Sources
- Sweller, J., & Cooper, G. A. (1985). The use of worked examples as a substitute for problem solving in learning algebra. *Cognition and Instruction, 2*(1), 59–89. [doi:10.1207/s1532690xci0201_3](https://doi.org/10.1207/s1532690xci0201_3)
- Renkl, A. (2014). Toward an instructionally oriented theory of example-based learning. *Cognitive Science, 38*(1), 1–37. [doi:10.1111/cogs.12086](https://doi.org/10.1111/cogs.12086)
- van Gog, T., & Rummel, N. (2010). Example-based learning: Integrating cognitive and social-cognitive research perspectives. *Educational Psychology Review, 22*(2), 155–174. [doi:10.1007/s10648-010-9134-7](https://doi.org/10.1007/s10648-010-9134-7)
- Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J. (2003). The expertise reversal effect. *Educational Psychologist, 38*(1), 23–31. [doi:10.1207/S15326985EP3801_4](https://doi.org/10.1207/S15326985EP3801_4)
- Clark, R. C., & Mayer, R. E. (2016). *E-Learning and the Science of Instruction* (4th ed.). Wiley. [doi:10.1002/9781119239086](https://doi.org/10.1002/9781119239086)
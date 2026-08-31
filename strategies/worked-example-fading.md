---
type: strategy
title: Worked Example Fading
description: A strategy that progressively transitions learners from studying fully worked examples to completing partial solutions to solving problems independently.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Worked Example Fading

> **Strategy** · [All strategies](index.md)

## Description
Worked example fading begins instruction with complete worked examples, then systematically removes steps — first the final step, then the last two, and so on — until learners solve entire problems on their own. The learner completes the truncated portion of each example, so every task sits at the boundary of current competence. This implements the completion and fading strategy from [Cognitive Load Theory](../theories/cognitive-load-theory.md) as a structured bridge from [Worked Examples](../principles/worked-examples.md) to independent [Practice](../elements/practice.md).

## Design Implications

Fading resolves the central tension of example-based learning: full examples are efficient for novices but become redundant as expertise grows, while unsupported problems overload beginners [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+M]. By matching support level to current ability, fading keeps learners in their zone of proximal development and avoids the [expertise reversal effect](../theories/expertise-reversal-effect.md) [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M]. Fading works best when paired with completion demands — learners must actively produce the missing steps, not merely observe their absence [Pairing worked examples with practice or fading supports transfer better than examples alone.](../claims/worked-examples-with-practice-improve-transfer.md) [+S].

### Context
#### Requirements
- A task domain with well-structured, sequential solution procedures (algebra, programming, physics, grammar)
- A library of isomorphic problem pairs so each faded example can be followed by a similar independent problem
- A defined fading schedule (e.g., backward fading: remove the last step first) and criteria for advancing learners
- Solution steps that can be cleanly segmented for truncation

#### Constraints
- Fading schedules that advance too quickly reintroduce unguided search and overload novices [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) [-M]
- In ill-structured domains (design, argumentation, open-ended writing) there may be no canonical steps to fade; use [Case Studies](../elements/case-studies.md) or [Comparing Cases](../elements/comparing-cases.md) instead
- Learners with higher prior knowledge profit more from early independent problem solving than from extended example study [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [-M] — a fixed fading sequence for all learners wastes expert time
- If faded steps are trivially predictable, completion tasks become busywork with little learning benefit [-W]

#### Implementation Variability
- **Backward fading** (omit final steps first) generally outperforms forward fading (omit first steps), because early steps establish the solution plan [+M]
- **Alternating example–problem pairs**: each worked example is immediately followed by an isomorphic problem to solve, rather than a block of examples then a block of problems [+S]
- **Completion problems**: learners receive a problem with an incomplete solution and fill the gap, before attempting full problems
- **Adaptive fading**: advancement is triggered by performance on completion steps rather than a fixed schedule [+W]

### Target Learners
- Novices in well-structured domains who would otherwise engage in inefficient means–ends search [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+M]
- Learners with low-to-moderate prior knowledge; the optimal starting support level rises with expertise [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M]
- Less suitable for advanced learners, who benefit from starting at or near full problem solving

### Target Learning Goals
- Procedural fluency: executing multi-step solution procedures accurately
- Schema acquisition: recognizing which solution method fits which problem structure
- Transfer to near problems: applying learned procedures to isomorphic variants [Pairing worked examples with practice or fading supports transfer better than examples alone.](../claims/worked-examples-with-practice-improve-transfer.md) [+S]

### Instructions
1. Analyze the target procedure and segment it into discrete, orderable solution steps ([Procedural Information](../elements/procedural-information.md))
2. Present a fully worked example with reasoning made explicit ([Demonstration](../elements/demonstration.md), [Think-Aloud](../elements/think-aloud.md))
3. Present a faded version of an isomorphic problem with the final step(s) removed; require the learner to complete them ([Practice](../elements/practice.md))
4. Progressively remove earlier steps across successive tasks until learners solve complete problems unaided ([Fading](../elements/fading.md))
5. Pair each example or completion task with immediate feedback and self-explanation prompts ([Self-Explanation](../elements/self-explanation.md), [Feedback](../elements/feedback.md))
6. Advance learners based on completion accuracy, not time on task ([Mastery Learning](../elements/mastery-learning.md))

## Related Strategies
- [Completion Problems](completion-problems.md) — the intermediate task format fading is built from
- [Example-Problem Pairs](../elements/example-problem-pairs.md) — the alternating structure that fading sequences typically embed
- [Self-Explanation Prompting](self-explanation-prompting.md) — prompts that deepen processing of the studied steps
- [Scaffolded Problem Sequencing](scaffolded-problem-sequencing.md) — broader difficulty management across a task series

## Examples
- **Renkl & Atkinson's fading studies** — algebra word-problem tutors that faded worked examples backward across a six-step sequence, with completion accuracy determining advancement; see the [Carnegie Learning MATHia tutor](https://www.carnegielearning.com), which operationalizes adaptive example-to-problem transitions in secondary mathematics
- **Codecademy's web development courses** — learners first read annotated, complete code, then fill in missing lines in a partially written program, then write full programs from a specification
- **Duolingo's early grammar lessons** — fully translated example sentences give way to completion items (select or type the missing word) before free production

## Key Sources
- Renkl, A., Atkinson, R. K., & Große, C. S. (2004). How fading worked solution steps works—A cognitive load perspective. *Instructional Science, 32*(1–2), 59–82. [doi:10.1023/B:TRUC.0000021815.74806.f6](https://doi.org/10.1023/B:TRUC.0000021815.74806.f6)
- Renkl, A., Atkinson, R. K., Maier, U. H., & Staley, R. (2002). From example study to problem solving: Smooth transitions help learning. *The Journal of Experimental Education, 70*(4), 293-315. [doi:10.1080/00220970209599510](https://doi.org/10.1080/00220970209599510)
- Sweller, J., & Cooper, G. A. (1985). The use of worked examples as a substitute for problem solving in learning algebra. *Cognition and Instruction, 2*(1), 59–89. [doi:10.1207/s1532690xci0201_3](https://doi.org/10.1207/s1532690xci0201_3)
- van Gog, T., & Rummel, N. (2010). Example-based learning: Integrating cognitive and social-cognitive research perspectives. *Educational Psychology Review, 22*(2), 155–174. [doi:10.1007/s10648-010-9134-7](https://doi.org/10.1007/s10648-010-9134-7)
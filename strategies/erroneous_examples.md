---
type: strategy
title: Erroneous Examples
description: Presenting deliberately flawed worked solutions for learners to diagnose, explain, and correct.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Erroneous Examples

> **Strategy** · [All strategies](index.md)

## Description
An erroneous example (also called an "incorrect example" or "faulty worked example") presents a complete but deliberately flawed solution, argument, or procedure. Learners must locate the error, explain why it is wrong, and often repair it. Rather than modeling correct performance, the flawed solution makes a common misconception or procedural slip visible and available for analysis.

## Design Implications

Diagnosing errors forces learners to articulate *why* a step is wrong, which engages deeper processing than passively studying correct solutions and directly targets conceptual understanding [Studying erroneous examples with explanation prompts improves conceptual knowledge more than correct-only examples.](../claims/erroneous-examples-build-conceptual-knowledge.md) [+M]. Errors should be plausible — drawn from real learner misconceptions or common procedural slips — so that diagnosis requires genuine reasoning rather than spotting an artificial absurdity. Because error analysis is more demanding than studying correct examples, it is typically sequenced after some correct [worked examples](../strategies/use_worked_examples.md) or paired with them in example–problem sequences [Example–problem pairs reduce cognitive load for novices relative to problem solving alone.](../claims/example-problem-sequences-reduce-cognitive-load.md) [+S].

### Context
#### Requirements
- Errors that map onto documented misconceptions of the target population, not arbitrary mistakes
- An explicit prompt to locate, explain, and (ideally) correct the error — unexplained exposure to wrong solutions risks learners encoding the error itself
- Sufficient prior knowledge to evaluate the flawed solution; learners must know what "right" looks like well enough to recognize deviation
- Feedback or a corrected version available after diagnosis ([Feedback](../elements/feedback.md))

#### Constraints
- Presenting errors without explanation prompts can teach the error: novices with weak prior knowledge may fail to detect the flaw and instead encode the incorrect procedure [-M]
- More cognitively demanding than correct worked examples; for complete novices the added load of error search can overwhelm [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) [~M]
- Effectiveness declines for learners with high prior knowledge, for whom error diagnosis adds little beyond what they already detect on their own (expertise-reversal; see [Expertise-Reversal Effect](../theories/expertise-reversal-effect.md)) [~M]
- Less suited to open-ended tasks with no canonical solution path; best for well-structured domains with identifiable misconceptions (mathematics, science, grammar, programming)

#### Implementation Variability
- **Correct-then-erroneous pairs:** a valid worked example followed by a flawed variant of the same problem, sharpening discrimination between the two
- **Completion format:** a partially correct solution where learners must find and fix the error (a hybrid with faded worked examples)
- **Peer-error analysis:** learners critique anonymous peer work, which doubles as formative assessment
- **Self-generated errors:** learners predict where *they* might go wrong before solving, using the erroneous example as a checklist

### Target Learners
- Learners with moderate prior knowledge — enough to recognize deviations from correct procedure, but still holding the target misconceptions [Studying erroneous examples with explanation prompts improves conceptual knowledge more than correct-only examples.](../claims/erroneous-examples-build-conceptual-knowledge.md) [+M]
- Learners who hold the misconception embedded in the error; diagnosing it creates [cognitive conflict](../elements/cognitive-conflict.md) that motivates conceptual change
- Not ideal for complete novices, who lack the baseline to detect the flaw [-M]

### Target Learning Goals
- Conceptual understanding: distinguishing correct principles from superficially plausible violations
- Misconception repair: surfacing and restructuring faulty mental models
- Self-monitoring: building the habit of checking one's own work for characteristic errors

### Instructions
1. Teach the correct procedure first, ideally with a [worked example](../strategies/use_worked_examples.md) so learners have a valid reference model.
2. Present the erroneous example and prompt learners to (a) locate the error, (b) explain why it violates a principle, and (c) correct it — the explanation step is what drives conceptual gains [+M].
3. Have learners compare the corrected version against the original correct example to consolidate the discrimination.
4. Follow with standard [practice](../elements/practice.md) problems, prompting learners to check their own solutions for the class of error just diagnosed.
5. Provide feedback confirming or correcting the diagnosis before misconceptions consolidate.

## Related Strategies
- [Use Worked Examples](use_worked_examples.md) — the correct-solution counterpart; erroneous examples are typically sequenced after or alongside them
- [Self-Explanation](../elements/self-explanation.md) — the explanation prompt that makes error diagnosis effective
- [Faded Worked Examples](faded-worked-examples.md) — completion-format erroneous examples blend the two approaches

## Examples
- **Incorrect examples in algebra instruction** (Renkl and colleagues' research program): students study a worked probability or algebra problem containing a typical error (e.g., adding fractions by adding numerators and denominators), explain what is wrong, then solve a near-transfer problem.
- **[Geogebra](https://www.geogebra.org) "fix the mistake" activities**: teachers share flawed constructions or proofs; students diagnose why the diagram or derivation fails.
- **Programming "debugging katas"**: courses present code with a seeded bug (off-by-one error, wrong comparison operator); learners trace execution, locate the bug, and patch it — error diagnosis as the primary practice format.

## Key Sources
- Durkin, K., & Rittle-Johnson, B. (2012). The effectiveness of using incorrect examples to support learning about decimal magnitude. *Learning and Instruction, 22*(1), 85–94. [doi:10.1016/j.learninstruc.2011.11.001](https://doi.org/10.1016/j.learninstruc.2011.11.001)
- Booth, J. L., Lange, K. E., Koedinger, K. R., & Newton, K. J. (2013). Using example problems to improve student learning in algebra: Differentiating between correct and incorrect examples. *Learning and Instruction, 25*, 24–34. [doi:10.1016/j.learninstruc.2012.11.002](https://doi.org/10.1016/j.learninstruc.2012.11.002)
- Renkl, R. (2014). Toward an instructionally oriented theory of example-based learning. *Cognitive Science, 38*(1), 1–37. [doi:10.1111/cogs.12086](https://doi.org/10.1111/cogs.12086)
- Große, C. S., & Renkl, A. (2007). Finding and fixing errors in worked examples: Can this foster learning outcomes? *Learning and Instruction, 17*(6), 612–634. [doi:10.1016/j.learninstruc.2007.09.008](https://doi.org/10.1016/j.learninstruc.2007.09.008)
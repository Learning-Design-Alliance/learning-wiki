---
type: strategy
title: Use Worked Examples
description: The instructor presents a fully solved problem — showing each step and explaining the reasoning behind it — and then asks learners to solve a similar problem independently or in pairs.
status: review
generated:
  by: claude/unspecified
  at: 2026-04-06
sources:
  - id: sweller-1985
    resource: "https://doi.org/10.1207/s1532690xci0201_3"
    title: "Sweller, J., & Cooper, G. A. (1985). The use of worked examples as a substitute for problem solving in learning algebra. *Cognition and Instruction, 2*(1), 59–89"
    author: "Sweller, J., & Cooper, G. A"
  - id: van-gog-2011
    resource: "https://doi.org/10.1016/j.cedpsych.2010.10.004"
    title: "van Gog, T., Kester, L., & Paas, F. (2011). Effects of worked examples, example–problem, and problem–example pairs on novices' learning. *Contemporary Educational Psychology, 36*(3), 212–218"
    author: "van Gog, T., Kester, L., & Paas, F"
  - id: atkinson-2000
    resource: "https://doi.org/10.3102/00346543070002181"
    title: "Atkinson, R. K., Derry, S. J., Renkl, A., & Wortham, D. (2000). Learning from examples: Instructional principles from the worked examples research. *Review of Educational Research, 70*(2), 181–214"
    author: "Atkinson, R. K., Derry, S. J., Renkl, A., & Wortham, D"
  - id: renkl-2014
    resource: "https://doi.org/10.1111/cogs.12086"
    title: "Renkl, A. (2014). Toward an instructionally oriented theory of example-based learning. *Cognitive Science, 38*(1), 1–37"
    author: Renkl, A
---

# Use Worked Examples

## Description
The instructor presents a fully solved problem — showing each step and explaining the reasoning behind it — and then asks learners to solve a similar problem independently or in pairs. The cycle of study-then-solve can repeat multiple times, with the level of detail in the example gradually reduced (faded) as learners gain confidence.

## Design Implications

By externalizing the solution process, worked examples let novices study task structure before attempting problems themselves, reducing the unproductive search that characterizes early skill acquisition [Worked examples reduce unnecessary search for novices.](/claims/worked-examples-reduce-novice-search.md) [+M]. The strategy works best when it is not passive: prompting learners to explain each step to themselves (self-explanation) substantially amplifies learning beyond silent study. Examples should be followed immediately by a practice problem of comparable difficulty — the example-then-problem sequence improves both cognitive load and transfer outcomes compared to problem-only practice [Example–problem sequences reduce cognitive load and improve learning outcomes](/claims/worked-examples-example-problem-sequences.md) [+S].

### Context
#### Requirements
- A [worked example](/elements/demonstration.md) that is clear, correctly solved, and annotated with reasoning — not just the steps
- An immediate [practice problem](/elements/practice.md) at comparable difficulty
- Optional: [self-explanation prompts](/elements/eliciting-student-thinking.md) ("Why did we do this step?") before moving to independent practice

#### Constraints
- Does not substitute for practice; learners who only study examples without solving problems do not develop fluency [Pairing worked examples with practice or fading supports transfer better than examples alone.](/claims/worked-examples-with-practice-improve-transfer.md) [-S]
- Less effective for open-ended or design tasks where there is no single correct approach
- Benefits diminish as expertise grows; continuing to use worked examples past the novice stage can become redundant or counterproductive [Worked-example guidance becomes less effective as learner expertise increases.](/claims/worked-examples-less-effective-with-expertise.md) [~M]

#### Implementation Variability
- **Faded examples:** Progressively remove steps from successive examples, requiring learners to complete the missing parts — bridges toward fully independent problem solving
- **Incorrect examples:** Present a worked example with a deliberate error and ask learners to find and fix it — effective for building error-detection and deepening procedural understanding
- **Comparison:** Present two worked examples solving the same problem by different methods and ask which is more efficient or generalizable

### Target Learners
- Novices in any domain where problem-solving involves learnable steps: mathematics, programming, science, writing, clinical reasoning
- Learners at risk of cognitive overload during unguided problem solving [Worked examples reduce unnecessary search for novices.](/claims/worked-examples-reduce-novice-search.md) [+M]
- Less beneficial once learners have sufficient prior knowledge [Worked-example guidance becomes less effective as learner expertise increases.](/claims/worked-examples-less-effective-with-expertise.md) [~M]

### Target Learning Goals
- Early procedural fluency: understanding the steps of a solution process
- Schema acquisition: recognizing the structure shared by a class of problems
- Metacognitive awareness: monitoring one's own understanding of each step

### Instructions
1. Select or write a problem that exemplifies the target skill or procedure
2. Solve it fully, annotating each step with a brief explanation of *why*, not just *what* — use [think-aloud](/elements/think-aloud.md) if delivering live
3. Ask learners to study the example and, if time permits, prompt self-explanation: "In your own words, why does this step work?"
4. Present a near-transfer [practice problem](/elements/practice.md) of similar structure before providing feedback
5. Repeat with a second example-problem pair, optionally fading detail from the example
6. As learners gain confidence, shift to problem-only practice

## Related Strategies
- [Worked Example Routine](/strategies/worked_example_routine.md) — a structured classroom routine that formalizes this cycle
- [Comparing Multiple Solution Methods](/strategies/comparing_multiple_solution_methods.md) — an extension that pairs two worked examples for comparison
- [Think-Aloud Modeling](/strategies/think-aloud-modeling.md) — the live narration technique for delivering demonstrations

## Examples

**Mathematics (secondary):** Teacher works through a two-step equation on the board, narrating each algebraic move ("I'm dividing both sides because I want to isolate x"). Students then solve a similar equation independently before the class discusses it. Common in direct instruction math curricula such as Saxon Math and Singapore Math.

**Programming (introductory CS):** An annotated code example shows how to write a function with a loop; comments explain the logic at each line. Students then write a function that solves a parallel problem. Used extensively in [CS50](https://cs50.harvard.edu), [Codecademy](https://www.codecademy.com), and most introductory coding textbooks.

**Science (lab skills):** Before students conduct a titration, the instructor performs one live with narrated reasoning. Students complete their own titrations with a checklist that mirrors the steps shown. The checklist is removed in subsequent labs as fluency develops.

**Writing (argument structure):** Teacher annotates a model paragraph (claim → evidence → warrant) using a think-aloud. Students then write their own paragraph on a different topic using the same structure, with the annotated model visible for reference until it is faded in later assignments.

## Key Sources
- Sweller, J., & Cooper, G. A. (1985). The use of worked examples as a substitute for problem solving in learning algebra. *Cognition and Instruction, 2*(1), 59–89. [doi:10.1207/s1532690xci0201_3](https://doi.org/10.1207/s1532690xci0201_3)
- van Gog, T., Kester, L., & Paas, F. (2011). Effects of worked examples, example–problem, and problem–example pairs on novices' learning. *Contemporary Educational Psychology, 36*(3), 212–218. [doi:10.1016/j.cedpsych.2010.10.004](https://doi.org/10.1016/j.cedpsych.2010.10.004)
- Atkinson, R. K., Derry, S. J., Renkl, A., & Wortham, D. (2000). Learning from examples: Instructional principles from the worked examples research. *Review of Educational Research, 70*(2), 181–214. [doi:10.3102/00346543070002181](https://doi.org/10.3102/00346543070002181)
- Renkl, A. (2014). Toward an instructionally oriented theory of example-based learning. *Cognitive Science, 38*(1), 1–37. [doi:10.1111/cogs.12086](https://doi.org/10.1111/cogs.12086)

---
type: strategy
status: review
last_edited: 2026-04-06
edited_by: Claude
---

# Use Worked Examples

## Description
The instructor presents a fully solved problem — showing each step and explaining the reasoning behind it — and then asks learners to solve a similar problem independently or in pairs. The cycle of study-then-solve can repeat multiple times, with the level of detail in the example gradually reduced (faded) as learners gain confidence.

## Design Implications

By externalizing the solution process, worked examples let novices study task structure before attempting problems themselves, reducing the unproductive search that characterizes early skill acquisition [[claims/we-1]] [+M]. The strategy works best when it is not passive: prompting learners to explain each step to themselves (self-explanation) substantially amplifies learning beyond silent study. Examples should be followed immediately by a practice problem of comparable difficulty — the example-then-problem sequence improves both cognitive load and transfer outcomes compared to problem-only practice [[claims/worked-examples-example-problem-sequences]] [+S].

### Context
#### Requirements
- A [[elements/demonstration|worked example]] that is clear, correctly solved, and annotated with reasoning — not just the steps
- An immediate [[elements/practice|practice problem]] at comparable difficulty
- Optional: [[elements/eliciting-student-thinking|self-explanation prompts]] ("Why did we do this step?") before moving to independent practice

#### Constraints
- Does not substitute for practice; learners who only study examples without solving problems do not develop fluency [[claims/we-2]] [-S]
- Less effective for open-ended or design tasks where there is no single correct approach
- Benefits diminish as expertise grows; continuing to use worked examples past the novice stage can become redundant or counterproductive [[claims/we-3]] [~M]

#### Implementation Variability
- **Faded examples:** Progressively remove steps from successive examples, requiring learners to complete the missing parts — bridges toward fully independent problem solving
- **Incorrect examples:** Present a worked example with a deliberate error and ask learners to find and fix it — effective for building error-detection and deepening procedural understanding
- **Comparison:** Present two worked examples solving the same problem by different methods and ask which is more efficient or generalizable

### Target Learners
- Novices in any domain where problem-solving involves learnable steps: mathematics, programming, science, writing, clinical reasoning
- Learners at risk of cognitive overload during unguided problem solving [[claims/we-1]] [+M]
- Less beneficial once learners have sufficient prior knowledge [[claims/we-3]] [~M]

### Target Learning Goals
- Early procedural fluency: understanding the steps of a solution process
- Schema acquisition: recognizing the structure shared by a class of problems
- Metacognitive awareness: monitoring one's own understanding of each step

### Instructions
1. Select or write a problem that exemplifies the target skill or procedure
2. Solve it fully, annotating each step with a brief explanation of *why*, not just *what* — use [[elements/think-aloud|think-aloud]] if delivering live
3. Ask learners to study the example and, if time permits, prompt self-explanation: "In your own words, why does this step work?"
4. Present a near-transfer [[elements/practice|practice problem]] of similar structure before providing feedback
5. Repeat with a second example-problem pair, optionally fading detail from the example
6. As learners gain confidence, shift to problem-only practice

## Related Strategies
- [[strategies/worked_example_routine|Worked Example Routine]] — a structured classroom routine that formalizes this cycle
- [[strategies/comparing_multiple_solution_methods|Comparing Multiple Solution Methods]] — an extension that pairs two worked examples for comparison
- [[strategies/think-aloud-modeling|Think-Aloud Modeling]] — the live narration technique for delivering demonstrations

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

---
type: strategy
id: whats_my_number
title: What’s My Number?
description: A guessing game where one person thinks of a number and provides clues, and others use logical reasoning and deduction to determine the number.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# What’s My Number?

> **Strategy** · [All strategies](index.md)

## Description
One player (or the instructor) selects a secret number within a stated range and reveals incremental clues — comparisons ("greater than 20"), properties ("even," "a multiple of 5"), or digit information — while other players narrow the candidate set through logical deduction. Each clue and guess is an opportunity to reason aloud about what the information eliminates, making the game a low-stakes vehicle for number sense, inequality reasoning, and strategic question-asking.

## Design Implications

The game's power comes from forcing learners to maintain and update a shrinking candidate set, which exercises the same constraint-satisfaction reasoning underlying algebra and proof. Because each clue restructures the problem space, the game rewards systematic elimination over random guessing; instructors should make that elimination visible (e.g., crossing out numbers on a hundred chart) to reduce working-memory demands [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+S]. Asking players to justify guesses before they are confirmed converts the game into a self-explanation activity, which improves conceptual understanding beyond what play alone produces [Self-explanation improves conceptual understanding.](../claims/self-explanation-improves-conceptual-understanding.md) [+S].

### Context
#### Requirements
- A clearly stated number range so the candidate set is well-defined
- Clues that are logically consistent and progressively informative; ambiguous clues stall the deduction chain
- An external representation (number line, hundred chart, written list) so learners can track eliminated candidates instead of holding them in memory
- A norm that players explain *why* a guess follows from the clues, not just name a number

#### Constraints
- Vague or contradictory clues break the deduction chain and turn the activity into pure guessing [-M]
- Learners with weak number sense may not be able to generate candidate sets at all, leaving them excluded from the reasoning; the range must be small enough that every player can enumerate it
- If the range is very large and clues are sparse, search becomes unguided and low-yield for novices [~M] — analogous to the unguided-search problem that makes pure discovery inefficient for novices
- Whole-class formats let most students go passive; only the guesser reasons unless every student records and updates their own candidate set

#### Implementation Variability
- **Reverse format:** students give clues for a teacher-chosen number, shifting the challenge from deduction to clue design — a harder task requiring deeper property knowledge
- **Twenty-Questions variant:** students earn points for guessing in fewer questions, rewarding optimal information-seeking (binary-search style halving)
- **Range scaling:** 1–10 for early counters, 1–100 with a hundred chart for mid-elementary, negative numbers or decimals for older students
- **Fraction/decimal variant:** clues reference benchmarks ("closer to ½ than to 1") to build magnitude reasoning

### Target Learners
- Elementary students building number sense and magnitude comparison; number-line and board-game formats with similar structure show measurable gains in numerical knowledge for young children [Playing linear number board games improves children's numerical knowledge.](https://doi.org/10.1037/0012-1649.44.2.345) [+S]
- Struggling students benefit when the range is small and a visual candidate set is provided, reducing load [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+S]
- Advanced students need larger ranges, sparser clues, or the clue-designing role to avoid trivial search

### Target Learning Goals
- Number sense: magnitude comparison, place value, and properties of numbers (odd/even, multiples, primes)
- Logical deduction: constraint satisfaction and systematic elimination
- Strategic questioning: choosing questions that maximize information gained
- Mathematical communication: justifying reasoning aloud

### Instructions
1. State the range and display the candidate set on a number line or hundred chart ([Problem Presentation](../elements/problem-presentation.md) if available; otherwise a posted chart).
2. The number-holder gives the first clue; players mark which candidates remain ([Application of Knowledge](../elements/application-of-knowledge.md)).
3. Before each guess, the player states which numbers are still possible and why ([Articulation](../elements/articulation.md)).
4. After the reveal, debrief one question: "Which clue eliminated the most numbers?" — feedback at the strategy level, not just right/wrong [Feedback is most effective at task and process levels.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S].
5. Rotate roles; when students become number-holders, require them to plan a clue sequence in advance.

## Related Strategies
- Twenty Questions — the same information-seeking structure applied to non-numerical domains
- Number Talks — complementary routine for building magnitude and computation reasoning through discourse
- Guess My Rule — the property-based clue variant focused on pattern and function rather than a single value

## Related Elements
- [Application of Knowledge](../elements/application-of-knowledge.md) — each guess applies number properties to a live problem
- [Articulation](../elements/articulation.md) — the justification norm that turns guessing into reasoning
- [Coaching](../elements/coaching.md) — instructor prompts ("What do you know for sure?") scaffold deduction
- [Assessment](../elements/assessment.md) — clues-needed-to-solve and justification quality serve as observable evidence

## Examples
- **Mental Math routines (K–5 classrooms):** "Guess My Number" on a hundred chart is a standard warm-up in Number Talks–style elementary curricula; teachers cross out eliminated numbers publicly so the whole class tracks the shrinking set.
- **Binary-search CS teaching:** the game is a common unplugged introduction to binary search — asking students to minimize guesses in 1–100 leads them to rediscover halving, connecting the game to algorithm design.
- **Fraction variant (grades 4–6):** secret number between 0 and 1 with benchmark clues ("greater than ¾") on a fraction number line builds rational-number magnitude, a known weak spot in elementary mathematics.

## Key Sources
- Ramani, G. B., & Siegler, R. S. (2008). Promoting broad and stable improvements in low-income children's numerical knowledge through playing number board games. *Child Development, 79*(2), 375–394. [doi:10.1111/j.1467-8624.2007.01131.x](https://doi.org/10.1111/j.1467-8624.2007.01131.x)
- Siegler, R. S., & Ramani, G. B. (2009). Playing linear number board games — but not circular ones — improves low-income preschoolers' numerical understanding. *Journal of Educational Psychology, 101*(3), 545–560. [doi:10.1037/a0014239](https://doi.org/10.1037/a0014239)
- Chi, M. T. H., de Leeuw, N., Chiu, M.-H., & LaVancher, C. (1994). Eliciting self-explanations improves understanding. *Cognitive Science, 18*(3), 439–477. [doi:10.1207/s15516709cog1803_3](https://doi.org/10.1207/s15516709cog1803_3)
- Hattie, J., & Timperley, H. (2007). The power of feedback. *Review of Educational Research, 77*(1), 81–112. [doi:10.3102/003465430298487](https://doi.org/10.3102/003465430298487)

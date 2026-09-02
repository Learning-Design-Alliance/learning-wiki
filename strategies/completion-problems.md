---
type: strategy
id: completion-problems
title: Completion Problems
description: Learners are given a partially solved problem and must complete the remaining steps, bridging worked examples and independent problem solving.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Completion Problems

> **Strategy** · [All strategies](index.md)

## Description
A completion problem (also called a completion strategy or fade-in problem) presents learners with a task that is partially solved — the initial steps are provided, and the learner must supply the remainder. It sits between a full [worked example](../principles/worked-examples.md) and an unsolved problem, operationalizing the "completion strategy" from early cognitive load research [van Merriënboer, 1990]. As expertise grows, the proportion completed by the learner increases until they solve problems independently.

## Design Implications

Completion problems reduce the unguided search that overwhelms novices while still requiring generative processing — the learner must actually execute part of the solution rather than merely study one [Example–problem sequences reduce cognitive load for novices.](../claims/example-problem-sequences-reduce-cognitive-load.md) [+S]. This makes them more effective than worked examples alone at producing transferable skill, because the completion requirement combats the passive "illusion of understanding" that pure example study can induce [Pairing worked examples with practice or fading supports transfer better than examples alone.](../claims/worked-examples-with-practice-improve-transfer.md) [+S]. The design decision is the *completion ratio*: how much is given versus left to the learner, and how that ratio shifts across a task sequence.

### Context
#### Requirements
- A set of high-quality worked solutions to draw the completed portion from
- A task sequence in which the completed portion shrinks (and learner-supplied portion grows) as competence develops ([Fading](../claims/fading-support-promotes-transfer-of-responsibility.md))
- Clear marking of which steps are given and which the learner must supply, so learners do not waste effort parsing the interface rather than the content
- Feedback or a correct final solution available for self-checking after completion

#### Constraints
- For learners with high prior knowledge, the provided portion is redundant and adds extraneous load rather than reducing it [Guidance becomes less effective — and can reverse in benefit — as expertise grows.](../claims/expertise-reversal-effect.md) [-M]
- If the completed portion is too large for too long, learners engage in shallow copy-and-continue behavior instead of reasoning [Pairing worked examples with practice or fading supports transfer better than examples alone.](../claims/worked-examples-with-practice-improve-transfer.md) [-M]
- Poorly aligned given/learner portions (e.g., giving the conceptually hard steps and asking for mechanical ones) undermine the intended scaffolding
- In ill-structured domains with no canonical solution path, a "partial solution" may mislead learners about the nature of the task

#### Implementation Variability
- **Forward fading**: start with a full worked example, then completion problems with decreasing support, then full problems — the classic sequence [Renkl & Atkinson, 2003]
- **Backward fading**: begin with completion problems where only the final step is missing, then fade earlier steps in; some evidence suggests fading later steps first benefits learners with weaker prior knowledge [~M]
- **Alternation**: interleave worked examples and isomorphic problems one-to-one rather than using completion problems as the intermediate form
- **Error-based variants**: the given portion contains a deliberate error the learner must find and fix [Erroneous examples can build conceptual knowledge by prompting learners to explain and correct flawed solutions.](../claims/erroneous-examples-build-conceptual-knowledge.md) [+W]

### Target Learners
- Novices in a structured domain (algebra, programming, physics, statistics) who would otherwise flounder in unguided search [Example–problem sequences reduce cognitive load for novices.](../claims/example-problem-sequences-reduce-cognitive-load.md) [+S]
- Intermediate learners transitioning from example study to independent problem solving
- Not recommended as the default for experts, who benefit more from problem solving with minimal support [Guidance becomes less effective — and can reverse in benefit — as expertise grows.](../claims/expertise-reversal-effect.md) [-M]

### Target Learning Goals
- Procedural skill acquisition: executing the steps of a well-defined solution method
- Schema construction: internalizing the structure of a problem type so full solutions are no longer needed
- Self-explanation and monitoring: noticing what the given steps accomplish and why the remaining steps follow

### Instructions
1. Select or author a fully worked solution to a representative task, with each step justified ([Worked Examples](../principles/worked-examples.md)).
2. Delete the final step(s) and ask learners to complete them, providing the solution for self-checking.
3. Sequence subsequent tasks so the learner-supplied portion grows — fade support progressively rather than jumping from full examples to unsolved problems [Fading support promotes transfer of responsibility.](../claims/fading-support-promotes-transfer-of-responsibility.md) [+M].
4. Prompt learners to self-explain the given steps, not just continue them [Self-explanation prompts improve learning from worked examples.](../claims/self-explanation-prompts-improve-learning-from-worked-examples.md) [+M].
5. Monitor performance and adjust the fading schedule; move to independent problems once completion is consistently accurate.

## Related Strategies
- [Worked Examples](worked-examples.md) — the fully-solved endpoint of the fading continuum; completion problems are the bridge out of them
- [Problem-Based Learning](problem-based-learning.md) — the contrast case: minimal guidance, appropriate only after schemas are established
- [Scaffolded Practice](scaffolded-practice.md) — completion problems are a form of scaffolded practice with the scaffold defined by solution completeness

## Examples
- **van Merriënboer's programming curriculum (LOGO and Pascal studies)** — learners completed partially written programs rather than writing programs from scratch, producing better learning with less invested effort than generation from scratch.
- **Khan Academy (https://www.khanacademy.org)** — its exercise hint system progressively reveals solution steps; a learner who takes the first hint is effectively working a completion problem.
- **Codecademy (https://www.codecademy.com)** — early exercises provide scaffolded code with TODO gaps the learner fills, fading toward free-form projects.
- **Math Academy (https://www.mathacademy.com)** — diagnostic-prescribed problem sequences that move from heavily supported items to independent problems as mastery evidence accumulates.

## Key Sources
- van Merriënboer, J. J. G. (1990). Strategies for programming instruction in high school: Program completion vs. program generation. *Journal of Educational Computing Research, 6*(3), 265–285.
- Paas, F., & van Merriënboer, J. J. G. (1994). Variability of worked examples and transfer of geometrical problem-solving skills: A cognitive-load approach. *Journal of Educational Psychology, 86*(1), 122–133. [doi:10.1037/0022-0663.86.1.122](https://doi.org/10.1037/0022-0663.86.1.122)
- Renkl, A., & Atkinson, R. K. (2003). Structuring the transition from example study to problem solving in cognitive skill acquisition: A cognitive load perspective. *Educational Psychologist, 38*(1), 15-22. [doi:10.1207/s15326985ep3801_3](https://doi.org/10.1207/s15326985ep3801_3)
- Sweller, J., van Merriënboer, J. J. G., & Paas, F. (2019). Cognitive architecture and instructional design: 20 years later. *Educational Psychology Review, 31*(2), 261–292. [doi:10.1007/s10648-019-09465-5](https://doi.org/10.1007/s10648-019-09465-5)
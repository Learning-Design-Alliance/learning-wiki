---
type: strategy
id: completion-problems-first
aliases: [completion-problems]
title: Completion Problems First
description: Learners begin with partially completed problems (completion problems) before moving to full problem solving, bridging worked examples and independent practice.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Completion Problems First

> **Strategy** · [All strategies](index.md)
> **Evidence** · 8 claims (4 for, 1 mixed, 2 against, 1 unmarked) · 12 studies (6 causal, 2 quant-synthesis, 2 review, 2 theoretical), `q1`–`q4` · 1 of 12 report an effect size · 2 claims rest on one study

## Description
Completion problems first is a sequencing strategy in which learners' earliest practice tasks are partially completed — some steps or solution states are given, and learners fill in the remainder. It operationalizes the *completion strategy* (van Merriënboer) as a bridge between studying full [worked examples](../principles/worked-examples.md) and solving problems unaided, implementing a smooth [fading](../elements/fading.md) of guidance rather than an abrupt transition.

## Design Implications

Completion problems reduce the unguided search that makes early problem solving inefficient for novices, while requiring more generative processing than passive example study [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+M]. Because learners must actively complete steps, the strategy avoids the shallow encoding and illusion of understanding that full-example study alone can produce [Example-based sequences outperform problem-only practice for novices, and fading support is argued to aid transfer](../claims/worked-examples-with-practice-improve-transfer.md) [+S]. The design task is choosing *which* steps to omit: omit steps that isolate the goal-rule or decision being taught, and fade progressively as performance improves.

### Context
#### Requirements
- A set of high-quality worked examples establishing the full solution procedure first
- A task sequence that fades support: full example → completion problem (most steps given) → completion problem (few steps given) → full problem ([Fading](../elements/fading.md))
- Deliberate selection of which steps to blank — typically the steps carrying the learning goal, not arbitrary gaps
- Feedback or a correct model answer so learners can check their completions
- A set of high-quality worked solutions to draw the completed portion from
- A task sequence in which the completed portion shrinks (and learner-supplied portion grows) as competence develops ([Fading](../claims/fading-support-promotes-transfer-of-responsibility.md))
- Clear marking of which steps are given and which the learner must supply, so learners do not waste effort parsing the interface rather than the content
- Feedback or a correct final solution available for self-checking after completion

#### Constraints
- If too many steps are omitted too early, learners revert to inefficient search strategies and cognitive overload [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) [-M]
- Blank steps that are trivial (e.g., routine arithmetic) add workload without promoting schema construction [~M]
- For learners with substantial prior knowledge, completion scaffolds become redundant and slow performance [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M]
- Without a model answer to compare against, learners may consolidate incorrect completions [-M]
- For learners with high prior knowledge, the provided portion is redundant and adds extraneous load rather than reducing it [Guidance becomes less effective — and can reverse in benefit — as expertise grows.](../claims/expertise-reversal-effect.md) [-M]
- Poorly aligned given/learner portions (e.g., giving the conceptually hard steps and asking for mechanical ones) undermine the intended scaffolding
- In ill-structured domains with no canonical solution path, a "partial solution" may mislead learners about the nature of the task

#### Implementation Variability
- **Backward fading:** remove the last steps first (learners finish solutions), then earlier steps — common in mathematics tutoring
- **Forward fading:** remove early steps first, forcing learners to plan before executing
- **Completion within worked-example pairs:** alternate example study with an isomorphic completion problem (example–problem pairs)
- **Programmatic fading:** in adaptive systems such as [ASSISTments](https://www.assistments.org) or [Squirrel AI](https://www.squirrelai.com), the number of given steps adjusts to learner performance
- **Forward fading**: start with a full worked example, then completion problems with decreasing support, then full problems — the classic sequence [Renkl & Atkinson, 2003]
- **Backward fading**: begin with completion problems where only the final step is missing, then fade earlier steps in; some evidence suggests fading later steps first benefits learners with weaker prior knowledge [~M]
- **Alternation**: interleave worked examples and isomorphic problems one-to-one rather than using completion problems as the intermediate form
- **Error-based variants**: the given portion contains a deliberate error the learner must find and fix [Erroneous examples can build conceptual knowledge by prompting learners to explain and correct flawed solutions.](../claims/erroneous-examples-build-conceptual-knowledge.md) [+W]

### Target Learners
- Novices who lack the schemas to benefit from unguided problem solving [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+M]
- Learners who have studied worked examples but are not yet ready for independent problems
- Less appropriate for advanced learners, who perform better solving problems directly [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M]
- Novices in a structured domain (algebra, programming, physics, statistics) who would otherwise flounder in unguided search [Example–problem sequences reduce cognitive load for novices.](../claims/example-problem-sequences-reduce-cognitive-load.md) [+S]
- Intermediate learners transitioning from example study to independent problem solving

### Target Learning Goals
- Procedural skill acquisition in well-structured domains (algebra, programming, statistics)
- Schema construction for recurring problem types
- Bridging toward transfer: faded completion supports application to novel variants [Example-based sequences outperform problem-only practice for novices, and fading support is argued to aid transfer](../claims/worked-examples-with-practice-improve-transfer.md) [+S]
- Procedural skill acquisition: executing the steps of a well-defined solution method
- Schema construction: internalizing the structure of a problem type so full solutions are no longer needed
- Self-explanation and monitoring: noticing what the given steps accomplish and why the remaining steps follow

### Instructions
1. Present a fully worked example with reasoning made visible ([Think-Aloud](../elements/think-aloud.md) or annotated steps).
2. Assign a completion problem on an isomorphic task with the goal-critical steps blanked; provide the completed example alongside for reference ([Worked Examples](../principles/worked-examples.md)).
3. Fade: progressively blank more steps across successive tasks ([Fading](../elements/fading.md)), monitoring accuracy ([Check-In](../elements/check-in.md)).
4. Transition to full problem solving once completion accuracy is high, with feedback on each attempt ([Practice](../elements/practice.md), [Assessment](../elements/assessment.md)).

## Related Strategies

- [Worked examples first](worked-examples-first.md) — the preceding phase; completion problems assume example study has occurred
- [Faded guidance](faded-guidance.md) — the general principle this strategy instantiates in problem sequences
- [Example-problem pairs](../elements/example-problem-pairs.md) — an alternating variant with similar rationale
- [Design AI educational systems that fade support and require learner justification to preserve independent problem solving](fade-ai-support-require-justification.md)
- [Problem-Based Learning](problem-based-learning.md) — the contrast case: minimal guidance, appropriate only after schemas are established
- [Scaffolded Practice](scaffolded-practice-sequences.md) — completion problems are a form of scaffolded practice with the scaffold defined by solution completeness

## Examples
- **van Merriënboer's 4C/ID task sequences** — complex-skill curricula (e.g., technical training) begin each task class with completion tasks and fade to conventional tasks ([Four-Component Instructional Design](../patterns/4cid-four-component-instructional-design.md))
- **[Khan Academy](https://www.khanacademy.org)** — hint sequences effectively function as on-demand completion problems, revealing solution steps one at a time
- **Renkl & Atkinson's fading studies** — algebra tutoring sequences that faded worked examples into completion problems and then full problems, improving near transfer
- **van Merriënboer's programming curriculum (LOGO and Pascal studies)** — learners completed partially written programs rather than writing programs from scratch, producing better learning with less invested effort than generation from scratch.
- **Khan Academy (https://www.khanacademy.org)** — its exercise hint system progressively reveals solution steps; a learner who takes the first hint is effectively working a completion problem.
- **Codecademy (https://www.codecademy.com)** — early exercises provide scaffolded code with TODO gaps the learner fills, fading toward free-form projects.
- **Math Academy (https://www.mathacademy.com)** — diagnostic-prescribed problem sequences that move from heavily supported items to independent problems as mastery evidence accumulates.

## Key Sources
- van Merriënboer, J. J. G. (1990). Strategies for programming instruction in high school: Program completion vs. program generation. *Journal of Educational Computing Research, 6*(3), 265–285. [doi:10.2190/NW2X-L8GK-M8PP-1L7N](https://doi.org/10.2190/NW2X-L8GK-M8PP-1L7N)
- Renkl, A., Atkinson, R. K., & Große, C. S. (2004). How fading worked solution steps works — a cognitive load perspective. *Instructional Science, 32*(1–2), 59–82. [doi:10.1023/b:truc.0000021815.74806.f6](https://doi.org/10.1023/b:truc.0000021815.74806.f6)
- van Merriënboer, J. J. G., & Kirschner, P. A. (2018). *Ten steps to complex learning* (3rd ed.). Routledge.
- Sweller, J., van Merriënboer, J. J. G., & Paas, F. (2019). Cognitive architecture and instructional design: 20 years later. *Educational Psychology Review, 31*(2), 261–292. [doi:10.1007/s10648-019-09465-5](https://doi.org/10.1007/s10648-019-09465-5)
- Paas, F., & van Merriënboer, J. J. G. (1994). Variability of worked examples and transfer of geometrical problem-solving skills: A cognitive-load approach. *Journal of Educational Psychology, 86*(1), 122–133. [doi:10.1037/0022-0663.86.1.122](https://doi.org/10.1037/0022-0663.86.1.122)
- Renkl, A., & Atkinson, R. K. (2003). Structuring the transition from example study to problem solving in cognitive skill acquisition: A cognitive load perspective. *Educational Psychologist, 38*(1), 15-22. [doi:10.1207/s15326985ep3801_3](https://doi.org/10.1207/s15326985ep3801_3)

<!-- merged 2026-10-13 from strategies/completion-problems ("Completion Problems"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Completion Problems

> **Strategy** · [All strategies](index.md)
> **Evidence** · 6 claims (4 for, 1 against, 1 unmarked) · 12 studies (5 causal, 2 quant-synthesis, 2 review, 2 theoretical, 1 associational), `q1`–`q4` · 1 of 12 report an effect size · 1 claim rests on one study

## Description
A completion problem (also called a completion strategy or fade-in problem) presents learners with a task that is partially solved — the initial steps are provided, and the learner must supply the remainder. It sits between a full [worked example](../principles/worked-examples.md) and an unsolved problem, operationalizing the "completion strategy" from early cognitive load research [van Merriënboer, 1990]. As expertise grows, the proportion completed by the learner increases until they solve problems independently.

## Design Implications

Completion problems reduce the unguided search that overwhelms novices while still requiring generative processing — the learner must actually execute part of the solution rather than merely study one [Example–problem sequences reduce cognitive load for novices.](../claims/example-problem-sequences-reduce-cognitive-load.md) [+S]. This makes them more effective than worked examples alone at producing transferable skill, because the completion requirement combats the passive "illusion of understanding" that pure example study can induce [Example-based sequences outperform problem-only practice for novices, and fading support is argued to aid transfer](../claims/worked-examples-with-practice-improve-transfer.md) [+S]. The design decision is the *completion ratio*: how much is given versus left to the learner, and how that ratio shifts across a task sequence.

### Context
#### Requirements
- A set of high-quality worked solutions to draw the completed portion from
- A task sequence in which the completed portion shrinks (and learner-supplied portion grows) as competence develops ([Fading](../claims/fading-support-promotes-transfer-of-responsibility.md))
- Clear marking of which steps are given and which the learner must supply, so learners do not waste effort parsing the interface rather than the content
- Feedback or a correct final solution available for self-checking after completion

#### Constraints
- For learners with high prior knowledge, the provided portion is redundant and adds extraneous load rather than reducing it [Guidance becomes less effective — and can reverse in benefit — as expertise grows.](../claims/expertise-reversal-effect.md) [-M]
- If the completed portion is too large for too long, learners engage in shallow copy-and-continue behavior instead of reasoning [Example-based sequences outperform problem-only practice for novices, and fading support is argued to aid transfer](../claims/worked-examples-with-practice-improve-transfer.md) [-M]
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
4. Prompt learners to self-explain the given steps, not just continue them [Self-explanation prompts improve learning from worked examples.](../claims/self-explanation-improves-conceptual-understanding.md) [+M].
5. Monitor performance and adjust the fading schedule; move to independent problems once completion is consistently accurate.

## Related Strategies

- [Worked Examples](worked-examples-first.md) — the fully-solved endpoint of the fading continuum; completion problems are the bridge out of them
- [Problem-Based Learning](problem-based-learning.md) — the contrast case: minimal guidance, appropriate only after schemas are established
- [Scaffolded Practice](scaffolded-practice-sequences.md) — completion problems are a form of scaffolded practice with the scaffold defined by solution completeness
- [Design AI educational systems that fade support and require learner justification to preserve independent problem solving](fade-ai-support-require-justification.md)

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
-->

---
type: strategy
title: Student-Generated Problems
description: Learners create their own problems based on concepts they are learning, share them with peers, and solve each other's problems.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Student-Generated Problems

## Description
Student-generated problems ask learners to author problems, questions, or tasks based on the concepts they are studying, rather than only solving problems supplied by the instructor. Authoring requires learners to identify the deep structure of a concept — what makes a problem solvable, what quantities or relationships matter, and what makes a distractor plausible. Problems are typically exchanged with peers, who solve them and give feedback, closing the loop between generation and application.

## Design Implications

Problem generation converts learners from consumers to constructors of tasks, forcing them to process material at the level of structure rather than surface features. Generating questions or problems improves comprehension and retention relative to answering only instructor-supplied items [Students generating their own questions outperform those answering supplied questions.](../claims/activation-improves-learning.md) [+M], and explaining or teaching content to peers produces durable learning gains for the explainer [Learning by teaching improves tutor learning.](../claims/learning-by-teaching-improves-tutor-learning.md) [+S]. The quality of generated problems depends on scaffolding: unguided generation often yields superficial recall questions, while training in question types or problem schemas produces deeper items [Guided question generation is more effective than unguided generation.](../claims/activation-improves-learning.md) [+M].

### Context
#### Requirements
- Learners with enough baseline knowledge of the concept to recognize its essential features
- Explicit criteria or exemplars for what makes a good problem (solvable, well-posed, targets the intended concept)
- A mechanism for exchange and feedback — peer solving, gallery walk, or shared problem bank
- Instructor review or curation for high-stakes uses, since flawed problems can propagate misconceptions

#### Constraints
- Unguided generation tends to produce low-level recall items rather than problems targeting deep structure [Guided question generation is more effective than unguided generation.](../claims/activation-improves-learning.md) [-M]
- Novices may generate ill-posed or unsolvable problems, wasting time and embedding confusion; instructor vetting or structured templates mitigate this
- Generation is effortful and slower than solving; when coverage pressure is high, time spent authoring competes with practice on existing problems
- Learners with very low prior knowledge lack the schema needed to construct meaningful problems and benefit more from studying [Worked Examples](../principles/worked-examples.md) first [Example-problem sequences reduce cognitive load for novices.](../claims/example-problem-sequences-reduce-cognitive-load.md) [~M]

#### Implementation Variability
- **Question generation**: learners write discussion or comprehension questions about a text (e.g., [Reciprocal Teaching](../patterns/cognitive-apprenticeship.md) question-asking role)
- **Problem authoring**: learners write mathematics or physics problems matching a target structure, often with constraints ("must involve a quadratic; must include one distractor")
- **Peer exchange and solving**: generated problems circulate; solvers flag ambiguity or errors, giving authors feedback on their own understanding
- **Problem banks**: generated problems accumulate into a class resource for review or exam preparation
- **Erroneous problem design**: learners deliberately build problems with common misconception traps, then explain why the trap works [Erroneous examples build conceptual knowledge.](../claims/erroneous-examples-build-conceptual-knowledge.md) [+M]

### Target Learners
- Intermediate learners who have enough schema to recognize problem structure but are still consolidating it [Guided question generation is more effective than unguided generation.](../claims/activation-improves-learning.md) [+M]
- Learners prone to illusion of knowing — authoring a solvable problem is a strong self-check on understanding
- Less suitable for complete novices, who should first study worked examples before generating [Example-problem sequences reduce cognitive load for novices.](../claims/example-problem-sequences-reduce-cognitive-load.md) [~M]

### Target Learning Goals
- Conceptual understanding: identifying the deep structure that defines a problem type
- Discrimination: distinguishing well-posed from ill-posed problems and core features from surface features
- Metacognition and self-assessment: authoring forces learners to evaluate their own grasp of what is askable
- Transfer: generating variants of a problem type supports recognizing that structure in new contexts [Multiple contrasting cases support abstraction of deep structure.](../claims/multiple-contrasting-cases-support-abstraction.md) [+M]

### Instructions
1. Teach or review the target concept and show one or two exemplar problems, making their structure explicit ([Advance Organizers](../elements/advance-organizers.md) can frame the problem schema).
2. Provide generation criteria: the problem must be solvable, well-posed, and target the concept; optionally require a worked solution key from the author.
3. Have learners draft problems individually or in pairs, using a template or question-type menu to push beyond recall ([Analogies](../elements/analogies.md) can seed novel contexts).
4. Exchange problems for peer solving ([Practice](../elements/practice.md)); solvers give feedback on clarity and difficulty ([Check-In](../elements/check-in.md) structures help surface confusion).
5. Debrief as a class: compare generated problems, identify which target deep structure, and resolve disputes about solvability — this discussion is where much of the learning occurs.

## Related Strategies
- [Peer Instruction](peer-instruction.md) — shares the peer-exchange mechanism but centers on answering rather than authoring
- [Reciprocal Questioning](reciprocal-questioning.md) — a structured variant where learners alternate generating and answering questions in groups
- [Self-Explanation](../elements/self-explanation.md) — complementary; explaining why a generated problem works deepens the authoring benefit

## Examples
- **Reciprocal Teaching** ([University of Illinois reading studies](https://www.readingrockets.org/strategies/reciprocal_teaching)) — students take turns generating questions about a text passage, a direct application of guided question generation.
- **"Write your own exam question" assignments** — common in university STEM courses; students submit problems with solutions, the instructor curates the best into a review bank before exams.
- **[Desmos Activity Builder](https://teacher.desmos.com)** — teachers and students can author custom graphing challenges; some classrooms have students design "marble slides" challenges for peers to solve.
- **Khan Academy "create a problem" prompts** in some math classrooms — after mastering a problem type, students write and swap original word problems matching the same structure.

## Key Sources
- Rosenshine, B., Meister, C., & Chapman, S. (1996). Teaching students to generate questions: A review of the intervention studies. *Review of Educational Research, 66*(2), 181–221. [doi:10.3102/00346543066002181](https://doi.org/10.3102/00346543066002181)
- King, A. (1990). Enhancing peer interaction and learning in the classroom through reciprocal questioning. *American Educational Research Journal, 27*(4), 663–687. [doi:10.3102/00028312027004663](https://doi.org/10.3102/00028312027004663)
- Foos, P. W., Mora, J. J., & Tkacs, S. (1994). Student study techniques and the generation effect. *Journal of Educational Psychology, 86*(4), 567–576. [doi:10.1037/0022-0663.86.4.567](https://doi.org/10.1037/0022-0663.86.4.567)
- Palincsar, A. S., & Brown, A. L. (1984). Reciprocal teaching of comprehension-fostering and comprehension-monitoring activities. *Cognition and Instruction, 1*(2), 117–175. [doi:10.1207/s1532690xci0102_1](https://doi.org/10.1207/s1532690xci0102_1)
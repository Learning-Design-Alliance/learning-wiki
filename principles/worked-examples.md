---
type: principle
id: worked-examples
title: Worked Examples
description: Worked examples present a partially or fully solved problem so learners can study task structure, decision points, and reasoning before attempting similar problems independently.
status: review
generated:
  by: claude/unspecified
  at: 2026-04-06
sources:
  - id: sweller-2010
    resource: "https://doi.org/10.1007/s10648-010-9128-5"
    title: "Sweller, J. (2010). Element interactivity and intrinsic, extraneous, and germane cognitive load. *Educational Psychology Review, 22*(2), 123–138"
    author: Sweller, J
  - id: tuovinen-1999
    resource: "https://doi.org/10.1037/0022-0663.91.2.334"
    title: "Tuovinen, J. E., & Sweller, J. (1999). A comparison of cognitive load associated with discovery learning and worked examples. *Journal of Educational Psychology, 91*(2), 334–341"
    author: "Tuovinen, J. E., & Sweller, J"
  - id: van-gog-2010
    resource: "https://doi.org/10.1007/s10648-010-9134-7"
    title: "van Gog, T., & Rummel, N. (2010). Example-based learning: Integrating cognitive and social-cognitive research perspectives. *Educational Psychology Review, 22*(2), 155–174"
    author: "van Gog, T., & Rummel, N"
  - id: van-gog-2011
    resource: "https://doi.org/10.1016/j.cedpsych.2010.10.004"
    title: "van Gog, T., Kester, L., & Paas, F. (2011). Effects of worked examples, example–problem, and problem–example pairs on novices' learning. *Contemporary Educational Psychology, 36*(3), 212–218"
    author: "van Gog, T., Kester, L., & Paas, F"
  - id: barbieri-2016
    resource: "https://doi.org/10.1016/j.lindif.2016.04.001"
    title: "Barbieri, C., & Booth, J. L. (2016). Support for struggling students in algebra: Contributions of incorrect worked examples. *Learning and Individual Differences, 48*, 36–44"
    author: "Barbieri, C., & Booth, J. L"
  - id: heffernan-2014
    resource: "https://doi.org/10.1007/s40593-014-0024-x"
    title: "Heffernan, N. T., & Heffernan, C. L. (2014). The ASSISTments ecosystem: Building a platform that brings scientists and teachers together for minimally invasive research on human learning and teaching. *International Journal of Artificial Intelligence in Education, 24*(4), 470–497"
    author: "Heffernan, N. T., & Heffernan, C. L"
---

# Worked Examples

> **Principle** · [All principles](index.md)
> **Evidence** · 8 claims (4 for, 2 mixed, 2 unmarked) · 8 studies (5 causal, 1 quant-synthesis, 1 review, 1 theoretical), `q2`–`q4` · 2 of 8 report an effect size · 4 claims rest on one study

## Description
Worked examples present a partially or fully solved problem so learners can study task structure, decision points, and reasoning before attempting similar problems independently.

## Implications

Worked examples can help learners who are new to a task or domain. By externalizing problem structure, they may reduce unproductive search during initial acquisition [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+M]. A meta-analysis reports benefits for mathematics performance [Worked examples improve mathematics performance, especially for novices.](../claims/worked-examples-improve-math-performance.md) [+S]. Subsequent practice, fading, and explanation are design options for moving toward independent performance, but their relative contribution depends on the comparison and outcome: one four-arm experiment found no detected immediate-test difference between examples only and example–problem pairs [Sequencing worked examples with practice problems improves learning for novices](../claims/worked-example-problem-sequences.md) [~M]. As expertise grows, guidance may become redundant [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M]. These relationships do not establish a universal schedule for fading or a delayed transfer effect.

### Conditional Model

**Proposed activity-to-learning relationship.** For a learner without a usable solution schema facing a structured task, studying a solution *before* attempting a similar problem may reduce search-heavy effort and improve subsequent performance. This is a theoretical explanation; lower effort and higher test performance are observations in particular studies, while schema formation is an inferred process. The [worked-examples pattern](../patterns/worked-examples.md) turns this conditional relationship into a sequence of design choices.

| Condition that may change the choice | Observation recorded in this wiki | Design implication and uncertainty |
|---|---|---|
| Novices; structured circuit troubleshooting; immediate test | Example-only and example→problem groups outperformed problem-only and problem→example groups. Example-only and example→problem were not detectably different on that test [~M]. [Sequencing worked examples with practice problems improves learning for novices](../claims/worked-example-problem-sequences.md) | Put the example first for a similar initial task. This does not establish that alternating pairs outperform examples only or that the benefit lasts or transfers far. |
| Prior knowledge, example type, **and task difficulty** considered together in college algebra | A three-way interaction appeared on the immediate posttest; the simpler prior-knowledge × example-type posttest interaction was not significant [~M]. [Three-way interaction claim](../claims/prior-knowledge-worked-example-task-difficulty-three-way-interaction-on-algebra-posttest.md) | Assess the actual task demand before choosing full versus completion examples. A high-prior-knowledge learner alone is insufficient to prescribe completion examples. |
| Goal is conceptual understanding or transfer from a novel concept | In a synthesis, problem solving before instruction beat instruction before problem solving on these outcomes; the procedural result was not detectably different [~S]. [Productive failure improves conceptual learning](../claims/productive-failure-improves-conceptual-learning.md) | Consider a problem-first sequence with consolidation as a competing design model. This is **not** a direct comparison with the specific example-first circuit lesson. |

**Discriminating observations.** Record prior knowledge *for the target task*, task demand, exact order and amount of help, the learner's attempts, immediate procedural performance, later conceptual/transfer performance, and mental effort where measured. If the task or intended outcome is missing, preserve that absence and qualify the recommendation. Reduced search, productive struggle, and schema acquisition are rival or complementary mechanism hypotheses; an outcome alone cannot identify which occurred.

### Context
#### Requirements
- A solved demonstration ([Demonstration](../elements/demonstration.md) or [Procedural Information](../elements/procedural-information.md)) when this example-first approach is selected
- Prompts that surface reasoning ([Eliciting Student Thinking](../elements/eliciting-student-thinking.md) or [Articulation](../elements/articulation.md)) — passive reading of examples produces weaker learning than active explanation
- A way to check and eventually support independent application ([Practice](../elements/practice.md)); the amount and timing of practice remain design decisions

#### Constraints
- Less effective when the main goal is open-ended generation or creative exploration
- Can create illusions of understanding if used without prompts or practice
- Benefits drop when examples are not aligned with later transfer tasks
- Effectiveness diminishes as learner expertise grows; continued use with advanced learners may become counterproductive

### Target Learners
- Novice learners encountering a domain or representation for the first time
- Learners at risk of cognitive overload during unguided problem solving
- Learners acquiring procedural skills that have clear correct steps
- Effects diminish as expertise increases [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M] — reduce or fade examples as competence develops

### Target Learning Objectives
- Early schema formation: building a mental model of task structure
- Procedural fluency with explanation, not just rote execution
- Recognizing structural similarity across problem types
- Transitioning from guided to independent performance

### Theory
#### Supporting
- [Cognitive Load Theory](../theories/cognitive-load-theory.md) (Sweller) — worked examples reduce extraneous cognitive load by making problem structure explicit, freeing working memory for schema formation
- [Information Processing Theory](../theories/information-processing-theory.md) — examples externalize solution steps, reducing the working-memory demand of holding intermediate states in mind
- [Self-Regulated Learning](../theories/self-regulated-learning.md) — prompts and example fading support monitoring and adaptive control of learning

#### Contradicting / Qualifying
- [Constructivism](../theories/constructivism.md) — emphasizes that learners build understanding through active generation and exploration; over-reliance on worked examples may reduce generative processing and limit transfer to novel problems

### Claims
- [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+M] — worked examples reduce unnecessary search for novices
- [Example-based sequences outperform problem-only practice for novices, and fading support is argued to aid transfer](../claims/worked-examples-with-practice-improve-transfer.md) [+M] — example-based sequences outperform problem-only practice in the recorded novice comparison; the fading argument is from a separate synthesis
- [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M] — guidance becomes redundant as expertise grows (expertise reversal)
- [Example–problem sequences reduce cognitive load and improve learning outcomes](../claims/worked-examples-example-problem-sequences.md) [+S] — example–problem sequences reduce cognitive load and improve outcomes vs. problem-only practice
- [Worked examples improve mathematics performance, especially for novices.](../claims/worked-examples-improve-math-performance.md) [+S] — worked examples improve math performance across grades (meta-analysis)
- [Prior knowledge, worked-example type, and task difficulty interact on an algebra posttest](../claims/prior-knowledge-worked-example-task-difficulty-three-way-interaction-on-algebra-posttest.md) [~M] — a three-way condition that limits simple matching rules
- [Productive failure improves conceptual learning](../claims/productive-failure-improves-conceptual-learning.md) [~S] — a competing sequence for some conceptual and transfer goals

## Related Principles
- [Purposeful Reflection](purposeful-reflection.md) — worked examples gain power when paired with structured prompts to reflect on why each step was taken
- [Guided Practice](guided-practice.md) — provides the scaffolded practice phase that converts example study into transferable performance
- [Explaining Their Thinking](explaining-their-thinking.md) — self-explanation of worked examples is one of the strongest amplifiers of example-based learning
- [Pairing Non-Examples With Examples](pairing-non-examples-with-examples.md) — extends worked examples by contrasting correct solutions with common errors, sharpening discrimination

## Examples

### Validated
- [Sequencing worked examples with practice problems improves learning for novices](../claims/worked-example-problem-sequences.md) [~M] — van Gog, Kester & Paas (2011) randomized 103 secondary students in circuit troubleshooting; 96 were analyzed. Example-only and example→problem conditions outperformed problem-only and problem→example on the immediate test, while example-only and example→problem did not differ detectably. This experiment does not establish a delayed or far-transfer effect.

### Illustrative

**[Worked Example Routine](../strategies/worked_example_routine.md)** — A classroom instructional routine in which the teacher presents a fully solved problem, thinks aloud through each step using [explicit modeling](../elements/demonstration.md), then immediately asks learners to solve a near-transfer problem. The routine builds in [self-explanation prompts](../elements/eliciting-student-thinking.md) before the independent attempt.

**[Comparing Multiple Solution Methods](../strategies/comparing_multiple_solution_methods.md)** — Learners study two or more [worked examples](../elements/demonstration.md) of the same problem solved differently, then compare and explain which method is more efficient or generalizable. Particularly effective for building flexible procedural knowledge in mathematics.

**[ASSISTments](https://www.assistments.org)** — A free web-based math platform (grades 6–12) that delivers [practice problems](../elements/practice.md) with on-demand [worked example hints](../elements/demonstration.md) that walk through solution steps. Learners can request a hint at any step, receiving targeted procedural guidance rather than the full solution. Heffernan & Heffernan (2014) report learning gains relative to homework-only conditions across several randomized school studies.

**[Carnegie Learning MATHia](https://www.carnegielearning.com/solutions/math/mathia/)** — An adaptive intelligent tutoring system for middle and high school math that combines [worked examples](../elements/demonstration.md), [mastery-based problem sets](../elements/practice.md), and [step-level hints](../elements/eliciting-student-thinking.md) that prompt learners to explain their reasoning before providing guidance. Mastery gating ensures learners do not advance until they demonstrate independent performance.

**Code walkthroughs with commentary** — A common pattern in programming instruction: an instructor or tutorial presents annotated [worked code](../elements/demonstration.md) explaining *why* each line exists, then immediately assigns a [coding exercise](../elements/practice.md) that requires adapting or extending the example. Widely used in MOOCs (e.g., Codecademy, CS50) and textbooks.

**Annotated reading comprehension walkthroughs** — A teacher reads a complex text aloud, using [think-aloud](../elements/demonstration.md) to make comprehension strategies visible (identifying main idea, inferencing, monitoring confusion), then asks learners to apply the same strategies to a new passage with [structured annotation prompts](../elements/eliciting-student-thinking.md).

## Key Sources
- Sweller, J. (2010). Element interactivity and intrinsic, extraneous, and germane cognitive load. *Educational Psychology Review, 22*(2), 123–138. [doi:10.1007/s10648-010-9128-5](https://doi.org/10.1007/s10648-010-9128-5)
- Tuovinen, J. E., & Sweller, J. (1999). A comparison of cognitive load associated with discovery learning and worked examples. *Journal of Educational Psychology, 91*(2), 334–341. [doi:10.1037/0022-0663.91.2.334](https://doi.org/10.1037/0022-0663.91.2.334)
- van Gog, T., & Rummel, N. (2010). Example-based learning: Integrating cognitive and social-cognitive research perspectives. *Educational Psychology Review, 22*(2), 155–174. [doi:10.1007/s10648-010-9134-7](https://doi.org/10.1007/s10648-010-9134-7)
- van Gog, T., Kester, L., & Paas, F. (2011). Effects of worked examples, example–problem, and problem–example pairs on novices' learning. *Contemporary Educational Psychology, 36*(3), 212–218. [doi:10.1016/j.cedpsych.2010.10.004](https://doi.org/10.1016/j.cedpsych.2010.10.004)
- Barbieri, C., & Booth, J. L. (2016). Support for struggling students in algebra: Contributions of incorrect worked examples. *Learning and Individual Differences, 48*, 36–44. [doi:10.1016/j.lindif.2016.04.001](https://doi.org/10.1016/j.lindif.2016.04.001)
- Heffernan, N. T., & Heffernan, C. L. (2014). The ASSISTments ecosystem: Building a platform that brings scientists and teachers together for minimally invasive research on human learning and teaching. *International Journal of Artificial Intelligence in Education, 24*(4), 470–497. [doi:10.1007/s40593-014-0024-x](https://doi.org/10.1007/s40593-014-0024-x)

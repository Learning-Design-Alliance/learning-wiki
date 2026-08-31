---
type: strategy
title: Self Explanation Prompts
description: Prompts that ask learners to explain to themselves why a step, statement, or solution is correct, integrating new material with prior knowledge.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Self Explanation Prompts

> **Strategy** · [All strategies](index.md)

## Description
Self explanation prompts ask learners to generate explanations *to themselves* — why a step in a worked solution was taken, why a statement is true, or how new material relates to what they already know. The prompt supplies the question; the learner supplies the reasoning. This differs from receiving an explanation (which is instructor-generated) and from [Think-Aloud](../elements/think-aloud.md) (which verbalizes ongoing processing rather than justifying specific content).

## Design Implications

Self explanation forces the learner to actively integrate new information with prior knowledge, exposing gaps and repairing flawed mental models during study rather than at assessment. A meta-analysis of 64 studies found self explanation prompts produce moderate learning gains across domains and ages [Bisra et al. (2010)](https://doi.org/10.1007/s10648-010-9129-4) [+M]. The quality of the explanation matters more than its mere production: prompts that direct attention to *why* and *how* yield deeper learning than prompts that merely restate content.

### Context
#### Requirements
- Content with explainable structure — worked solutions, proofs, diagrams, causal claims, or procedures with justifiable steps
- Prompts tied to specific content ("Why is this step valid here?") rather than generic ("Explain what you learned")
- Enough working memory headroom that explaining does not crowd out comprehension of the material itself
- A way for learners to check their explanations against expert reasoning ([Worked Examples](../elements/worked-examples.md) with step annotations, or instructor feedback)

#### Constraints
- Explaining familiar or trivial content wastes time and adds load without benefit [~M] — prompts must target genuinely non-obvious steps
- Learners with low prior knowledge may generate inaccurate explanations and encode the errors; explanations should be verifiable against authoritative content [-M]
- Prompting explanation of *already well-understood* material can disrupt fluent processing (the "over-explanation" cost seen with high-knowledge learners) [~M]
- Poorly timed prompts during reading can interrupt comprehension flow; place them after meaningful segments, not mid-sentence [~W]

#### Implementation Variability
- **Prompted during study** — embedded questions after each worked-example step (the classic Chi paradigm)
- **Learner-initiated** — training learners to spontaneously ask "why" while studying; slower to establish but more durable
- **Structured formats** — sentence starters, selection from menu of reasons, or [Concept Mapping](../elements/concept-mapping.md) as explanation scaffolds for younger or lower-prior-knowledge learners
- **Interactive** — pairs take turns explaining and questioning each other, blending self explanation with [Collaborative Learning](../principles/collaborative-learning.md)

### Target Learners
- Novices and intermediate learners; effects shrink or reverse for high-prior-knowledge learners for whom explanation is redundant [~M]
- Learners prone to illusions of understanding from fluent reading — explaining exposes what they cannot actually justify [+M]
- Young learners need more scaffolded prompt formats (menu-based or sentence-starter prompts) [~W]

### Target Learning Goals
- Conceptual understanding: why procedures work, not just how to execute them
- Schema construction: connecting new material to prior knowledge
- Metacognitive monitoring: discovering gaps and misconceptions during study
- Transfer: principle-based explanations support applying methods to novel problems [+M]

### Instructions
1. Select content with explainable reasoning steps — a worked solution, demonstration, or [Case Study](../elements/case-studies.md).
2. Write a prompt for each non-obvious step, focused on justification ("Why does this step follow?") rather than description.
3. Present the content, then the prompt, giving adequate time before revealing any expert explanation.
4. Let learners compare their explanation to an expert explanation or annotated solution, and revise.
5. Fade the prompts as expertise develops, shifting toward learner-initiated explanation ([Fading](../elements/fading.md)).

## Related Strategies
- [Worked Examples](../strategies/use_worked_examples.md) — the most common carrier; step-by-step self explanation prompts turn passive example study into active processing
- [Think-Aloud Modeling](../strategies/think-aloud-modeling.md) — instructor version of the same move; models the explaining learners are later prompted to do
- [Elaborative Interrogation](../strategies/elaborative-interrogation.md) — the "why is this true?" variant applied to factual text rather than procedures

## Examples
- **Chi et al.'s classic paradigm** — Studying physics worked examples with each step annotated, prompted "What is this line telling you? Explain why it was done."
- **Khan Academy** (https://www.khanacademy.org) — hint sequences progressively reveal solution steps, each functioning as a check on the learner's own explanation of the next move.
- **Cognitive Tutor / Carnegie Learning** (https://www.carnegielearning.com) — adaptive math tutors require justification selections ("Why did you choose this operation?") at each problem-solving step.

## Key Sources
- Chi, M. T. H., Bassok, M., Lewis, M. W., Reimann, P., & Glaser, R. (1989). Self-explanations: How students study and use examples in learning to solve problems. *Cognitive Science, 13*(2), 145–182. [doi:10.1207/s15516709cog1302_1](https://doi.org/10.1207/s15516709cog1302_1)
- Bisra, K., Liu, Q., Nesbit, J. C., Salimi, F., & Winne, P. H. (2010). Inducing self-explanation: A meta-analysis. *Educational Psychology Review, 22*(3), 273–308. [doi:10.1007/s10648-018-9434-x](https://doi.org/10.1007/s10648-018-9434-x)
- Atkinson, R. K., Renkl, A., & Merrill, M. M. (2003). Transitioning from studying examples to solving problems: Effects of self-explanation prompts and fading worked-out steps. *Journal of Educational Psychology, 95*(4), 774–783. [doi:10.1037/0022-0663.95.4.774](https://doi.org/10.1037/0022-0663.95.4.774)
- Fonseca, B. A., & Chi, M. T. H. (2011). Instruction based on self-explanation. In R. E. Mayer & P. A. Alexander (Eds.), *Handbook of Research on Learning and Instruction* (pp. 296–321). Routledge.
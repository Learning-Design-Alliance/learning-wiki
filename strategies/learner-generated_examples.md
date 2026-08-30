---
type: strategy
title: Learner-Generated Examples
description: Provide opportunities for learners to generate their own examples of a concept.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Learner-Generated Examples

## Description
Learner-generated examples ask students to produce their own instances of a concept, principle, or procedure — a novel illustration, a personal anecdote, a worked case — rather than only recognizing or studying examples supplied by the instructor. Generating an example requires retrieving the concept's defining features and mapping them onto new content, which promotes reflection, reinforces well-formed concepts, and exposes fuzzy boundaries or misconceptions that passive study leaves hidden.

## Design Implications

Generation is a form of retrieval and elaboration: producing an example forces learners to reconstruct the concept from memory and apply it, which produces more durable learning than rereading or recognizing instructor-provided instances [Self-explanation improves conceptual understanding.](../claims/self-explanation-improves-conceptual-understanding.md) [+S]. The quality of the generated example is diagnostic — a weak or wrong example reveals an incomplete concept and creates a natural opening for feedback and discussion. Because generation adds working-memory demands, it works best after learners have at least a minimal grasp of the concept; asking novices to generate examples before any instruction can overload them [Example-problem sequences reduce cognitive load.](../claims/example-problem-sequences-reduce-cognitive-load.md) [~M].

### Context
#### Requirements
- An interactive environment where learners can share, compare, and discuss examples ([Class Discussion](../elements/class-discussion.md), [Collaboration](../elements/collaboration.md))
- Sufficient initial instruction that learners possess the concept well enough to instantiate it
- Instructor or peer review to verify accuracy and relevance ([Practice](../elements/practice.md) with feedback)
- Clear criteria for what makes an example valid (which features must be present, which are incidental)

#### Constraints
- Learners with very low prior knowledge generate shallow or incorrect examples and may entrench misconceptions if errors go uncorrected [-M]
- Generated examples that are idiosyncratic or surface-similar can anchor learners to irrelevant features; contrasting multiple examples mitigates this [Multiple contrasting cases support abstraction.](../claims/multiple-contrasting-cases-support-abstraction.md) [~M]
- Requires facilitation effort: unvetted examples shared in class can spread confusion rather than correct it
- Time-intensive relative to presenting examples; poorly suited when coverage pressure is high

#### Implementation Variability
- **Individual generation** followed by instructor review — low-cost, works in large classes
- **Peer exchange and critique** — learners evaluate each other's examples, doubling as discrimination practice
- **Comparing generated to expert examples** — learners generate first, then compare against canonical cases to spot gaps
- **Erroneous-example analysis** — inverting the task by having learners diagnose flawed examples [Erroneous examples build conceptual knowledge.](../claims/erroneous-examples-build-conceptual-knowledge.md) [+W]
- **Personalized generation** — learners draw examples from their own interests, work, or culture, increasing relevance and task value

### Target Learners
- Learners with moderate prior knowledge who can retrieve the concept but need to consolidate and refine it [Self-explanation improves conceptual understanding.](../claims/self-explanation-improves-conceptual-understanding.md) [+S]
- Learners prone to illusions of understanding from fluent reading of provided examples — generation exposes what they cannot yet do
- Less suitable for complete novices, who lack the knowledge base to produce valid instances [Example-problem sequences reduce cognitive load.](../claims/example-problem-sequences-reduce-cognitive-load.md) [~M]

### Target Learning Goals
- Concept formation and refinement: sharpening defining features and boundary cases
- Transfer: connecting abstract principles to concrete, personally meaningful situations
- Misconception diagnosis: surfacing fuzzy or incorrect understanding for correction
- Deeper understanding beyond recognition-level mastery

### Instructions
1. Teach the concept first with instructor-provided examples and clear defining criteria.
2. Ask learners to generate one or more of their own examples ([Practice](../elements/practice.md)), ideally drawn from their own experience or interests.
3. Have learners explain *why* each example fits, articulating the mapping between concept features and the example [Self-explanation improves conceptual understanding.](../claims/self-explanation-improves-conceptual-understanding.md) [+S].
4. Share and compare examples across learners ([Class Discussion](../elements/class-discussion.md)); contrast valid and invalid cases to support abstraction [Multiple contrasting cases support abstraction.](../claims/multiple-contrasting-cases-support-abstraction.md) [+M].
5. Provide corrective feedback on inaccurate examples before misconceptions consolidate.

## Related Strategies
- [Self-Explanation](../elements/self-explanation.md) — the underlying mechanism: articulating why an example fits is a self-explanation act
- [Comparing Cases](../elements/comparing-cases.md) — generated examples gain power when contrasted with each other and with expert cases
- [Retrieval Practice](retrieval-practice.md) — generation is a retrieval event; both strengthen memory through effortful reconstruction

## Examples
- In a statistics course, students generate their own real-world scenarios illustrating Type I vs. Type II errors, then critique each other's scenarios in small groups.
- In a sexual harassment training course, learners generate their own examples to clarify the boundaries of acceptable behavior — a domain where concepts are not neatly defined and boundary cases matter most.
- In introductory programming, students write their own analogies or mini-scenarios for recursion, then compare them against canonical examples to test where the analogy breaks down.

## Key Sources
- Chi, M. T. H., de Leeuw, N., Chiu, M.-H., & LaVancher, C. (1994). Eliciting self-explanations improves understanding. *Cognitive Science, 18*(3), 439–477. [doi:10.1207/s15516709cog1803_3](https://doi.org/10.1207/s15516709cog1803_3)
- Slamecka, N. J., & Graf, P. (1978). The generation effect: Delineation of a phenomenon. *Journal of Experimental Psychology: Human Learning and Memory, 4*(6), 592–604. [doi:10.1037/0278-7393.4.6.592](https://doi.org/10.1037/0278-7393.4.6.592)
- Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques. *Psychological Science in the Public Interest, 14*(1), 4–58. [doi:10.1177/1529100612453266](https://doi.org/10.1177/1529100612453266)
- Renkl, A. (2014). Toward an instructionally oriented theory of example-based learning. *Cognitive Science, 38*(1), 1–37. [doi:10.1111/cogs.12086](https://doi.org/10.1111/cogs.12086)
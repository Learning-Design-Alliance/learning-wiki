---
type: strategy
title: Concept Discovery Through Examples and Non-examples
description: Expose learners to a wide range of examples and non-examples and allow them to discover the concept through guided comparison and classification.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Concept Discovery Through Examples and Non-examples

> **Strategy** · [All strategies](index.md)

## Description
Learners are presented with a carefully sequenced set of examples and non-examples of a target concept and asked to identify shared characteristics, classify new instances, and articulate the concept's defining attributes. The instructor or system supports exploration with questions and context-sensitive feedback that corrects misconceptions as they emerge. The strategy treats concept acquisition as pattern discrimination built from varied instances rather than transmission of a definition.

## Design Implications

Concept learning depends on exposure to varied, well-chosen instances: comparing multiple cases helps learners abstract the deep structure that defines a concept rather than surface features of any single instance [Multiple varied cases support flexible transfer of concepts.](../claims/cognitive-flexibility-theory-multiple-cases.md) [+M]. Non-examples are as important as examples — they establish the boundaries of the concept and prevent overgeneralization [Erroneous examples build conceptual knowledge by making boundaries explicit.](../claims/erroneous-examples-build-conceptual-knowledge.md) [+M]. However, unguided discovery is unreliable: learners left to explore without prompts, sequencing, or feedback frequently fail to induce the intended concept, and guided forms of discovery consistently outperform pure discovery [Guided discovery outperforms pure discovery across outcome measures.](../claims/guided-discovery-outperforms-pure-discovery.md) [+S].

### Context
#### Requirements
- A rich, representative set of examples and non-examples, varying surface features while holding defining attributes constant
- Sequencing that starts with clear, matched pairs (example/non-example differing on one attribute) before moving to harder discriminations
- Interactive classification tasks with immediate, context-sensitive feedback ([Practice](../elements/practice.md), [Feedback](../elements/feedback.md))
- Prompts that direct attention to relevant attributes rather than leaving search entirely open ([Advance Organizers](../elements/advance-organizers.md))

#### Constraints
- Unguided exploration with minimal prior knowledge produces weak or erroneous inductions; novices need more scaffolding than experts [Minimal guidance is less effective for novices than explicit guidance.](../claims/minimal-guidance-less-effective-for-novices.md) [-S]
- Effectiveness reverses with expertise: highly knowledgeable learners benefit less from heavily scaffolded example sets and may profit from more open exploration [Guidance benefits decline as learner expertise increases.](../claims/expertise-reversal-effect.md) [~M]
- Poorly chosen non-examples (differing on irrelevant features) teach spurious discriminations
- Time-intensive: building a sufficient instance set and feedback logic costs more design effort than presenting a definition

#### Implementation Variability
- **Rational set design**: systematically vary variables across examples (easy/difficult, divergent/range of divergence) per Tennyson & Park's concept-teaching model
- **Matched pairs**: present an example and non-example side by side differing on exactly one defining attribute
- **Learner-generated instances**: after classification practice, learners produce their own examples and non-examples, which deepens encoding
- **Erroneous examples**: present flawed instances for diagnosis, leveraging error analysis rather than avoidance [Erroneous examples build conceptual knowledge.](../claims/erroneous-examples-build-conceptual-knowledge.md) [+M]

### Target Learners
- Learners with some relevant prior knowledge who can notice attribute patterns with prompting [Activating prior knowledge improves learning of new related concepts.](../claims/activation-improves-learning.md) [+M]
- Intermediate learners refining fuzzy or misconceived concepts (e.g., distinguishing mass from weight)
- Novices benefit most when discovery is strongly guided; pure exploration suits them poorly [Minimal guidance is less effective for novices.](../claims/minimal-guidance-less-effective-for-novices.md) [-S]

### Target Learning Goals
- Concept acquisition: learning defining attributes and category boundaries
- Discrimination and classification: accurately sorting novel instances
- Conceptual change: replacing misconceptions through confrontation with counterexamples
- Inductive reasoning: practicing abstraction from instances to rule

### Instructions
1. Activate relevant prior knowledge and surface likely misconceptions before presenting instances ([Activation](../elements/activation.md))
2. Present a matched example/non-example pair and ask learners to identify the distinguishing attribute ([Comparing Cases](../elements/comparing-cases.md))
3. Present a varied sequence of additional examples and non-examples, prompting learners to test and refine their hypothesis about the concept's definition
4. Require classification of novel instances with immediate feedback on errors ([Practice](../elements/practice.md), [Feedback](../elements/feedback.md))
5. Ask learners to state the rule and generate their own example and non-example ([Articulation](../elements/articulation.md))
6. Fade support: move from prompted comparison to independent classification as accuracy grows ([Fading](../elements/fading.md))

## Related Strategies
- [Use Worked Examples](../strategies/use_worked_examples.md) — the procedural analogue: studying solved instances rather than inducing a concept
- [Comparing Cases](../elements/comparing-cases.md) — the core comparison mechanism this strategy sequences into a concept lesson
- [Guided Inquiry](../elements/guided-inquiry.md) — broader inquiry framing in which example sets serve as the data

## Related Elements
- [Non-Examples](../elements/non-examples.md) — the boundary-defining counterpart to examples; essential for preventing overgeneralization
- [Comparing Cases](../elements/comparing-cases.md) — the comparison activity that drives attribute abstraction
- [Feedback](../elements/feedback.md) — context-sensitive correction of misclassifications
- [Advance Organizers](../elements/advance-organizers.md) — frames what learners should look for before exploration

## Patterns That Use This Strategy
- [Concept Attainment](../patterns/concept-attainment.md) — the canonical pattern: hypothesis testing against positive and negative instances
- [Cognitive Flexibility Theory](../patterns/cognitive-flexibility-theory.md) — multiple varied cases across contexts for complex concepts
- [Direct Instruction](../patterns/direct-instruction.md) — uses example/non-example sequences but with teacher-led rule statement, contrasting on the discovery dimension

## Examples
- **Concept Attainment model (Bruner, Goodnow & Austin)** — learners see labeled YES/NO instances (e.g., of "democracy") and hypothesize the defining attributes, then classify new cases.
- **Impressionism lesson** — learners view a set of Impressionist paintings alongside Academic Salon works, identify shared characteristics (visible brushwork, light effects), then classify unfamiliar paintings.
- **[Wolfram Demonstrations](https://demonstrations.wolfram.com)** — interactive parameter manipulation lets learners discover what makes a function continuous by generating examples and non-examples on demand.
- **Merrill's Pebble-in-the-Pond concept lessons** — a portrayal (specific instance) followed by a sequence of similar portrayals for classification practice.

## Key Sources
- Tennyson, R. D., & Park, O.-C. (1980). The teaching of concepts: A review of instructional design research literature. *Review of Educational Research, 50*(1), 55–70. [doi:10.3102/00346543050001055](https://doi.org/10.3102/00346543050001055)
- Alfieri, L., Brooks, P. J., Aldrich, N. J., & Tenenbaum, H. R. (2011). Does discovery-based instruction enhance learning? A meta-analysis. *Journal of Educational Psychology, 103*(1), 1–18. [doi:10.1037/a0021017](https://doi.org/10.1037/a0021017)
- Kirschner, P. A., Sweller, J., & Clark, R. E. (2006). Why minimal guidance during instruction does not work. *Educational Psychologist, 41*(2), 75–86. [doi:10.1207/s15326985ep4102_1](https://doi.org/10.1207/s15326985ep4102_1)
- Merrill, M. D. (2002). First principles of instruction. *Educational Technology Research and Development, 50*(3), 43–59. [doi:10.1007/bf02505024](https://doi.org/10.1007/bf02505024)
- Marton, F., & Booth, S. (1997). *Learning and awareness*. Lawrence Erlbaum Associates.
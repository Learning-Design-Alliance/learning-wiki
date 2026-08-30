---
type: strategy
title: Matched Examples and Non-examples
description: Present matched examples and non-examples for concepts with closely related attributes, so learners can discriminate the defining features of a concept.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Matched Examples and Non-examples

## Description
This strategy pairs an example of a target concept with a non-example — an instance that is specifically *not* an instance of the concept — that differs from the example in one critical attribute. The pairs are presented simultaneously or in close succession so both can be held in working memory at once, allowing learners to isolate the attribute that separates the concept from its near neighbors. The goal is accurate concept formation: learners learn the boundaries of a concept, not just its center.

## Design Implications

Contrasting cases sharpen discrimination by making the defining attribute visible through variation; learners who compare multiple contrasting cases abstract more robust schemas than those who study examples alone [Multiple contrasting cases support abstraction of deep structure.](../claims/multiple-contrasting-cases-support-abstraction.md) [+S]. Non-examples are most valuable when they are *near misses* — instances sharing most attributes with the example but differing on the defining one — because far non-examples are trivially rejected and teach nothing about boundaries. Simultaneous presentation supports comparison; asking learners to explain *why* one instance qualifies and the other does not further strengthens conceptual understanding [Self-explanation improves conceptual understanding.](../claims/self-explanation-improves-conceptual-understanding.md) [+S].

### Context
#### Requirements
- Careful selection of examples and non-examples that differ on exactly one attribute (the defining one)
- Simultaneous or tightly sequenced presentation so both instances are in working memory together
- A discrimination task or [Self-Explanation](../elements/self-explanation.md) prompt that requires learners to articulate the critical difference
- A sufficient *variety* of examples and non-examples across contexts so learners do not bind the concept to surface features

#### Constraints
- Poorly chosen non-examples — differing on irrelevant attributes rather than the defining one — can teach the wrong boundary and actively mislead [-M]
- Presenting non-examples before learners have any grasp of the concept can create confusion, especially for novices with weak prior knowledge [~M]
- If all examples share a salient surface feature, learners overgeneralize that feature as defining; variety of surface features is essential [-S]
- Inefficient for skills or knowledge that is inherently procedural rather than conceptual; worked examples with fading are better suited [Example-problem sequences reduce cognitive load for novices.](../claims/example-problem-sequences-reduce-cognitive-load.md) [~M]

#### Implementation Variability
- **Classification tasks**: learners sort a mixed set of examples and non-examples, receiving feedback on errors
- **Erroneous examples**: a worked solution containing a conceptual error that learners must diagnose; erroneous examples build conceptual knowledge when learners explain the flaw [Erroneous examples build conceptual knowledge.](../claims/erroneous-examples-build-conceptual-knowledge.md) [+M]
- **Progressive discrimination**: begin with far non-examples and move to near misses as discrimination improves
- **[Cognitive Conflict](../elements/cognitive-conflict.md)**: deliberately present a non-example that learners initially classify as an example, then confront the mismatch

### Target Learners
- Novices forming a new concept, who otherwise overgeneralize from positive instances alone [+S]
- Learners confusing two closely related concepts (e.g., mass vs. weight, correlation vs. causation)
- Learners with some prior exposure benefit most; complete novices may need a [Demonstration](../elements/demonstration.md) of the concept first [~M]

### Target Learning Goals
- Concept formation and accurate classification
- Boundary knowledge: knowing what a concept is *not*, preventing overgeneralization
- Schema abstraction across varied surface features [Multiple contrasting cases support abstraction of deep structure.](../claims/multiple-contrasting-cases-support-abstraction.md) [+S]

### Instructions
1. Identify the defining attribute(s) of the concept and the common misconceptions or confusable concepts.
2. Select a clear example and a near-miss non-example differing on one defining attribute; vary surface features across pairs.
3. Present the pair simultaneously, using [Demonstration](../elements/demonstration.md) or side-by-side display so both are in working memory.
4. Prompt learners to state the critical difference ([Self-Explanation](../elements/self-explanation.md)), or use [Cognitive Conflict](../elements/cognitive-conflict.md) when a non-example is likely to be misclassified.
5. Follow with a classification task over a mixed set of new examples and non-examples, with feedback on errors.
6. Assess by asking learners to classify novel instances and justify the classification — not just recognize trained ones.

## Related Strategies
- [Comparing Cases](../elements/comparing-cases.md) — the broader strategy of structured comparison; matched example/non-example pairs are its minimal form
- [Worked Examples](worked-examples.md) — for procedural learning; pairs naturally with non-examples of common errors
- [Activating Prior Knowledge](activating-prior-knowledge.md) — surfacing the misconception first makes the non-example contrast meaningful

## Examples
- **Concept: "comics"** — pair a comic book page with a Roy Lichtenstein painting that uses comic-style imagery but is intended as fine art; the single differing attribute (sequential narrative) is isolated.
- **Statistics: correlation vs. causation** — pair a headline asserting causation from correlational data with a matched headline that includes the control or mechanism; learners identify the differing attribute.
- **Biology: mammal classification** — pair a dolphin with a shark to break the "lives in water = fish" overgeneralization, then a bat with a bird for the "flies = bird" boundary.
- **Mathematics: functions** — pair *y* = *x*² with the vertical-line-failing relation *x* = *y*²; learners explain why one is a function and the other is not.

## Key Sources
- Tennyson, R. D., & Park, O.-C. (1980). The teaching of concepts: A review of instructional design research literature. *Review of Educational Research, 50*(1), 55–70. [doi:10.3102/00346543050001055](https://doi.org/10.3102/00346543050001055)
- Gick, M. L., & Holyoak, K. J. (1983). Schema induction and analogical transfer. *Cognitive Psychology, 15*(1), 1–38. [doi:10.1016/0010-0285(83)90013-4](https://doi.org/10.1016/0010-0285(83)90013-4)
- Schwartz, D. L., & Bransford, J. D. (1998). A time for telling. *Cognition and Instruction, 16*(4), 475–522. [doi:10.1207/s1532690xci1604_4](https://doi.org/10.1207/s1532690xci1604_4)
- Merrill, M. D., & Tennyson, R. D. (1977). *Teaching concepts: An instructional design guide.* Educational Technology Publications.
- Marton, F., & Booth, S. (1997). *Learning and awareness.* Lawrence Erlbaum Associates.
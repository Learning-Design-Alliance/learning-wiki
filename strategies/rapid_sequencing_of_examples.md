---
type: strategy
title: Rapid Sequencing of Examples
description: Present instances of a concept in rapid sequence or allow all instances to be viewed simultaneously so they are co-active in working memory, supporting generalization.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Rapid Sequencing of Examples

## Description
Rapid sequencing of examples presents multiple instances of a concept in quick succession, or displays them simultaneously, so that learners can compare them while all are active in working memory. The temporal or spatial contiguity makes shared structural features salient and supports abstraction of the defining features of the concept. If examples are separated by long gaps or intervening content, learners tend to encode each instance in isolation and fail to generalize.

## Design Implications

Comparison across multiple instances is one of the most reliable routes to concept formation and schema abstraction; learners who study several contrasting cases together abstract more transferable schemas than those who study the same examples one at a time [Multiple contrasting cases support abstraction.](../claims/multiple-contrasting-cases-support-abstraction.md) [+S]. The mechanism is working-memory based: co-activating instances allows alignment of their structures, whereas sequential presentation with delay forces reliance on incomplete memory traces [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+M]. Sequencing works best when learners are prompted to explain *why* the instances belong to the same category, converting passive juxtaposition into active schema construction [Self-explanation improves conceptual understanding.](../claims/self-explanation-improves-conceptual-understanding.md) [+S].

### Context
#### Requirements
- A set of examples (typically 3–6) that vary surface features but share the target deep structure
- A presentation format — carousel, side-by-side grid, or rapid slideshow — that keeps prior examples visible or freshly retrievable
- Prompts that direct attention to commonalities and differences ([Comparing Cases](../elements/comparing-cases.md)), not just exposure
- A classification or application task in which learners classify new instances ([Practice](../elements/practice.md))

#### Constraints
- Too rapid a pace or too many simultaneous examples overwhelms working memory and produces shallow pattern-matching on surface features [-M]
- If examples are too similar, learners overgeneralize and include irrelevant features in the concept; if too dissimilar, alignment fails [-M]
- Novices may align examples on salient surface features rather than deep structure unless comparison prompts are provided [~M]
- Less effective for learners with high prior knowledge, who can abstract from single well-chosen examples and may find multiple redundant examples inefficient [~M]

#### Implementation Variability
- **Simultaneous display**: all examples visible in a grid; strongest for alignment but demands screen space and visual search
- **Rapid carousel**: examples shown seconds apart with minimal intervening content; preserves contiguity when space is limited
- **Interleaved with non-examples**: alternating positive and negative instances sharpens the concept boundary ([Non-Examples](../elements/non-examples.md))
- **Compare-then-solve**: rapid example sequence followed by an [Example-Problem Pair](../elements/example-problem-pairs.md) to consolidate the abstracted schema

### Target Learners
- Novices forming a new concept, especially an abstract one whose defining features are not visually obvious [Multiple contrasting cases support abstraction.](../claims/multiple-contrasting-cases-support-abstraction.md) [+S]
- Learners prone to encoding instances idiosyncratically; the juxtaposition forces structural comparison
- Less beneficial for advanced learners, who can generalize from fewer instances [~M]

### Target Learning Goals
- Concept formation and generalization: identifying defining features shared across instances
- Discrimination: distinguishing the target concept from near-miss categories
- Analogical transfer: mapping a learned structure onto new domains [Multiple contrasting cases support abstraction.](../claims/multiple-contrasting-cases-support-abstraction.md) [+M]

### Instructions
1. Select 3–6 examples that vary surface features but share the target deep structure; include at least one non-example if the concept has a confusable neighbor ([Non-Examples](../elements/non-examples.md))
2. Present the examples in rapid succession or side by side, with no intervening content ([Demonstration](../elements/demonstration.md))
3. Prompt learners to identify what the examples have in common and how they differ ([Comparing Cases](../elements/comparing-cases.md))
4. Ask learners to state or write the defining features — a self-explanation step that consolidates the abstraction [Self-explanation improves conceptual understanding.](../claims/self-explanation-improves-conceptual-understanding.md) [+S]
5. Follow immediately with classification of new, unseen instances to test and reinforce the generalized concept ([Practice](../elements/practice.md))

## Related Strategies
- [Comparing Cases](../elements/comparing-cases.md) — the comparison prompt that turns juxtaposition into abstraction
- [Non-Examples](../elements/non-examples.md) — negative instances define the concept boundary
- [Worked Examples](../principles/worked-examples.md) — rapid sequencing applied to solution procedures rather than concepts

## Examples
- **Art history**: presenting five Impressionist paintings in quick succession and asking students to identify shared brushwork and light treatment before classifying unseen works
- **[Schwartz & Bransford's contrasting cases](https://doi.org/10.1207/s1532690xci1604_1)**: students compare rapid sequences of data displays describing competing theories of learning before receiving the lecture, which improves subsequent learning from instruction
- **[Khan Academy](https://www.khanacademy.org)** concept intro videos show several worked instances of a problem type back-to-back before the first practice item

## Key Sources
- Tennyson, R. D., & Park, O.-C. (1980). The teaching of concepts: A review of instructional design research literature. *Review of Educational Research, 50*(1), 55–70. [doi:10.3102/00346543050001055](https://doi.org/10.3102/00346543050001055)
- Gick, M. L., & Holyoak, K. J. (1983). Schema induction and analogical transfer. *Cognitive Psychology, 15*(1), 1–38. [doi:10.1016/0010-0285(83)90002-6](https://doi.org/10.1016/0010-0285(83)90002-6)
- Schwartz, D. L., & Bransford, J. D. (1998). A time for telling. *Cognition and Instruction, 16*(4), 475–522. [doi:10.1207/s1532690xci1604_4](https://doi.org/10.1207/s1532690xci1604_4)
- Rittle-Johnson, B., & Star, J. R. (2007). Does comparing solution methods facilitate conceptual and procedural knowledge? An experimental study on learning to solve equations. *Journal of Educational Psychology, 99*(3), 561–574. [doi:10.1037/0022-0663.99.3.561](https://doi.org/10.1037/0022-0663.99.3.561)
---
type: strategy
title: Varying Irrelevant Attributes in Examples
description: When teaching concepts, use examples in which the irrelevant attributes vary widely.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Varying Irrelevant Attributes in Examples

> **Strategy** · [All strategies](index.md)

## Description
When teaching a concept, the examples presented should differ widely on attributes that are *irrelevant* to the concept while consistently displaying the attributes that define it. If all examples of "bird" are small, perching, brown animals, learners may encode size, habitat, or color as part of the concept; varying these across examples forces attention to the defining features. The strategy applies to any concept instruction: presenting a range of surface forms (media, context, difficulty, format, surface story) that share deep structure.

## Design Implications

Varied examples support schema formation by helping learners abstract the general rule rather than memorizing instance-specific features — a core recommendation of concept-learning research since Tennyson and Park's review of rational set theory [Tennyson & Park's analysis of concept-teaching research recommends wide variation of irrelevant attributes within the example set.](https://doi.org/10.3102/00346543050001055) [+S]. Variation also improves transfer: learners who study or practice with varied surface features perform better on novel problems than those trained on similar-looking items [Varied worked examples improved transfer of geometrical problem-solving compared to similar examples.](https://doi.org/10.1037/0022-0663.86.1.122) [+S]. The cost is higher intrinsic load during initial study, so variation should be introduced progressively rather than all at once.

### Context
#### Requirements
- A clear analysis of which attributes are *defining* (must stay constant) and which are *irrelevant* (should vary)
- A sufficient number of examples — typically at least 4–6 — to cover the range of irrelevant variation
- [Non-Examples](../elements/non-examples.md) paired with the varied examples, so learners can test hypotheses about which features matter
- Sequencing that starts with less variation for novices and widens as schemas form

#### Constraints
- High variation early in learning can overload novices, who lack schemas to distinguish relevant from irrelevant features — the effect reverses with expertise [Guidance that helps novices can hinder more knowledgeable learners.](../claims/expertise-reversal-effect.md) [~S]
- Variation increases study time and perceived difficulty; learners may judge varied sets as less effective even when they learn more (a desirable-difficulties mismatch)
- If irrelevant attributes vary but a defining attribute is accidentally absent in some examples, learners form misconceptions that are hard to correct
- For rote memorization or single-procedure skills, variation adds load without benefit

#### Implementation Variability
- **Within-set variation** (several examples presented together) vs. **across-time variation** (examples distributed over days); distributed variation adds spacing benefits
- **Learner-generated variation**: asking learners to produce their own examples of the concept, which requires them to apply the defining rule themselves
- **Interleaved variation**: mixing examples of related concepts so learners must also discriminate *between* concepts, not just recognize one
- In physical-skill domains the analog is variable practice (varying context and parameters of movement), which produces better retention and transfer than blocked practice [Contextual interference research shows random/varied practice schedules improve retention and transfer despite worse practice performance.](https://doi.org/10.1037/0022-0663.86.1.122) [+S]

### Target Learners
- Novices who have already grasped a first approximation of the concept and are ready to generalize beyond the initial example
- Learners preparing for transfer to novel contexts (new problem types, real-world settings)
- Not appropriate as the *first* exposure for complete novices; begin with a clear, low-variation example, then widen [Guidance that helps novices can hinder more knowledgeable learners.](../claims/expertise-reversal-effect.md) [~M]

### Target Learning Goals
- Concept acquisition: identifying defining features of categories, principles, or procedures
- Transfer: applying a concept to problems whose surface features differ from training
- Discrimination learning: distinguishing concept instances from near-miss non-instances

### Instructions
1. Identify the defining attributes of the concept and list the irrelevant attributes learners might mistakenly encode (surface story, medium, color, context, difficulty).
2. Select or author an initial, prototypical example with minimal irrelevant variation — a [Worked Example](../elements/worked-examples.md) is a good vehicle for procedural concepts.
3. Add 4–6 further examples that keep defining attributes constant while maximizing spread across irrelevant attributes; pair each with a matched [Non-Example](../elements/non-examples.md).
4. Use [Comparing Cases](../elements/comparing-cases.md) to prompt learners to articulate what varies and what does not, rather than leaving the abstraction implicit.
5. Fade support by asking learners to classify new varied instances, then generate their own examples, following an [Example-Problem Sequence](../claims/example-problem-sequences-reduce-cognitive-load.md).

## Related Strategies
- [Use Worked Examples](use_worked_examples.md) — varied worked examples are the standard vehicle for this strategy in problem-solving domains
- [Non-Examples](../elements/non-examples.md) — near-miss non-examples do the complementary work of isolating defining attributes
- [Interleaving](interleaving.md) — mixing concept categories compounds the discrimination benefits of varied examples

## Examples
- **Tennyson & Park's rational set framework** — the classic instructional design prescription: an "example set" with wide irrelevant variation plus a "non-example set" matched on irrelevant attributes.
- **[Khan Academy](https://www.khanacademy.org)** — math concept videos deliberately use different numbers, contexts, and visual representations across examples of the same concept (e.g., fractions shown as pizzas, number lines, and bars).
- **Science curricula such as [ASAP Biology](https://www.hhmi.org/biointeractive)** (HHMI BioInteractive) — teach "natural selection" through varied cases (finches, peppered moths, antibiotic resistance) so learners abstract the mechanism from the surface story.
- **Motor-skills instruction** — variable practice schedules in sports coaching (practicing the same shot from varied positions and against varied feeds) reflect the same principle.

## Key Sources
- Tennyson, R. D., & Park, O.-C. (1980). The teaching of concepts: A review of instructional design research literature. *Review of Educational Research, 50*(1), 55–70. [doi:10.3102/00346543050001055](https://doi.org/10.3102/00346543050001055)
- Paas, F., & van Merriënboer, J. J. G. (1994). Variability of worked examples and transfer of geometrical problem-solving skills: A cognitive-load approach. *Journal of Educational Psychology, 86*(1), 122–133. [doi:10.1037/0022-0663.86.1.122](https://doi.org/10.1037/0022-0663.86.1.122)
- Shea, J. B., & Morgan, R. L. (1979). Contextual interference effects on the acquisition, retention, and transfer of a motor skill. *Journal of Experimental Psychology: Human Learning and Memory, 5*(3), 179–187.
- Merrill, M. D., & Tennyson, R. D. (1977). *Teaching concepts: An instructional design guide.* Educational Technology Publications.
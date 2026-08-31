---
type: element
title: Analogies and prior knowledge activation
description: Uses comparisons to familiar concepts to support understanding.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Analogies and prior knowledge activation

> **Element** · [All elements](index.md)

## Description
This element uses comparisons to familiar concepts to support understanding of new, often abstract material, and deliberately activates relevant prior knowledge before new content is introduced. The analogy supplies a source structure the learner already possesses; activation ensures that structure is actually retrieved and available for mapping onto the target concept.

## Design Implications

Analogies support comprehension by letting learners import a known relational structure instead of building a new one from scratch, reducing the working-memory burden of processing unfamiliar material [Analogical reasoning supports learning of abstract relational concepts.](../principles/analogical-reasoning.md) [+M]. The benefit depends on the quality of the mapping: surface similarity without structural alignment produces plausible-but-wrong inferences, so the shared relations should be made explicit rather than left for learners to infer. Activating prior knowledge before instruction improves integration of new information with existing schemas, but only when the activated knowledge is actually relevant — activating irrelevant or misconceived knowledge interferes with encoding [~M].

### Context
#### Requirements
- A source concept learners genuinely know well; the analogy must be checked against the audience, not the instructor
- Explicit mapping of the shared relational structure — which features correspond and, critically, which do not
- Pre-instructional prompts or questions that retrieve relevant prior knowledge ([Advance Organizers](advance-organizers.md), opening questions, quick-writes)
- Follow-up activity that requires learners to apply the mapped structure ([Application of Knowledge](application-of-knowledge.md))

#### Constraints
- Analogies break down at their boundaries; unmapped features invite overextension of the source's properties to the target [-M] — always state where the analogy fails
- Surface-similar but structurally mismatched analogies actively harm learning by encouraging wrong relational mappings [-M]
- Activating prior knowledge that contains misconceptions strengthens those misconceptions unless they are surfaced and confronted [~M]
- Learners with rich domain knowledge often find analogies redundant or distracting, preferring direct technical description [Guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M]

### Target Learners
- Novices in abstract or technical subjects (physics, economics, biology, computing) who lack a domain schema to organize new material [+M]
- Learners whose everyday experience contains a usable source structure (flowing water for circuits, pressure for markets)
- Less valuable for advanced learners, who benefit more from precise technical language than from familiar comparisons [~M]

### Target Learning Goals
- Conceptual comprehension: building an initial mental model of an abstract system
- Knowledge transfer: applying a relational structure learned in one domain to another
- Misconception diagnosis: using learners' activated intuitions as a starting point for restructuring

### Affordances
- [Analogical Reasoning](../principles/analogical-reasoning.md) — this element enacts the principle directly: the analogy is the vehicle for structure-mapping from a familiar source to an unfamiliar target
- [Constructivist Learning](../principles/constructivist-learning.md) — new knowledge is built by connecting to what learners already know rather than transmitted as isolated facts; activation makes those connections available for construction
- [Cognitive Load Reduction](../principles/cognitive-load-reduction.md) — a well-chosen analogy compresses a complex system into a familiar schema, freeing working memory for the genuinely new relations [Chunking familiar structure reduces working-memory load.](../claims/chunking-reduces-working-memory-load.md) [+M]
- [Cognitive Activation](../principles/cognitive-activation.md) — activation prompts require learners to retrieve and examine what they know, engaging deep processing before new content arrives

## Related Elements
- [Analogies](analogies.md) — the comparison mechanism itself, without the activation component
- [Activation](activation.md) — the retrieval component, usable without an analogy
- [Advance Organizers](advance-organizers.md) — a structured pre-instructional bridge from prior knowledge to new material
- [Metaphors](metaphors.md) — compressed, non-literal comparisons serving the same mapping function
- [Dual Coding](dual-coding.md) — a complementary route: pairing verbal analogy with a visual model

## Patterns That Use This Element
- [Elaboration Theory](../patterns/elaboration-theory.md) — analogies serve as elaborative anchors that tie new content to existing knowledge structures
- [Cognitive Flexibility Theory](../patterns/cognitive-flexibility-theory.md) — multiple analogies across contexts build flexible, multi-perspective understanding of complex concepts
- [Cognitive Load Theory](../patterns/cognitive-load-theory.md) — familiar schemas imported via analogy reduce intrinsic load for novices

## Examples

**[Activating Prior Knowledge](../strategies/activating_prior_knowledge.md)** — Opening prompts or brainstorm questions that surface what learners already know before new content is presented; the analogy then builds on the retrieved structure.

**[PhET Interactive Simulations](https://phet.colorado.edu)** — Physics simulations pair abstract concepts (charge, energy) with visualizable analogues, combining analogy with [dual coding](dual-coding.md) through simultaneous visual and verbal representation.

**[Khan Academy](https://www.khanacademy.org)** — Explanations routinely open with everyday analogies (e.g., electrical potential as water pressure) before introducing formal notation.

**Case-based teaching in medicine** — Clinical teaching activates prior case knowledge ("this presents like the patient you saw last week") and uses the familiar case as an analogical source for the new one.

## Key Sources
- Gentner, D. (1983). Structure-mapping: A theoretical framework for analogy. *Cognitive Science, 7*(2), 155–170. [doi:10.1207/s15516709cog0702_3](https://doi.org/10.1207/s15516709cog0702_3)
- Richland, L. E., Zur, O., & Holyoak, K. J. (2007). Mathematics: Cognitive supports for analogical reasoning in the classroom. *Science, 316*(5828), 1128-1129. [doi:10.1126/science.1142103](https://doi.org/10.1126/science.1142103)
- Ausubel, D. P. (1968). *Educational psychology: A cognitive view*. Holt, Rinehart & Winston.
- Holyoak, K. J., & Thagard, P. (1995). *Mental leaps: Analogy in creative thought*. MIT Press.
- Mayer, R. E. (2009). *Multimedia learning* (2nd ed.). Cambridge University Press. [doi:10.1017/CBO9780511811678](https://doi.org/10.1017/CBO9780511811678)

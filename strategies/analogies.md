---
type: strategy
title: Analogies
description: Analogies compare an unfamiliar concept to something familiar, using the learner's prior knowledge as a bridge to understanding new material.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Analogies

> **Strategy** · [All strategies](index.md)

## Description
An analogies strategy introduces a new or abstract concept by explicitly comparing it to a familiar one, mapping the shared structure between the two ("an atom is like a solar system: the nucleus is the sun, the electrons are the planets"). The comparison functions as an [advance organizer](../elements/advance-organizers.md), giving learners a familiar schema into which new information can be integrated rather than memorized in isolation. Effective use goes beyond stating the comparison — it makes the mapping explicit, identifies where the analogy breaks down, and prompts learners to reason with it.

## Design Implications

Analogies work because they activate relevant prior knowledge and let learners reuse an existing mental model instead of building one from scratch, reducing the working-memory burden of interpreting unfamiliar material [Chunking reduces working-memory load.](../claims/chunking-reduces-working-memory-load.md) [+M]. Their benefit depends on structural alignment: learners gain most when the deep relations between source and target are mapped explicitly, not just surface features [Analogical comparison supports abstraction of shared structure.](../claims/multiple-contrasting-cases-support-abstraction.md) [+M]. Prompting learners to explain the mapping themselves strengthens the resulting understanding [Self-explanation improves conceptual understanding.](../claims/self-explanation-improves-conceptual-understanding.md) [+M].

### Context
#### Requirements
- Deep understanding of the target concept so the analogy can be mapped accurately
- A source concept that is genuinely familiar to the specific learners (audited, not assumed)
- Explicit mapping of corresponding features, plus identification of where the analogy fails
- A prompt for learners to articulate the relationship ([Self-Explanation](../elements/self-explanation.md) or discussion)

#### Constraints
- Analogies that share only surface features with the target produce confident misconceptions rather than understanding [~M] — e.g., the "solar system" atom analogy fosters the misconception that electrons follow fixed orbits
- Learners may overextend the analogy, importing features of the source that do not apply; unstated limits on the mapping are the primary source of analogy-induced error [-M]
- An analogy unfamiliar to part of the class adds load instead of reducing it, particularly for learners from different cultural or experiential backgrounds [-M]
- Overuse dilutes value: if everything is explained by analogy, learners may not build the target schema itself [~W]

#### Implementation Variability
- **Teacher-provided analogy**: instructor supplies and maps the comparison; fastest, but risks passive reception
- **Learner-generated analogy**: students invent their own comparison; harder, but produces deeper processing and reveals misconceptions for diagnosis [~M]
- **Multiple analogies**: presenting two or more different comparisons for the same concept limits overreliance on any single mapping and supports more complete understanding [~M]
- **Extended (analogical) instruction**: the analogy is developed over time alongside the target, as in Glynn's Teaching-With-Analogies model

### Target Learners
- Novices encountering an abstract or invisible concept (electricity, cells, markets, recursion) for the first time [+M]
- Learners with relevant prior knowledge in the source domain — the strategy depends on it; without a familiar source, the analogy teaches nothing [~M]
- Younger learners and low-prior-knowledge students benefit most from concrete, familiar sources; experts typically find analogies redundant [~M]

### Target Learning Goals
- Conceptual understanding of abstract, complex, or invisible phenomena
- Schema formation: anchoring new material to existing knowledge structures
- Transfer preparation: learners who understand a concept through its relational structure are better positioned to apply it in new contexts [~M]

### Instructions
1. Audit what learners already know and select a source concept that is familiar to *them* — [Recall prior knowledge](../elements/recall-prior-knowledge.md) before choosing the comparison
2. Present the target concept briefly, then introduce the analogy as an organizing frame ([Advance Organizers](../elements/advance-organizers.md))
3. Map the correspondence explicitly, feature by feature, during [Direct instruction](../elements/direct-instruction.md) — do not leave learners to infer the mapping
4. State the analogy's limits: name the features that do *not* transfer to prevent overextension
5. [Provide guidance](../elements/provide-guidance.md) as learners apply the analogy to a new case or problem, and ask them to explain the mapping in their own words
6. Fade the analogy once the target schema is established, so learners reason from the concept itself rather than the comparison

## Related Strategies
- [Advance Organizers](../strategies/advance_organizers.md) — analogies are one of the most powerful organizer types
- [Activating Prior Knowledge](../strategies/activating_prior_knowledge.md) — the mechanism analogies exploit
- [Multiple Representations](../strategies/multiple_representations.md) — an analogy is one representation among several that should ultimately be coordinated

## Related Elements
- [Analogies and Prior Knowledge Activation](../elements/analogies-and-prior-knowledge-activation.md) — the element form of this strategy
- [Activation](../elements/activation.md) — analogies depend on relevant prior knowledge being retrieved
- [Advance Organizers](../elements/advance-organizers.md) — the structural role an analogy plays at the start of instruction

## Patterns That Use This Strategy
- [Elaboration Theory](../patterns/elaboration-theory.md) — analogies are a designated elaboration device for anchoring new content
- [Direct Instruction](../patterns/direct-instruction.md) — analogies serve the "present the content" step for abstract material

## Examples
- **PhET Interactive Simulations** (https://phet.colorado.edu) — physics and chemistry simulations pair abstract models with everyday framings (e.g., resistance as friction) so learners connect formal concepts to familiar experience
- **CS Unplugged** (https://www.csunplugged.edu) — teaches computer science concepts (sorting networks, error detection) through physical analogies like playing cards and running races, before formal notation
- **Biology instruction**: teaching membrane transport with a crowded nightclub with a bouncer (selective permeability) — effective only when the instructor explicitly notes that membranes involve concentration gradients, which nightclubs do not

## Key Sources
- Ausubel, D. P. (1960). The use of advance organizers in the learning and retention of meaningful verbal material. *Journal of Educational Psychology, 51*(5), 267–272. [doi:10.1037/h0046669](https://doi.org/10.1037/h0046669)
- Glynn, S. M., & Takahashi, T. (1998). Learning from analogy-enhanced science text. *Journal of Research in Science Teaching, 35*(10), 1129–1149. [doi:10.1002/(SICI)1098-2736(199812)35:10<1129::AID-TEA5>3.0.CO;2-2](https://doi.org/10.1002/(SICI)1098-2736(199812)35:10<1129::AID-TEA5>3.0.CO;2-2)
- Donnelly, C. M., & McDaniel, M. A. (1993). Use of analogies in learning unknown scientific concepts. *Journal of Experimental Psychology: Learning, Memory, and Cognition, 19*(5), 1133–1145. [doi:10.1037/0278-7393.19.4.975](https://doi.org/10.1037/0278-7393.19.4.975)
- Duit, R. (1991). On the role of analogies and metaphors in learning science. *Science Education, 75*(6), 649–672. [doi:10.1002/sce.3730750606](https://doi.org/10.1002/sce.3730750606)
- Harrison, A. G., & Coll, R. K. (2008). *Using analogies in middle and secondary science classrooms*. Corwin Press.

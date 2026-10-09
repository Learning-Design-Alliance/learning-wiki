---
type: strategy
id: use-analogies
aliases: [use_analogies]
title: Use Analogies
description: Introduce new concepts by mapping them onto familiar, well-structured knowledge domains so learners can reason from the known to the unknown.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Use Analogies

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (2 for, 1 against) · 7 studies (4 causal, 3 quant-synthesis), `q3`–`q4` · 3 of 7 report an effect size

## Description
An analogy explains an unfamiliar target concept by relating it to a familiar source domain with a similar relational structure (e.g., the atom as a solar system, electrical current as water flow). The strategy works by activating prior knowledge and aligning its structure with the new material, so learners can infer relationships in the target domain from relationships they already understand [Analogical reasoning improves transfer of relational structure to new domains.](../claims/analogical-reasoning-improves-transfer.md) [+S].

## Design Implications

Analogies are effective because they transfer *relational structure*, not surface features — the instructional value comes from mapping how elements in the source correspond to elements in the target [Gentner's structure-mapping account of analogy.](../claims/analogical-reasoning-improves-transfer.md) [+S]. Effective use therefore requires making the mapping explicit: naming the correspondences, and just as importantly, naming where the analogy *breaks down*, since learners otherwise import inappropriate features from the source domain [~M]. Analogies also serve as advance organizers, giving learners a schema to hang new details on [Activation of prior knowledge improves learning of new material.](../claims/activation-improves-learning.md) [+M].

### Context
#### Requirements
- A source domain that is genuinely familiar to the target learners — familiarity is relative to the audience, not the instructor
- Deep structural similarity between source and target, not surface resemblance
- Explicit mapping of correspondences between source and target elements
- Explicit statement of the analogy's limits (where the mapping fails)
- A source domain that is genuinely familiar to the target learners (assess this; do not assume)
- Explicit mapping of relations, not just objects ("electrons flow *like* water flows" — the flow, pressure, and resistance map; the wetness does not)
- Clear statement of the analogy's boundaries — where it breaks down
- Follow-up engagement with the target concept on its own terms ([Application](../elements/application.md) or [Practice](../elements/practice.md))

#### Constraints
- Surface-similar but structurally mismatched analogies actively mislead learners, producing durable misconceptions (e.g., the solar-system atom implies electrons orbit in fixed planes) [~M]
- Analogies whose source is unfamiliar to learners add load rather than reduce it [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) [-M]
- Overextended analogies — pressed beyond their valid mapping — degrade accuracy; learners may retain the source's irrelevant features [-M]
- Less effective for arbitrary, non-relational content (vocabulary labels, symbol conventions) where there is no structure to map
- Surface-similar but structurally different analogies actively mislead, producing systematic misconceptions that persist after instruction [-M] — e.g., the "battery as reservoir" analogy encourages the misconception that current is used up in circuits
- Analogies unfamiliar to part of the class add load rather than reduce it; a source domain learners don't know is worse than no analogy [~M]
- Over-reliance can anchor learners to source-domain reasoning when target-domain reasoning is required; pairing with [Non-Examples](../elements/non-examples.md) or [Comparing Cases](../elements/comparing-cases.md) helps learners discriminate the target from the source

#### Implementation Variability
- **Advance analogy**: presented before instruction to frame the topic ([Advance Organizers](../elements/advance-organizers.md))
- **Embedded analogy**: interleaved during explanation at the point of difficulty
- **Learner-generated analogies**: students produce their own comparisons, which deepens processing but requires verification against misconceptions [~M]
- **Multiple analogies**: several sources for one target, which dilutes the idiosyncratic flaws of any single analogy and supports flexible understanding [~M]
- **Analogical scaffolds** — revisited and progressively faded as the target concept becomes familiar ([Analogies and Prior Knowledge Activation](../elements/analogies-and-prior-knowledge-activation.md))
- **Learner-generated analogies** — students produce their own comparisons, which deepens processing but requires more guidance and works best after instructor modeling
- **Multiple analogies** — several different source domains for the same concept, supporting flexible understanding ([Cognitive Flexibility](../principles/cognitive-flexibility.md))

### Target Learners
- Novices, who lack domain schemas and benefit most from importing structure from a familiar domain [Analogical reasoning improves transfer.](../claims/analogical-reasoning-improves-transfer.md) [+M]
- Younger learners and learners outside the domain, for whom abstract definitions alone are inert
- Less beneficial for experts, who already possess domain-internal structure and may find the analogy redundant or distorting [~W]
- Learners with rich everyday knowledge relevant to the source domain; ineffective when the analogy's source is as unfamiliar as the target [~M]
- Younger learners and those with limited domain vocabulary, for whom concrete source domains reduce language demands

### Target Learning Goals
- Conceptual understanding of abstract or invisible systems (molecular, economic, computational)
- Transfer of relational structure across domains [Analogical reasoning improves transfer of relational structure.](../claims/analogical-reasoning-improves-transfer.md) [+S]
- Prior knowledge activation and schema formation [Activation improves learning.](../claims/activation-improves-learning.md) [+M]
- Conceptual understanding of abstract, invisible, or counterintuitive phenomena (electricity, cells, markets, recursion)
- Schema formation: anchoring new concepts to existing knowledge structures

### Instructions
1. Identify the relational core of the target concept — what structure must learners grasp.
2. Select a source domain your learners know well and verify its structural match; discard surface-similar but structurally poor candidates.
3. Present the analogy before or at the point of difficulty, connecting it to activated prior knowledge ([Analogies and Prior Knowledge Activation](../elements/analogies-and-prior-knowledge-activation.md)).
4. Make the mapping explicit, element by element ([Analogies](../elements/analogies.md)).
5. State the analogy's boundaries — where the source fails — and contrast with the correct target behavior.
6. Follow with application in the target domain itself ([Application of Knowledge](../elements/application-of-knowledge.md)) so learners practice in the real structure, not the source.

## Related Strategies
- [Activating Prior Knowledge](activating-prior-knowledge.md) — analogies are a structured form of activation; both depend on what learners already hold
- [Use Concrete Examples](use_concrete_examples.md) — examples instantiate the target directly; analogies import structure from outside it
- [Use Multiple Representations](use_multiple_representations.md) — an analogy is one representation among several; combining them offsets any single analogy's distortions

## Examples
- **Electricity as water flow** — a staple of physics instruction: voltage as pressure, current as flow rate, resistance as pipe narrowing; effective only when instructors explicitly reject the "water is used up" implication.
- **[PhET Interactive Simulations](https://phet.colorado.edu)** — simulations often pair abstract models with everyday analogues (e.g., gas particles as balls in a box), letting learners test where the mapping holds.
- **Computer memory as a desk vs. filing cabinet** — instructors commonly contrast two analogies to teach the RAM/storage distinction, using the mismatch itself to sharpen understanding.
- **Water-flow analogy for electric circuits** — widely used in physics teaching (e.g., PhET Interactive Simulations' circuit construction activities, https://phet.colorado.edu); effective when voltage/pressure and resistance/constriction are mapped, misleading if current "drains" is left uncorrected
- **The "lock and key" model of enzyme action** — biology's canonical analogy, later refined to "induced fit" precisely because the original mapping broke down
- **Analogies in CS education** — variables as labeled boxes, recursion as Russian nesting dolls; research shows these help initial understanding but require explicit unwinding of where the mapping fails

## Key Sources
- Gentner, D. (1983). Structure-mapping: A theoretical framework for analogy. *Cognitive Science, 7*(2), 155–170. [doi:10.1207/s15516709cog0702_3](https://doi.org/10.1207/s15516709cog0702_3)
- Duit, R. (1991). On the role of analogies and metaphors in learning science. *Science Education, 75*(6), 649–672. [doi:10.1002/sce.3730750606](https://doi.org/10.1002/sce.3730750606)
- Donnelly, C. M., & McDaniel, M. A. (1993). Use of analogy in learning scientific concepts. *Journal of Experimental Psychology: Learning, Memory, and Cognition, 19*(4), 975-987. [doi:10.1037/0278-7393.19.4.975](https://doi.org/10.1037/0278-7393.19.4.975)
- Aubusson, P. J., Harrison, A. G., & Ritchie, S. M. (Eds.). (2006). *Metaphor and analogy in science education*. Springer. [doi:10.1007/1-4020-3830-5](https://doi.org/10.1007/1-4020-3830-5)
- Glynn, S. M. (1991). Explaining science concepts: A teaching-with-analogies model. In S. M. Glynn, R. H. Yeany, & B. K. Britton (Eds.), *The psychology of learning science* (pp. 219–239). Erlbaum.
- Donnelly, J. F., & McDaniel, M. A. (1993). Analogy with generic knowledge: Use of analogies in learning. *Journal of Educational Psychology, 85*(2), 333–343.

<!-- merged 2026-10-09 from strategies/use_analogies ("Use Analogies"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Use Analogies

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (2 for, 1 against) · 7 studies (4 causal, 3 quant-synthesis), `q3`–`q4` · 3 of 7 report an effect size

## Description
An analogy explains a new or abstract concept by relating it to something learners already know, making the structural correspondence explicit ("the heart is like a pump; the valves are like one-way doors"). The strategy is carried out by (a) activating the familiar source domain, (b) mapping its relations onto the target concept, and (c) marking where the mapping breaks down. Analogies function as a bridge between prior knowledge and new content, converting an unfamiliar situation into a familiar one with known gaps.

## Design Implications

Analogies improve comprehension and transfer when the source and target share deep structural features, not just surface similarity [Analogical reasoning improves transfer when mappings are structural rather than surface-level.](../claims/analogical-reasoning-improves-transfer.md) [+M]. They work by retrieving relevant prior knowledge and using it as a scaffold, consistent with evidence that activation of relevant background knowledge improves learning [Activation of prior knowledge improves learning.](../claims/activation-improves-learning.md) [+M]. Because learners may overextend a mapping, effective analogies explicitly state their limits — where the analogy holds and where it fails.

### Context
#### Requirements
- A source domain that is genuinely familiar to the target learners (assess this; do not assume)
- Explicit mapping of relations, not just objects ("electrons flow *like* water flows" — the flow, pressure, and resistance map; the wetness does not)
- Clear statement of the analogy's boundaries — where it breaks down
- Follow-up engagement with the target concept on its own terms ([Application](../elements/application.md) or [Practice](../elements/practice.md))

#### Constraints
- Surface-similar but structurally different analogies actively mislead, producing systematic misconceptions that persist after instruction [-M] — e.g., the "battery as reservoir" analogy encourages the misconception that current is used up in circuits
- Analogies unfamiliar to part of the class add load rather than reduce it; a source domain learners don't know is worse than no analogy [~M]
- Over-reliance can anchor learners to source-domain reasoning when target-domain reasoning is required; pairing with [Non-Examples](../elements/non-examples.md) or [Comparing Cases](../elements/comparing-cases.md) helps learners discriminate the target from the source
- For novices, a poorly chosen analogy consumes working memory on dual mappings rather than saving it [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) [-M]

#### Implementation Variability
- **Advance-organizer analogies** — presented before instruction to frame incoming material ([Advance Organizers](../elements/advance-organizers.md))
- **Analogical scaffolds** — revisited and progressively faded as the target concept becomes familiar ([Analogies and Prior Knowledge Activation](../elements/analogies-and-prior-knowledge-activation.md))
- **Learner-generated analogies** — students produce their own comparisons, which deepens processing but requires more guidance and works best after instructor modeling
- **Multiple analogies** — several different source domains for the same concept, supporting flexible understanding ([Cognitive Flexibility](../principles/cognitive-flexibility.md))

### Target Learners
- Novices who lack domain-specific schemas and need an accessible entry point [Analogical reasoning improves transfer when mappings are structural.](../claims/analogical-reasoning-improves-transfer.md) [+M]
- Learners with rich everyday knowledge relevant to the source domain; ineffective when the analogy's source is as unfamiliar as the target [~M]
- Younger learners and those with limited domain vocabulary, for whom concrete source domains reduce language demands

### Target Learning Goals
- Conceptual understanding of abstract, invisible, or counterintuitive phenomena (electricity, cells, markets, recursion)
- Transfer: applying a known relational structure to a new domain [Analogical reasoning improves transfer.](../claims/analogical-reasoning-improves-transfer.md) [+M]
- Schema formation: anchoring new concepts to existing knowledge structures

### Instructions
1. Identify the core relational structure of the target concept — what must the analogy preserve?
2. Select a source domain your learners demonstrably know; verify with a quick check ([Activation](../elements/activation.md))
3. Present the analogy and map each relevant relation explicitly, one at a time
4. State the analogy's limits: name at least one feature that does *not* map
5. Have learners apply the target concept in its own terms ([Application of Knowledge](../elements/application-of-knowledge.md)), then optionally generate or critique analogies themselves

## Related Strategies
- [Activate Background Knowledge](../strategies/activating-prior-knowledge.md) — analogies are a specific, high-leverage method of doing this
- [Use Concrete Examples](../strategies/use_concrete_examples.md) — examples instantiate the target directly; analogies import structure from elsewhere

## Examples
- **Water-flow analogy for electric circuits** — widely used in physics teaching (e.g., PhET Interactive Simulations' circuit construction activities, https://phet.colorado.edu); effective when voltage/pressure and resistance/constriction are mapped, misleading if current "drains" is left uncorrected
- **The "lock and key" model of enzyme action** — biology's canonical analogy, later refined to "induced fit" precisely because the original mapping broke down
- **Analogies in CS education** — variables as labeled boxes, recursion as Russian nesting dolls; research shows these help initial understanding but require explicit unwinding of where the mapping fails

## Key Sources
- Gentner, D. (1983). Structure-mapping: A theoretical framework for analogy. *Cognitive Science, 7*(2), 155–170. [doi:10.1207/s15516709cog0702_3](https://doi.org/10.1207/s15516709cog0702_3)
- Glynn, S. M. (1991). Explaining science concepts: A teaching-with-analogies model. In S. M. Glynn, R. H. Yeany, & B. K. Britton (Eds.), *The psychology of learning science* (pp. 219–239). Erlbaum.
- Donnelly, J. F., & McDaniel, M. A. (1993). Analogy with generic knowledge: Use of analogies in learning. *Journal of Educational Psychology, 85*(2), 333–343.
- Aubusson, P. J., Harrison, A. G., & Ritchie, S. M. (Eds.). (2006). *Metaphor and analogy in science education*. Springer. [doi:10.1007/1-4020-3830-5](https://doi.org/10.1007/1-4020-3830-5)
-->
